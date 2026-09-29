# -*- coding: utf-8 -*-
"""Gera 2 PDFs de tutorial de instalação:
   1) Tutorial do ALUNO (instalacao guiada pelo professor)
   2) Tutorial da TI (laboratorio: instalacao em massa, validacao e suporte)
Reutiliza o motor de diagramação de build_pdf.py.
Uso: python3 build_tutoriais.py
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, NextPageTemplate, KeepTogether, HRFlowable)

from build_pdf import (MyDoc, normal_page, _paint_navy, P, S, safe_para, plain, make_box,
                       make_code, make_table, band, rounded, big_section, NAVY, NAVY2, PRIMARY,
                       SKY, AMBER, AMBER_BG, AMBER_D, INK, INK_SOFT, LINE, ROW_ALT,
                       PAGE_W, PAGE_H, ML, MR, MT, MB, TW)

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------
def checklist(items, titulo="Checklist"):
    rows = [[Paragraph("", S["td"]), Paragraph(safe_para(t), S["td"])] for t in items]
    t = Table(rows, colWidths=[0.75 * cm, TW - 0.75 * cm])
    cmds = [("GRID", (0, 0), (0, -1), 0.9, NAVY),
            ("LINEBELOW", (1, 0), (1, -2), 0.4, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("BACKGROUND", (0, 0), (0, -1), ROW_ALT)]
    t.setStyle(TableStyle(cmds))
    return [P(f"<b>{titulo}</b>", S["h2"]), t, Spacer(1, 8)]

def capa(titulo, subtitulo, selo, selo_bg):
    cell = [
        Spacer(1, 0.5 * cm),
        Paragraph("CURSO TÉCNICO EM INFORMÁTICA · PROGRAMAÇÃO PARA INTERNET I · TURMA 2/2026",
                  ParagraphStyle("ck", fontName="Inter-Bk", fontSize=9.5, leading=13, textColor=AMBER)),
        Spacer(1, 0.5 * cm),
        Paragraph(titulo, ParagraphStyle("ct", fontName="Inter-Bk", fontSize=33, leading=39,
                                         textColor=white)),
        Spacer(1, 0.4 * cm),
        HRFlowable(width="32%", thickness=3.4, color=AMBER, hAlign="LEFT", spaceAfter=14),
        Paragraph(subtitulo, ParagraphStyle("cs", fontName="Inter-Md", fontSize=12.5, leading=17,
                                            textColor=HexColor("#C9DCF2"))),
        Spacer(1, 1.2 * cm),
    ]
    stamp = rounded([[Paragraph(selo, ParagraphStyle("st", fontName="Inter-Bk", fontSize=11.5,
                                                     leading=15, textColor=NAVY))]],
                    [TW * 0.8], selo_bg, radius=8, pad=10)
    cell += [stamp, Spacer(1, 0.8 * cm),
             Paragraph("Material de apoio da disciplina · baseado no Plano de Ensino e no "
                       "Cronograma oficiais · todos os softwares citados são gratuitos.",
                       ParagraphStyle("ft", fontName="Inter-Md", fontSize=8.6, leading=12.5,
                                      textColor=HexColor("#9FBBD9")))]
    t = Table([[cell]], colWidths=[TW])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return [t, NextPageTemplate("normal"), PageBreak()]

def make_onpage(label, header="PROGRAMAÇÃO PARA INTERNET I — TUTORIAL DE INSTALAÇÃO",
                centro="Softwares gratuitos · baixe apenas dos sites oficiais indicados"):
    from reportlab.lib.colors import HexColor as HC
    def onpage(c, doc):
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, PAGE_H - 0.28 * cm, PAGE_W, 0.28 * cm, stroke=0, fill=1)
        c.setFillColor(AMBER)
        c.rect(0, PAGE_H - 0.36 * cm, PAGE_W * 0.32, 0.08 * cm, stroke=0, fill=1)
        c.setFont("Inter-Sb", 7.3)
        c.setFillColor(INK_SOFT)
        c.drawString(ML, PAGE_H - 0.95 * cm, header)
        c.setFont("Inter-Md", 7.3)
        c.drawRightString(PAGE_W - MR, PAGE_H - 0.95 * cm,
                          "CURSO TÉCNICO EM INFORMÁTICA · TURMA 2/2026")
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        c.line(ML, PAGE_H - 1.18 * cm, PAGE_W - MR, PAGE_H - 1.18 * cm)
        c.line(ML, MB - 0.45 * cm, PAGE_W - MR, MB - 0.45 * cm)
        c.setFont("Inter-Md", 7.6)
        c.setFillColor(INK_SOFT)
        c.drawString(ML, MB - 0.95 * cm, label)
        c.drawCentredString(PAGE_W / 2 + 1.2 * cm, MB - 0.95 * cm, centro)
        c.setFillColor(NAVY)
        c.circle(PAGE_W - MR - 0.35 * cm, MB - 0.82 * cm, 0.34 * cm, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Inter-Bd", 8.6)
        c.drawCentredString(PAGE_W - MR - 0.35 * cm, MB - 0.95 * cm, str(doc.page))
        c.restoreState()
    return onpage


def build_doc(out_path, story_fn, label="", header=None, centro=None):
    doc = MyDoc(out_path, pagesize=A4, leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
                title="Tutorial de Instalação — Programação para Internet I",
                author="Curso Técnico em Informática — Turma 2/2026")
    doc.professor = False
    frame_normal = Frame(ML, MB, TW, PAGE_H - MT - MB, id="normal", leftPadding=0, rightPadding=0,
                         topPadding=0, bottomPadding=0)
    frame_big = Frame(ML, MB, TW, PAGE_H - 2.2 * cm - MB, id="big", leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="capa", frames=[frame_big], onPage=_paint_navy),
        PageTemplate(id="normal", frames=[frame_normal],
                       onPage=make_onpage(label, header or "PROGRAMAÇÃO PARA INTERNET I — TUTORIAL DE INSTALAÇÃO",
                                            centro or "Softwares gratuitos · baixe apenas dos sites oficiais indicados")),
    ])
    story = story_fn()
    doc.build(story)
    print("OK:", out_path)

# ---------------------------------------------------------------------------
# TUTORIAL 1 — ALUNO (guiado pelo professor)
# ---------------------------------------------------------------------------
def story_aluno():
    st = []
    st += capa("Kit de Preparação<br/>do Ambiente",
               "Tutorial de instalação passo a passo — VS Code, navegador com DevTools, "
               "XAMPP (servidor PHP) e pastas do curso. Para ser seguido pelo aluno, "
               "conduzido pelo professor em sala.",
               "VERSÃO DO ALUNO · COM NOTAS PARA O PROFESSOR", HexColor("#9CC3EC"))

    st += big_section("Como usar este tutorial", "Planejamento · ritmo · combinação de telas", page_break=False)
    st.append(P("Este guia instala, em <b>duas aulas de 50 minutos</b>, todo o ambiente usado no curso. "
                "Siga a ordem: cada passo testa o anterior. Trabalhe em <b>duplas</b>: quem termina primeiro "
                "ajuda a dupla vizinha (monitoria espontânea).", S["body"]))
    st.extend(make_table({"cab": ["Aula", "O que instalar", "Tempo estimado"],
                          "lin": [["Aula A", "VS Code + extensões · Navegador + DevTools · pasta do curso",
                                   "≈ 40 min + testes"],
                                  ["Aula B", "XAMPP (servidor PHP) · primeiro ola.php · checklist final",
                                   "≈ 35 min + testes"]],
                          "larguras": [2.0, 11.0, 4.0]}))
    st.append(make_box("dica", "Projete este PDF (ou os passos no quadro) e execute junto com a turma, "
                       "um passo por vez. Antes da aula, baixe os instaladores no servidor da escola "
                       "(pasta rede) — assim ninguém depende da internet durante a instalação.",
                       title="PARA O PROFESSOR — ANTES DA AULA"))
    st.append(make_box("atencao", "Baixe softwares <b>somente dos sites oficiais</b> listados aqui. Sites de "
                       "“download rápido” costumam embutir propaganda ou programas indesejados."))

    # ---------------- VS CODE ----------------
    st += big_section("1 · VS Code — o editor de código", "Parte II em diante · gratuito · Windows")
    st.append(make_box("conceito", "O <b>Visual Studio Code (VS Code)</b> é o editor de código do curso: "
                       "gratuito, leve e com recursos que ensinam junto — cores de sintaxe, autocompletar, "
                       "terminal integrado e extensões. Sites são escritos em <b>texto puro</b>: nunca use "
                       "Word ou similares.", title="O QUE É E POR QUE USAMOS"))
    st.append(P("<b>Passo a passo da instalação</b>", S["h2"]))
    st.extend([Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;{safe_para(t)}", S["li_num"]) for i, t in enumerate([
        "No navegador, acesse o site oficial: <b>code.visualstudio.com</b> e clique no botão azul "
        "<b>Download for Windows</b>;",
        "Abra o arquivo baixado (VSCodeUserSetup…exe). Se o Windows perguntar, responda <b>Sim</b>;",
        "Aceite o contrato e clique em <b>Avançar</b> duas vezes;",
        "Na tela <b>Selecionar tarefas adicionais</b>, MARQUE: <b>“Add to PATH”</b> e "
        "<b>“Register Code as an editor for supported file types”</b> (deixe as demais como estão);",
        "Clique em <b>Instalar</b> e depois em <b>Concluir</b>;",
        "Abra o VS Code pelo menu Iniciar (digite “code”).",
    ], 1)])
    st.append(P("<b>Tour rápido pela interface (2 min)</b>", S["h2"]))
    st.extend([Paragraph("•&nbsp;&nbsp;" + safe_para(t), S["li"]) for t in [
        "<b>Barra lateral esquerda</b>: Explorador de arquivos (o projeto inteiro em árvore);",
        "<b>Área central</b>: onde o código é escrito;",
        "<b>Terminal integrado</b>: menu Terminal → Novo Terminal (ou Ctrl+');",
        "<b>Barra de status (rodapé azul)</b>: idioma do arquivo, linha/coluna, notificações.",
    ]])
    st.append(P("<b>Extensões obrigatórias do curso</b> (Ctrl+Shift+X → pesquisar → Install)", S["h2"]))
    st.extend(make_table({"cab": ["Extensão", "Para que serve"],
                          "lin": [["<b>Live Server</b> (Ritwick Dey)",
                                   "Abre o HTML no navegador e recarrega sozinho a cada Ctrl+S"],
                                  ["<b>Portuguese (Brazil) Language Pack</b>",
                                   "Deixa o VS Code em português"],
                                  ["<b>Auto Close Tag</b>", "Fecha tags HTML automaticamente (</p> etc.)"],
                                  ["<b>Auto Rename Tag</b>", "Renomeia o par da tag quando você edita uma"]],
                          "larguras": [6.5, 10.5]}))
    st.append(P("<b>Ajustes finais</b>: Arquivo → Preferências → Configurações: ative <b>Auto Save</b>; "
                "aumente o zoom com Ctrl+ = até ficar legível no projetor; escolha um tema escuro "
                "(melhor contraste em sala).", S["body"]))
    st.append(make_code({"titulo": "Teste do editor (terminal integrado do VS Code)", "ling": "shell",
                         "linhas": ["code --version        # deve mostrar a versão instalada",
                                    "mkdir teste-vscode    # cria uma pasta pelo terminal",
                                    "cd teste-vscode",
                                    "code .                # abre a pasta no VS Code"]}))
    st.extend(make_table({"titulo": "Erros comuns e soluções",
                          "cab": ["Sintoma", "Causa provável", "Solução"],
                          "lin": [["“code não é reconhecido” no terminal",
                                   "PATH não marcado na instalação",
                                   "Feche e abra o terminal (ou o PC); ou reinstale marcando Add to PATH"],
                                  ["Extensão não aparece após instalar",
                                   "Falta recarregar a janela",
                                   "Ctrl+Shift+P → “Reload Window”"],
                                  ["Instalador baixado com nome estranho/anúncios",
                                   "Site não oficial",
                                   "Apague e baixe de novo em code.visualstudio.com"]],
                          "larguras": [5.5, 4.5, 7.0]}))
    st.append(make_box("dica", "Cronometre 15 min para instalação + extensões. Duplas que terminarem viram "
                       "“equipe de apoio”. Confirme visualmente o terminal funcionando em cada máquina.",
                       title="PARA O PROFESSOR — RITMO"))

    # ---------------- NAVEGADOR ----------------
    st += big_section("2 · Navegador + DevTools", "Todas as partes · Chrome ou Firefox")
    st.append(P("O navegador é nossa <b>ferramenta de teste</b> e o “laboratório” da Parte I (como a Web "
                "funciona). Atualize-o e aprenda a abrir as DevTools:", S["body"]))
    st.extend([Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;{safe_para(t)}", S["li_num"]) for i, t in enumerate([
        "Abra o navegador e atualize: Chrome → Menu ⋮ → Ajuda → Sobre o Google Chrome "
        "(Firefox → Menu ☰ → Ajuda → Sobre);",
        "Pressione <b>F12</b> para abrir as Ferramentas do Desenvolvedor;",
        "Conheça 3 abas: <b>Elements/Elementos</b> (o HTML real da página), <b>Network/Rede</b> "
        "(cada requisição feita) e <b>Console</b> (mensagens e erros);",
        "Teste: abra um portal de notícias, deixe a aba <b>Rede</b> aberta e recarregue (F5) — conte "
        "quantas requisições a página faz;",
        "Use <b>Ctrl+U</b> para ver o código-fonte HTML recebido (na Parte III, provará que o PHP "
        "“some” no servidor).",
    ], 1)])
    st.append(make_box("dica", "Demonstre a aba Rede no projetor antes dos alunos testarem: é o momento "
                       "“uau” da aula 2 (requisição × resposta).", title="PARA O PROFESSOR"))

    # ---------------- PASTAS ----------------
    st += big_section("3 · Pasta do curso no computador", "Organização padrão do semestre")
    st.append(P("Todo o trabalho do semestre vive dentro de UMA pasta, com subpastas por projeto "
                "(padrão do módulo 2 da apostila):", S["body"]))
    st.append(make_code({"titulo": "Crie pelo terminal do VS Code (ou pelo Explorador de Arquivos)",
                         "ling": "shell",
                         "linhas": ["cd Documents", "mkdir programacao-web",
                                    "cd programacao-web", "mkdir meu-site",
                                    "cd meu-site", "mkdir imagens css includes",
                                    "code .          # abre a pasta do projeto no VS Code"]}))
    st.append(P("Crie um <b>atalho</b> da pasta programacao-web na Área de Trabalho (botão direito → "
                "Enviar para → Área de Trabalho).", S["body"]))

    # ---------------- XAMPP ----------------
    st += big_section("4 · XAMPP — o servidor que executa PHP", "Parte III em diante · gratuito")
    st.append(make_box("conceito", "O <b>XAMPP</b> instala o <b>Apache</b> (servidor Web) + <b>PHP</b> + "
                       "<b>MySQL</b> no seu computador. Com ele, sua máquina vira um “servidor de verdade”: "
                       "os arquivos colocados na pasta <b>htdocs</b> ficam acessíveis em "
                       "<b>http://localhost/…</b>. Sem servidor, PHP <b>não executa</b>.",
                       title="O QUE É E POR QUE USAMOS"))
    st.extend([Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;{safe_para(t)}", S["li_num"]) for i, t in enumerate([
        "Baixe no site oficial <b>apachefriends.org</b> (botão “XAMPP for Windows”);",
        "Execute o instalador; se o Windows Defender/antivírus alertar, permita (é seguro e oficial);",
        "Se aparecer aviso de <b>UAC</b> (Controle de Conta de Usuário), clique em OK — evite instalar "
        "dentro de “Arquivos de Programas”;",
        "Aceite os componentes padrão (Apache, MySQL, PHP…) e a pasta sugerida <b>C:\\xampp</b>;",
        "Avance até <b>Concluir</b> e marque para abrir o <b>Painel de Controle</b>;",
        "No painel, clique em <b>Start</b> na linha <b>Apache</b> — o módulo fica <b>verde</b>;",
        "Abra o navegador e acesse <b>http://localhost</b> — deve aparecer o painel do XAMPP.",
    ], 1)])
    st.append(P("<b>Primeiro programa PHP (o teste que vale ouro)</b>", S["h2"]))
    st.extend([Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;{safe_para(t)}", S["li_num"]) for i, t in enumerate([
        "No VS Code: Arquivo → Abrir Pasta → <b>C:\\xampp\\htdocs</b>;",
        "Crie a pasta <b>meu-site</b> e, dentro dela, o arquivo <b>ola.php</b> com o código abaixo;",
        "Salve (Ctrl+S) e acesse <b>http://localhost/meu-site/ola.php</b>;",
        "Se apareceu “Olá, mundo! do servidor” — <b>seu ambiente PHP está pronto!</b>",
    ], 1)])
    st.append(make_code({"titulo": "htdocs/meu-site/ola.php", "ling": "php",
                         "linhas": ["<?php", "    echo \"<h1>Olá, mundo! do servidor</h1>\";",
                                    "    echo \"<p>Hoje é \" . date(\"d/m/Y\") . \".</p>\";",
                                    "?>"]}))
    st.append(make_box("atencao", "Nunca abra o .php com <b>dois cliques</b> (file://): o PHP não executa. "
                       "O endereço certo começa sempre com <b>http://localhost/</b>."))
    st.extend(make_table({"titulo": "Erros comuns e soluções",
                          "cab": ["Sintoma", "Causa provável", "Solução"],
                          "lin": [["Apache não inicia (fica vermelho)",
                                   "Porta 80 ocupada (Skype, IIS, outro servidor)",
                                   "Feche o programa conflitante; ou no XAMPP: Config → httpd.conf → "
                                   "troque “Listen 80” por “Listen 8080” e acesse localhost:8080"],
                                  ["Antivírus bloqueia o Apache",
                                   "Defender/tratando Apache como risco",
                                   "Adicionar exclusão da pasta C:\\xampp nas configurações do antivírus"],
                                  ["localhost não abre nada",
                                   "Apache parado",
                                   "Painel do XAMPP → Start no Apache (verde = ok)"],
                                  ["Página em branco",
                                   "Erro de sintaxe PHP",
                                   "Olhe a mensagem de erro (arquivo + linha) e corrija o ; ou aspas"]],
                          "larguras": [4.6, 4.6, 7.8]}))
    st.append(make_box("dica", "Alternativas válidas se o XAMPP der trabalho no laboratório: <b>Laragon</b> "
                       "(mais leve) ou o servidor embutido do PHP — na pasta do projeto: "
                       "<b>C:\\xampp\\php\\php -S localhost:8000</b> e acesse localhost:8000.",
                       title="PLANO B"))
    st.append(make_box("dica", "Aula B inteira para XAMPP + ola.php. Circule conferindo o “verde” do Apache "
                       "e o ola.php abrindo em cada máquina. Quem terminar, faça o desafio: exibir nome e "
                       "hora com date(\"H:i\").", title="PARA O PROFESSOR — RITMO"))

    # ---------------- CHECKLIST ----------------
    st += big_section("5 · Checklist final — “meu ambiente está pronto”", "Assinale (ou peça o visto do professor)")
    st.extend(checklist([
        "VS Code instalado e abrindo pelo menu Iniciar;",
        "Extensões instaladas: Live Server, Language Pack pt-BR, Auto Close Tag, Auto Rename Tag;",
        "Terminal integrado abre (Ctrl+') e responde a comandos;",
        "Pasta Documents/programacao-web/meu-site criada (com imagens/, css/, includes/);",
        "Navegador atualizado; F12 abre as DevTools (abas Elements, Network, Console);",
        "XAMPP instalado; Apache inicia e fica VERDE no painel;",
        "http://localhost abre o painel do XAMPP;",
        "http://localhost/meu-site/ola.php exibe “Olá, mundo! do servidor” com a data de hoje;",
        "Atalho da pasta do curso na Área de Trabalho;",
        "Apostila (PDF) e o QuizWeb salvos na pasta do curso ou no Drive da turma.",
    ], "Marque cada item concluído"))
    st.append(P("<b>Exercícios de aquecimento</b> (apostila): aula 5 (ambiente e pastas), aula 6 (primeiro "
                "HTML com Live Server) e aula 20 (primeiro PHP). Seu ambiente novo é exatamente o que eles "
                "pedem. Bons estudos!", S["body"]))
    return st

# ---------------------------------------------------------------------------
# TUTORIAL 2 — TI
# ---------------------------------------------------------------------------
def story_ti():
    st = []
    st += capa("Guia do Laboratório<br/>para a Equipe de TI",
               "Instalação, configuração e validação do ambiente da disciplina Programação para "
               "Internet I (VS Code, XAMPP, navegadores e materiais didáticos) — incluindo "
               "implantação em massa e solução de problemas.",
               "VERSÃO TÉCNICA · TI / COORDENAÇÃO", AMBER)

    st += big_section("1 · Escopo e requisitos", "O que será instalado e o que cada máquina precisa", page_break=False)
    st.extend(make_table({"cab": ["Software", "Versão sugerida", "Licença", "Espaço", "Função no curso"],
                          "lin": [["Visual Studio Code", "Última estável (User ou System Installer)",
                                   "Gratuita (Microsoft)", "~350 MB", "Editor de código (HTML/PHP)"],
                                  ["XAMPP", "8.x (PHP 8.x + Apache 2.4)", "Gratuita (Apache Friends)",
                                   "~2,5 GB", "Servidor local p/ PHP (localhost)"],
                                  ["Chrome ou Firefox", "Canal estável atualizado", "Gratuita",
                                   "—", "Testes + DevTools"],
                                  ["Materiais da disciplina", "Apostilas PDF, PPTX e QuizWeb.html",
                                   "Uso interno", "~5 MB", "Conteúdo das aulas"]],
                          "larguras": [3.6, 4.6, 3.0, 1.8, 4.0]}))
    st.extend(make_table({"titulo": "Requisitos mínimos por estação",
                          "cab": ["Item", "Mínimo", "Recomendado"],
                          "lin": [["Sistema", "Windows 10 x64", "Windows 10/11 x64"],
                                  ["RAM", "4 GB", "8 GB"],
                                  ["Disco livre", "10 GB", "20 GB (SSD)"],
                                  ["Rede", "Não obrigatória (ambiente offline funciona)",
                                   "Internet p/ módulos 1 e quizzes on-line"],
                                  ["Permissões", "Admin local p/ instalação",
                                   "Admin ou imagem pré-instalada"]],
                          "larguras": [3.5, 6.5, 7.0]}))
    st.append(make_box("conceito", "Estratégia recomendada: preparar <b>uma máquina-padrão (“gold”)</b> com "
                       "tudo instalado e testado e <b>clonar a imagem</b> para as demais (ferramenta de imageamento "
                       "da escola). Alternativas: script de instalação silenciosa por máquina (seção 3) ou "
                       "<b>kit portátil</b> em pen drive/servidor (VS Code portable + XAMPP portable) como plano B.",
                       title="ESTRATÉGIA DE IMPLANTAÇÃO"))

    st += big_section("2 · Preparação (antes de instalar)", "Downloads, exclusões e pasta de distribuição")
    st.extend(checklist([
        "Baixar instaladores OFFLINE uma única vez e colocar no compartilhamento da rede "
        "(ex.: \\\\servidor\\ti\\pi1\\): VSCodeUserSetup-x64.exe, xampp-windows-x64-8.x-installer.exe;",
        "Criar pasta de materiais \\\\servidor\\ti\\pi1\\materiais\\ com os 2 PDFs da apostila, o PPTX "
        "e o QuizWeb.html;",
        "No Defender/antivírus: adicionar exclusão de pasta C:\\xampp (evita bloqueio do Apache);",
        "Confirmar porta 80 livre nas estações (sem IIS/Skype/Outlook Web ativados como serviço);",
        "Garantir perfil de usuário com permissão de escrita em Documents e Área de Trabalho;",
        "Anotar patrimônio/hostname das estações do laboratório-alvo.",
    ], "Pré-instalação"))

    st += big_section("3 · Instalação em massa (silenciosa)", "Comandos para script/GPO ou execução manual")
    st.append(P("<b>VS Code (System/MSI ou EXE silencioso)</b>", S["h2"]))
    st.append(make_code({"titulo": "Instalação silenciosa do VS Code (admin)", "ling": "shell",
                         "linhas": ["REM opção A — instalador EXE silencioso:",
                                    "VSCodeUserSetup-x64.exe /VERYSILENT /MERGETASKS=\"addtopath,registereditor,!runcode\"",
                                    "",
                                    "REM opção B — MSI (GPO/SCCM):",
                                    "msiexec /i VSCodeSetup-x64.msi /quiet"]}))
    st.append(P("<b>Extensões</b> — a instalação é <b>por perfil de usuário</b>; execute no logon do aluno "
                "(script de logon GPO) ou uma vez por perfil:", S["body"]))
    st.append(make_code({"titulo": "extensoes.bat (executar na sessão do usuário)", "ling": "shell",
                         "linhas": ["code --install-extension ritwickdey.liveserver",
                                    "code --install-extension ms-ceintl.vscode-language-pack-pt-br",
                                    "code --install-extension formulahendry.auto-close-tag",
                                    "code --install-extension formulahendry.auto-rename-tag"]}))
    st.append(P("<b>XAMPP silencioso</b> (componentes padrão; instala em C:\\xampp):", S["h2"]))
    st.append(make_code({"titulo": "Instalação silenciosa do XAMPP (admin)", "ling": "shell",
                         "linhas": ["xampp-windows-x64-8.x-installer.exe --mode unattended --unattendedmodeui none",
                                    "REM ou instalador Inno: /VERYSILENT /SUPPRESSMSGBOXES"]}))
    st.append(make_box("atencao", "Não instale o Apache como <b>serviço automático</b> por padrão no "
                       "laboratório: conflitos de porta e travamentos de imagem são mais simples de tratar "
                       "com o Apache iniciado pelo Painel (ou sob demanda). Se preferir serviço: "
                       "C:\\xampp\\apache\\apache_install.bat com conta LocalSystem."))
    st.append(P("<b>Materiais didáticos</b>: copiar para C:\\aulas\\pi1\\ em cada estação (ou mapear unidade "
                "de rede) e criar atalho na Área de Trabalho “PI-I” apontando para a pasta.", S["body"]))

    st += big_section("4 · Validação pós-instalação", "Script de teste + conferência visual")
    st.append(make_code({"titulo": "valida-pi1.bat — rodar em cada estação (ou via GPO startup)", "ling": "shell",
                         "linhas": ["@echo off",
                                    "echo [1/4] VS Code:", "code --version",
                                    "echo [2/4] PHP do XAMPP:", "C:\\xampp\\php\\php -v",
                                    "echo [3/4] Apache responde?",
                                    "powershell -Command \"try{(Invoke-WebRequest -UseBasicParsing http://localhost/).StatusCode}catch{'APACHE PARADO'}\"",
                                    "echo [4/4] Extensões:",
                                    "code --list-extensions | findstr /i \"liveserver pt-br auto-close\"",
                                    "pause"]}))
    st.extend(checklist([
        "code --version retorna versão;",
        "php -v retorna PHP 8.x (caminho C:\\xampp\\php);",
        "http://localhost responde 200 (ou iniciar Apache e retestar);",
        "As 4 extensões aparecem no code --list-extensions do perfil do aluno;",
        "Arquivos de C:\\aulas\\pi1 abrem (PDFs, PPTX, QuizWeb.html);",
        "Teste funcional: C:\\xampp\\htdocs\\teste.php com <?php phpinfo(); ?> abre em localhost/teste.php;",
        "F12 abre DevTools no navegador padrão;",
        "Registro na ficha de entrega (seção 6).",
    ], "Conferência por estação"))

    st += big_section("5 · Solução de problemas", "Ocorrências típicas de laboratório")
    st.extend(make_table({"cab": ["Problema", "Diagnóstico", "Ação"],
                          "lin": [["Apache não inicia (porta 80 ocupada)",
                                   "netstat -ano | findstr :80 mostra outro PID (IIS/Skype)",
                                   "Desativar o serviço conflitante OU mudar para Listen 8080 no httpd.conf "
                                   "(ajustar atalhos/materiais p/ localhost:8080)"],
                                  ["Defender quarentena arquivos do Apache",
                                   "Histórico de proteção do Defender",
                                   "Restaurar + exclusão de C:\\xampp; redistribuir via GPO"],
                                  ["php não reconhecido no CMD do aluno",
                                   "PHP fora do PATH",
                                   "Adicionar C:\\xampp\\php ao PATH da máquina (ou usar caminho completo nos roteiros)"],
                                  ["Extensões não aparecem p/ novo aluno",
                                   "Extensões são por perfil",
                                   "Script de logon GPO com code --install-extension (seção 3)"],
                                  ["Estação clonada sem atalhos/materiais",
                                   "Imagem gold sem C:\\aulas",
                                   "Incluir C:\\aulas\\pi1 na imagem ou script de cópia pós-clone"],
                                  ["Laboratório sem internet no dia",
                                   "Rede indisponível",
                                   "Ambiente funciona 100% offline (localhost); usar QuizWeb.html local e "
                                   "capturas de registro.br salvas na pasta de materiais"]],
                          "larguras": [4.4, 4.6, 8.0]}))
    st.append(make_box("dica", "Mantenha um <b>pen drive “kit PI-I”</b> com: instaladores offline, "
                       "extensoes.bat, valida-pi1.bat, materiais e uma cópia portable do XAMPP. Ele resolve "
                       "90% das ocorrências em sala sem chamar a TI ao laboratório.",
                       title="KIT DE EMERGÊNCIA"))

    st += big_section("6 · Termo de entrega do laboratório", "Registro por estação (imprimir ou copiar)")
    rows = [["Nº/Patrimônio", "Hostname", "VS Code", "XAMPP/Apache", "Materiais", "Visto TI", "Data"]]
    for i in range(1, 9):
        rows.append([str(i), "", "(  ) ok", "(  ) ok", "(  ) ok", "", "____ / ____ / 2026"])
    t = Table([[Paragraph(c, S["th"]) for c in rows[0]]] +
              [[Paragraph(c if c else "&nbsp;", S["td"]) for c in r]
               for r in rows[1:]],
              colWidths=[2.2 * cm, 2.6 * cm, 1.7 * cm, 2.6 * cm, 2.0 * cm, 2.2 * cm, 3.7 * cm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY),
                           ("GRID", (0, 0), (-1, -1), 0.6, LINE),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("TOPPADDING", (0, 0), (-1, -1), 6),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    st.append(t)
    st.append(Spacer(1, 8))
    st.append(P("Observações: ______________________________________________________________"
                "________________________________________________________________", S["body_c"]))
    st.append(make_box("conceito", "Dúvidas pedagógicas (o que cada software ensina, ordem dos módulos, "
                       "projetos) estão no “Guia de softwares por tópico” conversado com a docente e na "
                       "apostila da disciplina — este guia cuida apenas da infraestrutura.",
                       title="INTERFACE COM A DOCÊNCIA"))
    return st

if __name__ == "__main__":
    build_doc(os.path.join(_ROOT, "output", "Tutorial_Instalacao_ALUNO_Programacao_para_Internet_I.pdf"),
              story_aluno, label="GUIA DO ALUNO · INSTALAÇÃO GUIADA PELO PROFESSOR")
    build_doc(os.path.join(_ROOT, "output", "Tutorial_Instalacao_TI_Laboratorio_Programacao_para_Internet_I.pdf"),
              story_ti, label="GUIA TÉCNICO · TI / COORDENAÇÃO DO LABORATÓRIO")
