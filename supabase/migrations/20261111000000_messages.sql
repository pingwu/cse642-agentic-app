-- Storage layer: one row per message in a chat session.
create table if not exists public.messages (
  id bigint generated always as identity primary key,
  session_id text not null,
  role text not null check (role in ('user', 'assistant')),
  content text not null,
  created_at timestamptz not null default now()
);
create index if not exists messages_session_idx on public.messages (session_id, id);
