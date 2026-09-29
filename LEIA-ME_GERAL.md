# LEIA-ME GERAL — Kit Sala de Aula · ARQUIVO MESTRE ("todo conteúdo")

Gerado em 28/09/2026 · PI-I × LP2 · Turma 2/2026 · Curso Técnico em Informática · Prof.ª Raquel ("Juh")
Repositório: `raphasantz/kit-sala-de-aula` (privado) — entregas via pacotes/zip (sem push direto).

Este ZIP reúne **tudo** o que foi produzido no projeto: 455 arquivos,
109.6 MB sem compressão. É o pacote definitivo para backup/transferência.

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
| `01_Entregaveis/` | **TUDO que é entregue pronto** (48 arquivos): kits zipados (Sala de Aula, Alunos, Manutenção, PR, Hotfix v1), videoaulas MP4, apostilas/aluno+professor, apresentações PPTX, guias e textos de apoio em PDF, cronogramas, apps HTML offline, roteiros e checklists. |
| `02_Servidor_e_Deploy/` | Código de servidor: `redserver/` (API v2, SQL, DEPLOY_NOTES sanitizado, túnel cloudflared), `deploy/` e `deploy-supabase/` (cópias congeladas vacinadas contra o bug das tags HTML). |
| `03_Fontes_Apps_e_Conteudo/` | Fábrica dos apps: `material/build_aula_app.py`, `build_kits_v2.py`, `build_deploy_supabase.py`, conteúdo das trilhas (`conteudo/`, `conteudo_lp2/` — inclui resoluções passo a passo do Módulo 1 LP2), geradores de PDF e `projeto-loja/`. |
| `04_PR_e_Git/` | Maquinário do PR: **`pr_work/repo/` é o repositório git completo** (baseline v1 + 9 commits da branch v2), scripts `make_repo.py`/`rezipa.py`/`valida_pr_final.py`, mensagens de commit e docs do PR. |
| `05_Video_Ferramentas/` | Scripts que geraram as videoaulas e PDFs (`slides.py`, `monta.py`, `slides_lp2.py`, `monta_lp2.py`, `gerar_pdf_passo.py`, `gerar_guia_tunel.py`, `gerar_checklist_deploy.py`) + os slides PNG das duas aulas. |
| `06_Videoaulas/` | Pasta canônica de mídia do servidor: `LEIA-ME_MEDIA.md` + PDFs Passo a Passo. **Os MP4 não estão aqui de propósito** — são byte-idênticos aos de `01_Entregaveis/` (veja md5 abaixo). Para o servidor, renomeie: `Video_Tutorial_PI-I_Loja_Tech.mp4` → `Videoaula_Programacao_para_Internet_I.mp4` e `Video_Tutorial_LP2_VB6.mp4` → `Videoaula_Linguagem_de_Programacao_II.mp4`. |
| `07_Referencias_do_Usuario/` | Materiais originais enviados pela Juh/Rapha: calendário escolar, cronogramas-modelo, planejamentos LP2, handovers do agente e as capturas de tela que originaram o diagnóstico do bug. |

## MD5 dos binários-chave (conferir após scp)

| Arquivo (em `01_Entregaveis/`) | Tamanho | MD5 |
|---|---|---|
| Kit_Sala_de_Aula.zip | 29.6 MB | `5544b356541afeab61fce4ca7bbd8eff` |
| PR_AulaViva_v2.zip | 1.4 MB | `56640056e16c40d12e6a922bb7b45fe2` |
| Manutencao_Redserver_v2.zip | 26.4 MB | `af2a83d3c9c2f3b65233a7f67febcab8` |
| Hotfix_v1_tags_HTML.zip | 457.2 KB | `14f8119b68a4ce95005bdb864a222f3c` |
| Kit_Alunos.zip | 279.5 KB | `45b0a5716bf2c870f652522a9957812c` |
| Kit_Sala_de_Aula_v2.zip | 144.0 KB | `f7f93bf940050e225c5b7112d9374376` |
| AulaViva_Kit_SoSupabase.zip | 127.1 KB | `639c9d4ade77583764083c41faefb254` |
| AulaViva_Kit_Vercel_Supabase.zip | 122.2 KB | `c0eb057330e63d72ef33f746de97596f` |
| Manutencao_Redserver.zip | 122.3 KB | `4fe22c77cc8fc7a76af7af81094f1eef` |
| Video_Tutorial_PI-I_Loja_Tech.mp4 | 15.6 MB | `99f5e6e3dd9aeae2f404d60c64b52964` |
| Video_Tutorial_LP2_VB6.mp4 | 12.4 MB | `7051dec380f47770635dc411600e3e47` |

MD5 dos vídeos na pasta canônica do servidor (mesmos bytes dos acima):
- `Videoaula_Programacao_para_Internet_I.mp4` = `99f5e6e3dd9aeae2f404d60c64b52964`
- `Videoaula_Linguagem_de_Programacao_II.mp4` = `7051dec380f47770635dc411600e3e47`

## Prova de completude (nada ficou para trás)

| Área dentro do zip | Arquivos | Peso |
|---|---|---|
| `01_Entregaveis/` | 48 arquivos | 92.8 MB |
| `02_Servidor_e_Deploy/` | 34 arquivos | 1.2 MB |
| `03_Fontes_Apps_e_Conteudo/` | 101 arquivos | 3.2 MB |
| `04_PR_e_Git/` | 177 arquivos | 6.8 MB |
| `05_Video_Ferramentas/` | 68 arquivos | 3.1 MB |
| `06_Videoaulas/` | 3 arquivos | 118.5 KB |
| `07_Referencias_do_Usuario/` | 24 arquivos | 2.3 MB |
| **TOTAL** | **455** | **109.6 MB** |

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
