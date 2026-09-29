# -*- coding: utf-8 -*-
"""Desenha os 27 slides ilustrados da vídeo-aula PI-I (Loja Tech da Turma)."""
import os, re
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "slides")
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

KW = r"(SELECT|FROM|WHERE|ORDER BY|INSERT INTO|VALUES|BEGIN|COMMIT|ROLLBACK|FOR UPDATE|foreach|if|else|echo|include|require|function|new|try|catch|exit|die|<\?php|\?>)"

def seg_colors(line):
    out, pos = [], 0
    for m in re.finditer(r"('[^']*'|\"[^\"]*\"|//.*$|#.*$|" + KW + r"|\$\w+)", line):
        if m.start() > pos: out.append((line[pos:m.start()], CODETX))
        t = m.group(0)
        if t[0] in "'\"": c = (152, 195, 121)
        elif t.startswith("//") or t.startswith("#"): c = (127, 140, 152)
        elif t.startswith("$"): c = (97, 175, 239)
        else: c = AMBER
        out.append((t, c)); pos = m.end()
    if pos < len(line): out.append((line[pos:], CODETX))
    return out

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
        d.text((28, H - 34), "PI-I · Turma 2/2026 · Loja Tech da Turma", font=FR(17), fill=MUT)
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
        d = self.d
        col = {"ok": GREEN, "tente": AMBER, "erro": RED}[kind]
        lines = wrap(txt, 21, w - 70)
        h = 46 + len(lines) * 30
        d.rounded_rectangle([x, y, x + w, y + h], 12, fill=(255, 255, 255), outline=col, width=3)
        d.rectangle([x, y + 8, x + 8, y + h - 8], fill=col)
        d.text((x + 26, y + 10), label, font=FB(20), fill=col)
        cy = y + 40
        for ln in lines:
            d.text((x + 26, cy), ln, font=FR(21), fill=NAVY); cy += 30
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

# ---------------------------------------------------------------- slides
def s01():
    s = S(dark=True); d = s.d
    d.rectangle([0, 0, W, H], fill=(13, 27, 42))
    d.rounded_rectangle([70, 80, 380, 130], 25, fill=AMBER)
    d.text((95, 90), "VÍDEO-AULA · PI-I", font=FB(26), fill=NAVY)
    d.text((70, 180), "Loja Tech", font=FBL(92), fill=WHITE)
    d.text((70, 285), "da Turma", font=FBL(92), fill=AMBER)
    d.text((72, 405), "Instalação, banco de dados e loja no ar — passo a passo,", font=FR(30), fill=(200, 212, 224))
    d.text((72, 447), "explicado com calma, como se fosse a primeira vez.", font=FR(30), fill=(200, 212, 224))
    x = 72
    for t in ("VS Code", "XAMPP", "MySQL", "PHP", "VB6"):
        x = chip(d, x, 520, t, fill=(30, 48, 68), fg=(220, 230, 240))
    d.text((72, 600), "Turma 2/2026 · Prof.ª Raquel · pause quando quiser: o vídeo é seu", font=FS(24), fill=(150, 168, 186))
    s.save("s01.png")

def s02():
    s = S(); d = s.d
    s.header("MAPA", "As 5 paradas do vídeo", 2)
    y = 130
    for i, (t, sub) in enumerate([
        ("Instalar o VS Code", "o caderno com superpoderes onde a gente escreve o site"),
        ("Instalar o XAMPP", "a caixa que transforma seu PC em servidor (Apache + MySQL + PHP)"),
        ("Criar o banco loja_turma", "o armário organizado: produtos, clientes, pedidos"),
        ("Loja no ar no navegador", "vitrine, produto, pagamento — e uma compra de verdade"),
        ("Espiar o código", "conexão, SELECT, foreach e o pedido com cinto de segurança")], 1):
        d.ellipse([60, y, y and 60 + 56, y + 56], fill=AMBER)
        d.text((78, y + 10), str(i), font=FBL(30), fill=NAVY)
        d.text((140, y + 2), t, font=FB(30), fill=NAVY)
        d.text((140, y + 40), sub, font=FR(22), fill=MUT)
        if i < 5: d.line([88, y + 56, 88, y + 88], fill=(200, 195, 185), width=4)
        y += 92
    s.box(60, 600, 1160, "COMBINADO", "Errar faz parte: se algo der errado, é só uma etapa fora de ordem — a gente resolve junto.", "tente")
    s.save("s02.png")

def s03():
    s = S(); d = s.d
    s.header("PASSO 1", "Baixar o VS Code no site oficial", 3)
    y = s.win(60, 120, 1160, 460, "", url="https://code.visualstudio.com")
    d.text((110, y + 20), "Visual Studio Code", font=FBL(52), fill=(0, 102, 180))
    d.text((110, y + 88), "Edição de código reimaginada. Gratuita e de código aberto.", font=FR(26), fill=MUT)
    btn(d, 110, y + 150, "Download for Windows", (0, 120, 200))
    d.text((110, y + 214), "botão azul grande = instalador certo pro seu Windows", font=FR(21), fill=MUT)
    s.box(60, 592, 1160, "SÓ O OFICIAL", "Sempre code.visualstudio.com — site estranho é o erro mais comum desta etapa.", "erro")
    s.save("s03.png")

def s04():
    s = S(); d = s.d
    s.header("PASSO 1", "Instalador: a telinha que não pode passar batida", 4)
    y = s.win(160, 120, 960, 470, "Setup - Visual Studio Code")
    d.text((200, y + 16), "Selecionar tarefas adicionais", font=FB(28), fill=NAVY)
    yy = y + 70
    for txt, on, star in ([("Criar atalho na área de trabalho", True, False),
                           ("Adicionar ao PATH (requer reinício)", True, True),
                           ("Registrar o code como editor suportado", True, True),
                           ("Adicionar ao menu de contexto do Explorer", False, False)]):
        d.rectangle([200, yy, 232, yy + 32], fill=WHITE, outline=NAVY, width=2)
        if on: d.text((205, yy - 2), "X", font=FB(26), fill=GREEN)
        col = NAVY
        d.text((248, yy + 2), txt, font=FR(24), fill=col)
        if star:
            d.rounded_rectangle([200 - 8, yy - 8, 900, yy + 40], 8, outline=AMBER, width=4)
        yy += 56
    d.text((200, yy + 6), "essas duas caixinhas fazem o “Abrir com Code” funcionar depois", font=FS(22), fill=AMBER)
    btn(d, 760, y + 350, "< Voltar", (200, 196, 186), fg=NAVY)
    btn(d, 900, y + 350, "Avançar >", (0, 120, 200))
    s.save("s04.png")

def s05():
    s = S(dark=True); d = s.d
    d.rectangle([0, 0, W, H], fill=(13, 27, 42))
    s.header("PASSO 1", "VS Code aberto: Arquivo › Abrir Pasta", 5)
    d.rounded_rectangle([60, 120, 1220, 660], 12, fill=(30, 37, 48))
    d.rectangle([60, 120, 1220, 160], fill=(50, 58, 72))
    for i, m in enumerate(["Arquivo", "Editar", "Seleção", "Exibir"]):
        d.text((90 + i * 110, 128), m, font=FS(19), fill=(210, 220, 232))
    d.rounded_rectangle([84, 116, 168, 164], 6, fill=AMBER)
    d.text((90, 128), "Arquivo", font=FS(19), fill=NAVY)
    d.rounded_rectangle([96, 170, 320, 400], 8, fill=(40, 48, 62))
    for i, m in enumerate(["Abrir Pasta...", "Abrir Arquivo...", "Salvar", "Preferências"]):
        yy = 182 + i * 42
        if i == 0:
            d.rounded_rectangle([100, yy - 6, 316, yy + 32], 6, fill=(0, 120, 200))
            d.text((112, yy), m, font=FS(20), fill=WHITE)
        else:
            d.text((112, yy), m, font=FS(20), fill=(190, 200, 214))
    d.text((420, 250), "Boas-vindas!", font=FBL(44), fill=(230, 238, 246))
    d.text((420, 320), "Depois a gente abre a pasta da loja aqui.", font=FR(26), fill=(150, 165, 182))
    d.text((420, 360), "Por enquanto: qualquer pasta serve pra testar.", font=FR(26), fill=(150, 165, 182))
    s.save("s05.png")

def s06():
    s = S(); d = s.d
    s.header("PASSO 2", "Baixar o XAMPP (Apache + MySQL + PHP)", 6)
    y = s.win(60, 120, 1160, 440, "", url="https://www.apachefriends.org")
    d.text((110, y + 16), "XAMPP", font=FBL(64), fill=(251, 122, 82))
    d.text((110, y + 96), "Apache + MySQL + PHP + Perl — tudo numa instalação só, grátis.", font=FR(26), fill=MUT)
    btn(d, 110, y + 160, "Download (Windows)", (251, 122, 82))
    d.text((110, y + 224), "aviso de “programa desconhecido”? aceite e rode como administrador", font=FR(21), fill=MUT)
    s.box(60, 572, 570, "ONDE INSTALAR", "Sempre C:\\xampp — pasta com espaço ou acento no nome quebra o PHP.", "erro")
    s.box(650, 572, 570, "COMPONENTES", "Deixe todos marcados: Apache, MySQL e PHP são os três que a aula usa.", "ok")
    s.save("s06.png")

def xampp_panel(s, num, running):
    d = s.d
    s.header("PASSO 2" if not running else "PASSO 3", "Painel de Controle do XAMPP", num)
    y = s.win(140, 120, 1000, 460, "XAMPP Control Panel v3.3.0")
    yy = y + 14
    d.rectangle([170, yy, 1110, yy + 44], fill=NAVY)
    for t, xx in [("Módulo", 182), ("PID", 560), ("Porta", 680), ("Ações", 820)]:
        d.text((xx, yy + 10), t, font=FS(20), fill=WHITE)
    yy += 44
    for nome, pid, porta, on in [("Apache", "4812", "80, 443", running), ("MySQL", "5236", "3306", running),
                                 ("FileZilla", "", "", False), ("Mercury", "", "", False)]:
        d.rectangle([170, yy, 1110, yy + 52], fill=(250, 249, 246) if on else WHITE, outline=(220, 215, 205))
        d.text((182, yy + 12), nome, font=FS(22), fill=NAVY)
        d.text((560, yy + 14), pid, font=MONOR(18), fill=MUT)
        d.text((680, yy + 14), porta, font=MONOR(18), fill=MUT)
        if on:
            d.rounded_rectangle([820, yy + 8, 930, yy + 44], 6, fill=GREEN)
            d.text((838, yy + 14), "running", font=FS(18), fill=WHITE)
        else:
            b = btn(d, 820, yy + 6, "Start", (200, 196, 186), fg=NAVY, size=18, w=110)
        d.ellipse([1122, yy + 16, 1140, yy + 34], fill=GREEN if on else RED)
        yy += 52
    return yy

def s07():
    s = S()
    yy = xampp_panel(s, 7, False)
    s.box(140, 600, 1000, "POR ENQUANTO", "Apache e MySQL parados (bolinha vermelha). No próximo passo a gente liga os dois.", "tente")
    s.save("s07.png")

def s08():
    s = S()
    yy = xampp_panel(s, 8, True)
    s.box(140, 600, 1000, "CHECK", "Status verde = servidor no ar. Se o Apache não ligar: quase sempre é a porta 80 ocupada (Skype/outro servidor).", "ok")
    s.save("s08.png")

def s09():
    s = S(); d = s.d
    s.header("PASSO 3", "Teste: localhost no navegador", 9)
    y = s.win(60, 120, 1160, 460, "", url="http://localhost")
    d.rounded_rectangle([110, y + 16, 1170, y + 130], 12, fill=(251, 122, 82))
    d.text((140, y + 44), "Bem-vindo ao XAMPP!", font=FBL(44), fill=WHITE)
    d.text((140, y + 150), "Seu computador agora é um servidor web: tudo que morar em", font=FR(26), fill=NAVY)
    d.text((140, y + 186), "C:\\xampp\\htdocs vira site no endereço localhost.", font=MONOR(24), fill=NAVY)
    s.box(60, 600, 1160, "DICA DE OURO", "localhost = “aqui mesmo”. É o apelido do seu próprio computador na rede.", "ok")
    s.save("s09.png")

def s10():
    s = S(); d = s.d
    s.header("PASSO 3", "phpMyAdmin: o painel do banco", 10)
    y = s.win(60, 120, 1160, 460, "", url="http://localhost/phpmyadmin")
    d.rectangle([80, y + 8, 360, y + 340], fill=(240, 238, 232))
    d.text((96, y + 20), "Novo  (criar banco)", font=FS(20), fill=(0, 102, 180))
    for i, t in enumerate(["information_schema", "mysql", "performance_schema", "phpmyadmin"]):
        d.text((110, y + 62 + i * 34), t, font=MONOR(17), fill=MUT)
    d.text((400, y + 20), "phpMyAdmin — painel visual do MySQL", font=FB(28), fill=NAVY)
    d.text((400, y + 66), "tabelas, consultas e importação com botões —", font=FR(24), fill=MUT)
    d.text((400, y + 100), "sem decorar comando nenhum pra começar.", font=FR(24), fill=MUT)
    x = 400
    for t in ("Estrutura", "SQL", "Importar", "Exportar"):
        x = chip(d, x, y + 160, t, fill=(228, 224, 214), fg=NAVY, size=18)
    s.box(60, 592, 1160, "DEIXE ABERTO", "É nesta aba que a gente cria o banco da loja no próximo passo.", "tente")
    s.save("s10.png")

def s11():
    s = S(); d = s.d
    s.header("PASSO 3", "Criar o banco loja_turma", 11)
    y = s.win(60, 120, 1160, 440, "", url="http://localhost/phpmyadmin")
    d.text((110, y + 16), "Criar banco de dados", font=FB(28), fill=NAVY)
    d.rounded_rectangle([110, y + 66, 620, y + 112], 8, fill=WHITE, outline=NAVY, width=2)
    d.text((126, y + 76), "loja_turma", font=MONOR(24), fill=NAVY)
    btn(d, 640, y + 66, "Criar", (0, 120, 200))
    d.text((110, y + 136), "minúsculo, sem acento, separando com sublinhado", font=FR(21), fill=MUT)
    d.rectangle([110, y + 190, 1170, y + 192], fill=(220, 215, 205))
    d.text((110, y + 210), "Banco de dados = armário organizado:", font=FB(26), fill=NAVY)
    s.bullets(110, y + 250, [("→", "cada gaveta é uma TABELA;"), ("→", "cada pasta na gaveta é uma LINHA;"), ("→", "as etiquetas das pastas são as COLUNAS.")], size=24)
    s.save("s11.png")

def s12():
    s = S(); d = s.d
    s.header("PASSO 3", "Importar o loja_turma.sql (a receita)", 12)
    y = s.win(60, 120, 1160, 420, "", url="http://localhost/phpmyadmin — banco: loja_turma")
    x = 110
    for t, on in [("Estrutura", False), ("SQL", False), ("Importar", True), ("Exportar", False)]:
        if on:
            d.rounded_rectangle([x, y + 10, x + 130, y + 48], 8, fill=NAVY)
            d.text((x + 20, y + 17), t, font=FS(19), fill=WHITE)
        else:
            d.text((x + 20, y + 17), t, font=FS(19), fill=MUT)
        x += 150
    d.rounded_rectangle([110, y + 70, 760, y + 122], 10, fill=(240, 238, 232))
    d.text((130, y + 82), "banco / loja_turma.sql", font=MONOR(22), fill=NAVY)
    d.text((790, y + 84), "← arquivo da pasta banco do ZIP", font=FR(20), fill=MUT)
    btn(d, 110, y + 150, "Executar", (0, 120, 200))
    d.text((110, y + 214), "em segundos: tabelas criadas + produtos de exemplo dentro", font=FR(22), fill=GREEN)
    s.box(60, 560, 570, "A RECEITA", "O .sql cria as tabelas e já coloca teclado, mouse, headset e webcam no estoque.", "ok")
    s.box(650, 560, 570, "PREFERE DIGITAR?", "A aba SQL aceita os mesmos comandos colados e executados.", "tente")
    s.save("s12.png")

def s13():
    s = S(); d = s.d
    s.header("PASSO 3", "Tabela produtos: o estoque inicial", 13)
    y = s.win(60, 120, 1160, 460, "", url="http://localhost/phpmyadmin — loja_turma › produtos › Visualizar")
    s.table(110, y + 16, ["id", "nome", "preco", "estoque"],
            [["1", "Headset sem fio", "199.90", "10"],
             ["2", "Mouse gamer", "89.90", "15"],
             ["3", "Teclado mecânico", "249.00", "8"],
             ["4", "Webcam Full HD", "179.50", "12"]],
            [80, 420, 200, 160])
    d.text((110, y + 250), "4 tabelas no banco: produtos · clientes · pedidos · itens_pedido", font=FS(24), fill=NAVY)
    s.box(60, 600, 1160, "CHECK", "Armário organizado, gavetas etiquetadas, pastas no lugar: banco pronto.", "ok")
    s.save("s13.png")

def s14():
    s = S(); d = s.d
    s.header("PASSO 4", "Copiar o site pra casa do XAMPP (htdocs)", 14)
    y = s.win(60, 120, 560, 420, "Explorador de Arquivos")
    d.text((100, y + 20), "Projeto_Loja_Tech_da_Turma.zip", font=MONOR(19), fill=MUT)
    d.text((100, y + 56), "↳ site\\   banco\\   vb6\\", font=MONOR(21), fill=NAVY)
    d.rounded_rectangle([92, y + 46, 190, y + 82], 6, outline=AMBER, width=4)
    d.text((100, y + 110), "botão direito › Extrair Tudo", font=FR(20), fill=MUT)
    d.text((100, y + 150), "banco = já usamos · vb6 = gerencial (LP2)", font=FR(20), fill=MUT)
    d.line([640, 300, 700, 300], fill=AMBER, width=6)
    d.polygon([(700, 288), (724, 300), (700, 312)], fill=AMBER)
    y2 = s.win(700, 120, 520, 420, "C:\\xampp\\htdocs")
    d.text((740, y2 + 16), "loja\\", font=MONOR(24), fill=NAVY)
    d.text((770, y2 + 54), "index.php", font=MONOR(19), fill=MUT)
    d.text((770, y2 + 84), "produtos.php · produto.php", font=MONOR(19), fill=MUT)
    d.text((770, y2 + 114), "pagamentos.php · cadastro.php", font=MONOR(19), fill=MUT)
    d.text((770, y2 + 144), "contato.php · processar_pedido.php", font=MONOR(19), fill=MUT)
    d.text((770, y2 + 174), "includes\\  css\\  imagens\\", font=MONOR(19), fill=MUT)
    s.box(60, 560, 1160, "REGRA DA CASA", "PHP só roda dentro da htdocs: C:\\xampp\\htdocs\\loja — arquivo .html NÃO executa PHP.", "erro")
    s.save("s14.png")

def s15():
    s = S(dark=True); d = s.d
    d.rectangle([0, 0, W, H], fill=(13, 27, 42))
    s.header("PASSO 4", "Abrir com o Code: o mapa do projeto", 15)
    d.rounded_rectangle([60, 120, 1220, 660], 12, fill=(30, 37, 48))
    d.rectangle([60, 120, 430, 660], fill=(37, 45, 58))
    d.text((84, 140), "LOJA", font=FB(22), fill=(220, 228, 238))
    tree = [("includes/", 0, 1), ("cabecalho.php", 1, 0), ("conexao.php", 1, 0), ("rodape.php", 1, 0),
            ("css/", 0, 0), ("imagens/", 0, 0), ("index.php", 0, 0), ("produtos.php", 0, 0),
            ("produto.php", 0, 0), ("pagamentos.php", 0, 0), ("processar_pedido.php", 0, 0),
            ("cadastro.php", 0, 0), ("contato.php", 0, 0)]
    yy = 180
    for nome, lvl, open_ in tree:
        col = AMBER if nome.endswith("/") else (200, 210, 222)
        d.text((92 + lvl * 26, yy), nome, font=MONOR(18), fill=col)
        yy += 32
    d.text((470, 180), "7 páginas PHP + 3 pastas", font=FBL(40), fill=(230, 238, 246))
    s.bullets(470, 260, [
        ("includes/", " cabeçalho, rodapé e conexão — o que se repete,"),
        ("", "escrito uma vez só;"),
        ("css/", " o estilo (cores, fontes, cartões);"),
        ("imagens/", " logo, banner, fotos dos produtos e mapa;"),
        ("index.php", " a vitrine: pergunta ao banco e desenha.")], size=24, color=(200, 210, 222))
    s.save("s15.png")

def produto_card(d, x, y, nome, preco):
    d.rounded_rectangle([x, y, x + 260, y + 210], 12, fill=WHITE, outline=(220, 215, 205), width=2)
    d.rounded_rectangle([x + 16, y + 16, x + 244, y + 108], 8, fill=(238, 236, 230))
    d.text((x + 96, y + 44), "[foto]", font=MONOR(20), fill=MUT)
    d.text((x + 16, y + 122), nome, font=FS(20), fill=NAVY)
    d.text((x + 16, y + 150), preco, font=FB(22), fill=(0, 120, 200))
    d.rounded_rectangle([x + 16, y + 178, x + 130, y + 200], 6, fill=AMBER)
    d.text((x + 34, y + 180), "Comprar", font=FS(15), fill=NAVY)

def s16():
    s = S(); d = s.d
    s.header("PASSO 4", "localhost/loja — a vitrine", 16)
    y = s.win(60, 120, 1160, 470, "", url="http://localhost/loja")
    d.rounded_rectangle([90, y + 8, 1190, y + 84], 10, fill=NAVY)
    d.text((120, y + 26), "Loja Tech da Turma", font=FBL(36), fill=AMBER)
    d.text((700, y + 36), "início · produtos · cadastro · contato", font=FS(20), fill=(210, 220, 232))
    produto_card(d, 90, y + 104, "Headset sem fio", "R$ 199,90")
    produto_card(d, 370, y + 104, "Mouse gamer", "R$ 89,90")
    produto_card(d, 650, y + 104, "Teclado mecânico", "R$ 249,00")
    produto_card(d, 930, y + 104, "Webcam Full HD", "R$ 179,50")
    s.box(60, 600, 1160, "REPARA", "Nenhum produto escrito à mão na página: a index.php pergunta ao banco e desenha.", "ok")
    s.save("s16.png")

def s17():
    s = S(); d = s.d
    s.header("PASSO 4", "produto.php?id=1 — uma página, qualquer produto", 17)
    y = s.win(60, 120, 1160, 460, "", url="http://localhost/loja/produto.php?id=1")
    d.rounded_rectangle([820, y + 4, 900, y + 34], 6, outline=RED, width=4)
    d.rounded_rectangle([100, y + 20, 460, y + 260], 12, fill=(238, 236, 230))
    d.text((220, y + 120), "[foto]", font=MONOR(28), fill=MUT)
    d.text((500, y + 30), "Headset sem fio", font=FBL(40), fill=NAVY)
    d.text((500, y + 90), "R$ 199,90 · estoque: 10", font=FB(28), fill=(0, 120, 200))
    d.text((500, y + 140), "Som limpo, bateria de 30 h, Bluetooth 5.3.", font=FR(24), fill=MUT)
    btn(d, 500, y + 196, "Comprar", AMBER, fg=NAVY)
    s.box(60, 600, 1160, "O SEGREDO DO ?id=", "O número no endereço diz QUAL produto mostrar: 1 página serve todos os produtos.", "ok")
    s.save("s17.png")

def s18():
    s = S(); d = s.d
    s.header("PASSO 4", "pagamentos.php — Pix, cartão ou boleto", 18)
    y = s.win(60, 120, 1160, 440, "", url="http://localhost/loja/pagamentos.php?id=1")
    x = 110
    for t in ("Pix", "Cartão", "Boleto"):
        d.rounded_rectangle([x, y + 16, x + 180, y + 76], 10, fill=WHITE, outline=(0, 120, 200) if t == "Pix" else (220, 215, 205), width=3 if t == "Pix" else 2)
        d.text((x + 56, y + 32), t, font=FS(24), fill=NAVY)
        x += 210
    d.text((110, y + 110), "(pagamento simulado: o que grava é o pedido, não o dinheiro)", font=FR(21), fill=MUT)
    d.rounded_rectangle([110, y + 160, 900, y + 230], 12, fill=(232, 244, 234), outline=GREEN, width=3)
    d.text((140, y + 178), "Pedido registrado com sucesso!", font=FB(30), fill=GREEN)
    s.box(60, 580, 1160, "NOS BASTIDORES", "processar_pedido.php grava em pedidos + itens_pedido e baixa 1 do estoque.", "ok")
    s.save("s18.png")

def s19():
    s = S(); d = s.d
    s.header("PASSO 4", "Prova real: o estoque baixou", 19)
    y = s.win(60, 120, 560, 380, "phpMyAdmin › produtos (antes)")
    s.table(100, y + 12, ["nome", "estoque"], [["Headset sem fio", "10"]], [300, 160])
    y2 = s.win(660, 120, 560, 380, "phpMyAdmin › produtos (depois)")
    s.table(700, y2 + 12, ["nome", "estoque"], [["Headset sem fio", "9"]], [300, 160], hl=0)
    d.line([620, 300, 650, 300], fill=AMBER, width=6)
    d.polygon([(650, 288), (674, 300), (650, 312)], fill=AMBER)
    s.box(60, 540, 570, "VENDA DE VERDADE", "Vendeu 1 headset → o banco mostra 9. Estoque que baixa é banco conversando com o site.", "ok")
    s.box(650, 540, 570, "EXPLORA", "Catálogo, cadastro de cliente e contato: tudo funciona sem internet.", "tente")
    s.save("s19.png")

def s20():
    s = S(); d = s.d
    s.header("PASSO 5", "includes/conexao.php — a ponte com o banco", 20)
    y = s.code(60, 120, 760, [
        "<?php",
        "// a ponte entre o site e o banco de dados",
        "$con = new mysqli(",
        "    'localhost',   // servidor",
        "    'root',          // usuário padrão do XAMPP",
        "    '',               // senha: vazia no XAMPP",
        "    'loja_turma'      // nosso banco",
        ");",
        "if ($con->connect_error) {",
        "    error_log('banco: ' . $con->connect_error);",
        "    exit('Estamos ajustando as prateleiras :(');",
        "}",
    ], title="includes/conexao.php")
    s.box(850, 130, 370, "REGRA DE PROFISSIONAL", "Erro de banco vira mensagem amigável + anotação no diário do servidor (error_log). Senha NUNCA aparece na tela.", "ok")
    s.box(850, 330, 370, "POR QUE VAZIA?", "No XAMPP local o root vem sem senha. Em servidor de verdade, senha sempre existe — e fica escondida.", "tente")
    s.save("s20.png")

def s21():
    s = S(); d = s.d
    s.header("PASSO 5", "index.php — SELECT, foreach e o sanduíche", 21)
    y = s.code(60, 120, 800, [
        "<?php include 'includes/cabecalho.php'; ?>",
        "",
        "<?php",
        "$r = $con->query(",
        "   'SELECT * FROM produtos ORDER BY nome');",
        "foreach ($r as $p):  // “para cada produto…”",
        "?>",
        "  <div class=\"card\">",
        "    foto · nome · preço · botão",
        "  </div>",
        "<?php endforeach; include 'includes/rodape.php'; ?>",
    ], title="index.php (resumo didático)")
    s.box(890, 130, 330, "TRADUZINDO O SQL", "SELECT * FROM produtos ORDER BY nome = “me traga todos os produtos, em ordem de nome”.", "ok")
    s.box(890, 320, 330, "SANDUÍCHE", "Cabeçalho (pão) + conteúdo (recheio) + rodapé (pão): menu escrito 1 vez, usado em 7 páginas.", "tente")
    s.box(890, 510, 330, "SITE DINÂMICO", "Mudou o banco, mudou a vitrine sozinho — sem mexer no HTML.", "ok")
    s.save("s21.png")

def s22():
    s = S(); d = s.d
    s.header("PASSO 5", "Quem conversa com quem", 22)
    def caixa(x, y, w, h, t1, t2, fill):
        d.rounded_rectangle([x, y, x + w, y + h], 14, fill=fill)
        d.text((x + 24, y + 24), t1, font=FBL(30), fill=WHITE)
        d.text((x + 24, y + 68), t2, font=FR(20), fill=(230, 238, 246))
    caixa(80, 260, 300, 130, "Navegador", "Chrome/Edge — pede a página", (0, 102, 180))
    caixa(490, 260, 300, 130, "Apache + PHP", "executa o código .php", (251, 122, 82))
    caixa(900, 260, 300, 130, "MySQL", "banco loja_turma", (30, 123, 52))
    d.line([380, 300, 480, 300], fill=NAVY, width=5); d.polygon([(480, 290), (498, 300), (480, 310)], fill=NAVY)
    d.text((386, 232), "requisição", font=FS(19), fill=NAVY)
    d.line([480, 350, 398, 350], fill=NAVY, width=5); d.polygon([(398, 340), (380, 350), (398, 360)], fill=NAVY)
    d.text((386, 396), "resposta (HTML)", font=FS(19), fill=NAVY)
    d.line([790, 300, 890, 300], fill=NAVY, width=5); d.polygon([(890, 290), (908, 300), (890, 310)], fill=NAVY)
    d.text((782, 232), "SELECT/INSERT", font=FS(19), fill=NAVY)
    d.line([890, 350, 808, 350], fill=NAVY, width=5); d.polygon([(808, 340), (790, 350), (808, 360)], fill=NAVY)
    d.text((782, 396), "linhas da tabela", font=FS(19), fill=NAVY)
    s.box(80, 470, 1120, "EM UMA FRASE", "O navegador pede; o PHP trabalha; o MySQL guarda; o PHP devolve a página pronta.", "ok")
    s.save("s22.png")

def s23():
    s = S(); d = s.d
    s.header("PASSO 5", "processar_pedido.php — pedido com cinto de segurança", 23)
    y = s.code(60, 120, 780, [
        "$con->begin_transaction();          // BEGIN",
        "$st = $con->prepare(",
        "  'SELECT estoque FROM produtos",
        "    WHERE id = ? FOR UPDATE');     // segura a poltrona",
        "// confere estoque, grava pedido e itens…",
        "$con->commit();                    // confirmou!",
        "// se algo falhar no meio:",
        "//   $con->rollback();              // desfaz tudo",
    ], title="processar_pedido.php (trecho)")
    s.box(870, 130, 350, "INGRESSO DE CINEMA", "BEGIN = segure a sessão; FOR UPDATE = segure a poltrona enquanto confere o dinheiro; COMMIT = confirmou, solte.", "tente")
    s.box(870, 360, 350, "TRANSAÇÃO", "Ou acontece TUDO, ou não acontece NADA: o estoque nunca some pela metade.", "ok")
    s.save("s23.png")

def s24():
    s = S(); d = s.d
    s.header("PASSO 5", "Limpeza: htmlspecialchars + prepare(?)", 24)
    s.code(60, 120, 700, [
        "echo htmlspecialchars($nome);  // desarma texto",
        "$st = $con->prepare(",
        "  'INSERT INTO clientes (nome) VALUES (?)');",
        "// dado entra como DADO, nunca como comando",
    ], title="regras de limpeza")
    s.box(800, 120, 420, "BRINCADEIRINHA DESARMADA", "Código disfarçado de texto vira texto inofensivo na tela — ninguém apaga nada da loja.", "ok")
    y = s.box(60, 360, 1160, "TENTE VOCÊ", "Cadastre um cliente com nome vazio: o site mostra o erro amigável. Tente comprar além do estoque: o site avisa que acabou.", "tente")
    s.box(60, y + 20, 1160, "CONFIANÇA", "Loja que avisa erro é loja que dá confiança — errar bonito também é funcionalidade.", "ok")
    s.save("s24.png")

def s25():
    s = S(); d = s.d
    s.header("RECAP", "As 5 fotos da caminhada", 25)
    y = 140
    for i, t in enumerate(["VS Code instalado — o caderno com superpoderes",
                           "XAMPP no ar — Apache e MySQL verdinhos",
                           "Banco loja_turma — tabelas e estoque importados",
                           "Loja na htdocs — compra feita, estoque baixou",
                           "Código por dentro — conexão, SELECT, foreach, transação"]):
        d.rounded_rectangle([80, y, 1200, y + 78], 12, fill=WHITE, outline=(220, 215, 205), width=2)
        d.ellipse([104, y + 14, 104 + 50, y + 64], fill=AMBER)
        d.text((120, y + 22), str(i + 1), font=FBL(28), fill=NAVY)
        d.text((180, y + 24), t, font=FS(26), fill=NAVY)
        y += 96
    s.save("s25.png")

def s26():
    s = S(); d = s.d
    s.header("MISSÃO", "A SUA loja, com o mesmo esqueleto", 26)
    s.bullets(70, 130, [
        ("✔", "Em duplas: pet shop, lanchonete, boutique, oficina — vocês escolhem;"),
        ("✔", "mínimo 4 páginas (vitrine, detalhe, pagamento, contato/cadastro);"),
        ("✔", "1 tabela nova com dados de vocês (importada ou digitada);"),
        ("✔", "formulário com validação e mensagens amigáveis;"),
        ("✔", "pedido que baixa estoque (transação de mãos dadas).")], size=25)
    s.table(70, 400, ["critério", "pts"], [
        ["site sem erros", "2,0"], ["formulários validados", "2,0"], ["consulta SQL mostrando dados", "2,0"],
        ["tabela própria com dados", "1,5"], ["pedido baixando estoque", "1,5"], ["backup comprovado", "1,0"]],
        [560, 120])
    d.text((760, 420), "rubrica completa no", font=FR(22), fill=MUT)
    d.text((760, 450), "Tutorial_Loja_Guia.html", font=MONOR(22), fill=NAVY)
    d.text((760, 490), "(tutorial ilustrado, offline)", font=FR(20), fill=MUT)
    s.save("s26.png")

def s27():
    s = S(dark=True); d = s.d
    d.rectangle([0, 0, W, H], fill=(13, 27, 42))
    d.text((90, 160), "Boa aula, turma!", font=FBL(84), fill=AMBER)
    d.text((94, 300), "Pause o vídeo · repita sem olhar · remonte a sua loja.", font=FR(32), fill=(210, 220, 232))
    d.text((94, 350), "Porque quem não consegue remontar ainda não aprendeu —", font=FR(26), fill=(150, 168, 186))
    d.text((94, 388), "e vocês já conseguem.", font=FR(26), fill=(150, 168, 186))
    x = 94
    for t in ("VS Code", "XAMPP", "loja_turma", "htdocs", "transação"):
        x = chip(d, x, 470, t, fill=(30, 48, 68), fg=(220, 230, 240))
    d.text((94, 560), "Nos vemos no próximo vídeo! · Prof.ª Raquel · Turma 2/2026", font=FS(26), fill=(200, 212, 224))
    s.save("s27.png")

for fn in [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15,
           s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27]:
    fn()
print("slides:", len(os.listdir(OUT)))
