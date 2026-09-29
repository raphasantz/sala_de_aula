# Manutenção Redserver v2 — AulaViva com contas, entregas e respostas

Kit "drop-in" no repositório/servidor (mesmos caminhos de produção):

| Arquivo deste kit            | Destino em Kit_Sala_de_Aula/            |
|------------------------------|------------------------------------------|
| api_v2.php                   | aulaviva/api.php (SUBSTITUIR o conteúdo) |
| aulaviva_v2.sql              | rodar 1× no MySQL (banco `loja_turma`)   |
| AulaViva_pi1_index.html      | apps-nuvem/AulaViva_pi1_index.html       |
| AulaViva_lp2_index.html      | apps-nuvem/AulaViva_lp2_index.html       |
| Painel_Professor_pi1.html    | apps-nuvem/Painel_Professor_pi1.html     |
| Painel_Professor_lp2.html    | apps-nuvem/Painel_Professor_lp2.html     |

## O que muda no servidor
1. **Banco**: rode `aulaviva_v2.sql` (cria as tabelas `aulaviva_contas/progresso/
   arquivos/entregas` no banco `loja_turma`, que já existe). A migração opcional
   do v1 (`aulaviva_alunos`) está comentada no final do SQL.
2. **API**: substitua o conteúdo de `aulaviva/api.php` pelo `api_v2.php`.
   Credenciais por ambiente no pool php-fpm do vhost (padrão do v1):
   `env[LOJA_DB_PASS] = <senha do loja_app>` e
   `env[AULAVIVA_PROF_TOKEN] = <token NOVO>` (o antigo circulou em docs — rotacione).
3. **Pastas**: crie `aulaviva/materiais/{pi1,lp2}` e `aulaviva/entregas/{pi1,lp2}`
   com permissão de escrita pelo usuário do php (ex.: `chown -R www-data`).
4. **nginx**: nada muda. O cookie de sessão só usa `Secure` quando a requisição
   chega via HTTPS (ngrok conta como HTTPS) — em HTTP puro o login também funciona.
5. **Apps/painel**: os 4 HTML apontam para `../aulaviva/api.php` (URL relativa —
   funciona em qualquer domínio). Aluno com aba antiga aberta precisa recarregar.

## Regras de acesso
- Aluno: cria conta com **nome único + senha**; cookie httpOnly mantém a sessão;
  ao reabrir o link, **volta direto onde parou**.
- ADM (“Juh”): vê o botão **Painel** no app; o painel ainda exige o token.
- USUÁRIO: não vê painel; guia/apostila do professor **não estão no kit do aluno**;
  em 📎 Materiais, itens com “professor”/“painel” no nome **não aparecem** para aluno
  (filtro no app e também no servidor — rota `arq` do `api.php`).
- Entregas: botão **📤 Entregar** (txt/doc/docx/pdf/odt, até 12 MB) →
  ficam em `aulaviva/entregas/<disc>/<code>/` e listadas no painel.
- Todas as respostas (checkpoint + chefe) ficam no payload (`hist`) → painel
  mostra por aluno e o CSV exporta o histórico completo.

## Segurança (não pule!)
- Nenhuma senha/token no código: `getenv` com fallback de dev (como no v1).
- Senhas de alunos: `password_hash` (bcrypt) — nunca em texto puro.
- Erros de BD vão para `error_log`; navegador recebe mensagem genérica.
