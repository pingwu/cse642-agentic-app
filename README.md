# CSE 642 starter app

The starter app for **CSE 642, Agentic AI and Applications** at CSTU. You run it in class, then
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

## Run it with Docker (Build Checkpoint 2 starting point)

Needs Docker Desktop (running) and Git. Nothing else to install: Python 3.12, Node 22 and Postgres with pgvector run in containers.

```bash
git clone --branch CP2-start https://github.com/pingwu/cse642-agentic-app.git
cd cse642-agentic-app
git switch -c my-app          # your edits live on your own branch
docker compose up --build     # the first start takes a few minutes
```

Open http://localhost:5173 and press **Ask**. The status line under the answer shows whether the backend is connected, whether the message was saved to the database, and whether the reply is from the model or a sample (no key). Without a key the app streams a sample reply, so the pipeline still works.

To use a real model, copy `backend/.env.example` to `backend/.env`, paste your OpenRouter key after `OPENROUTER_API_KEY=`, and run `docker compose up` again. Never commit your key (`.env` is git-ignored) and set a spending limit on your OpenRouter account.

Look at the saved messages:

```bash
docker compose exec db psql -U postgres -c "select role, left(content, 60) from public.messages order by id;"
```

| Need | Command |
|---|---|
| Stop (keep your data) | `docker compose down` |
| Start fresh (deletes the database data) | `docker compose down -v` |
| Port already in use | `FRONTEND_PORT=15173 BACKEND_PORT=18000 docker compose up` (PowerShell: `$env:FRONTEND_PORT=15173; $env:BACKEND_PORT=18000; docker compose up`) |

The database starts empty the first time: it enables pgvector and applies `supabase/migrations`. A new migration file only runs on a new database, so after adding one run `docker compose down -v`. Every port listens on this computer only (127.0.0.1).

## Run it without Docker (tag `S03`, Session 3)

Session 3 uses the frozen `S03` tag and runs on your computer directly. It needs Docker, Node 22, [uv](https://docs.astral.sh/uv/), and the [Supabase CLI](https://supabase.com/docs/guides/local-development/cli/getting-started).

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

Open http://127.0.0.1:5173 and press **Ask**. The answer should appear a few words at a time (Server-Sent Events). Each message is saved to the `messages` table; look at it in Studio at http://127.0.0.1:54323.

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
