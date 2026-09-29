# Kit Sala de Aula v2 — Nuvem (Supabase)

## Novidades desta versão
- **Login por aluno**: nome completo + senha criada pelo aluno. Nome **não pode duplicar**.
- **Retomada automática**: ao reabrir o link, o aluno cai **direto onde parou**.
- **Nome completo** no topo; **🗺 Trilha** e o título levam à tela inicial.
- **📤 Entregar**: aluno anexa txt/doc/docx/pdf/odt (fica ligado ao nome dele).
- **Histórico de respostas**: cada resposta (checkpoint e chefe) fica gravada p/ correção.
- **Perfis**: ADM = conta com nome “Juh” (vê o botão 👩‍ Painel); USUÁRIO = aluno normal
  (não vê painel; guia/apostila do professor não estão no kit do aluno). Em 📎 Materiais,
  itens com “professor”/“painel” no nome só aparecem para o ADM (a edge function filtra).
- **Bug corrigido**: alternativas com tags HTML (`<head>` etc.) agora aparecem como texto.

## Instalação (10 min)
1. **SQL**: Supabase → SQL Editor → rode o conteúdo de `supabase/aulaviva_v2.sql`.
2. **Funções** (substituem sync/arquivos antigos):
   - Edge Functions → **Add new function** → nome `avpi1` → cole `functions/avpi1/index.ts` → Deploy.
   - Repita com nome `avlp2` → cole `functions/avlp2/index.ts` → Deploy.
   - Em cada função: Settings → Environment Variables →
     `SUPABASE_URL` = URL do projeto; `SUPABASE_SERVICE_ROLE_KEY` = **secret** key
     (Settings → API Keys → secret); `PROF_TOKEN` = token do painel (crie um novo!).
   - **Verify JWT: DESLIGADO** nas duas.
   - (Opcional) apague as funções antigas `sync`, `sync-lp2`, `arquivos`, `arquivos-lp2`.
3. **Hospede** os 4 arquivos HTML (apps + painéis) no mesmo lugar de antes
   (GitHub Pages / Netlify / pasta do servidor).
4. Teste: abra o app → Criar conta → jogue → feche e reabra (deve voltar onde parou) →
   Painel: nome “Juh” + token.

## Arquivos
| Arquivo | O que é |
|---|---|
| `AulaViva_..._I.html` / `..._II.html` | apps dos alunos (nuvem, com login) |
| `prof_pi1.html` / `prof_lp2.html` | painel da professora (token + nome Juh) |
| `functions/avpi1/index.ts`, `functions/avlp2/index.ts` | edge functions unificadas |
| `supabase/aulaviva_v2.sql` | tabelas + buckets + políticas |
