# -*- coding: utf-8 -*-
"""LP2 — Módulos 1 a 4 (Partes I e II): ambiente, SGBD/conexão e SQL. Semanas 1 a 6."""

M1 = {
    "num": 1, "titulo": "Ambientação e linguagem de programação estruturada",
    "parte_num": 1, "parte_titulo": "Ambiente, SGBD e Conexão",
    "aulas_faixa": "Aulas 1 a 4", "semanas": "Semana 1",
    "objetivos": [
        "Compreender o escopo da disciplina e a arquitetura do projeto final.",
        "Reconhecer os três pilares da programação estruturada: sequência, seleção e repetição.",
        "Identificar os componentes do ambiente: IDE VB6, SGBD MySQL, driver ODBC e biblioteca ADO.",
        "Organizar o ambiente de trabalho e executar o primeiro programa VB6.",
    ],
    "aulas": [
        {"num": 1, "titulo": "Ambientação e visão geral", "blocos": [
            ("h", "O que vamos construir neste semestre"),
            ("p", "Em Linguagem de Programação II, você sai do “programa que só calcula” e entra no "
                  "mundo dos <b>dados que persistem</b>: programas que conversam com um <b>banco de "
                  "dados</b>, consultam com <b>SQL</b>, guardam informações em <b>arquivos</b>, imprimem "
                  "<b>relatórios e documentos</b> e viram um <b>pacote de instalação</b> completo. Tudo "
                  "isso se junta no projeto integrador das semanas 23–24."),
            ("conceito", ("Programação estruturada",
                          "Estilo de programar baseado em três estruturas de controle: <b>sequência</b> "
                          "(passo a passo), <b>seleção</b> (If/Select Case — decidir) e <b>repetição</b> "
                          "(For/Do While — repetir). Sem “pulos” desorganizados (o famoso GOTO): o código "
                          "fica legível, testável e fácil de manter.")),
            ("h", "A linguagem e o banco escolhidos (S)"),
            ("p", "Trabalharemos com <b>Visual Basic 6.0 (VB6)</b> como linguagem estruturada — com "
                  "vetores, matrizes, registros (Type), Strings, Sub/Function, arquivos e gráficos — e o "
                  "SGBD <b>MySQL</b>, acessado por <b>ODBC/ADO</b>. Se o laboratório não tiver servidor, "
                  "usamos o plano B documentado: Access (.mdb), mesmos conceitos."),
            ("tabela", {"titulo": "Componentes do ambiente",
                        "cab": ["Componente", "Papel no curso"],
                        "lin": [["IDE VB6", "Editor + compilador + construtor de telas (formulários)"],
                                ["MySQL Server", "SGBD: guarda bancos, tabelas e executa SQL"],
                                ["Driver MySQL ODBC", "Ponte que deixa o VB6 conversar com o MySQL"],
                                ["ADO (ActiveX Data Objects)", "Biblioteca VB6 que envia SQL e recebe resultados (Recordset)"]]}),
            ("h", "Arquitetura do projeto final"),
            ("lista", [
                "<b>Camada de dados</b>: banco MySQL com tabelas do tema escolhido;",
                "<b>Camada de acesso</b>: módulo de conexão + comandos SQL (ADO);",
                "<b>Camada de lógica</b>: Modules com Sub/Function (modularização);",
                "<b>Camada de apresentação</b>: formulários VB6 + relatórios/Printer;",
                "<b>Distribuição</b>: pacote de instalação (Package & Deployment Wizard).",
            ]),
            ("h", "Contrato da disciplina"),
            ("lista", [
                "4 aulas por semana em 4 etapas: conceitos → demonstração → prática → fixação;",
                "Avaliações: A1 (30) semanas 1–8 · A2 (30) semana 16 · A3 (40) semana 24;",
                "14 h não presenciais no AVA, distribuídas conforme o cronograma;",
                "Diagnóstico inicial nesta semana: vale ponto de participação, não de nota.",
            ]),
        ], "slides": {"pontos": [
            "Do programa isolado ao sistema com banco de dados, relatórios e instalação",
            "Programação estruturada: sequência · seleção · repetição (sem GOTO solto)",
            "Ambiente (S): VB6 + MySQL via ODBC/ADO (plano B: Access)",
            "Arquitetura do projeto: dados → acesso SQL → lógica modular → telas/relatórios → instalador",
            "96 aulas = 24 semanas × 4 etapas; A1/A2/A3 = 30/30/40",
        ], "nota": "Aula 1: presentare o semestre com a arquitetura em camadas no quadro e aplicar o "
                   "diagnóstico (10 min): o que já sabem de lógica e de banco?"}},
        {"num": 2, "titulo": "Primeiro programa VB6 e organização do ambiente", "blocos": [
            ("h", "Anatomia de um programa VB6"),
            ("p", "No VB6, o código vive em <b>módulos</b> (Modules) e <b>formulários</b> (Forms). "
                  "Subs executam ações; Functions retornam valores. O ponto de partida clássico é o "
                  "evento <b>Form_Load</b> (quando a janela abre) ou um botão clicado."),
            ("codigo", {"titulo": "Form1 — primeiro programa (sequência + saída)", "ling": "vb", "linhas": [
                "Private Sub Form_Load()",
                "    ' sequência: passo a passo, de cima para baixo",
                "    Dim nome As String",
                "    nome = \"Turma 2/2026\"",
                "    Print \"Olá, \" & nome & \"!\"          ' saída no formulário",
                "    Print \"Disciplina: Linguagem de Programação II\"",
                "End Sub",
            ]}),
            ("h", "As três estruturas, em um relance"),
            ("codigo", {"titulo": "Seleção e repetição (prévia das semanas 7+)", "ling": "vb", "linhas": [
                "' SELEÇÃO: decidir",
                "If nota >= 7 Then",
                "    Print \"Aprovado\"",
                "Else",
                "    Print \"Recuperação\"",
                "End If",
                "",
                "' REPETIÇÃO: repetir",
                "Dim i As Integer",
                "For i = 1 To 5",
                "    Print i",
                "Next i",
            ]}),
            ("h", "Organização do ambiente de trabalho"),
            ("lista_num", [
                "Crie a pasta do semestre: <b>C:\\LP2\\</b> (ou Documents\\LP2);",
                "Dentro dela, uma pasta por semana: <b>S01</b>, <b>S02</b>… e, no fim, <b>PROJETO</b>;",
                "Salve todo projeto VB6 (.vbp) dentro da pasta da semana correspondente;",
                "Nomes sem acento/espaço: <b>Conexao.bas</b>, <b>frmAlunos.frm</b>;",
                "Faça backup semanal da pasta no Drive (hábito de profissional).",
            ]),
            ("atencao", "VB6 é antigo e sensível a caminhos com acentos/espaços e a resoluções muito "
                        "altas. Padronize: pastas simples, arquivos .vbp versionados por data e sempre "
                        "FECHAR a IDE pelo menu (evita projetos corrompidos)."),
        ], "slides": {"pontos": [
            "Código em Modules/Forms; Sub executa, Function retorna",
            "Form_Load / cliques de botão = pontos de entrada",
            "Sequência, seleção (If) e repetição (For) — os 3 pilares",
            "Padrão de pastas: C:\\LP2\\S01..S24 + PROJETO (sem acentos)",
            "Backup semanal no Drive = hábito profissional",
        ], "codigo": {"titulo": "Primeiro programa", "linhas": [
            "Private Sub Form_Load()",
            "    Dim nome As String",
            "    nome = \"Turma 2/2026\"",
            "    Print \"Olá, \" & nome & \"!\"",
            "End Sub",
        ]}, "nota": "Demonstre ao vivo: criar projeto, rodar (F5), quebrar de propósito (tirar aspas) e "
                   "ler a mensagem de erro juntos."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Diagnóstico de lógica", "tipo": "escrito",
         "enunciado": "Sem computador: escreva em pseudocódigo (ou desenhe) um algoritmo que leia 3 notas, "
                      "calcule a média e imprima a situação (>=7 aprovado; >=5 recuperação; senão "
                      "reprovado). Identifique no seu algoritmo onde está cada estrutura: sequência, "
                      "seleção e repetição (use repetição para ler as 3 notas).",
         "resolucao": [
             {"t": "pseudo", "tit": "🧠 Resolução no papel (pseudocódigo)", "x":
              "algoritmo Media_da_Turma\n"
              "var\n"
              "    nota, soma, media : real\n"
              "    i               : inteiro\n"
              "inicio\n"
              "    soma <- 0\n"
              "    para i de 1 ate 3 faca          <-- REPETICAO (lê as 3 notas)\n"
              "        escreva(\"Digite a nota \", i, \": \")\n"
              "        leia(nota)\n"
              "        soma <- soma + nota\n"
              "    fim-para\n"
              "    media <- soma / 3               <-- SEQUENCIA (passo a passo, em ordem)\n"
              "    se media >= 7 entao             <-- SELECAO (decide o caminho)\n"
              "        escreva(\"APROVADO com media \", media)\n"
              "    senao-se media >= 5 entao\n"
              "        escreva(\"RECUPERACAO com media \", media)\n"
              "    senao\n"
              "        escreva(\"REPROVADO com media \", media)\n"
              "    fim-se\n"
              "fim"},
             {"t": "passos", "tit": "🎬 Demonstração com notas de exemplo", "x": [
                 "Notas digitadas: <b>6, 8 e 7</b>. O laço soma: 0+6=6 → 6+8=14 → 14+7=21.",
                 "Média = 21 / 3 = <b>7</b>. Entra no primeiro <b>se</b> (media >= 7) → imprime “APROVADO com media 7”.",
                 "Teste outro caso na lousa: notas 4, 5, 6 → soma 15 → média 5 → cai no <b>senao-se</b> (>= 5) → “RECUPERACAO”.",
                 "E notas 2, 3, 4 → média 3 → cai no <b>senao</b> → “REPROVADO”.",
             ]},
             {"t": "nota", "x":
              "Onde está cada estrutura? <b>Sequência</b>: os comandos em ordem (soma <- 0, media <- soma / 3). "
              "<b>Repetição</b>: o laço “para i de 1 ate 3” (lê as 3 notas sem repetir código). "
              "<b>Seleção</b>: o se / senao-se / senao que escolhe a situação pela média."},
         ],
         "esperado": "Algoritmo com laço para leitura das 3 notas, If/ElseIf encadeado para a situação e "
                     "identificação correta das três estruturas.",
         "orientacao": "Correção dialogada no projetor com 2–3 soluções de alunos; aproveite para nivelar a turma."},
        {"num": 2, "titulo": "Organização do ambiente", "tipo": "pratico",
         "enunciado": "Crie a estrutura de pastas do semestre (LP2\\S01..S04 + PROJETO), abra o VB6, crie um "
                      "projeto novo salvo em LP2\\S01\\ola.vbp e faça o Form_Load imprimir seu nome e a data "
                      "de hoje (use Date).",
         "resolucao": [
             {"t": "tree", "tit": "📁 1) As pastas do semestre (crie no Explorador de Arquivos)", "x":
              "Documentos\\\n"
              "└── LP2\\\n"
              "    ├── S01\\      ← aula de hoje (ola.vbp mora aqui)\n"
              "    ├── S02\\\n"
              "    ├── S03\\\n"
              "    ├── S04\\\n"
              "    └── PROJETO\\   ← trabalho final da disciplina"},
             {"t": "passos", "tit": "🪜 2) No VB6, na ordem certinha", "x": [
                 "Abra o VB6 → janela <b>Novo Projeto</b> → <b>Standard EXE</b> → OK.",
                 "ANTES de escrever código: <b>Arquivo → Salvar Projeto Como…</b> — salve o formulário como "
                 "<b>Form1.frm</b> e o projeto como <b>ola.vbp</b>, os dois DENTRO de <b>LP2\\S01</b>.",
                 "Dê dois cliques na parte cinza do formulário para abrir a janela de código e digite o código abaixo.",
                 "Aperte <b>F5</b> (ou o botão ▶ Iniciar): o formulário abre e as duas linhas aparecem impressas nele.",
             ]},
             {"t": "code", "tit": "💻 3) O código do Form_Load (imprime nome e data ao abrir)", "x":
              "Private Sub Form_Load()\n"
              "    Print \"Olá, eu sou a Prof.ª Raquel!\"\n"
              "    Print \"Hoje é \" & Date\n"
              "End Sub"},
             {"t": "nota", "x":
              "O <b>Print</b> escreve direto no formulário quando o programa roda. O <b>&</b> junta "
              "(concatena) o texto com o valor de <b>Date</b> (a data de hoje do Windows). Troque o nome "
              "entre aspas pelo seu — e salve de novo (Ctrl+S)."},
         ],
         "esperado": "Árvore de pastas criada; projeto .vbp salvo no caminho correto; formulário imprimindo "
                     "nome e data ao rodar (F5).",
         "orientacao": "Conferir caminho do .vbp (muitos salvam na área de trabalho) e uso de & para concatenar."},
        {"num": 3, "titulo": "As três estruturas na prática", "tipo": "pratico",
         "enunciado": "No mesmo projeto: adicione um botão que leia um número por InputBox e use If para "
                      "dizer se é par ou impar (Mod); adicione outro botão que imprima com For a tabuada "
                      "desse número de 1 a 10.",
         "resolucao": [
             {"t": "passos", "tit": "🪜 1) Os dois botões no formulário", "x": [
                 "Na caixa de ferramentas, clique no ícone <b>CommandButton</b> e desenhe um botão no formulário.",
                 "Com o botão selecionado, na janela <b>Propriedades</b>: mude <b>(Name)</b> para <b>btnParImpar</b> e <b>Caption</b> para <b>Par ou Ímpar?</b>.",
                 "Desenhe o segundo botão: <b>(Name)</b> = <b>btnTabuada</b>, <b>Caption</b> = <b>Tabuada 1 a 10</b>.",
                 "Dois cliques em cada botão para abrir o código deles e colar os blocos abaixo.",
             ]},
             {"t": "code", "tit": "💻 2) Botão 1 — lê o número e diz se é par ou ímpar", "x":
              "Private Sub btnParImpar_Click()\n"
              "    Dim n As Integer\n"
              "    n = Val(InputBox(\"Digite um número inteiro:\"))\n"
              "    If n Mod 2 = 0 Then\n"
              "        Print n & \" é PAR\"\n"
              "    Else\n"
              "        Print n & \" é ÍMPAR\"\n"
              "    End If\n"
              "End Sub"},
             {"t": "code", "tit": "💻 3) Botão 2 — a tabuada de 1 a 10 com For", "x":
              "Private Sub btnTabuada_Click()\n"
              "    Dim n As Integer, i As Integer\n"
              "    n = Val(InputBox(\"Tabuada de qual número?\"))\n"
              "    For i = 1 To 10\n"
              "        Print n & \" x \" & i & \" = \" & n * i\n"
              "    Next i\n"
              "End Sub"},
             {"t": "passos", "tit": "🎬 4) Teste na frente da turma", "x": [
                 "F5 → clique em <b>Par ou Ímpar?</b> → digite 7 → aparece “7 é ÍMPAR”; digite 10 → “10 é PAR”.",
                 "Clique em <b>Tabuada 1 a 10</b> → digite 7 → aparecem as 10 linhas, do 7 x 1 ao 7 x 10.",
                 "Explique o <b>Mod</b>: é o RESTO da divisão. 7 Mod 2 = 1 (sobrou 1 → ímpar); 10 Mod 2 = 0 (não sobrou nada → par).",
                 "Explique o <b>Val()</b>: o InputBox devolve TEXTO; o Val transforma em número para a conta funcionar.",
             ]},
             {"t": "nota", "x":
              "Conferindo as três estruturas: <b>sequência</b> (os comandos em ordem dentro de cada botão), "
              "<b>seleção</b> (o If...Then...Else do par/ímpar) e <b>repetição</b> (o For...Next da tabuada). "
              "Salve o projeto (Ctrl+S) na pasta LP2\\S01 antes de fechar."},
         ],
         "esperado": "Dois botões funcionais: par/impar com Mod e tabuada com For...Next usando & na montagem "
                     "das linhas.",
         "orientacao": "Ponto de atenção: Val(InputBox(...)) para converter texto em número; circular e ajudar "
                       "com a sintaxe do For."},
    ],
    "teste_rapido": [
        {"enunciado": "Programação estruturada se apoia em três estruturas:",
         "alt": ["entrada, processamento e saída", "sequência, seleção e repetição",
                 "variáveis, constantes e funções", "telas, relatórios e bancos"],
         "resposta": 1, "comentario": "Sequência executa em ordem; seleção decide; repetição repete blocos."},
        {"enunciado": "No ambiente do curso (S), quem conversa diretamente com o MySQL a partir do VB6 é:",
         "alt": ["o objeto Printer", "o driver ODBC + biblioteca ADO", "o Package & Deployment Wizard",
                 "o explorador de arquivos"],
         "resposta": 1, "comentario": "ODBC faz a ponte VB6↔MySQL; ADO envia SQL e recebe Recordset."},
        {"enunciado": "Um Sub difere de uma Function porque:",
         "alt": ["Sub retorna valor", "Function retorna valor", "Sub só roda em Modules", "não há diferença"],
         "resposta": 1, "comentario": "Function devolve resultado ao chamador; Sub apenas executa ações."},
        {"enunciado": "O padrão de organização de pastas adotado no curso é:",
         "alt": ["tudo na área de trabalho", "LP2\\S01..S24 + PROJETO, sem acentos/espaços",
                 "uma pasta por aluno no pendrive", "pastas com nome das disciplinas por extenso"],
         "resposta": 1, "comentario": "Caminhos simples evitam bugs no VB6 e facilitam backup/entrega."},
        {"enunciado": "Para converter o texto do InputBox em número usamos:",
         "alt": ["Str()", "Val()", "Mid()", "Len()"],
         "resposta": 1, "comentario": "Val converte string em número; Str faz o caminho inverso."},
    ],
    "avaliacao_ref": None,
}

M2 = {
    "num": 2, "titulo": "SGBD: instalação, configuração e conexão",
    "parte_num": 1, "parte_titulo": "Ambiente, SGBD e Conexão",
    "aulas_faixa": "Aulas 5 a 12", "semanas": "Semanas 2 a 3",
    "objetivos": [
        "Explicar o que é um SGBD e instalar/configurar o MySQL no laboratório.",
        "Validar o ambiente com comandos básicos do cliente MySQL.",
        "Compreender conexão: parâmetros, abertura, fechamento e string de conexão.",
        "Tratar falhas básicas de conexão no VB6 (On Error).",
    ],
    "aulas": [
        {"num": 2, "titulo": "SGBD — instalação e configuração (semana 2)", "blocos": [
            ("h", "O que é um SGBD"),
            ("conceito", ("SGBD — Sistema Gerenciador de Banco de Dados",
                          "Software que <b>armazena, organiza, protege e controla o acesso</b> aos dados: "
                          "cria tabelas, executa consultas, gerencia usuários e garante integridade. "
                          "Exemplos: MySQL, PostgreSQL, SQL Server, Access. No curso: <b>MySQL</b> (gratuito).")),
            ("p", "Sem SGBD, cada programa inventa seu próprio jeito de guardar dados (arquivos soltos, "
                  "planilhas…). Com SGBD, todos os programas falam a mesma língua: <b>SQL</b>."),
            ("h", "Instalação passo a passo (laboratório)"),
            ("lista_num", [
                "Baixe o instalador do MySQL (mysql-installer-community) do site oficial ou da pasta da rede;",
                "Execute e escolha o tipo <b>Server only</b> (ou Developer padrão se houver espaço);",
                "Configuração: authentication padrão, <b>senha do root</b> (anote! ex.: aluno123), serviço "
                "Windows MySQL habilitado (inicia com o sistema);",
                "Conclua e abra o <b>MySQL Command Line Client</b> (ou mysql -u root -p no prompt);",
                "Valide: <b>SHOW DATABASES;</b> deve listar information_schema, mysql, performance_schema, sys.",
            ]),
            ("codigo", {"titulo": "Primeiros comandos no cliente MySQL", "ling": "sql", "linhas": [
                "mysql -u root -p            -- entra no servidor (digite a senha)",
                "SHOW DATABASES;             -- lista os bancos existentes",
                "CREATE DATABASE escola;     -- cria nosso banco de estudo",
                "USE escola;                 -- seleciona o banco ativo",
                "SELECT VERSION();           -- confirma a versão instalada",
            ]}),
            ("dica", "Toda instrução SQL termina com <b>ponto e vírgula</b>. E todo comando de administração "
                     "(SHOW, CREATE DATABASE, USE) é um ótimo exercício de digitação: erro de uma letra = "
                     "mensagem de erro educativa."),
            ("atencao", "Senha do root perdida = laboratório parado. Padrão da turma + senha anotada no "
                        "caderno e no caderno do professor. Se o serviço não subir: Serviços do Windows → "
                        "MySQL80 → Iniciar."),
        ], "slides": {"pontos": [
            "SGBD = software que guarda/organiza/protege dados; todos falam SQL",
            "MySQL: installer → Server only → senha root → serviço ativo",
            "Validação: mysql -u root -p → SHOW DATABASES;",
            "CREATE DATABASE escola; USE escola; = nosso parque de estudos",
            "SQL termina com ; — sempre",
        ], "codigo": {"titulo": "Validação do ambiente", "linhas": [
            "mysql -u root -p",
            "SHOW DATABASES;",
            "CREATE DATABASE escola;",
            "USE escola;",
        ]}, "nota": "Aula 100% laboratório: instale projetando passo a passo; duplas se ajudam; termine com "
                   "100% das máquinas mostrando SHOW DATABASES."}},
        {"num": 3, "titulo": "SGBD — conexão: parâmetros, abertura e falhas (semana 3)", "blocos": [
            ("h", "O que é uma conexão"),
            ("p", "Conectar é <b>abrir um canal</b> entre o programa (cliente) e o SGBD (servidor). Para "
                  "isso, o cliente informa: <b>driver</b> (quem traduz), <b>servidor</b> (onde), "
                  "<b>banco</b> (qual), <b>usuário e senha</b> (credenciais). No VB6, isso vira uma "
                  "<b>connection string</b> passada ao objeto <b>ADODB.Connection</b>."),
            ("codigo", {"titulo": "Modulo Conexao.bas — abrir e fechar com tratamento", "ling": "vb", "linhas": [
                "Public cn As ADODB.Connection",
                "",
                "Public Sub AbrirConexao()",
                "    On Error GoTo Falha",
                "    Set cn = New ADODB.Connection",
                "    cn.ConnectionString = \"Driver={MySQL ODBC 8.0 Driver};\" & _",
                "                          \"Server=localhost;Database=escola;\" & _",
                "                          \"Uid=root;Pwd=aluno123;\"",
                "    cn.Open",
                "    Print \"Conectado ao MySQL!\"",
                "    Exit Sub",
                "Falha:",
                "    MsgBox \"Falha de conexão: \" & Err.Description, vbCritical",
                "End Sub",
                "",
                "Public Sub FecharConexao()",
                "    If Not cn Is Nothing Then cn.Close",
                "End Sub",
            ]}),
            ("tabela", {"titulo": "Parâmetros da string de conexão",
                        "cab": ["Parâmetro", "Significado", "Exemplo"],
                        "lin": [["Driver", "Driver ODBC instalado", "{MySQL ODBC 8.0 Driver}"],
                                ["Server", "Endereço do servidor", "localhost (ou IP da rede)"],
                                ["Database", "Banco selecionado ao conectar", "escola"],
                                ["Uid / Pwd", "Usuário e senha", "root / aluno123"]]}),
            ("h", "Tratamento básico de falhas"),
            ("lista", [
                "<b>On Error GoTo Falha</b>: desvia para o rótulo se algo der errado;",
                "<b>Err.Description</b>: mensagem técnica do erro (mostre ao usuário de forma amiga);",
                "Falhas típicas: serviço parado, senha errada, driver ausente, banco inexistente;",
                "Sempre <b>fechar</b> a conexão ao terminar (FecharConexao) — conexão aberta é recurso vazando.",
            ]),
            ("analogia", ("Conexão = ligação telefônica",
                          "Discar (cn.Open) exige número certo (Server), ramal (Database) e identificação "
                          "(Uid/Pwd). Se a linha está muda (serviço parado), você desliga e avisa (On Error). "
                          "E ao terminar a conversa, desliga (cn.Close) — ninguém deixa o telefone fora do "
                          "gancho a noite toda.")),
        ], "slides": {"pontos": [
            "Conexão = canal cliente↔servidor com driver, servidor, banco e credenciais",
            "ADODB.Connection + connection string no VB6",
            "On Error GoTo Falha + Err.Description = tratamento básico",
            "Sempre fechar a conexão ao terminar (cn.Close)",
            "Falhas clássicas: serviço parado, senha, driver, banco inexistente",
        ], "codigo": {"titulo": "Núcleo da conexão", "linhas": [
            "Set cn = New ADODB.Connection",
            "cn.ConnectionString = \"Driver={MySQL ODBC 8.0 Driver};\" & _",
            "    \"Server=localhost;Database=escola;Uid=root;Pwd=aluno123;\"",
            "cn.Open",
        ]}, "nota": "Provoque falhas ao vivo: pare o serviço, erre a senha — e leia Err.Description com a "
                   "turma. É a aula que transforma erro em conteúdo."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Instalação validada", "tipo": "pratico",
         "enunciado": "Instale (ou valide) o MySQL na sua máquina: entre no cliente, rode SHOW DATABASES;, "
                      "crie o banco <b>escola</b> e dentro dele a tabela <b>turma(id INT PRIMARY KEY "
                      "AUTO_INCREMENT, nome VARCHAR(40))</b>. Cole a saída no caderno/Drive.",
         "esperado": "Banco escola e tabela turma criados sem erros; saída do SHOW TABLES; conferindo.",
         "orientacao": "Checklist visual por máquina: cliente abre, banco existe, tabela existe. Anote as "
                       "máquinas com problema para a TI (tutorial de laboratório)."},
        {"num": 2, "titulo": "Conexão VB6 → MySQL", "tipo": "pratico",
         "enunciado": "Crie o projeto ConexaoS03 com o módulo Conexao.bas (modelo da aula) e um formulário "
                      "com botões Conectar/Desconectar que mostrem o status (conectado/falhado) em um Label.",
         "esperado": "Botão Conectar abre cn e mostra 'Conectado'; Desconectar fecha; com o serviço parado, "
                     "MsgBox amigável com Err.Description.",
         "orientacao": "Teste os 4 cenários de falha em duplas (serviço, senha, driver, banco). Cada dupla "
                       "registra qual erro provocou e qual mensagem apareceu."},
        {"num": 3, "titulo": "Mapa da conexão", "tipo": "escrito",
         "enunciado": "Desenhe o fluxo cliente/servidor da conexão (VB6 → ODBC → MySQL) e explique com suas "
                      "palavras o papel de cada parâmetro da connection string e o que acontece em cada "
                      "falha simulada no laboratório.",
         "esperado": "Diagrama com as 3 camadas e legenda correta dos parâmetros; explicação coerente das "
                     "falhas (serviço/senha/driver/banco).",
         "orientacao": "Use os melhores diagramas para montar o pôster da sala (fixação visual do semestre)."},
    ],
    "teste_rapido": [
        {"enunciado": "Um SGBD existe para:",
         "alt": ["substituir o sistema operacional", "armazenar, organizar e controlar o acesso aos dados",
                 "compilar programas VB6", "desenhar formulários"],
         "resposta": 1, "comentario": "É o gerente dos dados: criação, consulta, segurança e integridade."},
        {"enunciado": "O comando que lista os bancos do servidor é:",
         "alt": ["LIST ALL;", "SHOW DATABASES;", "SELECT BANKS;", "DIR /B;"],
         "resposta": 1, "comentario": "SHOW DATABASES; no cliente MySQL."},
        {"enunciado": "Na string de conexão, o parâmetro Database indica:",
         "alt": ["o nome do driver", "o banco selecionado ao conectar", "a porta do servidor",
                 "o nome do formulário"],
         "resposta": 1, "comentario": "Server = onde; Database = qual banco; Uid/Pwd = quem."},
        {"enunciado": "On Error GoTo Falha serve para:",
         "alt": ["apagar erros do código", "desviar a execução para um rótulo quando ocorrer erro",
                 "impedir erros de sintaxe", "reiniciar o programa"],
         "resposta": 1, "comentario": "Tratamento de erro em tempo de execução; Err.Description detalha."},
        {"enunciado": "Ao terminar de usar o banco, o programa deve:",
         "alt": ["deixar a conexão aberta para a próxima vez", "fechar a conexão (cn.Close)",
                 "desinstalar o driver", "reiniciar o MySQL"],
         "resposta": 1, "comentario": "Conexão aberta consome recurso do servidor; feche sempre."},
    ],
    "avaliacao_ref": None,
}

M3 = {
    "num": 3, "titulo": "SQL: fundamentos e manipulação de dados",
    "parte_num": 2, "parte_titulo": "Linguagem SQL",
    "aulas_faixa": "Aulas 13 a 20", "semanas": "Semanas 4 a 5",
    "objetivos": [
        "Diferenciar DDL (estrutura) de DML (dados) e escrever CREATE TABLE adequado.",
        "Inserir, alterar e excluir dados com INSERT, UPDATE e DELETE seguros.",
        "Consultar dados com SELECT simples.",
        "Integrar instruções SQL ao programa VB6 via cn.Execute.",
    ],
    "aulas": [
        {"num": 4, "titulo": "SQL — fundamentos: criar e consultar (semana 4)", "blocos": [
            ("h", "Duas famílias de comandos"),
            ("tabela", {"titulo": "DDL × DML",
                        "cab": ["Família", "Para que", "Comandos"],
                        "lin": [["DDL (definição)", "criar/alterar a ESTRUTURA", "CREATE, ALTER, DROP"],
                                ["DML (manipulação)", "cuidar dos DADOS", "INSERT, UPDATE, DELETE, SELECT"]]}),
            ("codigo", {"titulo": "Estrutura bem definida: tipos e chave primária", "ling": "sql", "linhas": [
                "USE escola;",
                "",
                "CREATE TABLE alunos (",
                "    id     INT PRIMARY KEY AUTO_INCREMENT,",
                "    nome   VARCHAR(40)  NOT NULL,",
                "    curso  VARCHAR(20),",
                "    nota   DECIMAL(3,1),",
                "    nacido DATE",
                ");",
            ]}),
            ("conceito", ("Chave primária e AUTO_INCREMENT",
                          "A <b>PRIMARY KEY</b> identifica cada linha de forma única (nunca repete, nunca "
                          "nula). Com <b>AUTO_INCREMENT</b>, o próprio MySQL numera as linhas: 1, 2, 3… — "
                          "você não informa o id no INSERT.")),
            ("codigo", {"titulo": "Consultar: o SELECT mínimo", "ling": "sql", "linhas": [
                "SELECT nome, nota FROM alunos;      -- colunas escolhidas",
                "SELECT * FROM alunos;               -- todas as colunas",
            ]}),
            ("h", "Boas práticas de digitação SQL"),
            ("lista", [
                "Comandos em MAIÚSCULAS, nomes de tabela/coluna em minúsculas (legibilidade);",
                "Uma cláusula por linha a partir do FROM/WHERE;",
                "Comentários com <b>--</b> explicando a intenção;",
                "Guarde scripts .sql por semana: eles viram seu histórico de estudo.",
            ]),
        ], "slides": {"pontos": [
            "DDL define estrutura (CREATE/ALTER/DROP); DML cuida dos dados",
            "CREATE TABLE com tipos certos + PRIMARY KEY AUTO_INCREMENT",
            "SELECT colunas FROM tabela = consulta mínima",
            "Scripts .sql salvos por semana = caderno de SQL",
        ], "codigo": {"titulo": "CREATE + SELECT", "linhas": [
            "CREATE TABLE alunos (",
            "  id INT PRIMARY KEY AUTO_INCREMENT,",
            "  nome VARCHAR(40) NOT NULL,",
            "  nota DECIMAL(3,1));",
            "SELECT nome, nota FROM alunos;",
        ]}, "nota": "Escreva o CREATE no projetor com erros propositalmente (vírgula faltando) e deixe a "
                   "turma achar antes de executar."}},
        {"num": 5, "titulo": "SQL — manipulação: INSERT, UPDATE, DELETE + VB6 (semana 5)", "blocos": [
            ("codigo", {"titulo": "Inserir, alterar, excluir", "ling": "sql", "linhas": [
                "INSERT INTO alunos (nome, curso, nota)",
                "VALUES ('Ana Silva', 'Informática', 8.5);",
                "",
                "UPDATE alunos SET nota = 7.0 WHERE id = 2;      -- SEMPRE com WHERE!",
                "",
                "DELETE FROM alunos WHERE id = 3;               -- SEMPRE com WHERE!",
            ]}),
            ("atencao", "<b>UPDATE/DELETE sem WHERE afetam TODAS as linhas.</b> Antes de executar, rode o "
                        "SELECT com o mesmo WHERE para conferir quais linhas serão tocadas. Regra de "
                        "laboratório: SELECT antes, manipulação depois."),
            ("h", "SQL dentro do programa VB6"),
            ("p", "Com a conexão aberta, o VB6 envia SQL com <b>cn.Execute</b>. Comandos de manipulação "
                  "não retornam tabela; consultas retornam um <b>Recordset</b> (veremos a fundo na semana 6 "
                  "e no módulo 11)."),
            ("codigo", {"titulo": "Modulo SqlAlunos.bas — manipulação pelo programa", "ling": "vb", "linhas": [
                "Public Sub InserirAluno(nome As String, nota As Single)",
                "    cn.Execute \"INSERT INTO alunos (nome, nota) VALUES ('\" & _",
                "                 nome & \"', \" & nota & \")\"",
                "End Sub",
                "",
                "Public Sub SubirNota(id As Integer, nova As Single)",
                "    cn.Execute \"UPDATE alunos SET nota = \" & nova & _",
                "                 \" WHERE id = \" & id",
                "End Sub",
            ]}),
            ("dica", "Montar SQL por concatenação (&) é o jeito didático agora; em sistemas reais usamos "
                     "parâmetros/validação para evitar injeção de SQL — consciência que já nasce aqui."),
        ], "slides": {"pontos": [
            "INSERT colunas VALUES (...); UPDATE/DELETE SEMPRE com WHERE",
            "SELECT com o mesmo WHERE antes de manipular (conferência)",
            "VB6: cn.Execute envia o SQL ao servidor",
            "Concatenação & monta o comando agora; consciência de injeção de SQL desde já",
        ], "codigo": {"titulo": "Manipulação segura", "linhas": [
            "UPDATE alunos SET nota = 7.0 WHERE id = 2;",
            "DELETE FROM alunos WHERE id = 3;",
            "-- antes: SELECT * FROM alunos WHERE id = 2;",
        ]}, "nota": "Demonstre o estrago: DELETE sem WHERE em tabela de teste (e o alívio do INSERT de "
                   "volta). Memória emocional = aprendizado."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Script completo da semana", "tipo": "pratico",
         "enunciado": "Entregue um script .sql com: CREATE TABLE produtos(id, nome, preco DECIMAL(7,2), "
                      "estoque INT); 5 INSERT; 2 UPDATE com WHERE; 1 DELETE com WHERE; e 3 SELECT (todos os "
                      "campos; só nome e preco; só os com estoque > 0).",
         "esperado": "Script executável sem erros, com WHERE em todas as manipulações e SELECT de conferência "
                     "antes delas.",
         "orientacao": "Correção automatizada: execute o script de cada dupla em um banco limpo de teste."},
        {"num": 2, "titulo": "Manipulação pelo VB6", "tipo": "pratico",
         "enunciado": "Formulário com 2 botões: ‘Cadastrar’ (InputBox nome e nota → InserirAluno) e "
                      "‘Corrigir nota’ (InputBox id e nova nota → SubirNota). Mostre MsgBox de confirmação.",
         "esperado": "Inserções e updates refletindo no banco (conferir via cliente MySQL); MsgBox após cada "
                     "operação.",
         "orientacao": "Conferir no projetor: alterar no VB6 e mostrar a mudança no cliente MySQL ao vivo "
                       "(efeito cliente/servidor)."},
        {"num": 3, "titulo": "Caça ao erro SQL", "tipo": "escrito",
         "enunciado": "Cada comando abaixo tem 1 erro. Identifique e corrija: (a) INSERT alunos VALUES "
                      "('Ana'); (b) UPDATE alunos SET nota = 9; (c) SELECT nome FROM alunos WHERE nota = "
                      "'8,5'; (d) DELETE FROM alunos WHERE nome = Ana.",
         "esperado": "(a) faltam colunas/valores completos; (b) falta WHERE; (c) Decimal usa ponto 8.5 sem "
                     "aspas de texto; (d) texto sem aspas simples 'Ana'.",
         "orientacao": "Correção dialogada; reforce a regra do WHERE e o uso de aspas simples em strings SQL."},
    ],
    "teste_rapido": [
        {"enunciado": "CREATE TABLE pertence a qual família do SQL?",
         "alt": ["DML", "DDL", "DCL", "TCL"],
         "resposta": 1, "comentario": "DDL define estrutura; DML manipula dados."},
        {"enunciado": "PRIMARY KEY AUTO_INCREMENT garante:",
         "alt": ["valores duplicados permitidos", "identificador único gerado automaticamente",
                 "ordenação alfabética", "criptografia da coluna"],
         "resposta": 1, "comentario": "Chave única, não nula, numerada pelo servidor."},
        {"enunciado": "UPDATE sem WHERE:",
         "alt": ["altera a primeira linha", "altera todas as linhas da tabela", "dá erro de sintaxe",
                 "não faz nada"],
         "resposta": 1, "comentario": "Sem filtro, o comando vale para todas as linhas — por isso o SELECT "
                       "de conferência antes."},
        {"enunciado": "No VB6, enviamos um comando SQL ao servidor com:",
         "alt": ["cn.Execute", "Printer.Print", "Form_Load", "MsgBox"],
         "resposta": 0, "comentario": "Connection.Execute; consultas devolvem Recordset."},
        {"enunciado": "Strings em SQL são escritas com:",
         "alt": ["aspas duplas", "aspas simples", "crases", "sem aspas"],
         "resposta": 1, "comentario": "'Ana Silva' — aspas simples; aspas duplas são do VB6."},
    ],
    "avaliacao_ref": None,
}

M4 = {
    "num": 4, "titulo": "SQL — consultas e filtros",
    "parte_num": 2, "parte_titulo": "Linguagem SQL",
    "aulas_faixa": "Aulas 21 a 24", "semanas": "Semana 6",
    "objetivos": [
        "Filtrar linhas com WHERE (comparação, BETWEEN, LIKE, IN).",
        "Ordenar resultados com ORDER BY (ASC/DESC).",
        "Resumir dados com funções de agregação (COUNT, SUM, AVG, MAX, MIN) e GROUP BY.",
        "Aplicar consultas em cenários reais de dados (estudo de caso).",
    ],
    "aulas": [
        {"num": 6, "titulo": "Consultas que respondem perguntas", "blocos": [
            ("h", "WHERE: a pergunta certa"),
            ("codigo", {"titulo": "Filtros essenciais", "ling": "sql", "linhas": [
                "SELECT nome, nota FROM alunos WHERE nota >= 7;",
                "SELECT nome FROM alunos WHERE curso = 'Informática' AND nota >= 7;",
                "SELECT nome FROM alunos WHERE nome LIKE 'A%';      -- começa com A",
                "SELECT nome FROM alunos WHERE nota BETWEEN 5 AND 7;",
                "SELECT nome FROM alunos WHERE curso IN ('Redes', 'Informática');",
            ]}),
            ("h", "ORDER BY: a apresentação do resultado"),
            ("codigo", {"titulo": "Ordenação", "ling": "sql", "linhas": [
                "SELECT nome, nota FROM alunos ORDER BY nota DESC;      -- maiores primeiro",
                "SELECT nome, nota FROM alunos ORDER BY nome ASC;       -- A → Z",
            ]}),
            ("h", "Agregações: o resumo da ópera"),
            ("codigo", {"titulo": "COUNT, SUM, AVG, MAX, MIN + GROUP BY", "ling": "sql", "linhas": [
                "SELECT COUNT(*)            AS total   FROM alunos;",
                "SELECT AVG(nota)           AS media   FROM alunos;",
                "SELECT MAX(nota), MIN(nota)           FROM alunos;",
                "",
                "SELECT curso, COUNT(*) AS qtd, AVG(nota) AS media",
                "FROM alunos",
                "GROUP BY curso",
                "ORDER BY media DESC;",
            ]}),
            ("conceito", ("GROUP BY responde “por grupo”",
                          "Sem GROUP BY, as agregações resumem a tabela inteira. Com GROUP BY curso, o MySQL "
                          "separa os grupos e calcula COUNT/AVG <b>dentro de cada grupo</b> — é assim que "
                          "nascem relatórios gerenciais.")),
            ("h", "Estudo de caso: a loja"),
            ("p", "Com a tabela vendas(id, produto, qtd, valor, datavenda): quantas vendas por produto? "
                  "Faturamento total? Melhor mês? Cada pergunta vira uma consulta — e depois vira relatório "
                  "no módulo 13."),
            ("codigo", {"titulo": "Perguntas de negócio em SQL", "ling": "sql", "linhas": [
                "SELECT produto, SUM(qtd) AS unidades, SUM(qtd * valor) AS faturamento",
                "FROM vendas",
                "GROUP BY produto",
                "ORDER BY faturamento DESC;",
            ]}),
        ], "slides": {"pontos": [
            "WHERE: =, >=, BETWEEN, LIKE 'A%', IN (...) — e AND/OR",
            "ORDER BY col ASC|DESC organiza a resposta",
            "COUNT/SUM/AVG/MAX/MIN resumem; GROUP BY resume POR GRUPO",
            "Cada pergunta de negócio = uma consulta (estudo de caso da loja)",
        ], "codigo": {"titulo": "Consulta gerencial", "linhas": [
            "SELECT curso, COUNT(*) qtd, AVG(nota) media",
            "FROM alunos GROUP BY curso ORDER BY media DESC;",
        ]}, "nota": "Monte as perguntas ANTES dos comandos com a turma ('quantos aprovados por curso?') e "
                   "deixe que proponham o SQL em duplas antes de mostrar."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Dez perguntas, dez consultas", "tipo": "pratico",
         "enunciado": "No banco escola (alunos, produtos, vendas): escreva e execute 10 consultas: 3 com "
                      "WHERE simples, 2 com LIKE/BETWEEN, 2 com ORDER BY, 3 com agregação (uma delas com "
                      "GROUP BY). Salve no script consultas_s06.sql.",
         "esperado": "Script com 10 SELECT corretos e resultados conferidos no caderno.",
         "orientacao": "Correção em duplas trocadas: cada dupla executa o script da outra e valida resultados."},
        {"num": 2, "titulo": "Consultas no VB6", "tipo": "pratico",
         "enunciado": "Formulário com ListBox e botão ‘Listar aprovados’: use cn.Execute com SELECT ... WHERE "
                      "nota >= 7 ORDER BY nome e preencha o ListBox percorrendo o Recordset (Do While Not "
                      "rs.EOF).",
         "esperado": "ListBox populado em ordem alfabética apenas com aprovados; rs.MoveNext e rs.Close "
                     "presentes.",
         "orientacao": "Este é o embrião do módulo 11: valorize o laço Do While Not rs.EOF como padrão ouro."},
        {"num": 3, "titulo": "Relatório em papel de uma consulta", "tipo": "escrito",
         "enunciado": "Escolha uma consulta com GROUP BY do exercício 1 e desenhe no caderno a tabela de "
                      "resultado (colunas e linhas) exatamente como o MySQL devolveria.",
         "esperado": "Tabela desenhada com os grupos e valores coerentes com os dados inseridos.",
         "orientacao": "Conferência cruzada com a saída real no cliente MySQL; discute interpretação de "
                       "resultado, não só sintaxe."},
    ],
    "teste_rapido": [
        {"enunciado": "Para filtrar nomes que começam com ‘A’:",
         "alt": ["WHERE nome = 'A'", "WHERE nome LIKE 'A%'", "WHERE nome IN 'A'", "WHERE LEFT(nome) = A"],
         "resposta": 1, "comentario": "LIKE com curinga % casa padrões de texto."},
        {"enunciado": "ORDER BY nota DESC exibe:",
         "alt": ["das menores para as maiores", "das maiores para as menores", "em ordem de inserção",
                 "aleatoriamente"],
         "resposta": 1, "comentario": "DESC = decrescente; ASC (padrão) = crescente."},
        {"enunciado": "COUNT(*) com GROUP BY curso retorna:",
         "alt": ["o total geral de alunos", "a quantidade de alunos por curso",
                 "o número de cursos existentes apenas", "a média por curso"],
         "resposta": 1, "comentario": "Agregação calculada dentro de cada grupo definido pelo GROUP BY."},
        {"enunciado": "BETWEEN 5 AND 7 equivale a:",
         "alt": ["nota > 5 AND nota < 7", "nota >= 5 AND nota <= 7", "nota IN (5,7)", "nota = 5 OR nota = 7"],
         "resposta": 1, "comentario": "BETWEEN inclui as pontas (fechado nos extremos)."},
        {"enunciado": "No VB6, o resultado de um SELECT chega como:",
         "alt": ["MsgBox", "Recordset (ADO)", "arquivo .txt", "Printer"],
         "resposta": 1, "comentario": "ADODB.Recordset percorrido com Do While Not rs.EOF."},
    ],
    "avaliacao_ref": "A1",
}

MODULOS = [M1, M2, M3, M4]
