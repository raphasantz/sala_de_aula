#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera Kit_Sala_de_Aula_TUDO_v1_LEVE.zip: o MESMO conteúdo do mestre, menos os dois
zips "já prontos" que são redundantes (o conteúdo deles está solto no pacote):
  - 01_Entregaveis/Kit_Sala_de_Aula.zip        (29,5 MB: docs + os 2 MP4)
  - 01_Entregaveis/Manutencao_Redserver_v2.zip (26,4 MB: redserver + os 2 MP4)
Resultado: ~47 MB em arquivo único — tamanho que baixa inteiro sem quebrar.

Uso: python3 video_tools/build_tudo_leve.py
"""
import os, sys, zipfile, hashlib

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MESTRE = os.path.join(RAIZ, "Kit_Sala_de_Aula_TUDO_v1.zip")
DESTINO = os.path.join(RAIZ, "Kit_Sala_de_Aula_TUDO_v1_LEVE.zip")
PULAR = {"01_Entregaveis/Kit_Sala_de_Aula.zip",
         "01_Entregaveis/Manutencao_Redserver_v2.zip"}

NOTA = """# Versão LEVE — o que mudou em relação ao zip mestre?

**Nada de conteúdo foi perdido.** Esta versão é o `Kit_Sala_de_Aula_TUDO_v1.zip`
inteiro, menos **dois arquivos redundantes**:

| Removido daqui | Por quê | Onde pegar, se quiser |
|---|---|---|
| `01_Entregaveis/Kit_Sala_de_Aula.zip` (29,5 MB) | é um zip *de arquivos que já estão soltos* neste pacote (apostilas, apps, cronogramas e os 2 MP4) | `output/Kit_Sala_de_Aula.zip` |
| `01_Entregaveis/Manutencao_Redserver_v2.zip` (26,4 MB) | idem: traz `redserver/` + videoaulas, que já estão em `02_Servidor_e_Deploy/` e `01_Entregaveis/` | `output/Manutencao_Redserver_v2.zip` |

Ganho: **102,7 MB → ~47 MB** em um arquivo só (baixa inteiro, sem quebrar).

As videoaulas MP4 continuam aqui dentro, em `01_Entregaveis/`:
`Video_Tutorial_PI-I_Loja_Tech.mp4` e `Video_Tutorial_LP2_VB6.mp4`.
O PR completo também: `01_Entregaveis/PR_AulaViva_v2.zip` + `04_PR_e_Git/`.

Se você quiser o pacote 100% idêntico ao mestre, use as 7 partes de `output/partes/`
(instruções em `output/partes/MANIFESTO_PARTES.md`).

— Agente de manutenção do Kit 🧰
"""


def main():
    src = zipfile.ZipFile(MESTRE)
    if os.path.exists(DESTINO):
        os.remove(DESTINO)
    n = 0
    with zipfile.ZipFile(DESTINO, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        z.writestr("_LEIA-ME_VERSAO_LEVE.md", NOTA)
        for i in src.infolist():
            if i.filename in PULAR:
                continue
            z.writestr(i, src.read(i.filename))
            n += 1
    h = hashlib.md5(open(DESTINO, "rb").read()).hexdigest()
    b = os.path.getsize(DESTINO)
    print(f"{os.path.basename(DESTINO)}: {n} arquivos (+1 nota) | {b/1024/1024:.2f} MB")
    print("MD5:", h)
    assert zipfile.ZipFile(DESTINO).testzip() is None, "zip corrompido!"
    print("integridade: OK ✔")


if __name__ == "__main__":
    main()
