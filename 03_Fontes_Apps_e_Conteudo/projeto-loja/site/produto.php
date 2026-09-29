<?php
// ============================================================
// PÁGINA DO PRODUTO — detalhes + foto + link de pagamento
// URL: produto.php?id=3   (o id vem por GET, validado com (int))
// ============================================================
include "includes/conexao.php";
include "includes/cabecalho.php";

$id = isset($_GET["id"]) ? (int)$_GET["id"] : 0;   // (int) = proteção didática
$p = null;
if ($id > 0) {
    $res = $con->query("SELECT id, nome, categoria, preco, estoque, foto, descricao
                        FROM produtos WHERE id = " . $id);
    $p = $res->fetch_assoc();
    $res->close();
}

if (!$p):
?>
    <div class="aviso erro"><b>Produto não encontrado.</b>
        <p style="margin-top:6px"><a href="produtos.php">← Ver o catálogo completo</a></p>
    </div>
<?php
    include "includes/rodape.php";
    exit;
endif;
?>

<p style="margin:4px 0 12px"><a class="voltar" href="produtos.php">‹ Voltar ao catálogo</a></p>

<div class="produto-detalhe">
    <div class="foto">
        <img src="<?= htmlspecialchars($p["foto"]) ?>" alt="Foto do produto <?= htmlspecialchars($p["nome"]) ?>">
    </div>
    <div>
        <span class="badge-cat"><?= htmlspecialchars($p["categoria"]) ?></span>
        <h2><?= htmlspecialchars($p["nome"]) ?></h2>
        <div class="preco-grande">R$ <?= number_format($p["preco"], 2, ",", ".") ?></div>
        <p class="desc"><?= htmlspecialchars($p["descricao"]) ?></p>
        <p>
            <?php if ($p["estoque"] > 0): ?>
                ✅ Em estoque: <b><?= (int)$p["estoque"] ?></b> unidade(s)
            <?php else: ?>
                ⚠ Produto esgotado no momento
            <?php endif; ?>
        </p>
        <p style="margin-top:6px; font-size:13.5px; color:#5b6b7c">
            Código do produto: #<?= (int)$p["id"] ?> ·
            Consulta feita ao banco em <?= date("d/m/Y H:i") ?>
        </p>
        <?php if ($p["estoque"] > 0): ?>
            <a class="btn-comprar" href="pagamentos.php?id=<?= (int)$p["id"] ?>">
                💳 Ir para o pagamento
            </a>
        <?php endif; ?>
    </div>
</div>

<h2 class="secao">Você também pode gostar</h2>
<div class="vitrine">
<?php
    $res = $con->query("SELECT id, nome, categoria, preco, foto FROM produtos
                        WHERE categoria = '" . $con->real_escape_string($p["categoria"]) . "'
                          AND id <> " . (int)$p["id"] . " ORDER BY nome LIMIT 3");
    while ($r = $res->fetch_assoc()):
?>
    <a class="card" href="produto.php?id=<?= (int)$r["id"] ?>">
        <img src="<?= htmlspecialchars($r["foto"]) ?>" alt="Foto do produto <?= htmlspecialchars($r["nome"]) ?>">
        <h3><?= htmlspecialchars($r["nome"]) ?></h3>
        <div class="cat"><?= htmlspecialchars($r["categoria"]) ?></div>
        <div class="preco">R$ <?= number_format($r["preco"], 2, ",", ".") ?></div>
    </a>
<?php
    endwhile;
    $res->close();
?>
</div>

<?php include "includes/rodape.php"; ?>
