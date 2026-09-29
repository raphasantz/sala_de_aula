# -*- coding: utf-8 -*-
"""Imagens extras da loja: mapa de localização + ícones de pagamento."""
import os, io as _io, time as _time
from PIL import Image, ImageDraw, ImageFont

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projeto-loja", "site", "imagens")
F = "/home/user/fonts/"
ALT = "/opt/arena-python/lib/python3.11/site-packages/reportlab/fonts/"
def font(sz, bold=False):
    cands = [F + ("Inter-Bold.ttf" if bold else "Inter-Regular.ttf"),
             ALT + ("VeraBd.ttf" if bold else "Vera.ttf")]
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

AZUL, AMB, NAVY = (27,95,170), (245,158,11), (13,43,78)

# ---------------- MAPA 900x520 ----------------
im = Image.new("RGB", (900, 520), (238, 243, 240)); d = ImageDraw.Draw(im)
d.rectangle((0, 0, 900, 90), fill=(214, 232, 245))            # rio/no topo
d.text((20, 30), "Rio Muriaé", font=font(20, True), fill=(120, 160, 190))
for x in (140, 420, 700):                                     # avenidas verticais
    d.rectangle((x, 90, x+56, 520), fill=(255, 255, 255))
    d.line((x+28, 90, x+28, 520), fill=(200, 205, 210), width=3)
for y in (180, 330, 450):                                   # ruas horizontais
    d.rectangle((0, y, 900, y+44), fill=(255, 255, 255))
    d.line((0, y+22, 900, y+22), fill=(200, 205, 210), width=3)
# quarteirões com prédios
for bx in (20, 220, 500, 780):
    for by in (100, 240, 390):
        rr(d, (bx, by, bx+100, by+64), 8, fill=(222, 228, 224))
# praça
d.ellipse((520, 350, 680, 440), fill=(198, 226, 200))
d.text((600, 395), "Praça", font=font(18, True), fill=(110, 150, 115), anchor="mm")
# PIN da loja
px, py = 448, 250
d.polygon([(px, py+58), (px-26, py+10), (px+26, py+10)], fill=(200, 40, 40))
d.ellipse((px-30, py-44, px+30, py+16), fill=(220, 50, 50))
d.ellipse((px-12, py-26, px+12, py-2), fill=(255, 255, 255))
rr(d, (px+40, py-70, px+330, py-14), 12, fill=NAVY)
d.text((px+56, py-42), "Loja Tech da Turma", font=font(22, True), fill=(255, 255, 255), anchor="lm")
d.text((40, 480), "Av. das Turmas, 42 — Centro (esquina com a Rua dos Bits)",
       font=font(20, True), fill=(70, 80, 95))
im.save(os.path.join(D, "mapa.png"))

# ---------------- ÍCONES DE PAGAMENTO 220x140 ----------------
im = Image.new("RGB", (220, 140), (255, 255, 255)); d = ImageDraw.Draw(im)
d.polygon([(110, 18), (178, 70), (110, 122), (42, 70)], fill=(50, 177, 166))   # pix
d.polygon([(110, 40), (150, 70), (110, 100), (70, 70)], fill=(255, 255, 255))
d.text((110, 70), "PIX", font=font(20, True), fill=(50, 177, 166), anchor="mm")
im.save(os.path.join(D, "icon-pix.png"))

im = Image.new("RGB", (220, 140), (255, 255, 255)); d = ImageDraw.Draw(im)
rr(d, (30, 30, 190, 116), 12, fill=AZUL)                                    # cartão
d.rectangle((30, 48, 190, 66), fill=(13, 43, 78))
rr(d, (46, 82, 78, 100), 4, fill=(245, 198, 66))
d.text((92, 92), "•••• 4242", font=font(16, True), fill=(255, 255, 255), anchor="lm")
im.save(os.path.join(D, "icon-cartao.png"))

im = Image.new("RGB", (220, 140), (255, 255, 255)); d = ImageDraw.Draw(im)
rr(d, (40, 18, 180, 122), 8, fill=(250, 250, 250), outline=(190, 195, 200), w=3)  # boleto
for i, x in enumerate(range(56, 168, 8)):
    d.rectangle((x, 34, x+ (4 if i % 2 else 2), 86), fill=(30, 30, 30))
d.text((110, 106), "BOLETO", font=font(16, True), fill=(90, 95, 100), anchor="mm")
im.save(os.path.join(D, "icon-boleto.png"))

print("extras ok:", [a for a in sorted(os.listdir(D)) if a.startswith(("mapa", "icon"))])
