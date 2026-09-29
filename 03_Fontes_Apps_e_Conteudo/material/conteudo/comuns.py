# -*- coding: utf-8 -*-
"""
Conteúdo compartilhado: informações do curso, esquema dos dados e textos de abertura.

ESQUEMA DE CADA MÓDULO (dict):
{
  "num": int,                      # número do módulo (1..12)
  "titulo": str,                   # título do módulo
  "parte_num": int,                # parte (I..VI -> 1..6)
  "parte_titulo": str,             # título da parte
  "aulas_faixa": str,              # ex.: "Aulas 1 a 4"
  "semanas": str,                  # ex.: "Semanas 1 e 2"
  "objetivos": [str, ...],         # objetivos de aprendizagem
  "aulas": [                       # teoria organizada por aula
    {
      "num": int,                  # número da aula no cronograma
      "titulo": str,
      "blocos": [                  # blocos de conteúdo (tuplas)
        ("p", "texto"),                                # parágrafo
        ("h", "subtítulo"),                            # subtítulo dentro da aula
        ("lista", ["item", ...]),                      # lista com marcadores
        ("lista_num", ["item", ...]),                  # lista numerada
        ("conceito", ("Título", "texto")),             # caixa conceito-chave
        ("analogia", ("Título", "texto")),             # caixa analogia
        ("dica", "texto"),                             # caixa dica
        ("atencao", "texto"),                          # caixa atenção
        ("codigo", {"titulo": str, "ling": str, "linhas": [str,...]}),
        ("tabela", {"titulo": str, "cab": [str,...], "lin": [[str,...]], "larguras": [float,...] (opcional)}),
      ],
      "slides": {                  # versão condensada para o PowerPoint
        "pontos": [str, ...],      # bullets do slide de teoria
        "codigo": {"titulo":..., "linhas":[...]},   # opcional — slide de código
        "extra": [str, ...],       # opcional — bullets de um 2º slide
        "nota": str,               # opcional — nota do apresentador
      },
    },
  ],
  "exercicios": [
    {
      "num": int, "titulo": str,
      "tipo": "pratico" | "escrito" | "grupo",
      "enunciado": str,
      "passos": [str, ...],               # opcional
      "codigo": {...},                    # opcional (código inicial/esqueleto)
      "esperado": str,                    # resultado esperado (gabarito professor)
      "orientacao": str,                  # orientação de correção (gabarito professor)
    },
  ],
  "teste_rapido": [
    {"enunciado": str, "alt": [str x4], "resposta": int (0-3), "comentario": str},
  ],
  "avaliacao_ref": str | None,     # ex.: "A1", "A2", "A3" — remete à seção de avaliações
}
"""

# ---------------------------------------------------------------------------
# INFORMAÇÕES DO CURSO (extraídas do Cronograma oficial — Turma 2/2026)
# ---------------------------------------------------------------------------
CURSO = {
    "disciplina": "Programação para Internet I",
    "curso": "Curso Técnico em Informática",
    "eixo": "Eixo Tecnológico: Informação e Comunicação",
    "turma": "Turma 2 / 2026",
    "ch_presencial": "60 h presenciais (aulas teóricas e práticas)",
    "ch_nao_presencial": "10 h não presenciais (atividades orientadas no AVA)",
    "aulas": "72 aulas · 24 semanas · 3 aulas semanais (períodos de 50 min)",
    "docente": "Docente responsável: ____________________________",
}

EMENTA = (
    "Desenvolvimento de projetos de website. Princípios de aplicações Web e hospedagem: "
    "portais, e-business, e-commerce, provedores, registro de domínio e acesso gratuito. "
    "Softwares e ferramentas adotados no desenvolvimento de aplicações web. Fundamentos de "
    "HTML e principais componentes de um documento HTML (BODY, HEAD, cabeçalhos, separadores). "
    "Formatação de textos, blocos e parágrafos. Listas ordenadas e numeradas. Tabelas. "
    "Linguagem PHP: configuração e uso. Utilização de ferramentas de desenvolvimento de "
    "soluções Web."
)

# Partes do semestre (faixas do cronograma oficial)
PARTES = [
    {"num": 1, "titulo": "Fundamentos da Internet e da Web", "aulas": "Aulas 1 a 4", "semanas": "Semanas 1 e 2",
     "modulos": [1]},
    {"num": 2, "titulo": "Ferramentas para Desenvolvimento Web (HTML)", "aulas": "Aulas 5 a 18", "semanas": "Semanas 2 a 6",
     "modulos": [2, 3, 4, 5]},
    {"num": 3, "titulo": "Introdução ao PHP", "aulas": "Aulas 19 a 36", "semanas": "Semanas 7 a 12",
     "modulos": [6, 7, 8, 9]},
    {"num": 4, "titulo": "Formulários + PHP", "aulas": "Aulas 37 a 42", "semanas": "Semanas 13 e 14",
     "modulos": [11]},
    {"num": 5, "titulo": "Organização e Desenvolvimento do Projeto", "aulas": "Aulas 43 a 48", "semanas": "Semanas 15 e 16",
     "modulos": [10]},
    {"num": 6, "titulo": "Desenvolvimento do Projeto Final", "aulas": "Aulas 49 a 72", "semanas": "Semanas 17 a 24",
     "modulos": [12]},
]

# Mapa de módulos (tabela do cronograma oficial)
MAPA_MODULOS = [
    ("1", "Introdução à Web", "Internet, Web, sites, aplicações Web, cliente/servidor, navegador, servidor, domínio, hospedagem", "1–4", "1–2"),
    ("2", "Ferramentas de desenvolvimento", "Editor de código, navegador, estrutura de projetos, arquivos e pastas", "5", "2"),
    ("3", "HTML – fundamentos", "Estrutura do documento, html, head, body, títulos, parágrafos, quebras, comentários", "6–9", "2–3"),
    ("4", "HTML – conteúdo", "Textos, formatação, links, imagens, listas e organização da informação", "10–12", "4"),
    ("5", "HTML – tabelas e formulários", "Tabelas, campos, input, select, textarea, button, formulários", "13–18", "5–6"),
    ("6", "Introdução ao PHP", "O que é PHP, servidor, instalação/configuração, primeiro programa", "19–21", "7"),
    ("7", "PHP básico", "Variáveis, constantes, tipos de dados, operadores e expressões", "22–26", "8–9"),
    ("8", "PHP – lógica", "if, else, elseif, switch, operadores lógicos", "27–29", "9–10"),
    ("9", "PHP – repetição", "for, while, do while, foreach (com arrays)", "30–35", "10–12"),
    ("10", "PHP + HTML", "Mistura de HTML e PHP, geração dinâmica de páginas; organização, include e funções", "36 e 43–48", "12 e 15–16"),
    ("11", "Formulários + PHP", "Recebimento e processamento de dados enviados pelo usuário", "37–42", "13–14"),
    ("12", "Projeto final", "Desenvolvimento, testes, correções, organização e apresentação", "49–72", "17–24"),
]

AVALIACOES_RESUMO = [
    ("1ª Avaliação", "30 pts", "Semanas 1 a 8",
     "Trabalho prático de HTML “site da empresa fictícia” (10 pts — entrega na semana 6) + "
     "atividades extraclasse/AVA e exercícios (5 pts — semanas 1 a 8) + teste escrito-prático "
     "sobre Web e HTML (15 pts — semana 8)."),
    ("2ª Avaliação", "30 pts", "Semana 16 (aula 48)",
     "Prova (obrigatoriamente; pode ser em duplas ou com consulta) contemplando HTML (estrutura "
     "a formulários), PHP (variáveis a arrays/funções) e GET/POST/validação."),
    ("3ª Avaliação", "40 pts", "Semana 24",
     "Prova escrita final individual e cumulativa (30 pts — aulas 70–71) + projeto integrador: "
     "entregas parciais e apresentação final (10 pts — aula 72)."),
]

METODOLOGIA = [
    "Exposição dialogada de conceitos, exemplos e atividades em sala.",
    "Aula invertida: estudo prévio em casa (bibliografia indicada) e aplicação em sala.",
    "Exercícios individuais e em grupo em cada tópico, com aplicação prática.",
    "Estudos de caso para análise crítica.",
    "Atividades extraclasse orientadas pelo Portal Acadêmico (AVA) — 10 h não presenciais.",
]

RECURSOS = [
    "Laboratório de informática e aulas presenciais.",
    "Recursos audiovisuais (projetor) e quadro branco.",
    "Portal Acadêmico (AVA): tarefas, fóruns e questionários.",
    "Google Drive, formulários e e-mail.",
    "Biblioteca virtual e WhatsApp (comunicação).",
]

ATIVIDADES_EXTRACLASSE = [
    ("Fase 1 — Web e HTML", "Semanas 1 a 6", "2,5 h",
     "Quizzes e leituras no AVA, tarefa “Meu curso” (aula 6), continuidade do projeto "
     "“Meu Primeiro Site” e finalização do site da empresa fictícia."),
    ("Fase 2 — PHP", "Semanas 7 a 12", "2,5 h",
     "Aula invertida (vídeos/leituras + questionários), listas de exercícios de lógica e "
     "repetição, preparação da revisão cumulativa."),
    ("Fase 3 — Formulários + PHP e organização", "Semanas 13 a 16", "2,0 h",
     "Exercícios de GET/POST/validação, leitura sobre funções e include, estudo dirigido "
     "para a 2ª avaliação."),
    ("Fase 4 — Projeto final", "Semanas 17 a 24", "3,0 h",
     "Desenvolvimento do projeto fora da aula, elaboração das entregas parciais, exercícios "
     "cumulativos de revisão e preparação da apresentação."),
]

BIBLIOGRAFIA_BASICA = [
    "ALVES, William Pereira. Desenvolvimento e design de sites. São Paulo: Erica, 2014.",
    "ALVES, William Pereira. Linguagem e lógica de programação. São Paulo: Erica, 2014.",
    "LAUREANO, Marcos Aurelio Pchek; CORDELLI, Rosa Lantmann. Fundamentos de software. São Paulo: Erica, 2019.",
]

BIBLIOGRAFIA_COMPLEMENTAR = [
    "ALVES, William Pereira. Projetos de sistemas Web. São Paulo: Erica, 2019.",
    "ALMEIDA, Rodrigo Maximiano A. de. Programação de sistemas embarcados. Rio de Janeiro: GEN LTC, 2016.",
    "MACIEL, Francisco Marcelo de Barros. Python e Django. Rio de Janeiro: Alta Books, 2020.",
    "SOUZA, Diogo B. da Costa (Org.). Sistemas digitais. Porto Alegre: SER - SAGAH, 2018.",
    "STAIR, Ralph M.; REYNOLDS, George W. Princípios de sistemas de informação. São Paulo: Cengage Learning, 2016.",
]

# ---------------------------------------------------------------------------
# TEXTOS DE ABERTURA DA APOSTILA
# ---------------------------------------------------------------------------
APRESENTACAO = [
    ("p", "Esta apostila foi elaborada a partir do <b>Plano de Ensino e do Cronograma oficiais</b> da disciplina "
          "<b>Programação para Internet I</b> do Curso Técnico em Informática (Turma 2/2026). Ela reúne, em um único "
          "material, a <b>teoria</b> de cada aula, <b>exercícios práticos</b>, <b>testes rápidos</b> de verificação da "
          "aprendizagem e as <b>avaliações</b> do semestre (A1, A2 e A3), além do roteiro completo do "
          "<b>projeto final integrador</b>."),
    ("p", "O material segue exatamente a sequência das <b>72 aulas em 24 semanas</b> (3 aulas semanais de 50 minutos), "
          "organizadas em <b>6 partes</b> e <b>12 módulos</b>. Cada módulo contém:"),
    ("lista", [
        "<b>Objetivos de aprendizagem</b> — o que você deve saber fazer ao final do módulo;",
        "<b>Teoria aula a aula</b> — explicações, exemplos, tabelas e blocos de código comentados;",
        "<b>Exercícios práticos</b> — atividades de laboratório e questões escritas para fixação;",
        "<b>Teste rápido</b> — 5 questões objetivas para você conferir o que aprendeu;",
        "<b>Indicação de avaliação</b> — quando o módulo termina em avaliação ou entrega (A1, A2, A3 ou projeto final).",
    ]),
    ("conceito", ("Como estudar com esta apostila (aula invertida)",
                  "Antes da aula, leia a teoria indicada e tente resolver os primeiros exercícios; em sala, "
                  "participe das atividades práticas e tire dúvidas; depois da aula, refaça o teste rápido e "
                  "registre suas dúvidas no AVA. Estudar programação é como aprender a andar de bicicleta: "
                  "não basta ler — é preciso praticar digitando o código e observando o resultado.")),
    ("dica", "Itens marcados com <b>(S)</b> são <b>propostas pedagógicas</b> de organização (datas de avaliações, "
             "entregas e distribuição das horas não presenciais) — não estão especificados no Plano de Ensino "
             "original. Demais informações reproduzem o Plano de Ensino oficial."),
]

COMO_USAR_ICONES = [
    ("tabela", {"titulo": "Ícones e caixas usadas neste material",
                "cab": ["Caixa", "O que significa", "Quando usar"],
                "lin": [
                    ["Conceito-chave", "Definição importante que provavelmente cairá nas avaliações.", "Leia e memorize; anote no caderno."],
                    ["Analogia", "Comparação com situações do cotidiano para facilitar o entendimento.", "Use para explicar o conceito com suas palavras."],
                    ["Dica", "Sugestão prática, atalho ou boa prática de quem programa.", "Aplique nos exercícios."],
                    ["Atenção", "Erro comum ou ponto em que a maioria dos estudantes tropeça.", "Leia com cuidado antes dos exercícios."],
                    ["Código", "Exemplo de código HTML/PHP comentado.", "Digite no editor e execute — nunca apenas leia!"],
                    ["Exercícios", "Atividades práticas e escritas do módulo.", "Resolva em sala e complete em casa (AVA)."],
                    ["Teste rápido", "5 questões objetivas de verificação.", "Responda sem consultar; depois corrija."],
                ],
                "larguras": [3.2, 8.3, 5.5]}),
]


META = {
    "slug": "Programacao_para_Internet_I",
    "kicker": "CURSO TÉCNICO EM INFORMÁTICA · EIXO: INFORMAÇÃO E COMUNICAÇÃO",
    "titulo_capa": "PROGRAMAÇÃO<br/>PARA INTERNET I",
    "sub_capa": "Apostila completa da disciplina — teoria aula a aula, exercícios "
                "práticos, testes rápidos e avaliações (A1 · A2 · A3)",
    "header": "PROGRAMAÇÃO PARA INTERNET I — APOSTILA COMPLETA",
    "rodape": "(S) = proposta pedagógica",
    "fecho": "Programação para Internet I · Curso Técnico em Informática · Turma 2/2026 — "
             "material elaborado a partir do Plano de Ensino e do Cronograma oficiais. "
             "Itens marcados com (S) são propostas pedagógicas de organização.",
    "titulo_doc": "Programação para Internet I",
    "aula_label": "Aula",
}
ORDEM_PARTES = {1: [1], 2: [2, 3, 4, 5], 3: [6, 7, 8, 9], 4: [11], 5: [10], 6: [12]}
NOTAS_PARTES = {
    3: "Observação: a aula 36 (revisão cumulativa + projeto PHP), ministrada na semana 12, "
       "pertence ao Módulo 10 — seu conteúdo completo está na Parte V.",
    5: "O Módulo 10 inclui a aula 36 (revisão cumulativa), ministrada na semana 12, ao final "
       "da Parte III — conforme a tabela oficial de módulos do cronograma.",
}

META.update({
    "pptx_footer": "PROGRAMAÇÃO PARA INTERNET I · CURSO TÉCNICO EM INFORMÁTICA · TURMA 2/2026",
    "pptx_capa1": "PROGRAMAÇÃO",
    "pptx_capa2": "PARA INTERNET I",
    "pptx_sub": "Apresentação de aulas — teoria, exercícios práticos, testes rápidos "
                "e avaliações (A1 · A2 · A3)",
    "pptx_rodape": "Material baseado no Plano de Ensino e no Cronograma oficiais · Turma 2/2026",
    "pptx_encerra1": "Programação para Internet I · Curso Técnico em Informática · Turma 2/2026",
    "pptx_encerra2": "Apostila (aluno e professor), testes rápidos e modelos de prova: "
                     "disponíveis no material da disciplina.",
})

FRONT = [
    {"kick": "Bem-vindos à disciplina", "tit": "O curso em 1 minuto",
     "bullets": ["Programação para Internet I — Curso Técnico em Informática (Turma 2/2026)",
                 "72 aulas em 24 semanas · 3 aulas semanais de 50 minutos",
                 "60 h presenciais (teoria + prática) e 10 h de atividades orientadas no AVA",
                 "Do zero ao projeto final: Web → HTML → PHP → formulários → sistema completo",
                 "Aulas dialogadas, muita prática no laboratório e projeto integrador em grupos"],
     "sub": "Ementa oficial: desenvolvimento de projetos de website, HTML e linguagem PHP."},
    {"kick": "Como funcionam as aulas", "tit": "Teoria + prática + testes rápidos",
     "bullets": ["Teoria aula a aula: conceitos com exemplos, analogias e código ao vivo",
                 "Exercícios práticos em cada módulo (laboratório) e questões escritas",
                 "Teste rápido ao final de cada módulo: 5 questões para fixar na hora",
                 "Atividades no AVA (10 h): quizzes, leituras e continuidade dos projetos",
                 "Projetos: “Meu Primeiro Site” → site da empresa (A1) → cadastro PHP → projeto final"]},
    {"kick": "Avaliações — 100 pontos", "tit": "A1 · A2 · A3",
     "bullets": ["A1 (30 pts): site da empresa fictícia (10) + AVA/exercícios (5) + teste Web/HTML (15)",
                 "A2 (30 pts): prova na semana 16 — HTML, PHP e GET/POST (duplas/consulta conforme o Plano)",
                 "A3 (40 pts): prova final individual (30) + projeto e apresentação (10)",
                 "Apoio contínuo: revisões nas aulas 36 e 60, reforço no AVA e entregas do projeto",
                 "Modelos de prova e rubricas: seção AVALIAÇÕES da apostila"]},
    {"kick": "Mapa do semestre", "tit": "Seis partes, doze módulos",
     "bullets": ["Parte I — Fundamentos da Internet e da Web (Aulas 1 a 4, Semanas 1 e 2)",
                 "Parte II — Ferramentas para Desenvolvimento Web (HTML) (Aulas 5 a 18, Semanas 2 a 6)",
                 "Parte III — Introdução ao PHP (Aulas 19 a 36, Semanas 7 a 12)",
                 "Parte IV — Formulários + PHP (Aulas 37 a 42, Semanas 13 e 14)",
                 "Parte V — Organização e Desenvolvimento do Projeto (Aulas 43 a 48, Semanas 15 e 16)",
                 "Parte VI — Desenvolvimento do Projeto Final (Aulas 49 a 72, Semanas 17 a 24)"],
     "sub": "Cada parte abre um bloco de slides; os módulos trazem teoria, exercícios e teste rápido."},
]
