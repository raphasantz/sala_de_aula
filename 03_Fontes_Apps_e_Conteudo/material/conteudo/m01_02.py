# -*- coding: utf-8 -*-
"""Módulos 1 e 2 — Parte I (Fundamentos da Internet e da Web) e abertura da Parte II."""

MODULO_1 = {
    "num": 1,
    "titulo": "Introdução à Web",
    "parte_num": 1,
    "parte_titulo": "Fundamentos da Internet e da Web",
    "aulas_faixa": "Aulas 1 a 4",
    "semanas": "Semanas 1 e 2",
    "objetivos": [
        "Explicar o que é a Internet e diferenciá-la da World Wide Web (Web).",
        "Descrever o modelo cliente/servidor e o papel do navegador.",
        "Entender o ciclo requisição → resposta e a diferença entre HTTP e HTTPS.",
        "Identificar as partes de uma URL (protocolo, domínio, caminho e recurso).",
        "Explicar os conceitos de endereço IP, DNS, domínio e hospedagem.",
        "Reconhecer portais, e-business e e-commerce e o fluxo de uma loja virtual.",
    ],
    "aulas": [
        {
            "num": 1,
            "titulo": "O que é a Internet?",
            "blocos": [
                ("h", "Redes de computadores"),
                ("p", "Uma <b>rede de computadores</b> é um conjunto de dispositivos (computadores, celulares, "
                      "servidores) conectados entre si para <b>trocar informações</b>. Redes locais (como a do "
                      "laboratório da escola) conectam dispositivos próximos; já a <b>Internet</b> é uma "
                      "<b>rede mundial de redes</b>: bilhões de dispositivos interligados que se comunicam usando "
                      "regras comuns, chamadas <b>protocolos</b>."),
                ("h", "Internet × Web"),
                ("p", "É muito comum confundir <b>Internet</b> com <b>Web</b>, mas elas não são a mesma coisa. "
                      "A Internet é a <b>infraestrutura</b> — as “estradas” por onde os dados trafegam. A Web "
                      "(World Wide Web, ou WWW) é <b>um dos serviços</b> que funcionam sobre essas estradas: o "
                      "conjunto de páginas e sites que acessamos pelo navegador."),
                ("conceito", ("Internet × Web",
                              "<b>Internet</b> = a rede física e lógica mundial que conecta dispositivos. "
                              "<b>Web</b> = serviço de páginas interligadas (sites) que trafega na Internet. "
                              "Outros serviços que também usam a Internet: e-mail, streaming de vídeo, jogos "
                              "on-line, mensagens instantâneas e transferência de arquivos.")),
                ("h", "Cliente e servidor"),
                ("p", "Na Web, dois papéis se destacam: o <b>cliente</b>, que <b>pede</b> uma informação, e o "
                      "<b>servidor</b>, que <b>fornece</b> essa informação. O computador ou celular que você usa "
                      "é o cliente; o computador remoto que guarda o site é o servidor. O programa cliente mais "
                      "conhecido é o <b>navegador</b> (browser), como Chrome, Firefox e Edge."),
                ("tabela", {"titulo": "Cliente × Servidor",
                            "cab": ["", "Cliente", "Servidor"],
                            "lin": [
                                ["Papel", "Solicita recursos (páginas, imagens, dados)", "Armazena e fornece recursos"],
                                ["Onde fica", "No dispositivo do usuário", "Em máquinas remotas, ligadas 24 h"],
                                ["Exemplos", "Navegador, celular, computador da escola", "Servidor Web, hospedagem de sites"],
                                ["Quem programa", "Front-end (HTML, CSS, JavaScript)", "Back-end (PHP, banco de dados)"],
                            ]}),
                ("analogia", ("A Internet é como um restaurante",
                              "Você (o <b>cliente</b>) senta e faz o pedido ao garçom. O pedido chega à cozinha "
                              "(o <b>servidor</b>), que prepara o prato e o envia de volta. Na Web funciona assim: "
                              "o navegador faz uma <b>requisição</b> (“quero a página inicial”), o servidor Web "
                              "processa o pedido e devolve uma <b>resposta</b> (o conteúdo da página). As "
                              "<b>estradas</b> por onde o garçom passa são os cabos, fibras ópticas e sinais "
                              "wi-fi da Internet.")),
            ],
            "slides": {
                "pontos": [
                    "Rede = dispositivos conectados trocando informações",
                    "Internet: rede mundial de redes (a infraestrutura)",
                    "Web (WWW): um dos serviços da Internet — sites e páginas",
                    "Cliente pede → Servidor fornece (modelo cliente/servidor)",
                    "Navegador = o programa cliente da Web",
                ],
                "nota": "Use a analogia do restaurante: cliente faz o pedido (requisição), cozinha prepara "
                        "(servidor), garçom entrega (resposta). Pergunte à turma: a Internet é a mesma coisa que "
                        "a Web? Deixe que respondam antes de mostrar o conceito-chave.",
            },
        },
        {
            "num": 2,
            "titulo": "Como a Web funciona?",
            "blocos": [
                ("h", "Requisição e resposta"),
                ("p", "Tudo na Web começa com uma <b>requisição</b>: você digita um endereço (ou clica em um "
                      "link) e o navegador <b>pede</b> aquele recurso a um servidor. O servidor <b>responde</b> "
                      "enviando o conteúdo (código HTML, imagens, etc.). O navegador então “desenha” a página na "
                      "tela. Esse ciclo se repete a cada clique."),
                ("lista_num", [
                    "Você digita o endereço do site no navegador;",
                    "O navegador descobre qual é o servidor responsável pelo endereço;",
                    "O navegador envia uma <b>requisição HTTP</b> ao servidor;",
                    "O servidor processa o pedido e devolve uma <b>resposta HTTP</b> (a página);",
                    "O navegador interpreta o HTML recebido e exibe a página na tela.",
                ]),
                ("h", "HTTP e HTTPS"),
                ("p", "<b>HTTP</b> (HyperText Transfer Protocol — Protocolo de Transferência de Hipertexto) é o "
                      "protocolo de comunicação da Web: o conjunto de regras que define como requisições e "
                      "respostas são feitas. O <b>HTTPS</b> é a versão <b>segura</b> do HTTP: os dados trafegam "
                      "<b>criptografados</b>, protegendo senhas e informações pessoais. Sites com HTTPS mostram "
                      "um <b>cadeado</b> na barra de endereços."),
                ("conceito", ("Por que HTTPS importa?",
                              "Em uma conexão HTTP “pura”, qualquer pessoa no caminho poderia ler os dados "
                              "trocados (senhas, cartões, mensagens). O HTTPS criptografa a comunicação entre "
                              "navegador e servidor. Regra prática: nunca digite dados pessoais ou senhas em "
                              "sites sem HTTPS (sem o cadeado).")),
                ("h", "Anatomia da URL"),
                ("p", "<b>URL</b> (Uniform Resource Locator) é o <b>endereço</b> de um recurso na Web. Cada parte "
                      "tem uma função:"),
                ("codigo", {"titulo": "As partes de uma URL", "ling": "texto", "linhas": [
                    "https://www.lojaexemplo.com.br/produtos/notebook.php?id=10",
                    "└─┬─┘   └───────┬────────┘└───┬───┘└────┬────┘└─┬──┘",
                    "protocolo     domínio        caminho    recurso  parâmetro",
                ]}),
                ("tabela", {"titulo": "Componentes da URL",
                            "cab": ["Parte", "Exemplo", "Para que serve"],
                            "lin": [
                                ["Protocolo", "https://", "Regra de comunicação usada (HTTP, HTTPS, FTP...)"],
                                ["Domínio", "www.lojaexemplo.com.br", "Nome do site — identifica o servidor"],
                                ["Caminho", "/produtos/", "Pasta (diretório) dentro do site"],
                                ["Recurso", "notebook.php", "Arquivo/página solicitada"],
                                ["Parâmetros", "?id=10", "Dados extras enviados à página (após o ?)"],
                            ]}),
                ("dica", "Para memorizar: o <b>protocolo</b> é “como” conversar; o <b>domínio</b> é “com quem” "
                         "conversar; o <b>caminho + recurso</b> é “o que” você quer; os <b>parâmetros</b> são "
                         "detalhes adicionais do pedido."),
            ],
            "slides": {
                "pontos": [
                    "Ciclo da Web: requisição → processamento → resposta",
                    "HTTP = protocolo (regras) da comunicação na Web",
                    "HTTPS = HTTP com criptografia (cadeado no navegador)",
                    "URL = endereço do recurso na Web",
                ],
                "extra": [
                    "URL: protocolo + domínio + caminho + recurso + parâmetros",
                    "Ex.: https://www.lojaexemplo.com.br/produtos/notebook.php?id=10",
                ],
                "codigo": {"titulo": "Anatomia da URL", "linhas": [
                    "https://www.lojaexemplo.com.br/produtos/notebook.php?id=10",
                    "protocolo    dominio            caminho     recurso   param",
                ]},
                "nota": "Peça para abrirem um site qualquer e identificarem cada parte da URL em voz alta. "
                        "Verifique se todos encontram o cadeado do HTTPS.",
            },
        },
        {
            "num": 3,
            "titulo": "Domínio, hospedagem e servidor Web",
            "blocos": [
                ("h", "Endereço IP"),
                ("p", "Todo dispositivo conectado a uma rede possui um <b>endereço IP</b> — um número que o "
                      "identifica, como <b>142.250.78.14</b>. É o “endereço da casa” do dispositivo na rede: "
                      "para enviar dados, é preciso saber o IP de destino."),
                ("h", "DNS — a agenda da Internet"),
                ("p", "Decorar números IP seria inviável. Por isso existem os <b>domínios</b>: nomes amigáveis "
                      "como <b>google.com</b>. O <b>DNS</b> (Domain Name System) é o sistema que <b>traduz o nome "
                      "do domínio para o endereço IP</b> do servidor, funcionando como uma grande “agenda de "
                      "telefones” da Internet."),
                ("analogia", ("DNS = agenda telefônica",
                              "Você procura “Pizzaria do João” na agenda (nome do domínio) para descobrir o "
                              "número de telefone (endereço IP) e então fazer a ligação (requisição). O DNS faz "
                              "exatamente isso, em milissegundos, cada vez que você digita um endereço.")),
                ("h", "Domínio: registro e escolha"),
                ("p", "O domínio é <b>registrado</b> (alugado por um período) em órgãos competentes: no Brasil, "
                      "domínios <b>.com.br</b> são registrados no <b>registro.br</b>; domínios internacionais "
                      "(.com, .net, .org) em registradores credenciados. Um domínio registrado é seu “endereço "
                      "oficial” na Web — nenhum outro site pode usar o mesmo nome."),
                ("h", "Hospedagem e servidor Web"),
                ("p", "Para que um site fique no ar, seus arquivos precisam ficar guardados em um computador "
                      "ligado 24 horas por dia, com software preparado para atender requisições: o "
                      "<b>servidor Web</b>. O serviço que aluga esse espaço é a <b>hospedagem</b>. Empresas que "
                      "oferecem hospedagem e outros serviços de acesso são os <b>provedores</b>."),
                ("tabela", {"titulo": "Tipos de hospedagem",
                            "cab": ["Tipo", "Como funciona", "Indicado para"],
                            "lin": [
                                ["Gratuita", "Espaço limitado, muitas vezes com anúncios e sem domínio próprio", "Estudos e testes (como nosso curso!)"],
                                ["Compartilhada", "Vários sites dividem o mesmo servidor", "Sites pequenos e pessoais"],
                                ["VPS", "Servidor virtual com recursos dedicados", "Sites médios e aplicações"],
                                ["Dedicada", "Um servidor físico inteiro para o cliente", "Grandes empresas e alto tráfego"],
                                ["Nuvem (cloud)", "Recursos distribuídos em vários servidores, cobrados sob demanda", "Aplicações que precisam escalar"],
                            ]}),
                ("h", "O caminho completo de um acesso"),
                ("lista_num", [
                    "Você digita <b>www.meusite.com.br</b> no navegador;",
                    "O <b>DNS</b> consulta e descobre o <b>IP</b> do servidor do site;",
                    "O navegador envia a <b>requisição</b> ao servidor Web naquele IP;",
                    "O <b>servidor Web</b> localiza os arquivos do site na <b>hospedagem</b>;",
                    "A <b>resposta</b> (HTML, imagens...) volta ao navegador, que exibe a página.",
                ]),
            ],
            "slides": {
                "pontos": [
                    "IP = número que identifica o dispositivo na rede",
                    "Domínio = nome amigável (ex.: meusite.com.br)",
                    "DNS = traduz domínio → IP (a “agenda” da Internet)",
                    "Hospedagem = espaço em servidor ligado 24 h",
                    "Servidor Web = software que atende as requisições",
                    "Gratuita × compartilhada × VPS × dedicada × nuvem",
                ],
                "nota": "Desenhe no quadro o fluxo: navegador → DNS → IP → servidor → resposta. Depois peça que "
                        "um aluno explique o caminho com as próprias palavras.",
            },
        },
        {
            "num": 4,
            "titulo": "Portais, e-business e e-commerce",
            "blocos": [
                ("h", "Portais"),
                ("p", "<b>Portal</b> é um site que <b>concentra conteúdo e serviços</b> em um só lugar, "
                      "funcionando como “porta de entrada” para um conjunto de informações. Exemplos comuns:"),
                ("lista", [
                    "<b>Portal institucional</b>: apresenta uma organização — empresa, prefeitura, escola "
                    "(notícias, serviços, contatos);",
                    "<b>Portal educacional</b>: ambiente de estudo — como o nosso <b>AVA/Portal Acadêmico</b>, "
                    "com tarefas, fóruns e questionários;",
                    "<b>Portal de notícias</b>: reúne matérias de vários assuntos (G1, UOL etc.).",
                ]),
                ("h", "e-Business — negócios digitais"),
                ("p", "<b>e-Business</b> (electronic business) é o uso da Internet para <b>conduzir os negócios "
                      "de uma empresa</b> de forma digital: atendimento ao cliente, comunicação com fornecedores, "
                      "gestão interna, marketing digital. É um conceito <b>amplo</b> — abrange toda a operação "
                      "digital da empresa, não apenas a venda."),
                ("h", "e-Commerce — comércio eletrônico"),
                ("p", "<b>e-Commerce</b> é a parte do e-business que trata da <b>compra e venda on-line</b>: a "
                      "<b>loja virtual</b>. O cliente navega pelo catálogo, coloca produtos no carrinho e "
                      "finaliza o pedido com pagamento eletrônico."),
                ("conceito", ("e-Business × e-Commerce",
                              "Todo e-commerce faz parte de um e-business, mas e-business é mais amplo: inclui "
                              "também processos internos, relacionamento com fornecedores e atendimento. "
                              "Resumindo: <b>e-business = negócio digital por completo</b>; "
                              "<b>e-commerce = vendas on-line</b>.")),
                ("h", "Fluxo de uma loja virtual"),
                ("lista_num", [
                    "<b>Início</b>: o cliente chega à página inicial da loja;",
                    "<b>Catálogo</b>: navega pelos produtos, busca e filtra;",
                    "<b>Ficha do produto</b>: vê fotos, descrição, preço e avaliações;",
                    "<b>Carrinho</b>: adiciona itens, ajusta quantidades;",
                    "<b>Checkout</b>: identifica-se, informa entrega e pagamento;",
                    "<b>Confirmação</b>: recebe o número do pedido e a confirmação.",
                ]),
                ("dica", "Observe esse fluxo em lojas reais (Mercado Livre, Amazon, Magalu): ele é praticamente "
                         "o mesmo em todas. Entender esse padrão ajuda a projetar qualquer site de vendas — "
                         "inclusive o seu projeto final!"),
            ],
            "slides": {
                "pontos": [
                    "Portal: concentra conteúdo/serviços (institucional, educacional, notícias)",
                    "e-Business: negócio conduzido de forma digital (conceito amplo)",
                    "e-Commerce: compra e venda on-line — a loja virtual",
                    "Todo e-commerce é e-business; nem todo e-business é e-commerce",
                ],
                "extra": [
                    "Fluxo da loja virtual:",
                    "início → catálogo → ficha do produto → carrinho → checkout → confirmação",
                ],
                "nota": "Estudo de caso: abra uma loja virtual conhecida e percorra o fluxo com a turma, "
                        "identificando cada etapa na tela.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Observação guiada de sites", "tipo": "pratico",
            "enunciado": "Abra <b>3 sites diferentes</b> no navegador (ex.: um portal de notícias, o site de uma "
                         "loja e o portal da escola). Para cada um, registre no caderno:",
            "passos": [
                "O endereço completo (URL) e as partes: protocolo, domínio, caminho e recurso;",
                "Se a conexão é HTTPS (cadeado) — clique no cadeado e anote o que aparece;",
                "Que tipo de site é: portal institucional, portal de notícias, e-commerce, outro;",
                "Compare as anotações com um colega.",
            ],
            "esperado": "Tabela com 3 linhas (uma por site) identificando URL correta, presença de HTTPS e "
                        "classificação do tipo de site.",
            "orientacao": "Verifique se distinguem domínio de caminho. Ótima oportunidade para corrigir o "
                          "vocabulário (‘site’ × ‘página’ × ‘URL’).",
        },
        {
            "num": 2, "titulo": "Análise de 5 URLs", "tipo": "escrito",
            "enunciado": "Identifique <b>protocolo, domínio, caminho, recurso e parâmetros</b> (quando houver) "
                         "nas URLs abaixo:",
            "passos": [
                "1) https://www.empresa.com.br/index.html",
                "2) http://portal.escola.edu.br/ava/login.php",
                "3) https://loja.com.br/produtos/celular.php?id=42&amp;cor=azul",
                "4) https://noticias.uol.com.br/ultimas/",
                "5) https://registro.br/tecnologia/dns/",
            ],
            "esperado": "1) https | empresa.com.br | / | index.html | — · 2) http | portal.escola.edu.br | "
                        "/ava/ | login.php | — · 3) https | loja.com.br | /produtos/ | celular.php | id=42 e "
                        "cor=azul · 4) https | noticias.uol.com.br | /ultimas/ | (pasta como recurso) | — · "
                        "5) https | registro.br | /tecnologia/dns/ | (pasta como recurso) | —",
            "orientacao": "Aceite variações razoáveis na separação caminho × recurso; o importante é "
                          "identificarem domínio e protocolo corretamente e notarem os parâmetros após o '?'.",
        },
        {
            "num": 3, "titulo": "Pesquisa em grupo: domínio × hospedagem × DNS", "tipo": "grupo",
            "enunciado": "Em grupos de 3 a 4 alunos, pesquisem e montem um resumo (cartaz ou 1 página) "
                         "respondendo:",
            "passos": [
                "O que é e onde se registra um domínio .com.br? Quanto custa por ano (pesquisa no registro.br)?",
                "O que é hospedagem? Citem 2 empresas que oferecem hospedagem gratuita e 2 pagas;",
                "Como funciona o DNS? Expliquem com uma analogia criada pelo grupo;",
                "Desenhem o fluxo completo: do navegador digitando a URL até a página aparecer na tela.",
            ],
            "esperado": "Resumo com: registro.br (~R$ 40/ano, valores podem variar), exemplos de hospedagens "
                        "(gratuitas: InfinityFree, GitHub Pages; pagas: HostGator, Locaweb, Hostinger), "
                        "analogia do DNS e desenho do fluxo em 5 etapas.",
            "orientacao": "Valorize a analogia criada pelo grupo e a clareza do desenho do fluxo. Cada grupo "
                          "apresenta em 2 minutos na aula seguinte.",
        },
        {
            "num": 4, "titulo": "Estudo de caso: o fluxo da loja virtual", "tipo": "escrito",
            "enunciado": "Escolha uma loja virtual conhecida e percorra uma compra (sem pagar!) até o carrinho. "
                         "Escreva as etapas observadas (início → catálogo → ficha → carrinho → checkout) e "
                         "responda: em quais etapas são usados formulários? Em qual etapa a loja precisa "
                         "processar dados no servidor?",
            "esperado": "Descrição das 5–6 etapas; identificação de formulários no login/cadastro, busca e "
                        "checkout; percepção de que catálogo, carrinho e confirmação exigem processamento no "
                        "servidor.",
            "orientacao": "Conecte com o que virá no curso: formulários (módulo 5) e processamento com PHP "
                          "(módulos 10 e 11).",
        },
    ],
    "teste_rapido": [
        {"enunciado": "Qual afirmação descreve corretamente a relação entre Internet e Web?",
         "alt": ["São sinônimos perfeitos, apenas em idiomas diferentes.",
                 "A Web é a infraestrutura física; a Internet são os sites.",
                 "A Web é um dos serviços que funcionam sobre a Internet.",
                 "A Internet só existe para acessar a Web."],
         "resposta": 2,
         "comentario": "A Internet é a rede mundial (infraestrutura); a Web é um serviço que trafega nela, "
                       "assim como e-mail, streaming e jogos."},
        {"enunciado": "No modelo cliente/servidor da Web, o navegador do usuário é:",
         "alt": ["o servidor, pois guarda as páginas.",
                 "o cliente, pois solicita os recursos ao servidor.",
                 "o DNS, pois traduz os endereços.",
                 "o protocolo, pois define as regras."],
         "resposta": 1,
         "comentario": "O navegador é o software cliente: ele faz a requisição e exibe a resposta enviada pelo "
                       "servidor Web."},
        {"enunciado": "A principal função do DNS é:",
         "alt": ["criptografar os dados entre navegador e servidor.",
                 "hospedar os arquivos dos sites.",
                 "traduzir o nome do domínio para o endereço IP do servidor.",
                 "acelerar o processamento de páginas PHP."],
         "resposta": 2,
         "comentario": "O DNS é a ‘agenda’ da Internet: converte nomes (meusite.com.br) em números IP."},
        {"enunciado": "Um site com HTTPS, em comparação com HTTP, oferece:",
         "alt": ["mais cores e imagens na página.",
                 "comunicação criptografada entre navegador e servidor.",
                 "hospedagem gratuita garantida.",
                 "domínio registrado automaticamente no registro.br."],
         "resposta": 1,
         "comentario": "HTTPS = HTTP + criptografia. O cadeado na barra indica conexão segura para digitar "
                       "senhas e dados pessoais."},
        {"enunciado": "Na URL https://loja.com.br/produtos/fone.php?id=7, o trecho <b>produtos/fone.php</b> "
                    "representa:",
         "alt": ["o protocolo da comunicação.",
                 "o domínio registrado da loja.",
                 "os parâmetros enviados ao servidor.",
                 "o caminho e o recurso (página) solicitado."],
         "resposta": 3,
         "comentario": "Protocolo = https; domínio = loja.com.br; caminho/recurso = /produtos/fone.php; "
                       "parâmetro = id=7."},
    ],
    "avaliacao_ref": None,
}

MODULO_2 = {
    "num": 2,
    "titulo": "Ferramentas de desenvolvimento",
    "parte_num": 2,
    "parte_titulo": "Ferramentas para Desenvolvimento Web (HTML)",
    "aulas_faixa": "Aula 5",
    "semanas": "Semana 2",
    "objetivos": [
        "Conhecer as ferramentas básicas do desenvolvedor Web: editor de código, navegador e terminal.",
        "Instalar e configurar o ambiente de desenvolvimento (sugestão: VS Code).",
        "Criar e organizar a estrutura de pastas de um projeto Web.",
        "Entender a importância das extensões de arquivo e do texto puro.",
    ],
    "aulas": [
        {
            "num": 5,
            "titulo": "Ambiente de desenvolvimento",
            "blocos": [
                ("h", "As 4 ferramentas do desenvolvedor Web"),
                ("tabela", {"titulo": "Para que serve cada ferramenta",
                            "cab": ["Ferramenta", "Papel no desenvolvimento", "Exemplos"],
                            "lin": [
                                ["Editor de código", "Escrever e editar os arquivos do site (HTML, PHP, CSS)", "VS Code (sugestão do curso), Notepad++, Sublime Text"],
                                ["Navegador", "Testar e visualizar o resultado; inspecionar com as DevTools (F12)", "Chrome, Firefox, Edge"],
                                ["Gerenciador de arquivos", "Criar e organizar pastas e arquivos do projeto", "Explorador de Arquivos (Windows), Files (Linux)"],
                                ["Terminal", "Executar comandos de texto: navegar em pastas, criar arquivos", "Prompt de Comando, PowerShell, bash"],
                            ]}),
                ("h", "Editor de código × processador de texto"),
                ("p", "Sites são escritos em <b>texto puro</b>. Um processador de texto (como o Word) adiciona "
                      "formatação invisível que <b>quebra o código</b>. Por isso usamos um <b>editor de código</b>, "
                      "que salva arquivos limpos e ainda ajuda com <b>cores de sintaxe</b>, <b>autocompletar</b> e "
                      "<b>extensões</b>."),
                ("atencao", "Nunca escreva HTML/PHP no Word! Use sempre um editor de código. E atenção às "
                            "extensões: o Windows pode escondê-las — um arquivo <b>index.html</b> deve terminar "
                            "em <b>.html</b>, e não em <b>index.html.txt</b>."),
                ("h", "Estrutura de um projeto Web"),
                ("p", "Todo projeto deve ter sua <b>própria pasta</b>, com os arquivos organizados por tipo. "
                      "Essa organização facilita encontrar arquivos, reutilizar código e hospedar o site:"),
                ("codigo", {"titulo": "Estrutura inicial do projeto (crie no laboratório)", "ling": "texto", "linhas": [
                    "meu-site/",
                    "├── index.html        ← página inicial (sempre 'index'!)",
                    "├── sobre.html",
                    "├── contato.html",
                    "├── imagens/          ← fotos, logos, ícones",
                    "│   └── foto.jpg",
                    "└── css/              ← folhas de estilo (mais adiante)",
                ]}),
                ("conceito", ("Por que a página inicial se chama index?",
                              "O servidor Web procura automaticamente um arquivo chamado <b>index</b> "
                              "(index.html ou index.php) quando alguém acessa o site sem informar a página. "
                              "Por isso a página inicial <b>sempre</b> se chama index.")),
                ("h", "Terminal: comandos essenciais"),
                ("codigo", {"titulo": "Comandos básicos (Windows / Linux)", "ling": "shell", "linhas": [
                    "cd documentos        # entra na pasta 'documentos'  (change directory)",
                    "cd ..                # volta para a pasta anterior",
                    "dir                  # lista arquivos e pastas       (Linux: ls)",
                    "mkdir meu-site       # cria a pasta 'meu-site'",
                    "cd meu-site          # entra na pasta criada",
                ]}),
                ("dica", "No VS Code, use <b>Arquivo → Abrir Pasta</b> e selecione <b>meu-site/</b>: o editor "
                         "mostra toda a estrutura do projeto na barra lateral, e o terminal integrado "
                         "(Ctrl+') já abre dentro da pasta certa."),
            ],
            "slides": {
                "pontos": [
                    "Editor de código: escrever HTML/PHP em texto puro (VS Code)",
                    "Navegador: testar o resultado + DevTools (F12)",
                    "Gerenciador de arquivos: organizar o projeto",
                    "Terminal: cd, dir/ls, mkdir",
                    "Cada projeto tem sua pasta: meu-site/ (index.html, imagens/, css/)",
                ],
                "codigo": {"titulo": "Estrutura do projeto", "linhas": [
                    "meu-site/",
                    "├── index.html   (pagina inicial)",
                    "├── sobre.html",
                    "├── imagens/",
                    "└── css/",
                ]},
                "nota": "Aula 100% prática: todos devem sair com o VS Code instalado, a pasta meu-site/ criada "
                        "e o primeiro arquivo de teste aberto no navegador. Palavra-chave: index = página inicial.",
            },
        },
    ],
    "exercicios": [
        {
            "num": 1, "titulo": "Montando o ambiente", "tipo": "pratico",
            "enunciado": "Prepare seu ambiente de desenvolvimento completo:",
            "passos": [
                "Instale (ou abra) o VS Code e explore: barra lateral, área de edição e terminal integrado;",
                "No terminal, crie a pasta do curso: <b>mkdir programacao-web</b> e entre nela;",
                "Dentro dela, crie a pasta do projeto: <b>mkdir meu-site</b> e entre nela;",
                "Crie a pasta <b>imagens/</b> e um arquivo de teste <b>teste.txt</b>;",
                "Abra a pasta <b>meu-site</b> no VS Code (Arquivo → Abrir Pasta) e confira a estrutura na lateral.",
            ],
            "esperado": "Estrutura: programacao-web/meu-site/ contendo imagens/ e teste.txt, aberta no VS Code.",
            "orientacao": "Circule pela sala conferindo a estrutura de cada aluno. Corrija erros comuns: pasta "
                          "criada no lugar errado, extensão .txt oculta, projeto aberto como arquivo e não como pasta.",
        },
        {
            "num": 2, "titulo": "Explorando o navegador como ferramenta", "tipo": "pratico",
            "enunciado": "Abra qualquer site no navegador, pressione <b>F12</b> (DevTools) e explore:",
            "passos": [
                "Na aba <b>Elements/Elementos</b>, encontre o título da página (tag &lt;title&gt;) e um texto qualquer;",
                "Na aba <b>Network/Rede</b>, recarregue a página e observe as requisições sendo feitas;",
                "Anote: quantas requisições a página fez? Qual foi a primeira?",
            ],
            "esperado": "Aluno localiza o HTML real da página na aba Elementos e observa dezenas de requisições "
                        "(HTML, imagens, CSS, JS) na aba Rede — a primeira normalmente é o documento HTML.",
            "orientacao": "Este exercício ‘abre a cabeça’ do aluno: o que aparece na tela é resultado de código. "
                          "Guarde isso para o módulo de HTML.",
        },
        {
            "num": 3, "titulo": "Desafio — mapa do meu projeto", "tipo": "escrito",
            "enunciado": "Desenhe no caderno a estrutura de pastas que você usará no projeto “Meu Primeiro Site” "
                         "(módulo 4): página inicial, página sobre, página de contato e pasta de imagens. "
                         "Escreva o nome exato de cada arquivo.",
            "esperado": "Árvore com meu-site/ contendo index.html, sobre.html, contato.html e imagens/.",
            "orientacao": "Confira os nomes: index.html (não ‘inicio.html’ ou ‘Home.html’). Nomes sem acento, "
                          "sem espaços e em minúsculas — explique o porquê (servidores e URLs).",
        },
    ],
    "teste_rapido": [
        {"enunciado": "Qual ferramenta é a mais adequada para escrever os arquivos HTML e PHP do projeto?",
         "alt": ["Microsoft Word, por causa do corretor ortográfico.",
                 "Um editor de código, como o VS Code.",
                 "O Bloco de Notas do celular.",
                 "O navegador Chrome."],
         "resposta": 1,
         "comentario": "Código é texto puro: editores de código oferecem cores de sintaxe e autocompletar sem "
                       "inserir formatação invisível (como faz o Word)."},
        {"enunciado": "A página inicial de um site deve se chamar <b>index.html</b> (ou index.php) porque:",
         "alt": ["é uma regra gramatical da linguagem HTML.",
                 "index significa ‘índice’ em latim e soa profissional.",
                 "o servidor Web procura automaticamente esse arquivo ao acessar o site.",
                 "o navegador não abre arquivos com outros nomes."],
         "resposta": 2,
         "comentario": "Ao receber um acesso sem página especificada, o servidor busca index.html/index.php na "
                       "pasta do site."},
        {"enunciado": "No terminal, o comando <b>mkdir imagens</b> serve para:",
         "alt": ["abrir a pasta imagens no navegador.",
                 "criar uma pasta chamada imagens.",
                 "apagar a pasta imagens.",
                 "listar os arquivos da pasta atual."],
         "resposta": 1,
         "comentario": "mkdir = make directory (criar diretório/pasta). Listar arquivos é dir (Windows) ou ls "
                       "(Linux); navegar é cd."},
        {"enunciado": "Por que não se deve usar nomes de arquivo com acentos ou espaços (ex.: “Página Inicial.html”)?",
         "alt": ["Porque o VS Code não salva arquivos assim.",
                 "Porque ocupam mais espaço em disco.",
                 "Porque URLs e servidores tratam acentos/espaços de forma inconsistente, podendo quebrar os links.",
                 "Porque o HTML proíbe letras maiúsculas."],
         "resposta": 2,
         "comentario": "Boa prática: nomes curtos, minúsculos, sem acento, separados por hífen ou sublinhado "
                       "(ex.: pagina-inicial.html)."},
        {"enunciado": "As DevTools do navegador (tecla F12) permitem, entre outras coisas:",
         "alt": ["editar o código HTML exibido da página e ver as requisições de rede.",
                 "criar novas pastas no projeto automaticamente.",
                 "registrar domínios gratuitamente.",
                 "traduzir o site para outro idioma."],
         "resposta": 0,
         "comentario": "As DevTools mostram o HTML recebido, permitem inspecionar elementos, ver a rede, o "
                       "console e muito mais — são a principal ferramenta de teste do desenvolvedor."},
    ],
    "avaliacao_ref": None,
}

MODULOS = [MODULO_1, MODULO_2]
