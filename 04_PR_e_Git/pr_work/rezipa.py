# -*- coding: utf-8 -*-
"""Rezipa PR_AulaViva_v2.zip e atualiza os zips de kits com os apps novos (paginador)."""
import os, zipfile, hashlib, shutil

# caminhos derivados do próprio arquivo (o sandbox reescreve literais "/home/user"
# em arquivos .py e nem sempre expande de volta — assim evita o problema)
HERE = os.path.dirname(os.path.abspath(__file__))          # .../pr_work
ROOT = os.path.dirname(HERE)                                # workspace
PR = os.path.join(HERE, "PR")
OUT = os.path.join(ROOT, "output")

def md5(b): return hashlib.md5(b).hexdigest()

# ---------- 1) PR_AulaViva_v2.zip (raiz PR_AulaViva_v2/) ----------
zp = os.path.join(OUT, "PR_AulaViva_v2.zip")
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for raiz, _, arqs in os.walk(PR):
        for a in sorted(arqs):
            fp = os.path.join(raiz, a)
            z.write(fp, os.path.join("PR_AulaViva_v2", os.path.relpath(fp, PR)))
print("PR_AulaViva_v2.zip:", len(zipfile.ZipFile(zp).namelist()), "entradas,",
      os.path.getsize(zp) // 1024, "KB")

# ---------- 2) Kit_Sala_de_Aula.zip: apps-offline/AulaViva_*_offline.html ----------
novos = {
    "apps-offline/AulaViva_PI-I_offline.html": os.path.join(OUT, "AulaViva_Programacao_para_Internet_I.html"),
    "apps-offline/AulaViva_LP2_offline.html": os.path.join(OUT, "AulaViva_Linguagem_de_Programacao_II.html"),
}
def atualiza_zip(nome_zip, mapa, raiz_prefixo=None):
    """Substitui entradas de um zip mantendo as demais intactas."""
    caminho = os.path.join(OUT, nome_zip)
    tmp = caminho + ".tmp"
    n_sub = 0
    with zipfile.ZipFile(caminho) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            key = item.filename
            if raiz_prefixo:
                key = os.path.relpath(item.filename, raiz_prefixo)
            if key in mapa:
                dados = open(mapa[key], "rb").read()
                n_sub += 1
            else:
                dados = zin.read(item.filename)
            zout.writestr(item.filename, dados)
    os.replace(tmp, caminho)
    return n_sub

n = atualiza_zip("Kit_Sala_de_Aula.zip", novos)
print("Kit_Sala_de_Aula.zip: entradas substituídas =", n)

# ---------- 3) Kit_Alunos.zip: Kit_Alunos/AulaViva_PI-I.html / LP2 ----------
alunos = {
    "Kit_Alunos/AulaViva_PI-I.html": novos["apps-offline/AulaViva_PI-I_offline.html"],
    "Kit_Alunos/AulaViva_LP2.html": novos["apps-offline/AulaViva_LP2_offline.html"],
}
n = atualiza_zip("Kit_Alunos.zip", alunos)
print("Kit_Alunos.zip: entradas substituídas =", n)

# ---------- 4) conferência: entradas dos zips == arquivos novos ----------
for znome, entradas in (("Kit_Sala_de_Aula.zip", ["apps-offline/AulaViva_PI-I_offline.html",
                                                   "apps-offline/AulaViva_LP2_offline.html"]),
                        ("Kit_Alunos.zip", ["Kit_Alunos/AulaViva_PI-I.html",
                                            "Kit_Alunos/AulaViva_LP2.html"])):
    with zipfile.ZipFile(os.path.join(OUT, znome)) as z:
        for e in entradas:
            dentro = z.read(e)
            src = None
            for v in list(novos.values()) + list(alunos.values()):
                if md5(dentro) == md5(open(v, "rb").read()):
                    src = os.path.basename(v); break
            print(f"  {znome}::{e} -> {src or '?? DIVERGENTE'} ({len(dentro)} bytes)")

# ---------- 5) mídia da turma (videoaulas/) nos kits ----------
import shutil as _sh
VID = os.path.join(ROOT, "videoaulas")
media_arqs = []
for raiz, _, arqs in os.walk(VID):
    for a in sorted(arqs):
        fp = os.path.join(raiz, a)
        media_arqs.append((os.path.relpath(fp, VID).replace(os.sep, "/"), fp))

def add_media(nome_zip, prefixo):
    caminho = os.path.join(OUT, nome_zip)
    tmp = caminho + ".tmp"
    with zipfile.ZipFile(caminho) as zin:
        existentes = set(zin.namelist())
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                zout.writestr(item, zin.read(item.filename))
            n = 0
            for rel, fp in media_arqs:
                alvo = prefixo + rel
                if alvo in existentes:
                    continue
                zout.write(fp, alvo)   # mp4/mp3: sem comprimir demais (store p/ mp4)
                n += 1
    os.replace(tmp, caminho)
    return n

print("Kit_Sala_de_Aula.zip: +videoaulas =", add_media("Kit_Sala_de_Aula.zip", "videoaulas/"))
print("Manutencao_Redserver_v2.zip: +videoaulas =",
      add_media("Manutencao_Redserver_v2.zip", "Manutencao_Redserver_v2/videoaulas/"))

# passo a passo em PDF também no kit dos alunos (leve, sem mp4)
def add_arqs(nome_zip, pares):
    caminho = os.path.join(OUT, nome_zip)
    tmp = caminho + ".tmp"
    with zipfile.ZipFile(caminho) as zin:
        existentes = set(zin.namelist())
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                zout.writestr(item, zin.read(item.filename))
            n = 0
            for alvo, fp in pares:
                if alvo in existentes:
                    continue
                zout.write(fp, alvo); n += 1
    os.replace(tmp, caminho)
    return n

pares_alunos = [("Kit_Alunos/Passo_a_Passo_Videoaula_PI-I_Loja_Tech.pdf",
                 os.path.join(VID, "Passo_a_Passo_Videoaula_PI-I_Loja_Tech.pdf")),
                ("Kit_Alunos/Passo_a_Passo_Videoaula_LP2_VB6.pdf",
                 os.path.join(VID, "Passo_a_Passo_Videoaula_LP2_VB6.pdf"))]
print("Kit_Alunos.zip: +passos =", add_arqs("Kit_Alunos.zip", pares_alunos))
