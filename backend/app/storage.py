"""Storage layer: saves messages to local Supabase (Postgres). Failures never break the chat."""
import logging
import os

import psycopg

log = logging.getLogger("uvicorn.error")

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
        log.warning("[storage] not saved: %s", err)
        return False


def db_ok() -> bool:
    """True when the database answers. Used by /api/health."""
    try:
        with psycopg.connect(DB_URL, connect_timeout=2) as conn:
            conn.execute("select 1")
        return True
    except psycopg.Error:
        return False
