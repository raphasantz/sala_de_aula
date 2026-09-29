# Manutenção Redserver v2 — AulaViva com contas, entregas e respostas

## O que muda no servidor
1. **Banco**: rode `aulaviva_v2.sql` (cria `loja_aulaviva` com contas/progresso/
   materiais/entregas). Se já existia a tabela antiga `aulaviva_alunos`, rode o
   INSERT de migração comentado no final do SQL.
2. **API**: substitua `apps-nuvem/api.php` pelo `api_v2.php` (renomeie para `api.php`).
   Edite no topo: `DB_PASS` (senha do `loja_app`) e `PROF_TOKEN` (novo token!).
3. **Pastas**: crie `apps-nuvem/materiais/{pi1,lp2}` e `apps-nuvem/entregas/{pi1,lp2}`
   com permissão de escrita pelo usuário do nginx/php (ex.: `chown -R www-data`).
4. **nginx**: nada muda (api.php já é atendido). Confirme HTTPS ativo (cookies `secure`).
5. **Apps/painel**: envie os 4 HTML para `apps-nuvem/` (ou onde estão hospedados).

## Regras de acesso
- Aluno: cria conta com **nome único + senha**; cookie httpOnly mantém a sessão;
  ao reabrir o link, **volta direto onde parou**.
- ADM (“Juh”): vê o botão **Painel** no app; o painel ainda exige o token.
- USUÁRIO: não vê painel; guia/apostila do professor **não estão no kit do aluno**.
- Entregas: botão **📤 Entregar** (txt/doc/docx/pdf/odt, até 12 MB) →
  ficam em `entregas/<disc>/<code>/` e listadas no painel.
- Todas as respostas (checkpoint + chefe) ficam no payload (`hist`) → painel
  mostra por aluno e o CSV exporta o histórico completo.

## Segurança (não pule!)
- Troque `DB_PASS` e `PROF_TOKEN` por valores novos (os antigos circularam em docs).
- Senhas de alunos: `password_hash` (bcrypt) — nunca em texto puro.
- Erros de BD vão para `error_log`; navegador recebe mensagem genérica.
