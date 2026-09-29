<?php
// ============================================================
// CATÁLOGO — filtro por categoria via GET + cards clicáveis
// + tabela completa de estoque (dados vivos do banco)
// Exemplo de URL: produtos.php?cat=perifericos
// ============================================================
include "includes/conexao.php";
include "includes/cabecalho.php";

// 1) Ler o filtro da URL com segurança:
$cat = "";
if (isset($_GET["cat"]) && $_GET["cat"] !== "") {
    $cat = $con->real_escape_string($_GET["cat"]);
}

// 2) Consulta conforme o filtro:
$sql = "SELECT id, nome, categoria, preco, estoque, foto FROM produtos";
if ($cat !== "") { $sql .= " WHERE categoria = '" . $cat . "'"; }
$sql .= " ORDER BY nome";
$res = $con->query($sql);

// 3) Categorias para o menu de filtros:
$cats = $con->query("SELECT DISTINCT categoria FROM produtos ORDER BY categoria");
?>

<h2 class="secao">Catálogo de produtos — clique para ver detalhes e comprar</h2>

<div class="filtros">
    <a href="produtos.php" class="<?= $cat === "" ? "ativo" : "" ?>">Todas</a>
    <?php while ($c = $cats->fetch_assoc()): ?>
        <a href="produtos.php?cat=<?= urlencode($c["categoria"]) ?>"
           class="<?= $cat === $c["categoria"] ? "ativo" : "" ?>">
           <?= htmlspecialchars(ucfirst($c["categoria"])) ?></a>
    <?php endwhile; ?>
</div>

<div class="vitrine">
<?php while ($p = $res->fetch_assoc()): ?>
    <a class="card" href="produto.php?id=<?= (int)$p["id"] ?>">
        <img src="<?= htmlspecialchars($p["foto"]) ?>" alt="Foto de <?= htmlspecialchars($p["nome"]) ?>">
        <h3><?= htmlspecialchars($p["nome"]) ?></h3>
        <div class="cat"><?= htmlspecialchars($p["categoria"]) ?></div>
        <div class="preco">R$ <?= number_format($p["preco"], 2, ",", ".") ?></div>
        <?php if ($p["estoque"] <= 5): ?>
            <div class="estoque-baixo">⚠ estoque baixo (<?= (int)$p["estoque"] ?>)</div>
        <?php endif; ?>
        <span class="ver">ver detalhes e comprar ›</span>
    </a>
<?php endwhile; $res->close(); ?>
</div>

<h2 class="secao">Tabela completa de estoque (dados vivos do banco)</h2>
<div class="tabela-wrap">
<table class="estoque">
    <thead>
        <tr><th>Código</th><th>Produto</th><th>Categoria</th><th>Preço</th><th>Estoque</th><th></th></tr>
    </thead>
    <tbody>
    <?php
        $res2 = $con->query("SELECT id, nome, categoria, preco, estoque FROM produtos ORDER BY nome");
        while ($l = $res2->fetch_assoc()):
    ?>
        <tr>
            <td><?= (int)$l["id"] ?></td>
            <td><?= htmlspecialchars($l["nome"]) ?></td>
            <td><?= htmlspecialchars($l["categoria"]) ?></td>
            <td>R$ <?= number_format($l["preco"], 2, ",", ".") ?></td>
            <td><?= (int)$l["estoque"] ?></td>
            <td><a href="produto.php?id=<?= (int)$l["id"] ?>" style="color:#1b5faa;font-weight:700">ver ›</a></td>
        </tr>
    <?php endwhile; $res2->close(); ?>
    </tbody>
    <tfoot>
        <?php $tot = $con->query("SELECT COUNT(*) AS q, SUM(estoque) AS e FROM produtos")->fetch_assoc(); ?>
        <tr>
            <td colspan="4">Totais da loja</td>
            <td><?= (int)$tot["q"] ?> produtos / <?= (int)$tot["e"] ?> itens</td>
            <td></td>
        </tr>
    </tfoot>
</table>
</div>

<?php include "includes/rodape.php"; ?>
