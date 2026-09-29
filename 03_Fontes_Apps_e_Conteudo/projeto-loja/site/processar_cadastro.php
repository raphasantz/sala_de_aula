<?php
// ============================================================
// PROCESSAR CADASTRO — validação + sanitização + INSERT
// (PI-I: isset/empty/htmlspecialchars · LP2: INSERT na tabela clientes)
// ============================================================
include "includes/conexao.php";
include "includes/cabecalho.php";

$erros = [];

// 1) VALIDAÇÃO no servidor:
if (empty($_POST["nome"]))  { $erros[] = "Informe o nome completo."; }
if (empty($_POST["email"])) { $erros[] = "Informe o e-mail."; }
if (!isset($_POST["termos"])) { $erros[] = "É preciso aceitar os termos."; }

// e-mail com formato checável:
if (!empty($_POST["email"]) && !filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
    $erros[] = "O e-mail digitado não parece válido.";
}

if (count($erros) > 0) {
    echo '<div class="aviso erro"><b>Ops! Corrija:</b><ul style="margin:6px 0 0 20px">';
    foreach ($erros as $e) { echo "<li>" . htmlspecialchars($e) . "</li>"; }
    echo '</ul><p style="margin-top:8px"><a href="cadastro.php">← Voltar</a></p></div>';
    include "includes/rodape.php";
    exit;
}

// 2) SANITIZAÇÃO:
$nome       = htmlspecialchars(trim($_POST["nome"]));
$email      = htmlspecialchars(trim($_POST["email"]));
$telefone   = htmlspecialchars(trim($_POST["telefone"] ?? ""));
$nascimento = !empty($_POST["nascimento"]) ? $con->real_escape_string($_POST["nascimento"]) : null;
$cidade     = htmlspecialchars($_POST["cidade"] ?? "");
$origem     = htmlspecialchars($_POST["origem"] ?? "não informada");

// 3) INSERT (LP2, semana 5):
$sql = "INSERT INTO clientes (nome, email, telefone, nascimento, cidade, origem)
        VALUES ('" . $con->real_escape_string($nome) . "',
                '" . $con->real_escape_string($email) . "',
                '" . $con->real_escape_string($telefone) . "',
                " . ($nascimento ? "'" . $nascimento . "'" : "NULL") . ",
                '" . $con->real_escape_string($cidade) . "',
                '" . $con->real_escape_string($origem) . "')";

if ($con->query($sql) === TRUE) {
    echo '<div class="aviso ok"><b>✔ Cadastro realizado, ' . $nome . '!</b><br>
          Seu código de cliente é <b>#' . $con->insert_id . '</b>.<br>
          Bem-vindo(a) à Loja Tech da Turma! 🎉</div>';
} else {
    echo '<div class="aviso erro">Falha ao gravar: ' . htmlspecialchars($con->error) . '</div>';
}
echo '<p style="margin-top:10px"><a href="index.php">← Voltar ao início</a></p>';

include "includes/rodape.php";
?>
