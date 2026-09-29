#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere se as partes, somadas, reproduzem o zip mestre byte a byte.
Uso: python3 video_tools/verifica_partes.py <mestre.zip> <pasta_das_partes>"""
import zipfile, glob, hashlib, os, sys

mestre = sys.argv[1] if len(sys.argv) > 1 else "Kit_Sala_de_Aula_TUDO_v1.zip"
pasta = sys.argv[2] if len(sys.argv) > 2 else os.path.join("output", "partes")

tot, dup = {}, []
for p in sorted(glob.glob(os.path.join(pasta, "Kit_TUDO_v1_parte*.zip"))):
    z = zipfile.ZipFile(p)
    for i in z.infolist():
        if i.filename.endswith("LEIA-ME_PARTES.md"):
            continue
        if i.filename in tot:
            dup.append(i.filename)
        tot[i.filename] = hashlib.md5(z.read(i.filename)).hexdigest()

m = zipfile.ZipFile(mestre)
mes = {i.filename: hashlib.md5(m.read(i.filename)).hexdigest() for i in m.infolist()}

faltando = sorted(set(mes) - set(tot))
extra = sorted(set(tot) - set(mes))
diferentes = sorted(k for k in set(mes) & set(tot) if mes[k] != tot[k])

print(f"partes somadas : {len(tot)} arquivos")
print(f"zip mestre     : {len(mes)} arquivos")
print(f"duplicados entre partes : {len(dup)}")
print(f"faltando : {len(faltando)} {faltando[:5]}")
print(f"sobrando : {len(extra)} {extra[:5]}")
print(f"md5 diferente : {len(diferentes)} {diferentes[:5]}")
ok = not (dup or faltando or extra or diferentes)
print("VEREDITO:", "IDENTICO ✔  (as partes reconstroem o mestre)" if ok else "DIVERGENTE ✘")
sys.exit(0 if ok else 1)
