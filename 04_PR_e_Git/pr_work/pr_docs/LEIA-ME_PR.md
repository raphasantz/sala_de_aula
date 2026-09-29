# LEIA-ME — Pacote do PR: AulaViva v2

Oi professora! Aqui está o PR prontinho pro Rapha aplicar no repositório
`raphasantz/kit-sala-de-aula`. Como eu (Qwen) não tenho credenciais de GitHub
neste ambiente, montei o pacote no formato combinado: **branch pronta em
patches + arquivos + descrição do PR**. É só seguir uma das opções abaixo.

## Conteúdo deste pacote

| Item | O que é |
|---|---|
| `patches/0001..0008-*.patch` | Os 8 commits da branch, em ordem (formato `git am`) |
| `PR_completo.diff` | O diff inteiro (master → branch) para revisão rápida |
| `arquivos_branch/` | Árvore final completa da branch (fallback: copiar e colar) |
| `PR_DESCRICAO.md` | Título + corpo do PR prontos para colar no GitHub |
| `extras/DEPLOY_NOTES.md` | Notas de deploy atualizadas (túnel, mídia, hotfix do título LP2) — copie para `redserver/DEPLOY_NOTES.md` após o merge; fica fora dos patches para não expor usuário/IP do servidor |
| `extras/Checklist_Deploy_PR_AulaViva_v2.pdf` | **1 página para imprimir**: as 4 etapas (branch → merge → deploy no servidor → teste de aceite). Responde à pergunta "só subir o PR já resolve?" — não: o merge entrega o código, o ar só muda na etapa 3 |

## Opção A — aplicar os patches no repo real (recomendado)

```bash
git clone https://github.com/raphasantz/kit-sala-de-aula.git
cd kit-sala-de-aula
git checkout -b feature/rapida-aulaviva-v2
git am /caminho/deste/pacote/patches/*.patch
git push -u origin feature/rapida-aulaviva-v2
```

Depois do push, o GitHub mostra o botão **"Compare & pull request"** na página do
repo — clique, cole o conteúdo de `PR_DESCRICAO.md` e pronto. (Se tiver o `gh`
instalado: `gh pr create --title "AulaViva v2 — login, entregas, histórico, retomada, paginador e materiais só da professora (+fix LP2)" --body-file PR_DESCRICAO.md`.)

> Se o `git am` reclamar de conflito (pode acontecer se o `api.php` da master foi
> editado direto no servidor com senhas reais): rode `git am --abort` e use a Opção B.

## Opção B — cópia manual (sempre funciona)

1. Crie a branch: `git checkout -b feature/rapida-aulaviva-v2`
2. Copie tudo de `arquivos_branch/` para a raiz do repo (os caminhos são idênticos:
   `aulaviva/…` e `apps-nuvem/…` e `apps-offline/…`) — **sobrescrevendo** os existentes.
3. Commit (pode ser um só): use as mensagens dos commits 1..8 dos patches, ou:
   `git commit -am "feat(aulaviva): AulaViva v2 — contas/senha, entregas, histórico, retomada, paginador, materiais só da professora, porta de entrada no login, túnel sem aviso + fix DISC LP2"`
4. `git push -u origin feature/rapida-aulaviva-v2` e abra o PR no site colando `PR_DESCRICAO.md`.

## "Só subir o PR já resolve?" — não, e é rápido de entender

Pense em três caixas separadas:

1. **GitHub (o PR)** = a *receita* guardada no caderno. Merger só muda o repositório.
2. **Servidor (redserver)** = a *cozinha*. Nada do que está no caderno entra em
   funcionamento até alguém executar o deploy lá: rodar o SQL, criar as pastas de
   `materiais/`+`entregas/`, colocar o token novo no php-fpm e enviar por scp o
   `api.php`, o `index.php` da raiz, os 4 HTML da nuvem e a pasta `videoaulas/`.
3. **O link que a turma usa** = o *prato na mesa*. Ele só muda depois da etapa 2.

O git **não carrega**: binários de mídia (mp4/mp3), o banco de dados, as variáveis de
ambiente nem as permissões de pasta — por isso esses itens estão na etapa 3.
Tudo está listado, em ordem e marcável, no `extras/Checklist_Deploy_PR_AulaViva_v2.pdf`
(1 página, 21 itens + teste de aceite).

Tempo realista: etapa 1 ≈ 5 min · etapa 2 ≈ 5 min · etapa 3 ≈ 20 min · etapa 4 ≈ 10 min.
Se o Rapha só puder fazer uma coisa hoje: **etapa 3 completa** (o merge pode até vir depois —
os arquivos da branch servem de fonte para o scp).

Enquanto isso, a v1 que está no ar continua funcionando (com o `Hotfix_v1_tags_HTML.zip`
aplicado para o bug das alternativas).

## Depois do merge — deploy no redserver (Rapha/Hermes)

Resumo (detalhes em `arquivos_branch/aulaviva/LEIA-ME_MIGRACAO.md`):

1. `mysql -u root -p loja_turma < aulaviva/migracao_contas_entregas.sql`
2. Substituir `Kit_Sala_de_Aula/aulaviva/api.php` (scp + md5, como sempre)
3. `mkdir -p aulaviva/materiais/{pi1,lp2} aulaviva/entregas/{pi1,lp2}` + `chown -R www-data`
4. php-fpm do vhost: `env[LOJA_DB_PASS]` e `env[AULAVIVA_PROF_TOKEN]` (**token novo** — rotacionar o antigo!)
5. Enviar os 4 HTML de `apps-nuvem/` (e os 2 de `apps-offline/` para o pendrive)
6. Copiar a pasta `videoaulas/` para a raiz do kit (vídeos, passo a passo em PDF e
   áudios de módulo que existirem) — contrato em `videoaulas/LEIA-ME_MEDIA.md`
7. Testar pela URL do túnel com o checklist da `PR_DESCRICAO.md`; apagar resíduos `qa_*`

## O que há de novo nesta revisão do pacote

- **Mídia de sala de aula** (rebuild do commit 7 + docs do commit 8): cartão 🎬 Videoaula na trilha (mp4 da pasta
  `videoaulas/` em player interno), botão 🔊 de áudio **opcional** por módulo (só
  aparece se o mp3 existir) e botão 👀 "Ver resolução passo a passo" em cada
  exercício (pseudocódigo/código/árvore + gabarito; Módulo 1 da LP2 completo para
  o dia sem laboratório). Binários de mídia não vão no git: estão nos kits zip
  (`videoaulas/`) e sobem por scp — o repo leva só o `LEIA-ME_MEDIA.md`.
- **Hotfix documentado** (DEPLOY_NOTES): o app v1 da LP2 em produção exibe o título
  "Programação para Internet I"; um `sed` de uma linha corrige hoje, o merge do PR
  resolve de vez.

- **Commit 5** — paginador dos módulos: "Página X de Y" + ⏮ Início / ◀ Voltar /
  campo para digitar a página / Próximo ▶ / ⏭ Fim em toda página do módulo, e o
  total de páginas nos cards da trilha.
- **Commit 6** — materiais exclusivos da professora: a partir do login do aluno,
  itens com "professor"/"painel" no nome (Painel do Professor, Guia da Professora,
  Apostila do Professor…) **somem** da lista 📎 Materiais — filtro no `api.php`
  (rota `arq`, por sessão) e no front dos 4 apps. Para a conta ADM ("Juh") tudo
  continua visível.
- **Commit 7** — porta de entrada: `index.php` novo na raiz do kit faz 302 para o
  app da disciplina (`?d=lp2` p/ LP2); o app abre **já pedindo nome + senha**.
  Se o login falhar, botão "🆕 É minha primeira vez — criar conta" troca de aba
  sem perder o nome digitado.
- **Commit 8** — túnel sem tela de aviso: `redserver/tunel/` (sobe-tunel.sh,
  serviço systemd, LEIA-ME) publica o vhost via cloudflared quick tunnel — o
  ngrok grátis interpunha o "Visit Site". DEPLOY_NOTES.md atualizado.

## ⚠️ Importante — zips ANTIGOS com bug

Se vocês chegaram a baixar os zips v2 que mandei antes deste PR
(`Manutencao_Redserver_v2.zip`, `Kit_Sala_de_Aula_v2.zip`, `Kit_Sala_de_Aula.zip`,
`Kit_Alunos.zip`), **não usem**: a LP2 saía com `DISC="pi1"` (misturava as turmas).
Todos foram **regerados corrigidos** (mesmos nomes, em `output/`). O v1 que está
no ar hoje NÃO tem esse problema — podem manter até o deploy do v2.

## Corretivo imediato para a v1 que está no ar

O pacote `Hotfix_v1_tags_HTML.zip` (em `output/`) conserta o bug do checkpoint com
alternativas em tags HTML (`<head>`, `<title>`…) **na v1 em produção**, sem esperar
o merge deste PR: 4 arquivos substitutos (2 nuvem + 2 offline), patch que aplica
limpo em `master` e LEIA-ME com passo a passo de scp+md5. A v2 deste PR já nasce
com a proteção (`rich()`), então após o deploy o hotfix é descartável.

## Regra de ouro respeitada

Nada de push em `master`; branch por tarefa; mudanças mínimas; sem renomear
caminhos; sem credencial nova no código; sem localStorage na nuvem. ✔
