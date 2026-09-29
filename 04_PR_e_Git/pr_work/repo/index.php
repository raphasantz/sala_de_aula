<?php
/*
 * Porta de entrada do Kit Sala de Aula (raiz de Kit_Sala_de_Aula/).
 * O QUÊ: quem abre /KiT_Sala_de_Aula/ (o link que a professora manda no grupo)
 *        é levado DIRETO ao app AulaViva da disciplina — e o app, sem sessão,
 *        abre já pedindo nome + senha (login/criar conta).
 * POR QUÊ: antes a raiz não tinha index (listagem de pastas ou página vazia),
 *        então o aluno clicava no link e não caía no login.
 * ONDE:  Kit_Sala_de_Aula/index.php (raiz do vhost pcs-replica).
 *        ?d=lp2 leva à disciplina LP2; sem parâmetro (ou ?d=pi1) leva à PI-I.
 * Regras respeitadas: sem credenciais novas, sem localStorage, sem tocar em
 * outros vhosts; apenas um redirecionamento 302 relativo.
 */
$d = strtolower(trim((string)($_GET['d'] ?? 'pi1')));
$alvo = ($d === 'lp2' || $d === 'lpii' || $d === 'linguagem')
    ? 'apps-nuvem/AulaViva_lp2_index.html'
    : 'apps-nuvem/AulaViva_pi1_index.html';
header('Cache-Control: no-store');
header('Location: ' . $alvo, true, 302);
exit;
