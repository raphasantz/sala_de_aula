<?php
/* ============================================================
   AulaViva · API v2 (redserver) — raquel.redserver.top
   Rotas (?disc=pi1|lp2&a=...):
     GET  get                     progresso pela sessão (cookie) → {nome,turma,payload} | {ok:false}
     POST put   {nome?,turma?,payload}   salva progresso
     POST reg   {nome,turma,senha}       cria conta (nome único p/ disciplina) → cookie
     POST login {nome,senha}             confere senha → cookie + {nome,turma,payload}
     POST logout                         apaga cookie
     GET  check&nome=                    {existe:bool} (nome já cadastrado?)
     GET  lista&token=PROF_TOKEN         lista p/ painel (com hist e entregas)
     GET  arq                            materiais da turma
     POST arqup {token,nome,base64,tipo} professor envia material
     POST entrega {nome,base64,tipo}     aluno anexa txt/doc/pdf
     GET  minhas                         entregas do aluno da sessão
     GET  entregas&token=PROF_TOKEN      todas as entregas (painel)
   Segurança: senha com password_hash; erros de BD → error_log;
   mensagem genérica ao navegador; CORS liberado p/ uso em sala.
   ============================================================ */
declare(strict_types=1);
define('DIR', '/home/raquel/apps-nuvem');
define('DB_NAME', 'loja_aulaviva');
define('DB_USER', 'loja_app');
define('DB_PASS', 'TROQUE_ESTA_SENHA_2026');
define('PROF_TOKEN', 'TROQUE_ESTE_TOKEN_2026');
define('MAX_ARQ', 15 * 1024 * 1024);

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Content-Type');
header('Access-Control-Allow-Methods: GET,POST,OPTIONS');
header('Content-Type: application/json; charset=utf-8');
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') exit;

function db(): PDO {
  static $pdo = null;
  if ($pdo === null) {
    $pdo = new PDO('mysql:host=127.0.0.1;dbname=' . DB_NAME . ';charset=utf8mb4',
      DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
      ]);
  }
  return $pdo;
}
function norm(string $s): string {
  $s = mb_strtolower(trim($s), 'UTF-8');
  $s = strtr($s, ['à'=>'a','á'=>'a','â'=>'a','ã'=>'a','ä'=>'a','é'=>'e','ê'=>'e','í'=>'i','ó'=>'o','ô'=>'o','õ'=>'o','ú'=>'u','ü'=>'u','ç'=>'c']);
  return preg_replace('/\s+/', ' ', $s);
}
function fail(string $msg, string $code = 'erro', int $st = 400): void {
  http_response_code($st);
  echo json_encode(['ok' => false, 'erro' => $code, 'msg' => $msg]);
  exit;
}
function corpo(): array {
  $raw = file_get_contents('php://input');
  $d = json_decode($raw ?: '{}', true);
  return is_array($d) ? $d : [];
}
function cookieCode(string $disc): string {
  return $_COOKIE['aulaviva_' . $disc] ?? '';
}
function setCookieCode(string $disc, string $code): void {
  setcookie('aulaviva_' . $disc, $code, [
    'expires' => time() + 60*60*24*120,
    'path' => '/',
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Lax',
  ]);
}
function novoCode(): string {
  $b = random_bytes(8); $s = '';
  foreach (str_split(bin2hex($b), 2) as $h) $s .= chr(65 + (hexdec($h) % 26));
  return substr($s, 0, 12);
}

$disc = preg_match('/^(pi1|lp2)$/', $_GET['disc'] ?? '') ? $_GET['disc'] : fail('disc inválida');
$a    = $_GET['a'] ?? 'get';
$code = cookieCode($disc);

try {
  switch ($a) {

    /* ---------- sessão / contas ---------- */
    case 'get': {
      if (!$code) { echo json_encode(['ok' => true, 'nome' => null]); exit; }
      $st = db()->prepare('SELECT c.nome, c.turma, p.payload FROM aulaviva_contas c
        LEFT JOIN aulaviva_progresso p ON p.disc=c.disc AND p.code=c.code
        WHERE c.disc=? AND c.code=?');
      $st->execute([$disc, $code]);
      $r = $st->fetch();
      if (!$r) { echo json_encode(['ok' => true, 'nome' => null]); exit; }
      echo json_encode(['ok' => true, 'nome' => $r['nome'], 'turma' => $r['turma'],
        'payload' => $r['payload'] ? json_decode($r['payload'], true) : null]);
      exit;
    }
    case 'put': {
      if (!$code) fail('sem sessão — faça login', 'sem_sessao', 401);
      $d = corpo();
      $pl = json_encode($d['payload'] ?? [], JSON_UNESCAPED_UNICODE);
      if (strlen($pl) > 4*1024*1024) fail('progresso grande demais');
      $st = db()->prepare('INSERT INTO aulaviva_progresso (disc,code,nome,turma,payload)
        VALUES (?,?,?,?,?) ON DUPLICATE KEY UPDATE
        nome=IF(VALUES(nome)="",nome,VALUES(nome)),
        turma=IF(VALUES(turma)="",turma,VALUES(turma)),
        payload=VALUES(payload)');
      $st->execute([$disc, $code, $d['nome'] ?? '', $d['turma'] ?? '', $pl]);
      echo json_encode(['ok' => true, 'code' => $code]);
      exit;
    }
    case 'reg': {
      $d = corpo();
      $nome = trim($d['nome'] ?? '');
      $senha = $d['senha'] ?? '';
      if (mb_strlen($nome) < 3) fail('nome muito curto', 'nome');
      if (mb_strlen($senha) < 4) fail('senha muito curta', 'senha');
      $nl = norm($nome);
      $st = db()->prepare('SELECT code FROM aulaviva_contas WHERE disc=? AND nome_lc=?');
      $st->execute([$disc, $nl]);
      if ($st->fetch()) fail('nome já cadastrado', 'nome', 409);
      $code = novoCode();
      $st = db()->prepare('INSERT INTO aulaviva_contas (disc,code,nome,nome_lc,turma,senha_hash)
        VALUES (?,?,?,?,?,?)');
      $st->execute([$disc, $code, $nome, $nl, trim($d['turma'] ?? ''), password_hash($senha, PASSWORD_DEFAULT)]);
      setCookieCode($disc, $code);
      echo json_encode(['ok' => true, 'nome' => $nome, 'payload' => null]);
      exit;
    }
    case 'login': {
      $d = corpo();
      $nl = norm($d['nome'] ?? '');
      $st = db()->prepare('SELECT code,nome,turma,senha_hash FROM aulaviva_contas WHERE disc=? AND nome_lc=?');
      $st->execute([$disc, $nl]);
      $c = $st->fetch();
      if (!$c || !password_verify($d['senha'] ?? '', $c['senha_hash']))
        fail('credenciais inválidas', 'cred', 401);
      setCookieCode($disc, $c['code']);
      $st = db()->prepare('SELECT payload FROM aulaviva_progresso WHERE disc=? AND code=?');
      $st->execute([$disc, $c['code']]);
      $p = $st->fetch();
      echo json_encode(['ok' => true, 'nome' => $c['nome'], 'turma' => $c['turma'],
        'payload' => $p && $p['payload'] ? json_decode($p['payload'], true) : null]);
      exit;
    }
    case 'logout': {
      setcookie('aulaviva_' . $disc, '', ['expires' => time()-3600, 'path' => '/']);
      echo json_encode(['ok' => true]);
      exit;
    }
    case 'check': {
      $st = db()->prepare('SELECT 1 FROM aulaviva_contas WHERE disc=? AND nome_lc=?');
      $st->execute([$disc, norm($_GET['nome'] ?? '')]);
      echo json_encode(['ok' => true, 'existe' => (bool)$st->fetch()]);
      exit;
    }

    /* ---------- painel do professor ---------- */
    case 'lista': {
      if (($_GET['token'] ?? '') !== PROF_TOKEN) fail('token inválido', 'token', 403);
      $st = db()->prepare('SELECT c.nome, c.turma, p.payload, p.updated_at
        FROM aulaviva_contas c
        LEFT JOIN aulaviva_progresso p ON p.disc=c.disc AND p.code=c.code
        WHERE c.disc=? ORDER BY c.nome');
      $st->execute([$disc]);
      $lin = [];
      foreach ($st->fetchAll() as $r) {
        $p = $r['payload'] ? json_decode($r['payload'], true) : [];
        $lin[] = ['nome' => $r['nome'], 'turma' => $r['turma'],
          'pts' => $p['pts'] ?? 0,
          'aulas' => array_sum(array_map('count', array_values($p['aulas'] ?? []))),
          'exercicios' => array_sum(array_map('count', array_values($p['exok'] ?? []))),
          'chefes' => count($p['boss'] ?? []), 'pos' => $p['pos'] ?? null,
          'hist' => $p['hist'] ?? [], 'atualizado' => $r['updated_at']];
      }
      echo json_encode($lin);
      exit;
    }

    /* ---------- materiais (professor → turma) ---------- */
    case 'arq': {
      $st = db()->prepare('SELECT nome,tipo,tamanho,updated_at FROM aulaviva_arquivos WHERE disc=? ORDER BY updated_at DESC');
      $st->execute([$disc]);
      $xs = array_map(function ($r) use ($disc) {
        $r['url'] = DIR . '/materiais/' . $disc . '/' . rawurlencode($r['nome']);
        return $r;
      }, $st->fetchAll());
      echo json_encode($xs);
      exit;
    }
    case 'arqup': {
      if (($_GET['token'] ?? '') !== PROF_TOKEN) fail('token inválido', 'token', 403);
      $d = corpo();
      $nome = preg_replace('/[^A-Za-z0-9._ -]/u', '', basename($d['nome'] ?? 'arquivo.pdf')) ?: 'arquivo.pdf';
      $b64 = $d['base64'] ?? '';
      $bin = base64_decode($b64, true);
      if ($bin === false || strlen($bin) < 2) fail('arquivo inválido');
      if (strlen($bin) > MAX_ARQ) fail('arquivo > 15 MB');
      $dir = DIR . '/materiais/' . $disc;
      if (!is_dir($dir)) mkdir($dir, 0775, true);
      file_put_contents($dir . '/' . $nome, $bin);
      $st = db()->prepare('INSERT INTO aulaviva_arquivos (disc,nome,tipo,tamanho) VALUES (?,?,?,?)
        ON DUPLICATE KEY UPDATE tipo=VALUES(tipo), tamanho=VALUES(tamanho)');
      $st->execute([$disc, $nome, $d['tipo'] ?? '', strlen($bin)]);
      echo json_encode(['ok' => true, 'nome' => $nome]);
      exit;
    }

    /* ---------- entregas (aluno → professora) ---------- */
    case 'entrega': {
      if (!$code) fail('sem sessão — faça login', 'sem_sessao', 401);
      $d = corpo();
      $nome = preg_replace('/[^A-Za-z0-9._ -]/u', '', basename($d['nome'] ?? 'atividade.pdf')) ?: 'atividade.pdf';
      $ext = strtolower(pathinfo($nome, PATHINFO_EXTENSION));
      if (!in_array($ext, ['txt','doc','docx','pdf','odt'])) fail('formato não permitido (use txt, doc, docx, pdf ou odt)');
      $bin = base64_decode($d['base64'] ?? '', true);
      if ($bin === false || strlen($bin) < 2) fail('arquivo inválido');
      if (strlen($bin) > 12*1024*1024) fail('arquivo > 12 MB');
      $st = db()->prepare('SELECT nome FROM aulaviva_contas WHERE disc=? AND code=?');
      $st->execute([$disc, $code]);
      $aluno = norm($st->fetchColumn() ?: 'aluno');
      $aluno = preg_replace('/[^a-z0-9]+/', '_', $aluno);
      $dir = DIR . '/entregas/' . $disc . '/' . $code;
      if (!is_dir($dir)) mkdir($dir, 0770, true);
      $ts = date('Ymd_His');
      $arq = $dir . '/' . $ts . '_' . $nome;
      file_put_contents($arq, $bin);
      $st = db()->prepare('INSERT INTO aulaviva_entregas (disc,code,aluno,arquivo,nome,tamanho) VALUES (?,?,?,?,?,?)');
      $st->execute([$disc, $code, $aluno, $arq, $nome, strlen($bin)]);
      echo json_encode(['ok' => true, 'arquivo' => basename($arq)]);
      exit;
    }
    case 'minhas': {
      if (!$code) fail('sem sessão', 'sem_sessao', 401);
      $st = db()->prepare('SELECT nome,tamanho,created_at AS atualizado FROM aulaviva_entregas
        WHERE disc=? AND code=? ORDER BY created_at DESC');
      $st->execute([$disc, $code]);
      echo json_encode($st->fetchAll());
      exit;
    }
    case 'entregas': {
      if (($_GET['token'] ?? '') !== PROF_TOKEN) fail('token inválido', 'token', 403);
      $st = db()->prepare('SELECT e.id, c.nome AS aluno, e.nome AS arquivo, e.tamanho, e.created_at
        FROM aulaviva_entregas e JOIN aulaviva_contas c ON c.disc=e.disc AND c.code=e.code
        WHERE e.disc=? ORDER BY e.created_at DESC LIMIT 400');
      $st->execute([$disc]);
      $xs = $st->fetchAll();
      $tok = urlencode($_GET['token'] ?? '');
      foreach ($xs as &$r)
        $r['url'] = 'api.php?disc=' . $disc . '&a=dlent&id=' . (int)$r['id'] . '&token=' . $tok;
      unset($r);
      echo json_encode($xs);
      exit;
    }
    case 'dlent': {
      if (($_GET['token'] ?? '') !== PROF_TOKEN) fail('token inválido', 'token', 403);
      $st = db()->prepare('SELECT arquivo, nome FROM aulaviva_entregas WHERE disc=? AND id=?');
      $st->execute([$disc, (int)($_GET['id'] ?? 0)]);
      $r = $st->fetch();
      if (!$r || !is_file($r['arquivo'])) fail('entrega não encontrada', 'nf', 404);
      header('Content-Type: application/octet-stream');
      header('Content-Disposition: attachment; filename="' . $r['nome'] . '"');
      header('Content-Length: ' . filesize($r['arquivo']));
      readfile($r['arquivo']);
      exit;
    }
    default:
      fail('rota desconhecida', 'rota', 404);
  }
} catch (Throwable $e) {
  error_log('api.php [' . $disc . '/' . $a . ']: ' . $e->getMessage());
  fail('erro interno — tente novamente em instantes', 'interno', 500);
}
