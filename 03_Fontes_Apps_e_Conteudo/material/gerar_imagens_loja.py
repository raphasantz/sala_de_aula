# -*- coding: utf-8 -*-
"""Desenha as imagens do projeto-loja em estilo flat (PIL)."""
import os
from PIL import Image, ImageDraw, ImageFont

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projeto-loja", "site", "imagens")
os.makedirs(D, exist_ok=True)
F = "/home/user/fonts/"
ALT = "/opt/arena-python/lib/python3.11/site-packages/reportlab/fonts/"
import io as _io, time as _time
def font(sz, bold=False):
    candidatos = [F + ("Inter-Bold.ttf" if bold else "Inter-Regular.ttf"),
                  ALT + ("VeraBd.ttf" if bold else "Vera.ttf")]
    ultimo = None
    for c in candidatos:
        for tentativa in range(4):          # sandbox às vezes pisca no acesso a arquivos
            try:
                return ImageFont.truetype(c, sz)
            except Exception as e:
                ultimo = e
                try:
                    with open(c, "rb") as fh:
                        return ImageFont.truetype(_io.BytesIO(fh.read()), sz)
                except Exception as e2:
                    ultimo = e2
                    _time.sleep(0.4)
    raise ultimo

AZUL, AZULE, AMB, NAVY, BRANCO = (27,95,170), (233,241,250), (245,158,11), (13,43,78), (255,255,255)
CINZA, PRETO = (229,231,235), (34,34,34)

def rr(d, box, r, fill=None, outline=None, w=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=w)

# ---------------- LOGO 512 ----------------
im = Image.new("RGB", (512, 512), BRANCO); d = ImageDraw.Draw(im)
rr(d, (150, 190, 362, 430), 46, fill=AZUL)                      # sacola
d.rounded_rectangle((206, 128, 306, 210), radius=40, outline=AZUL, width=22)  # alça
rr(d, (196, 246, 316, 336), 12, fill=BRANCO)                    # monitor
rr(d, (206, 256, 306, 316), 8, fill=NAVY)                      # tela
for i, c in enumerate([AMB, (110,182,255), AMB]):               # linhas de código
    d.rectangle((216, 266 + i*16, 216 + [60, 44, 70][i], 274 + i*16), fill=c)
d.polygon([(256, 214), (322, 240), (256, 266), (190, 240)], fill=AMB)  # capelo
d.rectangle((252, 262, 260, 292), fill=AMB)
d.ellipse((250, 288, 262, 300), fill=AMB)
im.save(os.path.join(D, "logo.png"))

# ---------------- BANNER 1200x400 ----------------
im = Image.new("RGB", (1200, 400), NAVY); d = ImageDraw.Draw(im)
for x in range(0, 1200, 60):                                    # pontinhos
    for y in range(0, 400, 60):
        d.ellipse((x, y, x+4, y+4), fill=(20, 58, 102))
d.ellipse((980, -120, 1320, 220), fill=(20, 58, 102))
rr(d, (640, 60, 1020, 280), 16, fill=BRANCO)                   # monitor
rr(d, (656, 76, 1004, 250), 10, fill=(20, 58, 102))
for i, c in enumerate([(158, 206, 106), AMB, (108, 182, 255), (158, 206, 106)]):
    d.rectangle((676, 96 + i*34, 676 + [180, 120, 220, 150][i], 112 + i*34), fill=c)
d.rectangle((800, 280, 860, 316), fill=(200, 210, 222))        # pé
rr(d, (740, 316, 920, 332), 8, fill=(200, 210, 222))
rr(d, (620, 344, 1040, 384), 12, fill=AZUL)                   # teclado
for k in range(12):
    rr(d, (636 + k*34, 352, 660 + k*34, 376), 5, fill=(233, 241, 250))
d.ellipse((1080, 330, 1140, 392), fill=PRETO)                  # mouse
d.rectangle((1106, 340, 1114, 358), fill=AMB)
d.arc((560, 90, 660, 190), 90, 270, fill=AMB, width=14)       # headset
rr(d, (548, 150, 584, 210), 12, fill=AZUL)
rr(d, (120, 250, 200, 330), 18, fill=(20, 58, 102))          # caixa decorativa
rr(d, (240, 290, 300, 340), 14, fill=(20, 58, 102))
d.ellipse((360, 120, 420, 180), outline=AMB, width=8)
im.save(os.path.join(D, "banner.png"))

# ---------------- PRODUTOS 600x450 ----------------
def base():
    im = Image.new("RGB", (600, 450), BRANCO); return im, ImageDraw.Draw(im)

im, d = base()                                                  # MOUSE
d.ellipse((210, 90, 390, 380), fill=PRETO)
d.rectangle((296, 110, 304, 200), fill=(60, 60, 60))
rr(d, (292, 150, 308, 190), 8, fill=AMB)
d.arc((230, 300, 370, 380), 20, 160, fill=(108, 182, 255), width=10)
d.ellipse((240, 380, 360, 400), fill=(243, 244, 246))
im.save(os.path.join(D, "prod-mouse.png"))

im, d = base()                                                  # TECLADO
rr(d, (60, 130, 540, 330), 22, fill=CINZA)
for r in range(4):
    for c in range(11):
        fill = AMB if (r == 1 and c == 10) else (249, 250, 251)
        rr(d, (78 + c*42, 148 + r*42, 112 + c*42, 182 + r*42), 7, fill=fill)
rr(d, (200, 316, 400, 344), 8, fill=(249, 250, 251))
im.save(os.path.join(D, "prod-teclado.png"))

im, d = base()                                                  # HEADSET
d.arc((180, 60, 420, 300), 180, 360, fill=AZUL, width=26)
rr(d, (160, 180, 220, 290), 24, fill=NAVY)
rr(d, (380, 180, 440, 290), 24, fill=NAVY)
d.line((190, 285, 250, 340), fill=NAVY, width=10)               # microfone
d.ellipse((244, 332, 268, 356), fill=AMB)
im.save(os.path.join(D, "prod-headset.png"))

im, d = base()                                                  # WEBCAM
d.ellipse((210, 80, 390, 260), fill=PRETO)
d.ellipse((238, 108, 362, 232), outline=(108, 182, 255), width=10)
d.ellipse((268, 138, 332, 202), fill=(20, 58, 102))
d.ellipse((286, 156, 314, 184), fill=(108, 182, 255))
rr(d, (280, 258, 320, 300), 8, fill=(60, 60, 60))             # clipe
rr(d, (240, 296, 360, 320), 10, fill=(60, 60, 60))
d.ellipse((240, 380, 360, 400), fill=(243, 244, 246))
im.save(os.path.join(D, "prod-webcam.png"))

im, d = base()                                                  # SEM FOTO
im = Image.new("RGB", (600, 450), (241, 245, 249)); d = ImageDraw.Draw(im)
rr(d, (220, 140, 380, 250), 18, outline=(148, 163, 184), w=8)
d.ellipse((272, 172, 328, 228), outline=(148, 163, 184), width=8)
d.rectangle((250, 152, 286, 176), fill=(148, 163, 184))
t = font(30, True); d.text((300, 300), "sem foto ainda", font=t, fill=(148, 163, 184), anchor="mm")
im.save(os.path.join(D, "sem-foto.png"))

print("imagens desenhadas:", sorted(os.listdir(D)))
