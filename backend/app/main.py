"""FastAPI app: wires state, inference and storage together and streams over SSE."""
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI  # noqa: E402
from sse_starlette.sse import EventSourceResponse  # noqa: E402

from . import state, storage  # noqa: E402
from .inference import llm_mode, stream_answer  # noqa: E402

app = FastAPI(title="CSE 642 skeleton")


@app.get("/api/health")
def health() -> dict:
    return {"ok": True, "db": storage.db_ok(), "llm": llm_mode()}


@app.get("/api/chat")
async def chat(session_id: str, prompt: str):
    state.add(session_id, "user", prompt)
    storage.save_message(session_id, "user", prompt)

    async def events():
        answer = ""
        async for piece in stream_answer(state.history(session_id)):
            answer += piece
            yield {"event": "token", "data": piece}
        state.add(session_id, "assistant", answer)
        storage.save_message(session_id, "assistant", answer)
        yield {"event": "done", "data": ""}

    return EventSourceResponse(events())
