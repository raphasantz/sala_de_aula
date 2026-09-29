# -*- coding: utf-8 -*-
"""LP2 — Módulos 5 a 10 (Partes III e IV): programação estruturada, estruturas de dados,
Strings, modularização e arquivos. Semanas 7 a 14."""

M5 = {
    "num": 5, "titulo": "Programação estruturada no VB6",
    "parte_num": 3, "parte_titulo": "Programação Estruturada e Estruturas de Dados",
    "aulas_faixa": "Aulas 25 a 28", "semanas": "Semana 7",
    "objetivos": [
        "Aplicar sequência, seleção (If/Select Case) e repetição (For/Do/While) no VB6.",
        "Escolher a estrutura de controle adequada a cada problema.",
        "Organizar o código com indentação, comentários e nomes claros.",
        "Resolver problemas clássicos de lógica com laços e decisões.",
    ],
    "aulas": [
        {"num": 7, "titulo": "Seleção e repetição: o cânone estruturado", "blocos": [
            ("h", "Seleção: If completo e Select Case"),
            ("codigo", {"titulo": "If / ElseIf / Else — situação do aluno", "ling": "vb", "linhas": [
                "Dim nota As Single",
                "nota = Val(InputBox(\"Digite a nota:\"))",
                "",
                "If nota >= 7 Then",
                "    Print nota; \"- APROVADO\"",
                "ElseIf nota >= 5 Then",
                "    Print nota; \"- RECUPERAÇÃO\"",
                "Else",
                "    Print nota; \"- REPROVADO\"",
                "End If",
            ]}),
            ("codigo", {"titulo": "Select Case — menu de opções", "ling": "vb", "linhas": [
                "Select Case opcao",
                "    Case 1",
                "        Call CadastrarAluno",
                "    Case 2",
                "        Call ListarAlunos",
                "    Case 3",
                "        Call GerarRelatorio",
                "    Case Else",
                "        MsgBox \"Opção inválida\", vbExclamation",
                "End Select",
            ]}),
            ("h", "Repetição: For, Do While e Do Until"),
            ("codigo", {"titulo": "Os três laços, lado a lado", "ling": "vb", "linhas": [
                "' FOR: quando se sabe quantas voltas",
                "For i = 1 To 10",
                "    Print i;",
                "Next i",
                "",
                "' DO WHILE: testa antes, repete enquanto verdadeiro",
                "Do While nota <> -1",
                "    soma = soma + nota",
                "    nota = Val(InputBox(\"Nota (-1 termina):\"))",
                "Loop",
                "",
                "' DO UNTIL: repete até a condição virar verdadeira",
                "Do Until senha = \"1234\"",
                "    senha = InputBox(\"Senha:\")",
                "Loop",
            ]}),
            ("conceito", ("Qual laço escolher?",
                          "<b>For</b>: número de voltas conhecido (contar, percorrer vetor). "
                          "<b>Do While</b>: repetir enquanto uma condição valer (ler até sentinela). "
                          "<b>Do Until</b>: repetir até alcançar um estado (validar entrada). "
                          "<b>While...Wend</b>: existe no VB6, mas evitamos — o Do é mais claro e flexível.")),
            ("h", "Organização lógica do código"),
            ("lista", [
                "Indentação de 4 espaços dentro de cada bloco (If/For/Select);",
                "Comentários ' explicando o PORQUÊ, não o óbvio;",
                "Uma responsabilidade por Sub (nome em verbo: CalcularMedia, ListarAprovados);",
                "Variáveis declaradas no topo com Dim e tipo explícito;",
                "Sentinela documentada: -1 termina a leitura (combinado com o usuário).",
            ]),
            ("atencao", "Laço infinito no VB6 trava a IDE: se acontecer, Ctrl+Break (ou o botão End) e "
                        "procure a variável que não avança. Todo Do/While precisa de um caminho que torne "
                        "a condição falsa."),
        ], "slides": {"pontos": [
            "If/ElseIf/Else para faixas; Select Case para menus/valores fixos",
            "For = voltas conhecidas · Do While = enquanto · Do Until = até",
            "While...Wend existe, mas o curso padroniza Do (mais claro)",
            "Organização: indentação, comentários de porquê, Sub com uma responsabilidade",
            "Sentinela -1 e Ctrl+Break contra laços infinitos",
        ], "codigo": {"titulo": "Menu com Select Case", "linhas": [
            "Select Case opcao",
            "    Case 1: Call CadastrarAluno",
            "    Case 2: Call ListarAlunos",
            "    Case Else: MsgBox \"Opção inválida\"",
            "End Select",
        ]}, "nota": "Aulas 25–28: demonstrar cada laço com o MESMO problema (soma de notas até sentinela) "
                   "e comparar as três soluções no projetor."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Calculadora estruturada", "tipo": "pratico",
         "enunciado": "Formulário com dois Text (n1, n2) e um Combo de operação (+, -, *, /): ao clicar em "
                      "=, use Select Case para calcular e Label para o resultado; trate divisão por zero com "
                      "MsgBox (If).",
         "esperado": "Calculadora funcional com Select Case e tratamento de divisão por zero sem travar.",
         "orientacao": "Conferir uso de Val() nos Text e Case Else para operação inválida."},
        {"num": 2, "titulo": "Leitura até sentinela", "tipo": "pratico",
         "enunciado": "Com Do While, leia notas até o usuário digitar -1; ao final mostre quantidade, soma, "
                      "média, maior e menor nota (variáveis de acompanhamento).",
         "esperado": "Laço com sentinela correta e cinco estatísticas certas (cuidado: -1 não entra na conta).",
         "orientacao": "Erro clássico: contar o -1. Peça teste com 0 notas digitadas (média não pode dar erro "
                       "de divisão)."},
        {"num": 3, "titulo": "Refatoração dirigida", "tipo": "escrito",
         "enunciado": "O código abaixo funciona, mas está desorganizado. Reescreva-o com indentação, "
                      "comentários de porquê, nomes claros e um Select Case no lugar dos Ifs encadeados de "
                      "menu: (código com 6 Ifs aninhados sem indentação fornecido no quadro/apostila).",
         "esperado": "Versão legível: Select Case para o menu, Subs nomeados por responsabilidade, "
                     "indentação consistente.",
         "orientacao": "Correção coletiva no projetor com votação: qual versão é mais fácil de manter? "
                       "Introduz o valor da modularização (próxima semana 12)."},
    ],
    "teste_rapido": [
        {"enunciado": "Para um menu com opções fixas 1, 2 e 3, a estrutura mais legível é:",
         "alt": ["If aninhados", "Select Case", "Do Until", "For"],
         "resposta": 1, "comentario": "Select Case compara um valor com casos fixos — menus ficam limpos."},
        {"enunciado": "Do While repete:",
         "alt": ["sempre ao menos uma vez", "enquanto a condição for verdadeira (teste antes)",
                 "até a condição virar verdadeira", "um número fixo de voltas"],
         "resposta": 1, "comentario": "Testa antes de cada volta; pode executar zero vezes."},
        {"enunciado": "Um laço infinito geralmente acontece por:",
         "alt": ["excesso de comentários", "variável de controle que nunca torna a condição falsa",
                 "usar Print dentro do laço", "declarar Dim dentro do laço"],
         "resposta": 1, "comentario": "Sem avanço/saída, a condição nunca muda — Ctrl+Break e corrija."},
        {"enunciado": "Sentinela é:",
         "alt": ["um erro de execução", "um valor combinado que encerra a leitura (ex.: -1)",
                 "uma variável global", "um tipo de laço"],
         "resposta": 1, "comentario": "Padrão de leitura até sentinela com Do While."},
        {"enunciado": "Val(InputBox(...)) serve para:",
         "alt": ["exibir texto", "converter o texto digitado em número", "validar senha",
                 "fechar a janela"],
         "resposta": 1, "comentario": "InputBox retorna String; Val converte para número."},
    ],
    "avaliacao_ref": None,
}

M6 = {
    "num": 6, "titulo": "Vetores e matrizes",
    "parte_num": 3, "parte_titulo": "Programação Estruturada e Estruturas de Dados",
    "aulas_faixa": "Aulas 29 a 36", "semanas": "Semanas 8 a 9",
    "objetivos": [
        "Declarar, preencher, ler e processar vetores (arrays unidimensionais).",
        "Trabalhar com matrizes (duas dimensões) e laços aninhados.",
        "Resolver problemas clássicos: média, maior/menor, busca, somas por linha/coluna.",
        "Combinar vetores/matrizes com laços e decisões de forma organizada.",
    ],
    "aulas": [
        {"num": 8, "titulo": "Vetores: muitas caixinhas, um nome só", "blocos": [
            ("h", "Declaração e índices"),
            ("codigo", {"titulo": "Vetor de 10 notas", "ling": "vb", "linhas": [
                "Dim notas(1 To 10) As Single",
                "Dim i As Integer",
                "",
                "' preenchimento",
                "For i = 1 To 10",
                "    notas(i) = Val(InputBox(\"Nota \" & i & \":\"))",
                "Next i",
                "",
                "' leitura/processamento",
                "Dim soma As Single",
                "For i = 1 To 10",
                "    soma = soma + notas(i)",
                "Next i",
                "Print \"Média: \"; soma / 10",
            ]}),
            ("conceito", ("Índice é o endereço da caixinha",
                          "notas(1) é a PRIMEIRA posição quando declaramos (1 To 10). O índice pode vir de "
                          "uma variável ou expressão: notas(i), notas(posicao) — é isso que permite "
                          "percorrer tudo com um laço.")),
            ("h", "Processamentos clássicos"),
            ("codigo", {"titulo": "Maior, menor e busca", "ling": "vb", "linhas": [
                "Dim maior As Single, menor As Single, pos As Integer",
                "maior = notas(1): menor = notas(1)",
                "For i = 2 To 10",
                "    If notas(i) > maior Then maior = notas(i)",
                "    If notas(i) < menor Then menor = notas(i)",
                "Next i",
                "",
                "' busca: em que posição está a nota 10?",
                "pos = 0",
                "For i = 1 To 10",
                "    If notas(i) = 10 Then pos = i",
                "Next i",
                "If pos > 0 Then Print \"Achou na posição \"; pos",
            ]}),
            ("dica", "Padrão de ouro: inicialize maior/menor com o PRIMEIRO elemento (não com 0!) e comece o "
                     "laço de comparação no segundo. Funciona até com notas negativas."),
        ], "slides": {"pontos": [
            "Dim notas(1 To 10) As Single — 10 posições sob um nome",
            "Índice variável (i) = percorrer com laço",
            "Clássicos: soma/média, maior/menor, busca por posição",
            "Maior/menor iniciam no 1º elemento, laço começa no 2º",
          ], "codigo": {"titulo": "Percorrer e processar", "linhas": [
            "For i = 1 To 10",
            "    soma = soma + notas(i)",
            "Next i",
        ]}, "nota": "Semana 8 = semana do TESTE da A1 (15 pts): reserve a aula 32 para revisão dirigida "
                   "com o modelo de prova da apostila."}},
        {"num": 9, "titulo": "Matrizes: linhas e colunas", "blocos": [
            ("h", "Declaração e acesso"),
            ("codigo", {"titulo": "Matriz 3×4 e laços aninhados", "ling": "vb", "linhas": [
                "Dim m(1 To 3, 1 To 4) As Integer",
                "Dim i As Integer, j As Integer",
                "",
                "' preenchimento",
                "For i = 1 To 3",
                "    For j = 1 To 4",
                "        m(i, j) = i * j",
                "    Next j",
                "Next i",
                "",
                "' soma por linha",
                "For i = 1 To 3",
                "    Dim sl As Integer: sl = 0",
                "    For j = 1 To 4",
                "        sl = sl + m(i, j)",
                "    Next j",
                "    Print \"Linha \"; i; \" soma \"; sl",
                "Next i",
            ]}),
            ("conceito", ("Laço de fora = linha; laço de dentro = coluna",
                          "Para varrer uma matriz, o laço externo percorre as <b>linhas</b> (i) e o interno, "
                          "as <b>colunas</b> (j). Somar por linha: zere o acumulador DENTRO do laço de "
                          "linhas, antes do laço de colunas.")),
            ("h", "Aplicações"),
            ("lista", [
                "Tabela de notas por aluno × bimestre;",
                "Tabuada 1–9 em grade;",
                "Mapa de estoque por loja × produto;",
                "Transposição e comparação de matrizes (desafio).",
            ]),
            ("atencao", "Índice fora da faixa (m(4,1) em matriz 3×4) gera erro de execução “subscript out "
                        "of range”. Confira os limites do For com a declaração."),
        ], "slides": {"pontos": [
            "Dim m(1 To 3, 1 To 4): linhas × colunas",
            "Laço externo = linha (i); interno = coluna (j)",
            "Acumulador por linha zera DENTRO do laço externo",
            "'Subscript out of range' = índice fora da faixa",
        ], "codigo": {"titulo": "Varredura padrão", "linhas": [
            "For i = 1 To 3",
            "    For j = 1 To 4",
            "        Print m(i, j);",
            "    Next j",
            "    Print",
            "Next i",
        ]}, "nota": "Desenhe a matriz no quadro como grade e “aponte” os índices com dois dedos (i, j) "
                   "enquanto o laço roda — visual fixa o aninhamento."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Vetor completo", "tipo": "pratico",
         "enunciado": "Leia 8 temperaturas em um vetor; mostre: média, maior, menor, quantas acima da média "
                      "e a posição da maior.",
         "esperado": "Cinco saídas corretas com um único vetor e laços separados por responsabilidade.",
         "orientacao": "Conferir inicialização maior/menor e a contagem acima da média (laço extra)."},
        {"num": 2, "titulo": "Matriz de notas", "tipo": "pratico",
         "enunciado": "Matriz 4 alunos × 3 bimestres: preencha por InputBox; mostre a média de cada aluno "
                      "(por linha), a média de cada bimestre (por coluna) e a maior nota com sua posição.",
         "esperado": "Médias por linha e coluna corretas + maior nota com (i, j).",
         "orientacao": "Ponto de atenção: dois acumuladores diferentes (linha × coluna) e zerar no lugar "
                       "certo. Teste cruzado entre duplas com gabarito manual."},
        {"num": 3, "titulo": "Busca no vetor", "tipo": "escrito",
         "enunciado": "Escreva de memória o padrão de busca: ler um valor e informar a posição dele no "
                      "vetor de 10 notas (ou ‘não encontrado’). Depois explique por que pos = 0 antes do "
                      "laço é essencial.",
         "esperado": "Laço com If comparando e guardando pos; explicação: 0 funciona como flag de “não "
                     "achou”, pois posições válidas começam em 1.",
         "orientacao": "Reforce o conceito de flag/sentinela de busca — reaparece em arquivos e Recordset."},
    ],
    "teste_rapido": [
        {"enunciado": "Dim v(1 To 5) As Integer cria:",
         "alt": ["5 variáveis chamadas v1..v5", "um vetor com posições 1 a 5", "uma matriz 5×5",
                 "um vetor de textos"],
         "resposta": 1, "comentario": "Array unidimensional com índices explícitos de 1 a 5."},
        {"enunciado": "Para percorrer todo o vetor, o índice usado no acesso deve ser:",
         "alt": ["fixo (v(1))", "a variável do laço (v(i))", "sempre 0", "um InputBox"],
         "resposta": 1, "comentario": "Índice variável é o que permite o percurso com For."},
        {"enunciado": "Na varredura de matriz, o laço EXTERNO normalmente percorre:",
         "alt": ["as colunas", "as linhas", "as diagonais", "os índices aleatórios"],
         "resposta": 1, "comentario": "Externo = linhas (i); interno = colunas (j)."},
        {"enunciado": "‘Subscript out of range’ significa:",
         "alt": ["variável não declarada", "índice fora dos limites declarados", "divisão por zero",
                 "arquivo não encontrado"],
         "resposta": 1, "comentario": "Acessar m(4,1) em matriz 3×4, por exemplo."},
        {"enunciado": "Para achar o maior valor de um vetor de notas (que podem ser negativas), inicialize "
                    "maior com:",
         "alt": ["0", "10", "o primeiro elemento do vetor", "um número aleatório"],
         "resposta": 2, "comentario": "Iniciar no 1º elemento garante corretude para qualquer faixa."},
    ],
    "avaliacao_ref": "A1-teste",
}

M7 = {
    "num": 7, "titulo": "Registros: agrupando informações relacionadas",
    "parte_num": 3, "parte_titulo": "Programação Estruturada e Estruturas de Dados",
    "aulas_faixa": "Aulas 37 a 40", "semanas": "Semana 10",
    "objetivos": [
        "Definir tipos estruturados com Type/End Type.",
        "Declarar variáveis e vetores de registros.",
        "Acessar campos com o operador ponto e processar coleções de registros.",
        "Modelar entidades reais (aluno, produto) com registros.",
    ],
    "aulas": [
        {"num": 10, "titulo": "Registros (Type): a ficha dentro do programa", "blocos": [
            ("h", "Definindo um tipo"),
            ("codigo", {"titulo": "Module Tipos.bas", "ling": "vb", "linhas": [
                "Public Type Aluno",
                "    nome   As String * 40",
                "    matricula As Integer",
                "    nota   As Single",
                "End Type",
                "",
                "Public Type Produto",
                "    codigo As Integer",
                "    descricao As String * 30",
                "    preco  As Currency",
                "    estoque As Integer",
                "End Type",
            ]}),
            ("h", "Usando registros e vetores de registros"),
            ("codigo", {"titulo": "Ficha e coleção", "ling": "vb", "linhas": [
                "Dim a As Aluno",
                "a.nome = \"Ana Silva\"",
                "a.matricula = 101",
                "a.nota = 8.5",
                "Print a.nome; \" - \"; a.nota",
                "",
                "' coleção: vetor de fichas",
                "Dim turma(1 To 30) As Aluno",
                "Dim i As Integer",
                "For i = 1 To 30",
                "    turma(i).nome = InputBox(\"Nome do aluno \" & i)",
                "    turma(i).nota = Val(InputBox(\"Nota:\"))",
                "Next i",
            ]}),
            ("conceito", ("Registro = linha de tabela dentro do programa",
                          "Um registro agrupa campos de tipos diferentes sob um nome só — exatamente como "
                          "uma LINHA de tabela no banco. Vetor de registros = tabela em memória. É a ponte "
                          "mental entre as estruturas do VB6 e as tabelas do MySQL.")),
            ("h", "Processamentos típicos"),
            ("codigo", {"titulo": "Aprovados da turma (vetor de registros)", "ling": "vb", "linhas": [
                "For i = 1 To 30",
                "    If turma(i).nota >= 7 Then",
                "        Print turma(i).nome; \" aprovado com \"; turma(i).nota",
                "    End If",
                "Next i",
            ]}),
            ("dica", "String * 40 fixa o tamanho do campo (herança dos arquivos de registro fixo). Para "
                     "textos de tamanho livre em memória, use String simples — discutimos o trade-off na "
                     "semana de arquivos."),
        ], "slides": {"pontos": [
            "Public Type ... End Type define a ficha (campos de tipos diferentes)",
            "Acesso por ponto: a.nome, turma(i).nota",
            "Vetor de registros = tabela em memória",
            "Ponte conceitual: registro ↔ linha de tabela no MySQL",
        ], "codigo": {"titulo": "Registro + coleção", "linhas": [
            "Public Type Aluno",
            "    nome As String * 40",
            "    nota As Single",
            "End Type",
            "Dim turma(1 To 30) As Aluno",
        ]}, "nota": "Compare lado a lado: CREATE TABLE alunos (...) no MySQL × Public Type Aluno no VB6. "
                   "A turma percebe que já pensa em banco de dados."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Ficha do produto", "tipo": "pratico",
         "enunciado": "Defina o Type Produto (codigo, descricao, preco, estoque); cadastre 5 produtos em um "
                      "vetor; liste os produtos com estoque < 5 (reposição) e o valor total do estoque "
                      "(preco × estoque somado).",
         "esperado": "Type correto, cadastro em vetor e duas saídas (reposição + valor total) conferindo.",
         "orientacao": "Conferir uso de Currency para preço e o acumulador do valor total."},
        {"num": 2, "titulo": "Turma completa", "tipo": "pratico",
         "enunciado": "Vetor de 10 registros Aluno: leia nome/matrícula/nota; mostre aprovados, reprovados, "
                      "média da turma e o nome do aluno de maior nota.",
         "esperado": "Quatro saídas corretas percorrendo o vetor de registros uma ou mais vezes.",
         "orientacao": "Incentive Subs separados (ListarAprovados, MediaTurma...) — prepara a semana 12."},
        {"num": 3, "titulo": "Modelagem no papel", "tipo": "escrito",
         "enunciado": "Para um controle de biblioteca, defina no caderno os Types Livro e Emprestimo "
                      "(campos e tipos) e explique como um vetor de cada um representaria as ‘tabelas’ do "
                      "sistema.",
         "esperado": "Types coerentes (ex.: Livro: codigo, titulo, autor, disponível; Emprestimo: codigoLivro, "
                     "matriculaAluno, data) e explicação da relação entre vetores.",
         "orientacao": "Essa modelagem vira o banco MySQL do projeto integrador — guarde os melhores modelos."},
    ],
    "teste_rapido": [
        {"enunciado": "Public Type Aluno ... End Type define:",
         "alt": ["um formulário", "um tipo estruturado (registro)", "um banco de dados", "uma Function"],
         "resposta": 1, "comentario": "Registro: campos de tipos diferentes sob um nome."},
        {"enunciado": "O acesso ao campo nota do i-ésimo aluno de um vetor de registros é:",
         "alt": ["turma.nota(i)", "turma(i).nota", "nota.turma(i)", "turma[i,nota]"],
         "resposta": 1, "comentario": "Primeiro o índice do vetor, depois o ponto e o campo."},
        {"enunciado": "Um vetor de registros equivale, no mundo do banco, a:",
         "alt": ["uma coluna", "uma tabela em memória (conjunto de linhas)", "um índice", "uma view"],
         "resposta": 1, "comentario": "Cada registro = linha; o vetor = conjunto de linhas."},
        {"enunciado": "String * 40 em um Type significa:",
         "alt": ["texto de até 40 caracteres com tamanho fixo", "40 strings diferentes",
                 "texto ilimitado", "número de 40 dígitos"],
         "resposta": 0, "comentario": "Campo de tamanho fixo — útil em arquivos de registro fixo."},
        {"enunciado": "Para somar o valor total do estoque (preco × estoque) percorrendo um vetor de "
                    "Produtos, usamos:",
         "alt": ["um laço com acumulador: total = total + p(i).preco * p(i).estoque",
                 "SUM(preco) como no SQL", "Print p.preco * p.estoque sem laço", "Count(p)"],
         "resposta": 0, "comentario": "Em memória, agregações são laços com acumulador — no banco, SQL."},
    ],
    "avaliacao_ref": None,
}

M8 = {
    "num": 8, "titulo": "Variáveis do tipo String",
    "parte_num": 4, "parte_titulo": "Strings, Modularização e Arquivos",
    "aulas_faixa": "Aulas 41 a 44", "semanas": "Semana 11",
    "objetivos": [
        "Armazenar, ler e exibir textos com variáveis String.",
        "Aplicar as funções de manipulação: Len, Mid$, Left$, Right$, UCase$, LCase$, Trim$, InStr, Replace.",
        "Validar e normalizar entradas de texto (caixa, espaços, padrões).",
        "Combinar Strings com números (Val, Str, Format) em saídas legíveis.",
    ],
    "aulas": [
        {"num": 11, "titulo": "String: o texto como dado", "blocos": [
            ("h", "O essencial das Strings"),
            ("codigo", {"titulo": "Funções de manipulação", "ling": "vb", "linhas": [
                "Dim s As String",
                "s = \"  Linguagem de Programação II  \"",
                "",
                "Print Len(s)                 ' 33 (conta espaços)",
                "Print Trim$(s)               ' sem espaços nas pontas",
                "Print UCase$(Trim$(s))       ' CAIXA ALTA",
                "Print Left$(s, 5)            ' \"  Lin\"",
                "Print Right$(s, 2)           ' \"  \"... cuidado com espaços!",
                "Print Mid$(s, 3, 9)          ' \"Linguagem\"",
                "Print InStr(s, \"Program\")    ' posição onde começa (16)",
                "Print Replace$(s, \"II\", \"III\")",
            ]}),
            ("conceito", ("Posições começam em 1",
                          "No VB6, Mid$/Left$/Right$ contam a partir de <b>1</b> (não de 0). InStr retorna 0 "
                          "quando não encontra — use como flag: If InStr(...) > 0 Then.")),
            ("h", "Validação e normalização de entrada"),
            ("codigo", {"titulo": "Padronizar nome digitado", "ling": "vb", "linhas": [
                "Dim nome As String",
                "nome = Trim$(InputBox(\"Nome completo:\"))",
                "",
                "If Len(nome) < 5 Then",
                "    MsgBox \"Nome muito curto!\"",
                "ElseIf InStr(nome, \" \") = 0 Then",
                "    MsgBox \"Digite nome e sobrenome!\"",
                "Else",
                "    nome = UCase$(nome)          ' padroniza caixa",
                "    Print nome",
                "End If",
            ]}),
            ("h", "Strings × números em saídas legíveis"),
            ("codigo", {"titulo": "Format e conversões", "ling": "vb", "linhas": [
                "Dim media As Single, txt As String",
                "media = 7.25",
                "txt = \"Média: \" & Format(media, \"0.00\")     ' Média: 7,25",
                "Print txt",
                "Print \"Hoje: \" & Format(Date, \"dd/mm/yyyy\")",
                "Print Str$(42) & \" | \" & Val(\"42 anos\")      ' 42 | 42",
            ]}),
            ("dica", "Montar mensagens com & e Format é o que separa saída de iniciante (“7,250000E+00”) de "
                     "saída profissional (“7,25”). Relatórios (semana 19) dependem disso."),
        ], "slides": {"pontos": [
            "Len, Trim$, UCase$, LCase$, Left$, Right$, Mid$, InStr, Replace$",
            "Posições começam em 1; InStr = 0 quando não acha",
            "Validação: comprimento, presença de espaço, caixa padronizada",
            "Format(n, \"0.00\") e Format(Date, \"dd/mm/yyyy\") para saídas legíveis",
        ], "codigo": {"titulo": "Normalizar entrada", "linhas": [
            "nome = UCase$(Trim$(InputBox(\"Nome:\")))",
            "If Len(nome) < 5 Or InStr(nome, \" \") = 0 Then",
            "    MsgBox \"Nome inválido\"",
        ]}, "nota": "Laboratório: peça validações criativas (placa de carro, telefone com DDD) — String é "
                   "o conteúdo mais divertido de validar."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Caixa de ferramentas de String", "tipo": "pratico",
         "enunciado": "Leia uma frase e mostre: comprimento sem espaços nas pontas; frase em caixa alta e "
                      "baixa; primeira e última palavra; posição da palavra ‘VB’; frase sem a palavra ‘não’ "
                      "(Replace).",
         "esperado": "Seis saídas corretas usando as funções da aula (última palavra via InStrRev ou Right "
                     "complito aceito).",
         "orientacao": "Discuta soluções diferentes para a última palavra — vale qualquer abordagem correta."},
        {"num": 2, "titulo": "Validador de matrículas", "tipo": "pratico",
         "enunciado": "Matrícula padrão: 2 letras + 4 números (ex.: AB1234). Leia uma string e valide "
                      "formato e comprimento com Len/Mid$/IsNumeric; mostre OK ou o motivo da recusa.",
         "esperado": "Validação por posição: Mid$(s,1,2) letras (Not IsNumeric) e Mid$(s,3,4) numérica; "
                     "mensagens específicas.",
         "orientacao": "Excelente para fixar Mid$ por posição; teste com casos inválidos variados."},
        {"num": 3, "titulo": "Recibo formatado", "tipo": "pratico",
         "enunciado": "Monte um ‘recibo’ em um Label multilinha: nome em caixa alta, data dd/mm/yyyy, valor "
                      "Format(v, \"R$ #,##0.00\") e linha separadora String(40, \"-\").",
         "esperado": "Recibo legível com todos os Format corretos e separador.",
         "orientacao": "Ponte direta para relatórios (semana 19): elogie os recibos mais bem alinhados."},
    ],
    "teste_rapido": [
        {"enunciado": "Mid$(\"LINGUAGEM\", 3, 4) retorna:",
         "alt": ["\"LING\"", "\"NGUA\"", "\"GUAG\"", "\"AGEM\""],
         "resposta": 1, "comentario": "Começa na posição 3 e pega 4 caracteres: N G U A."},
        {"enunciado": "InStr retorna 0 quando:",
         "alt": ["encontra no início", "não encontra o trecho", "o texto está vazio de espaços",
                 "o texto é numérico"],
         "resposta": 1, "comentario": "0 = não achou; >0 = posição inicial do trecho."},
        {"enunciado": "Para remover espaços das pontas de um texto digitado:",
         "alt": ["Trim$", "Mid$", "Left$", "Replace$ com \" \""],
         "resposta": 0, "comentario": "Trim$ corta espaços à esquerda e à direita."},
        {"enunciado": "No VB6, as posições de String contam a partir de:",
         "alt": ["0", "1", "-1", "depende do Option Base"],
         "resposta": 1, "comentario": "Funções de texto iniciam em 1."},
        {"enunciado": "Format(7.25, \"0.00\") produz:",
         "alt": ["7,25 como texto formatado", "725", "7.250000", "erro"],
         "resposta": 0, "comentario": "Saída legível com duas casas — padrão de relatórios."},
    ],
    "avaliacao_ref": None,
}

M9 = {
    "num": 9, "titulo": "Modularização: Sub, Function e Modules",
    "parte_num": 4, "parte_titulo": "Strings, Modularização e Arquivos",
    "aulas_faixa": "Aulas 45 a 48", "semanas": "Semana 12",
    "objetivos": [
        "Dividir programas em Sub e Function com responsabilidades únicas.",
        "Usar parâmetros (ByVal/ByRef) e retorno de valores.",
        "Organizar código em Modules (.bas) com escopos Public/Private.",
        "Refatorar código monolítico em módulos reutilizáveis.",
    ],
    "aulas": [
        {"num": 12, "titulo": "Modularização: dividir para conquistar", "blocos": [
            ("h", "Sub × Function (revisitando com profundidade)"),
            ("codigo", {"titulo": "Modulo Calculos.bas", "ling": "vb", "linhas": [
                "Public Function Media(n1 As Single, n2 As Single) As Single",
                "    Media = (n1 + n2) / 2        ' retorno = nome da Function",
                "End Function",
                "",
                "Public Function Situacao(m As Single) As String",
                "    If m >= 7 Then",
                "        Situacao = \"APROVADO\"",
                "    ElseIf m >= 5 Then",
                "        Situacao = \"RECUPERAÇÃO\"",
                "    Else",
                "        Situacao = \"REPROVADO\"",
                "    End If",
                "End Function",
                "",
                "Public Sub MostrarBoletim(n1 As Single, n2 As Single)",
                "    Dim m As Single",
                "    m = Media(n1, n2)",
                "    MsgBox \"Média \" & Format(m, \"0.0\") & \" - \" & Situacao(m)",
                "End Sub",
            ]}),
            ("h", "Parâmetros: ByVal e ByRef"),
            ("codigo", {"titulo": "Efeito colateral controlado", "ling": "vb", "linhas": [
                "Public Sub Dobrar(ByVal x As Integer, ByRef y As Integer)",
                "    x = x * 2      ' mexe só na CÓPIA local",
                "    y = y * 2        ' mexe na variável ORIGINAL do chamador",
                "End Sub",
                "",
                "Dim a As Integer, b As Integer",
                "a = 5: b = 5",
                "Dobrar a, b",
                "Print a; b           ' 5  10",
            ]}),
            ("conceito", ("ByVal protege; ByRef compartilha",
                          "<b>ByVal</b>: o parâmetro recebe uma cópia — o original não muda (padrão seguro). "
                          "<b>ByRef</b>: o parâmetro é a própria variável do chamador — use só quando a Sub "
                          "PRECISA devolver algo por parâmetro. No VB6, parâmetros são ByRef por padrão: "
                          "escreva ByVal explicitamente por segurança.")),
            ("h", "Escopo e organização em Modules"),
            ("lista", [
                "<b>Public</b> em Module (.bas): visível no projeto inteiro (conexão, cálculos, SQL);",
                "<b>Private</b>: só dentro do módulo/formulário (detalhes internos);",
                "Variável declarada dentro de Sub = <b>local</b>; no topo do Module com Public = <b>global</b> "
                "(use com parcimônia!);",
                "Nomes em verbo + objeto: CalcularMedia, ListarAprovados, GravarArquivo;",
                "Um módulo por assunto: Conexao.bas, Calculos.bas, Arquivos.bas, Relatorios.bas.",
            ]),
            ("h", "Refatoração: do monólito aos módulos"),
            ("p", "Pegue o exercício ‘monolítico’ da semana 7 (menu com tudo dentro de um clique) e divida: "
                  "um Module de regras (Functions puras), um Module de saída (Subs de Print/MsgBox) e o "
                  "formulário só orquestrando chamadas. Mesma funcionalidade, manutenção dez vezes mais "
                  "fácil."),
        ], "slides": {"pontos": [
            "Function retorna (nome da Function = retorno); Sub executa",
            "ByVal = cópia segura; ByRef = original (padrão VB6: declare ByVal!)",
            "Modules por assunto com Public/Private; globals com parcimônia",
            "Refatorar: formulário orquestra, módulos sabem fazer",
        ], "codigo": {"titulo": "Retorno por nome", "linhas": [
            "Public Function Media(n1 As Single, n2 As Single) As Single",
            "    Media = (n1 + n2) / 2",
            "End Function",
        ]}, "nota": "Refatoração ao vivo: comece com 80 linhas em um clique e termine com 4 módulos "
                   "legíveis. A turma vê o valor da técnica na prática."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Biblioteca de funções", "tipo": "pratico",
         "enunciado": "Crie Calculos.bas com: Media(n1,n2), MaiorDe3(a,b,c), EhPar(n) e PorExtensoDezena(n) "
                      "(10..19). Teste todas em um formulário com botões.",
         "esperado": "Quatro Functions puras (sem MsgBox dentro) retornando corretamente; formulário só "
                     "exibe resultados.",
         "orientacao": "Regra de ouro: Function não conversa com usuário (sem InputBox/MsgBox) — quem chama "
                       "orquestra."},
        {"num": 2, "titulo": "ByVal × ByRef na prática", "tipo": "pratico",
         "enunciado": "Implemente Sub Trocar(ByRef a, ByRef b) que inverte dois valores e Sub TrocarCopia"
                      "(ByVal a, ByVal b) que não muda nada fora; demonstre a diferença com Print.",
         "esperado": "Demonstração correta: Trocar altera as variáveis do chamador; TrocarCopia não.",
         "orientacao": "Pergunta de fixação: por que declaramos ByVal por padrão no curso?"},
        {"num": 3, "titulo": "Refatoração do monólito", "tipo": "pratico",
         "enunciado": "Refatore o menu monolítico da semana 7 em: Regras.bas (Functions), Saida.bas (Subs) e "
                      "formulário orquestrador com Select Case chamando as Subs.",
         "esperado": "Três camadas claras; nenhuma regra de negócio dentro do formulário.",
         "orientacao": "Checklist: nenhuma Function com MsgBox? nenhum Print em Regras.bas? nomes em verbo?"},
    ],
    "teste_rapido": [
        {"enunciado": "O valor de retorno de uma Function no VB6 é atribuído:",
         "alt": ["à palavra Return", "ao próprio nome da Function", "a uma variável global obrigatória",
                 "ao parâmetro ByRef sempre"],
         "resposta": 1, "comentario": "Media = (n1+n2)/2 — o nome da Function recebe o retorno."},
        {"enunciado": "ByVal significa que o parâmetro:",
         "alt": ["é a própria variável do chamador", "recebe uma cópia (original protegido)",
                 "deve ser numérico", "é opcional"],
         "resposta": 1, "comentario": "Cópia local; por segurança, declare ByVal explicitamente."},
        {"enunciado": "Modules .bas com rotinas Public servem para:",
         "alt": ["guardar telas", "compartilhar regras entre formulários do projeto",
                 "substituir o banco de dados", "compilar mais rápido"],
         "resposta": 1, "comentario": "Camada de regras reutilizável em todo o projeto."},
        {"enunciado": "Uma Function ‘pura’, no padrão do curso:",
         "alt": ["usa MsgBox para pedir dados", "não conversa com o usuário: só recebe e retorna",
                 "imprime com Print", "grava arquivo"],
         "resposta": 1, "comentario": "Entrada por parâmetros, saída por retorno; I/O fica com quem chama."},
        {"enunciado": "Variável declarada dentro de uma Sub é:",
         "alt": ["global", "local à execução da Sub", "pública do módulo", "estática permanente"],
         "resposta": 1, "comentario": "Escopo local: nasce e morre a cada chamada."},
    ],
    "avaliacao_ref": None,
}

M10 = {
    "num": 10, "titulo": "Arquivos e textos como transferência de dados",
    "parte_num": 4, "parte_titulo": "Strings, Modularização e Arquivos",
    "aulas_faixa": "Aulas 49 a 56", "semanas": "Semanas 13 a 14",
    "objetivos": [
        "Gravar e ler arquivos texto com Open/Close, Print #, Input # e Line Input #.",
        "Usar modos For Output, For Input e For Append corretamente.",
        "Detectar fim de arquivo com EOF e numerar arquivos com FreeFile.",
        "Integrar arquivos aos dados do programa: importação/exportação em fluxo controlado.",
    ],
    "aulas": [
        {"num": 13, "titulo": "Arquivos texto: gravar e ler", "blocos": [
            ("h", "O ciclo de vida de um arquivo"),
            ("codigo", {"titulo": "Gravar (Output) e acrescentar (Append)", "ling": "vb", "linhas": [
                "Dim n As Integer",
                "n = FreeFile                      ' número de arquivo livre",
                "Open \"c:\\lp2\\dados\\alunos.txt\" For Output As #n",
                "Print #n, \"Ana Silva;101;8.5\"     ' linha com campos separados",
                "Print #n, \"Beto Souza;102;6.0\"",
                "Close #n",
                "",
                "Open \"c:\\lp2\\dados\\alunos.txt\" For Append As #n",
                "Print #n, \"Carla Dias;103;7.5\"    ' acrescenta sem apagar",
                "Close #n",
            ]}),
            ("codigo", {"titulo": "Ler até o fim (EOF)", "ling": "vb", "linhas": [
                "Dim n As Integer, linha As String",
                "n = FreeFile",
                "Open \"c:\\lp2\\dados\\alunos.txt\" For Input As #n",
                "Do While Not EOF(n)",
                "    Line Input #n, linha",
                "    List1.AddItem linha",
                "Loop",
                "Close #n",
            ]}),
            ("tabela", {"titulo": "Modos de abertura",
                        "cab": ["Modo", "Efeito", "Quando usar"],
                        "lin": [["For Output", "cria/substitui o arquivo vazio", "gerar um arquivo novo"],
                                ["For Append", "abre e posiciona no final", "acrescentar sem perder"],
                                ["For Input", "somente leitura", "importar/consultar"]]}),
            ("conceito", ("EOF e FreeFile",
                          "<b>EOF(n)</b> = True quando a leitura chegou ao fim (fim do arquivo). "
                          "<b>FreeFile</b> devolve um número de arquivo livre — evita conflito quando vários "
                          "arquivos ficam abertos ao mesmo tempo. Par obrigatório: Open … Close.")),
            ("atencao", "Esquecer o <b>Close</b> = arquivo travado e dados perdidos no pior momento. "
                        "Esquecer que <b>Output apaga tudo</b> = tragédia de laboratório: para acrescentar, "
                        "use Append."),
        ], "slides": {"pontos": [
            "Ciclo: Open → Print #/Line Input # → Close (sempre!)",
            "Output substitui · Append acrescenta · Input só lê",
            "Do While Not EOF(n) percorre até o fim",
            "FreeFile evita conflito de números de arquivo",
        ], "codigo": {"titulo": "Leitura segura", "linhas": [
            "n = FreeFile",
            "Open arq For Input As #n",
            "Do While Not EOF(n)",
            "    Line Input #n, linha",
            "Loop",
            "Close #n",
        ]}, "nota": "Demonstre a tragédia didática: Output duas vezes seguidas (a 2ª apaga a 1ª) e depois a "
                   "solução com Append."}},
        {"num": 14, "titulo": "Arquivos + dados: importação/exportação controlada", "blocos": [
            ("h", "Do arquivo para o vetor de registros"),
            ("codigo", {"titulo": "Importar alunos.txt para a turma em memória", "ling": "vb", "linhas": [
                "Public Sub ImportarTurma(caminho As String)",
                "    Dim n As Integer, linha As String",
                "    Dim partes() As String",
                "    qt = 0",
                "    n = FreeFile",
                "    Open caminho For Input As #n",
                "    Do While Not EOF(n)",
                "        Line Input #n, linha",
                "        partes = Split(linha, \";\")          ' nome;matricula;nota",
                "        qt = qt + 1",
                "        turma(qt).nome = partes(0)",
                "        turma(qt).matricula = Val(partes(1))",
                "        turma(qt).nota = Val(partes(2))",
                "    Loop",
                "    Close #n",
                "End Sub",
            ]}),
            ("codigo", {"titulo": "Exportar (gravar) a turma de volta", "ling": "vb", "linhas": [
                "Public Sub ExportarTurma(caminho As String)",
                "    Dim n As Integer, i As Integer",
                "    n = FreeFile",
                "    Open caminho For Output As #n",
                "    For i = 1 To qt",
                "        Print #n, turma(i).nome & \";\" & turma(i).matricula & _",
                "                  \";\" & Format(turma(i).nota, \"0.0\")",
                "    Next i",
                "    Close #n",
                "End Sub",
            ]}),
            ("h", "Fluxo controlado de importação/exportação"),
            ("lista_num", [
                "Validar existência do arquivo antes de abrir (Dir(caminho) <> \"\");",
                "Abrir em Input e ler linha a linha com Split no separador combinado (;);",
                "Validar cada linha (qt de partes, tipos com Val/IsNumeric) antes de popular o vetor;",
                "Linhas inválidas: contar e reportar ao final (não travar nelas);",
                "Exportar com Format para manter padronização de números/datas.",
            ]),
            ("analogia", ("Arquivo = fila de caixas etiquetadas",
                          "Cada linha é uma caixa; o separador ; é a etiqueta interna que diz o que há dentro. "
                          "Importar é abrir caixas uma a uma e conferir o conteúdo; exportar é montar caixas "
                          "padronizadas e fechar o caminhão (Close).")),
        ], "slides": {"pontos": [
            "Split(linha, \";\") quebra a linha em campos",
            "Importar: validar linha a linha antes de popular o vetor",
            "Exportar: Format nos números para padronizar",
            "Dir(caminho) <> \"\" verifica existência antes de abrir",
            "Linhas inválidas: conte e reporte, não trave",
        ], "codigo": {"titulo": "Importação com Split", "linhas": [
            "partes = Split(linha, \";\")",
            "turma(qt).nome = partes(0)",
            "turma(qt).nota = Val(partes(2))",
        ]}, "nota": "Estudo de caso: forneça um alunos.txt com 2 linhas corrompidas e peça o relatório de "
                   "importação (importadas × recusadas)."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Diário de classe em arquivo", "tipo": "pratico",
         "enunciado": "Grave com Append as chamadas diárias (data;matricula;presença) em diario.txt; crie "
                      "botão que liste todo o arquivo em um ListBox usando EOF.",
         "esperado": "Arquivo crescendo a cada clique (Append) e listagem completa correta.",
         "orientacao": "Conferir se usaram Append (Output apagaria o histórico) e Close em ambos."},
        {"num": 2, "titulo": "Importação com validação", "tipo": "pratico",
         "enunciado": "Importe alunos.txt (nome;matricula;nota) para o vetor turma com validação por linha "
                      "(3 partes, nota numérica); ao final mostre: importadas, recusadas e média dos "
                      "importados.",
         "esperado": "Relatório de importação correto mesmo com linhas corrompidas no arquivo de teste.",
         "orientacao": "Forneça o arquivo com armadilhas; valorize o relatório de recusadas com motivo."},
        {"num": 3, "titulo": "Export → Import round-trip", "tipo": "escrito",
         "enunciado": "Explique por que exportar com Format(nota, \"0.0\") e importar com Val mantém o "
                      "round-trip íntegro; o que aconteceria sem o Format em notas como 8.25?",
         "esperado": "Explicação: Format padroniza casas e separador; sem ele, saídas como 8,250000 poluiriam "
                     "o arquivo; Val leria só o ‘8’ antes da vírgula em alguns cenários.",
         "orientacao": "Discussão curta que ancora a importância de padronização de dados em trânsito."},
    ],
    "teste_rapido": [
        {"enunciado": "Para ACRESCENTAR linhas sem apagar o conteúdo existente, abre-se com:",
         "alt": ["For Output", "For Input", "For Append", "For Random"],
         "resposta": 2, "comentario": "Append posiciona no fim; Output recria vazio."},
        {"enunciado": "EOF(n) retorna True quando:",
         "alt": ["o arquivo foi aberto", "a leitura chegou ao fim do arquivo", "houve erro de disco",
                 "o arquivo está vazio de linhas válidas"],
         "resposta": 1, "comentario": "Fim de arquivo — condição de parada do Do While."},
        {"enunciado": "FreeFile serve para:",
         "alt": ["liberar memória", "obter um número de arquivo livre", "apagar o arquivo",
                 "fechar todos os arquivos"],
         "resposta": 1, "comentario": "Evita conflito de #n com outros arquivos abertos."},
        {"enunciado": "Split(linha, \";\") devolve:",
         "alt": ["um texto único", "um vetor com os campos separados por ;", "o primeiro campo apenas",
                 "um registro Type"],
         "resposta": 1, "comentario": "Array de partes: partes(0), partes(1)..."},
        {"enunciado": "Esquecer o Close após gravação pode causar:",
         "alt": ["nada, o VB6 fecha sozinho sempre", "perda de dados e arquivo travado",
                 "conversão errada de tipos", "erro de sintaxe"],
         "resposta": 1, "comentario": "Buffer não descarregado/arquivo bloqueado — feche sempre."},
    ],
    "avaliacao_ref": None,
}

MODULOS = [M5, M6, M7, M8, M9, M10]
