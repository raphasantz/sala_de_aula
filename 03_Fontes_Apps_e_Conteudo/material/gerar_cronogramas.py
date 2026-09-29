# -*- coding: utf-8 -*-
"""Preenche o CRONOGRAMA DE AULA - MODELO com datas reais do calendário escolar,
para as duas disciplinas (PI-I e LP2), nos formatos DOCX (modelo oficial) e PDF."""
import datetime as dt
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "output")

# ------------------------------------------------------------ calendário
FERIADOS = {  # dias SEM aula (seg-sex) entre 14/09/2026 e o fim estendido
    dt.date(2026, 10, 12), dt.date(2026, 10, 13), dt.date(2026, 11, 2),
    dt.date(2026, 11, 20), dt.date(2026, 12, 25), dt.date(2026, 12, 30),
    dt.date(2026, 12, 28), dt.date(2026, 12, 29), dt.date(2026, 12, 31),
    dt.date(2027, 2, 8), dt.date(2027, 2, 9), dt.date(2027, 2, 10),
    dt.date(2027, 3, 24), dt.date(2027, 3, 25), dt.date(2027, 3, 26),
    dt.date(2027, 4, 21),
}
INICIO = dt.date(2026, 9, 14)
FIM_MAX = dt.date(2027, 4, 30)
DIA_NOME = {0: "segunda", 1: "terça", 2: "quarta", 3: "quinta", 4: "sexta",
            5: "sábado", 6: "domingo"}

def datas_validas():
    d = INICIO
    while d <= FIM_MAX:
        if d.weekday() <= 4 and d not in FERIADOS:
            if not (dt.date(2026, 12, 25) <= d <= dt.date(2027, 1, 31)):
                yield d
        d += dt.timedelta(days=1)

def slots_semanas(dias_semana, aulas_por_dia, total):
    """Retorna (datas, semanas) onde semanas = lista de listas de datas (slots)."""
    semanas = []
    for d in datas_validas():
        if d.weekday() in dias_semana:
            if not semanas or (d - semanas[-1][-1]).days > 3:
                semanas.append([])
            semanas[-1].append(d)
    datas = []
    semanas_slots = []
    for wk in semanas:
        wk_slots = []
        for d in wk:
            for _ in range(aulas_por_dia[d.weekday()]):
                if len(datas) < total:
                    wk_slots.append(d)
                    datas.append(d)
        if wk_slots:
            semanas_slots.append(wk_slots)
    return datas, semanas_slots

# PI-I: segunda (1 aula) + terça (2 aulas) = 3/semana → 72 aulas
PI1_DATAS, PI1_SEM = slots_semanas({0: 1, 1: 2}, {0: 1, 1: 2}, 72)
# LP2: quarta (2) + sexta (2) = 4/semana → 96 aulas
LP2_DATAS, LP2_SEM = slots_semanas({2: 2, 4: 2}, {2: 2, 4: 2}, 96)

# ------------------------------------------------------------ temas PI-I (72)
PI1_TEMAS = [
    "O que é a Internet? Redes, Internet × Web, cliente/servidor e navegador",
    "Como a Web funciona: requisição/resposta, HTTP/HTTPS, anatomia da URL",
    "Domínio, hospedagem e servidor Web: IP, DNS, provedores",
    "Portais, e-business e e-commerce; fluxo da loja virtual",
    "Ambiente de desenvolvimento: VS Code, pastas do projeto, terminal",
    "Primeiro documento HTML5: DOCTYPE, head, body, title",
    "Estrutura do HTML: elementos, tags, atributos, elementos vazios",
    "Cabeçalhos h1–h6, parágrafos, br e hr",
    "Formatação de textos: strong, em, mark, small (semântica)",
    "Links: a href, internos/externos, target; início do Meu Primeiro Site",
    "Imagens: img src/alt, caminhos relativos, formatos",
    "Listas: ul, ol, dl e aninhamento",
    "Tabelas: table, tr, th, td",
    "Tabelas na prática: thead/tbody/tfoot, colspan",
    "Formulários: form, label, input (text, email, password, number, date)",
    "Formulários na prática: cadastro de aluno (radio, checkbox)",
    "Select, textarea e buttons",
    "Projeto HTML: site da empresa fictícia — ENTREGA A1 (10 pts)",
    "O que é PHP: lado do servidor, XAMPP, localhost",
    "Primeiro programa PHP: blocos <?php ?>, echo",
    "PHP + HTML: conteúdo dinâmico no mesmo arquivo",
    "Variáveis: $, atribuição, constantes",
    "Tipos de dados e var_dump()",
    "Operadores aritméticos e concatenação — TESTE ESCRITO-PRÁTICO A1 (15 pts)",
    "Operadores de comparação: == × ===",
    "Operadores lógicos &&, ||, !",
    "Estrutura IF",
    "IF / ELSE / ELSEIF: situação do aluno",
    "SWITCH: case, break, default",
    "Laço for: contagem e tabuada",
    "WHILE: teste antes, laço infinito",
    "DO WHILE: executa e testa depois",
    "Arrays indexados: declaração e acesso",
    "Foreach: percorrendo arrays",
    "Arrays associativos: chave => valor",
    "Revisão cumulativa de PHP + projeto cadastro simples",
    "GET: dados na URL, $_GET",
    "POST: corpo da requisição, $_POST",
    "Validação: isset(), empty(), campos obrigatórios",
    "Sanitização: htmlspecialchars() e segurança (XSS)",
    "Formulário completo com confirmação",
    "Projeto: cadastro de alunos (cadastro + processar)",
    "Organização de arquivos: css/, imagens/, includes/",
    "Include: cabeçalho e rodapé reutilizáveis",
    "Funções: function, parâmetros, return",
    "Funções na prática: média, maioridade, desconto",
    "Arrays multidimensionais e foreach aninhado",
    "Projeto: listagem dinâmica — AVALIAÇÃO 2 (30 pts)",
    "Projeto final: definição, grupos e tema",
    "Requisitos do projeto: objetivo, usuários, funcionalidades",
    "Estrutura do projeto: pastas e arquivos",
    "Página inicial e menu do sistema",
    "Página de cadastro: formulário completo",
    "Processamento: formulário → validação → resultado",
    "Listagem dinâmica com foreach",
    "Melhorando a interface e navegação",
    "Validação do projeto: campos vazios e inválidos",
    "Testes: tabela teste × entrada × resultado esperado",
    "Correção de erros: sintaxe, lógica, execução",
    "Revisão geral da ementa (preparação da prova final)",
    "Planejamento final do projeto",
    "Construção da estrutura definitiva",
    "Desenvolvimento da página inicial",
    "Desenvolvimento dos formulários",
    "Processamento PHP dos dados",
    "Listagem dinâmica final",
    "Validação dos dados de entrada",
    "Tratamento de erros e feedback ao usuário",
    "Testes de todas as funcionalidades",
    "Correções e melhorias — PROVA ESCRITA FINAL A3 (parte)",
    "Preparação da apresentação — PROVA ESCRITA FINAL A3 (parte)",
    "Apresentação dos projetos e avaliação final (10 pts)",
]

# ------------------------------------------------------------ LP2: 25 semanas × 4 etapas
LP2_SEMANAS = [
    ("Ambientação e visão geral",
     "Apresentação da disciplina, programação estruturada e arquitetura do projeto",
     "Exemplos orientados: fluxo site × banco × gerencial",
     "Organização do ambiente (VS Code, XAMPP, pastas) e exercício inicial",
     "Fixação e diagnóstico de entrada"),
    ("SGBD — instalação",
     "Requisitos do SGBD para a linguagem; papel do MySQL",
     "Demonstração da instalação e configuração do MySQL/ODBC",
     "Prática guiada de instalação/configuração no laboratório",
     "Validação do ambiente (checklist de instalação)"),
    ("SGBD — conexão",
     "Conceitos de conexão, parâmetros, abertura/fechamento",
     "Conexão no VB6 (ADO) e no site (mysqli) ao vivo",
     "Laboratório de conexão com tratamento básico de falhas",
     "Fixação e teste rápido da semana"),
    ("SQL — fundamentos",
     "Instruções SQL: DDL/DML, CREATE TABLE, SELECT",
     "Criação e consulta da base loja_turma no phpMyAdmin",
     "Exercícios práticos de SQL (criação e consulta)",
     "Correção dialogada dos exercícios"),
    ("SQL — manipulação",
     "INSERT, UPDATE e DELETE com WHERE seguro",
     "Manipulação dos dados da loja ao vivo",
     "Lista prática de manipulação",
     "Correção dialogada — ENTREGA DA LISTA A1 (10 pts)"),
    ("SQL — consultas",
     "Filtros WHERE, ORDER BY, agregações e GROUP BY",
     "Consultas em cenários reais de dados da loja",
     "Estudo de caso + laboratório de consultas",
     "Fixação e teste rápido da semana"),
    ("Programação estruturada",
     "Sequência, seleção (If/Select Case) e repetição no VB6",
     "Exemplos orientados no gerencial",
     "Exercícios individuais e em grupo",
     "Fixação e verificação da aprendizagem"),
    ("Vetores",
     "Declaração, preenchimento e leitura de vetores",
     "Processamento de vetores no gerencial",
     "Laboratório de vetores",
     "Fixação — TESTE ESCRITO-PRÁTICO A1 (15 pts)"),
    ("Matrizes",
     "Linhas/colunas e laços aninhados",
     "Processamento de matrizes ao vivo",
     "Laboratório de matrizes",
     "Fixação e teste rápido da semana"),
    ("Registros",
     "Type/End Type: agrupando informações relacionadas",
     "Vetor de registros no gerencial",
     "Prática orientada com registros",
     "Fixação e teste rápido da semana"),
    ("Strings",
     "Variáveis String: Len, Mid, Trim, UCase",
     "Manipulação de textos ao vivo",
     "Laboratório de Strings",
     "Fixação e teste rápido da semana"),
    ("Modularização",
     "Sub, Function, parâmetros, retorno e Modules",
     "Refatoração: mdlConexao e mdlRelatorios",
     "Refatoração de exercícios em módulos",
     "Fixação e verificação da aprendizagem"),
    ("Arquivos e textos",
     "Open, Print#, Input#, Line Input, EOF, FreeFile",
     "Exportar/importar .txt ao vivo",
     "Laboratório de arquivos",
     "Fixação e teste rápido da semana"),
    ("Arquivos + dados",
     "Integração arquivos/textos com os dados do programa",
     "Importação/exportação em fluxo controlado",
     "Estudo de caso + prática",
     "Fixação e verificação da aprendizagem"),
    ("Cliente/Servidor",
     "Fluxo aplicação × SGBD em ambiente cliente/servidor",
     "Site e gerencial no mesmo banco, ao vivo",
     "Aula prática de integração",
     "Fixação e teste rápido da semana"),
    ("Cliente/Servidor — prática",
     "Operações com dados: pedido, estoque, validação",
     "Fluxo completo do pedido baixando estoque",
     "Laboratório + atividade em grupo",
     "AVALIAÇÃO 2 (30 pts) — prova conforme Plano de Ensino"),
    ("Backup",
     "Finalidade e procedimentos de cópia (mysqldump)",
     "Demonstração de backup do loja_turma",
     "Prática de backup no laboratório",
     "Fixação e verificação da aprendizagem"),
    ("Recuperação",
     "Restauração e validação após recuperação",
     "Restauração em banco de teste ao vivo",
     "Desastre didático + recuperação em dupla",
     "Fixação e teste rápido da semana"),
    ("Relatórios",
     "Geração de relatórios: seleção e organização",
     "Relatório via objeto Printer ao vivo",
     "Projeto prático de relatório",
     "Fixação e verificação da aprendizagem"),
    ("Impressão e documentos fiscais",
     "Impressão e geração de documentos fiscais (modelo didático)",
     "Cupom/nota simulada ao vivo",
     "Prática de impressão/PDF",
     "Fixação e teste rápido da semana"),
    ("Disco de instalação",
     "Pacote/disco de instalação do programa",
     "Geração do pacote ao vivo",
     "Oficina prática de instalação",
     "Fixação e verificação da aprendizagem"),
    ("Recursos gráficos",
     "Programação gráfica (herança DOS) e PictureBox",
     "Desenho no VB6 ao vivo",
     "Laboratório gráfico",
     "Fixação e teste rápido da semana"),
    ("Integração do projeto",
     "Integração: banco + SQL + estruturas + modularização + arquivos",
     "Gerencial + site integrados ao vivo",
     "Projeto integrador em duplas",
     "Acompanhamento e correções"),
    ("Consolidação e avaliação final",
     "Revisão geral: SGBD, SQL, estruturas, arquivos, relatórios",
     "Revisão geral e resolução de dúvidas",
     "PROVA ESCRITA FINAL A3 (30 pts) — parte 1",
     "PROVA ESCRITA FINAL A3 (30 pts) — parte 2"),
    ("Projeto final e encerramento",
     "Correções e melhorias finais do projeto",
     "Ensaio cronometrado das apresentações",
     "Apresentação dos projetos — A3 (10 pts)",
     "Entrega da versão final e encerramento"),
    ("Extensão do período e entrega final",
     "Revisão de pendências e ajustes finais orientados",
     "Atendimento a alunos em recuperação/pendência",
     "Entrega final dos projetos e documentação",
     "Fechamento do período letivo no diário"),
]

def lp2_atividades():
    out = []
    for wi, wk in enumerate(LP2_SEM):
        tema, t1, t2, t3, t4 = LP2_SEMANAS[wi]
        etapas = [f"{tema} — conceitos fundamentais: {t1}",
                  f"{tema} — exemplos orientados: {t2}",
                  f"{tema} — atividade prática: {t3}",
                  f"{tema} — fixação/verificação: {t4}"]
        k = len(wk)
        escolhidas = etapas if k >= 4 else ([etapas[0], etapas[2]] if k == 2 else etapas[:k])
        out.extend(escolhidas)
    return out

LP2_ATIV = lp2_atividades()
assert len(LP2_ATIV) == len(LP2_DATAS), (len(LP2_ATIV), len(LP2_DATAS))

# ------------------------------------------------------------ geradores
def fmt(d):
    return f"{d.day:02d}/{d.month:02d}/{d.year} ({DIA_NOME[d.weekday()]})"

def build_docx(disciplina, datas, atividades, nome_arq, obs, periodo=None):
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(10)
    t = doc.add_paragraph()
    r = t.add_run("CRONOGRAMA DE ATIVIDADES ESCOLARES")
    r.bold = True; r.font.size = Pt(14)
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t = doc.add_paragraph()
    r = t.add_run("CENTRO TÉCNICO PROFISSIONAL - Trilhas de Futuro 06")
    r.bold = True; r.font.size = Pt(11)
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t = doc.add_paragraph()
    r = t.add_run("CURSO: TÉCNICO EM INFORMÁTICA")
    r.bold = True
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for linha in [f"Disciplina: {disciplina}",
                  "Professor: ______________________________________________",
                  "Período Letivo: " + (periodo or "2026/02 (com extensão até abril/2027 para "
                  "complementação da carga horária, conforme autorização)")]:
        p = doc.add_paragraph(linha)
        p.runs[0].font.size = Pt(10)
    p = doc.add_paragraph(obs)
    p.runs[0].font.size = Pt(8.5)
    p.runs[0].font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    tbl = doc.add_table(rows=1, cols=3)
    tbl.style = "Table Grid"
    hdr = tbl.rows[0].cells
    for i, txt in enumerate(["AULA", "DIA", "Atividade Programada"]):
        hdr[i].text = txt
        hdr[i].paragraphs[0].runs[0].bold = True
    for i, (d, at) in enumerate(zip(datas, atividades), 1):
        row = tbl.add_row().cells
        row[0].text = f"{i:02d}"
        row[1].text = fmt(d)
        row[2].text = at
    tbl.columns[0].width = Cm(1.6)
    tbl.columns[1].width = Cm(3.6)
    tbl.columns[2].width = Cm(12.0)
    for row in tbl.rows:
        row.cells[0].width = Cm(1.6)
        row.cells[1].width = Cm(3.6)
        row.cells[2].width = Cm(12.0)
        for c in row.cells:
            for pp in c.paragraphs:
                for rr in pp.runs:
                    rr.font.size = Pt(9)
    doc.add_paragraph()
    p = doc.add_paragraph("Assinatura do Professor: _______________________________________       "
                          "Assinatura do Coordenador: ____________________________________________")
    p.runs[0].font.size = Pt(9)
    doc.save(os.path.join(OUT, nome_arq))
    print("DOCX ok:", nome_arq, f"({len(datas)} aulas)")

def build_pdf(disciplina, datas, atividades, nome_arq, obs, periodo=None):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    F = os.path.join(ROOT, "fonts", "")
    ALT = "/opt/arena-python/lib/python3.11/site-packages/reportlab/fonts/"
    def reg(n, pa, al):
        try: pdfmetrics.registerFont(TTFont(n, pa))
        except Exception: pdfmetrics.registerFont(TTFont(n, al))
    reg("Inter", F + "Inter-Regular.ttf", ALT + "Vera.ttf")
    reg("Inter-Bd", F + "Inter-Bold.ttf", ALT + "VeraBd.ttf")
    NAVY = colors.HexColor("#0D2B4E"); LINE = colors.HexColor("#C9D8E8")
    ROW = colors.HexColor("#F4F8FC")
    st_t = ParagraphStyle("t", fontName="Inter-Bd", fontSize=13, textColor=NAVY)
    st_i = ParagraphStyle("i", fontName="Inter", fontSize=8.5, textColor=colors.HexColor("#555555"))
    st_h = ParagraphStyle("h", fontName="Inter-Bd", fontSize=8.5, textColor=colors.white)
    st_c = ParagraphStyle("c", fontName="Inter", fontSize=7.6, leading=10)
    doc = SimpleDocTemplate(os.path.join(OUT, nome_arq), pagesize=A4,
        leftMargin=1.4*cm, rightMargin=1.4*cm, topMargin=1.4*cm, bottomMargin=1.4*cm,
        title="Cronograma " + disciplina)
    tw = A4[0] - 2.8*cm
    el = [Paragraph("CRONOGRAMA DE ATIVIDADES ESCOLARES", st_t),
          Paragraph("CENTRO TÉCNICO PROFISSIONAL - Trilhas de Futuro 06 · CURSO: TÉCNICO EM INFORMÁTICA", st_i),
          Paragraph(f"Disciplina: <b>{disciplina}</b> · Professor: ______________________ · "
                    f"Período Letivo: " + (periodo or "2026/02 (estendido p/ complementação de CH)"), st_i),
          Paragraph(obs, st_i), Spacer(1, 6)]
    rows = [[Paragraph("AULA", st_h), Paragraph("DIA", st_h), Paragraph("Atividade Programada", st_h)]]
    for i, (d, at) in enumerate(zip(datas, atividades), 1):
        rows.append([Paragraph(f"{i:02d}", st_c), Paragraph(fmt(d), st_c), Paragraph(at, st_c)])
    t = Table(rows, colWidths=[tw*0.08, tw*0.22, tw*0.70], repeatRows=1)
    cmd = [("BACKGROUND", (0,0), (-1,0), NAVY), ("GRID", (0,0), (-1,-1), 0.5, LINE),
           ("VALIGN", (0,0), (-1,-1), "TOP"),
           ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
           ("TOPPADDING", (0,0), (-1,-1), 3.5), ("BOTTOMPADDING", (0,0), (-1,-1), 3.5)]
    for i in range(1, len(rows)):
        if i % 2 == 0: cmd.append(("BACKGROUND", (0,i), (-1,i), ROW))
    t.setStyle(TableStyle(cmd))
    el.append(t)
    el.append(Spacer(1, 10))
    el.append(Paragraph("Assinatura do Professor: _______________________________________&nbsp;&nbsp;&nbsp;"
                        "Assinatura do Coordenador: ____________________________________________", st_i))
    doc.build(el)
    print("PDF ok:", nome_arq)

OBS_PI1 = ("Dias de aula: segunda-feira (1 aula) e terça-feira (2 aulas), noturno, Sala 310. "
           "Sem aula em: 12/10, 13/10, 02/11, 20/11/2026; 08–10/02 e 24–26/03/2027; férias de janeiro/2027. "
           "Cronograma estendido até 20/04/2027 para completar 72 aulas (60 h presenciais).")
OBS_LP2 = ("Dias de aula: quarta-feira (2 aulas) e sexta-feira (2 aulas), noturno, Sala 410. "
           "Sem aula em: 12/10, 13/10, 02/11, 20/11/2026; 08–10/02 e 24–26/03/2027; férias de janeiro/2027. "
           "Cronograma estendido até 16/04/2027 para completar 96 aulas (80 h presenciais).")

build_docx("Programação para Internet I", PI1_DATAS, PI1_TEMAS,
           "Cronograma_Preenchido_PI-I.docx", OBS_PI1)
build_docx("Linguagem de Programação II", LP2_DATAS, LP2_ATIV,
           "Cronograma_Preenchido_LP2.docx", OBS_LP2)
build_pdf("Programação para Internet I", PI1_DATAS, PI1_TEMAS,
          "Cronograma_Preenchido_PI-I.pdf", OBS_PI1)
build_pdf("Linguagem de Programação II", LP2_DATAS, LP2_ATIV,
          "Cronograma_Preenchido_LP2.pdf", OBS_LP2)
print("PI-I: início", fmt(PI1_DATAS[0]), "| término", fmt(PI1_DATAS[-1]))
print("LP2:  início", fmt(LP2_DATAS[0]), "| término", fmt(LP2_DATAS[-1]))
