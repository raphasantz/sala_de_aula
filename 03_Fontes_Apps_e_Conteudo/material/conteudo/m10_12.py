# -*- coding: utf-8 -*-
"""Módulos 10 a 12 — PHP + HTML (organização), Formulários + PHP e Projeto Final."""

MODULO_10 = {
    "num": 10,
    "titulo": "PHP + HTML — organização, include e funções",
    "parte_num": 5,
    "parte_titulo": "Organização e Desenvolvimento do Projeto",
    "aulas_faixa": "Aulas 36 e 43 a 48",
    "semanas": "Semanas 12, 15 e 16",
    "objetivos": [
        "Integrar HTML e PHP gerando páginas dinamicamente.",
        "Organizar os arquivos do projeto em pastas (css/, imagens/, includes/).",
        "Reutilizar partes da aplicação com include (cabeçalho e rodapé).",
        "Criar funções com parâmetros e retorno (function, return).",
        "Trabalhar com arrays multidimensionais e foreach aninhado.",
        "Gerar tabelas HTML dinamicamente a partir de dados em PHP.",
    ],
    "aulas": [
        {
            "num": 36,
            "titulo": "Revisão cumulativa e projeto “sistema de cadastro simples”",
            "blocos": [
                ("h", "O que já sabemos"),
                ("p", "Antes de avançar, esta aula faz uma <b>revisão cumulativa</b> de tudo o que foi visto em "
                      "PHP até aqui: variáveis, tipos, operadores, decisões (if/elseif/else, switch), laços "
                      "(for, while, do...while) e arrays (indexados, associativos, foreach)."),
                ("tabela", {"titulo": "Checklist da revisão",
                            "cab": ["Tema", "Você consegue..."],
                            "lin": [
                                ["Variáveis e tipos", "declarar $nome, usar var_dump e explicar string × int × float × bool?"],
                                ["Operadores", "calcular média com parênteses e usar % (resto)?"],
                                ["Comparações", "explicar a diferença entre == e ===?"],
                                ["Decisões", "programar a situação do aluno com if/elseif/else?"],
                                ["Switch", "montar um menu com case, break e default?"],
                                ["Laços", "escolher entre for, while e do...while?"],
                                ["Arrays", "criar array indexado e associativo e percorrê-los com foreach?"],
                            ]}),
                ("h", "Projeto integrador: sistema de cadastro simples"),
                ("p", "Juntando HTML + PHP: uma página que <b>armazena alunos em um array</b> (associativo e "
                      "multidimensional) e os <b>exibe em uma tabela HTML</b> gerada dinamicamente:"),
                ("codigo", {"titulo": "cadastro_simples.php", "ling": "php", "linhas": [
                    "<!DOCTYPE html>",
                    "<html lang=\"pt-br\">",
                    "<head><meta charset=\"UTF-8\"><title>Cadastro simples</title></head>",
                    "<body>",
                    "  <h1>Alunos cadastrados</h1>",
                    "  <?php",
                    "      $alunos = [",
                    "          [\"nome\" => \"Ana\",   \"curso\" => \"Informática\", \"nota\" => 9.0],",
                    "          [\"nome\" => \"Bruno\", \"curso\" => \"Redes\",       \"nota\" => 7.5],",
                    "      ];",
                    "  ?>",
                    "  <table border=\"1\">",
                    "    <tr><th>Nome</th><th>Curso</th><th>Nota</th></tr>",
                    "    <?php foreach ($alunos as $a): ?>",
                    "      <tr>",
                    "        <td><?= $a[\"nome\"] ?></td>",
                    "        <td><?= $a[\"curso\"] ?></td>",
                    "        <td><?= $a[\"nota\"] ?></td>",
                    "      </tr>",
                    "    <?php endforeach; ?>",
                    "  </table>",
                    "</body>",
                    "</html>",
                ]}),
                ("conceito", ("Sintaxe alternativa e <?= ?>",
                              "Misturando HTML e PHP, podemos usar <b>if (): endif;</b> e <b>foreach (): "
                              "endforeach;</b> (mais legíveis em templates) e a abreviação <b>&lt;?= $valor "
                              "?&gt;</b>, que equivale a <b>&lt;?php echo $valor; ?&gt;</b> — perfeita para "
                              "“imprimir” dados dentro do HTML.")),
            ],
            "slides": {
                "pontos": [
                    "Revisão cumulativa: variáveis → operadores → decisões → laços → arrays",
                    "Projeto: página que exibe alunos de um array em tabela HTML",
                    "Sintaxe alternativa: foreach (): endforeach;",
                    "<?= $valor ?> = atalho para <?php echo $valor; ?>",
                ],
                "codigo": {"titulo": "Tabela gerada por PHP", "linhas": [
                    "<table border=\"1\">",
                    "  <?php foreach ($alunos as $a): ?>",
                    "    <tr>",
                    "      <td><?= $a[\"nome\"] ?></td>",
                    "      <td><?= $a[\"nota\"] ?></td>",
                    "    </tr>",
                    "  <?php endforeach; ?>",
                    "</table>",
                ]},
                "nota": "Aula de revisão (12) + retomada na semana 15. Use o checklist no quadro: a turma "
                        "autoavalia cada item. O projeto integra tudo — base do projeto final.",
            },
        },
        {
            "num": 43,
            "titulo": "Organização de arquivos do projeto",
            "blocos": [
                ("h", "Por que organizar?"),
                ("p", "Projetos crescem rápido. Sem organização, encontrar arquivos vira um pesadelo. A "
                      "estrutura padrão separa cada tipo de arquivo em sua <b>pasta</b>:"),
                ("codigo", {"titulo": "Estrutura profissional do projeto", "ling": "texto", "linhas": [
                    "meu-projeto/",
                    "├── index.php           ← página inicial",
                    "├── cadastro.php        ← formulário de cadastro",
                    "├── listar.php          ← listagem dinâmica",
                    "├── processar.php       ← recebe e valida os dados",
                    "├── css/",
                    "│   └── estilo.css      ← estilos (aparência)",
                    "├── imagens/",
                    "│   └── logo.png        ← imagens do site",
                    "└── includes/",
                    "    ├── cabecalho.php   ← parte reutilizável (topo)",
                    "    └── rodape.php      ← parte reutilizável (rodapé)",
                ]}),
                ("conceito", ("Organizar = manter",
                              "1) <b>Encontrar rápido</b>: cada coisa no seu lugar; 2) <b>Reutilizar</b>: "
                              "includes/ evita copiar e colar código; 3) <b>Hospedar fácil</b>: a estrutura vai "
                              "inteira para o servidor; 4) <b>Trabalhar em equipe</b>: cada um sabe onde mexer. "
                              "Esses mesmos princípios valem para o <b>projeto final</b> (módulo 12).")),
                ("dica", "Regras de nomes (relembrando): minúsculas, sem acentos e sem espaços — use "
                         "<b>hífen</b> ou <b>underline</b> (processar-dados.php ou processar_dados.php)."),
            ],
            "slides": {
                "pontos": [
                    "Cada tipo de arquivo em sua pasta: css/, imagens/, includes/",
                    "Páginas principais na raiz: index, cadastro, listar, processar",
                    "Organizar = encontrar, reutilizar, hospedar, colaborar",
                    "Nomes: minúsculos, sem acento, sem espaço",
                ],
                "codigo": {"titulo": "Estrutura do projeto", "linhas": [
                    "meu-projeto/",
                    "├── index.php · cadastro.php · listar.php",
                    "├── css/estilo.css",
                    "├── imagens/logo.png",
                    "└── includes/cabecalho.php + rodape.php",
                ]},
                "nota": "Atividade: reorganizar o projeto antigo (arquivos soltos) na nova estrutura e "
                        "corrigir os caminhos dos links/imagens.",
            },
        },
        {
            "num": 44,
            "titulo": "include — reutilizando partes da aplicação",
            "blocos": [
                ("h", "O problema da repetição"),
                ("p", "Cabeçalho (logo + menu) e rodapé aparecem em <b>todas</b> as páginas. Copiar e colar "
                      "esse código em cada arquivo gera manutenção pesada: mudar o menu exigiria editar 10 "
                      "arquivos! A solução: escrever <b>uma vez</b> e <b>incluir</b> onde for preciso."),
                ("codigo", {"titulo": "includes/cabecalho.php", "ling": "php", "linhas": [
                    "<!DOCTYPE html>",
                    "<html lang=\"pt-br\">",
                    "<head>",
                    "    <meta charset=\"UTF-8\">",
                    "    <title>Meu Projeto</title>",
                    "</head>",
                    "<body>",
                    "    <header>",
                    "        <h1>Sistema de Cadastro</h1>",
                    "        <nav>",
                    "            <a href=\"index.php\">Início</a> |",
                    "            <a href=\"cadastro.php\">Cadastrar</a> |",
                    "            <a href=\"listar.php\">Listar</a>",
                    "        </nav>",
                    "        <hr>",
                    "    </header>",
                ]}),
                ("codigo", {"titulo": "includes/rodape.php", "ling": "php", "linhas": [
                    "    <hr>",
                    "    <footer>",
                    "        <small>Curso Técnico em Informática — <?= date(\"Y\") ?></small>",
                    "    </footer>",
                    "</body>",
                    "</html>",
                ]}),
                ("codigo", {"titulo": "index.php — página usando os includes", "ling": "php", "linhas": [
                    "<?php include \"includes/cabecalho.php\"; ?>",
                    "",
                    "    <h2>Bem-vindo!</h2>",
                    "    <p>Este é o sistema de cadastro da turma.</p>",
                    "",
                    "<?php include \"includes/rodape.php\"; ?>",
                ]}),
                ("tabela", {"titulo": "include × require",
                            "cab": ["Comando", "Se o arquivo não existir...", "Uso recomendado"],
                            "lin": [
                                ["include", "avisa (warning) e a página continua", "partes opcionais"],
                                ["require", "erro fatal e a página para", "partes essenciais (cabecalho!)"],
                                ["include_once / require_once", "idem, mas ignora inclusão duplicada", "evita incluir 2× o mesmo arquivo"],
                            ]}),
                ("atencao", "O caminho do include é <b>relativo ao arquivo que o chama</b>. De index.php (raiz), "
                            "usa-se \"includes/cabecalho.php\". Teste sempre navegando entre as páginas — link "
                            "errado no menu é o sintoma mais comum."),
            ],
            "slides": {
                "pontos": [
                    "Não repetir código: escrever 1×, incluir N×",
                    "include 'includes/cabecalho.php'; + rodape.php",
                    "require = erro fatal se não achar (partes essenciais)",
                    "include_once evita inclusão duplicada",
                    "Mudou o menu? Edite SÓ o cabecalho.php",
                ],
                "codigo": {"titulo": "Reutilização", "linhas": [
                    "<?php include \"includes/cabecalho.php\"; ?>",
                    "",
                    "<h2>Conteúdo da página</h2>",
                    "",
                    "<?php include \"includes/rodape.php\"; ?>",
                ]},
                "nota": "Demonstrar o poder do include: mudar o título do menu UMA vez e atualizar todas as "
                        "páginas. 'E se eu tivesse copiado e colado?'",
            },
        },
        {
            "num": 45,
            "titulo": "Funções — function, parâmetro e return",
            "blocos": [
                ("h", "O que são funções"),
                ("p", "Uma <b>função</b> é um bloco de código com <b>nome</b>, que executa uma tarefa e pode "
                      "<b>devolver um resultado</b>. Assim como o include evita repetir HTML, funções evitam "
                      "repetir <b>lógica</b>:"),
                ("codigo", {"titulo": "Criando e chamando funções", "ling": "php", "linhas": [
                    "<?php",
                    "    // 1) DEFINIR a função",
                    "    function saudacao($nome) {",
                    "        return \"Olá, $nome! Seja bem-vindo(a).\";",
                    "    }",
                    "",
                    "    // 2) CHAMAR a função (quantas vezes quiser)",
                    "    echo saudacao(\"Ana\");     // Olá, Ana! Seja bem-vindo(a).",
                    "    echo \"<br>\";",
                    "    echo saudacao(\"Bruno\");   // Olá, Bruno! Seja bem-vindo(a).",
                    "?>",
                ]}),
                ("tabela", {"titulo": "Anatomia da função",
                            "cab": ["Peça", "Papel", "No exemplo"],
                            "lin": [
                                ["function nome", "Define a função", "function saudacao"],
                                ["parâmetro", "Valor que ENTRA (dentro dos parênteses)", "$nome"],
                                ["return", "Valor que SAI (e encerra a função)", "return \"Olá, ...\""],
                                ["chamada", "Usar a função: nome(valor)", "saudacao(\"Ana\")"],
                            ]}),
                ("conceito", ("Parâmetro × argumento × retorno",
                              "<b>Parâmetro</b>: a “variável de entrada” na definição ($nome). "
                              "<b>Argumento</b>: o valor passado na chamada (\"Ana\"). <b>Retorno</b>: o que a "
                              "função devolve com return — quem chama decide o que fazer com ele (exibir, "
                              "guardar em variável, comparar...). Sem return, a função devolve null.")),
                ("h", "Funções com vários parâmetros e valor padrão"),
                ("codigo", {"titulo": "Mais exemplos", "ling": "php", "linhas": [
                    "<?php",
                    "    function soma($a, $b) {",
                    "        return $a + $b;",
                    "    }",
                    "",
                    "    function areaRetangulo($base, $altura = 1) {   // altura opcional",
                    "        return $base * $altura;",
                    "    }",
                    "",
                    "    echo soma(3, 4);            // 7",
                    "    echo areaRetangulo(5);      // 5 (altura padrão = 1)",
                    "    echo areaRetangulo(5, 2);   // 10",
                    "?>",
                ]}),
                ("dica", "Boas práticas: nome de função descreve a ação em verbo (calcularMedia, "
                         "verificarIdade); uma função faz <b>uma</b> tarefa; documentação com comentário antes "
                         "da definição."),
            ],
            "slides": {
                "pontos": [
                    "Função = bloco nomeado que faz UMA tarefa",
                    "function nome($parametro) { return resultado; }",
                    "Parâmetro entra · return sai · chamada usa",
                    "Vários parâmetros: function soma($a, $b)",
                    "Valor padrão: $altura = 1 (parâmetro opcional)",
                ],
                "codigo": {"titulo": "Função de saudação", "linhas": [
                    "function saudacao($nome) {",
                    "    return \"Olá, $nome!\";",
                    "}",
                    "echo saudacao(\"Ana\");",
                ]},
                "nota": "Analogia: máquina de suco — entra fruta (parâmetro), sai suco (retorno). A máquina "
                        "(função) não precisa ser refeita a cada uso.",
            },
        },
        {
            "num": 46,
            "titulo": "Funções na prática — utilitários do sistema",
            "blocos": [
                ("h", "Funções que usaremos no projeto final"),
                ("codigo", {"titulo": "funcoes.php — caixa de ferramentas", "ling": "php", "linhas": [
                    "<?php",
                    "    // Calcula a média de duas notas",
                    "    function calcularMedia($nota1, $nota2) {",
                    "        return ($nota1 + $nota2) / 2;",
                    "    }",
                    "",
                    "    // Verifica se é maior de idade",
                    "    function verificarMaioridade($idade) {",
                    "        return $idade >= 18;",
                    "    }",
                    "",
                    "    // Calcula o preço com desconto",
                    "    function calcularDesconto($preco, $percentual) {",
                    "        return $preco - ($preco * $percentual / 100);",
                    "    }",
                    "",
                    "    // Formata a situação do aluno",
                    "    function situacao($media) {",
                    "        if ($media >= 7)  return \"Aprovado\";",
                    "        if ($media >= 5)  return \"Recuperação\";",
                    "        return \"Reprovado\";",
                    "    }",
                    "?>",
                ]}),
                ("p", "Qualquer página do projeto pode usar essas funções bastando incluir o arquivo:"),
                ("codigo", {"titulo": "Usando as funções em outra página", "ling": "php", "linhas": [
                    "<?php",
                    "    require_once \"funcoes.php\";",
                    "",
                    "    $media = calcularMedia(8.0, 6.5);",
                    "    echo \"Média: $media <br>\";                 // 7.25",
                    "    echo \"Situação: \" . situacao($media);       // Aprovado",
                    "    echo \"<br>\";",
                    "    echo \"Maior de idade? \";",
                    "    echo verificarMaioridade(17) ? \"Sim\" : \"Não\";   // Não",
                    "    echo \"<br>Preço final: R$ \" . calcularDesconto(100, 15);  // 85",
                    "?>",
                ]}),
                ("conceito", ("Funções que retornam true/false",
                              "verificarMaioridade devolve um <b>booleano</b> — ideal para usar direto em "
                              "condições: <b>if (verificarMaioridade($idade)) { ... }</b>. A expressão "
                              "<b>cond ? \"Sim\" : \"Não\"</b> é o operador ternário: um if/else de uma linha "
                              "(condição ? valor se true : valor se false).")),
                ("dica", "Organização real: salve as funções em <b>funcoes.php</b> (ou em includes/) e use "
                         "<b>require_once</b> nas páginas — assim elas ficam disponíveis no projeto inteiro, "
                         "como uma caixa de ferramentas."),
            ],
            "slides": {
                "pontos": [
                    "calcularMedia, verificarMaioridade, calcularDesconto, situacao",
                    "Funções retornam valores: número, texto ou true/false",
                    "if (verificarMaioridade($idade)) — booleano direto na condição",
                    "Ternário: cond ? 'Sim' : 'Não'",
                    "funcoes.php + require_once = caixa de ferramentas do projeto",
                ],
                "codigo": {"titulo": "Utilitários", "linhas": [
                    "function calcularMedia($n1, $n2) {",
                    "    return ($n1 + $n2) / 2;",
                    "}",
                    "function situacao($media) {",
                    "    if ($media >= 7) return \"Aprovado\";",
                    "    if ($media >= 5) return \"Recuperação\";",
                    "    return \"Reprovado\";",
                    "}",
                ]},
                "nota": "Cada grupo implementa e testa as 4 funções. Desafio: função formatarPreco($v) que "
                        "devolve 'R$ 1.234,56' (number_format).",
            },
        },
        {
            "num": 47,
            "titulo": "Arrays multidimensionais",
            "blocos": [
                ("h", "Array de arrays"),
                ("p", "Um <b>array multidimensional</b> é um array cujos elementos <b>também são arrays</b>. "
                      "É assim que guardamos uma <b>lista de registros</b> (vários alunos, cada um com seus "
                      "campos):"),
                ("codigo", {"titulo": "Lista de alunos (array de fichas)", "ling": "php", "linhas": [
                    "<?php",
                    "    $alunos = [",
                    "        [\"nome\" => \"Ana\",   \"nota1\" => 8.0, \"nota2\" => 9.0],",
                    "        [\"nome\" => \"Bruno\", \"nota1\" => 6.0, \"nota2\" => 7.0],",
                    "        [\"nome\" => \"Carla\", \"nota1\" => 9.5, \"nota2\" => 8.5],",
                    "    ];",
                    "",
                    "    // acesso direto: aluno da posição 0, campo nome",
                    "    echo $alunos[0][\"nome\"];    // Ana",
                    "?>",
                ]}),
                ("h", "foreach aninhado — percorrendo as duas dimensões"),
                ("codigo", {"titulo": "Percorrendo a lista completa", "ling": "php", "linhas": [
                    "<?php",
                    "    foreach ($alunos as $aluno) {          // 1ª dimensão: cada aluno",
                    "        echo \"Aluno: \" . $aluno[\"nome\"] . \"<br>\";",
                    "        foreach ($aluno as $campo => $valor) {   // 2ª dimensão: cada campo",
                    "            echo \"&nbsp;&nbsp;$campo = $valor <br>\";",
                    "        }",
                    "        echo \"<hr>\";",
                    "    }",
                    "?>",
                ]}),
                ("conceito", ("Lendo a estrutura",
                              "$alunos é uma <b>lista</b> (índices 0, 1, 2). Cada posição guarda uma "
                              "<b>ficha</b> (array associativo com nome, nota1, nota2). Por isso o acesso usa "
                              "<b>dois colchetes</b>: $alunos[0][\"nome\"] = “na lista, posição 0; na ficha, "
                              "campo nome”. É exatamente a estrutura de uma <b>tabela</b>: linhas (alunos) × "
                              "colunas (campos).")),
                ("h", "Calculando com os dados"),
                ("codigo", {"titulo": "Média de cada aluno + média da turma", "ling": "php", "linhas": [
                    "<?php",
                    "    $somaTurma = 0;",
                    "    foreach ($alunos as $aluno) {",
                    "        $media = ($aluno[\"nota1\"] + $aluno[\"nota2\"]) / 2;",
                    "        echo $aluno[\"nome\"] . \": média $media <br>\";",
                    "        $somaTurma += $media;",
                    "    }",
                    "    echo \"Média da turma: \" . ($somaTurma / count($alunos));",
                    "?>",
                ]}),
            ],
            "slides": {
                "pontos": [
                    "Array multidimensional = array de arrays (lista de fichas)",
                    "$alunos[0]['nome'] → lista, posição 0, campo nome",
                    "Estrutura de tabela: linhas (alunos) × colunas (campos)",
                    "foreach aninhado: 1º cada aluno, 2º cada campo",
                    "Padrão: calcular média por aluno + acumular a da turma",
                ],
                "codigo": {"titulo": "Lista de alunos", "linhas": [
                    "$alunos = [",
                    "  [\"nome\"=>\"Ana\", \"nota1\"=>8.0, \"nota2\"=>9.0],",
                    "  [\"nome\"=>\"Bruno\", \"nota1\"=>6.0, \"nota2\"=>7.0],",
                    "];",
                    "echo $alunos[0][\"nome\"];  // Ana",
                ]},
                "nota": "Desenhar a estrutura no quadro como tabela. Este array é o 'banco de dados' do projeto "
                        "da aula 48 e do projeto final.",
            },
        },
        {
            "num": 48,
            "titulo": "Projeto: listagem dinâmica de alunos (semana da A2)",
            "blocos": [
                ("h", "PHP gerando tabela HTML"),
                ("p", "O projeto da aula junta tudo: um array multidimensional de alunos + foreach gerando as "
                      "linhas da tabela + função de situação:"),
                ("codigo", {"titulo": "listar.php — listagem dinâmica completa", "ling": "php", "linhas": [
                    "<?php require_once \"includes/cabecalho.php\"; ?>",
                    "<?php",
                    "    $alunos = [",
                    "        [\"nome\" => \"Ana\",   \"curso\" => \"Informática\", \"nota\" => 9.0],",
                    "        [\"nome\" => \"Bruno\", \"curso\" => \"Redes\",       \"nota\" => 6.0],",
                    "        [\"nome\" => \"Carla\", \"curso\" => \"Informática\", \"nota\" => 7.5],",
                    "    ];",
                    "    function situacao($nota) {",
                    "        if ($nota >= 7) return \"Aprovado\";",
                    "        if ($nota >= 5) return \"Recuperação\";",
                    "        return \"Reprovado\";",
                    "    }",
                    "?>",
                    "<h2>Alunos matriculados (<?= count($alunos) ?>)</h2>",
                    "<table border=\"1\">",
                    "  <thead>",
                    "    <tr><th>Nome</th><th>Curso</th><th>Nota</th><th>Situação</th></tr>",
                    "  </thead>",
                    "  <tbody>",
                    "  <?php foreach ($alunos as $a): ?>",
                    "    <tr>",
                    "      <td><?= $a[\"nome\"] ?></td>",
                    "      <td><?= $a[\"curso\"] ?></td>",
                    "      <td><?= $a[\"nota\"] ?></td>",
                    "      <td><?= situacao($a[\"nota\"]) ?></td>",
                    "    </tr>",
                    "  <?php endforeach; ?>",
                    "  </tbody>",
                    "</table>",
                    "<?php include \"includes/rodape.php\"; ?>",
                ]}),
                ("conceito", ("O poder da geração dinâmica",
                              "Repare: escrevemos as tags &lt;tr&gt;/&lt;td&gt; <b>uma única vez</b>; o foreach as "
                              "<b>repete para cada aluno</b>. Com 3 ou 300 alunos, o código é o mesmo — só o "
                              "array muda. É assim que sistemas reais exibem listas de produtos, pedidos, "
                              "contatos... E no projeto final, é assim que será a sua listagem.")),
                ("atencao", "<b>AVALIAÇÃO 2 (A2 — 30 pts) nesta aula/semana 16 (S)</b>: prova obrigatória "
                            "(pode ser em duplas ou com consulta, conforme o Plano de Ensino) sobre HTML "
                            "(estrutura a formulários), PHP (variáveis a arrays/funções) e GET/POST/validação. "
                            "Modelo de prova na seção <b>Avaliações</b> desta apostila — estudem por ele!"),
            ],
            "slides": {
                "pontos": [
                    "Projeto da aula: listar.php com tabela dinâmica",
                    "foreach gera <tr>/<td> para cada aluno — código único",
                    "3 ou 300 alunos: o mesmo código (só o array muda)",
                    "Integra: include + funções + arrays multidimensionais",
                    "⚠ AVALIAÇÃO 2 (30 pts) — semana 16: HTML + PHP + GET/POST",
                ],
                "codigo": {"titulo": "Linha dinâmica", "linhas": [
                    "<?php foreach ($alunos as $a): ?>",
                    "  <tr>",
                    "    <td><?= $a[\"nome\"] ?></td>",
                    "    <td><?= situacao($a[\"nota\"]) ?></td>",
                    "  </tr>",
                    "<?php endforeach; ?>",
                ]},
                "nota": "Revisão estratégica antes da A2: percorrer o checklist do módulo e resolver o modelo "
                        "de prova da apostila como estudo dirigido.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Cabeçalho e rodapé reutilizáveis", "tipo": "pratico",
            "enunciado": "Na pasta do seu projeto, crie <b>includes/cabecalho.php</b> (DOCTYPE, head, título, "
                         "menu com 3 links) e <b>includes/rodape.php</b> (footer com o ano atual via date(\"Y\")). "
                         "Reescreva index.php, cadastro.php e listar.php usando os includes.",
            "esperado": "3 páginas exibindo o mesmo cabeçalho/rodapé; alterar o título do menu uma única vez "
                        "atualiza todas as páginas.",
            "orientacao": "Testar clicando no menu em todas as páginas (caminhos relativos!). Desafio: destacar "
                          "no menu a página atual.",
        },
        {
            "num": 2, "titulo": "Caixa de ferramentas (funções)", "tipo": "pratico",
            "enunciado": "Crie <b>funcoes.php</b> com: calcularMedia($n1, $n2), verificarMaioridade($idade), "
                         "calcularDesconto($preco, $percentual) e situacao($media). Crie <b>teste_funcoes.php</b> "
                         "que as chame com valores de teste e exiba os resultados.",
            "esperado": "Testes: media(8, 6.5) = 7.25 · maioridade(17) = false · desconto(100, 15) = 85 · "
                        "situacao(7.25) = 'Aprovado'.",
            "orientacao": "Verificar uso correto de return (e não echo dentro da função — a função devolve, "
                          "quem chama exibe). Discutir por que isso importa (reaproveitamento).",
        },
        {
            "num": 3, "titulo": "Lista de alunos com médias", "tipo": "pratico",
            "enunciado": "Crie um array multidimensional com 4 alunos (nome, nota1, nota2). Com foreach: exiba "
                         "nome e média de cada um (usando calcularMedia do exercício 2) e a situação; ao final, "
                         "a média geral da turma.",
            "esperado": "4 linhas 'Nome — média — situação' + média da turma, usando require_once 'funcoes.php'.",
            "orientacao": "Este exercício é a base direta do projeto da aula 48 e da listagem do projeto final.",
        },
        {
            "num": 4, "titulo": "Listagem dinâmica em tabela", "tipo": "pratico",
            "enunciado": "Transforme o exercício 3 em <b>listar.php</b>: tabela HTML com thead/tbody gerada por "
                         "foreach (colunas: Nome, Média, Situação) + tfoot com a média da turma em colspan. "
                         "Use cabecalho/rodape via include.",
            "esperado": "Página completa: menu do include, tabela dinâmica com 4 linhas e tfoot com média geral.",
            "orientacao": "Checklist: <?= ?> usado corretamente? endforeach presente? tfoot com colspan? "
                          "Compare as soluções dos grupos no projetor.",
        },
    ],
    "teste_rapido": [
        {"enunciado": "A principal vantagem de usar include para o cabeçalho do site é:",
         "alt": ["a página carrega mais rápido no navegador.",
                 "escrever o cabeçalho uma única vez e reutilizá-lo em todas as páginas.",
                 "o Google indexa melhor o site.",
                 "include adiciona estilos CSS automaticamente."],
         "resposta": 1,
         "comentario": "Reutilização e manutenção: mudar o cabeçalho em um único arquivo atualiza o site inteiro."},
        {"enunciado": "Qual a diferença entre include e require quando o arquivo não é encontrado?",
         "alt": ["Não há diferença.",
                 "include gera erro fatal; require apenas avisa.",
                 "require gera erro fatal (para a página); include emite warning e continua.",
                 "require só funciona com arquivos PHP e include com HTML."],
         "resposta": 2,
         "comentario": "require = essencial (falhou, para tudo); include = opcional (falhou, avisa e segue)."},
        {"enunciado": "O que a função a seguir retorna? <b>function dobro($x) { $x * 2; }</b> (chamada: "
                    "dobro(5))",
         "alt": ["10", "5", "0", "null — falta a palavra-chave return."],
         "resposta": 3,
         "comentario": "Sem return, a função não devolve nada (null). O correto: return $x * 2;"},
        {"enunciado": "Dado $alunos = [[\"nome\" => \"Ana\", \"nota\" => 9]], como acessar a nota da primeira "
                    "aluna?",
         "alt": ["$alunos[\"nota\"]", "$alunos[0][\"nota\"]", "$alunos[1][\"nota\"]", "$alunos[0][0]"],
         "resposta": 1,
         "comentario": "Dois colchetes: posição na lista ([0]) + campo da ficha ([\"nota\"])."},
        {"enunciado": "Em uma página PHP que gera uma tabela com 50 produtos a partir de um array, as tags "
                    "<tr>/<td> são escritas:",
         "alt": ["50 vezes, uma para cada produto.",
                 "uma única vez dentro do foreach, que repete a linha para cada produto.",
                 "no CSS, que monta a tabela.",
                 "pelo navegador, automaticamente."],
         "resposta": 1,
         "comentario": "Geração dinâmica: o foreach repete o bloco HTML para cada item do array — o código não "
                       "cresce com a quantidade de dados."},
    ],
    "avaliacao_ref": "A2",
}

MODULO_11 = {
    "num": 11,
    "titulo": "Formulários + PHP",
    "parte_num": 4,
    "parte_titulo": "Formulários + PHP",
    "aulas_faixa": "Aulas 37 a 42",
    "semanas": "Semanas 13 e 14",
    "objetivos": [
        "Enviar dados de formulários com os métodos GET e POST.",
        "Ler os dados enviados com $_GET e $_POST.",
        "Validar campos com isset() e empty().",
        "Sanitizar dados com htmlspecialchars() (segurança básica).",
        "Construir o fluxo completo: formulário → processamento → validação → resultado.",
    ],
    "aulas": [
        {
            "num": 37,
            "titulo": "Método GET e a superglobal $_GET",
            "blocos": [
                ("h", "Enviando dados pela URL"),
                ("p", "No módulo 5 criamos formulários HTML; agora eles ganham vida: o <b>PHP recebe e processa</b> "
                      "os dados. Com <b>method=\"get\"</b>, os dados viajam <b>na própria URL</b>, após um "
                      "<b>?</b>, no formato nome=valor:"),
                ("codigo", {"titulo": "busca.html — formulário GET", "ling": "html", "linhas": [
                    "<form action=\"buscar.php\" method=\"get\">",
                    "    <label for=\"q\">Buscar produto:</label>",
                    "    <input type=\"text\" id=\"q\" name=\"produto\">",
                    "    <button type=\"submit\">Buscar</button>",
                    "</form>",
                ]}),
                ("codigo", {"titulo": "buscar.php — recebendo com $_GET", "ling": "php", "linhas": [
                    "<?php",
                    "    // após buscar 'notebook', a URL fica:",
                    "    // buscar.php?produto=notebook",
                    "",
                    "    $produto = $_GET[\"produto\"];",
                    "    echo \"Você buscou por: $produto\";",
                    "?>",
                ]}),
                ("conceito", ("$_GET é um array!",
                              "<b>$_GET</b> é um <b>array associativo</b> criado automaticamente pelo PHP com "
                              "tudo o que veio na URL: a chave é o <b>name</b> do campo no formulário; o valor é "
                              "o que o usuário digitou. Por isso o atributo <b>name</b> é obrigatório em todo "
                              "campo que será processado!")),
                ("h", "Características do GET"),
                ("lista", [
                    "Dados <b>visíveis na URL</b> — qualquer um vê (e pode alterar!);",
                    "Limitado a URLs curtas (poucos dados);",
                    "Fica no <b>histórico</b> e pode ser <b>favoritado</b>;",
                    "<b>Bom para</b>: buscas, filtros, paginação — dados públicos;",
                    "<b>Ruim para</b>: senhas e dados pessoais (nunca usar GET para isso!).",
                ]),
                ("dica", "Teste alterar a URL manualmente: digite buscar.php?produto=celular direto na barra de "
                         "endereços — o resultado muda. Isso mostra a transparência (e o perigo) do GET."),
            ],
            "slides": {
                "pontos": [
                    "method='get': dados viajam na URL (?nome=valor)",
                    "$_GET['name_do_campo'] lê o valor no PHP",
                    "$_GET é um array associativo automático",
                    "Visível, limitado, favoritado — bom para buscas/filtros",
                    "NUNCA enviar senha/dados pessoais por GET",
                ],
                "codigo": {"titulo": "GET na prática", "linhas": [
                    "<form action=\"buscar.php\" method=\"get\">",
                    "  <input type=\"text\" name=\"produto\">",
                    "</form>",
                    "// buscar.php?produto=notebook",
                    "$produto = $_GET[\"produto\"];",
                ]},
                "nota": "Demonstrar a alteração manual da URL. Pergunta: 'por que não enviar senha por GET?' — "
                        "ela ficaria visível e no histórico.",
            },
        },
        {
            "num": 38,
            "titulo": "Método POST e $_POST",
            "blocos": [
                ("h", "Dados no corpo da requisição"),
                ("p", "Com <b>method=\"post\"</b>, os dados viajam <b>no corpo da requisição HTTP</b> — invisíveis "
                      "na URL. O PHP os entrega no array <b>$_POST</b>:"),
                ("codigo", {"titulo": "contato.html + contato.php", "ling": "php", "linhas": [
                    "<!-- contato.html -->",
                    "<form action=\"contato.php\" method=\"post\">",
                    "    <label for=\"n\">Nome:</label>",
                    "    <input type=\"text\" id=\"n\" name=\"nome\">",
                    "    <label for=\"e\">E-mail:</label>",
                    "    <input type=\"email\" id=\"e\" name=\"email\">",
                    "    <button type=\"submit\">Enviar</button>",
                    "</form>",
                    "",
                    "<!-- contato.php -->",
                    "<?php",
                    "    $nome  = $_POST[\"nome\"];",
                    "    $email = $_POST[\"email\"];",
                    "    echo \"Obrigado, $nome! Confirmação enviada para $email.\";",
                    "?>",
                ]}),
                ("h", "GET × POST — comparativo"),
                ("tabela", {"titulo": "Quando usar cada método",
                            "cab": ["", "GET", "POST"],
                            "lin": [
                                ["Onde viajam os dados", "Na URL (após ?)", "No corpo da requisição"],
                                ["Visibilidade", "Todos veem (URL, histórico)", "Não aparecem na URL"],
                                ["Limite de tamanho", "Sim (URL curta)", "Praticamente sem limite"],
                                ["Favoritar/repetir", "Sim — a URL guarda os dados", "Não (reenvio pede confirmação)"],
                                ["Leitura no PHP", "$_GET[\"campo\"]", "$_POST[\"campo\"]"],
                                ["Uso típico", "Buscas, filtros, links", "Cadastros, logins, formulários"],
                            ]}),
                ("conceito", ("Regra de ouro",
                              "<b>GET</b> para <b>consultar</b> (a ação não altera nada: buscar, filtrar). "
                              "<b>POST</b> para <b>enviar dados sensíveis ou alterar algo</b> (cadastrar, "
                              "editar, excluir, login). Na dúvida em formulários de cadastro: <b>POST</b>.")),
            ],
            "slides": {
                "pontos": [
                    "method='post': dados no corpo da requisição (URL limpa)",
                    "$_POST['campo'] lê o valor enviado",
                    "GET = consultar (busca, filtro) · POST = enviar/cadastrar",
                    "POST: sem limite prático, não fica no histórico",
                    "Cadastros e logins: sempre POST",
                ],
                "codigo": {"titulo": "POST", "linhas": [
                    "<form action=\"contato.php\" method=\"post\">",
                    "  <input type=\"text\" name=\"nome\">",
                    "</form>",
                    "$nome = $_POST[\"nome\"];",
                ]},
                "nota": "Repetir o formulário da aula anterior com POST e comparar: a URL ficou limpa. Tabela "
                        "GET × POST no quadro com participação da turma.",
            },
        },
        {
            "num": 39,
            "titulo": "Validação: isset() e empty()",
            "blocos": [
                ("h", "Nunca confie nos dados do usuário"),
                ("p", "O usuário pode enviar o formulário vazio, alterar a URL (GET) ou usar ferramentas para "
                      "forjar requisições. Por isso o servidor <b>sempre valida</b> o que chegou — mesmo que o "
                      "HTML tenha required (ele pode ser contornado!)."),
                ("conceito", ("As duas funções-chave",
                              "<b>isset($x)</b>: verifica se a variável/campo <b>foi enviado</b> (existe). "
                              "<b>empty($x)</b>: verifica se o valor está <b>vazio</b> (\"\", 0, null, false). "
                              "Padrão de validação: primeiro isset (veio?), depois empty (veio preenchido?).")),
                ("codigo", {"titulo": "processar.php — validação de campos obrigatórios", "ling": "php", "linhas": [
                    "<?php",
                    "    if ($_SERVER[\"REQUEST_METHOD\"] === \"POST\") {",
                    "",
                    "        // 1) o campo foi enviado?",
                    "        if (!isset($_POST[\"nome\"])) {",
                    "            die(\"Campo nome não recebido.\");",
                    "        }",
                    "",
                    "        // 2) veio preenchido?",
                    "        if (empty($_POST[\"nome\"])) {",
                    "            die(\"Erro: o nome é obrigatório.\");",
                    "        }",
                    "",
                    "        $nome = $_POST[\"nome\"];",
                    "        echo \"Cadastro recebido, $nome!\";",
                    "    }",
                    "?>",
                ]}),
                ("h", "Validando vários campos"),
                ("codigo", {"titulo": "Coletando erros de todos os campos", "ling": "php", "linhas": [
                    "<?php",
                    "    $erros = [];",
                    "",
                    "    if (empty($_POST[\"nome\"]))  $erros[] = \"Nome é obrigatório.\";",
                    "    if (empty($_POST[\"email\"])) $erros[] = \"E-mail é obrigatório.\";",
                    "",
                    "    if (count($erros) > 0) {",
                    "        foreach ($erros as $erro) echo \"$erro <br>\";",
                    "    } else {",
                    "        echo \"Tudo certo! Processando cadastro...\";",
                    "    }",
                    "?>",
                ]}),
                ("dica", "O padrão do array $erros (acima) é profissional: valida <b>tudo</b> e mostra "
                         "<b>todos</b> os erros de uma vez — em vez de corrigir um, enviar, descobrir outro..."),
                ("atencao", "Checkbox não marcado <b>não é enviado</b> pelo formulário: isset($_POST[\"termos\"]) "
                            "será false. Para saber se foi marcado, teste o isset."),
            ],
            "slides": {
                "pontos": [
                    "NUNCA confiar nos dados do usuário — validar no servidor",
                    "isset($x): o campo foi enviado?",
                    "empty($x): o valor está vazio?",
                    "Padrão: array $erros[] — valida tudo, mostra todos os erros",
                    "required do HTML ajuda, mas pode ser contornado!",
                ],
                "codigo": {"titulo": "Validação padrão", "linhas": [
                    "$erros = [];",
                    "if (empty($_POST[\"nome\"]))",
                    "    $erros[] = \"Nome obrigatório.\";",
                    "if (count($erros) > 0) { /* exibir erros */ }",
                    "else { /* processar */ }",
                ]},
                "nota": "Demonstrar o required sendo contornado (F12 → remover atributo → enviar vazio). "
                        "Impacto forte: validação no servidor é inegociável.",
            },
        },
        {
            "num": 40,
            "titulo": "Sanitização e segurança básica",
            "blocos": [
                ("h", "O risco de exibir dados sem tratamento"),
                ("p", "Se exibirmos na página exatamente o que o usuário digitou, alguém pode enviar "
                      "<b>código</b> em vez de texto — por exemplo <b>&lt;script&gt;</b> — que seria executado "
                      "no navegador de outros visitantes. Esse ataque chama-se <b>XSS</b> (cross-site "
                      "scripting). A defesa básica: <b>sanitizar</b> a saída."),
                ("conceito", ("htmlspecialchars()",
                              "A função <b>htmlspecialchars($texto)</b> converte caracteres especiais de HTML "
                              "em entidades inofensivas: <b>&lt;</b> vira &amp;lt;, <b>&gt;</b> vira &amp;gt;, "
                              "<b>&amp;</b> vira &amp;amp; e aspas também. O texto aparece <b>normal na "
                              "tela</b>, mas <b>nunca é interpretado como código</b>.")),
                ("codigo", {"titulo": "comentarios.php — exibição segura", "ling": "php", "linhas": [
                    "<?php",
                    "    // usuário mal-intencionado digitou no campo 'mensagem':",
                    "    $mensagem = \"<script>alert('hackeado!')</script>\";",
                    "",
                    "    // JEITO PERIGOSO — executa o script na página:",
                    "    // echo $mensagem;",
                    "",
                    "    // JEITO SEGURO — mostra como texto inofensivo:",
                    "    echo htmlspecialchars($mensagem);",
                    "    // exibe: <script>alert('hackeado!')</script>",
                    "?>",
                ]}),
                ("h", "Regra do curso"),
                ("lista_num", [
                    "<b>Valide</b> a entrada (isset/empty — aula 39);",
                    "<b>Sanitize</b> a saída: todo dado do usuário exibido na página passa por "
                    "<b>htmlspecialchars()</b>;",
                    "Mensagem de erro clara para o usuário (sem detalhes técnicos).",
                ]),
                ("dica", "Guarde o dado <b>como foi enviado</b> (validado) e aplique htmlspecialchars <b>na "
                         "hora de exibir</b>. Em Programação para Internet II veremos sanitização avançada para "
                         "bancos de dados (prepared statements)."),
                ("atencao", "Sanitizar não é opcional “porque ninguém vai atacar meu site de estudos”: é "
                            "<b>hábito profissional</b>. Escreva sempre echo htmlspecialchars($dado); — vira "
                            "automático."),
            ],
            "slides": {
                "pontos": [
                    "Exibir dado bruto do usuário = risco de XSS (código injetado)",
                    "htmlspecialchars($x): < vira &lt; — texto vira texto, não código",
                    "Regra: validar a entrada + sanitizar a saída",
                    "Sempre: echo htmlspecialchars($dado);",
                    "Hábito profissional desde o primeiro projeto",
                ],
                "codigo": {"titulo": "Exibição segura", "linhas": [
                    "$msg = \"<script>alert('x')</script>\";",
                    "echo $msg;                  // PERIGO: executa",
                    "echo htmlspecialchars($msg); // SEGURO: só texto",
                ]},
                "nota": "Demonstração ao vivo do alert() executando sem htmlspecialchars e do mesmo texto "
                        "inofensivo com a função. Momento 'uau' que fixa o conteúdo.",
            },
        },
        {
            "num": 41,
            "titulo": "Formulário completo com confirmação",
            "blocos": [
                ("h", "O fluxo completo"),
                ("p", "Juntando as aulas: um formulário de contato (nome, e-mail, idade, curso e mensagem) com "
                      "POST, validação, sanitização e <b>página de confirmação</b>:"),
                ("codigo", {"titulo": "contato.html", "ling": "html", "linhas": [
                    "<form action=\"confirmar.php\" method=\"post\">",
                    "    <label for=\"nome\">Nome:</label>",
                    "    <input type=\"text\" id=\"nome\" name=\"nome\" required>",
                    "",
                    "    <label for=\"email\">E-mail:</label>",
                    "    <input type=\"email\" id=\"email\" name=\"email\" required>",
                    "",
                    "    <label for=\"idade\">Idade:</label>",
                    "    <input type=\"number\" id=\"idade\" name=\"idade\" min=\"1\" max=\"120\">",
                    "",
                    "    <label for=\"curso\">Curso:</label>",
                    "    <select id=\"curso\" name=\"curso\">",
                    "        <option value=\"informatica\">Informática</option>",
                    "        <option value=\"redes\">Redes</option>",
                    "        <option value=\"adm\">Administração</option>",
                    "    </select>",
                    "",
                    "    <label for=\"msg\">Mensagem:</label>",
                    "    <textarea id=\"msg\" name=\"mensagem\" rows=\"4\"></textarea>",
                    "",
                    "    <button type=\"submit\">Enviar</button>",
                    "</form>",
                ]}),
                ("codigo", {"titulo": "confirmar.php — recebe, valida, sanitiza e confirma", "ling": "php", "linhas": [
                    "<?php",
                    "    $erros = [];",
                    "",
                    "    if (empty($_POST[\"nome\"]))    $erros[] = \"Informe o nome.\";",
                    "    if (empty($_POST[\"email\"]))   $erros[] = \"Informe o e-mail.\";",
                    "    if (empty($_POST[\"mensagem\"])) $erros[] = \"Escreva a mensagem.\";",
                    "",
                    "    if (count($erros) > 0) {",
                    "        echo \"<h2>Corrija os erros:</h2>\";",
                    "        foreach ($erros as $e) echo \"<p>$e</p>\";",
                    "        exit;                       // interrompe: não processa",
                    "    }",
                    "",
                    "    // tudo válido → sanitizar e usar",
                    "    $nome = htmlspecialchars($_POST[\"nome\"]);",
                    "    $email = htmlspecialchars($_POST[\"email\"]);",
                    "    $curso = htmlspecialchars($_POST[\"curso\"]);",
                    "    $msg   = htmlspecialchars($_POST[\"mensagem\"]);",
                    "",
                    "    echo \"<h2>Mensagem recebida!</h2>\";",
                    "    echo \"<p>Nome: $nome</p>\";",
                    "    echo \"<p>E-mail: $email</p>\";",
                    "    echo \"<p>Curso: $curso</p>\";",
                    "    echo \"<p>Mensagem: $msg</p>\";",
                    "?>",
                ]}),
                ("conceito", ("Fluxo em 4 etapas",
                              "1) <b>Preenchimento</b> (HTML: form + labels + required) → 2) <b>Envio</b> "
                              "(method=post, action=confirmar.php) → 3) <b>Processamento</b> (PHP: isset/empty, "
                              "$_POST, validações) → 4) <b>Resultado</b> (confirmação sanitizada ou lista de "
                              "erros). Esse fluxo é o coração de TODO sistema Web — e do seu projeto final.")),
            ],
            "slides": {
                "pontos": [
                    "Fluxo: preenchimento → envio → processamento → resultado",
                    "HTML: form POST com required + label em tudo",
                    "PHP: $erros[] valida todos os campos de uma vez",
                    "exit interrompe em caso de erro",
                    "Confirmação SEMPRE com htmlspecialchars",
                ],
                "codigo": {"titulo": "Núcleo do processamento", "linhas": [
                    "if (empty($_POST[\"nome\"]))",
                    "    $erros[] = \"Informe o nome.\";",
                    "if (count($erros) > 0) {",
                    "    foreach ($erros as $e) echo \"<p>$e</p>\";",
                    "    exit;",
                    "}",
                    "$nome = htmlspecialchars($_POST[\"nome\"]);",
                ]},
                "nota": "Construir o fluxo ao vivo, testando: envio correto, envio vazio, e mensagem com "
                        "<script> (sanitizada).",
            },
        },
        {
            "num": 42,
            "titulo": "Projeto: cadastro de alunos (HTML + PHP)",
            "blocos": [
                ("h", "O projeto do módulo"),
                ("p", "Sistema de cadastro em 2 arquivos: <b>cadastro.html</b> (formulário) + "
                      "<b>processar.php</b> (recebimento, validação e resultado). É o ensaio geral para o "
                      "projeto final:"),
                ("codigo", {"titulo": "cadastro.html", "ling": "html", "linhas": [
                    "<!DOCTYPE html>",
                    "<html lang=\"pt-br\">",
                    "<head><meta charset=\"UTF-8\"><title>Cadastro de aluno</title></head>",
                    "<body>",
                    "    <h1>Cadastro de aluno</h1>",
                    "    <form action=\"processar.php\" method=\"post\">",
                    "        <label for=\"nome\">Nome:</label>",
                    "        <input type=\"text\" id=\"nome\" name=\"nome\" required>",
                    "",
                    "        <label for=\"email\">E-mail:</label>",
                    "        <input type=\"email\" id=\"email\" name=\"email\" required>",
                    "",
                    "        <label for=\"idade\">Idade:</label>",
                    "        <input type=\"number\" id=\"idade\" name=\"idade\" min=\"10\" max=\"120\">",
                    "",
                    "        <p>Curso:</p>",
                    "        <input type=\"radio\" id=\"inf\" name=\"curso\" value=\"Informática\">",
                    "        <label for=\"inf\">Informática</label>",
                    "        <input type=\"radio\" id=\"red\" name=\"curso\" value=\"Redes\">",
                    "        <label for=\"red\">Redes</label>",
                    "",
                    "        <button type=\"submit\">Cadastrar</button>",
                    "    </form>",
                    "</body>",
                    "</html>",
                ]}),
                ("codigo", {"titulo": "processar.php", "ling": "php", "linhas": [
                    "<?php",
                    "    $erros = [];",
                    "",
                    "    if (empty($_POST[\"nome\"]))   $erros[] = \"Nome é obrigatório.\";",
                    "    if (empty($_POST[\"email\"]))  $erros[] = \"E-mail é obrigatório.\";",
                    "    if (empty($_POST[\"curso\"]))  $erros[] = \"Escolha um curso.\";",
                    "",
                    "    if (!empty($_POST[\"idade\"]) && ($_POST[\"idade\"] < 10",
                    "            || $_POST[\"idade\"] > 120)) {",
                    "        $erros[] = \"Idade inválida (10 a 120).\";",
                    "    }",
                    "",
                    "    if (count($erros) > 0) {",
                    "        echo \"<h2>Erro de validação</h2>\";",
                    "        foreach ($erros as $e) echo \"<p>$e</p>\";",
                    "        echo '<a href=\"cadastro.html\">Voltar</a>';",
                    "        exit;",
                    "    }",
                    "",
                    "    $nome  = htmlspecialchars($_POST[\"nome\"]);",
                    "    $email = htmlspecialchars($_POST[\"email\"]);",
                    "    $curso = htmlspecialchars($_POST[\"curso\"]);",
                    "    $idade = (int) $_POST[\"idade\"];",
                    "",
                    "    echo \"<h2>Cadastro realizado!</h2>\";",
                    "    echo \"<p>Aluno: $nome ($idade anos)</p>\";",
                    "    echo \"<p>Curso: $curso</p>\";",
                    "    echo \"<p>Confirmação enviada para: $email</p>\";",
                    "?>",
                ]}),
                ("h", "Checklist de qualidade do projeto"),
                ("lista", [
                    "Todos os campos com <b>label + name</b> (e id);",
                    "<b>required</b> nos essenciais; number com min/max;",
                    "PHP valida <b>todos</b> os campos (isset/empty) antes de usar;",
                    "Saída sempre com <b>htmlspecialchars</b>;",
                    "Mensagens de erro claras + <b>link para voltar</b> ao formulário;",
                    "Código indentado e comentado.",
                ]),
                ("conceito", ("Limitação que virá no futuro",
                              "Ao recarregar a página, o cadastro “some”: o array vive só durante aquela "
                              "execução. Para <b>guardar de verdade</b> os dados entre acessos usamos arquivos "
                              "ou <b>bancos de dados</b> (MySQL) — conteúdo de Programação para Internet II. No "
                              "projeto final, simularemos a persistência com arrays/sessões conforme orientação "
                              "do professor.")),
            ],
            "slides": {
                "pontos": [
                    "Projeto do módulo: cadastro.html + processar.php",
                    "Fluxo: preenchimento → validação → resultado",
                    "Validação completa: obrigatórios + faixa de idade",
                    "Erros: mensagens claras + link 'Voltar'",
                    "Saída sanitizada com htmlspecialchars",
                    "Persistência real (banco de dados) = PI II",
                ],
                "nota": "Aula prática integral: cada dupla entrega cadastro.html + processar.php funcionando "
                        "com os 3 testes (ok, vazio, idade inválida). Correção pelo checklist.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Busca com GET", "tipo": "pratico",
            "enunciado": "Crie <b>busca.html</b> (campo produto, method=get, action=buscar.php) e "
                         "<b>buscar.php</b> que receba $_GET[\"produto\"], valide (isset/empty) e exiba "
                         "“Resultado da busca por: X” (sanitizado). Teste também digitando a URL manualmente.",
            "esperado": "Busca funcionando; envio vazio mostra erro; URL digitada manualmente funciona; "
                        "saída com htmlspecialchars.",
            "orientacao": "Peça que testem buscar por '&lt;b&gt;teste' e observem a sanitização em ação.",
        },
        {
            "num": 2, "titulo": "Contato com POST e validação completa", "tipo": "pratico",
            "enunciado": "Crie o formulário de contato completo (nome, e-mail, idade, curso em select, mensagem "
                         "em textarea) + confirmar.php com array $erros, validação de todos os campos, "
                         "sanitização e confirmação formatada.",
            "esperado": "Fluxo completo funcionando: envio válido → confirmação; campos vazios → lista de todos "
                        "os erros de uma vez.",
            "orientacao": "Testar os 3 cenários (ok / vazio / parcial). Conferir htmlspecialchars em TODAS as "
                          "saídas.",
        },
        {
            "num": 3, "titulo": "Teste de invasão (sanitização)", "tipo": "pratico",
            "enunciado": "No formulário do exercício 2, digite no campo mensagem: <b>&lt;script&gt;"
                         "alert('XSS')&lt;/script&gt;</b> e também <b>&lt;b&gt;negrito?&lt;/b&gt;</b>. Envie e "
                         "observe o resultado. Depois comente a linha do htmlspecialchars e envie de novo. "
                         "Explique por escrito a diferença.",
            "esperado": "Com htmlspecialchars: os textos aparecem literalmente, nada é executado/aplicado. Sem: "
                        "o alert dispara e 'negrito?' fica em negrito — prova de que o dado foi interpretado "
                        "como código.",
            "orientacao": "Exercício de impacto: deixa o XSS 'visível'. Restaurar o código seguro ao final e "
                          "discutir por que validar só no HTML (required) não basta.",
        },
        {
            "num": 4, "titulo": "Projeto do módulo: cadastro de alunos", "tipo": "pratico",
            "enunciado": "Desenvolva em dupla o sistema <b>cadastro.html + processar.php</b> conforme a aula 42, "
                         "atendendo ao checklist de qualidade (6 itens). Entrega pelo AVA.",
            "esperado": "Sistema completo validando nome/e-mail/curso (obrigatórios) e idade (10–120), com "
                        "mensagens de erro, link 'voltar' e saída sanitizada.",
            "orientacao": "Corrigir com o checklist da aula 42, item a item. Este projeto é pré-requisito "
                          "prático para o projeto final (módulo 12).",
        },
    ],
    "teste_rapido": [
        {"enunciado": "Com method=\"get\", os dados do formulário são enviados:",
         "alt": ["no corpo da requisição, invisíveis.",
                 "na URL, após o ?, no formato nome=valor.",
                 "por e-mail automaticamente.",
                 "em um arquivo temporário no servidor."],
         "resposta": 1,
         "comentario": "GET coloca os dados na URL (visíveis); POST os envia no corpo da requisição."},
        {"enunciado": "Para ler no PHP o campo <b>&lt;input name=\"email\"&gt;</b> enviado por POST, usamos:",
         "alt": ["$_GET[\"email\"]", "$_POST[\"email\"]", "$_FORM[\"email\"]", "$_EMAIL"],
         "resposta": 1,
         "comentario": "O método do form define a superglobal: method=post → $_POST; method=get → $_GET. A "
                       "chave é o name do campo."},
        {"enunciado": "As funções isset() e empty() servem, respectivamente, para verificar se o dado:",
         "alt": ["é numérico e se é texto.",
                 "foi enviado e se está vazio.",
                 "está criptografado e se é seguro.",
                 "é verdadeiro e se é falso."],
         "resposta": 1,
         "comentario": "isset = existe/foi enviado; empty = está vazio (\"\", 0, null, false). Juntas, formam a "
                       "validação básica."},
        {"enunciado": "A função htmlspecialchars() protege a página porque:",
         "alt": ["criptografa a senha do usuário.",
                 "impede o envio do formulário duas vezes.",
                 "converte <, > e aspas em entidades — o dado vira texto, nunca código.",
                 "valida se o e-mail digitado existe."],
         "resposta": 2,
         "comentario": "Sanitização de saída: neutraliza tags/scripts injetados (ataque XSS)."},
        {"enunciado": "Para um formulário de LOGIN (e-mail e senha), o método correto e o motivo são:",
         "alt": ["GET — porque é mais rápido.",
                 "POST — porque os dados não ficam visíveis na URL nem no histórico.",
                 "GET — porque a senha aparece criptografada na URL.",
                 "Tanto faz: os dois são igualmente seguros para senhas."],
         "resposta": 1,
         "comentario": "Dados sensíveis (senha!) nunca por GET: ficariam visíveis na URL, no histórico e em "
                       "logs. POST envia no corpo da requisição."},
    ],
    "avaliacao_ref": None,
}

MODULO_12 = {
    "num": 12,
    "titulo": "Projeto final integrador",
    "parte_num": 6,
    "parte_titulo": "Desenvolvimento do Projeto Final",
    "aulas_faixa": "Aulas 49 a 72",
    "semanas": "Semanas 17 a 24",
    "objetivos": [
        "Planejar uma aplicação Web simples: tema, objetivo, usuários e requisitos.",
        "Estruturar o projeto em pastas e arquivos profissionais.",
        "Desenvolver as páginas: inicial (menu), cadastro (formulário), processamento e listagem dinâmica.",
        "Validar dados, tratar erros e testar todas as funcionalidades (tabela de testes).",
        "Identificar e corrigir erros de sintaxe, lógica e execução.",
        "Preparar e apresentar o projeto final (roteiro, demonstração e avaliação).",
    ],
    "aulas": [
        {
            "num": 49,
            "titulo": "Definição do projeto: grupos e tema",
            "blocos": [
                ("h", "O que é o projeto final"),
                ("p", "Uma <b>aplicação Web simples e funcional</b>, desenvolvida <b>em grupos</b>, integrando "
                      "todo o curso: <b>HTML</b> (estrutura e conteúdo), <b>PHP</b> (processamento e conteúdo "
                      "dinâmico), <b>formulários</b> (entrada de dados), <b>validação</b> (controle dos dados), "
                      "<b>arrays</b> (armazenamento temporário) e <b>organização de arquivos</b> (estrutura do "
                      "projeto)."),
                ("h", "Temas sugeridos"),
                ("tabela", {"titulo": "Escolham UM tema (ou proponham outro ao professor)",
                            "cab": ["Tema", "Cadastro de...", "Listagem de..."],
                            "lin": [
                                ["Cadastro de alunos", "nome, idade, curso, e-mail", "alunos com situação"],
                                ["Agenda de contatos", "nome, telefone, e-mail, categoria", "contatos por categoria"],
                                ["Catálogo de produtos", "nome, categoria, preço, estoque", "produtos com estoque baixo"],
                                ["Sistema de contatos (mensagens)", "nome, e-mail, assunto, mensagem", "mensagens recebidas"],
                                ["Cadastro de clientes", "nome, CPF, cidade, telefone", "clientes por cidade"],
                                ["Biblioteca", "título, autor, gênero, disponível?", "livros e disponibilidade"],
                                ["Controle de tarefas", "título, prazo, prioridade, status", "tarefas por status"],
                            ]}),
                ("h", "Formação dos grupos e divisão de papéis"),
                ("lista", [
                    "Grupos de 3 a 4 alunos (critério do professor);",
                    "Papéis sugeridos: <b>líder/organizador</b>, <b>front-end</b> (HTML/visual), "
                    "<b>back-end</b> (PHP/lógica), <b>testador/documentador</b> — todos programam, mas cada um "
                    "lidera uma frente;",
                    "Combinem: encontros fora da aula (AVA/WhatsApp), repositório ou Drive compartilhado da "
                    "pasta do projeto.",
                ]),
                ("dica", "Escolham um tema que o grupo <b>entenda do assunto</b>: saber como funciona uma "
                         "biblioteca ou uma loja facilita levantar requisitos. Tema simples e bem feito vale "
                         "mais que tema ambicioso pela metade."),
            ],
            "slides": {
                "pontos": [
                    "PROJETO FINAL (aulas 49–72): aplicação Web em grupo",
                    "Integra: HTML + PHP + formulários + validação + arrays + organização",
                    "Temas: alunos · contatos · produtos · clientes · biblioteca · tarefas",
                    "Grupos de 3–4 com papéis definidos",
                    "Simples e COMPLETO > ambicioso e inacabado",
                ],
                "nota": "Aula de formação de grupos e escolha do tema. Encerrar com o tema de cada grupo "
                        "registrado (Entrega 1 começa aqui).",
            },
        },
        {
            "num": 50,
            "titulo": "Levantamento de requisitos",
            "blocos": [
                ("h", "Antes de codificar: planejar"),
                ("p", "<b>Requisitos</b> são as respostas de 5 perguntas sobre o sistema. Escrevê-las evita "
                      "retrabalho — é o que profissionais fazem antes de programar:"),
                ("tabela", {"titulo": "As 5 perguntas do planejamento",
                            "cab": ["Pergunta", "Exemplo (tema: Biblioteca)"],
                            "lin": [
                                ["1. Qual o OBJETIVO do sistema?", "Controlar o acervo e a disponibilidade dos livros"],
                                ["2. QUEM vai usar?", "Bibliotecário (cadastra) e aluno (consulta)"],
                                ["3. QUAIS FUNCIONALIDADES?", "Cadastrar livro, listar acervo, buscar por título"],
                                ["4. QUAIS PÁGINAS?", "index.php, cadastro.php, listar.php, processar.php"],
                                ["5. QUAIS DADOS (campos)?", "título, autor, gênero, ano, disponível (sim/não)"],
                            ]}),
                ("h", "Modelo de documento de requisitos (Entrega 1)"),
                ("codigo", {"titulo": "requisitos.txt — modelo (1 página)", "ling": "texto", "linhas": [
                    "PROJETO FINAL — PROGRAMAÇÃO PARA INTERNET I",
                    "Grupo: nomes · Turma: 2/2026 · Tema: Biblioteca da Escola",
                    "",
                    "1. OBJETIVO: controlar o acervo de livros da biblioteca.",
                    "2. USUÁRIOS: bibliotecário (cadastro) e alunos (consulta).",
                    "3. FUNCIONALIDADES:",
                    "   - Cadastrar livro (título, autor, gênero, ano, disponível)",
                    "   - Listar todos os livros em tabela",
                    "   - Mostrar total de livros e quantos disponíveis",
                    "4. PÁGINAS: index.php · cadastro.php · processar.php · listar.php",
                    "5. DADOS: título (texto, obrigatório) · autor (texto, obrigatório)",
                    "   gênero (select) · ano (número, 1900-2026) · disponível (checkbox)",
                    "6. VALIDAÇÕES: título/autor obrigatórios; ano entre 1900 e 2026.",
                ]}),
                ("conceito", ("Requisito bem escrito é testável",
                              "“O sistema deve ser bonito” não é requisito (como testar?). “A listagem exibe "
                              "título, autor e disponibilidade em tabela com thead” é requisito — dá para "
                              "verificar sim/não. Escrevam requisitos <b>concretos</b>: viram a tabela de "
                              "testes da aula 58!")),
            ],
            "slides": {
                "pontos": [
                    "5 perguntas: objetivo · usuários · funcionalidades · páginas · dados",
                    "Documento de requisitos = Entrega 1 (1 página)",
                    "Requisito bom é concreto e testável",
                    "Campos com tipo e regras (obrigatório, faixa de valores)",
                    "Planejar evita retrabalho — prática profissional",
                ],
                "nota": "Cada grupo preenche o modelo requisitos.txt com seu tema. Professor valida um por um "
                        "(visto = Entrega 1 encaminhada).",
            },
        },
        {
            "num": 51,
            "titulo": "Estrutura do projeto",
            "blocos": [
                ("h", "Criando o esqueleto"),
                ("p", "Com os requisitos definidos, criamos a estrutura de arquivos — exatamente o padrão do "
                      "módulo 10, agora aplicado ao projeto do grupo:"),
                ("codigo", {"titulo": "Estrutura do projeto final", "ling": "texto", "linhas": [
                    "projeto-final-grupo1/",
                    "├── index.php           ← página inicial com o menu",
                    "├── cadastro.php        ← formulário de cadastro",
                    "├── processar.php       ← recebe, valida e confirma",
                    "├── listar.php          ← listagem dinâmica (tabela)",
                    "├── sobre.php           ← sobre o sistema (opcional)",
                    "├── funcoes.php         ← funções utilitárias do grupo",
                    "├── css/",
                    "│   └── estilo.css",
                    "├── imagens/",
                    "│   └── logo.png",
                    "└── includes/",
                    "    ├── cabecalho.php",
                    "    └── rodape.php",
                ]}),
                ("h", "Ordem de construção recomendada"),
                ("lista_num", [
                    "Pastas e arquivos vazios (o esqueleto completo);",
                    "includes/cabecalho.php e rodape.php (menu pronto desde o início!);",
                    "index.php com o menu navegável (testar os links);",
                    "cadastro.php (o formulário HTML completo);",
                    "processar.php (validação + confirmação);",
                    "listar.php (tabela dinâmica);",
                    "funcoes.php (utilitários) e ajustes de interface (css).",
                ]),
                ("dica", "Commit mental: ao terminar cada passo, <b>teste no navegador</b> antes de passar ao "
                         "próximo. Construir tudo e testar só no fim é a receita para uma pilha de erros "
                         "difíceis de achar."),
                ("atencao", "Todo o grupo deve ter a <b>mesma versão</b> dos arquivos (Drive/pendrive "
                            "compartilhado, combinado na aula 49). Arquivo duplicado com nomes diferentes "
                            "(Cadastro.php × cadastro.php) causa bugs ‘fantasma’."),
            ],
            "slides": {
                "pontos": [
                    "Esqueleto: index · cadastro · processar · listar · funcoes",
                    "+ css/ · imagens/ · includes/ (cabecalho e rodape)",
                    "Ordem: estrutura → includes → index → cadastro → processar → listar",
                    "Testar no navegador a cada passo concluído",
                    "Grupo todo com a MESMA versão dos arquivos",
                ],
                "nota": "Aula mão na massa: criar a estrutura e os includes. Meta: sair com o menu navegando "
                        "entre páginas (mesmo que ainda vazias).",
            },
        },
        {
            "num": 52,
            "titulo": "Página inicial, cadastro e processamento",
            "blocos": [
                ("h", "Aulas 52 a 54 — as 3 páginas centrais"),
                ("p", "Semana 18: construímos o núcleo do sistema — <b>index.php</b> (menu), <b>cadastro.php</b> "
                      "(formulário completo) e <b>processar.php</b> (fluxo de recebimento)."),
                ("codigo", {"titulo": "index.php — página inicial com menu", "ling": "php", "linhas": [
                    "<?php require_once \"includes/cabecalho.php\"; ?>",
                    "",
                    "<h2>Bem-vindo ao sistema <?= $nomeSistema ?></h2>",
                    "<p>Escolha uma opção no menu acima:</p>",
                    "<ul>",
                    "    <li><a href=\"cadastro.php\">Cadastrar</a> — incluir novo registro</li>",
                    "    <li><a href=\"listar.php\">Listar</a> — ver os cadastros</li>",
                    "    <li><a href=\"sobre.php\">Sobre</a> — informações do sistema</li>",
                    "</ul>",
                    "",
                    "<?php include \"includes/rodape.php\"; ?>",
                ]}),
                ("h", "cadastro.php — checklist do formulário"),
                ("lista", [
                    "Todos os campos dos requisitos (item 5) presentes;",
                    "Cada campo com <b>label + name + id</b>;",
                    "Tipos certos: text, email, number (min/max), date, select, radio, checkbox;",
                    "<b>required</b> nos obrigatórios; placeholder com exemplo;",
                    "method=\"post\" e action=\"processar.php\";",
                    "botão submit com texto claro (“Cadastrar”).",
                ]),
                ("h", "processar.php — fluxo completo"),
                ("lista_num", [
                    "Confirmar que a requisição é POST ($_SERVER[\"REQUEST_METHOD\"]);",
                    "Validar cada campo: isset/empty + regras (faixa, formato) → array $erros;",
                    "Se houver erros: exibir todos + link “Voltar ao cadastro” + exit;",
                    "Sem erros: sanitizar (htmlspecialchars) e montar a confirmação;",
                    "(Extra do grupo) guardar o registro no array/sessão para a listagem.",
                ]),
                ("dica", "Reaproveitem o projeto do módulo 11 (cadastro de alunos) como base — adaptem os "
                         "campos ao tema do grupo. Não comecem do zero: comecem do que já funciona."),
            ],
            "slides": {
                "pontos": [
                    "index.php: boas-vindas + menu explicativo",
                    "cadastro.php: formulário completo (label, name, required, tipos)",
                    "processar.php: POST? → validar ($erros) → sanitizar → confirmar",
                    "Erros: exibir todos + link voltar + exit",
                    "Reaproveitar o projeto do módulo 11 como base",
                ],
                "nota": "Semana de construção supervisionada. Circule com o checklist; valide o formulário de "
                        "cada grupo antes de partirem para o processar.php.",
            },
        },
        {
            "num": 55,
            "titulo": "Listagem dinâmica, interface e validação do projeto",
            "blocos": [
                ("h", "Aulas 55 a 57 — completar e polir"),
                ("p", "<b>Listagem dinâmica</b> (aula 55): a tabela gerada por foreach a partir dos dados "
                      "cadastrados — padrão da aula 48, com os campos do tema do grupo:"),
                ("codigo", {"titulo": "listar.php — núcleo da listagem", "ling": "php", "linhas": [
                    "<table border=\"1\">",
                    "  <thead>",
                    "    <tr><th>#</th><th>Título</th><th>Autor</th><th>Disponível</th></tr>",
                    "  </thead>",
                    "  <tbody>",
                    "  <?php foreach ($livros as $i => $livro): ?>",
                    "    <tr>",
                    "      <td><?= $i + 1 ?></td>",
                    "      <td><?= htmlspecialchars($livro[\"titulo\"]) ?></td>",
                    "      <td><?= htmlspecialchars($livro[\"autor\"]) ?></td>",
                    "      <td><?= $livro[\"disponivel\"] ? \"Sim\" : \"Não\" ?></td>",
                    "    </tr>",
                    "  <?php endforeach; ?>",
                    "  </tbody>",
                    "  <tfoot>",
                    "    <tr><td colspan=\"4\">Total: <?= count($livros) ?> registros</td></tr>",
                    "  </tfoot>",
                    "</table>",
                ]}),
                ("h", "Interface (aula 56)"),
                ("lista", [
                    "Títulos claros (h1/h2) em cada página;",
                    "Menu consistente (include) e destacado na página atual;",
                    "Mensagens de sucesso/erro visíveis e educadas;",
                    "CSS mínimo de apoio: cores, espaçamento, tabela legível "
                    "(border-collapse, padding nas células);",
                    "Sem texto ‘solto’ sem contexto: tudo com label/título.",
                ]),
                ("h", "Validação do projeto (aula 57)"),
                ("p", "Antes de considerar pronto, o grupo testa o sistema como um todo — checklist:"),
                ("lista", [
                    "Formulário com campos vazios → mensagens corretas?",
                    "Valores inválidos (idade 999, ano 1800) → bloqueados?",
                    "Dados obrigatórios ausentes → erro claro + voltar?",
                    "Navegação: todos os links do menu funcionam de todas as páginas?",
                    "Listagem: mostra os dados cadastrados e o total?",
                    "Texto com &lt;b&gt; ou &lt;script&gt; digitado → exibido como texto (sanitizado)?",
                ]),
            ],
            "slides": {
                "pontos": [
                    "listar.php: foreach → <tr>/<td> + tfoot com count()",
                    "Saída da listagem SEMPRE sanitizada",
                    "Interface: títulos, menu consistente, mensagens claras, CSS mínimo",
                    "Validação do projeto: 6 testes obrigatórios (vazio, inválido, navegação...)",
                    "Entrega 4: listagem dinâmica + interface",
                ],
                "nota": "Cada grupo aplica o checklist de validação no sistema do OUTRO grupo (teste cruzado) — "
                        "achar bugs dos colegas é divertido e formativo.",
            },
        },
        {
            "num": 58,
            "titulo": "Testes: a tabela de testes",
            "blocos": [
                ("h", "Testar é parte de programar"),
                ("p", "Software profissional é <b>testado</b> com método, não “clicando de qualquer jeito”. A "
                      "ferramenta da aula: a <b>tabela de testes</b> — cada linha é um <b>caso de teste</b> com "
                      "<b>entrada</b> e <b>resultado esperado</b>:"),
                ("codigo", {"titulo": "Tabela de testes — exemplo (tema Biblioteca)", "ling": "texto", "linhas": [
                    "│ # │ Teste                │ Entrada                    │ Esperado              │",
                    "│ 1 │ Cadastro válido      │ título/autor ok, ano 2020  │ mensagem de sucesso   │",
                    "│ 2 │ Campos vazios        │ nada preenchido            │ erros de obrigatório  │",
                    "│ 3 │ Ano inválido         │ ano = 1800                 │ erro 'ano inválido'   │",
                    "│ 4 │ Texto com tags       │ título = <b>teste</b>      │ exibido como texto    │",
                    "│ 5 │ Listagem             │ 3 cadastros feitos         │ tabela com 3 linhas   │",
                    "│ 6 │ Navegação            │ menu em todas as páginas   │ links funcionando     │",
                ]}),
                ("h", "Como montar a sua tabela"),
                ("lista_num", [
                    "Liste as funcionalidades do sistema (dos requisitos);",
                    "Para cada uma, crie ao menos: <b>1 teste válido</b>, <b>1 teste inválido</b> e "
                    "<b>1 teste de limite</b> (ex.: ano = 1900 e 2026 exatos);",
                    "Escreva o resultado esperado <b>antes</b> de testar;",
                    "Execute, marque OK/FALHOU e registre o que aconteceu;",
                    "Toda FALHA vira tarefa de correção (aula 59).",
                ]),
                ("conceito", ("Teste de limite (caso de borda)",
                              "Erros gostam de se esconder nas <b>bordas</b>: ano exatamente 1900 (mínimo "
                              "permitido), 2026 (máximo), 1899 (um abaixo), 2027 (um acima), campo com 1 "
                              "caractere, campo enorme... Testar os limites é o que separa um teste amador de "
                              "um teste profissional.")),
            ],
            "slides": {
                "pontos": [
                    "Tabela de testes: teste × entrada × resultado esperado",
                    "Para cada funcionalidade: válido + inválido + limite",
                    "Escrever o esperado ANTES de executar",
                    "Registrar OK/FALHOU — falha vira tarefa de correção",
                    "Casos de borda: exatamente no limite (1900, 2026...)",
                ],
                "nota": "Cada grupo monta a tabela de testes do SEU sistema (mínimo 6 casos). Será usada na "
                        "aula 69 e vale para a Entrega 5.",
            },
        },
        {
            "num": 59,
            "titulo": "Correção de erros (debugging)",
            "blocos": [
                ("h", "Os 3 tipos de erro"),
                ("tabela", {"titulo": "Classificação dos erros",
                            "cab": ["Tipo", "O que é", "Exemplo", "Sintoma"],
                            "lin": [
                                ["Sintaxe", "Código fora das regras da linguagem", "esquecer ; ou fechar aspas",
                                 "mensagem de Parse error com arquivo e linha"],
                                ["Lógica", "Código válido, mas faz a coisa errada",
                                 "média = ($n1+$n2)/3", "sem mensagem — resultado errado"],
                                ["Execução", "Falha durante o funcionamento",
                                 "acessar $alunos[9] que não existe", "Warning/Notice ou página quebrada"],
                            ]}),
                ("h", "A estratégia em 5 passos"),
                ("lista_num", [
                    "<b>Ler</b> a mensagem de erro COMPLETA (ela diz arquivo e linha!);",
                    "<b>Identificar</b> o arquivo e a linha indicados;",
                    "<b>Entender</b> o que o código quis fazer × o que fez (var_dump é seu amigo);",
                    "<b>Corrigir</b> a causa — não o sintoma;",
                    "<b>Testar</b> de novo (e refazer os testes que já passavam).",
                ]),
                ("codigo", {"titulo": "Lendo uma mensagem de erro do PHP", "ling": "texto", "linhas": [
                    "Parse error: syntax error, unexpected token \"echo\",",
                    "expecting \";\" in /htdocs/projeto/listar.php on line 24",
                    "",
                    "  │            │                │            │",
                    "  tipo do erro │                │            arquivo e LINHA",
                    "               o que faltou    o que ele encontrou",
                ]}),
                ("h", "Ferramentas de investigação"),
                ("lista", [
                    "<b>var_dump($variavel)</b> + exit; — para o programa e mostra o conteúdo;",
                    "<b>echo</b> estratégico — “chegou aqui”, “valor = $x”;",
                    "<b>Comentar</b> blocos (//) para isolar a parte problemática;",
                    "<b>F12 → Console</b> no navegador — erros de HTML/JS;",
                    "Testar com <b>entradas simples</b> (números redondos, textos curtos).",
                ]),
                ("dica", "Erro de lógica é o mais traiçoeiro (não aparece mensagem!). Defesa: escreva o "
                         "resultado esperado ANTES (tabela de testes) e compare. Se differiu, var_dump nas "
                         "variáveis do cálculo."),
                ("atencao", "Resista ao impulso de reescrever o arquivo inteiro quando algo falha. Localize "
                            "primeiro: 90% dos erros estão em 1 linha. Reescrever sem entender = o erro volta."),
            ],
            "slides": {
                "pontos": [
                    "3 tipos: SINTAXE (parse error) · LÓGICA (resultado errado) · EXECUÇÃO (warning)",
                    "Mensagem do PHP diz: tipo + arquivo + LINHA",
                    "Estratégia: ler → identificar → entender → corrigir → testar",
                    "Ferramentas: var_dump + exit, echo 'chegou aqui', comentar blocos",
                    "Erro de lógica não avisa — tabela de testes pega",
                ],
                "codigo": {"titulo": "Anatomia do erro", "linhas": [
                    "Parse error: syntax error, unexpected token \"echo\"",
                    "in /htdocs/projeto/listar.php on line 24",
                    "→ abrir listar.php, olhar a LINHA 24 (e a anterior!)",
                ]},
                "nota": "Atividade 'caça-erros': distribuir códigos com 3 erros plantados (um de cada tipo). "
                        "Grupos competem para achar e corrigir usando a estratégia.",
            },
        },
        {
            "num": 60,
            "titulo": "Revisão geral da ementa",
            "blocos": [
                ("h", "Revisão cumulativa — preparação para a prova final"),
                ("p", "A aula 60 revisa <b>toda a ementa</b>: Internet e Web, HTML (estrutura a formulários) e "
                      "PHP (variáveis a GET/POST). Use o mapa abaixo como roteiro de estudo:"),
                ("tabela", {"titulo": "Mapa da revisão",
                            "cab": ["Bloco", "Conceitos essenciais", "Módulos"],
                            "lin": [
                                ["Internet e Web", "cliente/servidor, HTTP(S), URL, IP, DNS, domínio, hospedagem, portal, e-commerce", "1"],
                                ["Ferramentas", "editor de código, estrutura de pastas, index.html", "2"],
                                ["HTML estrutura", "DOCTYPE, head/body, tags/atributos, h1–h6, p, br, hr, strong/em", "3"],
                                ["HTML conteúdo", "a href/target, img src/alt, caminhos relativos, ul/ol/dl", "4"],
                                ["HTML dados", "table/tr/th/td, thead/tbody/tfoot, colspan, form, input types, select, textarea", "5"],
                                ["PHP básico", "blocos, echo, variáveis $, tipos, var_dump, operadores, == × ===, &&, ||", "6–7"],
                                ["PHP lógica", "if/elseif/else, switch/case/break/default", "8"],
                                ["PHP repetição", "for, while, do...while, arrays indexados/associativos, foreach", "9"],
                                ["PHP + HTML", "<?= ?>, include/require, function/return, arrays multidimensionais", "10"],
                                ["Formulários + PHP", "$_GET/$_POST, isset/empty, htmlspecialchars, fluxo completo", "11"],
                            ]}),
                ("dica", "Método de revisão ativo: para cada linha da tabela, <b>escreva um exemplo de código "
                         "sem consultar</b>. O que não conseguir escrever é o que precisa estudar. Refaça os "
                         "testes rápidos dos módulos — as questões das provas seguem o mesmo estilo."),
                ("conceito", ("As provas do curso",
                              "<b>A2 (30 pts)</b>: semana 16 (aula 48) — modelo na seção Avaliações. "
                              "<b>A3 (40 pts)</b>: prova escrita final individual (30 pts, aulas 70–71 — S) + "
                              "projeto e apresentação (10 pts, aula 72). Conteúdo cumulativo: tudo o que está "
                              "nesta tabela.")),
            ],
            "slides": {
                "pontos": [
                    "Revisão cumulativa: Web → ferramentas → HTML → PHP → formulários",
                    "Mapa da revisão com os conceitos-chave por bloco",
                    "Método ativo: escrever código sem consultar",
                    "Refaça os testes rápidos dos módulos 1 a 11",
                    "A3: prova final individual (30) + projeto/apresentação (10)",
                ],
                "nota": "Aula de revisão estratégica: quiz relâmpago no projetor (perguntas dos testes rápidos "
                        "anteriores) + espaço para dúvidas. Distribuir o mapa da revisão impresso.",
            },
        },
        {
            "num": 61,
            "titulo": "Aulas 61 a 69 — desenvolvimento guiado do projeto",
            "blocos": [
                ("h", "Três semanas predominantemente práticas"),
                ("p", "Semanas 21 a 23: o grupo desenvolve a <b>versão final</b> do projeto, aplicando tudo o "
                      "que foi construído nas etapas anteriores. Roteiro sugerido:"),
                ("tabela", {"titulo": "Roteiro das aulas 61 a 69",
                            "cab": ["Semana", "Aulas", "Metas da semana"],
                            "lin": [
                                ["21", "61–63",
                                 "Planejamento final (o que falta? quem faz?); estrutura completa revisada; "
                                 "página inicial e menu finalizados"],
                                ["22", "64–66",
                                 "Formulários completos com validação; processamento PHP robusto (erros + "
                                 "confirmação); listagem dinâmica com todos os campos"],
                                ["23", "67–69",
                                 "Validação de entrada em todos os campos; tratamento de erros com mensagens "
                                 "amigáveis; execução da tabela de testes completa → ENTREGA 5 (versão testada)"],
                            ]}),
                ("h", "Quadro de acompanhamento do grupo"),
                ("codigo", {"titulo": "checklist do projeto (cole no caderno/Drive do grupo)", "ling": "texto", "linhas": [
                    "[ ] Estrutura de pastas completa (css/, imagens/, includes/)",
                    "[ ] cabecalho.php + rodape.php usados em TODAS as páginas",
                    "[ ] index.php com menu e apresentação do sistema",
                    "[ ] cadastro.php com todos os campos dos requisitos",
                    "[ ] processar.php valida todos os campos (isset/empty + regras)",
                    "[ ] Mensagens de erro claras + link voltar",
                    "[ ] Saídas sanitizadas (htmlspecialchars em tudo)",
                    "[ ] listar.php com tabela dinâmica (thead/tbody/tfoot + total)",
                    "[ ] funcoes.php com pelo menos 2 funções do grupo",
                    "[ ] Tabela de testes executada (mínimo 6 casos) — OK/FALHOU",
                    "[ ] Correções das falhas aplicadas e retestadas",
                    "[ ] CSS mínimo: páginas consistentes e legíveis",
                ]}),
                ("dica", "Reunião de 5 minutos no início de cada aula do grupo: o que fizemos? o que falta? "
                         "quem faz o quê hoje? — é assim que equipes reais trabalham (daily meeting)."),
            ],
            "slides": {
                "pontos": [
                    "Semanas 21–23: desenvolvimento da versão final (prática)",
                    "Semana 21: planejamento + estrutura + página inicial",
                    "Semana 22: formulários + processamento + listagem",
                    "Semana 23: validação + erros + testes → Entrega 5",
                    "Checklist de 12 itens acompanha o progresso do grupo",
                ],
                "nota": "Professor atua como consultor: circula, desbloqueia, cobra o checklist. Cada aula "
                        "começa com a 'daily' de 5 min de cada grupo.",
            },
        },
        {
            "num": 70,
            "titulo": "Aulas 70 a 72 — finalização e apresentação",
            "blocos": [
                ("h", "Aula 70 — correções e melhorias"),
                ("p", "Ajustes finais de <b>código</b> (nomes, indentação, comentários), <b>interface</b> "
                      "(consistência, mensagens) e <b>usabilidade</b> (navegação clara). <b>(S) Nesta semana "
                      "aplica-se a prova escrita final individual — 30 pts da A3.</b>"),
                ("h", "Aula 71 — preparação da apresentação"),
                ("codigo", {"titulo": "Roteiro da apresentação (5 a 8 minutos por grupo)", "ling": "texto", "linhas": [
                    "1. ABERTURA (1 min): nome do sistema, tema, componentes do grupo.",
                    "2. OBJETIVO E USUÁRIOS (1 min): o problema que o sistema resolve.",
                    "3. DEMONSTRAÇÃO (3–4 min):",
                    "   - navegar pelo menu;",
                    "   - cadastrar um registro VÁLIDO (mostrar a confirmação);",
                    "   - tentar um cadastro INVÁLIDO (mostrar as mensagens de erro);",
                    "   - exibir a LISTAGEM dinâmica com os dados;",
                    "   - mostrar um trecho do CÓDIGO (foreach da listagem ou validação).",
                    "4. DIFICULDADES E APRENDIZADOS (1 min): o que foi difícil e como resolveram.",
                    "5. ENCERRAMENTO: agradecimento e espaço para perguntas.",
                ]}),
                ("h", "Checklist do ensaio"),
                ("lista", [
                    "Testar o sistema <b>no computador do laboratório/projetor</b> (resolução, navegador);",
                    "Ter dados de exemplo <b>já cadastrados</b> (a listagem não pode aparecer vazia);",
                    "Cronometrar: dentro dos 5–8 minutos;",
                    "Todos os membros falam (dividir as partes);",
                    "Plano B: prints/vídeo da demonstração, caso algo falhe ao vivo.",
                ]),
                ("h", "Aula 72 — apresentação e avaliação final"),
                ("p", "Apresentação dos projetos pelos grupos, avaliação final (10 pts — critério do professor, "
                      "conforme o Plano) e encerramento da disciplina. Critérios sugeridos (S): "
                      "<b>funcionalidade</b> (cadastro, listagem e validação funcionando), <b>organização dos "
                      "arquivos</b>, <b>qualidade do código</b> (nomes, indentação, comentários), <b>uso "
                      "correto de HTML e PHP</b> e <b>apresentação/demonstração</b>. A rubrica completa está na "
                      "seção <b>Avaliação A3</b> desta apostila."),
                ("conceito", ("Apresentar também é habilidade técnica",
                              "Na vida profissional, vocês vão demonstrar sistemas para clientes e gestores. "
                              "Quem apresenta bem um projeto simples se destaca de quem apresenta mal um "
                              "projeto complexo. Ensaio não é frescura — é parte do trabalho.")),
            ],
            "slides": {
                "pontos": [
                    "Aula 70: correções finais + prova escrita final (A3 — 30 pts) (S)",
                    "Aula 71: roteiro da apresentação (5 partes, 5–8 min)",
                    "Demonstração: cadastro válido + inválido + listagem + código",
                    "Ensaio: dados prontos, cronômetro, todos falam, plano B",
                    "Aula 72: apresentações + avaliação final (10 pts) + encerramento",
                ],
                "nota": "Sortear a ordem das apresentações na aula 71. Combinar o tempo com sinal (placa ou "
                        "timer no projetor). Plateia registra 1 pergunta por grupo.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Documento de requisitos do grupo", "tipo": "grupo",
            "enunciado": "Preencham o modelo requisitos.txt (aula 50) com o tema escolhido: objetivo, usuários, "
                         "funcionalidades, páginas e dados (campos com tipo e regras). <b>Vale como Entrega 1 "
                         "do projeto final (S).</b>",
            "esperado": "Documento de 1 página com os 6 itens preenchidos de forma concreta e testável "
                        "(campos com tipos e regras de validação definidos).",
            "orientacao": "Validar um por um com visto do professor. Requisitos vagos voltam para refinação "
                          "('sistema bonito' não é requisito).",
        },
        {
            "num": 2, "titulo": "Tabela de testes do sistema", "tipo": "grupo",
            "enunciado": "Montem a tabela de testes do sistema do grupo com <b>no mínimo 6 casos</b>: para cada "
                         "funcionalidade, 1 teste válido, 1 inválido e 1 de limite. Colunas: #, teste, entrada, "
                         "resultado esperado, resultado obtido, OK/FALHOU.",
            "esperado": "Tabela completa com esperados definidos ANTES da execução e registro dos resultados "
                        "reais; falhas viram lista de correções.",
            "orientacao": "Usar na aula 69 (Entrega 5). Teste cruzado entre grupos aumenta o rigor.",
        },
        {
            "num": 3, "titulo": "Caça-erros do projeto", "tipo": "escrito",
            "enunciado": "O trecho abaixo (de um listar.php) tem <b>3 erros</b>: um de sintaxe, um de lógica e "
                         "um de segurança. Identifique-os, classifique-os e corrija:",
            "codigo": {"titulo": "listar.php com erros", "ling": "php", "linhas": [
                "<?php",
                "    $livros = [",
                "        [\"titulo\" => \"PHP Básico\", \"ano\" => 2020],",
                "        [\"titulo\" => \"HTML Completo\", \"ano\" => 2022],",
                "    ]",
                "    $total = count($livros) + 1;",
                "    foreach ($livros as $livro) {",
                "        echo \"<tr><td>\" . $livro[\"titulo\"] . \"</td></tr>\";",
                "    }",
                "    echo \"Total de livros: $total\";",
                "?>",
            ]},
            "esperado": "SINTAXE: falta ; após o fechamento do array $livros = [...] (linha 5). LÓGICA: $total = "
                        "count($livros) + 1 exibe 3 em vez de 2. SEGURANÇA: echo do título sem "
                        "htmlspecialchars(). Correções: acrescentar ;, remover + 1 e envolver a saída com "
                        "htmlspecialchars($livro[\"titulo\"]).",
            "orientacao": "Reforça a aula 59. Peça que classifiquem ANTES de corrigir — a classificação é o "
                          "aprendizado principal.",
        },
        {
            "num": 4, "titulo": "Ensaio da apresentação", "tipo": "grupo",
            "enunciado": "Sigam o roteiro da aula 71 e ensaiem com cronômetro: abertura, objetivo, "
                         "demonstração (válido + inválido + listagem + código), dificuldades e encerramento. "
                         "Gravem um vídeo do ensaio (celular) e autoavaliem: tempo, clareza, todos falaram?",
            "esperado": "Apresentação de 5–8 minutos com demonstração funcional e participação de todos os "
                        "membros.",
            "orientacao": "Professor assiste a um ensaio de cada grupo na aula 71 e dá feedback. Dados de "
                          "exemplo já cadastrados são obrigatórios.",
        },
    ],
    "teste_rapido": [
        {"enunciado": "A ordem recomendada de construção do projeto final é:",
         "alt": ["listagem → formulário → estrutura → includes.",
                 "estrutura e includes → página inicial → cadastro → processamento → listagem.",
                 "CSS → imagens → formulários → PHP.",
                 "apresentação → código → testes."],
         "resposta": 1,
         "comentario": "Do alicerce ao acabamento: primeiro o esqueleto e o menu (navegável desde o início), "
                       "depois as funcionalidades na ordem do fluxo de dados."},
        {"enunciado": "Um requisito bem escrito se caracteriza por ser:",
         "alt": ["curto e genérico, como ‘o sistema deve ser bom’.",
                 "concreto e testável, como ‘a listagem exibe título, autor e disponibilidade em tabela’.",
                 "escrito em inglês técnico.",
                 "aprovado por todos os grupos da turma."],
         "resposta": 1,
         "comentario": "Requisito testável permite verificar sim/não na tabela de testes. Generalidades não "
                       "orientam o desenvolvimento."},
        {"enunciado": "Na tabela de testes, além dos casos válidos e inválidos, os ‘testes de limite’ servem "
                    "para:",
         "alt": ["testar o sistema em outros navegadores.",
                 "verificar o comportamento exatamente nas bordas das regras (ex.: ano mínimo e máximo).",
                 "medir a velocidade da página.",
                 "testar apenas campos obrigatórios."],
         "resposta": 1,
         "comentario": "Erros se escondem nas bordas: valores exatamente no limite (1900/2026) ou logo fora "
                       "(1899/2027) revelam condições mal escritas (>= vs >)."},
        {"enunciado": "A mensagem “Parse error: syntax error ... in listar.php on line 24” indica um erro de:",
         "alt": ["lógica — o resultado do cálculo está errado.",
                 "execução — a variável não existe.",
                 "sintaxe — o código viola as regras da linguagem; deve-se abrir o arquivo na linha indicada.",
                 "segurança — dados não sanitizados."],
         "resposta": 2,
         "comentario": "Parse error = sintaxe. A mensagem dá arquivo e linha: estratégia ler → identificar → "
                       "entender → corrigir → testar."},
        {"enunciado": "Na demonstração da apresentação final (aula 72), o roteiro prevê mostrar:",
         "alt": ["apenas a página inicial do sistema.",
                 "somente o código-fonte completo, lido linha a linha.",
                 "um cadastro válido, uma tentativa inválida com as mensagens de erro e a listagem dinâmica.",
                 "um vídeo pronto, sem executar o sistema ao vivo."],
         "resposta": 2,
         "comentario": "A demonstração prova que o sistema funciona E que trata erros — os dois lados da "
                       "validação. Plano B (vídeo) existe só para emergências."},
    ],
    "avaliacao_ref": "A3",
}

MODULOS = [MODULO_10, MODULO_11, MODULO_12]
