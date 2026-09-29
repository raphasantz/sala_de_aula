# -*- coding: utf-8 -*-
"""Módulos 3 a 5 — HTML: fundamentos, conteúdo, tabelas e formulários."""

MODULO_3 = {
    "num": 3,
    "titulo": "HTML – fundamentos",
    "parte_num": 2,
    "parte_titulo": "Ferramentas para Desenvolvimento Web (HTML)",
    "aulas_faixa": "Aulas 6 a 9",
    "semanas": "Semanas 2 e 3",
    "objetivos": [
        "Criar um documento HTML5 completo com DOCTYPE, head e body.",
        "Identificar elementos, tags, atributos e elementos sem fechamento.",
        "Usar cabeçalhos (h1–h6), parágrafos (p), quebras (br) e separadores (hr).",
        "Aplicar formatação semântica de textos (strong, em, mark, small).",
        "Diferenciar semântica de aparência (strong × b, em × i).",
    ],
    "aulas": [
        {
            "num": 6,
            "titulo": "Primeiro documento HTML",
            "blocos": [
                ("h", "O que é HTML?"),
                ("p", "<b>HTML</b> (<i>HyperText Markup Language</i> — Linguagem de Marcação de Hipertexto) é a "
                      "linguagem usada para <b>estruturar o conteúdo</b> de toda página Web: textos, imagens, "
                      "links, tabelas e formulários. HTML <b>não é linguagem de programação</b>: é uma linguagem "
                      "de <b>marcação</b> — ela apenas “marca” o conteúdo, indicando o que cada trecho é "
                      "(um título, um parágrafo, uma imagem...)."),
                ("conceito", ("Marcação × Programação",
                              "Uma <b>linguagem de marcação</b> (HTML) descreve a estrutura do conteúdo, sem "
                              "tomar decisões. Uma <b>linguagem de programação</b> (como PHP, que veremos na "
                              "Parte III) executa lógica: faz cálculos, toma decisões e repete ações. "
                              "Um site completo usa as duas juntas.")),
                ("h", "A estrutura básica do HTML5"),
                ("p", "Todo documento HTML5 segue a mesma “esqueleto”. Digite o exemplo no VS Code, salve como "
                      "<b>index.html</b> dentro de <b>meu-site/</b> e abra no navegador (clique duplo ou "
                      "arraste para a janela do navegador):"),
                ("codigo", {"titulo": "ola.html — o clássico “Olá, mundo!”", "ling": "html", "linhas": [
                    "<!DOCTYPE html>",
                    "<html lang=\"pt-br\">",
                    "<head>",
                    "    <meta charset=\"UTF-8\">",
                    "    <title>Minha primeira página</title>",
                    "</head>",
                    "<body>",
                    "    <h1>Olá, mundo!</h1>",
                    "    <p>Esta é a minha primeira página Web.</p>",
                    "</body>",
                    "</html>",
                ]}),
                ("tabela", {"titulo": "Para que serve cada parte",
                            "cab": ["Parte", "Função"],
                            "lin": [
                                ["&lt;!DOCTYPE html&gt;", "Declara que o documento usa HTML5 — deve ser a 1ª linha"],
                                ["&lt;html lang=\"pt-br\"&gt;", "Elemento raiz; lang informa o idioma da página"],
                                ["&lt;head&gt;", "Cabeça: configurações e metadados (não aparecem na página)"],
                                ["&lt;meta charset=\"UTF-8\"&gt;", "Define a codificação — permite acentos (ç, ã, é...)"],
                                ["&lt;title&gt;", "Título que aparece na aba do navegador e nos favoritos"],
                                ["&lt;body&gt;", "Corpo: todo o conteúdo visível da página"],
                            ]}),
                ("h", "head × body"),
                ("p", "O <b>head</b> guarda informações <b>sobre</b> a página (título da aba, codificação, "
                      "links para CSS — veremos depois). O <b>body</b> guarda o conteúdo <b>da</b> página "
                      "(tudo o que o usuário vê). Analogia: o head é a ficha catalográfica de um livro; o body "
                      "são as páginas com a história."),
                ("dica", "No VS Code, crie um arquivo <b>.html</b> vazio, digite <b>!</b> e pressione "
                         "<b>Tab</b>: o editor gera o esqueleto completo automaticamente (recurso Emmet). "
                         "Depois digite <b>Ctrl+Espaço</b> para ver sugestões de tags."),
                ("h", "Desafio “Sobre mim”"),
                ("p", "Como atividade da aula, crie a página <b>sobre.html</b> com um título <b>&lt;h1&gt;</b> "
                      "com seu nome e um parágrafo contando: seu nome completo, idade, cidade onde mora e por "
                      "que escolheu o curso de Informática. Salve e abra no navegador para conferir."),
            ],
            "slides": {
                "pontos": [
                    "HTML = linguagem de MARCAÇÃO (estrutura o conteúdo)",
                    "Marcação descreve; programação decide (PHP vem depois)",
                    "Esqueleto: DOCTYPE → html → head (configurações) → body (conteúdo)",
                    "meta charset=UTF-8 = acentos funcionando",
                    "title = aba do navegador; h1 = título na página",
                ],
                "codigo": {"titulo": "ola.html", "linhas": [
                    "<!DOCTYPE html>",
                    "<html lang=\"pt-br\">",
                    "<head>",
                    "  <meta charset=\"UTF-8\">",
                    "  <title>Minha primeira página</title>",
                    "</head>",
                    "<body>",
                    "  <h1>Olá, mundo!</h1>",
                    "  <p>Minha primeira página Web.</p>",
                    "</body>",
                    "</html>",
                ]},
                "nota": "Todos devem digitar o código (não copiar/colar!) e abrir no navegador. Desafio 'Sobre "
                        "mim' nos 15 minutos finais. Dica do Emmet: ! + Tab.",
            },
        },
        {
            "num": 7,
            "titulo": "Estrutura do HTML: elementos, tags e atributos",
            "blocos": [
                ("h", "Anatomia de um elemento"),
                ("p", "A unidade básica do HTML é o <b>elemento</b>, formado por <b>tag de abertura</b> + "
                      "<b>conteúdo</b> + <b>tag de fechamento</b>:"),
                ("codigo", {"titulo": "Anatomia de um elemento", "ling": "html", "linhas": [
                    "<p>Este texto é o conteúdo do elemento.</p>",
                    "│ │└────────── conteúdo ──────────┘│",
                    "│ └─ tag de abertura                └─ tag de fechamento (com /)",
                    "└─ o símbolo '<' inicia a tag",
                ]}),
                ("h", "Atributos"),
                ("p", "<b>Atributos</b> são configurações extras escritas <b>na tag de abertura</b>, no formato "
                      "<b>nome=\"valor\"</b>. Eles dão informações adicionais sobre o elemento:"),
                ("codigo", {"titulo": "Exemplos de atributos", "ling": "html", "linhas": [
                    "<html lang=\"pt-br\">        <!-- atributo lang: idioma da página -->",
                    "<meta charset=\"UTF-8\">      <!-- atributo charset: codificação -->",
                    "<a href=\"sobre.html\">     <!-- atributo href: destino do link -->",
                    "<img src=\"foto.jpg\" alt=\"Foto\">  <!-- src: arquivo; alt: descrição -->",
                ]}),
                ("h", "Elementos sem fechamento (vazios)"),
                ("p", "Alguns elementos <b>não têm conteúdo</b> entre tags e, por isso, <b>não usam tag de "
                      "fechamento</b>. São chamados de <b>elementos vazios</b>:"),
                ("lista", [
                    "<b>&lt;br&gt;</b> — quebra de linha;",
                    "<b>&lt;hr&gt;</b> — separador horizontal (linha);",
                    "<b>&lt;img&gt;</b> — imagem (o conteúdo está nos atributos src/alt);",
                    "<b>&lt;meta&gt;</b> — metadados (charset etc.);",
                    "<b>&lt;input&gt;</b> — campo de formulário (veremos no módulo 5).",
                ]),
                ("h", "Aninhamento correto"),
                ("p", "Elementos podem conter outros elementos (<b>aninhamento</b>), mas as tags devem fechar "
                      "<b>na ordem inversa</b> em que abriram — como caixas dentro de caixas:"),
                ("codigo", {"titulo": "Aninhamento: certo × errado", "ling": "html", "linhas": [
                    "<!-- CERTO: fecha na ordem inversa -->",
                    "<p>Texto com <strong>destaque</strong> interno.</p>",
                    "",
                    "<!-- ERRADO: tags cruzadas -->",
                    "<p>Texto com <strong>destaque</p></strong>",
                ]}),
                ("h", "Comentários"),
                ("p", "Comentários são anotações que <b>não aparecem</b> na página — servem para organizar e "
                      "documentar o código:"),
                ("codigo", {"titulo": "Comentário em HTML", "ling": "html", "linhas": [
                    "<!-- Isto é um comentário: o navegador ignora -->",
                    "<!-- Início do cabeçalho do site -->",
                ]}),
                ("atencao", "Sem <b>meta charset=\"UTF-8\"</b>, os acentos podem aparecer quebrados "
                            "(ex.: “AulaÃ§Ã£o”). Se isso acontecer, verifique a codificação do arquivo no VS Code "
                            "(canto inferior direito → UTF-8)."),
            ],
            "slides": {
                "pontos": [
                    "Elemento = tag de abertura + conteúdo + tag de fechamento",
                    "Atributos: nome=\"valor\" na tag de abertura",
                    "Elementos vazios (sem fechamento): br, hr, img, meta, input",
                    "Aninhamento: tags fecham na ordem inversa",
                    "Comentários: <!-- não aparecem na página -->",
                ],
                "codigo": {"titulo": "Anatomia + atributos", "linhas": [
                    "<p>conteúdo do elemento</p>",
                    "<html lang=\"pt-br\">",
                    "<img src=\"foto.jpg\" alt=\"Foto\">",
                    "<br>  <hr>  <!-- elementos vazios -->",
                    "<!-- comentário -->",
                ]},
                "nota": "Atividade 'leitura de elementos no quadro': escreva 5 linhas de código e peça que "
                        "identifiquem tags, atributos e conteúdo oralmente.",
            },
        },
        {
            "num": 8,
            "titulo": "Cabeçalhos e parágrafos",
            "blocos": [
                ("h", "Cabeçalhos: h1 a h6"),
                ("p", "Os cabeçalhos (ou títulos) organizam a página em <b>níveis hierárquicos</b>: <b>h1</b> é o "
                      "título principal; <b>h2</b> são as seções; <b>h3</b> subseções, e assim por diante até "
                      "<b>h6</b>. Quanto menor o número, maior o destaque."),
                ("codigo", {"titulo": "Hierarquia de títulos", "ling": "html", "linhas": [
                    "<h1>Minha Cidade</h1>            <!-- título principal (único!) -->",
                    "<h2>História</h2>                <!-- seção -->",
                    "<h3> Fundação </h3>              <!-- subseção -->",
                    "<h2>Pontos turísticos</h2>       <!-- outra seção -->",
                    "<h2>Culinária</h2>",
                ]}),
                ("conceito", ("Hierarquia não é tamanho!",
                              "Os cabeçalhos definem a <b>estrutura lógica</b> do conteúdo (como capítulos e "
                              "subcapítulos de um livro). Não use h1 só porque a letra é grande: use o nível "
                              "certo para cada trecho. Boas práticas: <b>um único h1 por página</b> e não pular "
                              "níveis (h1 → h3 sem h2).")),
                ("h", "Parágrafos, quebras e separadores"),
                ("lista", [
                    "<b>&lt;p&gt;</b> — parágrafo: agrupa um bloco de texto com espaçamento próprio;",
                    "<b>&lt;br&gt;</b> — quebra de linha <b>dentro</b> do mesmo parágrafo (elemento vazio);",
                    "<b>&lt;hr&gt;</b> — separador horizontal: marca uma mudança de assunto (elemento vazio).",
                ]),
                ("codigo", {"titulo": "pagina “Minha Cidade”", "ling": "html", "linhas": [
                    "<h1>Minha Cidade</h1>",
                    "<p>Curitiba é a capital do Paraná.<br>",
                    "   Fica na região Sul do Brasil.</p>",
                    "<hr>",
                    "<h2>História</h2>",
                    "<p>Fundada em 1693, cresceu ao redor da matriz.</p>",
                ]}),
                ("atencao", "O navegador <b>ignora</b> espaços e “Enter” extras no código HTML: dois parágrafos "
                            "digitados sem &lt;p&gt; viram um texto só na tela. Para separar textos, use "
                            "&lt;p&gt;; para quebra de linha simples, use &lt;br&gt; — não “Enter” no código."),
            ],
            "slides": {
                "pontos": [
                    "h1–h6: níveis hierárquicos de título (h1 = principal)",
                    "Um único h1 por página; não pular níveis",
                    "p = parágrafo · br = quebra de linha · hr = separador",
                    "br e hr são elementos vazios (sem fechamento)",
                    "HTML ignora 'Enter' e espaços extras do código",
                ],
                "codigo": {"titulo": "Estrutura de conteúdo", "linhas": [
                    "<h1>Minha Cidade</h1>",
                    "<h2>História</h2>",
                    "<p>Texto do parágrafo.<br>",
                    "   continuação na linha de baixo</p>",
                    "<hr>",
                ]},
                "nota": "Construir a página 'Minha Cidade' ao vivo no projetor, com a turma ditando o que cada "
                        "parte deve ser (título, seção, parágrafo).",
            },
        },
        {
            "num": 9,
            "titulo": "Formatação de textos: semântica × aparência",
            "blocos": [
                ("h", "Tags de formatação semântica"),
                ("tabela", {"titulo": "Principais tags de formatação",
                            "cab": ["Tag", "Significado (semântica)", "Aparência"],
                            "lin": [
                                ["&lt;strong&gt;", "Importante, forte ênfase", "negrito"],
                                ["&lt;em&gt;</em>", "Ênfase na leitura", "itálico"],
                                ["&lt;mark&gt;", "Trecho destacado/marcado", "fundo amarelo"],
                                ["&lt;small&gt;", "Texto secundário, letras miúdas", "menor"],
                                ["&lt;del&gt; / &lt;ins&gt;", "Removido / inserido (edições)", "tachado / sublinhado"],
                                ["&lt;sub&gt; / &lt;sup&gt;", "Subscrito / sobrescrito", "H₂O / 10²"],
                            ]}),
                ("codigo", {"titulo": "Formatação na prática", "ling": "html", "linhas": [
                    "<p>O curso é <strong>gratuito</strong> e as vagas são",
                    "   <em>limitadas</em>.</p>",
                    "<p>Não esqueça a <mark>data da prova</mark>:</p>",
                    "<p><small>Sujeito a alterações sem aviso.</small></p>",
                    "<p>A fórmula da água é H<sub>2</sub>O e 10<sup>2</sup> = 100.</p>",
                ]}),
                ("h", "Semântica × aparência: strong × b, em × i"),
                ("p", "As tags <b>&lt;b&gt;</b> e <b>&lt;i&gt;</b> deixam o texto em negrito e itálico, "
                      "respectivamente — <b>apenas aparência</b>, sem significado. Já <b>&lt;strong&gt;</b> e "
                      "<b>&lt;em&gt;</b> têm o mesmo visual, mas <b>transmitem significado</b>: dizem ao "
                      "navegador, aos leitores de tela (acessibilidade) e aos buscadores (SEO) que aquele "
                      "trecho é <b>importante</b> ou deve ser <b>enfatizado na leitura</b>."),
                ("conceito", ("Por que preferir tags semânticas?",
                              "1) <b>Acessibilidade</b>: leitores de tela avisam pessoas cegas que o trecho é "
                              "importante; 2) <b>SEO</b>: buscadores entendem melhor o conteúdo; 3) "
                              "<b>Manutenção</b>: o significado fica no código, não na aparência. "
                              "Regra do curso: use <b>strong</b> e <b>em</b>; evite <b>b</b> e <b>i</b>.")),
                ("analogia", ("Aparência é maquiagem; semântica é identidade",
                              "Dizer “isto é importante” (strong) é diferente de apenas engrossar a voz "
                              "(b). No primeiro caso, quem não pode ver a formatação (leitor de tela) ainda "
                              "assim entende o recado.")),
            ],
            "slides": {
                "pontos": [
                    "strong = importante (negrito com significado)",
                    "em = ênfase (itálico com significado)",
                    "mark = destacado · small = miúdo · sub/sup = H₂O, 10²",
                    "b e i = só aparência, sem significado",
                    "Semântica importa: acessibilidade (leitores de tela) e SEO",
                ],
                "codigo": {"titulo": "Formatação semântica", "linhas": [
                    "<p>Vagas <strong>limitadas</strong>, inscrição",
                    "   <em>gratuita</em> até <mark>sexta</mark>.</p>",
                    "<p><small>Sujeito a alterações.</small></p>",
                ]},
                "nota": "Exercício de semântica × aparência: mostre uma frase com b/i e peça para converterem "
                        "em strong/em justificando o porquê.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Página “Sobre mim”", "tipo": "pratico",
            "enunciado": "Crie <b>sobre.html</b> na pasta meu-site/ com a estrutura HTML5 completa e:",
            "passos": [
                "Título da aba: “Sobre mim — [seu nome]”;",
                "h1 com seu nome completo;",
                "Um parágrafo sobre você (idade, cidade, hobbies);",
                "Uma segunda seção com h2 “Meus objetivos no curso” e um parágrafo com strong e em;",
                "Um hr separando as seções e um small no final: “Página criada na aula 6”.",
            ],
            "esperado": "Documento HTML5 válido, charset UTF-8, hierarquia h1→h2 correta, formatação semântica "
                        "aplicada e página abrindo sem erros no navegador.",
            "orientacao": "Checklist de correção: DOCTYPE presente? lang='pt-br'? charset UTF-8? title na aba? "
                          "um único h1? tags fechadas na ordem? Passe pela sala conferindo o código (não só a tela).",
        },
        {
            "num": 2, "titulo": "Página “Minha cidade”", "tipo": "pratico",
            "enunciado": "Crie <b>cidade.html</b> apresentando sua cidade com, no mínimo: um h1, dois h2, "
                         "quatro parágrafos, um br, um hr, um mark e um strong.",
            "esperado": "Página com hierarquia correta de títulos e todos os elementos solicitados presentes e "
                        "bem aplicados (ex.: mark destacando um dado curioso, strong em informação importante).",
            "orientacao": "Peça que troquem de máquina com o colega e verifiquem o checklist. Erro comum: usar "
                          "vários h1 — corrija na hora.",
        },
        {
            "num": 3, "titulo": "Semântica × aparência", "tipo": "escrito",
            "enunciado": "Reescreva o trecho abaixo trocando as tags de aparência por tags semânticas e "
                         "justifique cada troca:",
            "codigo": {"titulo": "Trecho para corrigir", "ling": "html", "linhas": [
                "<p>A prova será <b>na sexta-feira</b> e o conteúdo",
                "   inclui <i>HTML básico</i>. Traga <b>documento</b>.",
                "   <i>Informações sujeitas a alteração.</i></p>",
            ]},
            "esperado": "&lt;b&gt;na sexta-feira&lt;/b&gt; → &lt;strong&gt; (informação importante); "
                        "&lt;i&gt;HTML básico&lt;/i&gt; → &lt;em&gt; (ênfase); o último &lt;i&gt; → &lt;small&gt; "
                        "(texto secundário) — aceita-se em com justificativa.",
            "orientacao": "O importante é a justificativa: semântica ajuda acessibilidade e SEO.",
        },
        {
            "num": 4, "titulo": "Caça-erros", "tipo": "escrito",
            "enunciado": "O código abaixo tem <b>5 erros</b>. Encontre todos e reescreva o código corrigido:",
            "codigo": {"titulo": "Código com erros", "ling": "html", "linhas": [
                "<html>",
                "<head>",
                "    <title>Teste",
                "</head>",
                "<body>",
                "    <h1>Título</h2>",
                "    <p>Um parágrafo com <strong>destaque</p></strong>",
                "    <br></br>",
                "    <p>Fim da página</p>",
                "</body>",
            ]},
            "esperado": "1) falta &lt;!DOCTYPE html&gt; (e lang no html); 2) falta charset UTF-8 (meta); "
                        "3) &lt;title&gt; sem fechamento; 4) &lt;h1&gt; fechado com &lt;/h2&gt;; 5) strong/p "
                        "cruzados + &lt;br&gt;&lt;/br&gt; (br é vazio, não tem fechamento).",
            "orientacao": "Corrija no quadro com participação da turma. Ótimo exercício pré-prova (cai na A1).",
        },
    ],
    "teste_rapido": [
        {"enunciado": "A declaração <b>&lt;!DOCTYPE html&gt;</b> serve para:",
         "alt": ["criar o título da página.",
                 "informar ao navegador que o documento usa HTML5.",
                 "definir a codificação UTF-8.",
                 "iniciar o corpo visível da página."],
         "resposta": 1,
         "comentario": "O DOCTYPE deve ser a primeira linha do arquivo e declara a versão do HTML (HTML5)."},
        {"enunciado": "As informações de configuração da página (charset, title) ficam dentro do elemento:",
         "alt": ["&lt;body&gt;", "&lt;head&gt;", "&lt;title&gt;", "&lt;meta&gt;"],
         "resposta": 1,
         "comentario": "O head guarda metadados e configurações; o body guarda o conteúdo visível. title e "
                       "meta são filhos do head."},
        {"enunciado": "Qual grupo contém apenas elementos <b>vazios</b> (sem tag de fechamento)?",
         "alt": ["p, h1, strong", "br, hr, img", "a, em, mark", "title, meta, body"],
         "resposta": 1,
         "comentario": "br, hr, img (e também meta, input) não envolvem conteúdo — não têm fechamento."},
        {"enunciado": "Sobre cabeçalhos, é <b>correto</b> afirmar:",
         "alt": ["podemos usar quantos h1 quisermos por página.",
                 "h6 é o título de maior destaque.",
                 "o ideal é um único h1 por página, representando o assunto principal.",
                 "cabeçalhos servem apenas para aumentar a fonte do texto."],
         "resposta": 2,
         "comentario": "h1 é o título principal (único por página); h2..h6 organizam seções em ordem "
                       "hierárquica — não são apenas tamanhos de fonte."},
        {"enunciado": "A diferença entre <b>&lt;strong&gt;</b> e <b>&lt;b&gt;</b> é que:",
         "alt": ["strong deixa itálico e b deixa negrito.",
                 "strong transmite importância (semântica); b apenas altera a aparência.",
                 "b é uma tag obsoleta que quebra a página.",
                 "não existe diferença: são sinônimos perfeitos."],
         "resposta": 1,
         "comentario": "Ambos exibem negrito, mas strong tem significado (importância) — usado por leitores de "
                       "tela e buscadores."},
    ],
    "avaliacao_ref": None,
}

MODULO_4 = {
    "num": 4,
    "titulo": "HTML – conteúdo",
    "parte_num": 2,
    "parte_titulo": "Ferramentas para Desenvolvimento Web (HTML)",
    "aulas_faixa": "Aulas 10 a 12",
    "semanas": "Semana 4",
    "objetivos": [
        "Criar links internos e externos com a tag a (href, target).",
        "Inserir imagens com caminhos relativos e texto alternativo (alt).",
        "Construir listas não ordenadas, ordenadas e de definição, inclusive aninhadas.",
        "Interligar as páginas de um pequeno site (navegação).",
    ],
    "aulas": [
        {
            "num": 10,
            "titulo": "Links — conectando as páginas",
            "blocos": [
                ("h", "A tag de link"),
                ("p", "O <b>hipertexto</b> é a essência da Web: textos que se conectam a outros por <b>links</b>. "
                      "O elemento <b>&lt;a&gt;</b> (âncora) cria um link; o atributo <b>href</b> indica o "
                      "<b>destino</b>; o conteúdo entre as tags é o texto clicável:"),
                ("codigo", {"titulo": "Tipos de link", "ling": "html", "linhas": [
                    "<!-- Link interno: outra página do MESMO site (caminho relativo) -->",
                    "<a href=\"sobre.html\">Sobre mim</a>",
                    "",
                    "<!-- Link externo: site de OUTRO domínio (URL absoluta) -->",
                    "<a href=\"https://www.google.com\">Google</a>",
                    "",
                    "<!-- Abrir em nova aba -->",
                    "<a href=\"https://developer.mozilla.org\" target=\"_blank\">Documentação MDN</a>",
                ]}),
                ("tabela", {"titulo": "Atributos do elemento a",
                            "cab": ["Atributo", "Função", "Exemplo"],
                            "lin": [
                                ["href", "Endereço de destino do link", "href=\"contato.html\""],
                                ["target", "Onde abrir (_blank = nova aba; padrão = mesma aba)", "target=\"_blank\""],
                                ["title", "Texto de dica ao passar o mouse", "title=\"Fale conosco\""],
                            ]}),
                ("h", "Projeto “Meu Primeiro Site”"),
                ("p", "A partir desta aula, construímos um site com <b>3 páginas interligadas</b> — index.html "
                      "(inicial), sobre.html (sobre você) e contato.html. Cada página terá um <b>menu</b> com "
                      "links para as outras duas:"),
                ("codigo", {"titulo": "Menu de navegação (presente em todas as páginas)", "ling": "html", "linhas": [
                    "<nav>",
                    "  <a href=\"index.html\">Início</a> |",
                    "  <a href=\"sobre.html\">Sobre</a> |",
                    "  <a href=\"contato.html\">Contato</a>",
                    "</nav>",
                ]}),
                ("conceito", ("Link interno × link externo",
                              "<b>Interno</b>: aponta para arquivo do próprio site — usa <b>caminho relativo</b> "
                              "(sobre.html, imagens/foto.jpg). <b>Externo</b>: aponta para outro site — usa "
                              "<b>URL absoluta</b> com protocolo e domínio (https://...). Confundir os dois é o "
                              "erro nº 1 de iniciantes: link interno com https:// não funciona!")),
                ("dica", "Teste <b>todos</b> os links após criá-los. Link quebrado (erro 404) quase sempre é "
                         "nome de arquivo digitado errado: o HTML diferencia maiúsculas de minúsculas em muitos "
                         "servidores — <b>Sobre.html</b> ≠ <b>sobre.html</b>."),
            ],
            "slides": {
                "pontos": [
                    "a href = link (âncora + destino)",
                    "Interno: caminho relativo (sobre.html) — mesmo site",
                    "Externo: URL absoluta (https://...) — outro site",
                    "target='_blank' abre em nova aba",
                    "Projeto: Meu Primeiro Site (index + sobre + contato com menu)",
                ],
                "codigo": {"titulo": "Links", "linhas": [
                    "<a href=\"sobre.html\">Sobre</a>",
                    "<a href=\"https://www.google.com\">Google</a>",
                    "<a href=\"docs.html\" target=\"_blank\">Nova aba</a>",
                ]},
                "nota": "Iniciar o projeto 'Meu Primeiro Site' nesta aula: criar as 3 páginas e o menu. Testar "
                        "cada link clicando.",
            },
        },
        {
            "num": 11,
            "titulo": "Imagens",
            "blocos": [
                ("h", "Inserindo imagens"),
                ("p", "O elemento vazio <b>&lt;img&gt;</b> exibe imagens. O atributo <b>src</b> indica o "
                      "<b>arquivo</b> da imagem; o atributo <b>alt</b> traz um <b>texto alternativo</b> que "
                      "aparece se a imagem não carregar:"),
                ("codigo", {"titulo": "Imagem com caminho relativo", "ling": "html", "linhas": [
                    "<!-- imagem dentro da pasta imagens/ do projeto -->",
                    "<img src=\"imagens/eu.jpg\" alt=\"Foto do aluno no laboratório\">",
                    "",
                    "<!-- controlando o tamanho (em pixels) -->",
                    "<img src=\"imagens/logo.png\" alt=\"Logo da escola\" width=\"150\">",
                ]}),
                ("h", "Caminhos relativos"),
                ("p", "O caminho da imagem é <b>relativo à página atual</b>:"),
                ("tabela", {"titulo": "Sintaxe de caminhos",
                            "cab": ["Caminho", "Significado", "Exemplo"],
                            "lin": [
                                ["arquivo.jpg", "Mesma pasta da página", "src=\"foto.jpg\""],
                                ["pasta/arquivo.jpg", "Subpasta da pasta atual", "src=\"imagens/foto.jpg\""],
                                ["../arquivo.jpg", "Pasta anterior (subir um nível)", "src=\"../index.html\""],
                                ["https://...", "URL externa (evite depender de imagens de outros sites)", "src=\"https://site.com/img.png\""],
                            ]}),
                ("h", "Formatos de imagem"),
                ("tabela", {"titulo": "Quando usar cada formato",
                            "cab": ["Formato", "Extensão", "Melhor para"],
                            "lin": [
                                ["JPEG", ".jpg / .jpeg", "Fotografias (muitas cores, arquivo leve — sem transparência)"],
                                ["PNG", ".png", "Imagens com fundo transparente, logos, capturas de tela"],
                                ["GIF", ".gif", "Animações simples"],
                                ["WebP", ".webp", "Versão moderna e leve de JPEG/PNG"],
                                ["SVG", ".svg", "Desenhos vetoriais (ícones) que não perdem qualidade ao ampliar"],
                            ]}),
                ("conceito", ("O atributo alt é obrigatório de verdade",
                              "O texto alternativo tem 3 funções: 1) <b>acessibilidade</b> — leitores de tela o "
                              "descrevem para pessoas cegas; 2) aparece quando a imagem <b>não carrega</b>; "
                              "3) ajuda no <b>SEO</b>. Escreva descrições reais: alt=\"Cachorro labrador "
                              "brincando na grama\", e não alt=\"imagem1\".")),
                ("atencao", "Imagem quebrada (ícone de ‘foto rasgada’)? Checklist: 1) o arquivo existe na pasta "
                            "certa? 2) o nome está idêntico (maiúsculas/minúsculas)? 3) o caminho relativo está "
                            "certo a partir da página atual? Use o F12 → aba Rede para ver o erro 404."),
            ],
            "slides": {
                "pontos": [
                    "img src alt — elemento vazio",
                    "Caminho relativo à página atual: imagens/foto.jpg, ../",
                    "alt: acessibilidade + imagem não carrega + SEO",
                    "Formatos: JPG (fotos) · PNG (transparência) · GIF (animação) · SVG (vetor)",
                    "width/height controlam o tamanho na tela",
                ],
                "codigo": {"titulo": "Imagens", "linhas": [
                    "<img src=\"imagens/eu.jpg\"",
                    "     alt=\"Foto do aluno no laboratório\">",
                    "<img src=\"imagens/logo.png\" alt=\"Logo\"",
                    "     width=\"150\">",
                ]},
                "nota": "Levar imagens de exemplo na pasta imagens/. Testar ao vivo um caminho errado para ver a "
                        "imagem quebrada e diagnosticar com F12.",
            },
        },
        {
            "num": 12,
            "titulo": "Listas",
            "blocos": [
                ("h", "Três tipos de lista"),
                ("tabela", {"titulo": "Tipos de lista em HTML",
                            "cab": ["Tipo", "Tags", "Uso"],
                            "lin": [
                                ["Não ordenada", "ul + li", "Itens sem sequência (compras, menu, características)"],
                                ["Ordenada", "ol + li", "Itens com sequência (passo a passo, ranking)"],
                                ["De definição", "dl + dt + dd", "Termo + definição (glossário)"],
                            ]}),
                ("codigo", {"titulo": "Listas na prática", "ling": "html", "linhas": [
                    "<h2>Lista de compras (não ordenada)</h2>",
                    "<ul>",
                    "  <li>Pão</li>",
                    "  <li>Leite</li>",
                    "  <li>Café</li>",
                    "</ul>",
                    "",
                    "<h2>Receita — passos (ordenada)</h2>",
                    "<ol>",
                    "  <li>Misture os ingredientes</li>",
                    "  <li>Leve ao forno por 30 min</li>",
                    "  <li>Deixe esfriar e sirva</li>",
                    "</ol>",
                ]}),
                ("codigo", {"titulo": "Lista de definição", "ling": "html", "linhas": [
                    "<dl>",
                    "  <dt>HTML</dt>",
                    "  <dd>Linguagem de marcação que estrutura páginas Web.</dd>",
                    "  <dt>Navegador</dt>",
                    "  <dd>Programa cliente que exibe páginas Web.</dd>",
                    "</dl>",
                ]}),
                ("h", "Listas aninhadas"),
                ("p", "Listas podem conter outras listas <b>dentro dos itens &lt;li&gt;</b> — útil para "
                      "subcategorias e menus:"),
                ("codigo", {"titulo": "Lista aninhada", "ling": "html", "linhas": [
                    "<ul>",
                    "  <li>Hardware",
                    "    <ul>",
                    "      <li>Processador</li>",
                    "      <li>Memória RAM</li>",
                    "    </ul>",
                    "  </li>",
                    "  <li>Software",
                    "    <ul>",
                    "      <li>Sistema operacional</li>",
                    "      <li>Navegador</li>",
                    "    </ul>",
                    "  </li>",
                    "</ul>",
                ]}),
                ("dica", "Listas não servem só para “listas de compras”: menus de navegação, sumários e até o "
                         "carrinho de um e-commerce são semanticamente listas. Use <b>ol</b> quando a ordem "
                         "importa e <b>ul</b> quando não importa."),
            ],
            "slides": {
                "pontos": [
                    "ul/li = lista não ordenada (a ordem não importa)",
                    "ol/li = lista ordenada (passos, ranking)",
                    "dl/dt/dd = lista de definição (termo + significado)",
                    "Aninhamento: lista dentro de li",
                    "Menus e sumários são semanticamente listas",
                ],
                "codigo": {"titulo": "Listas", "linhas": [
                    "<ul> <li>Pão</li> <li>Leite</li> </ul>",
                    "<ol> <li>Misture</li> <li>Asse</li> </ol>",
                    "<dl>",
                    "  <dt>HTML</dt>",
                    "  <dd>Linguagem de marcação.</dd>",
                    "</dl>",
                ]},
                "nota": "Atividade: converter o menu do 'Meu Primeiro Site' em lista (ul) — semântica correta "
                        "para menus.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Projeto “Meu Primeiro Site”", "tipo": "pratico",
            "enunciado": "Construa um site com 3 páginas interligadas (index.html, sobre.html, contato.html):",
            "passos": [
                "Todas as páginas com a estrutura HTML5 completa e o mesmo menu de navegação no topo;",
                "<b>index</b>: h1 de boas-vindas, um parágrafo com strong/em e uma imagem (imagens/);",
                "<b>sobre</b>: reaproveite/complete a página “Sobre mim” do módulo 3;",
                "<b>contato</b>: seus dados em uma lista não ordenada (e-mail, cidade, redes) e um link externo "
                "para o site da escola com target=\"_blank\";",
                "Teste todos os links partindo de qualquer página.",
            ],
            "esperado": "3 páginas navegando entre si sem links quebrados, imagem carregando por caminho "
                        "relativo, listas corretas e formatação semântica.",
            "orientacao": "Este projeto continua como atividade extraclasse (AVA, Fase 1). Checklist: menu igual "
                          "nas 3 páginas? alt nas imagens? links testados? title diferente em cada página?",
        },
        {
            "num": 2, "titulo": "Galeria de imagens", "tipo": "pratico",
            "enunciado": "Dentro do Meu Primeiro Site, crie <b>galeria.html</b> com 3 imagens na pasta "
                         "imagens/, cada uma com: caminho relativo correto, alt descritivo e largura ajustada. "
                         "Adicione a página ao menu das demais.",
            "esperado": "Galeria com 3 imagens visíveis, alts descritivos e navegação integrada ao site.",
            "orientacao": "Provocar erros de propósito (mover uma imagem de pasta) para treinarem o diagnóstico "
                          "de imagem quebrada com F12.",
        },
        {
            "num": 3, "titulo": "Receita em lista ordenada", "tipo": "pratico",
            "enunciado": "Crie <b>receita.html</b> com: h1 (nome do prato), uma ul com os ingredientes, uma ol "
                         "com o modo de preparo e uma dl explicando 2 termos culinários. Link no menu.",
            "esperado": "Uso correto dos 3 tipos de lista na mesma página, com hierarquia de títulos.",
            "orientacao": "Verificar: ingredientes em ul (ordem não importa) e preparo em ol (ordem importa). "
                          "Pergunte por que a escolha de cada tipo.",
        },
        {
            "num": 4, "titulo": "Caminhos relativos", "tipo": "escrito",
            "enunciado": "A página <b>pages/produtos.html</b> precisa exibir a imagem <b>imagens/foto.jpg</b> "
                         "(ambas dentro da pasta do projeto). Qual caminho correto no src? E se a imagem "
                         "estivesse em <b>pages/img/foto.jpg</b>?",
            "esperado": "1º caso: src=\"../imagens/foto.jpg\" (sair de pages/ e entrar em imagens/). "
                        "2º caso: src=\"img/foto.jpg\" (subpasta da pasta atual).",
            "orientacao": "Desenhe a árvore de pastas no quadro. O '../' é o ponto que mais gera erro — reforce "
                          "com mais exemplos se necessário.",
        },
    ],
    "teste_rapido": [
        {"enunciado": "Para criar um link que abre a página sobre.html do próprio site, usamos:",
         "alt": ["&lt;link src=\"sobre.html\"&gt;",
                 "&lt;a href=\"sobre.html\"&gt;Sobre&lt;/a&gt;",
                 "&lt;a src=\"https://sobre.html\"&gt;Sobre&lt;/a&gt;",
                 "&lt;href a=\"sobre.html\"&gt;Sobre&lt;/href&gt;"],
         "resposta": 1,
         "comentario": "Link interno usa a tag a com href e caminho relativo — sem https://."},
        {"enunciado": "O atributo <b>target=\"_blank\"</b> faz o link:",
         "alt": ["abrir em uma nova aba/janela.",
                 "ficar em negrito.",
                 "abrir apenas se o site for HTTPS.",
                 "ser invisível na página."],
         "resposta": 0,
         "comentario": "_blank = nova aba. Sem target, o link abre na mesma aba (comportamento padrão)."},
        {"enunciado": "Uma página em <b>pages/noticia.html</b> quer exibir <b>imagens/foto.jpg</b> (pasta "
                    "imagens/ na raiz do projeto). O src correto é:",
         "alt": ["imagens/foto.jpg", "pages/imagens/foto.jpg", "../imagens/foto.jpg", "/foto.jpg"],
         "resposta": 2,
         "comentario": "É preciso 'subir' um nível (..) a partir de pages/ para alcançar a pasta imagens/ da raiz."},
        {"enunciado": "A função do atributo <b>alt</b> em uma imagem é:",
         "alt": ["definir o tamanho da imagem na tela.",
                 "descrever a imagem para acessibilidade e para quando ela não carregar.",
                 "criar um link ao clicar na imagem.",
                 "indicar o formato do arquivo (jpg, png...)."],
         "resposta": 1,
         "comentario": "alt = texto alternativo: lido por leitores de tela, exibido se a imagem falhar e usado "
                       "por buscadores."},
        {"enunciado": "Para exibir os passos de uma receita, em que a <b>ordem importa</b>, o tipo de lista "
                    "adequado é:",
         "alt": ["ul — não ordenada, com marcadores.",
                 "ol — ordenada, com numeração automática.",
                 "dl — lista de definição.",
                 "table — tabela de passos."],
         "resposta": 1,
         "comentario": "ol numera os itens automaticamente (1, 2, 3...) — ideal para sequências e rankings."},
    ],
    "avaliacao_ref": None,
}

MODULO_5 = {
    "num": 5,
    "titulo": "HTML – tabelas e formulários",
    "parte_num": 2,
    "parte_titulo": "Ferramentas para Desenvolvimento Web (HTML)",
    "aulas_faixa": "Aulas 13 a 18",
    "semanas": "Semanas 5 e 6",
    "objetivos": [
        "Construir tabelas com table, tr, th e td.",
        "Organizar tabelas com thead, tbody, tfoot e mesclar células com colspan.",
        "Criar formulários com form, label e os principais tipos de input.",
        "Usar select, textarea e button em formulários completos.",
        "Desenvolver o projeto HTML de um site de empresa fictícia (entrega A1).",
    ],
    "aulas": [
        {
            "num": 13,
            "titulo": "Tabelas",
            "blocos": [
                ("h", "Estrutura básica"),
                ("p", "Tabelas organizam dados em <b>linhas</b> e <b>colunas</b>. No HTML: <b>&lt;table&gt;</b> é "
                      "a tabela; cada <b>&lt;tr&gt;</b> é uma linha (<i>table row</i>); cada <b>&lt;th&gt;</b> é "
                      "uma célula de <b>cabeçalho</b> (negrito, centralizada); cada <b>&lt;td&gt;</b> é uma célula "
                      "de <b>dados</b> (<i>table data</i>):"),
                ("codigo", {"titulo": "Primeira tabela", "ling": "html", "linhas": [
                    "<table border=\"1\">",
                    "  <tr>",
                    "    <th>Nome</th>",
                    "    <th>Curso</th>",
                    "  </tr>",
                    "  <tr>",
                    "    <td>Ana Silva</td>",
                    "    <td>Informática</td>",
                    "  </tr>",
                    "  <tr>",
                    "    <td>João Souza</td>",
                    "    <td>Informática</td>",
                    "  </tr>",
                    "</table>",
                ]}),
                ("conceito", ("Receita de tabela: tr sempre envolve th/td",
                              "Nunca coloque &lt;td&gt; solto dentro da &lt;table&gt;: toda célula (th ou td) "
                              "precisa estar dentro de uma linha (tr). A ordem é sempre: "
                              "table → tr → th/td. O atributo border=\"1\" mostra as bordas (para estudo; em "
                              "projetos reais, bordas vêm do CSS).")),
                ("analogia", ("Tabela = planilha",
                              "Pense em uma planilha: cada <b>tr</b> é uma linha; cada <b>td</b> é uma célula; "
                              "a primeira linha com <b>th</b> são os títulos das colunas (Nome, Curso, Nota).")),
            ],
            "slides": {
                "pontos": [
                    "table → tr (linha) → th (cabeçalho) / td (dado)",
                    "th: negrito e centralizado por padrão",
                    "Toda célula fica dentro de uma linha (tr)",
                    "border='1' apenas para estudo — bordas reais vêm do CSS",
                ],
                "codigo": {"titulo": "Tabela básica", "linhas": [
                    "<table border=\"1\">",
                    "  <tr> <th>Nome</th> <th>Curso</th> </tr>",
                    "  <tr> <td>Ana</td>  <td>Informática</td> </tr>",
                    "  <tr> <td>João</td> <td>Informática</td> </tr>",
                    "</table>",
                ]},
                "nota": "Construir a tabela ao vivo, linha por linha, perguntando 'o que acontece se eu tirar o "
                        "tr?'. Depois, cada aluno cria a sua.",
            },
        },
        {
            "num": 14,
            "titulo": "Tabelas na prática: thead, tbody, tfoot e colspan",
            "blocos": [
                ("h", "Seções da tabela"),
                ("p", "Tabelas organizadas separam o cabeçalho (<b>&lt;thead&gt;</b>), o corpo "
                      "(<b>&lt;tbody&gt;</b>) e o rodapé (<b>&lt;tfoot&gt;</b>). Isso dá significado à estrutura "
                      "e permite, no futuro, estilizar cada parte:"),
                ("codigo", {"titulo": "Tabela de alunos com seções e colspan", "ling": "html", "linhas": [
                    "<table border=\"1\">",
                    "  <thead>",
                    "    <tr> <th>Nome</th> <th>Curso</th> <th>Nota</th> </tr>",
                    "  </thead>",
                    "  <tbody>",
                    "    <tr> <td>Ana Silva</td>  <td>Informática</td> <td>9,0</td> </tr>",
                    "    <tr> <td>João Souza</td> <td>Informática</td> <td>7,5</td> </tr>",
                    "  </tbody>",
                    "  <tfoot>",
                    "    <tr>",
                    "      <td colspan=\"2\">Média da turma</td>",
                    "      <td>8,25</td>",
                    "    </tr>",
                    "  </tfoot>",
                    "</table>",
                ]}),
                ("h", "colspan — mesclando colunas"),
                ("p", "O atributo <b>colspan=\"N\"</b> faz uma célula <b>ocupar N colunas</b>. No exemplo acima, "
                      "“Média da turma” ocupa 2 colunas (Nome + Curso), e a última célula traz a média. "
                      "Existe também o <b>rowspan</b> (ocupar N linhas), usado com menos frequência."),
                ("atencao", "Ao usar colspan, <b>remova</b> as células que foram “engolidas” — senão a linha fica "
                            "com mais células que as outras e a tabela desalinha. Conte as colunas: se a tabela "
                            "tem 3 colunas, cada linha precisa somar 3 (células normais + colspans)."),
                ("dica", "Tabelas servem para <b>dados tabulares</b> (notas, horários, produtos com preço). "
                         "Não use tabelas para montar o layout da página — para isso existe CSS."),
            ],
            "slides": {
                "pontos": [
                    "thead = cabeçalho · tbody = corpo · tfoot = rodapé",
                    "colspan='N': célula ocupa N colunas",
                    "Remova as células 'engolidas' pelo colspan",
                    "Tabela é para dados tabulares — layout é com CSS",
                ],
                "codigo": {"titulo": "Tabela organizada", "linhas": [
                    "<thead> <tr><th>Nome</th><th>Curso</th><th>Nota</th></tr> </thead>",
                    "<tbody> <tr><td>Ana</td><td>Inf.</td><td>9,0</td></tr> </tbody>",
                    "<tfoot>",
                    "  <tr><td colspan=\"2\">Média</td><td>8,25</td></tr>",
                    "</tfoot>",
                ]},
                "nota": "Exercício da aula: tabela de alunos (nome, curso, nota) com thead/tbody/tfoot e "
                        "colspan na linha da média.",
            },
        },
        {
            "num": 15,
            "titulo": "Formulários: form, label e input",
            "blocos": [
                ("h", "Para que servem formulários"),
                ("p", "<b>Formulários</b> são a forma de o usuário <b>enviar dados</b> para o site: cadastros, "
                      "logins, buscas, contatos. São a ponte entre o visitante e o servidor — e a base de "
                      "qualquer aplicação Web (inclusive do seu projeto final)."),
                ("h", "Estrutura: form, label e input"),
                ("codigo", {"titulo": "Primeiro formulário", "ling": "html", "linhas": [
                    "<form action=\"processar.php\" method=\"post\">",
                    "  <label for=\"nome\">Nome:</label>",
                    "  <input type=\"text\" id=\"nome\" name=\"nome\">",
                    "",
                    "  <label for=\"email\">E-mail:</label>",
                    "  <input type=\"email\" id=\"email\" name=\"email\">",
                    "",
                    "  <button type=\"submit\">Enviar</button>",
                    "</form>",
                ]}),
                ("tabela", {"titulo": "Atributos principais",
                            "cab": ["Atributo", "Onde", "Função"],
                            "lin": [
                                ["action", "form", "Arquivo que vai receber/processar os dados"],
                                ["method", "form", "Como enviar: get ou post (módulo 11)"],
                                ["for/id", "label/input", "Associa o rótulo ao campo (clicar no label foca o campo)"],
                                ["name", "input", "Nome do campo — é assim que o PHP o identifica!"],
                                ["type", "input", "Tipo do campo (tabela abaixo)"],
                                ["placeholder", "input", "Dica de preenchimento (texto cinza dentro do campo)"],
                                ["required", "input", "Torna o preenchimento obrigatório"],
                            ]}),
                ("h", "Tipos de input"),
                ("tabela", {"titulo": "Principais tipos (type)",
                            "cab": ["type", "O que faz", "Exemplo de uso"],
                            "lin": [
                                ["text", "Texto simples de uma linha", "Nome, cidade"],
                                ["email", "E-mail (valida o formato ao enviar)", "Cadastro, contato"],
                                ["password", "Senha (oculta os caracteres)", "Login"],
                                ["number", "Números (com min/max/step)", "Idade, quantidade"],
                                ["date", "Seletor de data", "Data de nascimento"],
                                ["checkbox", "Caixa de marcação — opções independentes", "Aceito os termos"],
                                ["radio", "Botão de opção — escolha única no grupo (mesmo name)", "Turno: manhã/tarde"],
                                ["submit", "Botão de envio do formulário", "Enviar cadastro"],
                            ]}),
                ("conceito", ("radio × checkbox",
                              "<b>radio</b>: o usuário escolhe <b>uma</b> opção do grupo — todos os radios do "
                              "grupo devem ter o <b>mesmo name</b>. <b>checkbox</b>: o usuário marca "
                              "<b>quantos quiser</b> — cada opção pode ter name próprio. Ex.: turno de estudo = "
                              "radio; hobbies = checkboxes.")),
                ("atencao", "Sem o atributo <b>name</b>, o campo <b>não é enviado</b> ao servidor — o PHP não "
                            "conseguirá ler o valor. id é para o label/CSS; <b>name é para o processamento</b>."),
            ],
            "slides": {
                "pontos": [
                    "form action method = envelope dos dados",
                    "label for + input id = rótulo associado ao campo",
                    "name = identificador do campo para o servidor (obrigatório!)",
                    "types: text, email, password, number, date, checkbox, radio",
                    "radio = 1 opção do grupo (mesmo name) · checkbox = várias",
                    "required e placeholder ajudam o usuário",
                ],
                "codigo": {"titulo": "Formulário básico", "linhas": [
                    "<form action=\"processar.php\" method=\"post\">",
                    "  <label for=\"nome\">Nome:</label>",
                    "  <input type=\"text\" id=\"nome\" name=\"nome\" required>",
                    "  <button type=\"submit\">Enviar</button>",
                    "</form>",
                ]},
                "nota": "Demonstrar o clique no label focando o campo; demonstrar required bloqueando o envio; "
                        "comparar radio (mesmo name) com checkbox.",
            },
        },
        {
            "num": 16,
            "titulo": "Formulários na prática: cadastro de aluno",
            "blocos": [
                ("h", "Construindo um cadastro completo"),
                ("p", "Vamos montar o <b>Cadastro de Aluno</b> com: nome, e-mail, telefone, data de nascimento, "
                      "curso (radio) e senha. Repare na organização: cada campo tem seu label, id e name; os "
                      "radios de curso compartilham o mesmo name:"),
                ("codigo", {"titulo": "cadastro.html — cadastro de aluno", "ling": "html", "linhas": [
                    "<form action=\"processar.php\" method=\"post\">",
                    "  <label for=\"nome\">Nome completo:</label>",
                    "  <input type=\"text\" id=\"nome\" name=\"nome\" required>",
                    "",
                    "  <label for=\"email\">E-mail:</label>",
                    "  <input type=\"email\" id=\"email\" name=\"email\" required>",
                    "",
                    "  <label for=\"fone\">Telefone:</label>",
                    "  <input type=\"text\" id=\"fone\" name=\"telefone\" placeholder=\"(41) 99999-0000\">",
                    "",
                    "  <label for=\"nasc\">Data de nascimento:</label>",
                    "  <input type=\"date\" id=\"nasc\" name=\"nascimento\">",
                    "",
                    "  <p>Curso:</p>",
                    "  <input type=\"radio\" id=\"inf\" name=\"curso\" value=\"Informática\">",
                    "  <label for=\"inf\">Informática</label>",
                    "  <input type=\"radio\" id=\"adm\" name=\"curso\" value=\"Administração\">",
                    "  <label for=\"adm\">Administração</label>",
                    "",
                    "  <label for=\"senha\">Senha:</label>",
                    "  <input type=\"password\" id=\"senha\" name=\"senha\" required>",
                    "",
                    "  <button type=\"submit\">Cadastrar</button>",
                    "</form>",
                ]}),
                ("h", "Boas práticas de formulários"),
                ("lista", [
                    "Todo campo com <b>label</b> associado (for/id);",
                    "<b>required</b> nos campos essenciais;",
                    "<b>placeholder</b> com exemplo de formato (não substitui o label!);",
                    "Radios do mesmo grupo com o <b>mesmo name</b> e <b>value</b> em cada opção;",
                    "Ordem lógica dos campos: identificação → contato → dados específicos → senha → botão.",
                ]),
                ("dica", "O atributo <b>value</b> define o valor que será enviado ao servidor. Em radios e "
                         "checkboxes ele é essencial: sem value, o servidor recebe apenas 'on'."),
            ],
            "slides": {
                "pontos": [
                    "Cadastro de aluno: text, email, date, radio, password",
                    "Cada campo: label + id + name (+ required)",
                    "Radios do grupo 'curso' com mesmo name, values diferentes",
                    "Ordem lógica dos campos melhora a usabilidade",
                    "placeholder = dica; não substitui o label",
                ],
                "nota": "Aula prática de laboratório: montar o cadastro do zero. Circular pela sala conferindo "
                        "name em todos os campos. Este formulário será reaproveitado no módulo 11 (com PHP).",
            },
        },
        {
            "num": 17,
            "titulo": "Select, textarea e buttons",
            "blocos": [
                ("h", "Lista suspensa: select + option"),
                ("codigo", {"titulo": "select — escolha em lista suspensa", "ling": "html", "linhas": [
                    "<label for=\"turno\">Turno:</label>",
                    "<select id=\"turno\" name=\"turno\">",
                    "  <option value=\"\" disabled selected>Selecione...</option>",
                    "  <option value=\"manha\">Manhã</option>",
                    "  <option value=\"tarde\">Tarde</option>",
                    "  <option value=\"noite\">Noite</option>",
                    "</select>",
                ]}),
                ("p", "A primeira option (disabled + selected) funciona como “placeholder” da lista: aparece "
                      "selecionada, mas não pode ser escolhida de volta."),
                ("h", "Texto longo: textarea"),
                ("codigo", {"titulo": "textarea — mensagem de várias linhas", "ling": "html", "linhas": [
                    "<label for=\"msg\">Mensagem:</label>",
                    "<textarea id=\"msg\" name=\"mensagem\" rows=\"4\" cols=\"40\"",
                    "  placeholder=\"Escreva sua mensagem...\"></textarea>",
                ]}),
                ("p", "Diferente do input, o <b>textarea</b> tem tag de abertura <b>e</b> fechamento; o texto "
                      "inicial (se houver) fica entre elas. rows e cols definem o tamanho visível."),
                ("h", "Botões"),
                ("codigo", {"titulo": "Botões do formulário", "ling": "html", "linhas": [
                    "<button type=\"submit\">Cadastrar</button>  <!-- envia o formulário -->",
                    "<button type=\"reset\">Limpar</button>       <!-- apaga os campos -->",
                    "<input type=\"submit\" value=\"Enviar\">      <!-- alternativa ao button -->",
                ]}),
                ("tabela", {"titulo": "select × radio — qual usar?",
                            "cab": ["Situação", "Melhor campo"],
                            "lin": [
                                ["2 a 4 opções, todas importantes (sim/não, turno)", "radio — todas ficam visíveis"],
                                ["Muitas opções (cidades, cursos, estados)", "select — economiza espaço"],
                                ["Várias escolhas independentes (hobbies)", "checkbox"],
                                ["Texto livre de várias linhas (mensagem)", "textarea"],
                            ]}),
            ],
            "slides": {
                "pontos": [
                    "select/option = lista suspensa (muitas opções)",
                    "option disabled+selected = 'Selecione...' inicial",
                    "textarea rows cols = texto de várias linhas (tem fechamento!)",
                    "button type submit / reset",
                    "Poucas opções → radio; muitas → select",
                ],
                "codigo": {"titulo": "select + textarea", "linhas": [
                    "<select name=\"turno\">",
                    "  <option value=\"\" disabled selected>Selecione...</option>",
                    "  <option value=\"manha\">Manhã</option>",
                    "</select>",
                    "<textarea name=\"mensagem\" rows=\"4\"></textarea>",
                ]},
                "nota": "Finalizar o cadastro de aluno com select de turno e textarea de observações.",
            },
        },
        {
            "num": 18,
            "titulo": "Projeto HTML: site da empresa fictícia (entrega A1)",
            "blocos": [
                ("h", "O projeto"),
                ("p", "Hora de juntar <b>tudo</b> o que aprendemos de HTML em um projeto completo: o site de uma "
                      "<b>empresa fictícia</b> com <b>4 páginas</b> (index, empresa, produtos e contato). "
                      "Este é o <b>trabalho prático da Avaliação 1 (10 pts)</b> — entrega na semana 6 (S)."),
                ("h", "Requisitos do projeto"),
                ("lista_num", [
                    "<b>4 páginas</b>: index.html (início), empresa.html (quem somos), produtos.html "
                    "(catálogo) e contato.html (fale conosco);",
                    "<b>Menu de navegação</b> igual em todas as páginas (links testados!);",
                    "<b>Estrutura HTML5</b> completa em todas (DOCTYPE, lang, charset, title);",
                    "<b>index</b>: h1, textos com formatação semântica (strong/em), imagem com alt e uma lista;",
                    "<b>empresa</b>: história da empresa com h1/h2, parágrafos, br/hr e uma imagem;",
                    "<b>produtos</b>: <b>tabela</b> com pelo menos 4 produtos (nome, categoria, preço, "
                    "estoque) usando thead/tbody/tfoot e colspan na linha de total/rodapé;",
                    "<b>contato</b>: <b>formulário completo</b> — nome, e-mail, assunto (select), mensagem "
                    "(textarea), checkbox “quero receber novidades” e botão de envio;",
                    "Pasta <b>imagens/</b> organizada, nomes de arquivo sem acento/espaço.",
                ]),
                ("conceito", ("O que será avaliado (10 pts — S)",
                              "Estrutura e navegação (2 pts) · Elementos de conteúdo: títulos, textos, "
                              "imagens e listas (2 pts) · Tabela completa e correta (2 pts) · Formulário "
                              "completo e correto (2 pts) · Organização dos arquivos e qualidade do código "
                              "(2 pts). Critérios detalhados na seção <b>Avaliação A1</b> desta apostila.")),
                ("dica", "Planeje antes de codificar: desenhe o mapa do site e o esboço de cada página no "
                         "caderno. Desenvolva uma página por vez e teste no navegador a cada etapa. Reutilize "
                         "o menu: copie e cole entre as páginas, ajustando o destaque da página atual."),
            ],
            "slides": {
                "pontos": [
                    "PROJETO A1 (10 pts): site da empresa fictícia — 4 páginas",
                    "index · empresa · produtos · contato — menu em todas",
                    "Requisitos: HTML5, semântica, imagem+alt, listas",
                    "produtos: tabela com thead/tbody/tfoot + colspan",
                    "contato: formulário completo (select, textarea, checkbox)",
                    "Organização: pasta imagens/, nomes sem acento/espaço",
                ],
                "nota": "Entrega na semana 6. Reservar a aula para trabalho supervisionado: grupos tirando "
                        "dúvidas, professor circulando com o checklist de requisitos.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Tabela de horários", "tipo": "pratico",
            "enunciado": "Crie <b>horarios.html</b> com a tabela do seu horário escolar: 1ª linha com th "
                         "(dias da semana) e as demais com as aulas (td). Use thead e tbody.",
            "esperado": "Tabela alinhada com cabeçalho em th, dias como colunas e horários/aulas nas células.",
            "orientacao": "Confira se th está apenas no cabeçalho. Desafio extra: colspan para 'intervalo' "
                          "ocupando todos os dias.",
        },
        {
            "num": 2, "titulo": "Tabela de alunos com tfoot e colspan", "tipo": "pratico",
            "enunciado": "Construa a tabela de alunos (Nome, Curso, Nota) com 4 registros, usando thead, tbody "
                         "e tfoot. No tfoot, uma célula com colspan=\"2\" (ex.: “Média da turma”) e a média na "
                         "última coluna.",
            "esperado": "Tabela com 3 colunas; linha do tfoot com apenas 2 células (a primeira com colspan=2); "
                        "média calculada corretamente.",
            "orientacao": "Erro típico: manter 3 células no tfoot + colspan → linha desalinha. Faça-os contar "
                          "as colunas.",
        },
        {
            "num": 3, "titulo": "Cadastro de aluno completo", "tipo": "pratico",
            "enunciado": "Monte <b>cadastro.html</b> com: nome (text, required), e-mail (email, required), "
                         "telefone (text, placeholder), data de nascimento (date), curso (radio: Informática, "
                         "Administração, Redes), turno (select), observações (textarea), aceite dos termos "
                         "(checkbox) e botão Cadastrar.",
            "esperado": "Formulário completo com labels associados, names corretos, radios com mesmo name e "
                        "values definidos, select com opção 'Selecione...', textarea e checkbox funcionais.",
            "orientacao": "Testar envio (vai dar erro/abrir o processar.php inexistente — esperado; explique que "
                          "o back-end vem no módulo 11). Confira name em TODOS os campos.",
        },
        {
            "num": 4, "titulo": "Projeto A1 — site da empresa fictícia", "tipo": "grupo",
            "enunciado": "Em duplas (ou individual, a critério do professor), desenvolva o site completo da "
                         "empresa fictícia conforme os requisitos da aula 18. <b>Trabalho avaliativo — 10 pts "
                         "da A1 (S)</b>. Entrega: semana 6, via AVA/Drive + pasta do laboratório.",
            "passos": [
                "Planejar: nome da empresa, ramo, esboço das 4 páginas no caderno;",
                "Criar a estrutura de pastas (empresa-x/, imagens/);",
                "Desenvolver página por página, testando no navegador;",
                "Revisar o checklist de requisitos antes de entregar.",
            ],
            "esperado": "Site com 4 páginas navegáveis atendendo todos os requisitos da aula 18.",
            "orientacao": "Usar o rubrica da seção A1 para a nota. Sugestão: aula de revisão com autoavaliação "
                          "por checklist antes da entrega final.",
        },
    ],
    "teste_rapido": [
        {"enunciado": "Em uma tabela HTML, a diferença entre th e td é:",
         "alt": ["th é célula de dado; td é célula de cabeçalho.",
                 "th é célula de cabeçalho (destacada); td é célula de dado.",
                 "th só pode ser usado no tfoot.",
                 "não há diferença: são sinônimos."],
         "resposta": 1,
         "comentario": "th marca cabeçalhos de coluna/linha (negrito, centralizado por padrão); td marca dados."},
        {"enunciado": "O atributo <b>colspan=\"3\"</b> em uma célula faz com que ela:",
         "alt": ["seja repetida em 3 linhas.",
                 "ocupe o espaço de 3 colunas.",
                 "tenha 3 pixels de borda.",
                 "exiba 3 textos diferentes."],
         "resposta": 1,
         "comentario": "colspan mescla colunas (a célula ocupa 3); rowspan mesclaria linhas."},
        {"enunciado": "Em um formulário, o atributo <b>label for=\"nome\"</b> deve casar com qual atributo do "
                    "input?",
         "alt": ["name=\"nome\"", "id=\"nome\"", "value=\"nome\"", "type=\"nome\""],
         "resposta": 1,
         "comentario": "O for do label aponta para o id do campo. O name serve para o envio ao servidor — são "
                       "funções diferentes."},
        {"enunciado": "Para o usuário escolher <b>apenas uma</b> opção entre “Manhã, Tarde ou Noite”, o campo "
                    "adequado é:",
         "alt": ["3 checkboxes com names diferentes.",
                 "3 inputs type=\"radio\" com o mesmo name.",
                 "3 inputs type=\"text\".",
                 "1 textarea listando as opções."],
         "resposta": 1,
         "comentario": "Radios com o MESMO name formam um grupo de escolha única. Checkboxes permitem múltiplas "
                       "escolhas."},
        {"enunciado": "No form, os atributos <b>action</b> e <b>method</b> definem, respectivamente:",
         "alt": ["o estilo do formulário e a cor do botão.",
                 "o arquivo que processará os dados e o modo de envio (get/post).",
                 "o título da página e o idioma.",
                 "quais campos são obrigatórios e seus tipos."],
         "resposta": 1,
         "comentario": "action = destino do processamento (ex.: processar.php); method = forma de envio dos "
                       "dados (GET ou POST — módulo 11)."},
    ],
    "avaliacao_ref": "A1",
}

MODULOS = [MODULO_3, MODULO_4, MODULO_5]
