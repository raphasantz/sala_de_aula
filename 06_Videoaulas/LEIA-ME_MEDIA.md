# Pasta `videoaulas/` — mídia da turma (vídeos e áudios)

Esta pasta fica **ao lado** dos apps (irmã de `apps-nuvem/` e `apps-offline/`).
Os apps chamam a mídia por caminho relativo: `../videoaulas/...`.

## O que mora aqui

| arquivo | o que é |
|---|---|
| `Videoaula_Programacao_para_Internet_I.mp4` | vídeo-aula PI-I (Loja Tech da Turma, ~13 min) |
| `Videoaula_Linguagem_de_Programacao_II.mp4` | vídeo-aula LP2 (VB6 na prática, ~11 min) |
| `Passo_a_Passo_Videoaula_PI-I_Loja_Tech.pdf` | folha de papel companheira do vídeo PI-I |
| `Passo_a_Passo_Videoaula_LP2_VB6.pdf` | folha de papel companheira do vídeo LP2 |
| `audio/pi1_mNN.mp3` | (opcional) narração do módulo NN de PI-I |
| `audio/lp2_mNN.mp3` | (opcional) narração do módulo NN de LP2 |

## Como aparece no app

- **Tela inicial (trilha):** cartão dourado `🎬 Videoaula — <disciplina>` abre o vídeo
  num player dentro do próprio app (pausar, voltar, reassistir).
- **Abertura de cada módulo:** botão verde `🔊 Ouvir o resumo deste módulo (opcional)`.
  O botão **só aparece se o arquivo de áudio existir** nesta pasta no momento do build —
  aluno nunca vê botão que leva a lugar nenhum. Quem não quer ouvir, simplesmente não clica.

## Publicar no servidor (redserver)

1. Copie a pasta `videoaulas/` inteira para a raiz do kit:
   `/mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/videoaulas/`
2. Pronto: os apps em `apps-nuvem/` já apontam para `../videoaulas/`.
3. Teste pelo link público: abra o app → clique no cartão da videoaula → o vídeo toca.
   Se aparecer a mensagem "arquivo não encontrado", é porque a pasta não subiu inteira.

## No kit offline (pen drive / computador sem internet)

A mesma estrutura vale: `Kit_Sala_de_Aula/apps-offline/` + `Kit_Sala_de_Aula/videoaulas/`.
Abrindo o html offline com a pasta do lado, o cartão e os áudios funcionam igual.
Se o html for copiado sozinho (sem a pasta), o app abre normalmente e o cartão avisa
com carinho que o vídeo não está por perto.

## Regras de manutenção

- **Não renomeie** os arquivos: os nomes entram no build dos apps.
- Vídeo novo de outra disciplina: `Videoaula_<slug>.mp4` (slug igual ao do conteúdo).
- Áudio novo de módulo: `audio/<pi1|lp2>_m<NN>.mp3` (NN com dois dígitos: m01, m02…)
  e depois rode o build de novo (`build_aula_app.py`) para o botão aparecer.
- Os `.mp4` e `.mp3` **não vão para o repositório git** (peso); vão nos kits zip e no
  servidor. No git entra só este LEIA-ME.
