# -*- coding: utf-8 -*-
"""Gera, para cada bloco de aulas (5-18, 19-36, 37-42, 43-48, 49-72):
   • Texto_Apoio_Aulas_X_a_Y_*.pdf   — textinho corrido para falar em sala (padrão aulas 1-4)
   • Guia_Pratico_Aulas_X_a_Y_*.pdf  — passo a passo de laboratório (padrão Tutorial do Aluno)
Uso: python3 build_blocos.py
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)

from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Spacer

from build_pdf import P, S, make_box, make_code, make_table, big_section, safe_para
from build_tutoriais import build_doc, capa, checklist

SELO_TEXTO = HexColor("#9CC3EC")
SELO_GUIA = HexColor("#F5B50A")

# ===========================================================================
# BLOCOS
# ===========================================================================
BLOCOS = []

# ---------------------------------------------------------------- 5 a 18 ---
BLOCOS.append({
    "slug": "5_a_18_HTML",
    "faixa": "Aulas 5 a 18",
    "parte": "PARTE II · SEMANAS 2 A 6",
    "titulo_capa": "HTML:<br/>a estrutura de toda página",
    "sub_capa": "Texto de apoio para falar sobre as Aulas 5 a 18 — Parte II: ferramentas, "
                "fundamentos, conteúdo, tabelas e formulários, até o primeiro projeto avaliativo.",
    # ---------------- TEXTINHO ----------------
    "texto": [
        ("Abrindo o assunto",
         "Até aqui, nós entendemos como a Web funciona por fora. Agora chega a parte mais gostosa do "
         "curso: começar a <b>construir páginas</b>. E toda página da Web — do site da escola ao maior "
         "portal de notícias — é feita com a mesma linguagem: o <b>HTML</b>, que organiza o conteúdo em "
         "títulos, parágrafos, imagens, links, tabelas e formulários."),
        ("Aula 5 — O ambiente de trabalho",
         "Antes de codar, preparamos a bancada: um <b>editor de código</b> (o VS Code), o <b>navegador</b> "
         "para testar e o <b>gerenciador de arquivos</b> com a pasta do projeto. Site é <b>texto puro</b>: "
         "por isso nada de Word — e a página inicial de todo site se chama <b>index</b>, porque é ela que o "
         "servidor procura primeiro."),
        ("Aulas 6 a 9 — O esqueleto e o texto",
         "Todo documento HTML5 tem o mesmo esqueleto: <b>DOCTYPE</b>, <b>head</b> (as configurações, como o "
         "charset que garante os acentos) e <b>body</b> (o que aparece). Dentro do body, marcamos o conteúdo "
         "com <b>tags</b>: títulos de <b>h1 a h6</b> em hierarquia, parágrafos com <b>p</b>, quebras com "
         "<b>br</b>, separadores com <b>hr</b>. E na formatação, escolhemos tags com <b>significado</b>: "
         "<b>strong</b> para o que é importante, <b>em</b> para ênfase, <b>mark</b> para destacar."),
        ("Aulas 10 a 12 — Links, imagens e listas",
         "Os <b>links</b> são o que transforma páginas soltas em Web: com <b>a href</b> conectamos as páginas "
         "do nosso site (caminho relativo) e o mundo externo (URL absoluta). As <b>imagens</b> entram com "
         "<b>img src</b> e sempre com <b>alt</b> — a descrição que acessa quem não vê. E as <b>listas</b> "
         "(<b>ul</b>, <b>ol</b>, <b>dl</b>) organizam desde ingredientes até menus de navegação."),
        ("Aulas 13 a 18 — Tabelas, formulários e o primeiro projeto",
         "Para dados tabulares (notas, preços, estoque), usamos <b>tabelas</b>: <b>table, tr, th, td</b>, com "
         "<b>thead/tbody/tfoot</b> e <b>colspan</b> para mesclar. Para ouvir o usuário, usamos "
         "<b>formulários</b>: <b>form</b>, <b>label</b>, <b>input</b> de vários tipos, <b>select</b>, "
         "<b>textarea</b> e <b>button</b> — a ponte entre o visitante e o servidor. Fechando o bloco, o "
         "primeiro projeto avaliativo: o <b>site completo de uma empresa fictícia</b>, com 4 páginas, "
         "tabela e formulário (a entrega dos 10 pts da A1)."),
        ("Fechando a ideia",
         "HTML não toma decisões: ele <b>estrutura e dá significado</b> ao conteúdo. É o esqueleto bonito e "
         "organizado. O “cérebro” — validar, calcular, decidir, guardar — chega na Parte III, com o "
         "<b>PHP</b>. Por isso capriche agora: todo sistema grande começa com um HTML bem feito."),
    ],
    "frases": [
        "<b>Aula 5:</b> site é texto puro num editor de código; a página inicial se chama index e o projeto vive numa pasta organizada.",
        "<b>Aulas 6–9:</b> DOCTYPE + head (charset, title) + body (conteúdo); tags marcam tudo: h1–h6, p, br, hr, strong, em.",
        "<b>Aulas 10–12:</b> a href liga as páginas; img src+alt exibe imagens com descrição; ul/ol/dl organizam informações.",
        "<b>Aulas 13–18:</b> table/tr/th/td com thead/tbody/tfoot e colspan para dados; form/label/input/select/textarea para ouvir o usuário — e o projeto A1 junta tudo.",
    ],
    "termos": "tag · elemento · atributo · DOCTYPE · head · body · charset · h1–h6 · p · br · hr · "
              "strong · em · mark · a href · target · img src · alt · caminho relativo · ul · ol · dl · "
              "table · tr · th · td · thead · tbody · tfoot · colspan · form · action · method · label · "
              "input · select · textarea · button · required",
    "perguntas": [
        "Qual a diferença entre o head e o body?",
        "O que são elementos vazios? Cite dois.",
        "Quando devo usar strong e quando devo usar b?",
        "Para que serve o atributo alt de uma imagem?",
        "Qual a diferença entre radio e checkbox num formulário?",
    ],
    "gabarito": "1) head = configurações/metadados; body = conteúdo visível. 2) Não têm fechamento: br, hr, "
                "img, meta, input. 3) strong = importância (semântica); b = só aparência. 4) Descrever a "
                "imagem para leitores de tela e para quando ela não carrega. 5) radio = escolha única no "
                "grupo (mesmo name); checkbox = várias escolhas independentes.",
    # ---------------- GUIA PRÁTICO ----------------
    "guia_sub": "Passo a passo de laboratório das Aulas 5 a 18: ambiente, primeiras páginas, links, "
                "imagens, listas, tabelas, formulários e o projeto A1 — com testes, erros comuns e "
                "checklist final.",
    "planejamento": [
        ["Aula 5", "Ambiente: pasta do projeto, terminal, primeiro arquivo", "50 min"],
        ["Aulas 6–9", "Estrutura HTML5, títulos, parágrafos, formatação semântica", "4 × 50 min"],
        ["Aulas 10–12", "Links (Meu Primeiro Site), imagens com alt, listas", "3 × 50 min"],
        ["Aulas 13–14", "Tabelas: th/td, thead/tbody/tfoot, colspan", "2 × 50 min"],
        ["Aulas 15–17", "Formulários: input types, radio/checkbox, select, textarea", "3 × 50 min"],
        ["Aula 18", "Projeto A1: site da empresa fictícia (4 páginas)", "50 min + entrega"],
    ],
    "passos": [
        ("Aula 5 — Ambiente e primeira pasta", [
            "Abra o VS Code e crie (ou abra) a pasta <b>meu-site</b> dentro de Documents/programacao-web;",
            "Abra o terminal integrado (Ctrl+') e confirme com <b>dir</b> (ou ls) que está dentro da pasta;",
            "Crie as subpastas <b>imagens/</b>, <b>css/</b> e <b>includes/</b> pelo próprio terminal (mkdir);",
            "Crie o arquivo <b>index.html</b> vazio e deixe o projeto aberto na barra lateral.",
        ], None, None),
        ("Aulas 6–9 — Esqueleto, títulos e formatação", [
            "No index.html, digite <b>!</b> e pressione <b>Tab</b> (Emmet gera o esqueleto HTML5);",
            "Complete o <b>title</b> e salve (Ctrl+S); abra com o <b>Live Server</b> (botão direito → Open with Live Server);",
            "Monte a página “Minha cidade”: h1, dois h2, parágrafos, um br e um hr;",
            "Aplique <b>strong</b>, <b>em</b> e <b>mark</b> em trechos com significado real;",
            "Em duplas: troquem de máquina e façam o caça-erros do exercício 4 do módulo 3.",
        ], {"titulo": "Esqueleto gerado pelo Emmet (! + Tab)", "ling": "html", "linhas": [
            "<!DOCTYPE html>", "<html lang=\"pt-br\">", "<head>",
            "    <meta charset=\"UTF-8\">", "    <title>Minha cidade</title>", "</head>",
            "<body>", "    <h1>Minha Cidade</h1>", "    <!-- seu conteúdo aqui -->",
            "</body>", "</html>"]}, None),
        ("Aulas 10–12 — Meu Primeiro Site com links, imagens e listas", [
            "Crie <b>sobre.html</b> e <b>contato.html</b> com o mesmo esqueleto;",
            "Cole o menu abaixo no topo das três páginas e teste <b>todos</b> os links;",
            "Salve duas imagens em imagens/ e exiba-as com <b>img src + alt</b> descritivo;",
            "Na contato.html, liste seus contatos em <b>ul</b>; na sobre.html, conte sua rotina em <b>ol</b>;",
            "Desafio: um link externo com target=\"_blank\" (site da escola).",
        ], {"titulo": "Menu presente nas 3 páginas", "ling": "html", "linhas": [
            "<nav>", "  <a href=\"index.html\">Início</a> |",
            "  <a href=\"sobre.html\">Sobre</a> |", "  <a href=\"contato.html\">Contato</a>",
            "</nav>"]}, None),
        ("Aulas 13–14 — Tabelas passo a passo", [
            "Crie <b>tabela.html</b> e monte a tabela de alunos: 3 colunas (Nome, Curso, Nota);",
            "Primeiro o <b>thead</b> com th; depois 4 linhas de dados no <b>tbody</b>;",
            "No <b>tfoot</b>, uma célula com <b>colspan=\"2\"</b> (“Média da turma”) + a média;",
            "Confira a regra de ouro: cada linha deve somar o mesmo número de colunas;",
            "Visualize com border=\"1\" e ajuste até alinharem todas as células.",
        ], {"titulo": "Linha do tfoot com colspan", "ling": "html", "linhas": [
            "<tfoot>", "  <tr>", "    <td colspan=\"2\">Média da turma</td>",
            "    <td>8,25</td>", "  </tr>", "</tfoot>"]}, None),
        ("Aulas 15–17 — Cadastro de aluno completo", [
            "Crie <b>cadastro.html</b> com form action=\"processar.php\" method=\"post\";",
            "Adicione label+input para: nome (text), e-mail (email), telefone (text com placeholder), "
            "nascimento (date) e senha (password) — todos com name e required onde fizer sentido;",
            "Curso em <b>radio</b> (mesmo name, values diferentes); turno em <b>select</b> com opção "
            "“Selecione...” (disabled selected);",
            "Observações em <b>textarea</b> e botão <b>submit</b>;",
            "Teste o envio: sem o processar.php ainda, o navegador mostra erro — <b>é esperado</b>! "
            "O back-end chega no módulo 11.",
        ], {"titulo": "Radio com mesmo name = escolha única", "ling": "html", "linhas": [
            "<input type=\"radio\" id=\"inf\" name=\"curso\" value=\"Informática\">",
            "<label for=\"inf\">Informática</label>",
            "<input type=\"radio\" id=\"red\" name=\"curso\" value=\"Redes\">",
            "<label for=\"red\">Redes</label>"]}, None),
        ("Aula 18 — Projeto A1: site da empresa fictícia", [
            "Em dupla: escolham empresa e ramo; desenhem as 4 páginas no caderno antes de codar;",
            "Criem index, empresa, produtos e contato com menu idêntico e funcional;",
            "produtos.html: tabela com 4+ produtos (thead/tbody/tfoot + colspan);",
            "contato.html: formulário completo (select, textarea, checkbox, botão);",
            "Revisem o checklist da apostila (seção A1) e entreguem via AVA/Drive.",
        ], None, "A1"),
    ],
    "erros": [
        ["Acentos viram símbolos estranhos", "Falta meta charset UTF-8", "Inclua <meta charset=\"UTF-8\"> no head"],
        ["Imagem quebrada (ícone rasgado)", "Caminho/nome diferente (maiúsculas!)", "Conferir imagens/foto.jpg × Imagens/Foto.JPG"],
        ["Link interno não abre", "Usou https:// em página do próprio site", "Link interno = caminho relativo (sobre.html)"],
        ["Radio permite marcar os dois", "Names diferentes em cada radio", "Mesmo name para o grupo inteiro"],
        ["Tabela desalinhada", "colspan sem remover a célula engolida", "Contar colunas por linha ( soma = 3 )"],
        ["Página em branco no Live Server", "Arquivo salvo como .html.txt", "Exibir extensões no Windows e renomear"],
    ],
    "checklist": [
        "Crio o esqueleto HTML5 completo sem consultar (DOCTYPE, lang, charset, title, body);",
        "Uso hierarquia de títulos correta (um h1, h2 para seções);",
        "Formato com semântica: strong, em, mark (não b/i);",
        "Interligo páginas com menu de links testados;",
        "Insiro imagens por caminho relativo, sempre com alt;",
        "Escolho o tipo certo de lista (ul, ol, dl);",
        "Monta tabela completa com thead/tbody/tfoot e colspan;",
        "Monto formulário com label, types corretos, radio/checkbox/select/textarea;",
        "Entreguei (ou estou em dia com) o projeto A1 da empresa fictícia.",
    ],
    "prof": "Bloco longo (6 semanas): use o projeto “Meu Primeiro Site” como fio condutor — cada aula "
            "acrescenta uma peça. Reserve a aula 18 inteira para o A1 com revisão por checklist em duplas "
            "antes da entrega.",
})

# -------------------------------------------------------------- 19 a 36 ---
BLOCOS.append({
    "slug": "19_a_36_PHP",
    "faixa": "Aulas 19 a 36",
    "parte": "PARTE III · SEMANAS 7 A 12",
    "titulo_capa": "PHP:<br/>o cérebro do servidor",
    "sub_capa": "Texto de apoio para falar sobre as Aulas 19 a 36 — Parte III: introdução ao PHP, "
                "variáveis e operadores, decisões, repetições e arrays, com revisão cumulativa.",
    "texto": [
        ("Abrindo o assunto",
         "O HTML que construímos até aqui é um esqueleto bonito — mas não pensa. Não sabe somar duas "
         "notas, não sabe decidir se um aluno passou, não sabe mudar o conteúdo conforme o dia. É aí que "
         "entra o <b>PHP</b>: uma <b>linguagem de programação</b> que roda no <b>servidor</b> e dá vida ao "
         "site."),
        ("Aulas 19 a 21 — Onde o PHP vive",
         "A grande virada de chave: o HTML é interpretado no <b>navegador</b>; o PHP é executado no "
         "<b>servidor</b>. Você escreve blocos <b>&lt;?php … ?&gt;</b>, o servidor executa e entrega ao "
         "navegador apenas o <b>HTML gerado</b> — tanto que um Ctrl+U nunca mostra "
         "código PHP. Para testar em casa, o XAMPP transforma seu computador em servidor: tudo acessível "
         "em <b>http://localhost/…</b>. E o primeiro comando é um velho conhecido: <b>echo</b>, que “fala” "
         "com a página."),
        ("Aulas 22 a 26 — Variáveis, tipos e operadores",
         "Programar é guardar e transformar dados. No PHP, guardamos em <b>variáveis</b> com cifrão "
         "($nome, $idade); o tipo (texto, inteiro, decimal, booleano) o PHP descobre sozinho — e a lupa "
         "<b>var_dump()</b> revela tipo e valor. Com <b>operadores</b> fazemos contas (+ − * / %), "
         "juntamos textos (o ponto!) e comparamos valores — atenção ao par famoso: <b>==</b> compara só o "
         "valor, <b>===</b> compara valor <b>e</b> tipo. E os <b>lógicos</b> (&amp;&amp;, ||, !) combinam "
         "condições, como “média boa <b>e</b> frequência ok”."),
        ("Aulas 27 a 29 — Decisões",
         "Com condições, o programa escolhe caminhos: <b>if</b> executa se for verdadeiro; <b>if/else/"
         "elseif</b> encadeia várias possibilidades (o clássico “aprovado, recuperação ou reprovado”); e o "
         "<b>switch</b> compara um valor com opções fixas — perfeito para menus. Dois erros que viram "
         "lenda na turma: usar <b>=</b> (atribuição) dentro do if e esquecer o <b>break</b> do switch "
         "(a famosa cascata)."),
        ("Aulas 30 a 35 — Repetições e arrays",
         "Para repetir sem copiar e colar: <b>for</b> quando sabemos quantas voltas, <b>while</b> quando "
         "depende de uma condição (cuidado com o laço infinito!), <b>do…while</b> quando a primeira volta "
         "é garantida. E para guardar vários valores numa variável só: <b>arrays</b> — indexados (posições "
         "0, 1, 2…), <b>associativos</b> (chaves com significado: nome, idade, curso) e "
         "<b>multidimensionais</b> mais adiante. O <b>foreach</b> percorre tudo isso com elegância."),
        ("Aula 36 — Revisão que vira projeto",
         "O bloco fecha com uma <b>revisão cumulativa</b> que não é só teoria: ela vira o “sistema de "
         "cadastro simples”, juntando HTML + PHP + arrays + foreach numa página só. É a prova de que, com "
         "variáveis, decisões, laços e arrays, você já constrói sistemas de verdade."),
        ("Fechando a ideia",
         "Resumindo: o PHP é o cérebro que mora no servidor. Ele recebe dados, guarda em variáveis, "
         "compara, decide, repete e devolve HTML prontinho. Domine esse bloco e o resto do curso vira "
         "consequência."),
    ],
    "frases": [
        "<b>Aulas 19–21:</b> PHP roda no servidor e entrega HTML ao navegador; blocos <?php ?> com echo; testes em localhost (XAMPP).",
        "<b>Aulas 22–26:</b> variáveis com $, tipos revelados por var_dump, operadores (+ − * / % e .), == × ===, && || !.",
        "<b>Aulas 27–29:</b> if/elseif/else decidem em cadeia (mais restritiva primeiro); switch compara valores fixos com case/break/default.",
        "<b>Aulas 30–35:</b> for/while/do…while repetem; arrays guardam muitos valores; foreach percorre; associativos usam chave => valor.",
    ],
    "termos": "servidor · localhost · XAMPP · bloco <?php ?> · echo · ; · variável · $ · string · integer · "
              "float · boolean · var_dump · operador · % · concatenação (.) · == · === · && · || · ! · if · "
              "else · elseif · switch · case · break · default · for · while · do…while · laço infinito · "
              "array · índice · count() · foreach · chave => valor",
    "perguntas": [
        "Onde o código PHP é executado: no navegador ou no servidor?",
        "Qual a diferença entre echo e var_dump?",
        "Por que 5 == \"5\" é true mas 5 === \"5\" é false?",
        "Quando escolher for e quando escolher while?",
        "Em que situação um array associativo é melhor que um indexado?",
    ],
    "gabarito": "1) No servidor — o navegador só recebe o HTML gerado. 2) echo exibe conteúdo; var_dump "
                "mostra tipo + valor (depuração). 3) == compara só o valor; === exige valor e tipo iguais. "
                "4) for = voltas conhecidas/contador; while = condição que muda durante a execução. "
                "5) Quando cada item é uma “ficha” com campos nomeados (nome, idade, curso).",
    "guia_sub": "Passo a passo de laboratório das Aulas 19 a 36: primeiro PHP no XAMPP, variáveis, "
                "decisões, laços, arrays e o projeto de revisão — com testes, erros comuns e checklist.",
    "planejamento": [
        ["Aulas 19–21", "XAMPP rodando, ola.php, PHP misturado ao HTML", "3 × 50 min"],
        ["Aulas 22–24", "Variáveis, var_dump, calculadora com operadores", "3 × 50 min"],
        ["Aulas 25–26", "Comparações (== × ===) e tabela-verdade dos lógicos", "2 × 50 min"],
        ["Aulas 27–29", "if/elseif/else (situação do aluno) e switch (menu)", "3 × 50 min"],
        ["Aulas 30–32", "for (tabuada), while × do…while lado a lado", "3 × 50 min"],
        ["Aulas 33–35", "Arrays indexados, foreach, associativos (ficha do aluno)", "3 × 50 min"],
        ["Aula 36", "Revisão cumulativa + projeto cadastro simples", "50 min"],
    ],
    "passos": [
        ("Aulas 19–21 — O primeiro PHP no servidor", [
            "Abra o painel do XAMPP e inicie o <b>Apache</b> (verde);",
            "No VS Code, abra a pasta C:\\xampp\\htdocs\\meu-site (criada no tutorial de instalação);",
            "Crie <b>ola.php</b> com bloco <?php, dois echo e ponto e vírgula; salve;",
            "Acesse <b>http://localhost/meu-site/ola.php</b> e depois dê Ctrl+U (só HTML!);",
            "Misture HTML e PHP: exiba a data com date(\"d/m/Y\") dentro de um <p>.",
        ], {"titulo": "pagina.php — HTML + PHP + data dinâmica", "ling": "php", "linhas": [
            "<h1>Bem-vindo!</h1>", "<?php",
            "    echo \"<p>Hoje é \" . date(\"d/m/Y\") . \".</p>\";",
            "    echo \"<p>Agora são \" . date(\"H:i\") . \".</p>\";", "?>"]}, None),
        ("Aulas 22–26 — Variáveis, tipos e condições", [
            "Crie variaveis.php: $nome, $idade, $altura, $aprovado; exiba cada uma;",
            "Confirme os tipos com var_dump() (um por linha, com &lt;br&gt;);",
            "Monte a calculadora: soma, subtração, multiplicação, divisão, resto e média (parênteses!);",
            "Preveja no caderno: 10 == \"10\", 10 === \"10\", (true && false) || true — depois confirme;",
            "Monte a condição composta: aprovado = (media >= 7) && (freq >= 75).",
        ], {"titulo": "var_dump — a lupa", "ling": "php", "linhas": [
            "$idade = 17;", "var_dump($idade);    // int(17)",
            "$texto = \"17\";", "var_dump($texto);   // string(2) \"17\""]}, None),
        ("Aulas 27–29 — Decisões na prática", [
            "situacao.php: if/elseif/else com $nota (teste 9, 6.5 e 3 — anote as saídas);",
            "Inverta a ordem dos elseif de propósito e observe o estrago (discuta!);",
            "maioridade.php: três faixas (>=18, 16–17, <16) com mensagens;",
            "lanchonete.php: switch com 3 cases + default; remova um break e veja a cascata;",
            "Desafio: aprovação com frequência usando && dentro do if.",
        ], {"titulo": "Situação do aluno", "ling": "php", "linhas": [
            "$nota = 6.5;", "if ($nota >= 7)      { echo \"APROVADO\"; }",
            "elseif ($nota >= 5) { echo \"RECUPERAÇÃO\"; }",
            "else              { echo \"REPROVADO\"; }"]}, None),
        ("Aulas 30–32 — Laços sem sofrência", [
            "tabuada.php: for de 1 a 10 exibindo “7 x i = …”;",
            "Pares de 1 a 20 com $i += 2 (e depois com if + % dentro do laço);",
            "somas.php: while somando 1..5 com $contador++ (comente o ++ uma vez e veja o travamento);",
            "Compare lado a lado while × do…while com $x = 10 e condição $x < 5;",
            "Contagem regressiva 10→1 com for ($i = 10; $i >= 1; $i--).",
        ], {"titulo": "while com passo obrigatório", "ling": "php", "linhas": [
            "$contador = 1; $soma = 0;", "while ($contador <= 5) {",
            "    $soma += $contador;", "    $contador++;   // nunca esquecer!",
            "}"]}, None),
        ("Aulas 33–36 — Arrays, foreach e o projeto de revisão", [
            "alunos.php: array com 5 nomes; exiba [0] e [2]; adicione um 6º com $alunos[] = …;",
            "Percorra com foreach exibindo “Aluno: …”; some notas e calcule a média acumulando;",
            "ficha.php: array associativo (nome, idade, curso) + foreach $campo => $valor;",
            "Aula 36: junte tudo no cadastro_simples.php — array de fichas + tabela HTML via foreach;",
            "Autoavaliação com o checklist da revisão (apostila, módulo 9/10).",
        ], {"titulo": "Ficha associativa + foreach", "ling": "php", "linhas": [
            "$aluno = [\"nome\" => \"Ana\", \"idade\" => 17];",
            "foreach ($aluno as $campo => $valor) {",
            "    echo \"$campo: $valor <br>\";", "}"]}, None),
    ],
    "erros": [
        ["Parse error: unexpected …", "Faltou ; ou aspas fechando", "Ler arquivo+linha na mensagem e corrigir"],
        ["Página em branco ao abrir .php", "Abriu com dois cliques (file://)", "Sempre http://localhost/…"],
        ["Variável não aparece na string", "Aspas simples não interpolam: '$nome'", "Usar aspas duplas \"… $nome …\" ou ponto"],
        ["Laço infinito (navegador trava)", "while sem avanço do contador", "Garantir $i++/passo dentro do bloco"],
        ["Switch executa vários cases", "Faltou break", "break em cada case (menos onde a cascata é intencional)"],
        ["if sempre verdadeiro", "= (atribuição) no lugar de ==/===", "Comparar com == ou ==="],
    ],
    "checklist": [
        "Executo PHP pelo localhost e explico por que dois cliques não funcionam;",
        "Declaro variáveis e inspeciono tipos com var_dump;",
        "Escolho == ou === com justificativa;",
        "Combino condições com &&, || e !;",
        "Programo if/elseif/else na ordem correta das faixas;",
        "Monto menus com switch, case, break e default;",
        "Escolho for/while/do…while conforme o problema;",
        "Crio e percorro arrays indexados e associativos com foreach;",
        "Participei da revisão cumulativa (aula 36) e do projeto cadastro simples.",
    ],
    "prof": "Semana 8 = teste escrito-prático da A1 (15 pts): reserve a aula 24 para revisão dirigida com os "
            "testes rápidos dos módulos 1–5. A aula 36 é revisão + projeto: use o checklist oficial e o "
            "modelo de prova da apostila como estudo dirigido.",
})

# -------------------------------------------------------------- 37 a 42 ---
BLOCOS.append({
    "slug": "37_a_42_Formularios_PHP",
    "faixa": "Aulas 37 a 42",
    "parte": "PARTE IV · SEMANAS 13 E 14",
    "titulo_capa": "Formulários + PHP:<br/>o site ouve o usuário",
    "sub_capa": "Texto de apoio para falar sobre as Aulas 37 a 42 — Parte IV: GET e POST, validação, "
                "sanitização e o fluxo completo formulário → processamento → resultado.",
    "texto": [
        ("Abrindo o assunto",
         "Até agora, nossos formulários eram bonitos e mudos: o usuário digitava e… não acontecia nada. "
         "Neste bloco, o site finalmente <b>ouve e responde</b>: os dados digitados viajam até o PHP, que "
         "recebe, confere, protege e devolve uma confirmação. É o coração de todo sistema Web."),
        ("Aulas 37 e 38 — GET e POST: duas formas de enviar",
         "Com <b>method=\"get\"</b>, os dados viajam <b>na própria URL</b> (?produto=notebook) — ótimos para "
         "buscas e filtros, péssimos para senhas (todo mundo vê). Com <b>method=\"post\"</b>, viajam "
         "<b>escondidos no corpo da requisição</b> — o jeito certo para cadastros e logins. No PHP, a "
         "leitura é espelhada: <b>$_GET</b> e <b>$_POST</b>, dois arrays associativos automáticos cuja "
         "chave é o <b>name</b> de cada campo."),
        ("Aulas 39 e 40 — Validar e sanitizar: a dupla de segurança",
         "Regra de ouro: <b>nunca confie no que o usuário envia</b> — o required do HTML pode ser "
         "contornado. Por isso o servidor confere com <b>isset()</b> (veio?) e <b>empty()</b> (veio "
         "preenchido?), coletando todos os erros de uma vez. E na hora de <b>exibir</b> qualquer dado, "
         "<b>htmlspecialchars()</b> transforma < e > em entidades inofensivas — a vacina contra o ataque "
         "<b>XSS</b>, em que alguém tenta enviar código no lugar de texto."),
        ("Aulas 41 e 42 — O fluxo completo, de ponta a ponta",
         "Juntando tudo: formulário HTML com POST → PHP valida campo a campo → se houver erro, lista tudo "
         "com link “voltar” e para (exit) → se estiver tudo certo, sanitiza e exibe a <b>confirmação</b>. "
         "Esse fluxo de quatro etapas (preencher, enviar, processar, responder) é exatamente o que você "
         "vai repetir a vida inteira como programador Web — e é o núcleo do projeto: "
         "<b>cadastro.html + processar.php</b>."),
        ("Fechando a ideia",
         "Um site que só exibe é um mural; um site que recebe, valida e responde é um <b>sistema</b>. "
         "GET consulta, POST cadastra; isset/empty conferem; htmlspecialchars protege. Com esse bloco, "
         "seu projeto final já tem espinha dorsal."),
    ],
    "frases": [
        "<b>Aulas 37–38:</b> GET envia na URL ($_GET, buscas); POST envia no corpo ($_POST, cadastros e senhas).",
        "<b>Aulas 39–40:</b> isset/empty validam no servidor (required não basta); htmlspecialchars sanitiza a saída contra XSS.",
        "<b>Aulas 41–42:</b> fluxo completo: preencher → enviar → validar/processar → confirmar; projeto cadastro.html + processar.php.",
    ],
    "termos": "method · action · GET · POST · $_GET · $_POST · name · requisição · corpo · URL · isset() · "
              "empty() · validação · servidor · sanitização · htmlspecialchars() · XSS · exit · "
              "confirmação · fluxo em 4 etapas",
    "perguntas": [
        "Quando usar GET e quando usar POST? Dê um exemplo de cada.",
        "O que isset() e empty() verificam, respectivamente?",
        "Por que não basta o required do HTML?",
        "htmlspecialchars() protege contra qual ataque? Como?",
        "Quais são as 4 etapas do fluxo de um formulário com PHP?",
    ],
    "gabarito": "1) GET para buscas/filtros (dados na URL); POST para cadastros/logins (corpo da requisição). "
                "2) isset = foi enviado; empty = está vazio. 3) Porque pode ser contornado (F12); a validação "
                "séria é no servidor. 4) XSS: converte < > & aspas em entidades, então o código vira texto. "
                "5) Preencher → enviar → processar/validar → responder.",
    "guia_sub": "Passo a passo de laboratório das Aulas 37 a 42: busca com GET, cadastro com POST, "
                "validação com $erros, teste de XSS e o projeto cadastro.html + processar.php.",
    "planejamento": [
        ["Aula 37", "Formulário GET + buscar.php lendo $_GET", "50 min"],
        ["Aula 38", "Mesmo formulário com POST + $_POST; comparativo", "50 min"],
        ["Aula 39", "Validação com isset/empty e array $erros", "50 min"],
        ["Aula 40", "Sanitização: teste de XSS com htmlspecialchars", "50 min"],
        ["Aula 41", "Formulário completo com confirmação formatada", "50 min"],
        ["Aula 42", "Projeto do módulo: cadastro.html + processar.php", "50 min + entrega"],
    ],
    "passos": [
        ("Aula 37 — Busca com GET", [
            "Crie busca.html: form method=\"get\" action=\"buscar.php\" com input name=\"produto\";",
            "buscar.php: $produto = $_GET[\"produto\"]; exiba “Você buscou por: …”;",
            "Envie e observe a URL; depois digite a URL manualmente com outro valor;",
            "Com sanitize: exiba com htmlspecialchars (prepare o terreno da aula 40).",
        ], {"titulo": "buscar.php", "ling": "php", "linhas": [
            "<?php", "    $produto = $_GET[\"produto\"];",
            "    echo \"Você buscou por: \" . htmlspecialchars($produto);", "?>"]}, None),
        ("Aula 38 — O mesmo envio com POST", [
            "Duplique o form com method=\"post\" e action=\"contato.php\";",
            "contato.php: leia $_POST[\"nome\"] e $_POST[\"email\"] e confirme;",
            "Compare: a URL ficou limpa? O histórico guarda os dados?",
            "Discussão em dupla: quais campos NUNCA deveriam ir por GET?",
        ], None, None),
        ("Aula 39 — Validação séria no servidor", [
            "Em processar.php, monte $erros = [] e valide nome, e-mail e mensagem com empty();",
            "Se count($erros) > 0: exiba todos + link “Voltar” + <b>exit</b>;",
            "Teste 3 cenários: tudo preenchido / tudo vazio / metade preenchida;",
            "Contorne o required pelo F12 e prove que a validação do servidor segura.",
        ], {"titulo": "Padrão de validação", "ling": "php", "linhas": [
            "$erros = [];",
            "if (empty($_POST[\"nome\"]))  $erros[] = \"Nome obrigatório.\";",
            "if (count($erros) > 0) { /* exibir + exit */ }"]}, None),
        ("Aula 40 — O teste que impressiona (XSS)", [
            "No campo mensagem, digite: <script>alert('XSS')</script> e envie;",
            "Sem htmlspecialchars: o alert dispara (dados viram código!);",
            "Com htmlspecialchars: aparece como texto inofensivo;",
            "Regre no caderno: validar a entrada + sanitizar a saída, sempre.",
        ], None, None),
        ("Aulas 41–42 — Formulário completo e projeto do módulo", [
            "Monte contato completo: nome, e-mail, idade (number min/max), curso (select), mensagem;",
            "confirmar.php: valida tudo, sanitiza tudo e exibe confirmação formatada;",
            "Projeto em dupla: cadastro.html + processar.php (nome, e-mail, idade 10–120, curso radio);",
            "Testes obrigatórios: envio válido / campos vazios / idade fora da faixa;",
            "Entregue pelo AVA com os 3 testes documentados.",
        ], {"titulo": "Validação de faixa", "ling": "php", "linhas": [
            "$idade = isset($_POST[\"idade\"]) ? (int) $_POST[\"idade\"] : 0;",
            "if ($idade < 10 || $idade > 120) {",
            "    $erros[] = \"Idade deve estar entre 10 e 120.\";", "}"]}, None),
    ],
    "erros": [
        ["$_POST vazio / undefined key", "Campo sem name no HTML", "Todo campo processável precisa de name"],
        ["Leu $_POST mas o form é get", "Método e superglobal trocados", "method=get → $_GET; method=post → $_POST"],
        ["Erros somem e o código continua", "Faltou exit após exibir erros", "exit interrompe o processamento"],
        ["Alert de XSS dispara na confirmação", "echo puro do dado do usuário", "htmlspecialchars em toda saída"],
        ["Radio chega sem valor útil", "Radio sem value (envia 'on')", "Definir value em cada opção"],
    ],
    "checklist": [
        "Explico GET × POST com exemplos reais;",
        "Leio dados com $_GET/$_POST pela chave certa (name);",
        "Valido com isset/empty coletando todos os erros;",
        "Uso exit para não processar quando há erro;",
        "Sanitizo toda saída com htmlspecialchars;",
        "Montei o fluxo completo com mensagens e link voltar;",
        "Entreguei o projeto cadastro.html + processar.php com os 3 testes.",
    ],
    "prof": "A demonstração do XSS (aula 40) é o momento mais marcante do semestre: faça-a no projetor antes "
            "dos alunos testarem. Corrija o projeto do módulo com o checklist da aula 42 — ele é "
            "pré-requisito prático do projeto final.",
})

# -------------------------------------------------------------- 43 a 48 ---
BLOCOS.append({
    "slug": "43_a_48_Organizacao_PHP_HTML",
    "faixa": "Aulas 43 a 48",
    "parte": "PARTE V · SEMANAS 15 E 16",
    "titulo_capa": "Organização, include<br/>e funções",
    "sub_capa": "Texto de apoio para falar sobre as Aulas 43 a 48 — Parte V: estrutura de pastas, "
                "reutilização com include, funções com retorno, arrays multidimensionais e a listagem "
                "dinâmica (semana da A2).",
    "texto": [
        ("Abrindo o assunto",
         "Quando um sistema cresce, o inimigo não é a dificuldade — é a <b>bagunça</b>: menu copiado em dez "
         "páginas, cálculos repetidos, arquivos soltos. Este bloco ensina as três armas do programador "
         "organizado: <b>pastas certas</b>, <b>include</b> e <b>funções</b>."),
        ("Aulas 43 e 44 — Pastas certas e código reutilizado",
         "A estrutura profissional separa por tipo: páginas na raiz, <b>css/</b>, <b>imagens/</b> e "
         "<b>includes/</b>. No includes vivem o cabeçalho e o rodapé: escritos <b>uma vez</b>, inseridos "
         "em todas as páginas com <b>include</b> (ou <b>require</b>, que para tudo se o arquivo faltar). "
         "Mudou o menu? Editou um arquivo só — e o site inteiro atualiza."),
        ("Aulas 45 e 46 — Funções: a caixa de ferramentas",
         "Função é um bloco com nome que faz <b>uma tarefa</b>: recebe <b>parâmetros</b>, trabalha e "
         "<b>devolve</b> com return. calcularMedia, verificarMaioridade, calcularDesconto, situacao — "
         "guardadas num funcoes.php e usadas por qualquer página com require_once. Detalhe que separa "
         "iniciante de profissional: função <b>retorna</b>; quem chama decide se exibe."),
        ("Aulas 47 e 48 — Dados em duas dimensões e listagem dinâmica",
         "Um array de fichas de alunos (cada uma com nome, curso, nota) é um <b>array "
         "multidimensional</b>: lista de arrays, acessado com dois colchetes — $alunos[0][\"nome\"]. E aí "
         "acontece a mágica da <b>listagem dinâmica</b>: as tags <tr>/<td> escritas <b>uma única vez</b> "
         "dentro de um foreach se repetem para cada registro. Três alunos ou trezentos: o código é o "
         "mesmo. É assim que sistemas reais exibem produtos, pedidos e contatos — e é a semana da "
         "<b>Avaliação 2</b>."),
        ("Fechando a ideia",
         "Organizar não é frescura: é o que deixa o projeto final possível. Pastas certas para encontrar, "
         "include para não repetir HTML, funções para não repetir lógica, foreach para não repetir "
         "linhas de tabela. Quem domina este bloco constrói o projeto final com folga."),
    ],
    "frases": [
        "<b>Aulas 43–44:</b> estrutura em pastas (css/, imagens/, includes/) + include/require reutilizam cabeçalho e rodapé.",
        "<b>Aulas 45–46:</b> function com parâmetros e return; funcoes.php + require_once = caixa de ferramentas do sistema.",
        "<b>Aulas 47–48:</b> array multidimensional = lista de fichas ($alunos[0][\"nome\"]); foreach gera a tabela dinâmica — semana da A2.",
    ],
    "termos": "estrutura de pastas · includes/ · include · require · require_once · reutilização · "
              "function · parâmetro · argumento · return · null · valor padrão · ternário · array "
              "multidimensional · foreach aninhado · geração dinâmica · count() · A2",
    "perguntas": [
        "Qual a diferença entre include e require?",
        "O que uma função devolve se não tiver return?",
        "Como acesso o curso do segundo aluno em um array multidimensional?",
        "Por que chamamos a listagem de “dinâmica”?",
        "O que cai na Avaliação 2 e quando ela é aplicada?",
    ],
    "gabarito": "1) include avisa e continua; require gera erro fatal se o arquivo faltar. 2) null. "
                "3) $alunos[1][\"curso\"]. 4) Porque o HTML das linhas é gerado pelo PHP a partir dos dados "
                "(foreach) — o código não cresce com a quantidade. 5) HTML (estrutura a formulários), PHP "
                "(variáveis a funções) e GET/POST/validação — semana 16, aula 48.",
    "guia_sub": "Passo a passo de laboratório das Aulas 43 a 48: reorganizar o projeto, includes, "
                "funções utilitárias, arrays multidimensionais e a listagem dinâmica — com revisão da A2.",
    "planejamento": [
        ["Aula 43", "Reorganizar projeto em pastas; corrigir caminhos", "50 min"],
        ["Aula 44", "cabecalho.php + rodape.php com include em 3 páginas", "50 min"],
        ["Aulas 45–46", "funcoes.php: media, maioridade, desconto, situacao + testes", "2 × 50 min"],
        ["Aula 47", "Array multidimensional + foreach aninhado", "50 min"],
        ["Aula 48", "listar.php com tabela dinâmica + revisão A2", "50 min"],
    ],
    "passos": [
        ("Aulas 43–44 — Estrutura e includes", [
            "Mova seus arquivos para o padrão: páginas na raiz, css/, imagens/, includes/;",
            "Crie includes/cabecalho.php (DOCTYPE, head, menu) e includes/rodape.php (footer + date(\"Y\"));",
            "Reescreva index, cadastro e listar usando include nas duas pontas;",
            "Mude o título do menu UMA vez e recarregue as 3 páginas (uau!);",
            "Teste todos os links do menu a partir de cada página.",
        ], {"titulo": "Página usando os includes", "ling": "php", "linhas": [
            "<?php include \"includes/cabecalho.php\"; ?>",
            "<h2>Conteúdo da página</h2>",
            "<?php include \"includes/rodape.php\"; ?>"]}, None),
        ("Aulas 45–46 — Caixa de ferramentas de funções", [
            "Crie funcoes.php com calcularMedia, verificarMaioridade, calcularDesconto e situacao;",
            "teste_funcoes.php: chame cada uma e exiba os resultados (7.25, Não, 85, Aprovado);",
            "Troque echo por return onde estiver errado (discuta a diferença);",
            "Use o ternário para exibir Sim/Não da maioridade;",
            "Desafio: function formatarPreco($v) com number_format.",
        ], {"titulo": "funcoes.php — núcleo", "ling": "php", "linhas": [
            "function calcularMedia($n1, $n2) {",
            "    return ($n1 + $n2) / 2;", "}",
            "function situacao($media) {",
            "    if ($media >= 7) return \"Aprovado\";",
            "    if ($media >= 5) return \"Recuperação\";",
            "    return \"Reprovado\";", "}"]}, None),
        ("Aulas 47–48 — Duas dimensões e listagem dinâmica", [
            "Monte $alunos com 4 fichas (nome, curso, nota1, nota2);",
            "Acesse direto: $alunos[0][\"nome\"]; percorra com foreach aninhado;",
            "Calcule e exiba a média de cada aluno + média da turma (acumulando);",
            "listar.php: tabela com thead/tbody gerado por foreach + tfoot com count();",
            "Revisão da A2: resolva o modelo de prova da apostila em duplas.",
        ], {"titulo": "Linha dinâmica da tabela", "ling": "php", "linhas": [
            "<?php foreach ($alunos as $a): ?>",
            "  <tr>",
            "    <td><?= htmlspecialchars($a[\"nome\"]) ?></td>",
            "    <td><?= situacao(calcularMedia($a[\"nota1\"], $a[\"nota2\"])) ?></td>",
            "  </tr>",
            "<?php endforeach; ?>"]}, None),
    ],
    "erros": [
        ["include não acha o arquivo", "Caminho relativo à página errada", "De index.php: includes/cabecalho.php"],
        ["Função não mostra resultado", "return sem echo na chamada", "echo calcularMedia(8, 6.5);"],
        ["Tabela com linhas duplicadas/quebradas", "endforeach ou chaves mal fechadas", "Conferir foreach … endforeach;"],
        ["<?= não funciona em arquivo .html", "PHP só executa em .php via servidor", "Renomear para .php e acessar por localhost"],
        ["Média errada na listagem", "Soma acumulada fora/iniciada errada", "$soma = 0 antes do laço"],
    ],
    "checklist": [
        "Organizo qualquer projeto no padrão raiz + css/ + imagens/ + includes/;",
        "Reutilizo cabeçalho/rodapé com include (menu editado em 1 lugar);",
        "Escrevo funções com parâmetros e return (não echo interno);",
        "Monto e leio arrays multidimensionais com dois colchetes;",
        "Gero tabelas dinâmicas com foreach (3 ou 300 registros, mesmo código);",
        "Fiz a revisão dirigida para a A2 com o modelo de prova da apostila.",
    ],
    "prof": "Semana 16 = A2 (30 pts, prova; duplas/consulta conforme o Plano). Use a aula 48 para revisão "
            "ativa: modelo de prova da apostila em duplas + correção comentada no projetor.",
})

# -------------------------------------------------------------- 49 a 72 ---
BLOCOS.append({
    "slug": "49_a_72_Projeto_Final",
    "faixa": "Aulas 49 a 72",
    "parte": "PARTE VI · SEMANAS 17 A 24",
    "titulo_capa": "Projeto Final:<br/>do plano à apresentação",
    "sub_capa": "Texto de apoio para falar sobre as Aulas 49 a 72 — Parte VI: requisitos, desenvolvimento "
                "guiado, testes, depuração, revisão geral e apresentação final (A3).",
    "texto": [
        ("Abrindo o assunto",
         "Chegou a hora de juntar todas as peças do semestre em uma coisa só: um <b>sistema Web de "
         "verdade</b>, feito em grupo, do planejamento à apresentação. Não é um exercício a mais — é a "
         "prova de que vocês sabem construir."),
        ("Aulas 49 a 51 — Planejar antes de codar",
         "Tudo começa com escolhas bem feitas: o <b>tema</b> (cadastro de alunos, biblioteca, catálogo, "
         "tarefas…), os <b>papéis do grupo</b> e os <b>requisitos</b> — cinco perguntas: qual o objetivo? "
         "quem usa? quais funcionalidades? quais páginas? quais dados? Requisito bem escrito é "
         "<b>testável</b>: vira caso de teste depois. Com o plano na mão, nasce a estrutura: index, "
         "cadastro, processar, listar, funcoes, includes…"),
        ("Aulas 52 a 57 — Construir e polir",
         "A construção segue o fluxo que vocês dominam: página inicial com menu, formulário completo com "
         "labels e validação, processamento com $erros e htmlspecialchars, e a <b>listagem dinâmica</b> "
         "com foreach. Depois, o polimento: títulos claros, mensagens educadas, CSS mínimo consistente — "
         "e a <b>validação do projeto</b>: campos vazios, valores inválidos, navegação, sanitização. "
         "Teste cruzado entre grupos: olho novo acha bug novo."),
        ("Aulas 58 a 60 — Testar, depurar, revisar",
         "Software profissional é testado com método: a <b>tabela de testes</b> (teste × entrada × "
         "resultado esperado) com casos válidos, inválidos e <b>de limite</b>. Quando algo falha, a "
         "estratégia de depuração em 5 passos: ler a mensagem, identificar arquivo e linha, entender, "
         "corrigir a causa, testar de novo. E a aula 60 faz a <b>revisão geral</b> da ementa — o mapa "
         "completo para a prova final."),
        ("Aulas 61 a 72 — Desenvolver, apresentar, celebrar",
         "Três semanas de desenvolvimento guiado com “dailies” de 5 minutos: o que fizemos, o que falta, "
         "quem faz o quê. Depois, correções finais, <b>ensaio da apresentação</b> (roteiro: abertura, "
         "objetivo, demonstração com cadastro válido e inválido, listagem, um trecho de código, "
         "aprendizados) e o grande dia: as apresentações na aula 72, com a <b>prova escrita final</b> "
         "compondo a A3."),
        ("Fechando a ideia",
         "Ao final, cada grupo leva algo raro para quem está começando: um <b>sistema funcional no "
         "portfólio</b> e a experiência completa de equipe — planejar, construir, testar, corrigir e "
         "apresentar. Isso não se esquece. Isso é ser programador."),
    ],
    "frases": [
        "<b>Aulas 49–51:</b> tema + papéis + requisitos testáveis (objetivo, usuários, funcionalidades, páginas, dados) + estrutura de pastas.",
        "<b>Aulas 52–57:</b> menu, formulário validado, processamento seguro e listagem dinâmica; interface consistente e validação do projeto.",
        "<b>Aulas 58–60:</b> tabela de testes com casos de limite; depuração em 5 passos; revisão geral da ementa.",
        "<b>Aulas 61–72:</b> desenvolvimento guiado com dailies, entregas 1–6, ensaio e apresentação final (A3 = prova 30 + projeto 10).",
    ],
    "termos": "requisitos · teste · caso de limite · tabela de testes · erro de sintaxe · erro de lógica · "
              "erro de execução · depuração · var_dump · daily · entregas (1–6) · rubrica · demonstração · "
              "ensaio · A3 · prova final · apresentação",
    "perguntas": [
        "Quais são as 5 perguntas do levantamento de requisitos?",
        "O que é um caso de limite? Dê um exemplo do seu sistema.",
        "Quais são os 3 tipos de erro e qual deles não mostra mensagem?",
        "O que a demonstração da apresentação precisa mostrar obrigatoriamente?",
        "Como é composta a nota da A3?",
    ],
    "gabarito": "1) Objetivo, usuários, funcionalidades, páginas e dados. 2) Valor exatamente no mínimo/máximo "
                "das regras (ex.: ano = 1900 ou 2026). 3) Sintaxe (parse error), execução (warning) e lógica "
                "(sem mensagem — resultado errado). 4) Cadastro válido, tentativa inválida com mensagens e "
                "listagem dinâmica (+ um trecho de código). 5) 30 pts prova escrita final individual + "
                "10 pts projeto e apresentação.",
    "guia_sub": "Passo a passo das Aulas 49 a 72: formação dos grupos, requisitos, construção por semanas, "
                "tabela de testes, depuração, ensaio e apresentação — com o mapa das 6 entregas.",
    "planejamento": [
        ["Semana 17 (49–51)", "Grupos, tema, requisitos (Entrega 1), estrutura (Entrega 2)", "3 × 50 min"],
        ["Semana 18 (52–54)", "Página inicial + cadastro + processamento (Entrega 3)", "3 × 50 min"],
        ["Semana 19 (55–57)", "Listagem dinâmica, interface, validação (Entrega 4) + teste cruzado", "3 × 50 min"],
        ["Semanas 20–23 (58–69)", "Testes, correções, revisão (60) e desenvolvimento guiado (Entrega 5)", "12 × 50 min"],
        ["Semana 24 (70–72)", "Correções + prova final (A3) + ensaio + apresentações (Entrega 6)", "3 × 50 min"],
    ],
    "passos": [
        ("Semana 17 — Nasce o projeto", [
            "Formem grupos de 3–4 com papéis definidos (líder, front, back, testes);",
            "Escolham o tema e preencham o requisitos.txt (modelo da apostila, aula 50) → <b>Entrega 1</b>;",
            "Criem a estrutura completa de pastas e arquivos (mesmo vazios) → início da <b>Entrega 2</b>;",
            "Subam includes/cabecalho.php + rodape.php e o index.php com menu navegável;",
            "Combinem o repositório/compartilhamento único do grupo (Drive/pen-drive do líder).",
        ], {"titulo": "requisitos.txt — modelo (1 página)", "ling": "texto", "linhas": [
            "TEMA: Biblioteca da Escola · GRUPO: nomes",
            "1 OBJETIVO: controlar acervo e disponibilidade.",
            "2 USUÁRIOS: bibliotecário (cadastro), alunos (consulta).",
            "3 FUNCIONALIDADES: cadastrar, listar, buscar por título.",
            "4 PÁGINAS: index, cadastro, processar, listar.",
            "5 DADOS: título*, autor*, gênero (select), ano (1900-2026), disponível.",
            "6 VALIDAÇÕES: título/autor obrigatórios; ano na faixa."]}, None),
        ("Semanas 18–19 — Construir o núcleo", [
            "cadastro.php com todos os campos dos requisitos (label, name, types, required);",
            "processar.php: $erros + exit + link voltar + htmlspecialchars (Entrega 3);",
            "listar.php: tabela dinâmica com foreach + tfoot com total (Entrega 4);",
            "Interface: h1/h2 claros, mensagens de sucesso/erro, CSS mínimo no css/estilo.css;",
            "Validação do projeto: vazios, inválidos, limites, navegação, sanitização;",
            "Teste cruzado: troquem de sistema com outro grupo e anotem as falhas encontradas.",
        ], None, None),
        ("Semanas 20–23 — Testar, corrigir e desenvolver", [
            "Montem a tabela de testes (mín. 6 casos: válido, inválido, limite por funcionalidade);",
            "Executem, marquem OK/FALHOU e transformem falhas em tarefas da semana;",
            "Depurem com a estratégia dos 5 passos (ler → identificar → entender → corrigir → testar);",
            "Aula 60: revisão geral com o mapa da apostila (prepara a prova final);",
            "Dailies de 5 min no início de cada aula: feito / falta / quem faz;",
            "Fechem a <b>Entrega 5</b>: versão testada, com a tabela de testes preenchida.",
        ], {"titulo": "Tabela de testes — modelo", "ling": "texto", "linhas": [
            "| # | Teste          | Entrada            | Esperado           | OK? |",
            "| 1 | Cadastro válido| título/autor ok    | mensagem sucesso   |     |",
            "| 2 | Campos vazios  | nada               | erros obrigatórios |     |",
            "| 3 | Ano limite     | ano = 1900         | aceita             |     |",
            "| 4 | Ano fora       | ano = 1899         | erro de faixa      |     |",
            "| 5 | Texto com tag  | título <b>t</b>    | exibido como texto |     |",
            "| 6 | Listagem       | 3 cadastros        | tabela com 3 linhas|     |"]}, None),
        ("Semana 24 — Fechar com chave de ouro", [
            "Aula 70: correções finais de código/interface + <b>prova escrita final (A3, 30 pts)</b>;",
            "Aula 71: ensaio com cronômetro (5–8 min), dados de exemplo já cadastrados, todos falam;",
            "Gravem um vídeo-plano B da demonstração (celular) contra imprevistos;",
            "Aula 72: apresentações + avaliação final (10 pts) + <b>Entrega 6</b> (versão final);",
            "Celebrem: vocês construíram um sistema de verdade, em equipe, de ponta a ponta.",
        ], None, "A3"),
    ],
    "erros": [
        ["Grupo com 4 versões diferentes do código", "Arquivos em máquinas separadas", "Um único compartilhamento; líder sincroniza"],
        ["Demonstração com listagem vazia", "Dados de exemplo não cadastrados", "Pré-cadastrar 3–5 registros antes da apresentação"],
        ["Apresentação estoura o tempo", "Ensaio sem cronômetro", "Ensaiar 2× com timer; cortar falas longas"],
        ["Bug volta depois de 'corrigido'", "Corrigiu o sintoma, não a causa", "Reproduzir com teste antes e depois da correção"],
        ["Requisito virou função inesperada", "Requisito vago ('ser bonito')", "Reescrever requisito de forma testável"],
    ],
    "checklist": [
        "Entregas 1 a 6 feitas (ou agendadas) nas semanas corretas;",
        "requisitos.txt completo e testável aprovado pelo professor;",
        "Cadastro, processamento e listagem funcionando de ponta a ponta;",
        "Validação e sanitização em todos os pontos de entrada/saída;",
        "Tabela de testes com ≥ 6 casos executados e documentados;",
        "Correções das falhas aplicadas e retestadas;",
        "Ensaio cronometrado com participação de todos;",
        "Demonstração pronta: válido + inválido + listagem + trecho de código.",
    ],
    "prof": "Atue como consultor, não como executor: circule com o checklist de 12 itens da apostila e cobre "
            "as dailies. Na aula 71, assista a um ensaio por grupo. A rubrica dos 10 pts está na seção A3 da "
            "apostila — aplique-a durante as apresentações.",
})

# ===========================================================================
# GERACAO
# ===========================================================================
def story_texto(b):
    st = []
    st += capa(b["titulo_capa"], b["sub_capa"],
               f"{b['faixa'].upper()} · {b['parte']}", SELO_TEXTO)
    st += big_section("O textinho (para falar ou ler com a turma)", "tom de conversa · " + b["faixa"],
                      page_break=False)
    for titulo, par in b["texto"]:
        st.append(P(f"<b>{titulo}</b>", S["h2"]))
        st.append(P(par, S["body"]))
    st += big_section("Em uma frase (para escrever no quadro)", "O essencial de cada etapa")
    for f in b["frases"]:
        st.append(Paragraph("•&nbsp;&nbsp;" + safe_para(f), S["li"]))
    st.append(Spacer(1, 6))
    st.append(make_box("conceito", b["termos"], title="TERMOS PARA DEIXAR NO QUADRO"))
    st += big_section("Para fixar conversando", "Perguntas orais para fechar o bloco")
    for i, q in enumerate(b["perguntas"], 1):
        st.append(Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;{safe_para(q)}", S["li_num"]))
    st.append(Spacer(1, 4))
    st.append(make_box("dica", b["gabarito"], title="GABARITO RÁPIDO DO PROFESSOR"))
    return st

def story_guia(b):
    st = []
    st += capa(b["titulo_capa"], b["guia_sub"],
               f"GUIA PRÁTICO · {b['faixa'].upper()} · {b['parte']}", SELO_GUIA)
    st += big_section("Planejamento do bloco", "Encontros · atividades · tempos", page_break=False)
    st.extend(make_table({"cab": ["Encontro", "Atividade principal", "Tempo"],
                          "lin": b["planejamento"], "larguras": [3.4, 10.2, 3.4]}))
    st.append(make_box("dica", "Siga a ordem: cada passo testa o anterior. Trabalhe em duplas e projete os "
                       "passos; só avance quando a maioria concluir. Os códigos são para DIGITAR, não "
                       "copiar — é digitando que o erro ensina.", title="PARA O PROFESSOR — CONDUÇÃO"))
    for titulo, passos, cod, av in b["passos"]:
        st.append(P(f"<b>{titulo}</b>", S["h2"]))
        st.extend([Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;{safe_para(p)}", S["li_num"]) for i, p in enumerate(passos, 1)])
        if cod:
            st.append(make_code(cod))
        if av == "A1":
            st.append(make_box("dica", "Trabalho prático de HTML — 10 pts da A1 (entrega na semana 6). "
                               "Rubrica completa na seção AVALIAÇÕES da apostila.",
                               title="📝 AVALIAÇÃO À VISTA"))
        elif av == "A3":
            st.append(make_box("dica", "Prova escrita final individual (30 pts) + projeto e apresentação "
                               "(10 pts). Rubrica na seção AVALIAÇÕES da apostila.",
                               title="📝 AVALIAÇÃO À VISTA"))
    st += big_section("Erros comuns da turma (e como resolver)", "Cole no projetor quando aparecerem")
    st.extend(make_table({"cab": ["Sintoma", "Causa provável", "Solução"],
                          "lin": b["erros"], "larguras": [5.2, 4.6, 7.2]}))
    st += big_section("Checklist final do bloco", "“Eu sei fazer” — marque com o visto do professor")
    st.extend(checklist(b["checklist"], "Marque cada item concluído"))
    st.append(make_box("dica", b["prof"], title="PARA O PROFESSOR — RITMO E AVALIAÇÃO"))
    return st

if __name__ == "__main__":
    for b in BLOCOS:
        build_doc(os.path.join(_ROOT, "output", f"Texto_Apoio_{b['slug']}.pdf"),
                  lambda b=b: story_texto(b),
                  label=f"TEXTO DE APOIO · {b['faixa'].upper()}",
                  header="PROGRAMAÇÃO PARA INTERNET I — TEXTO DE APOIO",
                  centro="Material de apoio da disciplina · Turma 2/2026")
        build_doc(os.path.join(_ROOT, "output", f"Guia_Pratico_{b['slug']}.pdf"),
                  lambda b=b: story_guia(b),
                  label=f"GUIA PRÁTICO · {b['faixa'].upper()}",
                  header="PROGRAMAÇÃO PARA INTERNET I — GUIA PRÁTICO DE LABORATÓRIO",
                  centro="Digite os códigos, não copie e cole · teste a cada passo")
    print("Todos os blocos gerados.")
