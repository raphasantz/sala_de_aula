# Deploy no redserver (regra de ouro do handover)

Fonte de verdade: **/root/_drop/kit_sala/** → scp → **/mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/**
Confira `md5sum` local × remoto antes de dar por pronto. Teste SEMPRE pela URL do ngrok.

## Arquivos desta pasta de manutenção
| Origem (aqui) | Destino no servidor |
|---|---|
| aulaviva/api.php | Kit_Sala_de_Aula/aulaviva/api.php |
| aulaviva/aulaviva_alunos.sql | executar 1× no MySQL (sudo mysql loja_turma) |
| apps-nuvem/AulaViva_PI-I_index.html | Kit_Sala_de_Aula/apps-nuvem/… |
| apps-nuvem/AulaViva_LP2_index.html | idem |
| apps-nuvem/Painel_Professor_PI-I.html | idem |
| apps-nuvem/Painel_Professor_LP2.html | idem |

## Comandos modelo
    # USUARIO@SERVIDOR = usuário e IP do documento de handover (não versionar aqui)
    scp aulaviva/api.php USUARIO@SERVIDOR:/tmp/
    ssh USUARIO@SERVIDOR 'sudo cp /tmp/api.php /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/aulaviva/api.php && sudo chown www-data:www-data /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/aulaviva/api.php'
    md5sum aulaviva/api.php   # e compare com o remoto

## Antes do primeiro uso
1. Rode `aulaviva_alunos.sql` no MySQL (tabela aulaviva_alunos);
2. Crie `aulaviva/materiais/pi1/` e `aulaviva/materiais/lp2/` (chown www-data);
3. Defina no php-fpm (pool do vhost pcs-replica):
   `env[LOJA_DB_PASS] = <senha do loja_app>` e `env[AULAVIVA_PROF_TOKEN] = <token novo>`;
4. **ROTACIONE** a senha antiga e o token antigo (o doc de handover circulou com eles em claro).

## Deploy do v2 (após o merge do PR) — o git NÃO faz isso sozinho
Mergear o PR atualiza só o repositório; o ar muda com os passos abaixo.
Checklist imprimível de 1 página: `extras/Checklist_Deploy_PR_AulaViva_v2.pdf`.

| Origem (repo, após o merge) | Destino no servidor | Obs. |
|---|---|---|
| `aulaviva/migracao_contas_entregas.sql` | `mysql -u root -p loja_turma < …` | 1×, idempotente |
| `aulaviva/api.php` | `Kit_Sala_de_Aula/aulaviva/api.php` | scp + md5, chown www-data |
| `index.php` (raiz do kit) | `Kit_Sala_de_Aula/index.php` | porta de entrada: 302 p/ o app (`?d=lp2`) |
| `apps-nuvem/AulaViva_{pi1,lp2}_index.html` | `Kit_Sala_de_Aula/apps-nuvem/…` | login/senha, retomada, paginador, mídia |
| `apps-nuvem/Painel_Professor_{pi1,lp2}.html` | idem | histórico + entregas + materiais |
| `apps-offline/AulaViva_{PI-I,LP2}_offline.html` | pendrive da escola | não vai pro servidor |
| `videoaulas/` (pasta inteira) | `Kit_Sala_de_Aula/videoaulas/` | binário só por scp, nunca no git |

Depois: `mkdir -p aulaviva/materiais/{pi1,lp2} aulaviva/entregas/{pi1,lp2}` +
`chown -R www-data:www-data`, `env[AULAVIVA_PROF_TOKEN]` **novo** no pool php-fpm,
restart do php-fpm, teste pela URL do túnel e limpeza dos resíduos `qa_*`.
nginx: nada muda (cookie usa `Secure` automaticamente em HTTPS).

## Regras que eu (manutenção) respeito
- Nada de localStorage nos apps (shim de memória injetado);
- Erros de banco → error_log, mensagem genérica pro browser;
- Pedido de loja: transação + SELECT … FOR UPDATE (não reverter);
- Não tocar em outros vhosts (8081/8082, mesanerd, calistenia, siad…);
- Resíduos de teste (linhas qa_*) sempre apagados após QA.

## Túnel público sem tela de aviso (cloudflared) — novo
O ngrok grátis interpõe a tela "Visit Site" antes do Kit; o **cloudflared quick
tunnel** não. Arquivos em `redserver/tunel/` (passo a passo no LEIA-ME_TUNEL.md):
- `sobe-tunel.sh` — sobe túnel avulso p/ :8080 e imprime/salva o link (/root/url-tunel.txt);
- `tunel-cloudflared.service` — unidade systemd p/ túnel permanente (enable --now).
Links dos alunos após subir o túnel:
- PI-I: `<url-tunel>/KiT_Sala_de_Aula/`
- LP2:  `<url-tunel>/KiT_Sala_de_Aula/?d=lp2`
A raiz `Kit_Sala_de_Aula/index.php` (commit 7 do PR v2) faz o 302 para o app da
disciplina, que abre já pedindo nome + senha. Parar o ngrok só após teste no 4G.

## Mídia da turma (pasta videoaulas/) — novo
Os apps v2 exibem na trilha o cartão `🎬 Videoaula` e, na abertura dos módulos, o botão
opcional `🔊 Ouvir o resumo deste módulo`. A mídia mora em `videoaulas/`, IRMÃ de
`apps-nuvem/` (caminho relativo `../videoaulas/`):
```
scp -r videoaulas/ USUARIO@SERVIDOR:/tmp/
ssh USUARIO@SERVIDOR 'sudo cp -r /tmp/videoaulas /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/ && sudo chown -R www-data:www-data /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/videoaulas'
```
Conteúdo: Videoaula_Programacao_para_Internet_I.mp4, Videoaula_Linguagem_de_Programacao_II.mp4,
Passo_a_Passo_*.pdf e audio/{pi1,lp2}_mNN.mp3 (opcionais — o botão só aparece se existir).
Sem a pasta, o app funciona normalmente e o cartão avisa com mensagem amigável.

## Hotfix imediato em produção v1 (enquanto o PR não é mergeado)
O app v1 de LP2 em produção exibe o título errado ("Programação para Internet I"):
```
sudo sed -i 's/Programação para Internet I/Linguagem de Programação II/g' \
  /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/apps-nuvem/AulaViva_lp2_index.html
```
(aplique SOMENTE no arquivo lp2; o pi1 já tem o título certo. O PR v2 resolve de vez.)
