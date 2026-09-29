# AulaViva Linguagem de Programação II na nuvem (Vercel + Supabase)

Projeto serverless que salva o progresso dos alunos do AulaViva Linguagem de Programação II no Supabase.
Funciona **online e offline**: sem internet, o app continua salvando no aparelho
(localStorage) e sincroniza quando a conexão volta.

## 1) Criar o banco (Supabase) — uma única vez
1. Crie um projeto em https://supabase.com (grátis).
2. Abra **SQL Editor** e execute o conteúdo de `supabase/schema.sql`.
3. Em **Settings → API**, copie:
   - `Project URL`  → variável `SUPABASE_URL`
   - `service_role key` (SEGREDO!) → variável `SUPABASE_SERVICE_KEY`

## 2) Publicar no Vercel
1. Suba esta pasta como um projeto no Vercel (drag-and-drop em https://vercel.com/new
   ou `vercel deploy` pela CLI).
2. Em **Project → Settings → Environment Variables**, crie:
   - `SUPABASE_URL` = URL do projeto Supabase
   - `SUPABASE_SERVICE_KEY` = service role key
   - `PROF_TOKEN` = uma senha sua para o painel do professor (ex.: gere uma frase longa)
3. Deploy. Ao abrir:
   - `/` → app do aluno (com o selo ☁️ no topo: salvo / offline / sincronizado);
   - `/prof.html` → painel da turma (pede o PROF_TOKEN, mostra tabela e exporta CSV).

## 3) Como o aluno usa
- Abre o link do Vercel no celular/PC → digita o nome (cadastro) → joga.
- O progresso sobe sozinho (≈1 s após cada salvamento) e volta em qualquer aparelho:
  no aparelho novo, com o local vazio, o app baixa o save da nuvem automaticamente.
- O código anônimo do aparelho fica no localStorage (`aulaviva_code_lp2`).

## 4) API (referência)
| Método | Rota | Uso |
|---|---|---|
| GET  | `/api/sync?aluno=CODE` | baixa o save do aluno |
| PUT  | `/api/sync?aluno=CODE` (corpo JSON) | salva/atualiza (upsert) |
| GET  | `/api/sync?lista=1&token=PROF_TOKEN` | lista da turma (painel) |

## 5) Segurança (resumo)
- RLS do Supabase **fechado**: só a `service_role` (usada pela API) acessa a tabela.
- A service key fica **somente** nas env vars do Vercel (nunca no HTML).
- O painel exige `PROF_TOKEN`; os dados dos alunos são anônimos (code + nome opcional).

## 6) Os dois projetos
Este repositório/projeto atende apenas a disciplina Linguagem de Programação II (`disc = 'lp2'`).
O projeto irmão da outra disciplina usa a MESMA tabela (coluna `disc` separa os saves)
— execute o schema.sql uma única vez no Supabase compartilhado.
