"""State layer: what the app remembers about one conversation (in memory)."""
from collections import defaultdict

_history: dict[str, list[dict]] = defaultdict(list)


def add(session_id: str, role: str, content: str) -> None:
    _history[session_id].append({"role": role, "content": content})


def history(session_id: str) -> list[dict]:
    return list(_history[session_id])
