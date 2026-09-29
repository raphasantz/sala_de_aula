<?php
// ============================================================
// PROCESSAR CONTATO — validação + sanitização + INSERT
// (PI-I semanas 13-16 · LP2: INSERT INTO na tabela mensagens)
// Fluxo: receber → validar → sanitizar → gravar → confirmar
// ============================================================
include "includes/conexao.php";
include "includes/cabecalho.php";

$erros = [];

// 1) VALIDAR no servidor (nunca confiar só no required do HTML):
if (empty($_POST["nome"]))     { $erros[] = "Informe seu nome."; }
if (empty($_POST["email"]))    { $erros[] = "Informe seu e-mail."; }
if (empty($_POST["mensagem"])) { $erros[] = "Escreva uma mensagem."; }

if (count($erros) > 0) {
    echo '<div class="aviso erro"><b>Ops! Corrija os campos:</b><ul style="margin:6px 0 0 20px">';
    foreach ($erros as $e) { echo "<li>" . htmlspecialchars($e) . "</li>"; }
    echo '</ul><p style="margin-top:8px"><a href="contato.php">← Voltar ao formulário</a></p></div>';
    include "includes/rodape.php";
    exit;
}

// 2) SANITIZAR na saída/gravacao (htmlspecialchars):
$nome     = htmlspecialchars(trim($_POST["nome"]));
$email    = htmlspecialchars(trim($_POST["email"]));
$assunto  = isset($_POST["assunto"]) ? htmlspecialchars($_POST["assunto"]) : "outro";
$mensagem = htmlspecialchars(trim($_POST["mensagem"]));
$novidades = isset($_POST["novidades"]) ? 1 : 0;

// 3) GRAVAR no banco (a tabela 'mensagens' foi criada no loja_turma.sql):
$sql = "INSERT INTO mensagens (nome, email, assunto, mensagem, novidades)
        VALUES ('" . $con->real_escape_string($nome) . "',
                '" . $con->real_escape_string($email) . "',
                '" . $con->real_escape_string($assunto) . "',
                '" . $con->real_escape_string($mensagem) . "',
                " . $novidades . ")";

if ($con->query($sql) === TRUE) {
    echo '<div class="aviso ok"><b>✔ Mensagem recebida, ' . $nome . '!</b><br>
          Guarde o protocolo: <b>#' . $con->insert_id . '</b><br>
          Respondemos em ' . $email . ' em até 2 dias úteis.</div>';
} else {
    echo '<div class="aviso erro">Não foi possível gravar: ' .
         htmlspecialchars($con->error) . '</div>';
}
echo '<p style="margin-top:10px"><a href="index.php">← Voltar ao início</a></p>';

include "includes/rodape.php";
?>
