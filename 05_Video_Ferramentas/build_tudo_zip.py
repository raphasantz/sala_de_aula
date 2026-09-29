#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_tudo_zip.py — monta o ZIP mestre "todo conteúdo" do Kit Sala de Aula.

Regras:
  - Inclui: entregáveis (output/), fontes de servidor, material/conteúdo,
    maquinário do PR (com o repo git), ferramentas de vídeo (scripts+slides),
    mídia canônica (videoaulas/ sem os mp4 duplicados) e referências (uploads/).
  - Exclui: duplicidades e regeneráveis (mp4 idênticos, áudios brutos já
    embutidos nos vídeos, frames work/work2, fonts/, _rezip, PR/ kitv1full/
    hotfix/ de pr_work, Hotfix_v1_tags_HTML/ solto, __pycache__).
  - Já comprimidos (zip/mp4/pdf/png/...) entram STORED; texto entra DEFLATED.
"""
import collections
import datetime
import hashlib
import os
import sys
import zipfile
from pathlib import Path

HOJE = datetime.date.today().strftime("%d/%m/%Y")

ROOT = Path(__file__).resolve().parent.parent          # /home/user
OUT_ZIP = ROOT / "Kit_Sala_de_Aula_TUDO_v1.zip"
LEIAME = ROOT / "LEIA-ME_GERAL.md"

STORED_EXT = {".zip", ".mp4", ".mp3", ".pdf", ".png", ".jpg", ".jpeg",
              ".pptx", ".docx", ".xlsx", ".ttf", ".woff", ".woff2", ".gif"}

# (pasta_de_origem, prefixo_dentro_do_zip)
INCLUDE_MAP = [
    ("output",            "01_Entregaveis"),
    ("redserver",         "02_Servidor_e_Deploy/redserver"),
    ("deploy",            "02_Servidor_e_Deploy/deploy"),
    ("deploy-supabase",   "02_Servidor_e_Deploy/deploy-supabase"),
    ("material",          "03_Fontes_Apps_e_Conteudo/material"),
    ("projeto-loja",      "03_Fontes_Apps_e_Conteudo/projeto-loja"),
    ("pr_work",           "04_PR_e_Git/pr_work"),
    ("video_tools",       "05_Video_Ferramentas"),
    ("videoaulas",        "06_Videoaulas"),
    ("uploads",           "07_Referencias_do_Usuario"),
]

# Exclusões por caminho relativo à RAIZ do workspace (diretórios inteiros)
EXCLUDE_DIRS = {
    "output/partes",                     # fatiamento do próprio mestre (recursão!)
    "output/Hotfix_v1_tags_HTML",        # duplicado do .zip
    "material/_rezip",                   # staging de rezipe (já está nos zips)
    "pr_work/PR",                        # duplicado de output/PR_AulaViva_v2.zip
    "pr_work/kitv1full",                 # duplicado do kit v1 (já no hotfix zip)
    "pr_work/hotfix",                    # duplicado de output/Hotfix_v1_tags_HTML.zip
    "video_tools/work",                  # frames intermediários
    "video_tools/work2",                 # frames intermediários
    "video_tools/__pycache__",
    "videoaulas/audio",                  # vazio (áudios por módulo ainda não gerados)
}
EXCLUDE_FILES = {
    str(OUT_ZIP.relative_to(ROOT)),      # nunca incluir a si mesmo
    "LEIA-ME_GERAL.md",                  # entra como primeira entrada, à parte
}

def keep(rel: str) -> bool:
    if rel in EXCLUDE_FILES:
        return False
    parts = rel.split("/")
    if "__pycache__" in parts:
        return False
    for d in EXCLUDE_DIRS:
        if rel == d or rel.startswith(d + "/"):
            return False
    # fontes binárias pesadas que só servem p/ regenerar PDFs
    if rel.startswith("videoaulas/") and rel.endswith(".mp4"):
        return False   # idênticos aos de output/ (md5 batido)
    return True

def md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def coletar():
    pares = []  # (path_abs, nome_no_zip)
    for src, dst in INCLUDE_MAP:
        base = ROOT / src
        if not base.exists():
            print(f"AVISO: {src} não existe, pulando")
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames
                                  if keep(str(Path(dirpath, d).relative_to(ROOT))))
            for fn in sorted(filenames):
                abs_p = Path(dirpath, fn)
                rel = str(abs_p.relative_to(ROOT))
                if not keep(rel):
                    continue
                nome = dst + "/" + str(abs_p.relative_to(base))
                pares.append((abs_p, nome.replace("\\", "/")))
    return pares

def human(n: float) -> str:
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024 or u == "GB":
            return f"{n:.1f} {u}" if u != "B" else f"{int(n)} B"
        n /= 1024

def main():
    pares = coletar()
    print(f"Arquivos coletados: {len(pares)}")
    if len(pares) > 9500:
        print("ERRO: perto do limite de 10.000 arquivos do snapshot."); sys.exit(1)

    # ---- tabela md5 dos binários-chave (para o LEIA-ME e p/ scp do Rapha) ----
    chave = [
        "output/Kit_Sala_de_Aula.zip",
        "output/PR_AulaViva_v2.zip",
        "output/Manutencao_Redserver_v2.zip",
        "output/Hotfix_v1_tags_HTML.zip",
        "output/Kit_Alunos.zip",
        "output/Kit_Sala_de_Aula_v2.zip",
        "output/AulaViva_Kit_SoSupabase.zip",
        "output/AulaViva_Kit_Vercel_Supabase.zip",
        "output/Manutencao_Redserver.zip",
        "output/Video_Tutorial_PI-I_Loja_Tech.mp4",
        "output/Video_Tutorial_LP2_VB6.mp4",
    ]
    md5_rows = []
    for rel in chave:
        p = ROOT / rel
        if p.exists():
            md5_rows.append((rel.replace("output/", ""), human(p.stat().st_size), md5(p)))

    # ---- LEIA-ME geral (índice mestre) ----
    total_bytes = sum(p.stat().st_size for p, _ in pares)
    n_01 = sum(1 for _, n in pares if n.startswith("01_"))
    por_area = collections.Counter(n.split("/")[0] for _, n in pares)
    tab_area = "\n".join(
        f"| `{k}/` | {por_area[k]} arquivos | "
        f"{human(sum(p.stat().st_size for p, n in pares if n.startswith(k + '/')))} |"
        for k in sorted(por_area))
    linhas_md5 = "\n".join(f"| {a} | {b} | `{c}` |" for a, b, c in md5_rows)
    LEIAME.write_text(f"""# LEIA-ME GERAL — Kit Sala de Aula · ARQUIVO MESTRE ("todo conteúdo")

Gerado em {HOJE} · PI-I × LP2 · Turma 2/2026 · Curso Técnico em Informática · Prof.ª Raquel ("Juh")
Repositório: `raphasantz/kit-sala-de-aula` (privado) — entregas via pacotes/zip (sem push direto).

Este ZIP reúne **tudo** o que foi produzido no projeto: {len(pares)} arquivos,
{human(total_bytes)} sem compressão. É o pacote definitivo para backup/transferência.

> ⚠️ **Este arquivo tem ~103 MB — grande demais para descer inteiro pelo
> visualizador.** Se o download chegar truncado (tamanho esquisito, tipo "154 B"),
> você tem **duas saídas**:
>
> 1. **`Kit_Sala_de_Aula_TUDO_v1_LEVE.zip` (~47 MB, arquivo único)** — mesmo
>    conteúdo, sem os 2 zips redundantes (`Kit_Sala_de_Aula.zip` e
>    `Manutencao_Redserver_v2.zip`, cujo conteúdo já está solto aqui dentro).
>    Gerar: `python3 video_tools/build_tudo_leve.py`.
> 2. **Versão fatiada em `output/partes/`** — `Kit_TUDO_v1_parte1_de7.zip` …
>    `parte7_de7.zip` (≤ 30 MB cada), **100% idêntica a este mestre** (conferido
>    MD5 a MD5): basta extrair as 7 partes **na mesma pasta**. Índice e instruções
>    em `output/partes/MANIFESTO_PARTES.md`. Refatiar: `python3 video_tools/build_tudo_partes.py`.

## O que tem dentro (mapa das pastas)

| Pasta | Conteúdo |
|---|---|
| `01_Entregaveis/` | **TUDO que é entregue pronto** ({n_01} arquivos): kits zipados (Sala de Aula, Alunos, Manutenção, PR, Hotfix v1), videoaulas MP4, apostilas/aluno+professor, apresentações PPTX, guias e textos de apoio em PDF, cronogramas, apps HTML offline, roteiros e checklists. |
| `02_Servidor_e_Deploy/` | Código de servidor: `redserver/` (API v2, SQL, DEPLOY_NOTES sanitizado, túnel cloudflared), `deploy/` e `deploy-supabase/` (cópias congeladas vacinadas contra o bug das tags HTML). |
| `03_Fontes_Apps_e_Conteudo/` | Fábrica dos apps: `material/build_aula_app.py`, `build_kits_v2.py`, `build_deploy_supabase.py`, conteúdo das trilhas (`conteudo/`, `conteudo_lp2/` — inclui resoluções passo a passo do Módulo 1 LP2), geradores de PDF e `projeto-loja/`. |
| `04_PR_e_Git/` | Maquinário do PR: **`pr_work/repo/` é o repositório git completo** (baseline v1 + 9 commits da branch v2), scripts `make_repo.py`/`rezipa.py`/`valida_pr_final.py`, mensagens de commit e docs do PR. |
| `05_Video_Ferramentas/` | Scripts que geraram as videoaulas e PDFs (`slides.py`, `monta.py`, `slides_lp2.py`, `monta_lp2.py`, `gerar_pdf_passo.py`, `gerar_guia_tunel.py`, `gerar_checklist_deploy.py`) + os slides PNG das duas aulas. |
| `06_Videoaulas/` | Pasta canônica de mídia do servidor: `LEIA-ME_MEDIA.md` + PDFs Passo a Passo. **Os MP4 não estão aqui de propósito** — são byte-idênticos aos de `01_Entregaveis/` (veja md5 abaixo). Para o servidor, renomeie: `Video_Tutorial_PI-I_Loja_Tech.mp4` → `Videoaula_Programacao_para_Internet_I.mp4` e `Video_Tutorial_LP2_VB6.mp4` → `Videoaula_Linguagem_de_Programacao_II.mp4`. |
| `07_Referencias_do_Usuario/` | Materiais originais enviados pela Juh/Rapha: calendário escolar, cronogramas-modelo, planejamentos LP2, handovers do agente e as capturas de tela que originaram o diagnóstico do bug. |

## MD5 dos binários-chave (conferir após scp)

| Arquivo (em `01_Entregaveis/`) | Tamanho | MD5 |
|---|---|---|
{linhas_md5}

MD5 dos vídeos na pasta canônica do servidor (mesmos bytes dos acima):
- `Videoaula_Programacao_para_Internet_I.mp4` = `99f5e6e3dd9aeae2f404d60c64b52964`
- `Videoaula_Linguagem_de_Programacao_II.mp4` = `7051dec380f47770635dc411600e3e47`

## Prova de completude (nada ficou para trás)

| Área dentro do zip | Arquivos | Peso |
|---|---|---|
{tab_area}
| **TOTAL** | **{len(pares)}** | **{human(total_bytes)}** |

Verificação independente: `05_Video_Ferramentas/conferencia_completude.py` varre o
workspace inteiro e compara com o conteúdo deste zip → resultado esperado
**"FALTANDO no mestre: 0"**. E `verifica_partes.py` confere que as 7 partes,
somadas, reproduzem este zip byte a byte → **"VEREDITO: IDENTICO ✔"**.

## O que ficou de FORA (e por quê)

- **MP4 duplicados** de `videoaulas/` — mesmos bytes dos de `01_Entregaveis/` (md5 idêntico).
- **Áudios brutos** (`audio_vid/`, `audio_vid2/`) — já embutidos nos MP4 finais.
- **Frames intermediários** (`video_tools/work*/`) — regeneráveis pelos scripts.
- **`fonts/`** (Inter + JetBrains Mono, 37 MB) — usadas só para renderizar PDFs/slides;
  se precisar regenerar, baixe as mesmas famílias no Google Fonts e reponha a pasta `fonts/`.
- **Staging duplicado** (`material/_rezip/`, `pr_work/PR|kitv1full|hotfix/`,
  `output/Hotfix_v1_tags_HTML/` solto) — o conteúdo final já está nos ZIPs de `01_Entregaveis/`.
- **`videoaulas/audio/`** — vazia de propósito: os áudios opcionais por módulo (27 clipes)
  ainda vão ser gerados; quando existirem, o builder liga os botões 🔊 automaticamente.

## Por onde começar

1. **Deploy no servidor (Rapha):** `01_Entregaveis/PR_AulaViva_v2.zip` +
   `Checklist_Deploy_PR_AulaViva_v2.pdf` (etapas 1–4) + `DEPLOY_NOTES.md` de `02_Servidor_e_Deploy/redserver/`.
   Lembrete amigo: *mergear o PR não deploya* — migration, env e mídia vão por scp.
2. **Enquanto a produção é v1:** aplicar `01_Entregaveis/Hotfix_v1_tags_HTML.zip`
   (bug dos botões vazios) e o `sed` do título LP2 documentado no DEPLOY_NOTES.
3. **Sala de aula (Juh):** `01_Entregaveis/Kit_Sala_de_Aula.zip` (tudo, +videoaulas) e
   `Kit_Alunos.zip` (o que o aluno pode ver).
4. **Sem ngrok/tela de aviso:** `02_Servidor_e_Deploy/redserver/tunel/LEIA-ME_TUNEL.md` +
   `01_Entregaveis/Guia_Do_Link_Sem_Misterio_Cloudflared.pdf`.

— Agente de manutenção do Kit 🧰
""", encoding="utf-8")

    # ---- monta o zip ----
    if OUT_ZIP.exists():
        OUT_ZIP.unlink()
    n = 0
    with zipfile.ZipFile(OUT_ZIP, "w", allowZip64=True) as z:
        z.write(LEIAME, "LEIA-ME_GERAL.md", compress_type=zipfile.ZIP_DEFLATED)
        n += 1
        for abs_p, nome in pares:
            ext = abs_p.suffix.lower()
            ct = zipfile.ZIP_STORED if ext in STORED_EXT else zipfile.ZIP_DEFLATED
            z.write(abs_p, nome, compress_type=ct)
            n += 1
            if n % 500 == 0:
                print(f"  ...{n} entradas")
    print(f"OK: {n} entradas -> {OUT_ZIP.name}")
    print(f"Tamanho final: {human(OUT_ZIP.stat().st_size)}")
    print(f"MD5 do mestre: {md5(OUT_ZIP)}")

if __name__ == "__main__":
    main()
