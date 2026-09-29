-- AulaViva Cloud — tabela de progresso (usada pelos dois projetos: pi1 e lp2)
-- Execute UMA vez no SQL Editor do seu projeto Supabase.
create table if not exists public.progresso (
  id         bigint generated always as identity primary key,
  disc       text not null,               -- 'pi1' | 'lp2'
  code       text not null,               -- código anônimo do aparelho/aluno
  nome       text default '',
  turma      text default '',
  payload    jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now(),
  unique (disc, code)
);

alter table public.progresso enable row level security;
-- Sem políticas públicas: somente a API (service key) lê/grava.
-- O painel do professor usa a mesma API com PROF_TOKEN.

comment on table public.progresso is
  'Progresso do AulaViva por aluno (code) e disciplina (disc).';

-- Índice para o painel da turma (ordena por atualização)
create index if not exists idx_progresso_disc_at
  on public.progresso (disc, updated_at desc);
