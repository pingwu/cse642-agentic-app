import os

os.environ.pop("OPENROUTER_API_KEY", None)

from fastapi.testclient import TestClient  # noqa: E402

from app import state, storage  # noqa: E402
from app.main import app  # noqa: E402

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"ok": True}


def test_streams_tokens_then_done(monkeypatch):
    monkeypatch.setattr(storage, "save_message", lambda *a: True)
    state.clear()
    with client.stream("GET", "/api/chat/stream", params={"prompt": "hi"}) as r:
        body = "".join(r.iter_text())
    assert body.count("event: token") > 3
    assert "event: done" in body
    assert [m["role"] for m in state.history("demo")] == ["user", "assistant"]
