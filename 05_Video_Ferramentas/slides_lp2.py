# -*- coding: utf-8 -*-
"""Desenha os 27 slides ilustrados da vídeo-aula LP2 (VB6 na prática)."""
import os, re
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "slides2")
os.makedirs(OUT, exist_ok=True)
F = os.path.join(ROOT, "fonts")

def font(nome, tam):
    return ImageFont.truetype(os.path.join(F, nome), tam)

FB = lambda t: font("Inter-Bold.ttf", t)
FBL = lambda t: font("Inter-Black.ttf", t)
FR = lambda t: font("Inter-Regular.ttf", t)
FS = lambda t: font("Inter-SemiBold.ttf", t)
MONO = lambda t: font("JetBrainsMono-Bold.ttf", t)
try:
    MONOR = lambda t: font("JetBrainsMono-Regular.ttf", t)
except Exception:
    MONOR = MONO

W, H = 1280, 720
BG   = (246, 243, 236)
NAVY = (18, 38, 58)
AMBER= (242, 163, 60)
GREEN= (30, 123, 52)
RED  = (192, 57, 43)
MUT  = (107, 122, 141)
CODEBG=(22, 32, 46)
CODETX=(232, 237, 242)
WHITE= (255, 255, 255)
PURP = (109, 40, 217)

KW = r"(Dim|As|Integer|String|Private|Public|Sub|End|If|Then|Else|ElseIf|For|To|Next|Print|Val|InputBox|Mod|Date|And|Or|Not|Click|Load)"

def seg_colors(line):
    out, pos = [], 0
    for m in re.finditer(r"('[^']*'|\"[^\"]*\"|' *.*$|" + KW + r")", line):
        if m.start() > pos: out.append((line[pos:m.start()], CODETX))
        t = m.group(0)
        if t[0] in "'\"": c = (152, 195, 121)
        else: c = AMBER
        out.append((t, c)); pos = m.end()
    if pos < len(line): out.append((line[pos:], CODETX))
    return out

def wrap(txt, size, wmax):
    words, lines, cur = txt.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if FR(size).getlength(t) <= wmax: cur = t
        else:
            if cur: lines.append(cur)
            cur = w_
    if cur: lines.append(cur)
    return lines

class S:
    def __init__(self, dark=False):
        self.im = Image.new("RGB", (W, H), (13, 27, 42) if dark else BG)
        self.d = ImageDraw.Draw(self.im)
    def header(self, badge, title, num):
        d = self.d
        d.rectangle([0, 0, W, 96], fill=NAVY)
        d.rounded_rectangle([28, 26, 28 + 13 * len(badge) + 60, 70], 10, fill=AMBER)
        d.text((28 + 30, 33), badge, font=FB(26), fill=NAVY)
        d.text((28 + 13 * len(badge) + 80, 28), title, font=FB(34), fill=WHITE)
        d.text((W - 90, 34), f"{num:02d}/27", font=FS(22), fill=(180, 195, 210))
        d.text((28, H - 34), "LP2 · Turma 2/2026 · VB6 na prática", font=FR(17), fill=MUT)
    def win(self, x, y, w, h, title, url=None):
        d = self.d
        d.rounded_rectangle([x, y, x + w, y + h], 14, fill=WHITE, outline=(210, 205, 195), width=2)
        d.rounded_rectangle([x, y, x + w, y + 40], 14, fill=(228, 224, 214))
        d.rectangle([x, y + 26, x + w, y + 40], fill=(228, 224, 214))
        for i, c in enumerate([(224, 90, 80), (242, 163, 60), (110, 180, 110)]):
            d.ellipse([x + 16 + i * 24, y + 13, x + 30 + i * 24, y + 27], fill=c)
        ty = y + 40
        if url:
            d.rounded_rectangle([x + 14, y + 48, x + w - 14, y + 82], 17, fill=(240, 238, 232))
            d.text((x + 30, y + 55), url, font=MONOR(16), fill=NAVY)
            ty = y + 92
        else:
            d.text((x + 90, y + 10), title, font=FS(16), fill=(90, 90, 90))
            ty = y + 48
        return ty
    def code(self, x, y, w, lines, size=19, lh=30, title=None):
        d = self.d
        h = len(lines) * lh + 26
        d.rounded_rectangle([x, y, x + w, y + h], 12, fill=CODEBG)
        if title:
            d.text((x + 18, y + 8), title, font=MONOR(15), fill=(127, 140, 152))
            y += 24
        for i, ln in enumerate(lines):
            cx = x + 18
            d.text((cx, y + 8 + i * lh), f"{i+1:>2}", font=MONOR(size - 4), fill=(80, 95, 115))
            cx += 44
            for t, c in seg_colors(ln):
                d.text((cx, y + 8 + i * lh), t, font=MONOR(size), fill=c)
                cx += MONOR(size).getlength(t)
        return y + h
    def bullets(self, x, y, items, size=25, gap=14, color=NAVY, wmax=1180):
        d = self.d
        cy = y
        for it in items:
            pref, txt = (it[0], it[1]) if isinstance(it, tuple) else ("•", it)
            d.text((x, cy), pref, font=FS(size), fill=AMBER)
            cx = x + 44
            for ln in wrap(txt, size, wmax - 44):
                d.text((cx, cy), ln, font=FR(size), fill=color)
                cy += size + 12
            cy += gap
        return cy
    def box(self, x, y, w, label, txt, kind="ok"):
        col = {"ok": GREEN, "tente": AMBER, "erro": RED}[kind]
        lines = wrap(txt, 21, w - 70)
        h = 46 + len(lines) * 30
        self.d.rounded_rectangle([x, y, x + w, y + h], 12, fill=(255, 255, 255), outline=col, width=3)
        self.d.rectangle([x, y + 8, x + 8, y + h - 8], fill=col)
        self.d.text((x + 26, y + 10), label, font=FB(20), fill=col)
        cy = y + 40
        for ln in lines:
            self.d.text((x + 26, cy), ln, font=FR(21), fill=NAVY); cy += 30
        return y + h
    def table(self, x, y, cols, rows, widths, hl=None):
        d = self.d
        rh = 40
        d.rounded_rectangle([x, y, x + sum(widths), y + rh], 8, fill=NAVY)
        cx = x
        for c, wd in zip(cols, widths):
            d.text((cx + 12, y + 9), c, font=FS(20), fill=WHITE); cx += wd
        for i, r in enumerate(rows):
            yy = y + rh + i * rh
            fill = (255, 255, 255) if i % 2 == 0 else (238, 235, 228)
            if hl is not None and i == hl: fill = (252, 236, 214)
            d.rectangle([x, yy, x + sum(widths), yy + rh], fill=fill)
            d.line([x, yy + rh, x + sum(widths), yy + rh], fill=(210, 205, 195))
            cx = x
            for c, wd in zip(r, widths):
                d.text((cx + 12, yy + 9), str(c), font=MONOR(17), fill=NAVY); cx += wd
        return y + rh * (len(rows) + 1)
    def save(self, name):
        self.im.save(os.path.join(OUT, name), quality=95)

def chip(d, x, y, txt, fill=NAVY, fg=WHITE, size=20):
    w_ = FS(size).getlength(txt) + 36
    d.rounded_rectangle([x, y, x + w_, y + 40], 20, fill=fill)
    d.text((x + 18, y + 8), txt, font=FS(size), fill=fg)
    return x + w_ + 12

def btn(d, x, y, txt, fill, fg=WHITE, size=20, w=None):
    w_ = w or (FS(size).getlength(txt) + 44)
    d.rounded_rectangle([x, y, x + w_, y + 44], 8, fill=fill)
    d.text((x + 22, y + 10), txt, font=FS(size), fill=fg)
    return x + w_ + 12

def vbbtn(d, x, y, w, h, caption):
    """botão cinza estilo VB6"""
    d.rounded_rectangle([x, y, x + w, y + h], 6, fill=(214, 212, 206), outline=(120, 118, 112), width=2)
    d.line([x + 2, y + 2, x + w - 2, y + 2], fill=(245, 244, 240))
    tw = FR(17).getlength(caption)
    d.text((x + (w - tw) / 2, y + (h - 22) / 2), caption, font=FR(17), fill=(30, 30, 30))

# ---------------------------------------------------------------- slides
def s01():
    s = S(dark=True); d = s.d
    d.rounded_rectangle([90, 120, 1190, 620], 26, fill=(20, 40, 64))
    d.rounded_rectangle([90, 120, 1190, 200], 26, fill=AMBER)
    d.rectangle([90, 176, 1190, 200], fill=AMBER)
    d.text((130, 138), "VIDEOAULA · LINGUAGEM DE PROGRAMAÇÃO II", font=FB(30), fill=NAVY)
    d.text((130, 240), "VB6 na prática:", font=FBL(64), fill=WHITE)
    d.text((130, 316), "do zero ao primeiro programa", font=FBL(48), fill=AMBER)
    d.text((130, 420), "Instalação · pastas do semestre · ola.vbp · par/ímpar · tabuada",
           font=FR(26), fill=(190, 205, 220))
    d.ellipse([1010, 430, 1130, 550], fill=AMBER)
    d.polygon([(1052, 462), (1052, 518), (1102, 490)], fill=NAVY)
    d.text((130, 540), "Prof.ª Raquel · Curso Técnico em Informática · Turma 2/2026",
           font=FS(22), fill=(150, 170, 190))
    s.save("s01.png")

def s02():
    s = S(); d = s.d
    s.header("HOJE", "O que vamos construir juntos", 2)
    y = s.bullets(70, 140, [
        ("1.", "Um formulário que cumprimenta você pelo nome e mostra a data de hoje (Form_Load)."),
        ("2.", "Um botão que lê um número e diz na hora: PAR ou ÍMPAR (If + Mod)."),
        ("3.", "Um botão que imprime a tabuada de 1 a 10 de qualquer número (For...Next)."),
        ("4.", "No papel: o algoritmo da média com as três estruturas (sequência, seleção, repetição)."),
    ], size=26, gap=20)
    s.box(70, y + 10, 1140, "SEM LABORATÓRIO HOJE?",
          "Sem problema: assista e acompanhe na tela. Cada clique aparece aqui, devagarzinho. "
          "Quando você tiver um computador, é só repetir os passos.", kind="tente")
    s.save("s02.png")

def s03():
    s = S(); d = s.d
    s.header("PASSO 1", "Conhecendo o VB6", 3)
    s.bullets(70, 140, [
        ("•", "VB6 = Visual Basic 6: ambiente visual da Microsoft para criar programas com janelas e botões."),
        ("•", "Você DESENHA a tela (formulário) e escreve o código atrás de cada clique."),
        ("•", "F5 roda o programa na hora — ver funcionando é a melhor parte."),
        ("•", "Usamos ele na escola porque mostra as três estruturas acontecendo na tela."),
    ], size=26, gap=18)
    ty = s.win(760, 380, 450, 210, "Instalador")
    d.text((790, ty + 16), "  setup.exe", font=MONO(24), fill=NAVY)
    d.text((790, ty + 60), "clique com o botão direito", font=FR(20), fill=MUT)
    d.text((790, ty + 92), "→ Propriedades", font=FS(22), fill=GREEN)
    s.box(70, 430, 640, "ONDE ENCONTRAR",
          "Pasta do instalador enviada pela professora (ou pen drive da escola). "
          "No PC do laboratório, ele já vem instalado — pule para o slide 5.", kind="ok")
    s.save("s03.png")

def s04():
    s = S(); d = s.d
    s.header("PASSO 1", "Compatibilidade: o segredo da instalação", 4)
    ty = s.win(120, 130, 620, 470, "setup.exe — Propriedades")
    d.text((150, ty + 14), "Compatibilidade", font=FB(24), fill=NAVY)
    d.rectangle([150, ty + 56, 176, ty + 82], outline=GREEN, width=3)
    d.text((155, ty + 56), "X", font=FB(24), fill=GREEN)
    d.text((190, ty + 58), "Executar em modo de compatibilidade:", font=FR(21), fill=NAVY)
    d.rounded_rectangle([190, ty + 96, 560, ty + 134], 8, fill=WHITE, outline=(150, 150, 150), width=2)
    d.text((204, ty + 104), "Windows 7  (ou Windows XP)", font=FR(20), fill=NAVY)
    d.rectangle([150, ty + 160, 176, ty + 186], outline=GREEN, width=3)
    d.text((155, ty + 160), "X", font=FB(24), fill=GREEN)
    d.text((190, ty + 162), "Executar este programa como administrador", font=FR(21), fill=NAVY)
    btn(d, 440, ty + 230, "OK", (214, 212, 206), fg=(30, 30, 30), w=120)
    s.bullets(790, 160, [
        ("1)", "Botão direito no setup.exe → Propriedades."),
        ("2)", "Aba Compatibilidade."),
        ("3)", "Marque as DUAS caixinhas ao lado."),
        ("4)", "OK → dois cliques no setup → assistente padrão."),
        ("5)", "Reinicie o PC no final."),
    ], size=23, gap=16, wmax=450)
    s.save("s04.png")

def s05():
    s = S(); d = s.d
    s.header("PASSO 1", "Abrir o VB6 (se já está instalado)", 5)
    ty = s.win(140, 150, 560, 330, "Menu Iniciar do Windows")
    d.rounded_rectangle([170, ty + 10, 670, ty + 52], 10, fill=(240, 238, 232))
    d.text((186, ty + 18), "Digite: Visual Basic 6", font=MONOR(22), fill=NAVY)
    d.rounded_rectangle([170, ty + 66, 670, ty + 122], 10, fill=(232, 240, 250))
    d.text((186, ty + 80), "► Microsoft Visual Basic 6.0", font=FS(22), fill=NAVY)
    d.text((186, ty + 150), "← clique aqui para abrir", font=FS(21), fill=GREEN)
    s.bullets(760, 170, [
        ("✓", "Instalou em casa? Depois de reiniciar, abra pelo Menu Iniciar também."),
        ("✓", "Primeira abertura pode demorar uns segundos — é normal."),
        ("✓", "Apareceu a janela NOVO PROJETO? Está tudo certo: siga comigo."),
    ], size=24, gap=20, wmax=440)
    s.box(140, 520, 1000, "LEMBRETE CARINHOSO",
          "Se algo travar na instalação, não insista: anote a mensagem e me mande no portal. "
          "Ninguém fica sem programar por causa de instalador.", kind="tente")
    s.save("s05.png")

def s06():
    s = S(); d = s.d
    s.header("PASSO 2", "As pastas do semestre", 6)
    d.rounded_rectangle([120, 130, 700, 560], 16, fill=WHITE, outline=(210, 205, 195), width=2)
    d.text((150, 150), "Documentos", font=MONO(24), fill=NAVY)
    linhas = [("└── ", "LP2\\", NAVY, True),
              ("    ├── ", "S01\\   ← aula de hoje", GREEN, True),
              ("    ├── ", "S02\\", NAVY, False),
              ("    ├── ", "S03\\", NAVY, False),
              ("    ├── ", "S04\\", NAVY, False),
              ("    └── ", "PROJETO\\   ← trabalho final", PURP, True)]
    y = 200
    for pref, txt, cor, hl in linhas:
        if hl:
            d.rounded_rectangle([150, y - 6, 670, y + 34], 8, fill=(250, 246, 236))
        d.text((160, y), pref + txt, font=MONO(24), fill=cor)
        y += 52
    s.bullets(760, 160, [
        ("1)", "Explorador de Arquivos → Documentos."),
        ("2)", "Botão direito → Novo → Pasta: LP2."),
        ("3)", "Dentro dela: S01, S02, S03, S04 e PROJETO."),
        ("•", "Cada etapa do semestre mora na sua pasta."),
        ("•", "Todo projeto seu terá endereço fixo. Sempre."),
    ], size=24, gap=16, wmax=450)
    s.save("s06.png")

def s07():
    s = S(); d = s.d
    s.header("PASSO 2", "Por que organizar antes de programar?", 7)
    s.bullets(70, 150, [
        ("!", "O erro nº 1 da aula não é de código: é arquivo salvo “em qualquer lugar”."),
        ("→", "Com pastas, a professora acha seu trabalho — e você também."),
        ("", "Na prova e no projeto final, organização economiza minutos preciosos."),
        ("✓", "Organizar por fora ensina a organizar por dentro: código também é estrutura."),
    ], size=26, gap=22)
    s.box(70, 470, 1140, "COMBINADO DA TURMA",
          "Daqui pra frente, toda vez que salvar um projeto: pasta certa, nome certo. "
          "“Salvei na área de trabalho” vira piada interna — das antigas.", kind="ok")
    s.save("s07.png")

def s08():
    s = S(); d = s.d
    s.header("PASSO 3", "O palco: o formulário (Form)", 8)
    d.rounded_rectangle([330, 150, 950, 560], 12, fill=(238, 236, 230), outline=(120, 118, 112), width=3)
    d.rectangle([330, 150, 950, 186], fill=(18, 38, 58))
    d.text((346, 156), "Form1", font=FS(20), fill=WHITE)
    d.text((900, 156), "—  □  x", font=FS(18), fill=(180, 195, 210))
    vbbtn(d, 380, 460, 220, 56, "Command1")
    vbbtn(d, 640, 460, 220, 56, "Command2")
    d.text((380, 220), "área cinza = palco do programa", font=FR(21), fill=MUT)
    d.ellipse([560, 300, 700, 400], outline=AMBER, width=4)
    s.bullets(70, 590, [("•", "Tudo que o usuário vê e clica acontece no formulário. Botões, textos, imagens: é aqui.")],
              size=23, gap=8, wmax=1160)
    s.save("s08.png")

def s09():
    s = S(); d = s.d
    s.header("PASSO 3", "Caixa de ferramentas + Propriedades", 9)
    d.rounded_rectangle([90, 140, 300, 560], 12, fill=WHITE, outline=(150, 150, 150), width=2)
    d.text((110, 152), "Toolbox", font=FB(20), fill=NAVY)
    ico = ["□", "A", "T", "○", "■", "●"]
    for i, t in enumerate(ico):
        x = 110 + (i % 2) * 90; y = 195 + (i // 2) * 90
        d.rounded_rectangle([x, y, x + 76, y + 76], 8, fill=(238, 240, 244),
                            outline=(AMBER if t == "●" else (170, 170, 170)), width=3)
        d.text((x + 24, y + 22), t, font=FB(30), fill=NAVY)
    d.text((110, 480), "● = CommandButton (botão)", font=FS(18), fill=GREEN)
    d.rounded_rectangle([360, 140, 760, 560], 12, fill=WHITE, outline=(150, 150, 150), width=2)
    d.text((380, 152), "Propriedades", font=FB(20), fill=NAVY)
    props = [("(Name)", "btnParImpar"), ("Caption", "Par ou Ímpar?"), ("BackColor", "&H8000000F&"),
             ("Height", "400"), ("Width", "1200")]
    y = 200
    for k, v in props:
        d.text((380, y), k, font=MONOR(19), fill=MUT)
        d.text((520, y), v, font=MONO(19), fill=NAVY)
        y += 46
    s.bullets(800, 170, [
        ("→", "Toolbox: clique no ícone e desenhe a peça no form."),
        ("→", "Propriedades: ajuste nome, texto, cor, tamanho."),
        ("✓", "(Name) é como o CÓDIGO chama a peça."),
        ("✓", "Caption é o texto que a PESSOA vê."),
    ], size=23, gap=18, wmax=440)
    s.save("s09.png")

def s10():
    s = S(); d = s.d
    s.header("PASSO 3", "Projeto e código: a cozinha", 10)
    d.rounded_rectangle([90, 140, 430, 430], 12, fill=WHITE, outline=(150, 150, 150), width=2)
    d.text((110, 152), "Project1", font=FB(20), fill=NAVY)
    d.text((120, 200), "+ Form1.frm", font=MONOR(20), fill=NAVY)
    d.text((120, 240), "+ ola.vbp", font=MONOR(20), fill=GREEN)
    d.text((110, 300), "janela do projeto:", font=FR(18), fill=MUT)
    d.text((110, 330), "os arquivos organizados", font=FR(18), fill=MUT)
    y = s.code(480, 140, 720, [
        "Private Sub Form_Load()",
        "    Print \"Olá!\"",
        "End Sub",
    ], size=20, lh=30, title="janela de código — dois cliques no form")
    s.bullets(480, y + 20, [
        ("→", "Código = cozinha: onde os comandos viram ação."),
        ("→", "Dois cliques em qualquer peça abre o código dela."),
    ], size=23, gap=12, wmax=700)
    s.save("s10.png")

def s11():
    s = S(); d = s.d
    s.header("PASSO 4", "Novo projeto: Standard EXE", 11)
    d.rounded_rectangle([240, 140, 1040, 560], 14, fill=WHITE, outline=(120, 118, 112), width=3)
    d.rectangle([240, 140, 1040, 184], fill=(18, 38, 58))
    d.text((260, 150), "Novo Projeto", font=FS(22), fill=WHITE)
    opcs = ["Standard EXE", "ActiveX DLL", "ActiveX EXE", "ActiveX Control"]
    y = 220
    for i, o in enumerate(opcs):
        sel = i == 0
        d.rounded_rectangle([280, y, 700, y + 56], 8,
                            fill=(252, 236, 214) if sel else (244, 244, 242),
                            outline=AMBER if sel else (190, 190, 188), width=3 if sel else 1)
        d.text((304, y + 14), ("►  " if sel else "   ") + o, font=FS(22), fill=NAVY)
        y += 68
    btn(d, 760, 470, "OK", (18, 38, 58), w=120)
    btn(d, 900, 470, "Cancelar", (214, 212, 206), fg=(30, 30, 30), w=120)
    d.text((760, 240), "escolha o primeiro:", font=FS(21), fill=GREEN)
    d.text((760, 272), "Standard EXE", font=FB(26), fill=NAVY)
    d.text((760, 320), "= programa com janela,", font=FR(20), fill=MUT)
    d.text((760, 348), "do jeitinho que usamos", font=FR(20), fill=MUT)
    s.save("s11.png")

def s12():
    s = S(); d = s.d
    s.header("PASSO 4", "Regra de ouro: SALVE ANTES do código", 12)
    ty = s.win(120, 140, 640, 420, "Salvar projeto como…", url="Documentos > LP2 > S01")
    d.text((150, ty + 14), "Nome do arquivo:", font=FR(20), fill=MUT)
    d.rounded_rectangle([150, ty + 46, 600, ty + 86], 8, fill=WHITE, outline=(150, 150, 150), width=2)
    d.text((164, ty + 54), "ola.vbp", font=MONO(22), fill=NAVY)
    d.text((150, ty + 106), "antes dele, salve também:", font=FR(19), fill=MUT)
    d.text((150, ty + 136), "Form1.frm  (o formulário)", font=MONO(21), fill=GREEN)
    btn(d, 460, ty + 200, "Salvar", (18, 38, 58), w=140)
    s.bullets(800, 170, [
        ("1)", "Arquivo → Salvar Projeto Como…"),
        ("2)", "Formulário: Form1.frm em LP2\\S01."),
        ("3)", "Projeto: ola.vbp na MESMA pasta."),
        ("!", "Só depois disso escreva código."),
    ], size=24, gap=18, wmax=440)
    s.box(800, 420, 400, "POR QUÊ?",
          "Projeto salvo = endereço fixo. Nada de .vbp perdido na área de trabalho.", kind="tente")
    s.save("s12.png")

def s13():
    s = S(); d = s.d
    s.header("PASSO 4", "Form_Load: o cumprimento", 13)
    y = s.code(80, 140, 660, [
        "Private Sub Form_Load()",
        "    Print \"Olá, eu sou a Prof.ª Raquel!\"",
        "    Print \"Hoje é \" & Date",
        "End Sub",
    ], size=21, lh=34, title="dois cliques no form → janela de código")
    s.bullets(80, y + 18, [
        ("▶", "F5 roda: o form abre e as linhas aparecem impressas nele."),
        ("&", "junta texto com valor (concatenar). Date = data de hoje."),
    ], size=22, gap=10)
    d.rounded_rectangle([790, 160, 1190, 470], 12, fill=(238, 236, 230), outline=(120, 118, 112), width=3)
    d.rectangle([790, 160, 1190, 194], fill=(18, 38, 58))
    d.text((806, 166), "Form1  (rodando)", font=FS(19), fill=WHITE)
    d.text((820, 230), "Olá, eu sou a Prof.ª Raquel!", font=MONO(20), fill=NAVY)
    d.text((820, 275), "Hoje é 18/09/2026", font=MONO(20), fill=GREEN)
    d.text((820, 350), "← o Print escreve aqui,", font=FR(19), fill=MUT)
    d.text((820, 378), "direto no formulário", font=FR(19), fill=MUT)
    s.save("s13.png")

def s14():
    s = S(); d = s.d
    s.header("PAUSA", "Errar faz parte — e o VB6 ajuda", 14)
    y = s.code(80, 140, 640, [
        "Private Sub Form_Load()",
        "    Print \"Olá, eu sou a Prof.ª Raquel!",
        "    Print \"Hoje é \" & Date",
        "End Sub",
    ], size=21, lh=34, title="quebrei de propósito: faltou a aspa final")
    d.rounded_rectangle([96, 140 + 26 + 34, 700, 140 + 26 + 68], 6, outline=RED, width=4)
    d.rounded_rectangle([760, 200, 1190, 400], 12, fill=WHITE, outline=RED, width=3)
    d.text((786, 216), "⚠  Erro de compilação:", font=FB(21), fill=RED)
    d.text((786, 252), "esperado: fim da linha / aspa", font=MONOR(18), fill=NAVY)
    d.text((786, 300), "ele APONTA a linha pra você", font=FR(19), fill=MUT)
    d.text((786, 330), "respire, leia, corrija uma coisa por vez", font=FS(19), fill=GREEN)
    s.bullets(80, y + 16, [("✓", "Mensagem de erro não é bronca: é o programa mostrando onde dói.")], size=22)
    s.save("s14.png")

def s15():
    s = S(); d = s.d
    s.header("PAUSA", "Três dicas que valem ouro", 15)
    s.box(70, 150, 1140, "1 · SUB ABRE E FECHA",
          "Todo procedimento começa com Private Sub e termina com End Sub. "
          "Faltou End Sub? Nada roda.", kind="ok")
    s.box(70, 300, 1140, "2 · TEXTO ENTRE ASPAS",
          "Texto vai entre aspas: \"Olá\". Número vai sem aspas: 7. "
          "Aspas trocadas são o erro mais comum da primeira semana.", kind="ok")
    s.box(70, 450, 1140, "3 · CTRL+S SEMPRE",
          "Salve a cada mudança, na sua pasta. Código bom é código salvo.", kind="ok")
    s.save("s15.png")

def s16():
    s = S(); d = s.d
    s.header("EXERCÍCIO 1", "A média no papel — começo", 16)
    s.bullets(70, 130, [
        ("•", "Leia 3 notas, calcule a média e imprima a situação (>=7 aprovado; >=5 recuperação; senão reprovado)."),
        ("→", "Use as três estruturas: sequência, seleção e repetição."),
    ], size=24, gap=12, wmax=1160)
    s.code(70, 250, 1140, [
        "algoritmo Media_da_Turma",
        "var nota, soma, media : real;  i : inteiro",
        "inicio",
        "    soma <- 0",
        "    para i de 1 ate 3 faca",
        "        leia(nota)",
        "        soma <- soma + nota",
        "    fim-para",
    ], size=21, lh=33, title="pseudocódigo — parte 1 (repetição)")
    d.rounded_rectangle([806, 250 + 26 + 4 * 33, 1180, 250 + 26 + 5 * 33 + 8], 6, outline=AMBER, width=4)
    d.text((70, 600), "← o laço lê as 3 notas sem repetir o “leia” três vezes", font=FS(21), fill=GREEN)
    s.save("s16.png")

def s17():
    s = S(); d = s.d
    s.header("EXERCÍCIO 1", "A média no papel — decisão", 17)
    s.code(70, 130, 1140, [
        "    media <- soma / 3",
        "    se media >= 7 entao",
        "        escreva(\"APROVADO com media \", media)",
        "    senao-se media >= 5 entao",
        "        escreva(\"RECUPERACAO com media \", media)",
        "    senao",
        "        escreva(\"REPROVADO com media \", media)",
        "    fim-se",
        "fim",
    ], size=21, lh=33, title="pseudocódigo — parte 2 (sequência + seleção)")
    x = chip(s.d, 90, 560, "SEQUÊNCIA: passos em ordem", GREEN)
    x = chip(s.d, x, 560, "SELEÇÃO: se / senao-se / senao", AMBER, fg=NAVY)
    chip(s.d, x, 560, "REPETIÇÃO: para...faca", PURP)
    s.save("s17.png")

def s18():
    s = S(); d = s.d
    s.header("EXERCÍCIO 1", "Testando o algoritmo na lousa", 18)
    s.table(90, 150, ["passo", "nota lida", "soma acumulada"],
            [["i = 1", "6", "0 + 6 = 6"],
             ["i = 2", "8", "6 + 8 = 14"],
             ["i = 3", "7", "14 + 7 = 21"]],
            [220, 260, 380], hl=2)
    s.box(90, 350, 520, "MÉDIA", "21 ÷ 3 = 7  →  média >= 7  →  “APROVADO com media 7”.", kind="ok")
    s.box(650, 350, 560, "OUTROS CASOS",
          "4, 5, 6 → média 5 → RECUPERAÇÃO.   2, 3, 4 → média 3 → REPROVADO. "
          "Teste os três na lousa: a seleção mostra a cara.", kind="tente")
    s.bullets(90, 540, [("•", "Na prova escrita: laço + divisão + se encadeado + onde está cada estrutura.")], size=23)
    s.save("s18.png")

def s19():
    s = S(); d = s.d
    s.header("EXERCÍCIO 3A", "Desenhando o botão Par ou Ímpar", 19)
    d.rounded_rectangle([90, 140, 640, 520], 12, fill=(238, 236, 230), outline=(120, 118, 112), width=3)
    d.rectangle([90, 140, 640, 176], fill=(18, 38, 58))
    d.text((106, 146), "Form1", font=FS(19), fill=WHITE)
    vbbtn(d, 140, 400, 240, 60, "Par ou Ímpar?")
    d.rounded_rectangle([136, 396, 384, 464], 6, outline=AMBER, width=4)
    d.text((140, 210), "1) Toolbox → CommandButton", font=FR(20), fill=MUT)
    d.text((140, 240), "2) clique dentro do form", font=FR(20), fill=MUT)
    d.text((140, 270), "3) ajuste em Propriedades →", font=FR(20), fill=GREEN)
    d.rounded_rectangle([690, 140, 1190, 430], 12, fill=WHITE, outline=(150, 150, 150), width=2)
    d.text((710, 152), "Propriedades", font=FB(20), fill=NAVY)
    d.text((710, 210), "(Name)", font=MONOR(20), fill=MUT)
    d.text((860, 210), "btnParImpar", font=MONO(20), fill=NAVY)
    d.text((710, 260), "Caption", font=MONOR(20), fill=MUT)
    d.text((860, 260), "Par ou Ímpar?", font=MONO(20), fill=NAVY)
    d.text((710, 330), "(Name) = chama no código", font=FR(18), fill=MUT)
    d.text((710, 360), "Caption = pessoa vê", font=FR(18), fill=MUT)
    s.bullets(90, 560, [("→", "Dois cliques no botão abre a janela de código dele: btnParImpar_Click().")], size=23)
    s.save("s19.png")

def s20():
    s = S(); d = s.d
    s.header("EXERCÍCIO 3A", "O código do par ou ímpar", 20)
    s.code(90, 140, 1100, [
        "Private Sub btnParImpar_Click()",
        "    Dim n As Integer",
        "    n = Val(InputBox(\"Digite um número inteiro:\"))",
        "    If n Mod 2 = 0 Then",
        "        Print n & \" é PAR\"",
        "    Else",
        "        Print n & \" é ÍMPAR\"",
        "    End If",
        "End Sub",
    ], size=22, lh=36, title="btnParImpar_Click")
    s.bullets(90, 520, [
        ("", "InputBox abre a janelinha que pergunta; Val transforma o TEXTO digitado em número."),
        ("/", "Mod = resto da divisão: 7 Mod 2 = 1 (ímpar) · 10 Mod 2 = 0 (par)."),
    ], size=23, gap=12)
    s.save("s20.png")

def s21():
    s = S(); d = s.d
    s.header("EXERCÍCIO 3A", "Teste na tela: 7 e 10", 21)
    d.rounded_rectangle([90, 150, 620, 330], 12, fill=WHITE, outline=(120, 118, 112), width=3)
    d.rectangle([90, 150, 620, 186], fill=(18, 38, 58))
    d.text((106, 156), "InputBox — pergunta", font=FS(19), fill=WHITE)
    d.text((116, 206), "Digite um número inteiro:", font=FR(21), fill=NAVY)
    d.rounded_rectangle([116, 244, 470, 284], 6, fill=WHITE, outline=(150, 150, 150), width=2)
    d.text((130, 252), "7", font=MONO(22), fill=NAVY)
    btn(d, 486, 244, "OK", (214, 212, 206), fg=(30, 30, 30), w=90)
    d.rounded_rectangle([680, 150, 1190, 330], 12, fill=(238, 236, 230), outline=(120, 118, 112), width=3)
    d.rectangle([680, 150, 1190, 186], fill=(18, 38, 58))
    d.text((696, 156), "Form1", font=FS(19), fill=WHITE)
    d.text((710, 230), "7 é ÍMPAR", font=MONO(30), fill=RED)
    d.rounded_rectangle([90, 380, 620, 560], 12, fill=(238, 236, 230), outline=(120, 118, 112), width=3)
    d.rectangle([90, 380, 620, 416], fill=(18, 38, 58))
    d.text((106, 386), "Form1", font=FS(19), fill=WHITE)
    d.text((120, 460), "10 é PAR", font=MONO(30), fill=GREEN)
    s.bullets(680, 400, [
        ("▶", "F5 → clique no botão → digite → veja o Print no form."),
        ("→", "Teste vários números: o If decide sempre certinho."),
    ], size=23, gap=16, wmax=480)
    s.save("s21.png")

def s22():
    s = S(); d = s.d
    s.header("EXERCÍCIO 3B", "O botão da tabuada", 22)
    d.rounded_rectangle([90, 140, 640, 470], 12, fill=(238, 236, 230), outline=(120, 118, 112), width=3)
    d.rectangle([90, 140, 640, 176], fill=(18, 38, 58))
    d.text((106, 146), "Form1", font=FS(19), fill=WHITE)
    vbbtn(d, 140, 380, 220, 56, "Par ou Ímpar?")
    vbbtn(d, 390, 380, 220, 56, "Tabuada 1 a 10")
    d.rounded_rectangle([386, 376, 614, 440], 6, outline=AMBER, width=4)
    d.rounded_rectangle([690, 140, 1190, 380], 12, fill=WHITE, outline=(150, 150, 150), width=2)
    d.text((710, 152), "Propriedades", font=FB(20), fill=NAVY)
    d.text((710, 205), "(Name)", font=MONOR(20), fill=MUT)
    d.text((860, 205), "btnTabuada", font=MONO(20), fill=NAVY)
    d.text((710, 255), "Caption", font=MONOR(20), fill=MUT)
    d.text((860, 255), "Tabuada 1 a 10", font=MONO(20), fill=NAVY)
    s.bullets(90, 510, [("→", "Mesmo esquema: desenhar → nomear → dois cliques → código.")], size=23)
    s.save("s22.png")

def s23():
    s = S(); d = s.d
    s.header("EXERCÍCIO 3B", "For...Next: repetir sem cansar", 23)
    s.code(90, 140, 1100, [
        "Private Sub btnTabuada_Click()",
        "    Dim n As Integer, i As Integer",
        "    n = Val(InputBox(\"Tabuada de qual número?\"))",
        "    For i = 1 To 10",
        "        Print n & \" x \" & i & \" = \" & n * i",
        "    Next i",
        "End Sub",
    ], size=22, lh=36, title="btnTabuada_Click")
    d.rounded_rectangle([196, 140 + 26 + 3 * 36, 1160, 140 + 26 + 5 * 36 + 6], 6, outline=AMBER, width=4)
    s.bullets(90, 480, [
        ("→", "For i = 1 To 10: i começa em 1, sobe de 1 em 1, para no 10."),
        ("•", "O & cola os pedaços: número, “ x ”, contador, “ = ”, resultado."),
    ], size=23, gap=12)
    s.save("s23.png")

def s24():
    s = S(); d = s.d
    s.header("EXERCÍCIO 3B", "A tabuada do 7, linha a linha", 24)
    d.rounded_rectangle([120, 130, 620, 620], 12, fill=(238, 236, 230), outline=(120, 118, 112), width=3)
    d.rectangle([120, 130, 620, 166], fill=(18, 38, 58))
    d.text((136, 136), "Form1 — rodando", font=FS(19), fill=WHITE)
    y = 190
    for i in range(1, 11):
        d.text((160, y), f"7 x {i:>2} = {7*i:>2}", font=MONO(22), fill=NAVY if i != 10 else GREEN)
        y += 42
    s.bullets(680, 180, [
        ("→", "Dez linhas impressas sem escrever dez Prints."),
        ("✓", "Isso é REPETIÇÃO: o For fez o trabalho repetido por você."),
        ("★", "Junto com o If do outro botão: as três estruturas vivas no mesmo form."),
    ], size=24, gap=22, wmax=480)
    s.save("s24.png")

def s25():
    s = S(); d = s.d
    s.header("CHECKLIST", "Conferindo tudo antes de fechar", 25)
    itens = ["Pastas LP2\\S01..S04 + PROJETO criadas",
             "ola.vbp + Form1.frm salvos dentro de S01",
             "Form_Load imprime nome e data (Print + Date)",
             "btnParImpar: InputBox + Val + If com Mod",
             "btnTabuada: For...Next imprimindo 1 a 10",
             "F5 rodou tudo · Ctrl+S salvou tudo"]
    y = 150
    for it in itens:
        d.rounded_rectangle([90, y, 1190, y + 62], 12, fill=WHITE, outline=(188, 217, 188), width=2)
        d.ellipse([110, y + 15, 140, y + 45], fill=GREEN)
        d.text((117, y + 18), "✓", font=FB(20), fill=WHITE)
        d.text((160, y + 18), it, font=FS(22), fill=NAVY)
        y += 74
    s.save("s25.png")

def s26():
    s = S(); d = s.d
    s.header("E AGORA?", "Para onde ir depois do vídeo", 26)
    s.bullets(70, 150, [
        ("→", "AulaViva → Módulo 2: cartas novas, checkpoints e um chefe novinho esperando você."),
        ("•", "Materiais da turma: apostila, listas e o guia prático com os passos de hoje."),
        ("•", "Esta videoaula fica no kit da sala e no app: reassista quantas vezes quiser."),
        ("•", "Nos módulos do app tem áudio opcional: aperte em Ouvir se quiser, ignore se preferir ler."),
    ], size=25, gap=20)
    s.box(70, 470, 1140, "DICA DE QUEM ENSINA",
          "Refazer o ola.vbp do zero, sem olhar o vídeo, é o melhor estudo para a prova. "
          "Se travar, volte no trecho — errar e consertar É estudar.", kind="ok")
    s.save("s26.png")

def s27():
    s = S(dark=True); d = s.d
    d.rounded_rectangle([90, 110, 1190, 610], 26, fill=(20, 40, 64))
    d.text((130, 170), "Você chegou até aqui.", font=FBL(52), fill=WHITE)
    d.text((130, 260), "Programar é isso: organizar, tentar, quebrar, consertar —", font=FR(27), fill=(190, 205, 220))
    d.text((130, 300), "e celebrar cada botão que funciona.", font=FR(27), fill=(190, 205, 220))
    d.text((130, 380), "Exercício 1, 2 e 3 do Módulo 1?", font=FS(27), fill=AMBER)
    d.text((130, 420), "Feitos. E, melhor: entendidos.", font=FS(27), fill=AMBER)
    d.text((130, 510), "Te vejo na próxima aula.  ·  Prof.ª Raquel · Turma 2/2026", font=FS(23), fill=(150, 170, 190))
    s.save("s27.png")

if __name__ == "__main__":
    for i in range(1, 28):
        globals()[f"s{i:02d}"]()
        print(f"s{i:02d} ok")
