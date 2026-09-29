# AulaViva v2 — login com senha, entregas, histórico, retomada, paginador e materiais só da professora (+ fix crítico: LP2 sincronizava como PI-I)

## Resumo

Implementa a lista de 10 ajustes pedida pela professora no AulaViva (PI-I e LP2) e
corrige um **bug crítico do gerador** descoberto na revisão: os apps da LP2 saíam
com `DISC = "pi1"`, o que misturaria as duas turmas (mesmo cookie, mesmo painel,
mesmos materiais). O v1 em produção **não** é afetado (o bug nasceu na reescrita v2).
Inclui também dois pedidos extras: **navegação página a página** dos módulos
(commit 5) e a **privacidade dos materiais da professora** (commit 6) — aluno não
vê mais "Painel do Professor", "Guia da Professora" nem "Apostila do Professor"
na lista 📎 Materiais da turma.
E dois pedidos de campo: **porta de entrada** (commit 7 — o link da raiz cai
direto no app, que abre pedindo nome + senha) e **túnel sem tela de aviso**
(commit 8 — cloudflared no lugar do ngrok grátis) e **mídia de sala de aula**
(videoaula na trilha, áudio opcional por módulo e resolução passo a passo nos
exercícios — rebuild dentro do commit 7 + contrato da pasta no commit 8).

Branch: `feature/rapida-aulaviva-v2` · 8 commits · árvore final em `arquivos_branch/`

## ⚠️ Fix crítico: LP2 com disciplina errada

- **Causa**: no gerador, `"linguagem" in slug` era case-sensitive e o slug é
  `Linguagem_de_Programacao_II` (L maiúsculo) → LP2 virava `pi1`.
- **Impacto se fosse ao ar**: alunos da LP2 criariam conta na turma da PI-I
  (nome único cruzado entre disciplinas), painel da PI-I misturado, materiais
  trocados; no offline, os dois apps gravariam na mesma chave `localStorage`.
- **Correção**: `slug.lower()` + assert no builder (`const DISC = "lp2"` obrigatório
  no kit da LP2) + placeholder `__PAINEL__` p/ o link do painel nunca quebrar.

## O que muda (por commit)

1. **`aulaviva/api.php`** (substituição de conteúdo; mesmo caminho — nginx não muda)
   - Contas com **nome único + senha** (`reg`/`login`/`logout`/`check`), senha com
     `password_hash`; sessão por **cookie httpOnly** (SameSite=Lax; `Secure` só em
     HTTPS — HTTP puro/ngrok continua funcionando).
   - **Entregas de arquivos** dos alunos (`entrega`/`minhas`/`entregas`/`dlent`):
     txt/doc/docx/pdf/odt ≤ 12 MB, gravadas em `aulaviva/entregas/<disc>/<code>/`,
     download no painel somente com token (sem URL pública).
   - Rotas v1 **mantidas** com mesmos nomes/campos: `get`, `put` (`{nome,turma,payload}`),
     `lista&token=`, `arq`, `arqup`.
   - Credenciais **só por ambiente** (`LOJA_DB_PASS`/`AULAVIVA_PROF_TOKEN`), padrão v1;
     erros de BD → `error_log` + mensagem genérica; caminhos via `__DIR__`.
   - Novo: `aulaviva/migracao_contas_entregas.sql` (4 tabelas no banco `loja_turma`
     que já existe; idempotente; migração do v1 opcional/comentada) e
     `aulaviva/LEIA-ME_MIGRACAO.md` (passo a passo do deploy).

2. **`apps-nuvem/AulaViva_pi1_index.html` + `AulaViva_lp2_index.html`** (novos builds, mesmos nomes)
   - Login/cadastro com senha; ao reabrir o link, **volta direto onde parou** (retomada automática).
   - **Nome completo** no topo; botão **🏠 home**; **🎯 Ir para** (mapa de aulas).
   - **📤 Entregar** + **Minhas entregas** (arquivos p/ professora) e **📎 Materiais**.
   - **Fix do bug das alternativas vazias**: alternativas com tags HTML (ex.: `<head>`)
     sumiam; agora renderizam como texto (escape `rich()`, `<` do JSON como `\u003c`).
   - ADM (`/juh/i`) vê o botão **👩‍ Painel** → `Painel_Professor_{disc}.html`;
     aluno comum não vê painel nem material de professor.
   - API relativa `../aulaviva/api.php` (convenção v1 — funciona em ngrok/domínio/local).
   - **Zero localStorage** na versão nuvem; Modo Turma (641–900px) e mobile (640px) preservados.

3. **`apps-nuvem/Painel_Professor_pi1.html` + `Painel_Professor_lp2.html`** (novos builds)
   - Turma inteira com pontos/aulas/exercícios/chefes; **detalhe por aluno com o
     histórico completo de respostas** (checkpoints + chefes); **CSV** inclui o histórico.
   - Envio de **materiais** p/ a turma; listagem e **download das entregas** dos alunos.
   - Gate duplo: nome ADM (`/juh/i`) + token; sem token válido → 403 na API.

4. **`apps-offline/AulaViva_PI-I_offline.html` + `AulaViva_LP2_offline.html`** (novos builds)
   - Mesmas correções da nuvem (alternativas, home, mapa, retomada, nome completo)
     para o pendrive da escola + **fix da chave localStorage por disciplina**
     (antes PI-I e LP2 se sobrescreviam no mesmo navegador).
   - Offline usa localStorage por definição (a regra "nada de localStorage" é da nuvem).

5. **Paginador dos módulos** (mesmos 4 HTML de apps, novo build — commit separado)
   - Barra no topo de **toda página** do módulo: `Página X de Y`, **⏮ Início**,
     **◀ Voltar**, campo para **digitar a página** + **Ir** (Enter também vai),
     **Próximo ▶** e **⏭ Fim** — além do rótulo do que é a página atual
     ("carta 3 · Aula 12", "checkpoint · Aula 5 (2/3)", "chefe · pergunta 1"…).
   - **Total de páginas** nos cards da trilha ("… · N páginas") e no mapa 🎯
     (cabeçalho "página X de Y" + atalhos ⏮ Início e ⏭ Fim).
   - Setas do teclado não viram página enquanto o cursor está num campo.
   - Só front-end dos apps: nada de API, banco, painéis ou nomes de arquivo.
     (PI-I: 12 módulos, 733 páginas no total, maior módulo com 109; LP2: 15
     módulos, 366 páginas. Fórmula do total conferida módulo a módulo contra o
     fluxo real do app — 0 divergências.)

6. **Materiais exclusivos da professora somem para o aluno** (pedido novo)
   - A partir do momento em que o usuário coloca o nome (login), os itens
     **"Painel do Professor", "Guia da Professora" e "Apostila do Professor"**
     desaparecem da lista 📎 Materiais da turma — para qualquer conta que não
     seja ADM ("Juh").
   - **Filtro duplo**: no servidor (rota `arq` do `api.php` lê o nome da sessão
     pelo cookie e oculta arquivos com "professor"/"painel" no nome para
     não-ADM — sem sessão, também oculta) e no cliente dos 4 apps (função
     `visivelMaterial()`, para a UI nunca chegar a mostrar os nomes).
   - Regra de nome: basta o arquivo conter "professor", "professora" ou
     "painel" no nome (ex.: `Guia_da_Professora.pdf`). Materiais para a turma
     (apostila do aluno, listas, slides) continuam visíveis normalmente.
   - O mesmo filtro foi aplicado às edge functions do caminho alternativo
     Supabase (fora deste repo — `Kit_Sala_de_Aula_v2.zip`).
   - Nada de rota nova, campo novo ou mudança de banco: só o `case 'arq'` e o
     front dos apps.

7. **Porta de entrada: clicou no link, caiu no login** (pedido novo da professora)
   - `index.php` novo na raiz do kit: `/KiT_Sala_de_Aula/` faz **302** para o app da
     disciplina (`?d=lp2` leva à LP2; sem parâmetro, PI-I). O app, sem sessão,
     **abre já com o modal 👤 nome + senha** ("Já tenho conta" / "Criar conta").
   - Acolhida na primeira vez: se o login falhar, aparece o botão
     **"🆕 É minha primeira vez — criar conta"**, que troca de aba **sem perder o
     nome digitado** (`preNome`/`preTurma`); "trocar de conta" limpa a memória.
   - Sem credenciais novas, sem localStorage, sem rota nova: só um redirect e o
     rebuild dos 4 apps a partir do BASE.

8. **Túnel público sem tela de aviso** (cloudflared, pedido novo)
   - O ngrok grátis interpõe a tela "Visit Site" antes do Kit (e a pré-visualização
     do link no WhatsApp mostrava a propaganda do ngrok). `redserver/tunel/` traz
     `sobe-tunel.sh` (quick tunnel p/ :8080, imprime e salva o link em
     `/root/url-tunel.txt`), `tunel-cloudflared.service` (systemd, túnel
     permanente) e `LEIA-ME_TUNEL.md` com passo a passo + teste de aceite.
   - `DEPLOY_NOTES.md` ganha a seção do túnel novo. Link do quick tunnel muda a
     cada subida (como o ngrok mutável atual); o LEIA-ME documenta o opcional
     túnel nomeado para link fixo.

9. **Mídia de sala de aula: videoaula, áudio opcional e resolução dos exercícios**
   *(embarcada no rebuild dos 4 apps do commit 7; `videoaulas/LEIA-ME_MEDIA.md` no commit 8)*
   - **🎬 Videoaula na tela inicial**: cartão dourado na trilha (ao lado dos
     módulos) com o nome da disciplina ("Videoaula — Programação para Internet I"
     / "… Linguagem de Programação II"); abre o mp4 da pasta irmã `videoaulas/`
     num player interno (pausar, voltar, reassistir). Pedido da professora.
   - **🔊 Áudio opcional por módulo**: botão "Ouvir o resumo deste módulo
     (opcional)" na abertura de cada módulo. O botão **só existe se o arquivo
     `videoaulas/audio/<disc>_mNN.mp3` existir no build** — nenhum botão órfão.
     Quem prefere ler simplesmente não clica (escolha do aluno, sem imposição).
   - **👀 Resolução passo a passo nos exercícios**: aviso "sem laboratório hoje?"
     e, em cada exercício, botão que abre bloco visual com pseudocódigo/código/
     árvore de pastas/passo a passo + **gabarito** (resposta esperada). O Módulo 1
     da LP2 já vem completo (média no papel, ola.vbp/Form_Load, botões par/ímpar e
     tabuada) — é a demonstração projetada para o dia sem laboratório.
   - **`videoaulas/LEIA-ME_MEDIA.md`**: contrato da pasta de mídia (nomes, como
     publicar no servidor, como o offline acha os arquivos, regras de manutenção).
     Os binários (.mp4/.mp3) **não** entram no git: viajam nos kits zip e no scp.
   - `DEPLOY_NOTES.md`: seção de mídia (scp da pasta) + **hotfix imediato** do
     título v1 do app LP2 em produção (mostrava "Programação para Internet I").
   - Só front-end dos 4 apps + conteúdo LP2 (campo `resolucao`): nenhuma rota,
     campo de banco ou credencial novos; zero localStorage na nuvem; Modo Turma
     e 640px preservados.

## Compatibilidade / impacto

- `put` agora **exige sessão** (401 sem cookie): aluno com aba do v1 aberta recarrega
  a página uma vez e cai no login/cadastro. Progresso v1: migração opcional documentada
  no SQL (conta nova começa do zero; histórico antigo permanece consultável no banco).
- `arq` continua pública, mas a **lista** vem filtrada para não-ADM. Obs.: a URL
  direta de um arquivo em `materiais/` continua acessível para quem souber o nome
  exato (servido estático pelo nginx) — se quiser bloqueio total, Rapha pode
  adicionar um `location ~ ^/Kit_Sala_de_Aula/aulaviva/materiais/ { deny all; }`
  no vhost e servir os arquivos por uma rota autenticada depois (opcional,
  fora do escopo deste PR).
- Nenhum caminho/rota renomeado; `index.html` do kit não precisa mudar (sem páginas novas).
- `projeto-loja/`, `apostilas/`, `slides/`, `supabase/` (legado): **intocados**.

## Deploy (após o merge — quem aplica é Rapha/Hermes)

> **Merge ≠ deploy.** Mergear este PR atualiza apenas o repositório; o que a turma
> acessa só muda depois dos passos abaixo (SQL + pastas + env + scp dos HTML/`index.php`
> + pasta `videoaulas/`). Checklist imprimível de 1 página:
> `extras/Checklist_Deploy_PR_AulaViva_v2.pdf`.

1. `mysql -u root -p loja_turma < aulaviva/migracao_contas_entregas.sql`
2. Substituir `aulaviva/api.php` e criar `aulaviva/materiais/{pi1,lp2}` +
   `aulaviva/entregas/{pi1,lp2}` com `chown www-data`.
3. php-fpm (pool do vhost): `env[LOJA_DB_PASS]` + `env[AULAVIVA_PROF_TOKEN]`
   **novo** (rotacionar o antigo — circulou em docs).
4. Enviar os 4 HTML de `apps-nuvem/` e os 2 de `apps-offline/`.
5. Copiar a pasta `videoaulas/` (mp4 + pdfs + áudios que existirem) para a raiz do
   kit — `../videoaulas/` relativo aos apps; detalhes em `videoaulas/LEIA-ME_MEDIA.md`.
6. Detalhes: `aulaviva/LEIA-ME_MIGRACAO.md`.

## Checklist de teste (via ngrok, como de costume)

- [ ] `reg` cria conta → cookie httpOnly setado → `get` devolve nome/turma/payload
- [ ] `login` com senha errada → 401 genérico; nome duplicado no `reg` → 409
- [ ] `put` sem cookie → 401; com cookie → round-trip ok
- [ ] Alternativas com `<head>`/`<body>` aparecem como texto (não somem)
- [ ] LP2: conta criada na LP2 **não** aparece no painel da PI-I (disc separado)
- [ ] 📤 entrega txt/pdf ≤ 12 MB → aparece no painel → download via `dlent` ok;
      `.exe`/`.zip` → recusado com aviso
- [ ] `lista`/`entregas` com token errado → 403; ADM "Juh" vê botão Painel; aluno não vê
- [ ] Retomada: fechar e reabrir o link → volta na mesma posição
- [ ] Paginador: "Página X de Y" confere com o mapa 🎯; ⏮/◀/▶/⏭ funcionam;
      digitar nº + Ir (e Enter) salta certo; setas do teclado não interferem
      enquanto digita no campo; cards da trilha mostram "N páginas"
- [ ] Materiais: professora (ADM) envia pelo painel um arquivo com "Professor"
      no nome → na conta dela aparece; na conta de um aluno **não aparece**
      (nem chamando `api.php?disc=pi1&a=arq` direto com o cookie do aluno)
- [ ] Celular 640px e Modo Turma 641–900px sem quebra de layout (paginador incluso)
- [ ] Resíduos `qa_*` apagados do banco após o teste

## Enquanto a v2 não é mergeada (produção ainda na v1)

O bug das alternativas com tags HTML (checkpoint da Aula 6: botões vazios, página
"engolida" pelo `<title>`) **existe na v1 que está no ar**. O pacote
`Hotfix_v1_tags_HTML.zip` (pasta `output/`) corrige **somente a v1**, com a mesma
função `rich()` que a v2 já usa: 4 arquivos substitutos + patch que aplica limpo
em `master` (branch sugerida `feature/rapida-fix-tags-html`, deploy por scp+md5
como de costume). Depois que a v2 for deployada, o hotfix deixa de ser necessário.

## Regras do repositório (checklist do agente)

- [x] Sintaxe verificada (JS dos 6 HTML: `node --check`; filtro do app testado em
      node com DOM stub; PHP revisado + testes de rota simulados — `php -l`
      indisponível no ambiente do agente)
- [x] Nenhum `localStorage` adicionado nas versões de nuvem
- [x] Nenhum caminho/arquivo renomeado
- [x] Nenhuma credencial/token novo no código (só `getenv` + fallback de dev, padrão v1)
- [x] Commits explicando o quê / por quê / onde
- [x] Mudança mínima: só o que a tarefa pede (nada de refactor extra)
