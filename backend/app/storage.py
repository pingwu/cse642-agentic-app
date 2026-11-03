"""Storage layer: saves messages to local Supabase (Postgres). Failures never break the chat."""
import os

import psycopg

DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@127.0.0.1:54322/postgres")


def save_message(session_id: str, role: str, content: str) -> bool:
    try:
        with psycopg.connect(DB_URL, connect_timeout=2) as conn:
            conn.execute(
                "insert into public.messages (session_id, role, content) values (%s, %s, %s)",
                (session_id, role, content),
            )
        return True
    except psycopg.Error as err:
        print(f"[storage] not saved: {err}")
        return False
