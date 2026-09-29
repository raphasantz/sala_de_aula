# -*- coding: utf-8 -*-
"""Módulos 6 a 9 — Parte III: Introdução ao PHP."""

MODULO_6 = {
    "num": 6,
    "titulo": "Introdução ao PHP",
    "parte_num": 3,
    "parte_titulo": "Introdução ao PHP",
    "aulas_faixa": "Aulas 19 a 21",
    "semanas": "Semana 7",
    "objetivos": [
        "Explicar o que é PHP e diferenciá-lo do HTML (servidor × navegador).",
        "Configurar o ambiente com servidor local (XAMPP ou similar).",
        "Escrever e executar o primeiro programa PHP (echo, blocos <?php ?>).",
        "Misturar HTML e PHP no mesmo arquivo para gerar conteúdo dinâmico.",
    ],
    "aulas": [
        {
            "num": 19,
            "titulo": "O que é PHP?",
            "blocos": [
                ("h", "Uma linguagem do lado do servidor"),
                ("p", "<b>PHP</b> (PHP: Hypertext Preprocessor) é uma <b>linguagem de programação</b> criada para "
                      "a Web. Diferente do HTML — que é interpretado no <b>navegador</b> —, o código PHP é "
                      "executado no <b>servidor</b>: lá ele faz cálculos, toma decisões, lê formulários e "
                      "<b>gera HTML</b>, que então é enviado pronto ao navegador."),
                ("conceito", ("HTML × PHP — quem faz o quê?",
                              "<b>HTML</b>: estrutura o conteúdo; processado/exibido no <b>navegador</b> "
                              "(lado do cliente); o resultado é sempre o mesmo para todos. <b>PHP</b>: executa "
                              "lógica; processado no <b>servidor</b> (lado do servidor); o resultado pode mudar "
                              "a cada acesso (conteúdo <b>dinâmico</b>): hora atual, dados do usuário, "
                              "registros de um banco...")),
                ("codigo", {"titulo": "O fluxo com PHP", "ling": "texto", "linhas": [
                    "NAVEGADOR (cliente)              SERVIDOR",
                    "     │                             │",
                    "     │── requisicao: pagina.php ──▶│",
                    "     │                             │ 1. interpreta o PHP",
                    "     │                             │ 2. executa a lógica",
                    "     │                             │ 3. gera HTML",
                    "     │◀─── resposta: HTML puro ────│",
                    "     │                             │",
                    "  exibe a página",
                ]}),
                ("h", "Configuração: servidor local"),
                ("p", "Para executar PHP no computador do laboratório, instalamos um <b>pacote com servidor "
                      "Web + PHP</b> (sugestão: <b>XAMPP</b>, gratuito). Após instalar:"),
                ("lista_num", [
                    "Abra o painel do XAMPP e <b>inicie o Apache</b> (o servidor Web);",
                    "Coloque a pasta do projeto dentro de <b>htdocs/</b> (pasta que o Apache publica);",
                    "Acesse pelo navegador: <b>http://localhost/meu-site/arquivo.php</b>.",
                ]),
                ("atencao", "Arquivo <b>.php</b> aberto com dois cliques (file://) <b>não executa</b> o PHP — o "
                            "navegador mostra o código ou uma página em branco. PHP só roda passando pelo "
                            "servidor: <b>http://localhost/...</b>."),
                ("h", "O que dá para fazer com PHP"),
                ("lista", [
                    "Gerar <b>conteúdo dinâmico</b> (data/hora, saudações personalizadas, listas de dados);",
                    "<b>Receber e processar formulários</b> (cadastros, logins, buscas — módulo 11);",
                    "Tomar <b>decisões</b> e <b>repetir</b> tarefas (módulos 8 e 9);",
                    "Guardar dados em <b>bancos de dados</b> (Programação para Internet II);",
                    "Grandes sites usam/ usaram PHP: Wikipédia, WordPress, Facebook (no início)...",
                ]),
            ],
            "slides": {
                "pontos": [
                    "PHP = linguagem de programação do lado do SERVIDOR",
                    "HTML: navegador exibe (estático) · PHP: servidor processa e gera HTML (dinâmico)",
                    "Fluxo: requisição → servidor executa PHP → resposta em HTML",
                    "Ambiente: XAMPP → Apache iniciado → projeto em htdocs/",
                    "Acesso: http://localhost/meu-site/pagina.php",
                ],
                "nota": "Demonstração visual HTML × PHP: abrir um .html com dois cliques (funciona) e um .php "
                        "com dois cliques (não funciona) — depois via localhost (funciona). Esse contraste fixa "
                        "o conceito de servidor.",
            },
        },
        {
            "num": 20,
            "titulo": "Primeiro programa PHP",
            "blocos": [
                ("h", "Blocos PHP, echo e ponto e vírgula"),
                ("p", "O código PHP vive dentro de <b>blocos</b> <b>&lt;?php ... ?&gt;</b>. O comando "
                      "<b>echo</b> envia texto para a página. Toda instrução termina com <b>ponto e vírgula "
                      "(;)</b> — esquecê-lo é o erro mais comum de iniciante!"),
                ("codigo", {"titulo": "ola.php — o primeiro programa", "ling": "php", "linhas": [
                    "<?php",
                    "    // comentário de uma linha (igual em muitas linguagens)",
                    "    echo \"Olá, mundo!\";",
                    "    echo \"<br>\";              // posso enviar HTML pelo echo",
                    "    echo \"Meu nome é PHP e rodo no servidor.\";",
                    "?>",
                ]}),
                ("p", "Salve como <b>ola.php</b> em <b>htdocs/meu-site/</b> e acesse "
                      "<b>http://localhost/meu-site/ola.php</b>. Resultado na tela: “Olá, mundo! Meu nome é PHP "
                      "e rodo no servidor.”"),
                ("h", "Regras básicas da sintaxe"),
                ("lista", [
                    "Blocos: <b>&lt;?php</b> abre e <b>?&gt;</b> fecha (o fechamento é opcional em arquivos "
                    "só com PHP);",
                    "Instruções terminam com <b>;</b>",
                    "Texto (string) vai entre <b>aspas duplas</b> \"...\" ou simples '...';",
                    "Comentários: <b>//</b> (uma linha) ou <b>/* ... */</b> (várias linhas);",
                    "PHP diferencia maiúsculas/minúsculas em <b>variáveis</b> ($nome ≠ $Nome), mas não em "
                    "<b>palavras-chave</b> (echo = ECHO).",
                ]),
                ("dica", "Para “ver” o que o servidor fez, use <b>Ctrl+U</b> (exibir código-fonte) no navegador: "
                         "você verá apenas o <b>HTML gerado</b> — o código PHP nunca chega ao cliente. Isso "
                         "prova que ele foi executado no servidor."),
                ("atencao", "Erros de sintaxe (como esquecer o ; ou fechar aspas) fazem o PHP exibir uma "
                            "mensagem de erro com o <b>arquivo e a linha</b>. Leia a mensagem: ela diz "
                            "exatamente onde está o problema — não tenha medo dela!"),
            ],
            "slides": {
                "pontos": [
                    "Bloco PHP: <?php ... ?>",
                    "echo \"texto\"; → envia conteúdo para a página",
                    "Toda instrução termina com ; (erro nº 1: esquecer!)",
                    "Strings entre aspas · comentários // e /* */",
                    "Ctrl+U no navegador mostra só o HTML gerado (nunca o PHP)",
                ],
                "codigo": {"titulo": "ola.php", "linhas": [
                    "<?php",
                    "    echo \"Olá, mundo!\";",
                    "    echo \"<br>\";",
                    "    echo \"PHP roda no servidor.\";",
                ]},
                "nota": "Todos devem executar o ola.php via localhost. Depois, Ctrl+U para ver que o PHP "
                        "'sumiu' — só sobrou HTML.",
            },
        },
        {
            "num": 21,
            "titulo": "PHP + HTML no mesmo arquivo",
            "blocos": [
                ("h", "Misturando as linguagens"),
                ("p", "Um arquivo <b>.php</b> pode conter <b>HTML normalmente</b> + <b>blocos PHP</b> "
                      "intercalados. O servidor executa os blocos PHP e entrega ao navegador um documento "
                      "HTML único:"),
                ("codigo", {"titulo": "pagina.php — HTML + PHP juntos", "ling": "php", "linhas": [
                    "<!DOCTYPE html>",
                    "<html lang=\"pt-br\">",
                    "<head>",
                    "    <meta charset=\"UTF-8\">",
                    "    <title>Página dinâmica</title>",
                    "</head>",
                    "<body>",
                    "    <h1>Bem-vindo ao meu site!</h1>",
                    "",
                    "    <?php",
                    "        echo \"<p>Hoje é dia \" . date(\"d/m/Y\") . \".</p>\";",
                    "        echo \"<p>Agora são \" . date(\"H:i\") . \" horas.</p>\";",
                    "    ?>",
                    "",
                    "    <p>Este parágrafo é HTML puro.</p>",
                    "</body>",
                    "</html>",
                ]}),
                ("conceito", ("Conteúdo dinâmico",
                              "A página acima muda <b>sozinha</b>: a data e a hora exibidas são as do momento do "
                              "acesso — calculadas pelo servidor. Isso é <b>conteúdo dinâmico</b>: o mesmo "
                              "arquivo gera resultados diferentes a cada execução. HTML puro nunca faria isso.")),
                ("h", "O operador de concatenação ( . )"),
                ("p", "Em PHP, o <b>ponto (.)</b> junta (concatena) textos: <b>\"Olá, \" . $nome</b>. No exemplo, "
                      "juntamos \"Hoje é dia \" com o resultado de <b>date(\"d/m/Y\")</b> e com \".\". A função "
                      "<b>date()</b> devolve a data formatada conforme o padrão informado (d = dia, m = mês, "
                      "Y = ano com 4 dígitos, H = hora, i = minuto)."),
                ("dica", "Também dá para escrever variáveis diretamente dentro de aspas duplas: "
                         "echo \"Olá, $nome!\"; — veremos isso no módulo 7."),
            ],
            "slides": {
                "pontos": [
                    "Arquivo .php = HTML normal + blocos <?php ?> intercalados",
                    "Servidor executa o PHP e entrega HTML pronto",
                    "Conteúdo dinâmico: o mesmo arquivo, resultados diferentes",
                    "date('d/m/Y') e date('H:i') — data e hora do servidor",
                    "Ponto (.) concatena textos no PHP",
                ],
                "codigo": {"titulo": "pagina.php", "linhas": [
                    "<h1>Bem-vindo!</h1>",
                    "<?php",
                    "  echo \"<p>Hoje é \" . date(\"d/m/Y\") . \".</p>\";",
                    "?>",
                    "<p>Isto é HTML puro.</p>",
                ]},
                "nota": "Atualizar a página várias vezes para ver os minutos mudando. Pergunta-chave: 'quem "
                        "calculou a data — o navegador ou o servidor?'",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Olá, mundo! em PHP", "tipo": "pratico",
            "enunciado": "Com o Apache iniciado e o projeto em htdocs/meu-site/, crie <b>ola.php</b> que exiba: "
                         "seu nome em um h1, um parágrafo dizendo por que você escolheu o curso e a data de hoje "
                         "(date).",
            "esperado": "Página acessível em http://localhost/meu-site/ola.php exibindo nome (h1), parágrafo e "
                        "data atual calculada pelo servidor.",
            "orientacao": "Verifique: bloco <?php correto, ponto e vírgula, concatenação com ponto. Faça-os dar "
                          "Ctrl+U para confirmar que só há HTML na resposta.",
        },
        {
            "num": 2, "titulo": "Cartão de visita dinâmico", "tipo": "pratico",
            "enunciado": "Crie <b>cartao.php</b> com a estrutura HTML5 completa e, no body, um bloco PHP que "
                         "gere dinamicamente: uma saudação conforme nada (apenas texto), a data e a hora "
                         "completas e uma mensagem com strong.",
            "esperado": "Documento .php misturando HTML e blocos PHP, exibindo data/hora do servidor e "
                        "formatação HTML enviada via echo.",
            "orientacao": "Reforce que echo pode conter tags HTML. Desafio: duas atualizações de página devem "
                          "mostrar horários diferentes.",
        },
        {
            "num": 3, "titulo": "O que o navegador recebe?", "tipo": "escrito",
            "enunciado": "Sem executar, escreva o HTML que o <b>navegador recebe</b> (saída) para o código "
                         "abaixo:",
            "codigo": {"titulo": "saida.php", "ling": "php", "linhas": [
                "<?php",
                "    echo \"<h2>Resultado</h2>\";",
                "    echo \"<p>\" . (10 + 5) . \"</p>\";",
                "    echo \"2\" . \"5\";",
                "?>",
            ]},
            "esperado": "&lt;h2&gt;Resultado&lt;/h2&gt;&lt;p&gt;15&lt;/p&gt;25 — na tela: título 'Resultado', "
                        "parágrafo '15' e o texto '25' (concatenação de strings, não soma!).",
            "orientacao": "Ponto-chave: (10+5) é soma = 15; \"2\".\"5\" é concatenação = 25. Discuta a "
                          "diferença antes de revelar.",
        },
    ],
    "teste_rapido": [
        {"enunciado": "O código PHP é executado:",
         "alt": ["no navegador do usuário.",
                 "no servidor Web, antes de a página ser enviada.",
                 "no editor de código, ao salvar o arquivo.",
                 "no sistema DNS."],
         "resposta": 1,
         "comentario": "PHP é server-side: o servidor executa e envia ao navegador apenas o HTML resultante."},
        {"enunciado": "O comando usado para exibir conteúdo na página em PHP é:",
         "alt": ["print-screen", "echo", "display", "show"],
         "resposta": 1,
         "comentario": "echo (e seu primo print) envia conteúdo para a resposta da página."},
        {"enunciado": "Um arquivo com PHP deve ter qual extensão e como deve ser acessado?",
         "alt": [".html, com dois cliques no arquivo.",
                 ".php, pelo endereço http://localhost/...",
                 ".php, com dois cliques no arquivo.",
                 ".txt, pelo bloco de notas."],
         "resposta": 1,
         "comentario": "Extensão .php e acesso via servidor (localhost). Com dois cliques (file://), o PHP não "
                       "é executado."},
        {"enunciado": "O que o comando <b>echo \"3\" . \"4\";</b> exibe?",
         "alt": ["7", "34", "3.4", "erro de sintaxe"],
         "resposta": 1,
         "comentario": "O ponto concatena strings: \"3\".\"4\" = \"34\". Soma seria com o operador + entre "
                       "números: 3+4 = 7."},
        {"enunciado": "Uma página mostra a data de hoje diferente a cada acesso, mesmo sendo o mesmo arquivo. "
                    "Isso acontece porque:",
         "alt": ["o navegador guarda datas aleatórias.",
                 "o HTML foi recompilado.",
                 "o PHP gera conteúdo dinâmico no servidor a cada requisição.",
                 "o DNS altera o conteúdo enviado."],
         "resposta": 2,
         "comentario": "Conteúdo dinâmico: a cada requisição o servidor executa o PHP (ex.: date()) e gera um "
                       "resultado atualizado."},
    ],
    "avaliacao_ref": None,
}

MODULO_7 = {
    "num": 7,
    "titulo": "PHP básico",
    "parte_num": 3,
    "parte_titulo": "Introdução ao PHP",
    "aulas_faixa": "Aulas 22 a 26",
    "semanas": "Semanas 8 e 9",
    "objetivos": [
        "Declarar e exibir variáveis em PHP.",
        "Identificar os tipos de dados (string, integer, float, boolean) e inspecioná-los com var_dump().",
        "Aplicar operadores aritméticos e de concatenação em expressões.",
        "Diferenciar operadores de comparação (== × ===).",
        "Combinar condições com operadores lógicos (&&, ||, !).",
    ],
    "aulas": [
        {
            "num": 22,
            "titulo": "Variáveis",
            "blocos": [
                ("h", "Declarando variáveis"),
                ("p", "Uma <b>variável</b> é um “espaço na memória com nome” para guardar dados que o programa "
                      "usa. Em PHP, toda variável começa com <b>cifrão ($)</b> e não precisa declarar o tipo — "
                      "o PHP descobre sozinho pelo valor atribuído:"),
                ("codigo", {"titulo": "variaveis.php", "ling": "php", "linhas": [
                    "<?php",
                    "    $nome = \"Maria\";          // atribuição de texto",
                    "    $idade = 17;               // número inteiro",
                    "    $altura = 1.65;            // número com casas decimais",
                    "",
                    "    echo $nome;                // exibe: Maria",
                    "    echo \"<br>\";",
                    "    echo \"Nome: $nome - Idade: $idade\";   // variável dentro de aspas duplas",
                    "?>",
                ]}),
                ("h", "Regras de nomes de variáveis"),
                ("lista", [
                    "Começam com <b>$</b>, seguidos de letra ou underscore: $nome, $_total;",
                    "<b>Não</b> podem começar com número nem conter acentos ou espaços: $2valores ✗, "
                    "$meu nome ✗;",
                    "Diferenciam maiúsculas: <b>$nota ≠ $Nota</b>;",
                    "Use nomes com significado: $precoFinal em vez de $x (boas práticas!).",
                ]),
                ("conceito", ("Atribuição × comparação",
                              "Um sinal de igual (<b>=</b>) <b>atribui</b>: $x = 5 guarda 5 em $x. "
                              "Dois/três iguais (<b>==</b>, <b>===</b>) <b>comparam</b>: $x == 5 pergunta se $x "
                              "vale 5. Confundir os dois é erro clássico — voltaremos nisso na aula 25.")),
                ("h", "Constantes"),
                ("p", "<b>Constantes</b> guardam valores que <b>não mudam</b> durante o programa. Define-se com "
                      "<b>define()</b> e usa-se sem $:"),
                ("codigo", {"titulo": "Constantes", "ling": "php", "linhas": [
                    "<?php",
                    "    define(\"PI\", 3.14159);",
                    "    define(\"ESCOLA\", \"Instituto Técnico\");",
                    "",
                    "    echo \"Escola: \" . ESCOLA . \"<br>\";",
                    "    echo \"Área do círculo (r=2): \" . PI * 2 * 2;",
                    "?>",
                ]}),
                ("dica", "Convenção: constantes em <b>MAIÚSCULAS</b> (PI, ESCOLA, TAXA_DESCONTO) — fica fácil "
                         "reconhecê-las no código."),
            ],
            "slides": {
                "pontos": [
                    "Variável: $nome = valor; (o $ sempre acompanha)",
                    "PHP descobre o tipo sozinho (dinâmico)",
                    "Nomes: sem número no início, sem acento, case-sensitive",
                    "= atribui · == / === comparam",
                    "Constantes: define('PI', 3.14); — MAIÚSCULAS, sem $",
                ],
                "codigo": {"titulo": "Variáveis e constantes", "linhas": [
                    "$nome = \"Maria\";",
                    "$idade = 17;",
                    "echo \"Nome: $nome - Idade: $idade\";",
                    "define(\"PI\", 3.14159);",
                    "echo PI * 2 * 2;",
                ]},
                "nota": "Experimentos no laboratório: criar variáveis com seus próprios dados e exibir. "
                        "Provocar erro de nome inválido ($2x) para ver a mensagem do PHP.",
            },
        },
        {
            "num": 23,
            "titulo": "Tipos de dados e var_dump()",
            "blocos": [
                ("h", "Os 4 tipos principais"),
                ("tabela", {"titulo": "Tipos de dados em PHP",
                            "cab": ["Tipo", "O que guarda", "Exemplos"],
                            "lin": [
                                ["string", "Texto (entre aspas)", "\"Maria\", 'PHP', \"123\""],
                                ["integer", "Número inteiro", "17, -5, 2026"],
                                ["float (double)", "Número com casas decimais", "1.65, 9.8, -0.5"],
                                ["boolean", "Verdadeiro ou falso (lógica)", "true, false"],
                            ]}),
                ("p", "Veremos também <b>arrays</b> (listas de valores) no módulo 9 — outro tipo fundamental."),
                ("h", "var_dump() — a lupa do programador"),
                ("p", "<b>var_dump()</b> mostra o <b>tipo</b> e o <b>valor</b> de uma variável. É a ferramenta "
                      "nº 1 para entender o que está guardado:"),
                ("codigo", {"titulo": "tipos.php", "ling": "php", "linhas": [
                    "<?php",
                    "    $nome = \"Maria\";",
                    "    $idade = 17;",
                    "    $altura = 1.65;",
                    "    $aprovado = true;",
                    "",
                    "    var_dump($nome);      // string(5) \"Maria\"",
                    "    echo \"<br>\";",
                    "    var_dump($idade);     // int(17)",
                    "    echo \"<br>\";",
                    "    var_dump($altura);    // float(1.65)",
                    "    echo \"<br>\";",
                    "    var_dump($aprovado);  // bool(true)",
                    "?>",
                ]}),
                ("atencao", "Cuidado: <b>\"17\"</b> (entre aspas) é <b>string</b>; <b>17</b> (sem aspas) é "
                            "<b>integer</b>. Parecem iguais na tela, mas o PHP os trata de forma diferente em "
                            "cálculos e comparações. Na dúvida: var_dump()."),
                ("h", "Booleanos na prática"),
                ("p", "Booleanos (true/false) são a base das <b>decisões</b> (módulo 8): toda condição — "
                      "$idade &gt;= 18, $nota &gt;= 7 — resulta em true ou false. No PHP, valores “vazios” "
                      "(0, \"\", null, false) são considerados falsos em condições."),
            ],
            "slides": {
                "pontos": [
                    "string 'texto' · integer 17 · float 1.65 · boolean true/false",
                    "var_dump($x) mostra tipo + valor — use sem dó!",
                    "'17' (string) ≠ 17 (integer)",
                    "Booleanos são a base das decisões (if)",
                    "Arrays vêm no módulo 9",
                ],
                "codigo": {"titulo": "Inspecionando tipos", "linhas": [
                    "$idade = 17;",
                    "var_dump($idade);   // int(17)",
                    "$texto = \"17\";",
                    "var_dump($texto);   // string(2) \"17\"",
                ]},
                "nota": "Atividade: cada aluno cria 4 variáveis (um de cada tipo) e confere com var_dump. "
                        "Pergunta provocadora: qual é o tipo de '17'?",
            },
        },
        {
            "num": 24,
            "titulo": "Operadores aritméticos e expressões",
            "blocos": [
                ("h", "Os operadores"),
                ("tabela", {"titulo": "Operadores aritméticos e de texto",
                            "cab": ["Operador", "Nome", "Exemplo", "Resultado"],
                            "lin": [
                                ["+", "adição", "7 + 2", "9"],
                                ["−", "subtração", "7 − 2", "5"],
                                ["*", "multiplicação", "7 * 2", "14"],
                                ["/", "divisão", "7 / 2", "3.5"],
                                ["%", "resto da divisão (módulo)", "7 % 2", "1"],
                                ["**", "potenciação", "7 ** 2", "49"],
                                [".", "concatenação (junta textos)", "\"7\" . \"2\"", "\"72\""],
                            ]}),
                ("h", "Expressões e precedência"),
                ("p", "Uma <b>expressão</b> combina valores e operadores e produz um resultado. Vale a ordem da "
                      "matemática: <b>parênteses</b> → <b>** </b> → <b>* / %</b> → <b>+ −</b>. Na dúvida, use "
                      "parênteses para deixar claro:"),
                ("codigo", {"titulo": "calculadora.php", "ling": "php", "linhas": [
                    "<?php",
                    "    $nota1 = 8.0;",
                    "    $nota2 = 6.5;",
                    "    $media = ($nota1 + $nota2) / 2;      // parênteses garantem a soma antes da divisão",
                    "",
                    "    echo \"Média: $media <br>\";          // 7.25",
                    "    echo \"Resto de 10 / 3: \" . (10 % 3); // 1",
                    "?>",
                ]}),
                ("conceito", ("O operador % (resto) é muito útil",
                              "O resto da divisão resolve problemas clássicos: <b>par ou ímpar</b> ($n % 2 == 0 "
                              "→ par), <b>é múltiplo?</b> ($n % 5 == 0 → múltiplo de 5), e cálculos de tempo "
                              "(90 minutos = 90/60 → 1 hora, resto 90%60 → 30 minutos).")),
                ("atencao", "Esta é a semana da <b>1ª Avaliação (A1 — 30 pts)</b>: entrega do trabalho HTML "
                            "(10 pts), atividades do AVA (5 pts) e <b>teste escrito-prático sobre Web e HTML "
                            "(15 pts)</b>. O modelo do teste está na seção Avaliações desta apostila — revise "
                            "os módulos 1 a 5!"),
            ],
            "slides": {
                "pontos": [
                    "+ − * / % ** e o ponto (.) de concatenação",
                    "% = resto da divisão (par/ímpar, múltiplos)",
                    "Precedência: () → ** → * / % → + −",
                    "Média: ($n1 + $n2) / 2 — parênteses importam!",
                    "⚠ Semana 8: AVALIAÇÃO 1 (30 pts) — rever módulos 1–5",
                ],
                "codigo": {"titulo": "Calculadora simples", "linhas": [
                    "$nota1 = 8.0; $nota2 = 6.5;",
                    "$media = ($nota1 + $nota2) / 2;",
                    "echo \"Média: $media\";   // 7.25",
                    "echo 10 % 3;             // 1 (resto)",
                ]},
                "nota": "Construir a calculadora passo a passo. Reforçar o lembrete da A1 e entregar o roteiro "
                        "de revisão (módulos 1 a 5).",
            },
        },
        {
            "num": 25,
            "titulo": "Operadores de comparação",
            "blocos": [
                ("h", "Comparando valores"),
                ("p", "Operadores de comparação <b>respondem perguntas</b> e sempre produzem um resultado "
                      "<b>booleano</b> (true ou false):"),
                ("tabela", {"titulo": "Operadores de comparação",
                            "cab": ["Operador", "Significado", "Exemplo", "Resultado"],
                            "lin": [
                                ["==", "igual (só o valor)", "5 == \"5\"", "true"],
                                ["===", "idêntico (valor E tipo)", "5 === \"5\"", "false"],
                                ["!=", "diferente (valor)", "5 != 3", "true"],
                                ["!==", "não idêntico (valor ou tipo)", "5 !== \"5\"", "true"],
                                ["&gt;", "&lt;", "&gt;=", "&lt;=", "maior, menor, maior/igual, menor/igual", "7 &gt;= 7", "true"],
                            ]}),
                ("h", "== × === : a diferença que derruba iniciantes"),
                ("codigo", {"titulo": "comparacao.php", "ling": "php", "linhas": [
                    "<?php",
                    "    $a = 5;        // integer",
                    "    $b = \"5\";      // string",
                    "",
                    "    var_dump($a == $b);    // bool(true)  — valores iguais",
                    "    echo \"<br>\";",
                    "    var_dump($a === $b);   // bool(false) — tipos diferentes!",
                    "?>",
                ]}),
                ("conceito", ("Regra prática",
                              "<b>==</b> compara apenas o <b>valor</b> (o PHP converte os tipos antes — "
                              "“5” vira 5). <b>===</b> compara <b>valor E tipo</b> (5 inteiro é diferente de "
                              "\"5\" texto). Em projetos reais, prefira <b>===</b>: evita surpresas.")),
                ("h", "Tabela-verdade das comparações"),
                ("codigo", {"titulo": "Complete mentalmente antes de executar", "ling": "php", "linhas": [
                    "10 > 3        // true        \"ana\" == \"Ana\"   // false (case-sensitive!)",
                    "10 >= 10      // true        7 != 7            // false",
                    "\"10\" === 10  // false       \"10\" == 10      // true",
                ]}),
                ("atencao", "Textos também são case-sensitive na comparação: <b>\"Ana\" == \"ana\"</b> é "
                            "<b>false</b>. E lembre: em condições, use == ou === — nunca = (que atribui!)."),
            ],
            "slides": {
                "pontos": [
                    "== igual (valor) · === idêntico (valor E tipo)",
                    "!= !== diferentes · > < >= <= tamanho",
                    "5 == '5' → true · 5 === '5' → false",
                    "Resultado é sempre boolean (true/false)",
                    "Textos: comparação diferencia maiúsculas ('Ana' ≠ 'ana')",
                ],
                "codigo": {"titulo": "== vs ===", "linhas": [
                    "$a = 5;  $b = \"5\";",
                    "var_dump($a == $b);   // true",
                    "var_dump($a === $b);  // false",
                ]},
                "nota": "Montar a tabela-verdade no quadro COM a turma (prever antes de executar) e depois "
                        "confirmar no projetor com var_dump. Jogo 'verdadeiro ou falso' com 8 comparações.",
            },
        },
        {
            "num": 26,
            "titulo": "Operadores lógicos",
            "blocos": [
                ("h", "Combinando condições"),
                ("p", "Operadores lógicos <b>combinam</b> comparações em condições compostas:"),
                ("tabela", {"titulo": "Operadores lógicos",
                            "cab": ["Operador", "Nome", "É true quando...", "Exemplo"],
                            "lin": [
                                ["&amp;&amp;", "E (and)", "os DOIS lados são true", "$idade &gt;= 18 &amp;&amp; $temCnh"],
                                ["||", "OU (or)", "pelo menos UM lado é true", "$dia == \"sab\" || $dia == \"dom\""],
                                ["!", "NÃO (not)", "inverte o valor", "!$chovendo (não está chovendo)"],
                            ]}),
                ("h", "Tabelas-verdade"),
                ("codigo", {"titulo": "&& (E) — só é true se tudo for true", "ling": "php", "linhas": [
                    "true  && true   →  true       false || false  →  false",
                    "true  && false  →  false      true  || false  →  true",
                    "false && true   →  false      false || true   →  true",
                    "false && false  →  false      true  || true   →  true",
                    "",
                    "!true  → false      !false → true",
                ]}),
                ("codigo", {"titulo": "condicoes.php — exemplo real", "ling": "php", "linhas": [
                    "<?php",
                    "    $idade = 17;",
                    "    $autorizado = false;",
                    "",
                    "    // pode entrar se: for maior de idade OU estiver acompanhado",
                    "    $podeEntrar = ($idade >= 18) || $autorizado;",
                    "    var_dump($podeEntrar);      // bool(false)",
                    "",
                    "    // aprovação: média >= 7 E frequência >= 75%",
                    "    $media = 8.0;  $freq = 80;",
                    "    $aprovado = ($media >= 7) && ($freq >= 75);",
                    "    var_dump($aprovado);        // bool(true)",
                    "?>",
                ]}),
                ("analogia", ("E × OU no dia a dia",
                              "<b>E (&&)</b>: “vou à festa se terminar a tarefa <b>e</b> meus pais deixarem” — "
                              "precisa dos dois. <b>OU (||)</b>: “posso pagar com Pix <b>ou</b> cartão” — "
                              "qualquer um serve. <b>NÃO (!)</b>: inverte — “não está chovendo”.")),
                ("dica", "Use <b>parênteses</b> em cada comparação: ($a &gt; $b) &amp;&amp; ($c == $d). Além de "
                         "evitar erros de precedência, o código fica muito mais legível."),
            ],
            "slides": {
                "pontos": [
                    "&& (E): true só se os dois lados forem true",
                    "|| (OU): true se pelo menos um lado for true",
                    "! (NÃO): inverte o valor lógico",
                    "Ex.: aprovado = ($media >= 7) && ($freq >= 75)",
                    "Parênteses em cada comparação = clareza + segurança",
                ],
                "codigo": {"titulo": "Condição composta", "linhas": [
                    "$media = 8.0; $freq = 80;",
                    "$aprovado = ($media >= 7) && ($freq >= 75);",
                    "var_dump($aprovado);  // true",
                ]},
                "nota": "Construir a tabela-verdade no quadro e fazer 'simulações humanas': dois alunos são "
                        "condições, a turma decide o resultado do && e do ||.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Laboratório de variáveis e tipos", "tipo": "pratico",
            "enunciado": "Crie <b>variaveis.php</b> com 4 variáveis sobre você: $nome (string), $idade "
                         "(integer), $altura (float) e $estuda (boolean = true). Exiba cada uma com echo em um "
                         "parágrafo e confirme os tipos com var_dump().",
            "esperado": "Saída com os 4 valores exibidos e var_dump mostrando string(N), int(), float() e "
                        "bool(true).",
            "orientacao": "Pergunte: 'o que aconteceria se colocasse a idade entre aspas?' — teste e compare.",
        },
        {
            "num": 2, "titulo": "Calculadora simples", "tipo": "pratico",
            "enunciado": "Crie <b>calculadora.php</b> com duas variáveis $a = 12 e $b = 5. Exiba, cada um em "
                         "uma linha: soma, subtração, multiplicação, divisão, resto (%) e a média.",
            "esperado": "17 · 7 · 60 · 2.4 · 2 · 8.5 — cada operação identificada com um texto.",
            "orientacao": "Confira o uso de parênteses na média e a concatenação com ponto. Desafio: converter "
                          "90 minutos em 'Xh Ymin' usando / e %.",
        },
        {
            "num": 3, "titulo": "Preveja a saída (== × ===)", "tipo": "escrito",
            "enunciado": "Sem executar, anote true ou false para cada expressão e depois confirme no PHP:",
            "passos": [
                "a) 10 == \"10\"   b) 10 === \"10\"   c) 7 != 8   d) \"abc\" === \"abc\"",
                "e) 5 > 3 && 2 > 4   f) 5 > 3 || 2 > 4   g) !(5 > 3)   h) (8 % 2 == 0) && true",
            ],
            "esperado": "a) true  b) false  c) true  d) true  e) false  f) true  g) false  h) true",
            "orientacao": "Correção comentada item a item. Os itens e/f/h consolidam tabelas-verdade; b "
                          "consolida ===.",
        },
        {
            "num": 4, "titulo": "Elegibilidade com condição composta", "tipo": "pratico",
            "enunciado": "Crie <b>eleicao.php</b>: variáveis $idade = 17 e $temTitulo = true. Com uma única "
                         "expressão lógica, defina $podeVotar = (idade &gt;= 16) &amp;&amp; $temTitulo e exiba o "
                         "resultado com uma mensagem amigável.",
            "esperado": "var_dump true (17 ≥ 16 e tem título) e mensagem do tipo 'Pode votar: 1'.",
            "orientacao": "Testar variações: idade 15 (false), sem título (false). Prepara o terreno para o if "
                          "(próximo módulo).",
        },
    ],
    "teste_rapido": [
        {"enunciado": "Qual é a forma correta de declarar uma variável em PHP?",
         "alt": ["nome = \"Ana\";", "var nome = \"Ana\";", "$nome = \"Ana\";", "string $nome = \"Ana\";"],
         "resposta": 2,
         "comentario": "Variáveis em PHP começam com $ e não exigem declaração de tipo."},
        {"enunciado": "O comando var_dump($x) serve para:",
         "alt": ["apagar a variável $x.",
                 "exibir o tipo e o valor da variável.",
                 "somar todos os valores guardados.",
                 "converter $x para string."],
         "resposta": 1,
         "comentario": "var_dump é a 'lupa' do programador: mostra tipo e valor, essencial para depurar."},
        {"enunciado": "Qual é o resultado de <b>10 % 3</b>?",
         "alt": ["3.33", "3", "1", "0"],
         "resposta": 2,
         "comentario": "% é o resto da divisão inteira: 10 ÷ 3 = 3 com resto 1."},
        {"enunciado": "O resultado de <b>5 === \"5\"</b> é:",
         "alt": ["true, pois os valores são iguais.",
                 "false, pois os tipos são diferentes (integer × string).",
                 "erro de sintaxe.",
                 "a string \"5\"."],
         "resposta": 1,
         "comentario": "=== exige valor E tipo idênticos. Com ==, o resultado seria true."},
        {"enunciado": "A expressão <b>(true && false) || true</b> resulta em:",
         "alt": ["true", "false", "null", "erro"],
         "resposta": 0,
         "comentario": "true && false = false; false || true = true. Parênteses primeiro, depois o ||."},
    ],
    "avaliacao_ref": "A1-teste",
}

MODULO_8 = {
    "num": 8,
    "titulo": "PHP – lógica (decisões)",
    "parte_num": 3,
    "parte_titulo": "Introdução ao PHP",
    "aulas_faixa": "Aulas 27 a 29",
    "semanas": "Semanas 9 e 10",
    "objetivos": [
        "Usar a estrutura if para executar blocos condicionais.",
        "Aplicar if/else/elseif para múltiplas condições (ex.: situação do aluno).",
        "Utilizar switch com case, break e default para menus de opções.",
        "Escolher a estrutura adequada (if × switch) para cada situação.",
    ],
    "aulas": [
        {
            "num": 27,
            "titulo": "Estrutura IF",
            "blocos": [
                ("h", "Decisões no programa"),
                ("p", "Programas tomam <b>decisões</b>: “se a nota for maior ou igual a 7, exibir aprovado”. "
                      "A estrutura <b>if</b> executa um bloco de código <b>somente se</b> a condição for "
                      "<b>true</b>:"),
                ("codigo", {"titulo": "Sintaxe e primeiro exemplo", "ling": "php", "linhas": [
                    "if (condição) {",
                    "    // comandos executados quando a condição é TRUE",
                    "}",
                    "",
                    "----------------------------------------------",
                    "",
                    "<?php",
                    "    $idade = 17;",
                    "",
                    "    if ($idade >= 18) {",
                    "        echo \"Pode tirar a carteira de motorista.\";",
                    "    }",
                    "    echo \"Fim do programa.\";   // sempre executa",
                    "?>",
                ]}),
                ("p", "Com $idade = 17, a condição (17 &gt;= 18) é <b>false</b>: o bloco do if é pulado e só "
                      "“Fim do programa.” aparece."),
                ("conceito", ("Condição = pergunta de sim ou não",
                              "Dentro do if vai uma expressão que resulta em <b>true ou false</b> — normalmente "
                              "uma comparação (==, &gt;, &lt;=...) ou combinação com operadores lógicos "
                              "(&amp;&amp;, ||). Se a resposta for “sim”, o bloco entre { } executa; se for "
                              "“não”, o bloco é ignorado.")),
                ("atencao", "Erro clássico: usar <b>=</b> (atribuição) no lugar de <b>==</b> (comparação) "
                            "dentro do if. <b>if ($x = 5)</b> não compara — atribui 5 e quase sempre resulta em "
                            "true! Compare com <b>==</b> ou <b>===</b>."),
                ("h", "Blocos com mais de um comando"),
                ("codigo", {"titulo": "Vários comandos dentro do if", "ling": "php", "linhas": [
                    "<?php",
                    "    $temIngresso = true;",
                    "",
                    "    if ($temIngresso === true) {",
                    "        echo \"Bem-vindo ao cinema!<br>\";",
                    "        echo \"Sala 3, sessão das 19h.\";",
                    "    }",
                    "?>",
                ]}),
                ("dica", "Chaves { } delimitam o bloco. Se houver um único comando, elas são opcionais — mas o "
                         "curso adota <b>sempre usar chaves</b> (evita bugs e melhora a legibilidade). "
                         "Indente o conteúdo do bloco com 4 espaços."),
            ],
            "slides": {
                "pontos": [
                    "if (condição) { bloco } — executa se a condição for true",
                    "Condição: comparações e operadores lógicos",
                    "false → bloco é pulado; código segue depois do if",
                    "NUNCA use = no if (atribui!); use == ou ===",
                    "Sempre usar chaves { } e indentar",
                ],
                "codigo": {"titulo": "Primeiro if", "linhas": [
                    "$idade = 17;",
                    "if ($idade >= 18) {",
                    "    echo \"Pode dirigir.\";",
                    "}",
                    "echo \"Fim.\";",
                ]},
                "nota": "Testar com idade 17 e depois 20 — prever o resultado antes de executar (hábito de "
                        "programador).",
            },
        },
        {
            "num": 28,
            "titulo": "IF / ELSE / ELSEIF — situação do aluno",
            "blocos": [
                ("h", "Dois caminhos: if/else"),
                ("codigo", {"titulo": "Sintaxe if/else", "ling": "php", "linhas": [
                    "if (condição) {",
                    "    // se TRUE",
                    "} else {",
                    "    // se FALSE",
                    "}",
                ]}),
                ("h", "Vários caminhos: elseif"),
                ("p", "Quando há <b>mais de duas possibilidades</b>, encadeamos <b>elseif</b>. O PHP testa as "
                      "condições <b>em ordem</b> e executa <b>apenas o primeiro</b> bloco verdadeiro — os demais "
                      "são pulados, mesmo que também fossem true:"),
                ("codigo", {"titulo": "situacao.php — o clássico “situação do aluno”", "ling": "php", "linhas": [
                    "<?php",
                    "    $nota = 6.5;",
                    "",
                    "    if ($nota >= 7) {",
                    "        echo \"APROVADO\";",
                    "    } elseif ($nota >= 5) {",
                    "        echo \"RECUPERAÇÃO\";",
                    "    } else {",
                    "        echo \"REPROVADO\";",
                    "    }",
                    "    // Saída: RECUPERAÇÃO",
                    "?>",
                ]}),
                ("conceito", ("A ordem das condições importa!",
                              "Se invertêssemos (testar $nota &gt;= 5 antes de $nota &gt;= 7), uma nota 8 cairia "
                              "em “RECUPERAÇÃO” — pois 8 &gt;= 5 é a primeira condição verdadeira. Regra: em "
                              "cadeias de elseif, teste da condição <b>mais restritiva para a menos "
                              "restritiva</b>.")),
                ("h", "Condições compostas dentro do if"),
                ("codigo", {"titulo": "Aprovação com frequência (módulo 7 + módulo 8 juntos)", "ling": "php", "linhas": [
                    "<?php",
                    "    $media = 8.0;",
                    "    $frequencia = 70;",
                    "",
                    "    if (($media >= 7) && ($frequencia >= 75)) {",
                    "        echo \"Aprovado!\";",
                    "    } elseif (($media >= 7) && ($frequencia < 75)) {",
                    "        echo \"Reprovado por falta.\";",
                    "    } else {",
                    "        echo \"Recuperação ou reprovado por nota.\";",
                    "    }",
                    "?>",
                ]}),
                ("analogia", ("elseif é uma fila de guichês",
                              "Você passa pelo 1º guichê (if): se resolver, sai do banco — nem olha os outros. "
                              "Se não, tenta o 2º (elseif)... Se nenhum resolver, vai ao “outros assuntos” "
                              "(else). <b>Só um guichê atende você.</b>")),
            ],
            "slides": {
                "pontos": [
                    "if/else: dois caminhos (true / false)",
                    "elseif: vários caminhos testados em ordem",
                    "Apenas o PRIMEIRO bloco verdadeiro executa",
                    "Ordem: condição mais restritiva primeiro (>= 7 antes de >= 5)",
                    "Situação do aluno: aprovado / recuperação / reprovado",
                ],
                "codigo": {"titulo": "Situação do aluno", "linhas": [
                    "$nota = 6.5;",
                    "if ($nota >= 7)      echo \"APROVADO\";",
                    "elseif ($nota >= 5)  echo \"RECUPERAÇÃO\";",
                    "else                 echo \"REPROVADO\";",
                ]},
                "nota": "Construir o programa ao vivo e testar com notas 9, 6.5 e 3. Provocar: 'e se eu inverter "
                        "a ordem dos elseif?' — deixar a turma prever e depois executar.",
            },
        },
        {
            "num": 29,
            "titulo": "SWITCH — menu de opções",
            "blocos": [
                ("h", "Quando um valor é comparado com várias opções"),
                ("p", "<b>switch</b> compara <b>uma variável</b> com uma <b>lista de valores fixos</b> "
                      "(cases). É ideal para <b>menus</b> e opções fechadas:"),
                ("codigo", {"titulo": "menu.php — switch com case, break e default", "ling": "php", "linhas": [
                    "<?php",
                    "    $opcao = 2;",
                    "",
                    "    switch ($opcao) {",
                    "        case 1:",
                    "            echo \"Cadastrar aluno\";",
                    "            break;",
                    "        case 2:",
                    "            echo \"Consultar notas\";",
                    "            break;",
                    "        case 3:",
                    "            echo \"Sair do sistema\";",
                    "            break;",
                    "        default:",
                    "            echo \"Opção inválida!\";",
                    "    }",
                    "    // Saída: Consultar notas",
                    "?>",
                ]}),
                ("tabela", {"titulo": "Peças do switch",
                            "cab": ["Peça", "Função"],
                            "lin": [
                                ["switch ($var)", "Variável que será comparada com os cases"],
                                ["case valor:", "Um valor possível; se bater, executa o bloco abaixo"],
                                ["break;", "Encerra o switch — SEM ele, os cases seguintes também executam!"],
                                ["default:", "O “else” do switch: nenhum case bateu"],
                            ]}),
                ("atencao", "Esquecer o <b>break</b> causa o efeito “cascata”: o PHP continua executando os "
                            "cases seguintes até achar um break ou terminar o switch. É o erro nº 1 com switch!"),
                ("h", "if × switch — qual usar?"),
                ("tabela", {"titulo": "Escolhendo a estrutura",
                            "cab": ["Situação", "Melhor estrutura"],
                            "lin": [
                                ["Faixas de valores (nota >= 7, idade entre...)", "if / elseif"],
                                ["Condições variadas e compostas (&&, ||)", "if / elseif"],
                                ["Um valor comparado a opções fixas (menu, dia da semana)", "switch"],
                                ["Sim / não simples", "if / else"],
                            ]}),
                ("dica", "switch compara com == (frouxo): case \"1\" bate com 1. Em menus digitados, converta a "
                         "entrada para número ou use strings consistentes."),
            ],
            "slides": {
                "pontos": [
                    "switch ($var) { case valor: ... break; default: ... }",
                    "Compara 1 variável com valores FIXOS (menus)",
                    "break encerra — sem ele, cascata de cases!",
                    "default = opção inválida (o 'else' do switch)",
                    "Faixas/condições compostas → if · opções fixas → switch",
                ],
                "codigo": {"titulo": "Menu com switch", "linhas": [
                    "switch ($opcao) {",
                    "  case 1: echo \"Cadastrar\"; break;",
                    "  case 2: echo \"Consultar\"; break;",
                    "  case 3: echo \"Sair\";      break;",
                    "  default: echo \"Inválida!\";",
                    "}",
                ]},
                "nota": "Demonstrar a cascata removendo um break ao vivo. Exercício: menu de lanchonete "
                        "(1-sanduíche, 2-suco, 3-combo).",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Situação do aluno (completo)", "tipo": "pratico",
            "enunciado": "Crie <b>situacao.php</b> com as variáveis $nota e $frequencia. Regras: aprovado se "
                         "nota ≥ 7 E frequência ≥ 75; recuperação se nota entre 5 e 6,9 (frequência ok); caso "
                         "contrário, reprovado. Se a frequência for &lt; 75, reprovado por falta (independentemente "
                         "da nota). Teste com 3 combinações diferentes.",
            "esperado": "Programa com if/elseif/else e condições compostas (&&) exibindo a situação correta "
                        "para cada teste.",
            "orientacao": "Verifique a ordem das condições (mais restritiva primeiro). Peça que documentem os "
                          "testes feitos em comentários.",
        },
        {
            "num": 2, "titulo": "Verificador de maioridade", "tipo": "pratico",
            "enunciado": "Crie <b>maioridade.php</b>: dada $idade, exiba “Maior de idade — pode votar e dirigir” "
                         "(≥18), “Pode votar mas não dirigir” (16–17) ou “Menor de idade” (&lt;16).",
            "esperado": "Cadeia if/elseif/else com as 3 faixas corretas e mensagens claras.",
            "orientacao": "Testar idades 20, 16 e 12. Erro comum: testar >= 16 antes de >= 18 (ordem errada).",
        },
        {
            "num": 3, "titulo": "Menu da lanchonete com switch", "tipo": "pratico",
            "enunciado": "Crie <b>lanchonete.php</b> com $pedido. Cases: 1 = “Sanduíche — R$ 8,00”, 2 = “Suco — "
                         "R$ 5,00”, 3 = “Combo — R$ 12,00”, default = “Pedido inválido”. Teste com os 4 "
                         "cenários.",
            "esperado": "switch com 3 cases + default, breaks presentes, saída correta para cada valor.",
            "orientacao": "Desafio: remover um break de propósito e observar/explicar a cascata.",
        },
        {
            "num": 4, "titulo": "O que aparece na tela?", "tipo": "escrito",
            "enunciado": "Sem executar, escreva a saída exata de cada programa:",
            "codigo": {"titulo": "Programas para análise", "ling": "php", "linhas": [
                "// A)                          // B)",
                "$n = 5;                       $op = 1;",
                "if ($n = 3) {                 switch ($op) {",
                "    echo \"Aprovado\";             case 1: echo \"Um\";",
                "} else {                          case 2: echo \"Dois\";",
                "    echo \"Reprovado\";             break;",
                "}                               default: echo \"Outro\";",
                "                              }",
            ]},
            "esperado": "A) “Aprovado” — pegadinha: $n = 3 é atribuição (resultado 3 = true), não comparação! "
                        "B) “UmDois” — falta break no case 1 (cascata até o break do case 2).",
            "orientacao": "Os dois erros mais clássicos do módulo em um exercício só. Corrija com discussão "
                          "aberta: como consertar cada um?",
        },
    ],
    "teste_rapido": [
        {"enunciado": "O bloco de um <b>if</b> é executado quando:",
         "alt": ["a condição resulta em false.",
                 "a condição resulta em true.",
                 "sempre, independentemente da condição.",
                 "apenas se houver um else."],
         "resposta": 1,
         "comentario": "if executa o bloco somente se a condição for verdadeira (true)."},
        {"enunciado": "Em uma cadeia if/elseif/else, quando uma condição elseif é verdadeira:",
         "alt": ["todos os blocos seguintes também executam.",
                 "apenas o bloco dela executa e o restante da cadeia é ignorado.",
                 "o programa gera um erro.",
                 "o bloco do else executa junto."],
         "resposta": 1,
         "comentario": "O PHP executa apenas o primeiro bloco verdadeiro da cadeia e ignora os demais."},
        {"enunciado": "No programa da situação do aluno (>=7 aprovado; >=5 recuperação; else reprovado), qual "
                    "é a saída para nota = 8?",
         "alt": ["RECUPERAÇÃO", "REPROVADO", "APROVADO", "APROVADO e RECUPERAÇÃO"],
         "resposta": 2,
         "comentario": "8 >= 7 é a primeira condição verdadeira → APROVADO. (Se a ordem estivesse invertida, "
                       "cairia em recuperação — por isso a ordem importa.)"},
        {"enunciado": "A palavra-chave <b>break</b> dentro de um switch serve para:",
         "alt": ["reiniciar o switch.",
                 "encerrar o switch, evitando que os cases seguintes executem.",
                 "pular para o default.",
                 "comparar o valor com o próximo case."],
         "resposta": 1,
         "comentario": "Sem o break, ocorre a cascata: os blocos dos cases seguintes executam mesmo sem bater."},
        {"enunciado": "O que está errado em <b>if ($nota = 7) { echo \"Aprovado\"; }</b>?",
         "alt": ["Falta o ponto e vírgula dentro do if.",
                 "Deveria usar == ou === para comparar; = está atribuindo 7 à variável.",
                 "A condição deveria estar sem parênteses.",
                 "Nada: o código está correto."],
         "resposta": 1,
         "comentario": "= atribui (e o resultado 7 é 'verdadeiro'), então o bloco sempre executa. Comparação "
                       "correta: == ou ===."},
    ],
    "avaliacao_ref": None,
}

MODULO_9 = {
    "num": 9,
    "titulo": "PHP – repetição e arrays",
    "parte_num": 3,
    "parte_titulo": "Introdução ao PHP",
    "aulas_faixa": "Aulas 30 a 35",
    "semanas": "Semanas 10 a 12",
    "objetivos": [
        "Repetir blocos de código com for, while e do...while.",
        "Escolher o laço adequado para cada situação e evitar laços infinitos.",
        "Criar e acessar arrays indexados.",
        "Percorrer arrays com foreach.",
        "Utilizar arrays associativos (chave => valor).",
    ],
    "aulas": [
        {
            "num": 30,
            "titulo": "Laço for — repetição com contador",
            "blocos": [
                ("h", "Por que repetir?"),
                ("p", "Exibir os números de 1 a 1000 com echo seria inviável. <b>Estruturas de repetição</b> "
                      "(laços) executam um bloco <b>várias vezes</b> automaticamente. O <b>for</b> é o laço com "
                      "<b>contador</b> — use quando você sabe <b>quantas vezes</b> repetir."),
                ("codigo", {"titulo": "Sintaxe do for", "ling": "php", "linhas": [
                    "for (início do contador; condição; passo) {",
                    "    // bloco repetido enquanto a condição for true",
                    "}",
                    "",
                    "----------------------------------------------",
                    "",
                    "<?php",
                    "    for ($i = 1; $i <= 10; $i++) {",
                    "        echo \"Número: $i <br>\";",
                    "    }",
                    "?>",
                ]}),
                ("tabela", {"titulo": "As 3 partes do for",
                            "cab": ["Parte", "Exemplo", "Quando acontece"],
                            "lin": [
                                ["Inicialização", "$i = 1", "Uma única vez, no começo"],
                                ["Condição", "$i &lt;= 10", "Testada antes de cada volta (true → repete)"],
                                ["Incremento", "$i++", "Executado ao final de cada volta"],
                            ]}),
                ("p", "O contador $i++ (equivale a $i = $i + 1) faz o for andar: 1, 2, 3... até 10. Quando $i "
                      "chega a 11, a condição falha e o laço termina."),
                ("codigo", {"titulo": "Tabuada do 7 com for", "ling": "php", "linhas": [
                    "<?php",
                    "    $n = 7;",
                    "    for ($i = 1; $i <= 10; $i++) {",
                    "        $resultado = $n * $i;",
                    "        echo \"$n x $i = $resultado <br>\";",
                    "    }",
                    "?>",
                ]}),
                ("dica", "O for também conta <b>para trás</b> (for ($i = 10; $i &gt;= 1; $i--) — contagem "
                         "regressiva) e <b>de 2 em 2</b> ($i += 2 — só pares)."),
            ],
            "slides": {
                "pontos": [
                    "Laço = repetir bloco várias vezes",
                    "for (início; condição; passo) — quando se sabe quantas vezes",
                    "$i++ = $i + 1 · $i-- = $i − 1",
                    "Contagem de 1 a 10, tabuada, contagem regressiva",
                    "A condição é testada ANTES de cada volta",
                ],
                "codigo": {"titulo": "for clássico", "linhas": [
                    "for ($i = 1; $i <= 10; $i++) {",
                    "    echo \"Número: $i <br>\";",
                    "}",
                ]},
                "nota": "Executar o for de 1 a 10 e 'seguir' o valor de $i no quadro volta a volta. Depois, "
                        "desafio-relâmpago: pares de 1 a 20.",
            },
        },
        {
            "num": 31,
            "titulo": "Laço while",
            "blocos": [
                ("h", "Repetir ENQUANTO uma condição valer"),
                ("p", "O <b>while</b> repete o bloco <b>enquanto</b> a condição for true — teste <b>antes</b> de "
                      "executar. Use quando <b>não se sabe</b> quantas voltas serão necessárias (ex.: repetir "
                      "até o usuário acertar):"),
                ("codigo", {"titulo": "while — soma de 1 até 5", "ling": "php", "linhas": [
                    "<?php",
                    "    $contador = 1;",
                    "    $soma = 0;",
                    "",
                    "    while ($contador <= 5) {",
                    "        $soma = $soma + $contador;   // acumula",
                    "        $contador++;                 // AVANÇA o contador!",
                    "    }",
                    "",
                    "    echo \"Soma de 1 a 5: $soma\";     // 15",
                    "?>",
                ]}),
                ("atencao", "<b>Laço infinito</b>: se você esquecer o $contador++ (ou qualquer coisa que torne a "
                            "condição false), o while nunca termina — a página trava/carrega para sempre. "
                            "Regra: <b>todo while precisa de um passo que caminhe para o fim</b>."),
                ("h", "Padrão de uso do while"),
                ("lista_num", [
                    "Inicialize a variável de controle <b>antes</b> do laço ($contador = 1);",
                    "Teste a condição no while ($contador &lt;= 5);",
                    "Dentro do bloco, faça o trabalho <b>e avance o controle</b> ($contador++).",
                ]),
                ("dica", "Se a condição já for false na 1ª verificação, o bloco do while <b>não executa nenhuma "
                         "vez</b>. (Isso vai mudar no do...while — próxima aula.)"),
            ],
            "slides": {
                "pontos": [
                    "while (condição) { bloco } — testa ANTES de executar",
                    "Use quando não sabe quantas voltas",
                    "Padrão: inicializar → testar → avançar ($contador++)",
                    "Sem avanço = LAÇO INFINITO (página trava!)",
                    "Condição false no início → 0 execuções",
                ],
                "codigo": {"titulo": "while", "linhas": [
                    "$contador = 1; $soma = 0;",
                    "while ($contador <= 5) {",
                    "    $soma += $contador;",
                    "    $contador++;   // nunca esquecer!",
                    "}",
                ]},
                "nota": "Demonstrar (com cuidado) o laço infinito comentando o $contador++ e explicar como "
                        "interromper no navegador. Fixa a importância do avanço.",
            },
        },
        {
            "num": 32,
            "titulo": "Laço do...while",
            "blocos": [
                ("h", "Executa primeiro, testa depois"),
                ("p", "O <b>do...while</b> executa o bloco <b>ao menos uma vez</b> e só depois testa a condição. "
                      "Útil quando a ação deve acontecer antes da primeira verificação (ex.: pedir uma senha e "
                      "depois checar se está correta):"),
                ("codigo", {"titulo": "do...while — comparando com while", "ling": "php", "linhas": [
                    "<?php",
                    "    $x = 10;",
                    "",
                    "    // WHILE: testa antes — condição falsa, não executa",
                    "    while ($x < 5) {",
                    "        echo \"while executou\";    // nunca aparece",
                    "    }",
                    "",
                    "    // DO WHILE: executa 1ª vez e só então testa",
                    "    do {",
                    "        echo \"do-while executou 1 vez\";   // aparece!",
                    "    } while ($x < 5);",
                    "?>",
                ]}),
                ("tabela", {"titulo": "Comparação lado a lado",
                            "cab": ["", "while", "do...while"],
                            "lin": [
                                ["Teste da condição", "Antes de executar o bloco", "Depois de executar o bloco"],
                                ["Mínimo de execuções", "0 (pode nunca executar)", "1 (sempre executa a 1ª vez)"],
                                ["Sintaxe", "while (cond) { }", "do { } while (cond); — note o ; final!"],
                                ["Uso típico", "Repetir enquanto valer", "Executar e depois validar"],
                            ]}),
                ("atencao", "O <b>ponto e vírgula</b> depois do while(cond) no do...while é obrigatório — "
                            "esquecê-lo gera erro de sintaxe."),
            ],
            "slides": {
                "pontos": [
                    "do { bloco } while (condição); — executa e DEPOIS testa",
                    "Mínimo 1 execução (while pode executar 0 vezes)",
                    "Ponto e vírgula final obrigatório",
                    "Uso: validar após a ação (menus, senhas, tentativas)",
                ],
                "codigo": {"titulo": "A diferença em 4 linhas", "linhas": [
                    "$x = 10;",
                    "while ($x < 5) { echo \"não executa\"; }",
                    "do { echo \"executa 1x\"; } while ($x < 5);",
                ]},
                "nota": "Comparação lado a lado no projetor com o MESMO valor inicial. Prever antes de executar.",
            },
        },
        {
            "num": 33,
            "titulo": "Arrays indexados",
            "blocos": [
                ("h", "Uma variável, vários valores"),
                ("p", "Guardar 5 alunos em 5 variáveis ($aluno1, $aluno2...) é inviável. Um <b>array</b> guarda "
                      "<b>vários valores em uma única variável</b>, cada um em uma <b>posição</b> (índice):"),
                ("codigo", {"titulo": "Criando e acessando arrays", "ling": "php", "linhas": [
                    "<?php",
                    "    $alunos = [\"Ana\", \"Bruno\", \"Carla\", \"Diego\"];",
                    "",
                    "    echo $alunos[0];        // Ana      — o PRIMEIRO é o índice 0!",
                    "    echo \"<br>\";",
                    "    echo $alunos[2];        // Carla",
                    "    echo \"<br>\";",
                    "",
                    "    $alunos[4] = \"Elisa\";  // adiciona na posição 4",
                    "    echo \"Total: \" . count($alunos);   // 5",
                    "?>",
                ]}),
                ("conceito", ("Índices começam em 0",
                              "A posição do primeiro elemento é <b>[0]</b>, o segundo é <b>[1]</b>, e assim por "
                              "diante. Um array com 4 itens tem índices 0 a 3. Acessar $alunos[4] antes de "
                              "existir gera aviso (undefined) — cuidado!")),
                ("h", "Funções úteis"),
                ("lista", [
                    "<b>count($array)</b> — quantidade de elementos;",
                    "<b>$array[] = valor</b> — adiciona no final (sem informar índice);",
                    "<b>$array[i] = valor</b> — altera/cria a posição i;",
                    "<b>sort($array)</b> — ordena (crescente).",
                ]),
                ("dica", "Escreva o array em várias linhas quando ficar grande — facilita ler e manter:"),
                ("codigo", {"titulo": "Array multilinha", "ling": "php", "linhas": [
                    "$notas = [",
                    "    8.5,",
                    "    7.0,",
                    "    9.25,",
                    "];",
                ]}),
            ],
            "slides": {
                "pontos": [
                    "Array = vários valores em uma variável",
                    "$alunos = ['Ana', 'Bruno', 'Carla'];",
                    "Índices começam em 0: $alunos[0] = 'Ana'",
                    "count() = tamanho · $arr[] = x adiciona ao final",
                    "sort() ordena o array",
                ],
                "codigo": {"titulo": "Array indexado", "linhas": [
                    "$alunos = [\"Ana\", \"Bruno\", \"Carla\"];",
                    "echo $alunos[0];     // Ana",
                    "$alunos[] = \"Diego\"; // adiciona",
                    "echo count($alunos); // 4",
                ]},
                "nota": "Desenhar o array como 'caixinhas numeradas' no quadro. Exercício-relâmpago: qual é o "
                        "índice de 'Carla'?",
            },
        },
        {
            "num": 34,
            "titulo": "foreach — percorrendo arrays",
            "blocos": [
                ("h", "Item a item, sem se preocupar com índices"),
                ("p", "O <b>foreach</b> percorre um array <b>do primeiro ao último elemento</b> automaticamente. "
                      "A cada volta, o valor do elemento atual fica disponível em uma variável:"),
                ("codigo", {"titulo": "foreach — exibindo a lista de alunos", "ling": "php", "linhas": [
                    "<?php",
                    "    $alunos = [\"Ana\", \"Bruno\", \"Carla\", \"Diego\"];",
                    "",
                    "    foreach ($alunos as $aluno) {",
                    "        echo \"Aluno: $aluno <br>\";",
                    "    }",
                    "    // foreach ($array as $item) — 'para cada $item do $array'",
                    "?>",
                ]}),
                ("h", "A versão com índice: as $i => $valor"),
                ("codigo", {"titulo": "foreach com chave e valor", "ling": "php", "linhas": [
                    "<?php",
                    "    $notas = [8.5, 7.0, 9.25];",
                    "",
                    "    foreach ($notas as $indice => $nota) {",
                    "        echo \"Nota da posição $indice: $nota <br>\";",
                    "    }",
                    "?>",
                ]}),
                ("h", "foreach × for em arrays"),
                ("codigo", {"titulo": "As duas formas de percorrer", "ling": "php", "linhas": [
                    "// com for — controlando o índice",
                    "for ($i = 0; $i < count($alunos); $i++) {",
                    "    echo $alunos[$i];",
                    "}",
                    "",
                    "// com foreach — mais simples e legível",
                    "foreach ($alunos as $aluno) {",
                    "    echo $aluno;",
                    "}",
                ]}),
                ("conceito", ("Quando usar cada laço?",
                              "<b>for</b>: quando o número de voltas é conhecido/definido por um contador "
                              "(1 a 10, tabuada). <b>while/do...while</b>: quando depende de uma condição que "
                              "muda durante a execução. <b>foreach</b>: quando o objetivo é percorrer "
                              "<b>todos os elementos de um array</b> — é o laço dos arrays.")),
                ("dica", "Acumular dentro do foreach é padrão comum: somar todas as notas para calcular a média "
                         "($soma += $nota; e ao final $media = $soma / count($notas))."),
            ],
            "slides": {
                "pontos": [
                    "foreach ($arr as $item) { } — percorre todos os elementos",
                    "foreach ($arr as $i => $valor) — com o índice junto",
                    "Mais simples que for para arrays",
                    "Padrão: acumular ($soma += $x) para médias/totais",
                    "for = contador · while = condição · foreach = array",
                ],
                "codigo": {"titulo": "Lista de alunos", "linhas": [
                    "$alunos = [\"Ana\", \"Bruno\", \"Carla\"];",
                    "foreach ($alunos as $aluno) {",
                    "    echo \"Aluno: $aluno <br>\";",
                    "}",
                ]},
                "nota": "Exercício: soma e média das notas com foreach. Comparar no quadro com a versão usando "
                        "for.",
            },
        },
        {
            "num": 35,
            "titulo": "Arrays associativos",
            "blocos": [
                ("h", "Chaves com significado"),
                ("p", "No array indexado, a posição é um número (0, 1, 2...). No <b>array associativo</b>, "
                      "<b>você define as chaves</b> (textos com significado), no formato "
                      "<b>chave =&gt; valor</b>:"),
                ("codigo", {"titulo": "Ficha do aluno", "ling": "php", "linhas": [
                    "<?php",
                    "    $aluno = [",
                    "        \"nome\"  => \"Ana Silva\",",
                    "        \"idade\" => 17,",
                    "        \"curso\" => \"Informática\",",
                    "    ];",
                    "",
                    "    echo $aluno[\"nome\"];        // Ana Silva",
                    "    echo \"<br>\";",
                    "    echo \"Curso: \" . $aluno[\"curso\"];",
                    "    echo \"<br>\";",
                    "",
                    "    $aluno[\"media\"] = 9.0;      // acrescenta um novo par",
                    "?>",
                ]}),
                ("h", "foreach em arrays associativos"),
                ("codigo", {"titulo": "Percorrendo chave => valor", "ling": "php", "linhas": [
                    "<?php",
                    "    foreach ($aluno as $campo => $valor) {",
                    "        echo \"$campo: $valor <br>\";",
                    "    }",
                    "    // nome: Ana Silva",
                    "    // idade: 17",
                    "    // curso: Informática",
                    "?>",
                ]}),
                ("conceito", ("Indexado × associativo",
                              "<b>Indexado</b>: posição numérica automática (0, 1, 2...) — ideal para <b>listas "
                              "de coisas do mesmo tipo</b> (vários alunos). <b>Associativo</b>: chaves com nome "
                              "— ideal para <b>fichas/registros</b> (um aluno com vários campos). Os dois serão "
                              "combinados no módulo 10 (array de fichas = multidimensional).")),
                ("analogia", ("Array associativo = formulário",
                              "Cada par chave =&gt; valor é como um campo preenchido de um formulário: "
                              "nome: Ana · idade: 17 · curso: Informática. A chave é o label; o valor é o que "
                              "foi digitado.")),
            ],
            "slides": {
                "pontos": [
                    "Array associativo: chave => valor (chaves com significado)",
                    "$aluno = ['nome' => 'Ana', 'idade' => 17];",
                    "Acesso: $aluno['nome']",
                    "foreach ($arr as $campo => $valor)",
                    "Indexado = lista · Associativo = ficha/registro",
                ],
                "codigo": {"titulo": "Ficha do aluno", "linhas": [
                    "$aluno = [",
                    "  \"nome\" => \"Ana\",",
                    "  \"idade\" => 17,",
                    "];",
                    "echo $aluno[\"nome\"];  // Ana",
                ]},
                "nota": "Construir a ficha de um aluno da turma ao vivo. Depois, cada um cria a sua e exibe com "
                        "foreach chave => valor.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Tabuada com for", "tipo": "pratico",
            "enunciado": "Crie <b>tabuada.php</b> que exiba a tabuada de um número $n (de 1 a 10) formatada: "
                         "“7 x 1 = 7”. Desafio: exibir apenas os números pares de 1 a 20 em outro laço.",
            "esperado": "10 linhas de tabuada corretas; desafio com for ($i = 2; $i &lt;= 20; $i += 2) ou "
                        "if ($i % 2 == 0) dentro do laço.",
            "orientacao": "Pergunte qual abordagem do desafio é melhor e por quê (menos voltas × mais simples).",
        },
        {
            "num": 2, "titulo": "while × do...while", "tipo": "pratico",
            "enunciado": "Crie <b>somas.php</b>: com $limite = 0, some de 1 até $limite usando while e depois "
                         "usando do...while, exibindo os dois resultados. Explique (em comentário) por que os "
                         "resultados diferem.",
            "esperado": "while: 0 (não executa, condição falsa desde o início); do...while: 1 (executa a 1ª "
                        "volta somando 1). Comentário explicando a diferença do momento do teste.",
            "orientacao": "Excelente para fixar 'mínimo 0 × mínimo 1 execução'. Depois testar com $limite = 5.",
        },
        {
            "num": 3, "titulo": "Lista de alunos com média", "tipo": "pratico",
            "enunciado": "Crie <b>alunos.php</b> com dois arrays: $alunos (5 nomes) e $notas (5 notas). "
                         "Exiba cada nome com sua nota usando foreach com índice ($i =&gt; $valor) e, ao final, "
                         "a média da turma.",
            "esperado": "5 linhas 'Nome — Nota' e a média correta (soma acumulada / count).",
            "orientacao": "Reforce o padrão de acumulação ($soma += ...). Desafio: exibir 'aprovado/recuperação' "
                          "por aluno usando o if do módulo 8 dentro do foreach.",
        },
        {
            "num": 4, "titulo": "Ficha do aluno (associativo)", "tipo": "pratico",
            "enunciado": "Crie <b>ficha.php</b> com um array associativo contendo nome, idade, curso e cidade "
                         "de um colega. Exiba a ficha formatada percorrendo com foreach ($campo =&gt; $valor).",
            "esperado": "Ficha exibida linha a linha ('nome: ...', 'idade: ...').",
            "orientacao": "Confira a sintaxe => e aspas nas chaves. Este é o embrião do 'cadastro' do projeto "
                          "final.",
        },
        {
            "num": 5, "titulo": "Preveja a saída", "tipo": "escrito",
            "enunciado": "Sem executar, escreva a saída exata:",
            "codigo": {"titulo": "Analise o código", "ling": "php", "linhas": [
                "<?php",
                "    $numeros = [3, 7, 2];",
                "    $soma = 0;",
                "    foreach ($numeros as $n) {",
                "        if ($n > 2) {",
                "            $soma = $soma + $n;",
                "        }",
                "    }",
                "    echo $soma;",
                "?>",
            ]},
            "esperado": "10 — soma de 3 e 7 (o 2 não entra porque a condição é n > 2).",
            "orientacao": "Simular no quadro 'mesa redonda': uma linha por vez, acompanhando $soma. Combina "
                          "foreach + if (integração de módulos).",
        },
    ],
    "teste_rapido": [
        {"enunciado": "Quantas vezes o bloco executa em: <b>for ($i = 0; $i &lt; 5; $i++) { ... }</b>?",
         "alt": ["4 vezes", "5 vezes", "6 vezes", "infinitas vezes"],
         "resposta": 1,
         "comentario": "$i assume 0, 1, 2, 3, 4 → 5 voltas. Quando $i chega a 5, a condição $i < 5 falha."},
        {"enunciado": "O maior risco ao usar while é:",
         "alt": ["esquecer o ponto e vírgula do echo.",
                 "criar um laço infinito por não atualizar a variável de controle.",
                 "usar chaves no bloco.",
                 "o laço nunca executar a primeira vez."],
         "resposta": 1,
         "comentario": "Sem o avanço ($contador++ ou similar), a condição nunca vira false e o laço não termina."},
        {"enunciado": "A diferença do do...while para o while é que o do...while:",
         "alt": ["só funciona com arrays.",
                 "executa o bloco pelo menos uma vez, pois testa a condição no final.",
                 "não precisa de condição.",
                 "executa sempre duas vezes."],
         "resposta": 1,
         "comentario": "do...while = faz e depois confere: mínimo de 1 execução; while = confere e depois faz: "
                       "pode executar 0 vezes."},
        {"enunciado": "Dado $frutas = [\"maçã\", \"banana\", \"uva\"], o comando <b>echo $frutas[1];</b> exibe:",
         "alt": ["maçã", "banana", "uva", "erro: índice fora do array"],
         "resposta": 1,
         "comentario": "Índices começam em 0: [0]=maçã, [1]=banana, [2]=uva."},
        {"enunciado": "Para percorrer todos os elementos de um array sem controlar índices manualmente, o laço "
                    "ideal é:",
         "alt": ["for", "while", "foreach", "do...while"],
         "resposta": 2,
         "comentario": "foreach foi criado para arrays: foreach ($arr as $item). Com chave: as $k => $v."},
    ],
    "avaliacao_ref": None,
}

MODULOS = [MODULO_6, MODULO_7, MODULO_8, MODULO_9]
