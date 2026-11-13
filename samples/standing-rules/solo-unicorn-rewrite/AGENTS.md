# AGENTS.md (a short rewrite of the Solo Unicorn rules)

Solo Unicorn Builder is a product incubator. Strategy lives in ANCHOR.md, coding principles in DEVELOPMENT-STANDARDS.md. This file holds only the rules you cannot guess.

## Hard lines
- Run installs, builds, dev servers and tests inside Docker, never on the host. Development must match production, and the host stays clean.
- Never hardcode keys, passwords or tokens, and never commit .env files. Read secrets from environment variables.
- Write app code only inside a sub-project of ../my_projects/. This repo holds the incubator, not apps.
- Treat ../my_knowledge/ as my private vault: read it for context, never commit it here.
- Do not edit template_knowledge/ unless I say so. It is a template that gets copied.

## How to work
- Start containers detached. Add new dev tools to Dockerfile.dev, not the host.
- Run the test suite in the container before every commit: docker compose exec dev npm run test:run
- Write the test first, build the simplest thing that proves the idea, and add no speculative features.
- Pick skills from skills/ by the job, not by role. Each skill file says when to use it.

## Conventions
- Every .md file has front matter with name (kebab-case) and description (one line).
- TypeScript strict mode. React Server Components by default; add use client only when needed.
- Python packages go through uv, never ad-hoc pip install.
