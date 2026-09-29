#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prova de completude: compara tudo que existe no workspace (menos intermediários
regeneráveis, documentados no LEIA-ME) com o conteúdo do zip mestre.
Imprime o que falta e uma tabela-resumo de cobertura por área.

Uso: python3 video_tools/conferencia_completude.py [mestre.zip]
"""
import os, sys, zipfile, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MESTRE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "Kit_Sala_de_Aula_TUDO_v1.zip")

# mesmas regras de exclusão do build_tudo_zip.py (regeneráveis/duplicados)
EXCLUIR = [
    "fonts/",                      # dependência de render (Google Fonts)
    "audio_vid/", "audio_vid2/",    # áudios brutos já embutidos nos MP4
    "video_tools/work/", "video_tools/work2/",  # frames intermediários
    "video_tools/__pycache__/",
    "material/_rezip/",             # staging de rezipe
    "pr_work/PR/", "pr_work/kitv1full/", "pr_work/hotfix/",  # duplicados dos zips
    "output/Hotfix_v1_tags_HTML/",  # duplicado do .zip
    "output/partes/",               # o próprio fatiamento
    "videoaulas/audio/",            # vazio (áudios por módulo ainda não gerados)
]
EXCLUIR += ["Kit_Sala_de_Aula_TUDO_v1.zip", "Kit_Sala_de_Aula_TUDO_v1_LEVE.zip",
            "LEIA-ME_GERAL.md"]

# videoaulas: mp4 ficam de fora do 06_ (são byte-idênticos aos de 01_)
def excluido(rel):
    for e in EXCLUIR:
        if rel == e.rstrip("/") or rel.startswith(e):
            return True
    if rel.startswith("videoaulas/") and rel.endswith(".mp4"):
        return True
    if "/__pycache__/" in rel or rel.endswith(".pyc"):
        return True
    return False

no_disco = []
for dp, dn, fn in os.walk(RAIZ):
    dn[:] = [d for d in dn if d != ".git" or "pr_work/repo/.git" in os.path.join(dp, d)]
    for f in fn:
        rel = os.path.relpath(os.path.join(dp, f), RAIZ).replace(os.sep, "/")
        if excluido(rel):
            continue
        no_disco.append(rel)

z = zipfile.ZipFile(MESTRE)
no_zip = set(z.namelist())
# tira o LEIA-ME interno e o readme das partes (extras do zip)
no_zip = {n for n in no_zip if not n.endswith("LEIA-ME_PARTES.md")}

# mapeia caminho no disco -> caminho no zip (prefixos 01_..07_)
PREF = {
    "output/": "01_Entregaveis/",
    "redserver/": "02_Servidor_e_Deploy/redserver/",
    "deploy/": "02_Servidor_e_Deploy/deploy/",
    "deploy-supabase/": "02_Servidor_e_Deploy/deploy-supabase/",
    "material/": "03_Fontes_Apps_e_Conteudo/material/",
    "projeto-loja/": "03_Fontes_Apps_e_Conteudo/projeto-loja/",
    "pr_work/": "04_PR_e_Git/pr_work/",
    "video_tools/": "05_Video_Ferramentas/",
    "videoaulas/": "06_Videoaulas/",
    "uploads/": "07_Referencias_do_Usuario/",
}
faltando = []
for rel in sorted(no_disco):
    alvo = None
    for k, v in PREF.items():
        if rel.startswith(k):
            alvo = v + rel[len(k):]
            break
    if alvo is None:
        faltando.append((rel, "(sem prefixo de destino)"))
    elif alvo not in no_zip:
        faltando.append((rel, alvo))

print(f"arquivos no disco (elegíveis): {len(no_disco)}")
print(f"arquivos dentro do mestre    : {len(no_zip)}")
print(f"FALTANDO no mestre           : {len(faltando)}")
for rel, alvo in faltando[:40]:
    print(f"  ✘ {rel}  ->  esperava '{alvo}'")

# cobertura por área
cov = collections.Counter()
for rel in no_disco:
    area = rel.split("/")[0]
    cov[area] += 1
print("\nCobertura por área (arquivos elegíveis no disco):")
for k in sorted(cov):
    print(f"  {k:20s} {cov[k]:4d}")
sys.exit(1 if faltando else 0)
