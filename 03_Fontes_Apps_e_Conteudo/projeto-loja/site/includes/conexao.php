<?php
// ============================================================
// CONEXÃO COM O BANCO — usada pelo SITE (PI-I) e é o mesmo
// banco que o gerencial VB6 (LP2) utiliza.
// Padrão XAMPP: usuário root, sem senha.
// Se der erro: (1) MySQL iniciado no XAMPP? (2) importou o
// arquivo banco/loja_turma.sql no phpMyAdmin?
// ============================================================
$servidor = "localhost";
$usuario  = "root";
$senha    = "";
$banco    = "loja_turma";

$con = new mysqli($servidor, $usuario, $senha, $banco);
if ($con->connect_error) {
    die("Falha na conexão: " . $con->connect_error .
        " — Verifique o MySQL no XAMPP e importe banco/loja_turma.sql");
}
$con->set_charset("utf8");
?>
