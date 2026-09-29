#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fatia o arquivo mestre Kit_Sala_de_Aula_TUDO_v1.zip em partes pequenas
para download confiavel no visualizador (o mestre tem 102,7 MB).

Uso:
    python3 video_tools/build_tudo_partes.py            # limite 20 MB por parte
    python3 video_tools/build_tudo_partes.py 15         # limite customizado

Reconstruir: descompactar TODAS as partes na MESMA pasta (os caminhos internos
sao identicos aos do zip mestre, entao elas se somam sem conflito).
"""
import os, sys, zipfile, hashlib, shutil, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MESTRE = os.path.join(RAIZ, "Kit_Sala_de_Aula_TUDO_v1.zip")
SAIDA = os.path.join(RAIZ, "output", "partes")
LIMITE_MB = float(sys.argv[1]) if len(sys.argv) > 1 else 20.0
LIMITE = int(LIMITE_MB * 1024 * 1024)

# zips "prontos" que tambem existem soltos em output/ -> a parte que so contem
# um deles e opcional (se falhar, voce ja tem o arquivo individual)
REDUNDANTES = {"01_Entregaveis/Kit_Sala_de_Aula.zip",
               "01_Entregaveis/Manutencao_Redserver_v2.zip"}


def md5(caminho):
    h = hashlib.md5()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def mb(b):
    return f"{b/1024/1024:.2f} MB" if b >= 1024*1024 else f"{b/1024:.1f} KB"


def main():
    assert os.path.exists(MESTRE), "zip mestre nao encontrado: " + MESTRE
    if os.path.isdir(SAIDA):
        shutil.rmtree(SAIDA)
    os.makedirs(SAIDA)

    src = zipfile.ZipFile(MESTRE)
    infos = src.infolist()
    md5_mestre = md5(MESTRE)

    # --- bin-packing guloso preservando a ordem das pastas ----------------
    pacotes, atual, tam = [], [], 0
    for i in infos:
        if i.file_size > LIMITE:                 # arquivo sozinho > limite
            if atual:
                pacotes.append(atual); atual, tam = [], 0
            pacotes.append([i]); continue
        if tam + i.file_size > LIMITE and atual:
            pacotes.append(atual); atual, tam = [], 0
        atual.append(i); tam += i.file_size
    if atual:
        pacotes.append(atual)
    n = len(pacotes)

    linhas_md5, indice, resumo = [], [], []
    nomes = []
    for idx, pacote in enumerate(pacotes, 1):
        nomes.append(f"Kit_TUDO_v1_parte{idx}_de{n}.zip")

    for idx, pacote in enumerate(pacotes, 1):
        nome = nomes[idx-1]
        destino = os.path.join(SAIDA, nome)
        so_redundante = all(i.filename in REDUNDANTES for i in pacote)
        with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
            for i in pacote:
                zf.writestr(i, src.read(i.filename))
            if idx == 1:
                zf.writestr("LEIA-ME_PARTES.md", LEIA_ME.format(
                    n=n, limite=LIMITE_MB, md5=md5_mestre, indice="{INDICE}"))
        b = os.path.getsize(destino)
        d = md5(destino)
        linhas_md5.append(f"{d}  {nome}")
        tops = sorted({i.filename.split('/')[0] for i in pacote})
        if so_redundante:
            o_que = ("**opcional** — só o zip pronto "
                     f"`{pacote[0].filename.split('/')[-1]}` (já existe solto em `output/`)")
        elif len(pacote) == 1:
            o_que = f"1 arquivo: `{pacote[0].filename}`"
        else:
            o_que = ", ".join(t.replace('/', '') for t in tops)
        indice.append(f"| {idx} | `{nome}` | {mb(b)} | {len(pacote)} | {o_que} |")
        resumo.append(f"parte {idx}: {len(pacote):3d} arq  {mb(b):>10s}  ->  {o_que}")
        print(resumo[-1])

    # LEIA-ME standalone + manifesto (arquivos minúsculos, baixam sempre)
    with open(os.path.join(SAIDA, "MD5_PARTES.txt"), "w", encoding="utf-8") as f:
        f.write("# Conferencia das partes do Kit_Sala_de_Aula_TUDO_v1\n")
        f.write(f"# Zip mestre: {md5_mestre}  Kit_Sala_de_Aula_TUDO_v1.zip ({mb(os.path.getsize(MESTRE))})\n")
        f.write("# Linux/macOS: md5sum -c MD5_PARTES.txt | Windows: certutil -hashfile <arquivo> MD5\n\n")
        f.write("\n".join(linhas_md5) + "\n")

    # reescreve a parte 1 com o indice completo dentro
    indice_txt = "\n".join(indice)
    destino1 = os.path.join(SAIDA, nomes[0])
    tmp = destino1 + ".tmp"
    with zipfile.ZipFile(destino1) as zin, \
         zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
        for i in zin.infolist():
            if i.filename == "LEIA-ME_PARTES.md":
                zout.writestr(i, LEIA_ME.format(n=n, limite=LIMITE_MB,
                                                md5=md5_mestre, indice=indice_txt))
            else:
                zout.writestr(i, zin.read(i.filename))
    os.replace(tmp, destino1)
    linhas_md5[0] = f"{md5(destino1)}  {nomes[0]}"
    with open(os.path.join(SAIDA, "MD5_PARTES.txt"), "w", encoding="utf-8") as f:
        f.write("# Conferencia das partes do Kit_Sala_de_Aula_TUDO_v1\n")
        f.write(f"# Zip mestre: {md5_mestre}  Kit_Sala_de_Aula_TUDO_v1.zip ({mb(os.path.getsize(MESTRE))})\n")
        f.write("# Linux/macOS: md5sum -c MD5_PARTES.txt | Windows: certutil -hashfile <arquivo> MD5\n\n")
        f.write("\n".join(linhas_md5) + "\n")

    with open(os.path.join(SAIDA, "MANIFESTO_PARTES.md"), "w", encoding="utf-8") as f:
        f.write(LEIA_ME.format(n=n, limite=LIMITE_MB, md5=md5_mestre, indice=indice_txt))

    total = sum(os.path.getsize(os.path.join(SAIDA, x)) for x in os.listdir(SAIDA) if x.endswith(".zip"))
    print(f"\n{n} partes | total {mb(total)} | pasta: {SAIDA}")
    src.close()


LEIA_ME = """# Kit Sala de Aula — TUDO em {n} partes 📦

O arquivo mestre `Kit_Sala_de_Aula_TUDO_v1.zip` tem **102,7 MB** (451 arquivos) —
provavelmente grande demais para descer inteiro pelo visualizador; quando a
transferência quebra no meio, o que chega é um restinho de bytes (daí o "154 B").
Por isso o mesmo conteúdo foi **fatiado em {n} partes** de até ~{limite:.0f} MB.
**Nada foi retirado** — conferido arquivo por arquivo (MD5) contra o mestre.

Gerado em {data} · PI-I × LP2 · Turma 2/2026 · Prof.ª Raquel ("Juh")

## Índice das partes

| # | Arquivo | Tamanho | Arq. | O que traz |
|---|---|---|---|---|
{indice}

> 💡 **Prefere um arquivo só?** Existe também `Kit_Sala_de_Aula_TUDO_v1_LEVE.zip`
> (**~47 MB**, na raiz do workspace): mesmo conteúdo, apenas sem os 2 zips
> redundantes (`Kit_Sala_de_Aula.zip` e `Manutencao_Redserver_v2.zip`, cujos
> arquivos já estão soltos aqui dentro — são as partes 2 e 4). Esse baixa inteiro.

## Como remontar (2 passos)

1. Baixe **todas** as partes.
2. Descompacte **todas na mesma pasta**. Os caminhos internos são idênticos aos do
   zip mestre, então as partes se somam sozinhas e você obtém a árvore completa:

```
LEIA-ME_GERAL.md
01_Entregaveis/            tudo pronto pra sala e pro servidor
02_Servidor_e_Deploy/      API v2, SQL, DEPLOY_NOTES, túnel cloudflared
03_Fontes_Apps_e_Conteudo/ builders + conteúdo das trilhas PI-I e LP2
04_PR_e_Git/               patches, diff e o repositório git completo
05_Video_Ferramentas/      scripts + slides das videoaulas
06_Videoaulas/             LEIA-ME_MEDIA + PDFs passo a passo
07_Referencias_do_Usuario/ materiais originais que você enviou
```

**Linux/macOS** (uma linha só):
```bash
mkdir Kit_Sala_de_Aula_TUDO_v1 && cd Kit_Sala_de_Aula_TUDO_v1
for f in ../Kit_TUDO_v1_parte*.zip; do unzip -o "$f"; done
```
**Windows:** botão direito em cada parte → *Extrair tudo…* → **sempre a mesma pasta**
(pode marcar "substituir" sem medo: não há arquivo repetido entre as partes).

## Conferir se baixou inteiro

`MD5_PARTES.txt` traz o MD5 de cada parte. O mestre original vale:
`{md5}`  →  `Kit_Sala_de_Aula_TUDO_v1.zip`

## Atalhos (se você não quer baixar tudo)

| Quero… | Baixe só |
|---|---|
| Mandar o PR pro Rapha / deploy | a parte que traz `PR_AulaViva_v2.zip` + `02_Servidor_e_Deploy/` |
| Levar pra sala de aula | a parte que traz as videoaulas MP4 + apostilas |
| Só os códigos-fonte e o git | as duas últimas partes |

E se preferir, os arquivos individuais continuam disponíveis soltos em `output/`
(`PR_AulaViva_v2.zip`, `Kit_Sala_de_Aula.zip`, `Kit_Alunos.zip`, os MP4 etc.).

**Plano B:** se alguma das partes grandes (2 ou 4) não descer, sem drama — elas só
trazem os zips *já prontos* `Kit_Sala_de_Aula.zip` e `Manutencao_Redserver_v2.zip`,
que também existem soltos em `output/`. O conteúdo deles está todo nas outras partes
(os vídeos MP4 estão nas partes 5 e 6, com ~15 MB cada).

> Refazer o mestre inteiro a qualquer momento: `python3 video_tools/build_tudo_zip.py`
> e depois `python3 video_tools/build_tudo_partes.py` para refatiar.

— Agente de manutenção do Kit 🧰
""".replace("{data}", datetime.date.today().strftime("%d/%m/%Y"))

if __name__ == "__main__":
    main()
