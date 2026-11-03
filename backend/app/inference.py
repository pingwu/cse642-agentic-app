"""Inference layer: talks to the model. Nothing else in the app does."""
import asyncio
import json
import os
from collections.abc import AsyncIterator

import httpx

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = os.getenv("MODEL", "openai/gpt-4o-mini")


async def stream_answer(messages: list[dict]) -> AsyncIterator[str]:
    """Yield the model's answer a few words at a time."""
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        # No key yet: stream a canned reply so the pipeline still works.
        reply = "No OPENROUTER_API_KEY is set, so this is a canned reply. Add your key to backend/.env to hear from a real model."
        for word in reply.split(" "):
            await asyncio.sleep(0.05)
            yield word + " "
        return
    payload = {"model": MODEL, "messages": messages, "stream": True}
    headers = {"Authorization": f"Bearer {key}"}
    async with httpx.AsyncClient(timeout=60) as client:
        async with client.stream("POST", OPENROUTER_URL, json=payload, headers=headers) as r:
            r.raise_for_status()
            async for line in r.aiter_lines():
                if not line.startswith("data: ") or line.endswith("[DONE]"):
                    continue
                delta = json.loads(line[6:])["choices"][0]["delta"].get("content")
                if delta:
                    yield delta
