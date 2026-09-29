# Kit Sala de Aula — PI-I × LP2 (Turma 2/2026)

Backup completo do projeto Kit Sala de Aula — Curso Técnico em Informática, Prof.ª Raquel ("Juh").

Gerado em 28/09/2026 · 360 arquivos · ~110 MB sem compressão.

## Mapa das pastas

| Pasta | Conteúdo |
|---|---|
| `01_Entregaveis/` | Tudo que é entregue pronto: kits zipados, videoaulas MP4, apostilas (aluno+professor), apresentações PPTX, guias e textos de apoio em PDF, cronogramas, apps HTML offline, roteiros e checklists. |
| `02_Servidor_e_Deploy/` | Código de servidor: `redserver/` (API v2, SQL, DEPLOY_NOTES, túnel cloudflared), `deploy/` e `deploy-supabase/` (cópias congeladas vacinadas contra o bug das tags HTML). |
| `03_Fontes_Apps_e_Conteudo/` | Fábrica dos apps: `build_aula_app.py`, `build_kits_v2.py`, `build_deploy_supabase.py`, conteúdo das trilhas (`conteudo/`, `conteudo_lp2/`), geradores de PDF e `projeto-loja/`. |
| `04_PR_e_Git/` | Maquinário do PR: scripts `make_repo.py`/`rezipa.py`/`valida_pr_final.py`, mensagens de commit e docs do PR. |
| `05_Video_Ferramentas/` | Scripts que geraram as videoaulas e PDFs + os slides PNG das duas aulas. |
| `06_Videoaulas/` | Pasta canônica de mídia do servidor: `LEIA-ME_MEDIA.md` + PDFs Passo a Passo (os MP4 ficam em `01_Entregaveis/` — byte-idênticos). |
| `07_Referencias_do_Usuario/` | Materiais originais: calendário escolar, cronogramas-modelo, planejamentos, handovers e capturas de tela. |

## Documentação completa

- `LEIA-ME_GERAL.md` — arquivo mestre: mapa detalhado, MD5 dos binários-chave, prova de completude e instruções de deploy.

## Por onde começar

1. **Deploy no servidor:** `01_Entregaveis/PR_AulaViva_v2.zip` + `Checklist_Deploy_PR_AulaViva_v2.pdf` (etapas 1–4) + `DEPLOY_NOTES.md` de `02_Servidor_e_Deploy/redserver/`
2. **Produção em v1:** aplicar `01_Entregaveis/Hotfix_v1_tags_HTML.zip` (bug dos botões vazios)
3. **Sala de aula:** `01_Entregaveis/Kit_Sala_de_Aula_v2.zip` e `Kit_Alunos.zip`
