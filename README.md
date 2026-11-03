# CSE 642 starter app (tag `S03`)

The Session 3 skeleton for **CSE 642, Agentic AI and Applications** at CSTU. You run it in class, then
grow it across the course into an Agentic RAG app for your own career or service offering.

```
React + Vite (browser)  --SSE-->  FastAPI  --->  model (OpenRouter)
                                     |
                                     +--->  local Supabase (Postgres)
```

The backend keeps three jobs in three files, so you can swap any one without touching the others:

| Layer | File | Owns |
|---|---|---|
| State | `backend/app/state.py` | what this conversation remembers |
| Inference | `backend/app/inference.py` | the only code that talks to a model |
| Storage | `backend/app/storage.py` | saving messages to Postgres |

## Run it

Needs Docker, Node 22, [uv](https://docs.astral.sh/uv/), and the [Supabase CLI](https://supabase.com/docs/guides/local-development/cli/getting-started).

```bash
git clone https://github.com/pingwu/cse642-agentic-app.git
cd cse642-agentic-app
git checkout S03
```

```bash
supabase start          # prints the local API, DB and Studio addresses
```

```bash
cd backend
cp .env.example .env    # then paste your OpenRouter key after OPENROUTER_API_KEY=
uv venv --python 3.12 && uv pip install -r pyproject.toml
.venv/bin/uvicorn app.main:app --port 8000
```

```bash
cd frontend             # in a second terminal
npm install && npm run dev
```

Open http://127.0.0.1:5173 and press **Ask**. The answer should appear a few words at a time
(Server-Sent Events). With no key the app streams a canned reply, so the pipeline still works.
Each message is saved to the `messages` table; look at it in Studio at http://127.0.0.1:54323.
Never commit your key: `.env` is git-ignored. Set a spending limit on your OpenRouter account.

## Two ways to build what this course teaches

1. **With an LLM coding agent** (Claude Code, Codex, GitHub Copilot, the Antigravity app). You can
   ask one of these to produce the same career or service-offering result for yourself, alone.
   Fast, and fine for a personal tool.
2. **With agent frameworks** (LangChain for RAG, CrewAI for agents and flows). Choose this way when
   you want to **productize** your solution: something other people use, with evaluation, tracing
   and a structure you can maintain. The course teaches this way, session by session.

## Not covered here: build a platform on your own

A real platform needs **paywalls, authentication and entitlements** (who may see what, and who has paid).
Each is a subject of its own and does not fit in a 7-week course, so this app has none of them.
If you want to turn your solution into a platform application, plan to study these yourself.
Start with your auth provider's docs, a payments provider's test mode, and a rule for how an
account maps to what it is allowed to use.

## License

MIT. See `LICENSE`.
