#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atualiza o LEIA-ME_GERAL.md dentro do zip mestre (sem tocar no resto).
Uso: python3 video_tools/atualiza_leiame_mestre.py [mestre.zip] [leiame.md]"""
import zipfile, os, sys, shutil, hashlib, time

mestre = sys.argv[1] if len(sys.argv) > 1 else "Kit_Sala_de_Aula_TUDO_v1.zip"
leiame = sys.argv[2] if len(sys.argv) > 2 else "LEIA-ME_GERAL.md"
ALVO = "LEIA-ME_GERAL.md"

novo = open(leiame, "rb").read()
tmp = mestre + ".tmp"
t0 = time.time()
zin = zipfile.ZipFile(mestre)
trocou = False
with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
    for i in zin.infolist():
        if i.filename == ALVO:
            zout.writestr(i, novo); trocou = True
        else:
            zout.writestr(i, zin.read(i.filename))
zin.close()
assert trocou, ALVO + " nao existe no mestre"
os.replace(tmp, mestre)
h = hashlib.md5(open(mestre, 'rb').read()).hexdigest()
print(f"{ALVO} atualizado dentro de {mestre} em {time.time()-t0:.1f}s")
print("novo MD5 do mestre:", h, "|", round(os.path.getsize(mestre)/1024/1024, 2), "MB")
