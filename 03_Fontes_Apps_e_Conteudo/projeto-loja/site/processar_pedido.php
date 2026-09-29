<?php
// ============================================================
// PROCESSAR PEDIDO — valida, grava a VENDA e BAIXA o estoque
// (PI-I: validação/sanitização · LP2: INSERT + UPDATE no mesmo fluxo)
// ============================================================
include "includes/conexao.php";
include "includes/cabecalho.php";

$erros  = [];
$id     = isset($_POST["id"])     ? (int)$_POST["id"]     : 0;
$qtd    = isset($_POST["qtd"])    ? (int)$_POST["qtd"]    : 0;
$forma  = isset($_POST["forma"])  ? $_POST["forma"]       : "";
$nomec  = isset($_POST["nomec"])  ? trim($_POST["nomec"]) : "";
$emailc = isset($_POST["emailc"]) ? trim($_POST["emailc"]) : "";

// 1) VALIDAÇÕES no servidor:
if ($id < 1 || $qtd < 1 || $qtd > 10)               { $erros[] = "Pedido/quantidade inválidos."; }
if (!in_array($forma, ["pix", "cartao", "boleto"])) { $erros[] = "Forma de pagamento inválida."; }
if (strlen($nomec) < 3)                            { $erros[] = "Informe o nome de quem compra."; }
if (!filter_var($emailc, FILTER_VALIDATE_EMAIL))   { $erros[] = "E-mail inválido."; }

$p = null;
if ($id > 0) {
    $res = $con->query("SELECT id, nome, preco, estoque FROM produtos WHERE id = " . $id);
    $p = $res->fetch_assoc();
    $res->close();
}
if (!$p)                        { $erros[] = "Produto não encontrado."; }
elseif ($qtd > $p["estoque"])   { $erros[] = "Estoque insuficiente (restam " . (int)$p["estoque"] . ")."; }

if (count($erros) > 0) {
    echo '<div class="aviso erro"><b>Ops! Corrija:</b><ul style="margin:6px 0 0 20px">';
    foreach ($erros as $e) { echo "<li>" . htmlspecialchars($e) . "</li>"; }
    echo '</ul><p style="margin-top:8px"><a href="produtos.php">← Voltar ao catálogo</a></p></div>';
    include "includes/rodape.php";
    exit;
}

// 2) valores:
$total     = $p["preco"] * $qtd;
$nome_seg  = $con->real_escape_string(htmlspecialchars($nomec));
$email_seg = $con->real_escape_string(htmlspecialchars($emailc));

// 3) grava a VENDA:
$ok = $con->query("INSERT INTO vendas (produto_id, qtd, total) VALUES ("
                  . $id . ", " . $qtd . ", " . number_format($total, 2, ".", "") . ")");

// 4) baixa o ESTOQUE (o gerencial VB6 e a vitrine veem a mudança!):
$estoque_antes = (int)$p["estoque"];
if ($ok) {
    $con->query("UPDATE produtos SET estoque = estoque - " . $qtd . " WHERE id = " . $id);
}

$rotulo = ["pix"    => "Pix — aprovado na hora ⚡",
           "cartao" => "Cartão simulado — aprovado ✔",
           "boleto" => "Boleto gerado — vence em 2 dias 📄"];
?>

<div class="aviso ok">
    <b>✔ Pedido confirmado, <?= htmlspecialchars($nomec) ?>!</b><br>
    Produto: <b><?= htmlspecialchars($p["nome"]) ?></b> · <?= $qtd ?> un ·
    total <b>R$ <?= number_format($total, 2, ",", ".") ?></b><br>
    Pagamento: <?= $rotulo[$forma] ?><br>
    Comprovante enviado para <?= htmlspecialchars($emailc) ?> (simulado). ·
    Protocolo: <b>#<?= $con->insert_id ?></b>
</div>

<div class="card" style="text-align:left; padding:18px; margin-top:14px">
    <b>O que acabou de acontecer no banco (confira no phpMyAdmin!):</b>
    <ul style="margin:8px 0 0 22px; line-height:1.7">
        <li>INSERT em <b>vendas</b>: nova linha com produto, quantidade e total;</li>
        <li>UPDATE em <b>produtos</b>: estoque caiu de <?= $estoque_antes ?>
            para <?= max(0, $estoque_antes - $qtd) ?>;</li>
        <li>A vitrine do site e o gerencial VB6 já enxergam o novo estoque.</li>
    </ul>
</div>

<p style="margin-top:12px">
    <a class="btn-comprar" href="index.php">Voltar ao início</a>
    <a class="voltar" style="margin-left:14px" href="produtos.php">Continuar comprando</a>
</p>

<?php include "includes/rodape.php"; ?>
