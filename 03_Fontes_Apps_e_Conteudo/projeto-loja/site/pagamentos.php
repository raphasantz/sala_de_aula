<?php
// ============================================================
// PÁGINA DE PAGAMENTO — resumo do pedido + forma de pagamento
// URL: pagamentos.php?id=3&qtd=1   (ambiente DIDÁTICO: nenhuma cobrança real)
// ============================================================
include "includes/conexao.php";
include "includes/cabecalho.php";

$id  = isset($_GET["id"])  ? (int)$_GET["id"]  : 0;
$qtd = isset($_GET["qtd"]) ? (int)$_GET["qtd"] : 1;
if ($qtd < 1)  { $qtd = 1; }
if ($qtd > 10) { $qtd = 10; }

$p = null;
if ($id > 0) {
    $res = $con->query("SELECT id, nome, preco, estoque, foto FROM produtos WHERE id = " . $id);
    $p = $res->fetch_assoc();
    $res->close();
}

if (!$p || $p["estoque"] < 1) {
    echo '<div class="aviso erro"><b>Pedido inválido ou produto esgotado.</b>' .
         '<p style="margin-top:6px"><a href="produtos.php">← Escolher um produto</a></p></div>';
    include "includes/rodape.php";
    exit;
}
if ($qtd > $p["estoque"]) { $qtd = $p["estoque"]; }
$total = $p["preco"] * $qtd;
?>

<h2 class="secao">Pagamento — pedido #<?= date("ymd") ?>-<?= (int)$p["id"] ?></h2>

<div class="pgto-resumo">
    <img src="<?= htmlspecialchars($p["foto"]) ?>" alt="Foto do produto">
    <div style="flex:1">
        <b style="font-size:18px; color:#0d2b4e"><?= htmlspecialchars($p["nome"]) ?></b>
        <p style="color:#5b6b7c; font-size:14px">R$ <?= number_format($p["preco"], 2, ",", ".") ?> cada ·
           estoque disponível: <?= (int)$p["estoque"] ?></p>
        <form method="get" action="pagamentos.php" style="margin-top:8px">
            <input type="hidden" name="id" value="<?= (int)$p["id"] ?>">
            <label style="display:inline; margin-right:6px" for="qtd">Quantidade:</label>
            <select name="qtd" id="qtd"
                    style="width:auto; padding:6px 10px; border:2px solid #d9d4ee; border-radius:8px"
                    onchange="this.form.submit()">
                <?php for ($i = 1; $i <= min(10, $p["estoque"]); $i++): ?>
                    <option value="<?= $i ?>" <?= $i == $qtd ? "selected" : "" ?>><?= $i ?></option>
                <?php endfor; ?>
            </select>
            <noscript><button type="submit" style="margin-left:6px">ok</button></noscript>
        </form>
    </div>
    <div style="text-align:right">
        <div style="color:#5b6b7c; font-size:13px">Total a pagar</div>
        <div class="total">R$ <?= number_format($total, 2, ",", ".") ?></div>
    </div>
</div>

<form class="cartao" action="processar_pedido.php" method="post">
    <input type="hidden" name="id"  value="<?= (int)$p["id"] ?>">
    <input type="hidden" name="qtd" value="<?= $qtd ?>">

    <label>Escolha a forma de pagamento:</label>
    <div class="pgto-opcoes">
        <label><img src="imagens/icon-pix.png" alt="Pix">
            <input type="radio" name="forma" value="pix" checked> Pix (aprova na hora)</label>
        <label><img src="imagens/icon-cartao.png" alt="Cartão">
            <input type="radio" name="forma" value="cartao"> Cartão (simulado)</label>
        <label><img src="imagens/icon-boleto.png" alt="Boleto">
            <input type="radio" name="forma" value="boleto"> Boleto (2 dias)</label>
    </div>

    <div class="aviso-seguro">🔒 <b>Ambiente de estudo:</b> nenhuma cobrança real acontece.
        Não digite dados verdadeiros de cartão — use números fictícios como 4242 4242 4242 4242.</div>

    <label for="nomec">Nome de quem compra *</label>
    <input type="text" id="nomec" name="nomec" required placeholder="Nome completo">

    <label for="emailc">E-mail para o comprovante *</label>
    <input type="email" id="emailc" name="emailc" required placeholder="voce@exemplo.com">

    <button type="submit">Confirmar pedido</button>
</form>

<p><a class="voltar" href="produto.php?id=<?= (int)$p["id"] ?>">← Voltar ao produto</a></p>

<?php include "includes/rodape.php"; ?>
