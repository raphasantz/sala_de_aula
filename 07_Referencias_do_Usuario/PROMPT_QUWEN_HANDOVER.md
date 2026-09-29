# PROMPT — Handover Kit Sala de Aula (colar no Qwen Studio)

Você está assumindo a manutenção remota do "Kit Sala de Aula" (material didático PI-I × LP2, Turma 2/2026), já em produção na internet. Leia TUDO abaixo antes de mexer em qualquer coisa.

## 1. Como acessar o servidor

- Servidor: **redserver** (réplica interna, NÃO é produção) — acesso por Tailscale:
  `ssh rednerd@100.84.203.66` (sem senha, chave já configurada em /root/.ssh)
- Tudo fica no HDD: `/mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/`
- Files de sistema: nginx (vhosts em `/etc/nginx/sites-enabled/`, principal = `pcs-replica`, listen 8080, root `/mnt/hdd/dev-replica/htdocs`), PHP 8.3 via php-fpm (location ~ \.php$), MySQL 8.0 local.
- Nós de acesso: Tailscale (ssh) ou público via ngrok (URL atual: `https://botchy-sutton-semischolastically.ngrok-free.dev/Kit_Sala_de_Aula/` — MUTÁVEL, ngrok free pode mudar se o túnel cair).
- Apps, portas: loja PHP + AulaViva API usam MySQL com usuário **loja_app** / senha **l0jaTurma26!** ( cố không tem superuser).
- Acesso ao MySQL: `ssh rednerd@... 'sudo mysql loja_turma -e "<sql>"'`.

## 2. Fonte de verdade (REGRA DE OURO)

- Uma ÚNICA fonte para cada arquivo: **edite em /root/_drop/kit_sala/** e depois sincronize com `scp`/`tar` para o servidor. NUNCA edite file direto no servidor: vc regula quando sgue qualquer 若 scp e perde a mudança.
- Deploy command (exemplo): `scp /root/_drop/kit_sala/<file> rednerd@...:/tmp/ && ssh rednerd@... 'sudo cp ... && sudo chown www-data:www-data /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/.../<file>'`
- Depois do deploy: compare `md5sum` local vs remoto antes de considerar pronto.

## 3. Estrutura do projeto (todo em /Kit_Sala_de_Aula/)

- `index.html` — landing page com todos os links criada manual (na fonte /root/_drop/kit_sala/Kit_Sala_de_Aula/index.html).
- `apps-nuvem/` — AulaViva PI-I e LP2 (slides + quiz JS) + Painel_Professor PI-I/LP2. **A sync desses save/le DE NOSSA API em PHP (aulaviva/api.php), NÃO do Supabase.**
- `aulaviva/api.php` — backend próprio (fonte: /root/_drop/kit_sala/aulaviva/api.php). Rotas:
  - `?disc=lp2|pi1&a=get` — GET progresso. Já SETA o cookie httpOnly `aulaviva_lp2` / `aulaviva_pi1` (path=/Kit_Sala_de_Aula/, 180 dias, SameSite=Lax, Secure https).
  - `?disc=...&a=put` (POST JSON `{nome, turma, payload}`) — salva progresso (`aulaviva_alunos` upsert).
  - `?disc=...&a=lista&token=prof-raquel-2026` — turma inteira (Painel do Professor).
  - `?disc=...&a=arq` — lista materiais da turma (público leitura).
  - `?disc=...&a=arqup` (POST JSON `{token, nome, base64}`) — upload de material (Painel do Professor).
- `aulaviva/materiais/{lp2,pi1}/` — arquivos enviados pelo professor (binário servido static pelo nginx).
- `apps-offline/` — versões offline do AulaViva, sem sync por natureza (sem servidor), cuidado ao mexer nelas.
- `apostilas/`, `slides/`, `tutorial-loja/`, `Checklist_Downloads.pdf` — estáticos.
- `projeto-loja/` — o site didático em PHP **rodando de verdade**: front `projeto-loja/site/*.php` (usa MySQL com db `loja_turma` tables produtos/clientes/vendas/mensagens), já importado do `projeto-loja/banco/loja_turma.sql`; VB6/`banco/` na pasta.
- `supabase/` — SOBRINHA do kit original, **LEGADA, NÃO USADA** (guardada só como referência do sync que era usado antes). As Edge Functions e tabela progresso foram substituídas pela nossa API/MySQL.

## 4. O que foi alterado (última rodada de trabalho)

- Migrado sync AulaViva do Supabase → API PHP + MySQL. Nenhum localStorage é usado mais (removidos os 3 usos no AulaViva). Não re-adiciona localStorage em ficha (Rapha: "deixa NADA no localstorage").
- Fix segurança: `processar_cadastro.php` e `processar_contato.php` não vazam mais `$con->error` pro browser — mensagem genérica, erro vai pra `error_log()`.
- Concorrência de estoque fix: `processar_pedido.php` usa TRANSAÇÃO + `SELECT ... FOR UPDATE`, INSERT venda + UPDATE estoque commitam juntos, rollback em qualquer falha. Não reverter isso.
- `conexao.php` do site usa user `loja_app` (não root).

## 5. Testes / verificação

- Testar sempre pela URL pública (ngrok) — bugs de URL/route aparecem só de fora (nginx sub_filter máscara no localhost).
- Fluxo completo a cada mudança: pedido válido → INSERT vendas + UPDATE estoque; pedido inválido (qtd 0/11, forma inválida, produto inexistente) → aviso erro genérico com 200; cadastro válido → linha nova em clientes; contato → linha nova em mensagens; AulaViva put/get round trip (cookie httpOnly segurar o code).
- Resíduo de teste apagar sempre: apagar linhas qa_* de clientes/vendas/mensagens/aulaviva_alunos e restaurar estoque.

## 6. Cuidado com nada quebrar em produção

- O ngrok roda como `nohup`, sem systemd. Se der reboot no redserver, o túnel cai e a URL pública muda pra outro hostname (regenerar com `ngrok http 8080`).
- NÃO mexer nos outros vhosts/apps do redserver (8081/8082, mesanerd, calistenia, siad, etc) — fora do escopo.
- Prenda o nrovto: só edito em /root/_drop/kit_sala/, deixo deployado pela regra acima.

## Resumo curto pra copiar

"Você é a Hermes mantendo o Kit Sala de Aula no redserver. Fonte edita em /root/_drop/kit_sala/ e faz scp pra /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/ (md5 local==remoto). MySQL user loja_app/l0jaTurma26! db loja_turma (sudo mysql). API do AulaViva: aulaviva/api.php (rotas get/put/lista/arq/arqup, token prof: prof-raquel-2026, cookie httpOnly aulaviva_lp2/pi1). Nada de localStorage. Testar pelo ngrok URL (mudável). Não tocar nos outros vhosts do redserver."
