# -*- coding: utf-8 -*-
"""Conferência de glifos: quais símbolos as fontes do kit suportam."""
from PIL import ImageFont

CHARS = "→←↑↓✓✔⚠●◯■□─└├▶►•·—…×÷1234abcd"
NOTDEF = chr(0xFFFF)

for fn in ("Inter-Regular.ttf", "Inter-Bold.ttf", "JetBrainsMono-Regular.ttf"):
    f = ImageFont.truetype("fonts/" + fn, 30)
    ref = f.getmask(NOTDEF)
    ref_bb = ref.getbbox()
    miss = []
    for ch in CHARS:
        m = f.getmask(ch)
        bb = m.getbbox()
        if bb == ref_bb:
            miss.append(ch)
    print(fn, "FALTANDO:", "".join(miss) if miss else "(nenhum)")
