# -*- coding: utf-8 -*-
"""Mockups 4-7: navegador (home e produto/pagamento), terminal e VB6."""
import os, io as _io, time as _time
from PIL import Image, ImageDraw, ImageFont

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mockups_loja")
os.makedirs(D, exist_ok=True)
F = "/home/user/fonts/"
ALT = "/opt/arena-python/lib/python3.11/site-packages/reportlab/fonts/"
def font(sz, bold=False, mono=False):
    if mono:
        cands = [F + ("JetBrainsMono-Bold.ttf" if bold else "JetBrainsMono-Regular.ttf"),
                 ALT + "VeraBd.ttf" if bold else ALT + "Vera.ttf"]
    else:
        cands = [F + ("Inter-Bold.ttf" if bold else "Inter-Regular.ttf"),
                 ALT + "VeraBd.ttf" if bold else ALT + "Vera.ttf"]
    last = None
    for c in cands:
        for t in range(4):
            try: return ImageFont.truetype(c, sz)
            except Exception as e:
                last = e
                try:
                    with open(c, "rb") as fh: return ImageFont.truetype(_io.BytesIO(fh.read()), sz)
                except Exception as e2: last = e2; _time.sleep(0.3)
    raise last

def rr(d, box, r, fill=None, outline=None, w=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=w)

NAVY=(13,43,78); AZUL=(27,95,170); AMB=(245,158,11); VERDE=(30,123,52)
VB_BLUE=(10,43,132)
WHITE=(255,255,255); TXT=(31,41,55); CINZA=(243,244,246); BORDA=(209,213,219)

def chrome(w, h, url, titulo):
    im = Image.new("RGB", (w, h), WHITE); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, w, 40), fill=(222,226,230))
    rr(d, (10, 7, 250, 33), 8, fill=(248,249,250))
    d.ellipse((22, 14, 34, 26), fill=AZUL)
    d.text((42, 20), titulo, font=font(13, True), fill=TXT, anchor="lm")
    d.rectangle((0, 40, w, 76), fill=(248,249,250))
    for i, sy in enumerate([(24,58),(52,58),(80,58)]):
        d.ellipse((sy[0]-6, sy[1]-6, sy[0]+6, sy[1]+6), outline=(120,125,130), width=2)
    rr(d, (110, 46, w-160, 70), 12, fill=WHITE, outline=BORDA)
    d.text((130, 58), url, font=font(13, mono=True), fill=(60,64,67), anchor="lm")
    d.ellipse((w-120, 50, w-104, 66), outline=(120,125,130), width=2)
    return im, d

def produto_shape(d, cx, cy, kind):
    if kind == "mouse":
        d.ellipse((cx-28, cy-38, cx+28, cy+38), fill=(34,34,34))
        rr(d, (cx-3, cy-26, cx+3, cy-10), 3, fill=AMB)
    elif kind == "teclado":
        rr(d, (cx-40, cy-20, cx+40, cy+20), 6, fill=(229,231,235))
        for r in range(3):
            for c in range(8):
                rr(d, (cx-35+c*9, cy-15+r*11, cx-29+c*9, cy-9+r*11), 2,
                   fill=AMB if (r==1 and c==7) else (249,250,251))
    elif kind == "headset":
        d.arc((cx-26, cy-30, cx+26, cy+22), 180, 360, fill=AZUL, width=6)
        rr(d, (cx-30, cy-2, cx-18, cy+22), 6, fill=NAVY)
        rr(d, (cx+18, cy-2, cx+30, cy+22), 6, fill=NAVY)
    else:
        d.ellipse((cx-24, cy-24, cx+24, cy+24), fill=(34,34,34))
        d.ellipse((cx-10, cy-10, cx+10, cy+10), fill=AZUL)

# ================= NAVEGADOR: HOME =================
W, H = 1100, 780
im, d = chrome(W, H, "http://localhost/loja/index.php", "Loja Tech da Turma")
d.rectangle((0, 76, W, 150), fill=NAVY)
d.ellipse((24, 88, 72, 136), fill=WHITE)
d.ellipse((34, 98, 62, 126), fill=AZUL)
d.text((86, 113), "Loja Tech da Turma", font=font(22, True), fill=WHITE, anchor="lm")
for i, m in enumerate(["Início", "Produtos", "Contato e Localização", "Cadastre-se"]):
    x = 620 + i*120
    rr(d, (x, 98, x+110, 128), 15, fill=AMB if i == 0 else (30,60,95))
    d.text((x+55, 113), m, font=font(12, True), fill=NAVY if i == 0 else WHITE, anchor="mm")
d.rectangle((0, 150, W, 330), fill=(20,58,102))
for i, c in enumerate([(158,206,106), AMB, (108,182,255)]):
    d.rectangle((640, 180+i*38, 640+[220,150,260][i], 196+i*38), fill=c)
d.text((40, 200), "Loja Tech da Turma", font=font(30, True), fill=WHITE, anchor="lm")
d.text((40, 240), "Tudo aqui sai do banco loja_turma, ao vivo!", font=font(16), fill=(201,220,242), anchor="lm")
rr(d, (40, 268, 260, 306), 19, fill=AMB)
d.text((150, 287), "Ver catálogo completo", font=font(14, True), fill=NAVY, anchor="mm")
d.text((30, 360), "Produtos em destaque — clique para ver e comprar", font=font(20, True), fill=NAVY, anchor="lm")
d.rectangle((30, 372, 36, 396), fill=AMB)
for i, (nome, preco, kind) in enumerate([("Mouse Gamer", "89,90", "mouse"),
                                         ("Teclado Turbo", "249,00", "teclado"),
                                         ("Headset Turma", "179,50", "headset"),
                                         ("Webcam FullHD", "199,90", "webcam")]):
    x = 30 + i*265
    rr(d, (x, 400, x+250, 640), 14, fill=WHITE, outline=BORDA, w=2)
    produto_shape(d, x+125, 470, kind)
    d.text((x+125, 540), nome, font=font(15, True), fill=NAVY, anchor="mm")
    d.text((x+125, 566), "R$ " + preco, font=font(17, True), fill=VERDE, anchor="mm")
    d.text((x+125, 596), "ver detalhes e comprar ›", font=font(12, True), fill=AZUL, anchor="mm")
d.rectangle((0, 690, W, 780), fill=NAVY)
d.text((W//2, 725), "Loja Tech da Turma — projeto das disciplinas PI-I e LP2 · Turma 2/2026",
       font=font(13), fill=(201,220,242), anchor="mm")
im.save(os.path.join(D, "mock_browser_home.png"))

# ================= NAVEGADOR: PRODUTO + PAGAMENTO =================
W, H = 1100, 800
im, d = chrome(W, H, "http://localhost/loja/produto.php?id=1", "Mouse Gamer AzulTech")
d.rectangle((0, 76, W, 150), fill=NAVY)
d.text((30, 113), "Loja Tech da Turma", font=font(20, True), fill=WHITE, anchor="lm")
d.text((30, 176), "‹ Voltar ao catálogo", font=font(13, True), fill=AZUL, anchor="lm")
rr(d, (30, 196, 470, 560), 14, fill=(246,249,253), outline=BORDA, w=2)
produto_shape(d, 250, 380, "mouse")
d.text((30, 216), "foto do banco (imagens/prod-mouse.png)", font=font(11), fill=(120,130,140), anchor="lm")
x = 500
rr(d, (x, 200, x+120, 228), 14, fill=(227,236,247))
d.text((x+60, 214), "PERIFÉRICOS", font=font(11, True), fill=NAVY, anchor="mm")
d.text((x, 258), "Mouse Gamer AzulTech", font=font(26, True), fill=NAVY, anchor="lm")
d.text((x, 306), "R$ 89,90", font=font(30, True), fill=VERDE, anchor="lm")
for i, ln in enumerate(["Mouse ergonômico com 6 botões, LED azul e",
                        "sensor de 7200 DPI. Ideal para jogos e para",
                        "o CAD da aula de desenho."]):
    d.text((x, 344+i*24), ln, font=font(14), fill=(55,65,80), anchor="lm")
d.text((x, 428), "✅ Em estoque: 12 unidade(s)", font=font(14, True), fill=VERDE, anchor="lm")
d.text((x, 452), "Código #1 · consulta ao banco em 20/09/2026 19:40", font=font(11), fill=(120,130,140), anchor="lm")
rr(d, (x, 478, x+250, 522), 22, fill=AMB)
d.text((x+125, 500), "💳 Ir para o pagamento", font=font(15, True), fill=NAVY, anchor="mm")
d.text((30, 600), "Escolha a forma de pagamento (simulado):", font=font(16, True), fill=NAVY, anchor="lm")
for i, (nome, cor) in enumerate([("PIX", (50,177,166)), ("CARTÃO", AZUL), ("BOLETO", (120,125,130))]):
    x = 30 + i*250
    rr(d, (x, 620, x+230, 730), 12, fill=WHITE, outline=AMB if i == 0 else BORDA, w=3)
    if i == 0:
        d.polygon([(x+115, 636), (x+155, 666), (x+115, 696), (x+75, 666)], fill=cor)
    elif i == 1:
        rr(d, (x+75, 640, x+155, 692), 8, fill=cor); d.rectangle((x+75, 652, x+155, 664), fill=NAVY)
    else:
        rr(d, (x+80, 636, x+150, 696), 6, fill=(250,250,250), outline=cor, w=2)
        for k in range(7): d.rectangle((x+88+k*8, 646, x+91+k*8, 682), fill=(30,30,30))
    d.text((x+115, 714), nome, font=font(13, True), fill=NAVY, anchor="mm")
im.save(os.path.join(D, "mock_browser_produto.png"))

# ================= TERMINAL: BACKUP =================
W, H = 920, 430
im = Image.new("RGB", (W, H), (12,12,12)); d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, 32), fill=(40,40,40))
d.text((W//2, 16), "Prompt de Comando — mysqldump", font=font(13, mono=True), fill=(220,220,220), anchor="mm")
linhas = [
    ("Microsoft Windows [versão 10.0.19045.5011]", (204,204,204)),
    ("(c) Microsoft Corporation. Todos os direitos reservados.", (204,204,204)),
    ("", (204,204,204)),
    ("C:\\Users\\Prof>cd C:\\xampp\\mysql\\bin", (240,240,240)),
    ("", (204,204,204)),
    ("C:\\xampp\\mysql\\bin>mysqldump -u root loja_turma > C:\\lp2\\backups\\loja_aula.sql", (255,255,255)),
    ("", (204,204,204)),
    ("C:\\xampp\\mysql\\bin>dir C:\\lp2\\backups", (240,240,240)),
    (" 20/09/2026  19:42            14.382 loja_aula.sql", (158,206,106)),
    ("               1 arquivo(s)        14.382 bytes", (158,206,106)),
    ("", (204,204,204)),
    ("C:\\xampp\\mysql\\bin> _", (240,240,240)),
]
t = font(14, mono=True)
y = 52
for ln, c in linhas:
    d.text((18, y), ln, font=t, fill=c); y += 28
im.save(os.path.join(D, "mock_terminal.png"))

# ================= VB6 IDE =================
W, H = 1150, 720
im = Image.new("RGB", (W, H), (192,192,192)); d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, 30), fill=VB_BLUE)
d.text((12, 15), "Microsoft Visual Basic — LojaTech.vbp — frmGerencial.frm", font=font(13, True),
       fill=WHITE, anchor="lm")
d.rectangle((0, 30, W, 54), fill=(212,212,212))
for i, m in enumerate(["File", "Edit", "View", "Project", "Run", "Debug", "Tools"]):
    d.text((14+i*58, 42), m, font=font(13), fill=(30,30,30), anchor="lm")
d.rectangle((0, 54, W, 82), fill=(200,200,200))
for i in range(14):
    rr(d, (10+i*30, 58, 34+i*30, 78), 3, fill=(230,230,230), outline=(150,150,150))
# project explorer
rr(d, (8, 90, 228, 330), 4, fill=WHITE, outline=(120,120,120))
d.rectangle((8, 90, 228, 112), fill=(10,43,132))
d.text((16, 101), "Project Explorer", font=font(12, True), fill=WHITE, anchor="lm")
for i, n in enumerate(["LojaTech.vbp", "frmGerencial.frm", "mdlConexao.bas", "mdlRelatorios.bas"]):
    sel = (i == 1)
    if sel: d.rectangle((12, 118+i*24, 224, 140+i*24), fill=(10,43,132))
    d.text((24, 129+i*24), n, font=font(12, mono=True), fill=WHITE if sel else (30,30,30), anchor="lm")
# form window
rr(d, (250, 100, 700, 470), 6, fill=(192,192,192), outline=(90,90,90), w=2)
d.rectangle((250, 100, 700, 126), fill=(10,43,132))
d.text((262, 113), "Gerencial — Loja Tech da Turma", font=font(12, True), fill=WHITE, anchor="lm")
rr(d, (268, 140, 682, 300), 3, fill=WHITE, outline=(120,120,120))
for i, ln in enumerate(["1 | Mouse Gamer AzulTech | R$ 89,90 | est: 11",
                        "2 | Teclado Mecânico Turbo | R$ 249,00 | est: 4",
                        "3 | Headset Som de Turma | R$ 179,50 | est: 8",
                        "4 | Webcam FullHD Aula | R$ 199,90 | est: 3"]):
    d.text((276, 152+i*22), ln, font=font(12, mono=True), fill=(30,30,30), anchor="lm")
d.text((268, 312), "Nome:", font=font(12), fill=(30,30,30), anchor="lm")
rr(d, (320, 300, 560, 322), 3, fill=WHITE, outline=(120,120,120))
d.text((268, 340), "Preço:", font=font(12), fill=(30,30,30), anchor="lm")
rr(d, (320, 328, 440, 350), 3, fill=WHITE, outline=(120,120,120))
d.text((452, 340), "Estoque:", font=font(12), fill=(30,30,30), anchor="lm")
rr(d, (512, 328, 580, 350), 3, fill=WHITE, outline=(120,120,120))
for i, b in enumerate(["Adicionar", "Atualizar lista", "Relatório", "Exportar .txt", "Sair"]):
    x = 268 + (i % 3)*140; y = 366 + (i // 3)*40
    rr(d, (x, y, x+130, y+32), 4, fill=(212,212,212), outline=(90,90,90), w=2)
    d.text((x+65, y+16), b, font=font(12, True), fill=(30,30,30), anchor="mm")
rr(d, (268, 448, 682, 464), 3, fill=(192,192,192), outline=(120,120,120))
d.text((276, 456), "Conectado ao MySQL (loja_turma). 8 produto(s).", font=font(11), fill=(30,30,30), anchor="lm")
# code window
rr(d, (716, 100, 1142, 470), 4, fill=WHITE, outline=(120,120,120))
d.rectangle((716, 100, 1142, 122), fill=(212,212,212))
d.text((724, 111), "frmGerencial.frm (Code)", font=font(12, True), fill=(30,30,30), anchor="lm")
code = [
    ("Private Sub cmdAdicionar_Click()", (10,43,132)),
    ("  Dim nome As String", (30,30,30)),
    ("  nome = Trim$(txtNome.Text)", (30,30,30)),
    ("  If Len(nome) < 3 Then", (10,43,132)),
    ("    MsgBox \"Digite 3+ letras\"", (30,30,30)),
    ("    Exit Sub", (10,43,132)),
    ("  End If", (10,43,132)),
    ("  InserirProduto nome, _", (30,30,30)),
    ("    cboCategoria.Text, _", (30,30,30)),
    ("    Val(txtPreco.Text), _", (30,30,30)),
    ("    Val(txtEstoque.Text)", (30,30,30)),
    ("  AtualizarLista", (30,30,30)),
    ("End Sub", (10,43,132)),
]
t = font(12, mono=True)
y = 132
for ln, c in code:
    d.text((726, y), ln, font=t, fill=c); y += 24
# status bar
d.rectangle((0, H-26, W, H), fill=(212,212,212))
d.text((12, H-13), "Pronto  ·  Conectado: loja_turma  ·  Run (F5) para testar", font=font(12), fill=(60,60,60), anchor="lm")
im.save(os.path.join(D, "mock_vb6.png"))
print("mockups 4-7 ok")
