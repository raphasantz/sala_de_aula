# AulaViva Programação para Internet I — SOMENTE Supabase (sem Vercel, sem GitHub)

## 1) Criar a atendente (Edge Function) — 3 minutos
1. No painel do Supabase, menu esquerdo: **Edge Functions**;
2. Clique em **New function**;
3. **Name**: `sync`  (se já existir uma com esse nome, abra-a para editar);
4. Apague todo o código que aparecer no editor e **cole o conteúdo de `edge-sync.ts`**;
5. **Antes do Deploy**: na linha `const PROF_TOKEN = "...`, troque pelo token que você inventar
   (ex.: `prof-raquel-2026`) — ele é a senha do seu painel;
6. Clique em **Deploy** e espere o selo ficar verde.

Pronto: sua API está viva em
`https://fzpipqrgnjupyfugztjo.supabase.co/functions/v1/sync`

## 2) Usar o app — zero instalação
- **Duplo clique no `index.html`** deste kit (ou envie o arquivo aos alunos pelo
  Classroom/Drive/WhatsApp — funciona até offline);
- O selo ☁️ no topo mostra: conectado / salvo / offline;
- Trocou de aparelho? Com o local vazio, o app baixa o save da nuvem sozinho.

## 3) Painel da turma
- Abra **`prof.html`** (duplo clique), digite o PROF_TOKEN e veja a tabela + CSV.

## 4) Se o selo ficar ☁️ offline
- Confira se a função `sync` está **Deployed** (Edge Functions);
- Confira se o `schema.sql` foi executado no SQL Editor (tabela `progresso`);
- Abra `https://fzpipqrgnjupyfugztjo.supabase.co/functions/v1/sync?aluno=teste` no navegador:
  deve aparecer `{}`  (chaves vazias) — se aparecer erro, me mande o texto dele.

## 📎 Materiais da turma (anexos para os alunos)
1. **SQL Editor** do Supabase: execute `storage_materiais.sql` (uma única vez);
2. **Edge Functions → New function** → nome: `arquivos` → cole o conteúdo de `arquivos.ts` → Deploy;
3. No **Painel do Professor** (`prof.html`): digite o PROF_TOKEN, escolha o arquivo e **Enviar**;
4. Os alunos verão o botão **📎 Materiais** no topo do AulaViva para baixar.
   (Downloads são públicos; uploads exigem o PROF_TOKEN — só você envia.)
