<?php
// ============================================================
// PÁGINA INICIAL — vitrine com produtos CLICÁVEIS vindos do banco
// (clique no produto → página de detalhes com foto e link de pagamento)
// ============================================================
include "includes/conexao.php";
include "includes/cabecalho.php";
?>

<section class="hero">
    <img class="fundo" src="imagens/banner.png" alt="Banner da loja com equipamentos de informática">
    <div class="texto">
        <h1>Loja Tech da Turma 🖥️</h1>
        <p>Tudo aqui sai do banco de dados <b>loja_turma</b> (MySQL) e é montado em PHP,
           ao vivo, a cada acesso. Clique em um produto para ver detalhes e comprar.</p>
        <a class="cta" href="produtos.php">Ver catálogo completo</a>
    </div>
</section>

<h2 class="secao">Produtos em destaque — clique para ver e comprar</h2>
<div class="vitrine">
<?php
    $sql = "SELECT id, nome, categoria, preco, foto, estoque
            FROM produtos WHERE destaque = 1 ORDER BY nome";
    $res = $con->query($sql);
    while ($p = $res->fetch_assoc()):
?>
    <a class="card" href="produto.php?id=<?= (int)$p["id"] ?>">
        <img src="<?= htmlspecialchars($p["foto"]) ?>" alt="Foto do produto <?= htmlspecialchars($p["nome"]) ?>">
        <h3><?= htmlspecialchars($p["nome"]) ?></h3>
        <div class="cat"><?= htmlspecialchars($p["categoria"]) ?></div>
        <div class="preco">R$ <?= number_format($p["preco"], 2, ",", ".") ?></div>
        <?php if ($p["estoque"] <= 5): ?>
            <div class="estoque-baixo">⚠ últimas <?= (int)$p["estoque"] ?> unidades!</div>
        <?php endif; ?>
        <span class="ver">ver detalhes e comprar ›</span>
    </a>
<?php
    endwhile;
    $res->close();
?>
</div>

<h2 class="secao">Todos os produtos</h2>
<div class="vitrine">
<?php
    $res = $con->query("SELECT id, nome, categoria, preco, foto FROM produtos
                        WHERE destaque = 0 ORDER BY nome");
    while ($p = $res->fetch_assoc()):
?>
    <a class="card" href="produto.php?id=<?= (int)$p["id"] ?>">
        <img src="<?= htmlspecialchars($p["foto"]) ?>" alt="Foto do produto <?= htmlspecialchars($p["nome"]) ?>">
        <h3><?= htmlspecialchars($p["nome"]) ?></h3>
        <div class="cat"><?= htmlspecialchars($p["categoria"]) ?></div>
        <div class="preco">R$ <?= number_format($p["preco"], 2, ",", ".") ?></div>
        <span class="ver">ver detalhes e comprar ›</span>
    </a>
<?php
    endwhile;
    $res->close();
?>
</div>

<h2 class="secao">Sobre a loja (e sobre o projeto)</h2>
<div class="card" style="text-align:left; padding:20px">
    <p>A <b>Loja Tech da Turma</b> é o projeto-modelo das disciplinas
       <b>Programação para Internet I</b> e <b>Linguagem de Programação II</b>:</p>
    <ul style="margin:10px 0 0 22px; line-height:1.7">
        <li><b>PI-I:</b> HTML semântico, CSS, formulários com validação e PHP que monta as páginas;</li>
        <li><b>LP2:</b> banco MySQL (SGBD), comandos SQL, gerencial em VB6, relatórios e backup;</li>
        <li><b>Integração:</b> cada pedido realizado baixa o estoque no banco — site e gerencial
            veem os mesmos dados!</li>
    </ul>
    <p style="margin-top:10px">Aluno(a): sua missão é criar a <b>sua própria loja</b>
       (petshop, lanchonete, boutique…) com a mesma estrutura. 💪</p>
</div>

<?php include "includes/rodape.php"; ?>
