-- Bucket público de materiais da turma (execute 1x no SQL Editor)
insert into storage.buckets (id, name, public)
values ('materiais', 'materiais', true)
on conflict (id) do nothing;

-- leitura pública (alunos baixam sem login):
drop policy if exists materiais_leitura_publica on storage.objects;
create policy materiais_leitura_publica
  on storage.objects for select
  using (bucket_id = 'materiais');

-- uploads/exclusões: SOMENTE pela Edge Function 'arquivos' (service role).
-- Nenhuma policy de insert para anon => ninguém mais consegue enviar.
