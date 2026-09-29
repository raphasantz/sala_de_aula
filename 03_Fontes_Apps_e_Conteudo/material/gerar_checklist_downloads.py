# -*- coding: utf-8 -*-
"""Gera o Checklist_Downloads.pdf (1 página, imprimível) — Projeto Loja & Laboratório."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether)

F = "/home/user/fonts/"
ALT = "/opt/arena-python/lib/python3.11/site-packages/reportlab/fonts/"
def reg(name, path, alt):
    try:
        pdfmetrics.registerFont(TTFont(name, path))
    except Exception:
        pdfmetrics.registerFont(TTFont(name, alt))
reg("Inter", F + "Inter-Regular.ttf", ALT + "Vera.ttf")
reg("Inter-Bd", F + "Inter-Bold.ttf", ALT + "VeraBd.ttf")
reg("Inter-Bk", F + "Inter-Black.ttf", ALT + "VeraBd.ttf")
reg("Mono", F + "JetBrainsMono-Regular.ttf", ALT + "Vera.ttf")

NAVY = HexColor("#0D2B4E"); AZUL = HexColor("#1B5FAA"); AMB = HexColor("#F59E0B")
AMBBG = HexColor("#FEF4E2"); SKY = HexColor("#E9F1FA"); INK = HexColor("#1F2937")
SOFT = HexColor("#5B6B7C"); LINE = HexColor("#C9D8E8"); VERDE = HexColor("#1E7B34")

S = {}
S["h1"] = ParagraphStyle("h1", fontName="Inter-Bk", fontSize=21, leading=25, textColor=NAVY)
S["sub"] = ParagraphStyle("sub", fontName="Inter", fontSize=10.5, leading=15, textColor=SOFT)
S["th"] = ParagraphStyle("th", fontName="Inter-Bd", fontSize=9.2, leading=12, textColor=white)
S["td"] = ParagraphStyle("td", fontName="Inter", fontSize=9.3, leading=13, textColor=INK)
S["tdb"] = ParagraphStyle("tdb", fontName="Inter-Bd", fontSize=9.3, leading=13, textColor=NAVY)
S["boxt"] = ParagraphStyle("boxt", fontName="Inter-Bd", fontSize=9, leading=12, textColor=HexColor("#9A6206"))
S["box"] = ParagraphStyle("box", fontName="Inter", fontSize=9.2, leading=13.4, textColor=INK)
S["link"] = ParagraphStyle("link", fontName="Mono", fontSize=8.6, leading=12, textColor=AZUL)
S["foot"] = ParagraphStyle("foot", fontName="Inter", fontSize=8.4, leading=11.5, textColor=SOFT)

def P(t, s): return Paragraph(t, S[s])

doc = SimpleDocTemplate(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                     "output", "Checklist_Downloads.pdf"),
                        pagesize=A4, leftMargin=1.6*cm, rightMargin=1.6*cm,
                        topMargin=1.4*cm, bottomMargin=1.4*cm,
                        title="Checklist de Instalação — Projeto Loja",
                        author="Loja Tech da Turma · Turma 2/2026")
TW = A4[0] - 3.2*cm
st = []

# topo
topo = Table([[P("CHECKLIST DE INSTALAÇÃO", "th"),
               P("Projeto Loja Tech da Turma · Turma 2/2026", "th")]],
             colWidths=[TW*0.5, TW*0.5])
topo.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), NAVY),
                          ("ALIGN", (1,0), (1,0), "RIGHT"),
                          ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
                          ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
                          ("ROUNDEDCORNERS", [8,8,0,0])]))
st.append(topo)
st.append(Table([[P("Marque cada item após instalar e testar. Todos os itens são <b>gratuitos</b>, "
                    "exceto o VB6 (licença/CD da escola). Na dúvida: chame a professora! 😊", "td")]],
                colWidths=[TW]))
st[-1].setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), SKY),
                            ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
                            ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8)]))
st.append(Spacer(1, 8))

linhas = [
    ["1", "<b>VS Code</b><br/>Editor de código (HTML, PHP, CSS, SQL)",
     "code.visualstudio.com<br/>botão azul “Download for Windows”",
     "Todos", "[&nbsp;&nbsp;]"],
    ["2", "<b>XAMPP</b><br/>Apache + MySQL + PHP + phpMyAdmin",
     "apachefriends.org<br/>instalar com Next… Next… Finish",
     "Todos", "[&nbsp;&nbsp;]"],
    ["3", "<b>Chrome ou Firefox atualizado</b><br/>Testar o site + DevTools (F12)",
     "Já vem no PC — só atualize",
     "Todos", "[&nbsp;&nbsp;]"],
    ["4", "<b>MySQL Connector/ODBC</b><br/>Ponte VB6 ↔ MySQL (só parte LP2)",
     "dev.mysql.com/downloads/connector/odbc<br/>escolha “Windows (x86, 32-bit)” MSI",
     "Só LP2/VB6", "[&nbsp;&nbsp;]"],
    ["5", "<b>Visual Basic 6.0</b> (!)<br/>IDE do gerencial (não tem download oficial)",
     "Pegar com a coordenação/TI da escola<br/>(licença/CD antigo da instituição)",
     "Só LP2/VB6", "[&nbsp;&nbsp;]"],
]
t = Table([[P(c, "th") for c in ["#", "Software e para que serve", "Onde baixar (site oficial)", "Quem precisa", "Feito"]]] +
          [[P(r[0], "tdb"), P(r[1], "td"), P(r[2], "td"), P(r[3], "td"), P(r[4], "td")] for r in linhas],
          colWidths=[TW*0.05, TW*0.34, TW*0.36, TW*0.15, TW*0.10])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), AZUL),
    ("GRID", (0,0), (-1,-1), 0.6, LINE),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ALIGN", (0,0), (0,-1), "CENTER"), ("ALIGN", (4,0), (4,-1), "CENTER"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, HexColor("#F4F8FC")]),
    ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
    ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ("ROUNDEDCORNERS", [0,0,8,8]),
]))
st.append(t)
st.append(Spacer(1, 10))

# testes obrigatórios
testes = Table([[P("TESTES OBRIGATÓRIOS ANTES DA PRIMEIRA AULA PRÁTICA", "boxt")],
                [P("1. XAMPP Control Panel: clicar <b>Start</b> em <b>Apache</b> e em <b>MySQL</b> (ficam verdes).<br/>"
                   "2. Navegador: abrir <b>http://localhost</b> → painel do XAMPP aparece.<br/>"
                   "3. Navegador: abrir <b>http://localhost/phpmyadmin</b> → entra sem senha.<br/>"
                   "4. VS Code: criar pasta <b>loja</b>, arquivo <b>teste.php</b> com "
                   "<font name='Mono'>&lt;?php echo \"oi\"; ?&gt;</font> e salvar em "
                   "<font name='Mono'>C:\\xampp\\htdocs\\loja\\</font>.<br/>"
                   "5. Navegador: <b>http://localhost/loja/teste.php</b> → mostra “oi”. ", "box")]],
               colWidths=[TW])
testes.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), AMBBG),
                            ("LINEBEFORE", (0,0), (0,-1), 3.2, AMB),
                            ("LEFTPADDING", (0,0), (-1,-1), 11), ("RIGHTPADDING", (0,0), (-1,-1), 11),
                            ("TOPPADDING", (0,0), (-1,-1), 9), ("BOTTOMPADDING", (0,0), (-1,-1), 9),
                            ("ROUNDEDCORNERS", [8,8,8,8])]))
st.append(KeepTogether(testes))
st.append(Spacer(1, 8))

nao = Table([[P("NÃO BAIXE", "boxt")],
             [P("• Node.js (não está nas ementas) · “XAMPP modificado” ou PHP de sites estranhos · "
                "extensões pagas do VS Code · “VB6 grátis download” de sites aleatórios (vírus!).<br/>"
                "• Extensões úteis e gratuitas do VS Code (opcionais): <b>Portuguese (Brazil) Language Pack</b>, "
                "<b>Auto Close Tag</b>, <b>Auto Rename Tag</b>.", "box")]],
            colWidths=[TW])
nao.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), HexColor("#FBEAE8")),
                         ("LINEBEFORE", (0,0), (0,-1), 3.2, HexColor("#C0392B")),
                         ("LEFTPADDING", (0,0), (-1,-1), 11), ("RIGHTPADDING", (0,0), (-1,-1), 11),
                         ("TOPPADDING", (0,0), (-1,-1), 9), ("BOTTOMPADDING", (0,0), (-1,-1), 9),
                         ("ROUNDEDCORNERS", [8,8,8,8])]))
st.append(KeepTogether(nao))
st.append(Spacer(1, 10))

rod = Table([[P("Aluno(a): ______________________________________  Turma: __________  "
                "Data: ____ / ____ / 2026", "td")],
             [P("Visto da professora: ______________  ·  Dúvidas? Leve este papel (ou um print) na próxima aula. ", "foot")]],
            colWidths=[TW])
rod.setStyle(TableStyle([("LINEABOVE", (0,0), (-1,0), 0.8, LINE),
                         ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 2),
                         ("LEFTPADDING", (0,0), (-1,-1), 2)]))
st.append(rod)

doc.build(st)
print("Checklist_Downloads.pdf gerado")
