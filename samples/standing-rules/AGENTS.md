# AGENTS.md

My MASProjects workspace: code for my courses and projects, plus my career notes.

## Where things go
- Application code goes in my_projects/. Essays, plans, notes and ledgers go in my_knowledge/. My career folder is my_knowledge/career.
- Change files only in the folder I name. Ask before creating anything outside MASProjects.

## Rules, with reasons
- Keep keys and passwords out of files; use environment variables. These repos get pushed to GitHub.
- Treat career/sources as read-only. Those are my originals; put summaries in new files.
- Keep applications/, salary notes and current-employer details off public pages. A landing page is public.
- After you change a career file, update career/index.md and add one line to career/log.md: the date, then ingest, query or lint, then a title. The log is how I see what changed.

## How I work
- Run the app with docker compose up, and check a change in the browser before you say it works.
- Work on a branch in small commits. Never push to main.
- Tell me the plan before you change more than three files.
