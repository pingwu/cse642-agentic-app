# Session 5 data

Everything here is **fictional sample data** for the CSE 642 labs. None of it describes a real school, company, job or market.

| Folder | What it is | Used by |
|---|---|---|
| `reference/` | Short pages to chunk and embed. The file name starts with its `source_type`: `catalog`, `skills`, `job`, `courses` (Career) and `competitor`, `market`, `case` (Startup). Pages you collect with Firecrawl land here too. | Session 5 embed step |
| `benchmarks/` | `career.json` and `startup.json`: the small lookup files behind the `lookup_external_benchmark` tool. | `mcp_server.py` |

**Embedding model, pinned:** `openai/text-embedding-3-small`, 1536 dimensions, through OpenRouter (see `backend/.env.example`). The vector column is `vector(1536)`. If you change the model, change the dimension and re-embed everything: vectors from different models cannot be compared.

**No embedding key?** Load `supabase/seed_vectors.sql` (pre-computed vectors for `reference/`). Instructors rebuild it with `scripts/make_seed_vectors.py`.
