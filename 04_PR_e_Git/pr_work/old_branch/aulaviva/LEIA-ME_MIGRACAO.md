# Migração p/ o AulaViva v2 (contas, entregas, histórico) — 5 passos

Arquivos desta pasta: `api.php` (novo), `migracao_contas_entregas.sql`,
`aulaviva_alunos.sql` (v1, mantido só p/ referência).

1. **Banco (rodar 1×, idempotente):**
   `mysql -u root -p loja_turma < migracao_contas_entregas.sql`
   Cria `aulaviva_contas/progresso/arquivos/entregas` no banco que já
   existe (`loja_turma`) — o usuário `loja_app` já tem acesso.
   A migração do v1 (`aulaviva_alunos`) é OPCIONAL e está comentada no
   final do SQL (o histórico antigo fica amarrado ao code velho; conta
   nova de aluno começa do zero).

2. **Pastas** (aqui dentro de `aulaviva/`):
   `mkdir -p materiais/pi1 materiais/lp2 entregas/pi1 entregas/lp2`
   `chown -R www-data:www-data materiais entregas`

3. **Credenciais por ambiente** (pool php-fpm do vhost — padrão do v1):
   `env[LOJA_DB_PASS] = <senha do loja_app>`
   `env[AULAVIVA_PROF_TOKEN] = <token NOVO>`  ← rotacione o antigo!
   (fallbacks no topo do api.php são só p/ dev; não coloque senha real no código)

4. **nginx:** nada muda. O cookie de sessão usa `Secure` automaticamente
   quando a requisição chega via HTTPS (ngrok conta); em HTTP puro funciona.

5. **Testar (via ngrok):** cadastro (reg) → login → get/put round-trip;
   📤 entrega de arquivo → aparece no painel → download via dlent;
   material (arqup) → aparece no 📎 do aluno; `lista` com token errado → 403;
   apagar resíduos `qa_*` do banco depois do teste.

**Aviso aos alunos:** quem estiver com a aba do AulaViva v1 aberta precisa
recarregar a página uma vez (o `put` do v2 exige login/sessão).
