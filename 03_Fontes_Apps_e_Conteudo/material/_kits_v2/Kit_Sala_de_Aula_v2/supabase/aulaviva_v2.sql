-- AulaViva v2 · Supabase (rodar UMA vez no SQL Editor)
create table if not exists aulaviva_contas (
  id bigserial primary key,
  disc text not null check (disc in ('pi1','lp2')),
  code text not null,
  nome text not null,
  nome_lc text not null,
  turma text default '',
  salt text not null,
  senha_hash text not null,
  adm int default 0,
  created_at timestamptz default now(),
  unique (disc, code),
  unique (disc, nome_lc)
);
create table if not exists aulaviva_progresso (
  disc text not null check (disc in ('pi1','lp2')),
  code text not null,
  nome text default '',
  turma text default '',
  payload jsonb default '{}',
  updated_at timestamptz default now(),
  primary key (disc, code)
);
create table if not exists aulaviva_arquivos (
  disc text not null check (disc in ('pi1','lp2')),
  nome text not null,
  tipo text default '',
  tamanho bigint default 0,
  updated_at timestamptz default now(),
  primary key (disc, nome)
);
create table if not exists aulaviva_entregas (
  id bigserial primary key,
  disc text not null check (disc in ('pi1','lp2')),
  code text not null,
  aluno text default '',
  nome text not null,
  caminho text not null,
  tamanho bigint default 0,
  created_at timestamptz default now()
);
create index if not exists ix_ent_code on aulaviva_entregas (disc, code);

-- Buckets
insert into storage.buckets (id, name, public) values ('materiais','materiais', true)
  on conflict (id) do nothing;
insert into storage.buckets (id, name, public) values ('entregas','entregas', false)
  on conflict (id) do nothing;

-- Materiais: leitura pública, escrita só pela função (service role)
drop policy if exists "materiais leitura publica" on storage.objects;
create policy "materiais leitura publica" on storage.objects
  for select using (bucket_id = 'materiais');
-- Entregas: bucket privado — só a função (service role) lê/escreve.

-- RLS: tabelas fechadas (só a edge function, com service role, acessa)
alter table aulaviva_contas     enable row level security;
alter table aulaviva_progresso  enable row level security;
alter table aulaviva_arquivos   enable row level security;
alter table aulaviva_entregas   enable row level security;

-- Migração v1 → v2 (se a tabela aulaviva_alunos existir):
-- insert into aulaviva_progresso (disc, code, nome, turma, payload)
--   select disc, code, nome, turma, coalesce(payload::jsonb,'{}') from aulaviva_alunos
--   on conflict (disc, code) do nothing;
