# -*- coding: utf-8 -*-
"""Conteúdo compartilhado — Linguagem de Programação II (Turma 2/2026).
Base documental: Plano de Ensino + Cronograma oficial (96 aulas · 24 semanas · 4 aulas/semana).
Escolha de ambiente documentada (S): Visual Basic 6.0 + MySQL (ODBC/ADO)."""

CURSO = {
    "disciplina": "Linguagem de Programação II",
    "curso": "Curso Técnico em Informática",
    "eixo": "Eixo Tecnológico: Informação e Comunicação",
    "turma": "Turma 2 / 2026",
    "ch_presencial": "80 h presenciais (aulas teóricas e práticas)",
    "ch_nao_presencial": "14 h não presenciais (atividades orientadas no AVA)",
    "aulas": "96 aulas · 24 semanas · 4 aulas semanais (períodos de 50 min)",
    "docente": "Docente responsável: ____________________________",
    "instituicao": "Fundação Presidente Antônio Carlos — Centro Técnico Profissional",
}

EMENTA = (
    "Instalação e configuração dos requisitos de SGBD para a Linguagem; Conexão com Banco de "
    "Dados; Programação de instruções SQL; Programação gráfica em ambiente DOS; Criação de "
    "programas usando linguagem de programação estruturada; Arquivos e textos como forma de "
    "transferência de dados; Manipulação de Dados Cliente/Servidor; Backup e Recuperação de "
    "Banco de Dados; Geração de Relatórios; Impressão e Geração de Documentos Fiscais; Criação "
    "do Disco de Instalação do Programa; Estruturação de dados com vetor, Matriz e registro; "
    "Técnicas de modularização de programas; Variáveis do tipo String; Recursos gráficos."
)

AMBIENTE = (
    "Escolha pedagógica documentada (S): linguagem <b>Visual Basic 6.0</b> (IDE VB6) como "
    "linguagem de programação estruturada da ementa — vetores/matrizes/registros (arrays e "
    "Type), Strings, modularização (Modules com Sub/Function), arquivos (Open/Print#/Input#), "
    "relatórios e impressão (objeto Printer), recursos gráficos (PictureBox) e disco de "
    "instalação (Package & Deployment Wizard); SGBD <b>MySQL</b> acessado por <b>ODBC/ADO</b> "
    "para conexão, SQL, manipulação cliente/servidor, backup e recuperação. Plano B documentado "
    "para laboratórios sem servidor: Access (arquivo .mdb) com os mesmos conceitos."
)

PARTES = [
    {"num": 1, "titulo": "Ambiente, SGBD e Conexão", "aulas": "Aulas 1 a 12", "semanas": "Semanas 1 a 3",
     "modulos": [1, 2]},
    {"num": 2, "titulo": "Linguagem SQL", "aulas": "Aulas 13 a 24", "semanas": "Semanas 4 a 6",
     "modulos": [3, 4]},
    {"num": 3, "titulo": "Programação Estruturada e Estruturas de Dados", "aulas": "Aulas 25 a 40",
     "semanas": "Semanas 7 a 10", "modulos": [5, 6, 7]},
    {"num": 4, "titulo": "Strings, Modularização e Arquivos", "aulas": "Aulas 41 a 56",
     "semanas": "Semanas 11 a 14", "modulos": [8, 9, 10]},
    {"num": 5, "titulo": "Dados Cliente/Servidor e Administração do Banco", "aulas": "Aulas 57 a 72",
     "semanas": "Semanas 15 a 18", "modulos": [11, 12]},
    {"num": 6, "titulo": "Saídas, Distribuição, Gráficos e Projeto Integrador", "aulas": "Aulas 73 a 96",
     "semanas": "Semanas 19 a 24", "modulos": [13, 14, 15]},
]

MAPA_MODULOS = [
    ("1", "Ambientação e linguagem estruturada", "Apresentação da disciplina; programação estruturada; arquitetura do projeto; organização do ambiente", "1–4", "1"),
    ("2", "SGBD: instalação e conexão", "Requisitos do SGBD; instalação; configuração; conexão; parâmetros; tratamento de falhas", "5–12", "2–3"),
    ("3", "SQL: fundamentos e manipulação", "Instruções SQL; criação/consulta; INSERT, UPDATE, DELETE; integração ao programa", "13–20", "4–5"),
    ("4", "SQL: consultas e filtros", "SELECT com WHERE, ORDER BY, agrupamentos; organização de consultas; cenários de dados", "21–24", "6"),
    ("5", "Programação estruturada", "Sequência, seleção (If/Select Case) e repetição (For/Do/While); organização lógica", "25–28", "7"),
    ("6", "Vetores e matrizes", "Declaração, preenchimento, leitura e processamento de arrays uni e bidimensionais", "29–36", "8–9"),
    ("7", "Registros", "Type/End Type; agrupamento de informações relacionadas; uso no programa", "37–40", "10"),
    ("8", "Strings", "Variáveis String; armazenamento, leitura e manipulação de textos (Len, Mid, UCase, Trim…)", "41–44", "11"),
    ("9", "Modularização", "Sub, Function, parâmetros, retorno; Modules; reutilização e organização", "45–48", "12"),
    ("10", "Arquivos e textos", "Leitura/gravação de arquivos; For Output/Input/Append; integração com dados do programa", "49–56", "13–14"),
    ("11", "Manipulação de dados Cliente/Servidor", "ADO/ODBC; Recordset; fluxo aplicação × banco; validação e tratamento de problemas", "57–64", "15–16"),
    ("12", "Backup e recuperação", "Procedimentos de cópia (mysqldump); restauração; validação após recuperação", "65–72", "17–18"),
    ("13", "Relatórios e documentos fiscais", "Geração de relatórios; seleção e organização de dados; objeto Printer; documentos fiscais", "73–80", "19–20"),
    ("14", "Disco de instalação e gráficos", "Package & Deployment Wizard; recursos gráficos (PictureBox; herança DOS)", "81–88", "21–22"),
    ("15", "Projeto integrador e consolidação", "Integração geral; revisão; apresentação do projeto; avaliação final", "89–96", "23–24"),
]

METODOLOGIA = [
    "Exposição de conceitos, exemplos e atividades em sala (aulas dialogadas).",
    "Aula invertida: estudo prévio em casa (bibliografia indicada) e aplicação em sala.",
    "Exercícios individuais e em grupo em cada tópico, com aplicação prática.",
    "Estudos de caso para análise crítica (cenários reais de dados e sistemas).",
    "Laboratórios práticos ao longo de todos os tópicos.",
    "Projeto integrador nas semanas 23–24 consolidando os conteúdos.",
]

RECURSOS = [
    "Laboratório de informática com Windows e Visual Basic 6.0 instalado.",
    "Servidor MySQL (ou plano B: Access) nas máquinas do laboratório.",
    "Recursos audiovisuais (projetor) e quadro branco.",
    "Portal Acadêmico (AVA): tarefas, fóruns e questionários.",
    "Google Drive, formulários e e-mail.",
    "Biblioteca virtual e WhatsApp (comunicação).",
]

ATIVIDADES_EXTRACLASSE = [
    ("Semanas 2–4", "2 h", "Preparação do ambiente e estudo orientado sobre SGBD e conexão."),
    ("Semanas 7–10", "3 h", "Exercícios de programação estruturada, vetor, matriz e registro."),
    ("Semanas 11–14", "3 h", "Atividades sobre String, modularização e arquivos/textos."),
    ("Semanas 15–18", "2 h", "Estudo orientado sobre Cliente/Servidor, backup e recuperação."),
    ("Semanas 19–22", "2 h", "Preparação de relatórios, documentos e instalação."),
    ("Semanas 23–24", "2 h", "Consolidação e preparação do projeto/avaliação final."),
]

AVALIACOES_RESUMO = [
    ("1ª Avaliação", "30 pts", "Semanas 1 a 8",
     "Lista prática de SQL + estruturas (10 pts — entrega semana 6) + atividades AVA (5 pts) + "
     "teste escrito-prático de SGBD/SQL/estruturas (15 pts — semana 8). (S)"),
    ("2ª Avaliação", "30 pts", "Semana 16",
     "Prova obrigatória (pode ser em duplas ou com consulta — Plano de Ensino): Strings, "
     "modularização, arquivos e Cliente/Servidor."),
    ("3ª Avaliação", "40 pts", "Semana 24",
     "Prova escrita final individual e cumulativa (30 pts) + projeto integrador e apresentação "
     "(10 pts — critério do professor)."),
]

BIBLIOGRAFIA_BASICA = [
    "ALVES, William Pereira. Linguagem e lógica de programação. São Paulo: Erica, 2014.",
    "CARDOSO, Vírginia M. Linguagem SQL. São Paulo: Saraiva, 2009.",
    "MILANI, Alessandra M. P. G. et al. Consultas em bancos de dados. Porto Alegre: SAGAH, 2021.",
]

BIBLIOGRAFIA_COMPLEMENTAR = [
    "ALVES, William Pereira. Projetos de sistemas Web. São Paulo: Erica, 2019.",
    "GONÇALVEZ, Priscila de Fátima (Org.). Testes de software e gerência de configuração. Porto Alegre: SAGAH, 2019.",
    "JOSÉ, Marcel Fialho; REIS, Bruna de Souza. Projetos gráficos. São Paulo: Erica, 2015.",
    "LEDUR, Cleverson Lopes. Desenvolvimento de sistemas com C. Porto Alegre: SAGAH, 2018.",
    "MARTINS, Juliano V. S. et al. Raciocínio algorítmico. Porto Alegre: SAGAH, 2020.",
    "SIEBEL, Thomas M. Transformação digital. Rio de Janeiro: Alta Books, 2021.",
    "VELLOSO, Fernando de Castro. Informática. Rio de Janeiro: GEN LTC, 2017.",
]

META = {
    "slug": "Linguagem_de_Programacao_II",
    "kicker": "CURSO TÉCNICO EM INFORMÁTICA · EIXO: INFORMAÇÃO E COMUNICAÇÃO · FUPAC/CENTRO TÉCNICO",
    "titulo_capa": "LINGUAGEM DE<br/>PROGRAMAÇÃO II",
    "sub_capa": "Apostila completa da disciplina — teoria por semana (4 etapas), exercícios "
                "práticos, testes rápidos e avaliações (A1 · A2 · A3) · VB6 + MySQL",
    "header": "LINGUAGEM DE PROGRAMAÇÃO II — APOSTILA COMPLETA",
    "rodape": "(S) = proposta pedagógica · ambiente: VB6 + MySQL",
    "fecho": "Linguagem de Programação II · Curso Técnico em Informática · Turma 2/2026 — "
             "material elaborado a partir do Plano de Ensino e do Cronograma oficiais "
             "(96 aulas · 24 semanas). Itens marcados com (S) são propostas pedagógicas.",
    "titulo_doc": "Linguagem de Programação II",
    "aula_label": "Semana",
    "pptx_footer": "LINGUAGEM DE PROGRAMAÇÃO II · CURSO TÉCNICO EM INFORMÁTICA · TURMA 2/2026",
    "pptx_capa1": "LINGUAGEM DE",
    "pptx_capa2": "PROGRAMAÇÃO II",
    "pptx_sub": "Apresentação de aulas — teoria, laboratórios, testes rápidos e avaliações "
                "(A1 · A2 · A3) · VB6 + MySQL",
    "pptx_rodape": "Material baseado no Plano de Ensino e no Cronograma oficiais · 96 aulas · Turma 2/2026",
    "pptx_encerra1": "Linguagem de Programação II · Curso Técnico em Informática · Turma 2/2026",
    "pptx_encerra2": "Apostila (aluno e professor), testes rápidos e modelos de prova: "
                     "disponíveis no material da disciplina.",
}

ORDEM_PARTES = {1: [1, 2], 2: [3, 4], 3: [5, 6, 7], 4: [8, 9, 10], 5: [11, 12], 6: [13, 14, 15]}
NOTAS_PARTES = {
    1: "As semanas 2–3 instalam e validam o ambiente (SGBD + conexão): é a base de todo o "
       "resto do semestre — não pule os laboratórios.",
    6: "A Parte VI reúne saídas (relatórios/impressão), distribuição (disco de instalação), "
       "gráficos e o projeto integrador das semanas 23–24.",
}

FRONT = [
    {"kick": "Bem-vindos à disciplina", "tit": "O curso em 1 minuto",
     "bullets": ["Linguagem de Programação II — Curso Técnico em Informática (Turma 2/2026)",
                 "96 aulas em 24 semanas · 4 aulas semanais de 50 minutos",
                 "80 h presenciais (teoria + prática) e 14 h de atividades orientadas no AVA",
                 "Ambiente do curso (S): Visual Basic 6.0 + MySQL (ODBC/ADO)",
                 "Do banco de dados ao programa completo: SQL → estruturas → arquivos → "
                 "cliente/servidor → relatórios → projeto integrador"],
     "sub": "Ementa oficial: SGBD, conexão, SQL, programação estruturada, vetor/matriz/registro, "
            "Strings, modularização, arquivos, cliente/servidor, backup, relatórios, impressão, "
            "disco de instalação e gráficos."},
    {"kick": "Como funcionam as aulas", "tit": "4 etapas por semana",
     "bullets": ["Etapa 1 — introdução e conceitos fundamentais (teoria dialogada)",
                 "Etapa 2 — exemplos orientados e demonstração no projetor",
                 "Etapa 3 — atividade prática individual/em grupo no laboratório",
                 "Etapa 4 — fixação e verificação da aprendizagem (teste rápido)",
                 "Cada semana vira um bloco do app AulaViva e um quiz no QuizWeb"],
     "sub": "É exatamente a estrutura oficial do cronograma: 96 aulas = 24 semanas × 4 etapas."},
    {"kick": "Avaliações — 100 pontos", "tit": "A1 · A2 · A3",
     "bullets": ["A1 (30 pts): lista prática SQL+estruturas (10) + AVA (5) + teste escrito-prático (15) — semana 8 (S)",
                 "A2 (30 pts): prova na semana 16 — Strings, modularização, arquivos, cliente/servidor (duplas/consulta conforme o Plano)",
                 "A3 (40 pts): prova final individual (30) + projeto integrador e apresentação (10)",
                 "Revisões estratégicas: semana 12 (modularização) e semana 24 (consolidação)",
                 "Modelos de prova e rubricas: seção AVALIAÇÕES da apostila"]},
    {"kick": "Mapa do semestre", "tit": "Seis partes, quinze módulos",
     "bullets": ["Parte I — Ambiente, SGBD e Conexão (semanas 1–3)",
                 "Parte II — Linguagem SQL (semanas 4–6)",
                 "Parte III — Programação Estruturada e Estruturas de Dados (semanas 7–10)",
                 "Parte IV — Strings, Modularização e Arquivos (semanas 11–14)",
                 "Parte V — Dados Cliente/Servidor e Administração do Banco (semanas 15–18)",
                 "Parte VI — Saídas, Distribuição, Gráficos e Projeto Integrador (semanas 19–24)"],
     "sub": "Cada parte abre um bloco de slides; os módulos trazem teoria, laboratórios e teste rápido."},
]


APRESENTACAO = [
    ("p", "Esta apostila foi elaborada a partir do <b>Plano de Ensino e do Cronograma oficiais</b> da "
          "disciplina <b>Linguagem de Programação II</b> (Curso Técnico em Informática, Turma 2/2026): "
          "<b>96 aulas em 24 semanas, 4 aulas semanais</b>. Ela reúne a teoria de cada semana nas "
          "<b>4 etapas oficiais</b> (conceitos → demonstração → prática → fixação), exercícios de "
          "laboratório, testes rápidos e os modelos das avaliações A1, A2 e A3."),
    ("p", "O ambiente de trabalho do curso (escolha documentada — S) é <b>Visual Basic 6.0</b> com o SGBD "
          "<b>MySQL</b> acessado por <b>ODBC/ADO</b>; o plano B para laboratórios sem servidor é o Access, "
          "com os mesmos conceitos. Todos os códigos de exemplo seguem esse ambiente."),
    ("lista", [
        "<b>Semanas 1–3</b>: ambiente, SGBD (instalação/configuração) e conexão;",
        "<b>Semanas 4–6</b>: linguagem SQL (fundamentos, manipulação e consultas);",
        "<b>Semanas 7–10</b>: programação estruturada, vetores, matrizes e registros;",
        "<b>Semanas 11–14</b>: Strings, modularização e arquivos/textos;",
        "<b>Semanas 15–18</b>: dados Cliente/Servidor (ADO), backup e recuperação;",
        "<b>Semanas 19–24</b>: relatórios, documentos fiscais, disco de instalação, gráficos e "
        "projeto integrador.",
    ]),
    ("conceito", ("Como estudar com esta apostila (aula invertida)",
                  "Antes da semana: leia a teoria e tente o primeiro exercício; em sala: laboratório em "
                  "duplas e correção dialogada; depois: teste rápido da semana e atividades do AVA. "
                  "Programação se aprende digitando: todo exemplo desta apostila deve ser executado, "
                  "quebrado e consertado por você.")),
    ("dica", "Itens marcados com <b>(S)</b> são <b>propostas pedagógicas</b> de organização (datas de "
             "avaliações, entregas, escolha de ambiente) — não especificadas no Plano de Ensino original. "
             "Demais informações reproduzem o Plano de Ensino e o Cronograma oficiais."),
]

COMO_USAR_ICONES = [
    ("tabela", {"titulo": "Ícones e caixas usadas neste material",
                "cab": ["Caixa", "O que significa", "Quando usar"],
                "lin": [
                    ["Conceito-chave", "Definição importante que provavelmente cairá nas avaliações.", "Leia e memorize; anote no caderno."],
                    ["Analogia", "Comparação com situações do cotidiano.", "Use para explicar com suas palavras."],
                    ["Dica", "Sugestão prática ou boa prática profissional.", "Aplique nos laboratórios."],
                    ["Atenção", "Erro comum ou ponto de risco (dados, laços, arquivos).", "Leia antes de executar."],
                    ["Código", "Exemplo VB6/SQL/shell comentado.", "Digite e execute — nunca apenas leia!"],
                    ["Exercícios", "Atividades práticas e escritas do módulo.", "Resolva em sala e complete no AVA."],
                    ["Teste rápido", "5 questões objetivas de verificação da semana/módulo.", "Responda sem consultar; depois corrija."],
                ],
                "larguras": [3.2, 8.3, 5.5]}),
]
