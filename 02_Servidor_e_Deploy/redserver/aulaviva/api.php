<?php
// ============================================================
// AulaViva API — redserver (referência documentada)
// Rotas (query string):
//   ?disc=pi1|lp2&a=get              -> progresso do aluno (cookie httpOnly identifica)
//   ?disc=...&a=put   (POST JSON)    -> salva progresso {nome, turma, payload}
//   ?disc=...&a=lista&token=PROF     -> turma inteira (Painel do Professor)
//   ?disc=...&a=arq                  -> lista materiais da turma (leitura pública)
//   ?disc=...&a=arqup (POST JSON)    -> upload de material {token, nome, base64}
// Segurança: erros NUNCA vazam pro browser (error_log); token de professor
// obrigatório em lista/arqup; nome de arquivo sanitizado; limite de tamanho.
// SENHAS: defina por ambiente (LOJA_DB_PASS / AULAVIVA_PROF_TOKEN) no php-fpm
// ou num arquivo fora do webroot. Os valores abaixo são SOMENTE fallback de dev.
// ============================================================
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

$DISC = $_GET['disc'] ?? '';
$A    = $_GET['a']    ?? '';
if (!in_array($DISC, ['pi1', 'lp2'], true)) {
    http_response_code(400); echo json_encode(['erro' => 'disc']); exit;
}

$DB_PASS    = getenv('LOJA_DB_PASS')     ?: 'COLOQUE_AQUI_A_SENHA_DO_loja_app';
$PROF_TOKEN = getenv('AULAVIVA_PROF_TOKEN') ?: 'COLOQUE_AQUI_O_TOKEN_DO_PROFESSOR';
$BASE_DIR   = dirname(__DIR__);                 // /…/Kit_Sala_de_Aula
$MAT_DIR    = __DIR__ . '/materiais/' . $DISC;   // uploads de materiais
$COOKIE     = 'aulaviva_' . $DISC;
$MAX_UP     = 15 * 1024 * 1024;                  // 15 MB

function falha(string $msg, int $code = 500): void {
    error_log('[aulaviva-api] ' . $msg);
    http_response_code($code);
    echo json_encode(['erro' => 'indisponível']);  // mensagem genérica pro browser
    exit;
}

// ---------- MySQL ----------
try {
    $db = new PDO(
        'mysql:host=127.0.0.1;dbname=loja_turma;charset=utf8mb4',
        'loja_app', $DB_PASS,
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
    );
} catch (Throwable $e) { falha('db: ' . $e->getMessage()); }

// ---------- cookie httpOnly = identidade do aluno ----------
function codigo_aluno(string $cookie): string {
    $code = $_COOKIE[$cookie] ?? '';
    if ($code === '' || !preg_match('/^[a-f0-9]{16}$/', $code)) {
        $code = bin2hex(random_bytes(8));
        $sec  = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off');
        setcookie($cookie, $code, [
            'expires'  => time() + 180 * 86400,
            'path'     => '/Kit_Sala_de_Aula/',
            'httponly' => true,
            'samesite' => 'Lax',
            'secure'   => $sec,
        ]);
        $_COOKIE[$cookie] = $code;
    }
    return $code;
}

function corpo_json(): array {
    $raw = file_get_contents('php://input');
    $j = json_decode($raw ?: '[]', true);
    return is_array($j) ? $j : [];
}

// ---------- rotas ----------
switch ($A) {
    case 'get': {
        $code = codigo_aluno($COOKIE);
        $st = $db->prepare('SELECT nome, turma, payload, updated_at FROM aulaviva_alunos
                            WHERE disc = ? AND code = ? LIMIT 1');
        $st->execute([$DISC, $code]);
        $row = $st->fetch(PDO::FETCH_ASSOC);
        echo json_encode($row ? [
            'nome'  => $row['nome'],
            'turma' => $row['turma'],
            'payload' => json_decode($row['payload'] ?: '{}', true),
            'updated_at' => $row['updated_at'],
        ] : new stdClass());
        break;
    }
    case 'put': {
        $code = codigo_aluno($COOKIE);
        $b = corpo_json();
        $payload = json_encode($b['payload'] ?? [], JSON_UNESCAPED_UNICODE);
        $st = $db->prepare('INSERT INTO aulaviva_alunos (disc, code, nome, turma, payload, updated_at)
                            VALUES (?, ?, ?, ?, ?, NOW())
                            ON DUPLICATE KEY UPDATE nome=VALUES(nome), turma=VALUES(turma),
                            payload=VALUES(payload), updated_at=NOW()');
        $ok = $st->execute([$DISC, $code, (string)($b['nome'] ?? ''), (string)($b['turma'] ?? ''), $payload]);
        echo json_encode(['ok' => (bool)$ok]);
        break;
    }
    case 'lista': {
        if (($_GET['token'] ?? '') !== $PROF_TOKEN || $PROF_TOKEN === 'COLOQUE_AQUI_O_TOKEN_DO_PROFESSOR') {
            http_response_code(403); echo json_encode(['erro' => 'token']); exit;
        }
        $st = $db->prepare('SELECT nome, turma, payload, updated_at FROM aulaviva_alunos
                            WHERE disc = ? ORDER BY updated_at DESC');
        $st->execute([$DISC]);
        $rows = $st->fetchAll(PDO::FETCH_ASSOC);
        foreach ($rows as &$r) { $r['payload'] = json_decode($r['payload'] ?: '{}', true); }
        echo json_encode($rows);
        break;
    }
    case 'arq': {
        if (!is_dir($MAT_DIR)) { echo json_encode([]); break; }
        $out = [];
        foreach (scandir($MAT_DIR) ?: [] as $f) {
            if ($f === '.' || $f === '..') continue;
            $p = $MAT_DIR . '/' . $f;
            if (!is_file($p)) continue;
            $out[] = [
                'nome' => $f,
                'tamanho' => filesize($p),
                'atualizado' => date('c', filemtime($p)),
                'url' => 'aulaviva/materiais/' . $DISC . '/' . rawurlencode($f),
            ];
        }
        usort($out, fn($x, $y) => strcmp($y['atualizado'], $x['atualizado']));
        echo json_encode($out);
        break;
    }
    case 'arqup': {
        if (($_POST['token'] ?? corpo_json()['token'] ?? '') !== $PROF_TOKEN) {
            http_response_code(403); echo json_encode(['erro' => 'token']); exit;
        }
        $b = corpo_json();
        $nome = basename((string)($b['nome'] ?? ''));
        $nome = preg_replace('/[^\w.\-() ]+/u', '_', $nome);
        $b64  = (string)($b['base64'] ?? '');
        $bin  = base64_decode($b64, true);
        if ($nome === '' || $bin === false || strlen($bin) > $MAX_UP) falha('upload inválido', 400);
        if (!is_dir($MAT_DIR)) mkdir($MAT_DIR, 0775, true);
        $dest = $MAT_DIR . '/' . time() . '-' . $nome;
        if (file_put_contents($dest, $bin) === false) falha('gravação');
        echo json_encode(['ok' => true, 'url' => 'aulaviva/materiais/' . $DISC . '/' . rawurlencode(basename($dest))]);
        break;
    }
    default:
        http_response_code(400); echo json_encode(['erro' => 'rota']);
}
