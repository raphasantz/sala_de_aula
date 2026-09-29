# -*- coding: utf-8 -*-
"""Desenha 'prints' simulados (mockups) para o Tutorial Ilustrado da Loja."""
import os, io as _io, time as _time
from PIL import Image, ImageDraw, ImageFont

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mockups_loja")
os.makedirs(D, exist_ok=True)
F = "/home/user/fonts/"
ALT = "/opt/arena-python/lib/python3.11/site-packages/reportlab/fonts/"
def font(sz, bold=False, mono=False):
    cands = []
    if mono:
        cands = [F + ("JetBrainsMono-Bold.ttf" if bold else "JetBrainsMono-Regular.ttf"),
                 ALT + "VeraBd.ttf" if bold else ALT + "Vera.ttf"]
    else:
        cands = [F + ("Inter-Bold.ttf" if bold else "Inter-Regular.ttf"),
                 ALT + "VeraBd.ttf" if bold else ALT + "Vera.ttf"]
    last = None
    for c in cands:
        for t in range(4):
            try:
                return ImageFont.truetype(c, sz)
            except Exception as e:
                last = e
                try:
                    with open(c, "rb") as fh:
                        return ImageFont.truetype(_io.BytesIO(fh.read()), sz)
                except Exception as e2:
                    last = e2; _time.sleep(0.3)
    raise last

# cores
VS_BG=(30,30,30); VS_SIDE=(37,37,38); VS_BAR=(51,51,51); VS_TXT=(212,212,212)
CHROME=(222,226,230); CHROME_D=(32,33,36); WHITE=(255,255,255)
NAVY=(13,43,78); AZUL=(27,95,170); AMB=(245,158,11); VERDE=(30,123,52)
CINZA=(243,244,246); BORDA=(209,213,219); TXT=(31,41,55)
XAMP=(248,250,252); XAMP_H=(203,225,244)
VB_GRAY=(192,192,192); VB_BLUE=(10,43,132)

def rr(d, box, r, fill=None, outline=None, w=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=w)

def titlebar(d, w, title, dark=True):
    c = VS_BAR if dark else CHROME
    d.rectangle((0, 0, w, 34), fill=c)
    for i, cc in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
        d.ellipse((12+i*22, 10, 26+i*22, 24), fill=cc)
    t = font(15, mono=True)
    d.text((w//2, 17), title, font=t, fill=(200,200,200) if dark else (60,64,67), anchor="mm")

# ============================================================ VS CODE
W, H = 1150, 680
im = Image.new("RGB", (W, H), VS_BG); d = ImageDraw.Draw(im)
titlebar(d, W, "index.php — loja — Visual Studio Code")
d.rectangle((0, 34, 46, H), fill=VS_SIDE)
for i in range(5):
    d.rectangle((14, 52+i*34, 32, 70+i*34), outline=(120,120,120), width=2)
d.rectangle((46, 34, 286, H), fill=VS_SIDE)
t = font(14, bold=True); d.text((60, 50), "EXPLORADOR", font=t, fill=(187,197,205))
t = font(15, mono=True)
tree = [("LOJA", 0, True), ("css", 1, False), ("  estilo.css", 2, False),
        ("imagens", 1, False), ("includes", 1, False), ("  conexao.php", 2, False),
        ("  cabecalho.php", 2, False), ("  rodape.php", 2, False),
        ("index.php", 1, True), ("produtos.php", 1, False),
        ("cadastro.html", 1, False), ("processar_cadastro.php", 1, False),
        ("contato.html", 1, False), ("processar_contato.php", 1, False)]
y = 84
for nome, niv, hl in tree:
    if hl and nome == "index.php":
        d.rectangle((46, y-4, 286, y+20), fill=(55,65,80))
    col = (225,225,225) if hl else (160,170,180)
    d.text((60 + niv*14, y), nome, font=t, fill=col)
    y += 26
# abas
d.rectangle((286, 34, W, 68), fill=(37,37,38))
d.rectangle((286, 34, 420, 68), fill=VS_BG)
d.text((300, 51), "index.php", font=font(14, mono=True), fill=(255,255,255))
d.text((440, 51), "conexao.php", font=font(14, mono=True), fill=(150,150,150))
# código
code = [
    ("<?php", [(0,5,(198,120,222))]),
    ("include \"includes/conexao.php\";", [(0,7,(198,120,222)), (8,29,(152,195,121))]),
    ("include \"includes/cabecalho.php\";", [(0,7,(198,120,222)), (8,30,(152,195,121))]),
    ("?>", [(0,2,(198,120,222))]),
    ("<section class=\"hero\">", [(1,8,(224,108,108)), (14,19,(209,154,110)), (20,26,(152,195,121))]),
    ("  <img src=\"imagens/banner.png\">", [(3,6,(224,108,108)), (11,33,(152,195,121))]),
    ("  <h1>Loja Tech da Turma</h1>", [(3,5,(224,108,108)), (24,28,(224,108,108))]),
    ("</section>", [(1,8,(224,108,108))]),
    ("", []),
    ("<h2 class=\"secao\">Destaques da semana</h2>", [(1,3,(224,108,108)), (9,14,(209,154,110)), (15,22,(152,195,121))]),
    ("<div class=\"vitrine\">", [(1,4,(224,108,108)), (10,17,(209,154,110)), (18,26,(152,195,121))]),
    ("<?php", [(0,5,(198,120,222))]),
    ("  $sql = \"SELECT nome, preco, foto", [(2,6,(224,108,108)), (9,40,(152,195,121))]),
    ("          FROM produtos", [(10,14,(198,120,222)), (15,23,(224,108,108))]),
    ("          WHERE destaque = 1\";", [(10,15,(198,120,222)), (26,27,(209,154,110))]),
    ("  $res = $con->query($sql);", [(2,6,(224,108,108)), (9,13,(224,108,108)), (17,22,(97,175,239))]),
    ("  while ($p = $res->fetch_assoc()):", [(2,7,(198,120,222)), (10,11,(224,108,108)), (14,18,(224,108,108)), (20,32,(97,175,239))]),
    ("?>", [(0,2,(198,120,222))]),
    ("  <div class=\"card\"> ... </div>", [(3,6,(224,108,108)), (12,16,(209,154,110))]),
    ("<?php endwhile; ?>", [(0,5,(198,120,222)), (6,14,(198,120,222)), (15,17,(198,120,222))]),
]
t = font(15, mono=True); tn = font(13, mono=True)
y = 84
for i, (linha, cores) in enumerate(code, 1):
    d.text((268, y), str(i), font=tn, fill=(110,110,110), anchor="rm")
    x = 300
    pos = 0
    for (a, b, c) in cores:
        if a > pos:
            d.text((x, y), linha[pos:a], font=t, fill=VS_TXT); x += t.getlength(linha[pos:a])
        d.text((x, y), linha[a:b], font=t, fill=c); x += t.getlength(linha[a:b])
        pos = b
    if pos < len(linha):
        d.text((x, y), linha[pos:], font=t, fill=VS_TXT)
    y += 27
# barra de status
d.rectangle((0, H-26, W, H), fill=AZUL)
d.text((14, H-13), " main   PHP   UTF-8   Ln 12, Col 4", font=font(13), fill=WHITE, anchor="lm")
im.save(os.path.join(D, "mock_vscode.png"))

# ============================================================ XAMPP
W, H = 900, 560
im = Image.new("RGB", (W, H), XAMP); d = ImageDraw.Draw(im)
titlebar(d, W, "XAMPP Control Panel 3.3.0", dark=False)
d.rectangle((0, 34, 150, H), fill=(232,240,248))
for i, m in enumerate(["Config", "Netstat", "Shell", "Explorer", "Services", "Help"]):
    d.text((20, 60+i*38), m, font=font(15, bold=True), fill=(70,90,110))
d.rectangle((150, 50, W-20, 90), fill=XAMP_H)
d.text((170, 70), "Modules", font=font(15, bold=True), fill=(40,60,80), anchor="lm")
d.text((560, 70), "PID(s)", font=font(15, bold=True), fill=(40,60,80), anchor="lm")
d.text((660, 70), "Port(s)", font=font(15, bold=True), fill=(40,60,80), anchor="lm")
d.text((760, 70), "Actions", font=font(15, bold=True), fill=(40,60,80), anchor="lm")
rows = [("Apache", "12344", "80, 443", True), ("MySQL", "12380", "3306", True),
        ("FileZilla", "—", "—", False), ("Mercury", "—", "—", False)]
y = 100
for nome, pid, ports, on in rows:
    d.rectangle((150, y, W-20, y+52), fill=WHITE, outline=BORDA)
    d.rectangle((152, y+2, 166, y+50), fill=VERDE if on else (150,150,150))
    d.text((180, y+26), nome, font=font(16, bold=True), fill=TXT, anchor="lm")
    d.text((560, y+26), pid, font=font(15, mono=True), fill=TXT, anchor="lm")
    d.text((660, y+26), ports, font=font(15, mono=True), fill=TXT, anchor="lm")
    bx = 750
    for lbl, cc in [("Start", VERDE), ("Stop", (200,60,60)), ("Config", (120,130,140))]:
        if (lbl == "Start") and on: cc = (170,180,190)
        if (lbl == "Stop") and not on: cc = (170,180,190)
        rr(d, (bx, y+12, bx+62, y+40), 6, fill=cc)
        d.text((bx+31, y+26), lbl, font=font(12, bold=True), fill=WHITE, anchor="mm")
        bx += 68
    y += 58
d.rectangle((150, y+10, W-20, y+90), fill=(254,244,226), outline=AMB)
d.text((170, y+30), "Apache e MySQL VERDES = servidores ligados.", font=font(15, bold=True), fill=(154,98,6), anchor="lm")
d.text((170, y+58), "É isso que o aluno deve ver antes de abrir o localhost!", font=font(14), fill=(120,90,20), anchor="lm")
im.save(os.path.join(D, "mock_xampp.png"))

# ============================================================ phpMyAdmin
W, H = 1150, 640
im = Image.new("RGB", (W, H), WHITE); d = ImageDraw.Draw(im)
titlebar(d, W, "phpMyAdmin — localhost — Mozilla Firefox", dark=False)
d.rectangle((0, 34, W, 78), fill=(240,243,247))
d.text((20, 56), "phpMyAdmin", font=font(18, bold=True), fill=(111,111,153), anchor="lm")
d.rectangle((0, 78, 240, H), fill=(246,248,251))
d.text((16, 96), "Novo", font=font(14, bold=True), fill=AZUL)
dbs = [("information_schema", False), ("loja_turma", True), ("mysql", False),
       ("performance_schema", False), ("phpmyadmin", False), ("test", False)]
y = 126
for nome, on in dbs:
    if on: d.rectangle((4, y-6, 236, y+20), fill=(214,228,244))
    d.text((20, y), ("▾ " if on else "▸ ") + nome, font=font(14, bold=on), fill=(40,60,90) if on else (90,100,115))
    y += 26
    if on:
        for tb in ["clientes", "mensagens", "produtos", "vendas"]:
            d.text((40, y), tb, font=font(14), fill=AZUL); y += 24
d.rectangle((240, 78, W, 118), fill=(246,248,251))
for i, tab in enumerate(["Estrutura", "SQL", "Pesquisar", "Consultar", "Importar", "Operações"]):
    x = 260 + i*120
    if tab == "Estrutura": d.rectangle((x-8, 84, x+100, 114), fill=WHITE, outline=BORDA)
    d.text((x, 99), tab, font=font(14, bold=(tab == "Estrutura")), fill=TXT, anchor="lm")
d.text((260, 140), "Banco de dados: loja_turma", font=font(17, bold=True), fill=TXT)
hdr = ["Tabela", "Linhas", "Tipo", "Ação"]
xs = [260, 560, 700, 900]
d.rectangle((250, 165, W-20, 197), fill=(222,232,244))
for x, htxt in zip(xs, hdr):
    d.text((x, 181), htxt, font=font(14, bold=True), fill=(40,60,90), anchor="lm")
rows = [("clientes", "2", "InnoDB"), ("mensagens", "1", "InnoDB"),
        ("produtos", "8", "InnoDB"), ("vendas", "3", "InnoDB")]
y = 197
for nome, ln, tp in rows:
    d.rectangle((250, y, W-20, y+34), fill=WHITE if (y//34) % 2 else (248,250,252), outline=(230,235,240))
    d.text((260, y+17), nome, font=font(14, bold=True), fill=AZUL, anchor="lm")
    d.text((560, y+17), ln, font=font(14, mono=True), fill=TXT, anchor="lm")
    d.text((700, y+17), tp, font=font(14), fill=TXT, anchor="lm")
    d.text((900, y+17), "Explorar  |  Estrutura  |  SQL", font=font(13), fill=AZUL, anchor="lm")
    y += 34
d.rectangle((250, y+16, W-20, y+66), fill=(232,244,234), outline=VERDE)
d.text((270, y+41), "OK: 4 tabelas + view vw_estoque_baixo importadas com sucesso!",
       font=font(15, bold=True), fill=VERDE, anchor="lm")
im.save(os.path.join(D, "mock_phpmyadmin.png"))
print("mockups 1-3 ok")
