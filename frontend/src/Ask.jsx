import { useEffect, useRef, useState } from "react";

const sessionId = crypto.randomUUID();

export default function Ask() {
  const [prompt, setPrompt] = useState("Explain RAG in two sentences.");
  const [answer, setAnswer] = useState("");
  const [status, setStatus] = useState(null);
  const source = useRef(null);

  useEffect(() => {
    fetch("/api/health").then((r) => r.json()).then(setStatus).catch(() => setStatus({ ok: false }));
  }, []);

  function ask() {
    source.current?.close();
    setAnswer("");
    const url = `/api/chat?session_id=${sessionId}&prompt=${encodeURIComponent(prompt)}`;
    const es = new EventSource(url);
    source.current = es;
    es.addEventListener("token", (e) => setAnswer((a) => a + e.data));
    es.addEventListener("done", () => es.close());
    es.onerror = () => es.close();
  }

  return (
    <div className="page">
      <nav>
        <a href="/">← Home</a>
        <span>Assistant</span>
      </nav>
      <h1>Ask a question</h1>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} rows={3} />
      <button onClick={ask}>Ask</button>
      <p style={{ whiteSpace: "pre-wrap" }}>{answer}</p>
      {status && (
        <p style={{ color: "#5d6a6e", fontSize: "0.9rem" }}>
          Backend: {status.ok ? "connected" : "not reachable"} · Saved to database: {status.db ? "yes" : "no"} · Replies: {status.llm === "live" ? "from the model" : "sample (no API key)"}
        </p>
      )}
    </div>
  );
}
