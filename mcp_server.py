# /// script
# requires-python = ">=3.11"
# dependencies = ["mcp>=1.9,<2"]
# ///
"""Session 5 template: a small MCP server called "benchmarks".

It exposes one tool, lookup_external_benchmark, over Streamable HTTP.

Run it (uv installs mcp for you, nothing else to set up):

    uv run mcp_server.py

Then add it to your coding agent:

    claude mcp add --transport http benchmarks http://127.0.0.1:8001/mcp

Rules this file keeps, and your edits should too:
  * It listens on 127.0.0.1 only. Never change the host to 0.0.0.0: that would
    let anyone on your network call your tools.
  * No key or secret appears in this file.
  * A question with no match returns a clear "no data" message, not a guess.

Your track decides the data file. Career uses career.json, Startup uses startup.json.
Set it for one run with:   BENCHMARK_TRACK=startup uv run mcp_server.py
"""

import json
import os
import re
from pathlib import Path

from mcp.server.fastmcp import FastMCP

HOST = "127.0.0.1"
PORT = 8001

TRACK = os.environ.get("BENCHMARK_TRACK", "career")
DATA_FILE = Path(__file__).parent / "data" / "benchmarks" / f"{TRACK}.json"

mcp = FastMCP("benchmarks", host=HOST, port=PORT)


def _load_entries() -> list[dict]:
    with DATA_FILE.open(encoding="utf-8") as f:
        return json.load(f)["entries"]


def _words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


@mcp.tool()
def lookup_external_benchmark(query: str) -> str:
    """Look up a short market or job-demand benchmark for a role, skill or product category.

    Use this when the user asks how much demand, pay or competition exists for something.
    Pass a short phrase such as "data engineer demand" or "small team help desk pricing".
    Returns one short answer and the source it came from. If nothing matches, says so.
    """
    wanted = _words(query)
    best, best_score = None, 0
    for entry in _load_entries():
        keys = set().union(*(_words(k) for k in entry["keywords"]))
        score = len(wanted & keys)
        if score > best_score:
            best, best_score = entry, score
    if best is None:
        return f"No benchmark data for '{query}' in the {TRACK} data file."
    return f"{best['answer']} (Source: {best['source']})"


if __name__ == "__main__":
    print(f"benchmarks server ({TRACK} data) listening on http://{HOST}:{PORT}/mcp", flush=True)
    mcp.run(transport="streamable-http")
