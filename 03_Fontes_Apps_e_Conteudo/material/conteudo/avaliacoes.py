# -*- coding: utf-8 -*-
"""Avaliações do semestre (A1, A2, A3) e especificação do Projeto Final Integrador.

Modelos de prova propostos (S) — o professor pode adaptá-los.
Cada questão traz 'resposta' e 'comentario' (exibidos apenas na versão do professor).
"""

# ---------------------------------------------------------------------------
# PROJETO FINAL INTEGRADOR — especificação oficial do cronograma
# ---------------------------------------------------------------------------
PROJETO_FINAL = {
    "titulo": "Projeto Final Integrador",
    "o_que_e": (
        "Aplicação Web simples e funcional desenvolvida em grupos, integrando HTML (estrutura e conteúdo), "
        "PHP (processamento e conteúdo dinâmico), formulários (entrada de dados), validação (controle dos "
        "dados), arrays (armazenamento temporário) e organização de arquivos (estrutura do projeto)."
    ),
    "temas": [
        "Cadastro de alunos", "Agenda de contatos", "Catálogo de produtos",
        "Sistema de contatos", "Cadastro de clientes", "Biblioteca", "Controle de tarefas",
    ],
    "entregas": [
        ("Entrega 1", "Proposta do projeto e requisitos (tema, objetivo, usuários, funcionalidades)", "Aulas 49–50", "Semana 17"),
        ("Entrega 2", "Estrutura de arquivos/pastas e página inicial com menu", "Aulas 51–52", "Semanas 17–18"),
        ("Entrega 3", "Página de cadastro (formulário completo) e processamento PHP", "Aulas 53–54", "Semana 18"),
        ("Entrega 4", "Listagem dinâmica, interface e validação do projeto", "Aulas 55–57", "Semana 19"),
        ("Entrega 5", "Versão testada: testes, tratamento de erros e correções", "Aulas 58–70", "Semanas 20–24"),
        ("Entrega 6", "Versão final + apresentação do projeto (aula 72)", "Aulas 71–72", "Semana 24"),
    ],
    "criterios_10pts": [
        ("Funcionalidade", "2,0", "Cadastro, listagem e validação funcionando de ponta a ponta."),
        ("Organização dos arquivos", "2,0", "Estrutura em pastas (css/, imagens/, includes/), includes reutilizados, nomes padronizados."),
        ("Qualidade do código", "2,0", "Nomes significativos, indentação consistente, comentários úteis."),
        ("Uso correto de HTML e PHP", "2,0", "HTML semântico e válido; PHP com validação (isset/empty) e sanitização (htmlspecialchars)."),
        ("Apresentação e demonstração", "2,0", "Roteiro seguido, demonstração funcional (válido + inválido + listagem), todos participam, dentro do tempo."),
    ],
}

# ---------------------------------------------------------------------------
# AVALIAÇÃO 1 — 30 pts (Semanas 1 a 8)
# ---------------------------------------------------------------------------
A1 = {
    "id": "A1",
    "titulo": "Avaliação 1 — Web e HTML (30 pts)",
    "periodo": "Semanas 1 a 8 (S)",
    "composicao": [
        ("Trabalho prático de HTML — “site da empresa fictícia”", "10 pts", "Entrega na semana 6 (aula 18)"),
        ("Atividades extraclasse/AVA e exercícios de fixação", "5 pts", "Semanas 1 a 8"),
        ("Teste escrito-prático sobre Web e HTML", "15 pts", "Semana 8"),
    ],
    "trabalho": {
        "titulo": "Trabalho prático (10 pts): site da empresa fictícia",
        "descricao": (
            "Desenvolver o site de uma empresa fictícia com 4 páginas (index.html, empresa.html, "
            "produtos.html e contato.html), aplicando todos os conteúdos de HTML do curso até o módulo 5. "
            "Pode ser feito em duplas ou individualmente (critério do professor)."
        ),
        "requisitos": [
            "4 páginas com estrutura HTML5 completa (DOCTYPE, html lang, meta charset, title) e menu de navegação idêntico e funcional em todas;",
            "index.html: h1, parágrafos com formatação semântica (strong, em), imagem com alt, lista (ul ou ol) e separador hr;",
            "empresa.html: hierarquia h1/h2, textos, quebras (br) e separadores (hr), imagem;",
            "produtos.html: tabela com no mínimo 4 produtos (nome, categoria, preço, estoque) usando thead, tbody, tfoot e colspan no rodapé;",
            "contato.html: formulário com nome (text), e-mail (email), assunto (select), mensagem (textarea), checkbox de novidades e botão de envio, todos os campos com label;",
            "Organização: pasta imagens/, nomes de arquivos em minúsculas sem acento/espaço, código indentado.",
        ],
        "rubrica": [
            ("Estrutura e navegação", "2,0", "HTML5 completo nas 4 páginas; menu idêntico e sem links quebrados."),
            ("Conteúdo e semântica", "2,0", "Hierarquia de títulos correta; strong/em (não b/i); imagens com alt descritivo; listas adequadas."),
            ("Tabela de produtos", "2,0", "thead/tbody/tfoot, colspan correto, 4+ produtos, células alinhadas."),
            ("Formulário de contato", "2,0", "Todos os campos pedidos, labels associados (for/id), types corretos, select/textarea/checkbox presentes."),
            ("Organização e qualidade", "2,0", "Estrutura de pastas, nomes de arquivos padronizados, indentação e legibilidade do código."),
        ],
    },
    "teste": {
        "titulo": "Teste escrito-prático (15 pts) — modelo (S)",
        "instrucoes": [
            "Prova individual, sem consulta. Duração: 1 aula (50 min).",
            "Parte A: 6 questões objetivas (1 pt cada). Parte B: 3 questões práticas (3 pts cada).",
            "Nas questões de código, escreva com clareza; indentação e legibilidade também são avaliadas.",
        ],
        "parte_a": {
            "titulo": "Parte A — questões objetivas (1 pt cada)",
            "questoes": [
                {"enunciado": "A Web (World Wide Web) é:",
                 "alt": ["sinônimo de Internet.",
                         "a infraestrutura física de cabos e servidores.",
                         "um dos serviços que funcionam sobre a Internet, formado por páginas interligadas.",
                         "um protocolo de criptografia de dados."],
                 "resposta": 2, "comentario": "A Web é um serviço sobre a Internet; e-mail, streaming etc. são outros serviços."},
                {"enunciado": "Na URL https://loja.com.br/produtos/tv.php?cor=preta, o trecho “?cor=preta” é:",
                 "alt": ["o protocolo.", "o domínio.", "o caminho.", "um parâmetro enviado à página."],
                 "resposta": 3, "comentario": "Parâmetros vêm após ? no formato nome=valor."},
                {"enunciado": "A função do DNS é:",
                 "alt": ["criptografar a conexão HTTPS.",
                         "traduzir nomes de domínio em endereços IP.",
                         "hospedar os arquivos do site.",
                         "exibir as páginas no navegador."],
                 "resposta": 1, "comentario": "DNS converte nome (loja.com.br) em IP do servidor."},
                {"enunciado": "Qual grupo tem apenas elementos HTML semânticos de formatação?",
                 "alt": ["b, i, font", "strong, em, mark", "div, span, p", "table, tr, td"],
                 "resposta": 1, "comentario": "strong/em/mark carregam significado; b/i são apenas aparência."},
                {"enunciado": "Para uma célula de tabela ocupar 2 colunas, usa-se:",
                 "alt": ["rowspan=\"2\"", "colspan=\"2\"", "span=\"2\"", "merge=\"2\""],
                 "resposta": 1, "comentario": "colspan mescla colunas; rowspan mesclaria linhas."},
                {"enunciado": "Em um formulário, o atributo que identifica o campo no processamento pelo servidor é:",
                 "alt": ["id", "class", "name", "for"],
                 "resposta": 2, "comentario": "name é a chave usada pelo PHP ($_POST/$_GET); id é para label/CSS."},
            ],
        },
        "parte_b": {
            "titulo": "Parte B — questões práticas (3 pts cada)",
            "questoes": [
                {
                    "tipo": "escrever_codigo",
                    "enunciado": "Escreva o código HTML5 completo de uma página chamada “Cursos da Escola” que contenha: "
                                 "título principal (h1) “Cursos Técnicos”, um parágrafo com a palavra “gratuitos” em "
                                 "strong, uma lista não ordenada com os 3 cursos (Informática, Redes, Administração) e "
                                 "uma imagem cursos.jpg (pasta imagens/) com texto alternativo adequado.",
                    "resposta_codigo": [
                        "<!DOCTYPE html>",
                        "<html lang=\"pt-br\">",
                        "<head>",
                        "    <meta charset=\"UTF-8\">",
                        "    <title>Cursos da Escola</title>",
                        "</head>",
                        "<body>",
                        "    <h1>Cursos Técnicos</h1>",
                        "    <p>Nossos cursos são <strong>gratuitos</strong>.</p>",
                        "    <ul>",
                        "        <li>Informática</li>",
                        "        <li>Redes</li>",
                        "        <li>Administração</li>",
                        "    </ul>",
                        "    <img src=\"imagens/cursos.jpg\" alt=\"Alunos nos cursos técnicos\">",
                        "</body>",
                        "</html>",
                    ],
                    "criterio": "Estrutura completa (0,5) · h1 e parágrafo com strong (0,75) · ul/li com os 3 itens (0,75) · "
                                "img com caminho relativo e alt descritivo (1,0).",
                },
                {
                    "tipo": "corrigir_codigo",
                    "enunciado": "O código abaixo contém 4 erros. Reescreva-o corrigido e sublinhe/numere as correções: "
                                 "(código: <html> sem DOCTYPE e sem lang; <p>Texto com <strong>importante</p></strong>; "
                                 "<h1>Título</h3>; <a src=\"sobre.html\">Sobre</a>)",
                    "resposta_codigo": [
                        "<!DOCTYPE html>",
                        "<html lang=\"pt-br\">",
                        "<head><meta charset=\"UTF-8\"><title>Teste</title></head>",
                        "<body>",
                        "    <h1>Título</h1>",
                        "    <p>Texto com <strong>importante</strong>.</p>",
                        "    <a href=\"sobre.html\">Sobre</a>",
                        "</body>",
                        "</html>",
                    ],
                    "criterio": "Cada correção vale 0,75: 1) DOCTYPE (+lang/charset); 2) strong/p descruzados; "
                                "3) h1 fechado com /h1; 4) href em vez de src no link.",
                },
                {
                    "tipo": "construir",
                    "enunciado": "Construa (a) uma tabela 3×3 com cabeçalho (th) “Produto, Preço, Estoque”, uma linha de "
                                 "dados (Mouse, 25.00, 10) e um tfoot com “Total de itens” ocupando 2 colunas (colspan) "
                                 "e o valor 10; e (b) um formulário com campo de e-mail (obrigatório), um select “Turno” "
                                 "(Manhã/Tarde/Noite) e botão de envio.",
                    "resposta_codigo": [
                        "<table border=\"1\">",
                        "  <thead><tr><th>Produto</th><th>Preço</th><th>Estoque</th></tr></thead>",
                        "  <tbody><tr><td>Mouse</td><td>25.00</td><td>10</td></tr></tbody>",
                        "  <tfoot><tr><td colspan=\"2\">Total de itens</td><td>10</td></tr></tfoot>",
                        "</table>",
                        "",
                        "<form action=\"processar.php\" method=\"post\">",
                        "  <label for=\"email\">E-mail:</label>",
                        "  <input type=\"email\" id=\"email\" name=\"email\" required>",
                        "  <label for=\"turno\">Turno:</label>",
                        "  <select id=\"turno\" name=\"turno\">",
                        "    <option value=\"manha\">Manhã</option>",
                        "    <option value=\"tarde\">Tarde</option>",
                        "    <option value=\"noite\">Noite</option>",
                        "  </select>",
                        "  <button type=\"submit\">Enviar</button>",
                        "</form>",
                    ],
                    "criterio": "Tabela: thead/th (0,5) · tbody correto (0,5) · tfoot com colspan=2 (0,5). "
                                "Formulário: type=email + required (0,5) · label/for (0,25) · select com 3 options (0,5) · "
                                "button submit + action/method (0,25).",
                },
            ],
        },
    },
}

# ---------------------------------------------------------------------------
# AVALIAÇÃO 2 — 30 pts (Semana 16, aula 48)
# ---------------------------------------------------------------------------
A2 = {
    "id": "A2",
    "titulo": "Avaliação 2 — prova de HTML + PHP (30 pts)",
    "periodo": "Semana 16 — aula 48 (S)",
    "composicao": [
        ("Prova obrigatória (pode ser em duplas ou com consulta — conforme o Plano de Ensino)", "30 pts",
         "60% prática (leitura/escrita de código) + 40% conceitual"),
    ],
    "teste": {
        "titulo": "Modelo de prova (S) — 10 questões × 3 pts",
        "instrucoes": [
            "Conteúdo: HTML (estrutura a formulários), PHP (variáveis a arrays/funções) e GET/POST/validação.",
            "Modalidade definida pelo professor conforme o Plano de Ensino (duplas e/ou consulta permitidos).",
            "Questões 1–4: conceituais. Questões 5–10: práticas (prever saída, corrigir e escrever código).",
            "Duração sugerida: 2 aulas (100 min).",
        ],
        "questoes": [
            # ---- Conceituais (4 × 3 = 12 pts) ----
            {"tipo": "objetiva",
             "enunciado": "Sobre HTML e PHP, é correto afirmar:",
             "alt": ["HTML é processado no servidor e PHP no navegador.",
                     "HTML estrutura o conteúdo no navegador; PHP executa lógica no servidor e gera HTML.",
                     "Ambos são linguagens de programação com variáveis e decisões.",
                     "PHP substitui o HTML: páginas PHP não contêm HTML."],
             "resposta": 1,
             "comentario": "HTML = marcação interpretada no navegador; PHP = programação executada no servidor, "
                           "que gera HTML como resposta."},
            {"tipo": "objetiva",
             "enunciado": "Para enviar um formulário de cadastro com senha, o método e a leitura corretos são:",
             "alt": ["method=get, lido com $_GET — dados aparecem na URL.",
                     "method=post, lido com $_POST — dados viajam no corpo da requisição.",
                     "method=submit, lido com $_FORM.",
                     "method=get, lido com $_POST."],
             "resposta": 1,
             "comentario": "Dados sensíveis (senha) → POST; o PHP lê no array $_POST pela chave name do campo."},
            {"tipo": "objetiva",
             "enunciado": "O padrão seguro para receber dados de um formulário em PHP é:",
             "alt": ["usar $_POST diretamente no echo, sem verificações.",
                     "confiar no required do HTML e dispensar validação no servidor.",
                     "verificar com isset/empty, validar as regras e exibir com htmlspecialchars.",
                     "criptografar a URL com GET."],
             "resposta": 2,
             "comentario": "Validação no servidor (isset/empty + regras) + sanitização na saída "
                           "(htmlspecialchars) — required do HTML pode ser contornado."},
            {"tipo": "objetiva",
             "enunciado": "Sobre include e funções, é correto afirmar:",
             "alt": ["include serve para reutilizar partes de página (ex.: cabeçalho); funções reutilizam lógica com parâmetros e retorno.",
                     "include e function são sinônimos em PHP.",
                     "funções não podem receber parâmetros.",
                     "require emite apenas aviso se o arquivo não existir."],
             "resposta": 0,
             "comentario": "include/require reutilizam trechos de código/página; function define lógica nomeada "
                           "com parâmetros e return. require gera erro FATAL se faltar o arquivo."},
            # ---- Práticas (6 × 3 = 18 pts) ----
            {"tipo": "prever_saida",
             "enunciado": "Qual é a saída exibida pelo código abaixo?",
             "codigo": [
                "<?php",
                "    $notas = [7.0, 5.5, 9.0];",
                "    $soma = 0;",
                "    foreach ($notas as $n) {",
                "        if ($n >= 7) {",
                "            $soma += $n;",
                "        }",
                "    }",
                "    echo \"Soma: $soma\";",
                "?>",
             ],
             "resposta_texto": "Soma: 16 — apenas 7.0 e 9.0 passam na condição (5.5 é ignorado).",
             "criterio": "Resultado 16 (2 pts) + justificativa do filtro (1 pt)."},
            {"tipo": "prever_saida",
             "enunciado": "O que aparece na tela? Explique a diferença entre as duas comparações.",
             "codigo": [
                "<?php",
                "    $a = 10;",
                "    $b = \"10\";",
                "    if ($a == $b)  { echo \"iguais \"; }",
                "    if ($a === $b) { echo \"identicos\"; } else { echo \"nao identicos\"; }",
                "?>",
             ],
             "resposta_texto": "Saída: “iguais nao identicos” — == compara valor (10 = “10” → true); === "
                               "compara valor E tipo (integer × string → false).",
             "criterio": "Saída exata (1,5 pt) + explicação == × === (1,5 pt)."},
            {"tipo": "corrigir_codigo",
             "enunciado": "O programa abaixo deveria exibir a tabuada do 4 (4 x 1 = 4 ... 4 x 10 = 40), mas tem "
                          "2 erros. Reescreva-o corrigido.",
             "codigo": [
                "<?php",
                "    $n = 4",
                "    for ($i = 1; $i <= 10; $i++) {",
                "        echo \"$n x $i = \" . $n * $i . \"<br>\"",
                "    }",
                "?>",
             ],
             "resposta_texto": "Faltam os ponto e vírgula: após $n = 4 e após o echo dentro do for.",
             "resposta_codigo": [
                "<?php",
                "    $n = 4;",
                "    for ($i = 1; $i <= 10; $i++) {",
                "        echo \"$n x $i = \" . ($n * $i) . \"<br>\";",
                "    }",
                "?>",
             ],
             "criterio": "1,5 pt por ponto e vírgula corrigido. Parênteses na multiplicação são opcionais "
                         "(precedência correta), mas recomendados."},
            {"tipo": "escrever_codigo",
             "enunciado": "Escreva uma função PHP chamada situacao($media) que retorne “Aprovado” se a média for "
                          "≥ 7, “Recuperação” se ≥ 5 e “Reprovado” caso contrário. Em seguida, chame a função com "
                          "$media = 6.5 e exiba o resultado.",
             "resposta_codigo": [
                "<?php",
                "    function situacao($media) {",
                "        if ($media >= 7) {",
                "            return \"Aprovado\";",
                "        } elseif ($media >= 5) {",
                "            return \"Recuperação\";",
                "        } else {",
                "            return \"Reprovado\";",
                "        }",
                "    }",
                "    $media = 6.5;",
                "    echo situacao($media);   // Recuperação",
                "?>",
             ],
             "criterio": "function com parâmetro (0,5) · 3 ramificações corretas na ordem certa (1,5) · "
                         "return (não echo) dentro da função (0,5) · chamada e exibição (0,5)."},
            {"tipo": "escrever_codigo",
             "enunciado": "Dado o array associativo multidimensional abaixo, escreva o código que percorre os "
                          "alunos com foreach e exibe, para cada um, uma linha “Nome — Curso”, usando "
                          "htmlspecialchars na saída.",
             "codigo": [
                "$alunos = [",
                "    [\"nome\" => \"Ana\",   \"curso\" => \"Informática\"],",
                "    [\"nome\" => \"Bruno\", \"curso\" => \"Redes\"],",
                "];",
             ],
             "resposta_codigo": [
                "<?php",
                "    foreach ($alunos as $aluno) {",
                "        echo htmlspecialchars($aluno[\"nome\"]) . \" — \"",
                "           . htmlspecialchars($aluno[\"curso\"]) . \"<br>\";",
                "    }",
                "?>",
             ],
             "criterio": "foreach correto (1,0) · acesso por chave (0,5) · htmlspecialchars nos dois campos "
                         "(1,0) · formatação da linha (0,5)."},
            {"tipo": "escrever_codigo",
             "enunciado": "Escreva o PHP de processar.php que: (a) recebe por POST os campos nome e idade; "
                          "(b) valida — nome obrigatório (empty) e idade entre 10 e 120; (c) em caso de erro, "
                          "exibe as mensagens e um link para voltar; (d) se válido, exibe a confirmação "
                          "sanitizada “Cadastro de NOME (IDADE anos) realizado!”.",
             "resposta_codigo": [
                "<?php",
                "    $erros = [];",
                "",
                "    if (empty($_POST[\"nome\"])) {",
                "        $erros[] = \"Nome é obrigatório.\";",
                "    }",
                "    $idade = isset($_POST[\"idade\"]) ? (int) $_POST[\"idade\"] : 0;",
                "    if ($idade < 10 || $idade > 120) {",
                "        $erros[] = \"Idade deve estar entre 10 e 120.\";",
                "    }",
                "",
                "    if (count($erros) > 0) {",
                "        foreach ($erros as $e) {",
                "            echo \"<p>$e</p>\";",
                "        }",
                "        echo '<a href=\"cadastro.html\">Voltar</a>';",
                "        exit;",
                "    }",
                "",
                "    $nome = htmlspecialchars($_POST[\"nome\"]);",
                "    echo \"Cadastro de $nome ($idade anos) realizado!\";",
                "?>",
             ],
             "criterio": "Leitura de $_POST (0,5) · validação nome (0,5) · validação faixa de idade (0,5) · "
                         "mensagens + link voltar + exit (0,75) · sanitização e confirmação (0,75). "
                         "Soluções equivalentes (if/else sem array $erros) recebem nota integral se cumprirem os requisitos."},
        ],
    },
}

# ---------------------------------------------------------------------------
# AVALIAÇÃO 3 — 40 pts (Semana 24)
# ---------------------------------------------------------------------------
A3 = {
    "id": "A3",
    "titulo": "Avaliação 3 — prova final + projeto (40 pts)",
    "periodo": "Semanas 20 a 24 (prova nas aulas 70–71 — S; projeto e apresentação na aula 72)",
    "composicao": [
        ("Prova escrita final individual e cumulativa (obrigatória — Plano de Ensino)", "30 pts", "Aulas 70–71 (S)"),
        ("Projeto integrador: entregas parciais + apresentação final (critério do professor)", "10 pts", "Aula 72"),
    ],
    "teste": {
        "titulo": "Modelo de prova final (S) — 10 questões × 3 pts — cumulativa",
        "instrucoes": [
            "Prova individual, sem consulta, cobrindo TODA a ementa (Web, HTML, PHP, formulários, projeto).",
            "Duração: 1 a 2 aulas (a definir pelo professor).",
            "Questões 1–5: objetivas/conceituais. Questões 6–10: práticas (prever, corrigir, escrever).",
        ],
        "questoes": [
            {"tipo": "objetiva",
             "enunciado": "O ciclo de funcionamento da Web é:",
             "alt": ["resposta → requisição → processamento.",
                     "requisição do navegador → processamento no servidor → resposta em HTML.",
                     "processamento no navegador → requisição ao DNS → resposta do cliente.",
                     "requisição do servidor → resposta do navegador → exibição."],
             "resposta": 1,
             "comentario": "Cliente requisita (HTTP), servidor processa (ex.: PHP) e responde com o HTML que o "
                           "navegador exibe."},
            {"tipo": "objetiva",
             "enunciado": "Para exibir dados enviados pelo usuário com segurança contra XSS, usa-se:",
             "alt": ["str_repeat()", "htmlspecialchars()", "count()", "var_dump()"],
             "resposta": 1,
             "comentario": "htmlspecialchars converte <, >, & e aspas em entidades: o dado vira texto "
                           "inofensivo na saída."},
            {"tipo": "objetiva",
             "enunciado": "Sobre laços de repetição em PHP:",
             "alt": ["while executa o bloco pelo menos uma vez sempre.",
                     "for só funciona com arrays.",
                     "do...while testa a condição após executar o bloco (mínimo 1 execução).",
                     "foreach requer contador manual ($i++)."],
             "resposta": 2,
             "comentario": "do...while = executa e depois testa. while pode executar 0 vezes; for usa contador "
                           "para N voltas conhecidas; foreach percorre arrays sem contador manual."},
            {"tipo": "objetiva",
             "enunciado": "A estrutura de projeto recomendada no curso organiza os arquivos assim:",
             "alt": ["todos os arquivos soltos na raiz, com nomes longos e descritivos.",
                     "páginas na raiz (index, cadastro, processar, listar) + pastas css/, imagens/ e includes/.",
                     "um único arquivo com todo o código do sistema.",
                     "cada página em uma pasta própria, com cópias do cabeçalho."],
             "resposta": 1,
             "comentario": "Padrão do módulo 10: páginas principais na raiz + pastas por tipo de arquivo; "
                           "includes/ centraliza cabeçalho/rodapé reutilizáveis."},
            {"tipo": "objetiva",
             "enunciado": "Na tabela de testes de um sistema, os ‘casos de limite’ verificam:",
             "alt": ["a velocidade de carregamento das páginas.",
                     "o comportamento exatamente nas bordas das regras de validação (ex.: valor mínimo e máximo).",
                     "se o layout funciona em celulares.",
                     "se o DNS resolve o domínio corretamente."],
             "resposta": 1,
             "comentario": "Limites/bordas (mínimo, máximo, um além) revelam erros de condição (>= vs >) — "
                           "conteúdo das aulas 58 e 59."},
            {"tipo": "prever_saida",
             "enunciado": "Qual é a saída do código?",
             "codigo": [
                "<?php",
                "    $precos = [10, 25, 5];",
                "    $maior = 0;",
                "    foreach ($precos as $p) {",
                "        if ($p > $maior) {",
                "            $maior = $p;",
                "        }",
                "    }",
                "    echo \"Maior preço: $maior\";",
                "    echo \"<br>Total: \" . count($precos);",
                "?>",
             ],
             "resposta_texto": "Maior preço: 25 · Total: 3",
             "criterio": "Cada linha correta: 1,5 pt."},
            {"tipo": "prever_saida",
             "enunciado": "O que o switch abaixo exibe? Explique.",
             "codigo": [
                "<?php",
                "    $opcao = 2;",
                "    switch ($opcao) {",
                "        case 1:",
                "            echo \"Um \";",
                "        case 2:",
                "            echo \"Dois \";",
                "        case 3:",
                "            echo \"Tres \";",
                "            break;",
                "        default:",
                "            echo \"Outro\";",
                "    }",
                "?>",
             ],
             "resposta_texto": "“Dois Tres” — faltam breaks nos cases 1 e 2: ao bater no case 2, a cascata "
                               "continua executando o case 3 até encontrar o break.",
             "criterio": "Saída exata (1,5 pt) + explicação da cascata por falta de break (1,5 pt)."},
            {"tipo": "corrigir_codigo",
             "enunciado": "O código deveria gerar uma tabela HTML com os nomes do array, mas tem 3 erros "
                          "(sintaxe, lógica e segurança). Corrija-os.",
             "codigo": [
                "<?php",
                "    $nomes = [\"Ana\", \"Bruno\"]",
                "    echo \"<table>\";",
                "    foreach ($nomes as $nome) {",
                "        echo \"<tr><td>\" . $nome . \"</td></tr>\";",
                "    }",
                "    echo \"<tr><td>Total: \" . count($nomes) + 1 . \"</td></tr>\";",
                "?>",
             ],
             "resposta_codigo": [
                "<?php",
                "    $nomes = [\"Ana\", \"Bruno\"];              // 1) ; após o array",
                "    echo \"<table>\";",
                "    foreach ($nomes as $nome) {",
                "        echo \"<tr><td>\" . htmlspecialchars($nome) . \"</td></tr>\";  // 3) sanitizar",
                "    }",
                "    echo \"<tr><td>Total: \" . (count($nomes)) . \"</td></tr>\";      // 2) sem + 1",
                "    echo \"</table>\";                          // (bônus) fechar a tabela",
                "?>",
             ],
             "criterio": "1 pt por erro corrigido: sintaxe (;), lógica (+1 indevido no total), segurança "
                         "(htmlspecialchars). Fechar </table> não pontua, mas deve ser elogiado."},
            {"tipo": "escrever_codigo",
             "enunciado": "Escreva um arquivo pagina.php que: inclua includes/cabecalho.php; declare a função "
                          "media($a, $b) que retorna a média; chame a função com 7.5 e 9.0 guardando em $resultado; "
                          "e exiba “Média: X” dentro de um parágrafo HTML. Finalize incluindo includes/rodape.php.",
             "resposta_codigo": [
                "<?php include \"includes/cabecalho.php\"; ?>",
                "<?php",
                "    function media($a, $b) {",
                "        return ($a + $b) / 2;",
                "    }",
                "    $resultado = media(7.5, 9.0);",
                "?>",
                "<p>Média: <?= $resultado ?></p>",
                "<?php include \"includes/rodape.php\"; ?>",
             ],
             "criterio": "include do cabeçalho (0,5) · função com return correto (1,0) · chamada guardando em "
                         "$resultado (0,5) · exibição em <p> com echo/<?= (0,5) · include do rodapé (0,5)."},
            {"tipo": "escrever_codigo",
             "enunciado": "Escreva o HTML de um formulário de busca de produtos que envie por GET para "
                          "buscar.php, com: campo texto name=produto (obrigatório), select name=categoria "
                          "(Todas/Eletrônicos/Livros) e botão “Buscar”. Em seguida, escreva o PHP de buscar.php "
                          "que lê e exibe (sanitizado) “Buscando PRODUTO na categoria CATEGORIA”, tratando "
                          "campo vazio com mensagem de erro.",
             "resposta_codigo": [
                "<!-- buscar.html -->",
                "<form action=\"buscar.php\" method=\"get\">",
                "    <label for=\"produto\">Produto:</label>",
                "    <input type=\"text\" id=\"produto\" name=\"produto\" required>",
                "    <label for=\"categoria\">Categoria:</label>",
                "    <select id=\"categoria\" name=\"categoria\">",
                "        <option value=\"todas\">Todas</option>",
                "        <option value=\"eletronicos\">Eletrônicos</option>",
                "        <option value=\"livros\">Livros</option>",
                "    </select>",
                "    <button type=\"submit\">Buscar</button>",
                "</form>",
                "",
                "<!-- buscar.php -->",
                "<?php",
                "    if (empty($_GET[\"produto\"])) {",
                "        echo \"Erro: informe o produto.\";",
                "        exit;",
                "    }",
                "    $produto = htmlspecialchars($_GET[\"produto\"]);",
                "    $categoria = htmlspecialchars($_GET[\"categoria\"] ?? \"todas\");",
                "    echo \"Buscando $produto na categoria $categoria\";",
                "?>",
             ],
             "criterio": "HTML: form get/action (0,5) · input name+required (0,5) · select com options (0,5) · "
                         "button (0,25). PHP: leitura $_GET (0,5) · validação empty + exit (0,5) · "
                         "htmlspecialchars (0,5) · mensagem final (0,25)."},
        ],
    },
    "projeto_rubrica": {
        "titulo": "Rubrica do projeto e apresentação (10 pts — critério do professor)",
        "itens": PROJETO_FINAL["criterios_10pts"],
        "observacoes": [
            "As entregas parciais (1 a 5) alimentam a nota de funcionalidade e organização — acompanhe com vistos.",
            "Na apresentação (aula 72), o grupo deve demonstrar: cadastro válido, tentativa inválida (mensagens "
            "de erro) e listagem dinâmica.",
            "Sugestão: plateia registra uma pergunta por grupo; respostas também compõem a avaliação da "
            "apresentação.",
        ],
    },
}

# Mapa de referências usadas pelos módulos (avaliacao_ref)
REFERENCIAS = {"A1": A1, "A2": A2, "A3": A3, "A1-teste": A1}
