import { useEffect, useRef, useState } from "react";
import { createRoot } from "react-dom/client";

const sessionId = crypto.randomUUID();

function App() {
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
    <main style={{ maxWidth: 640, margin: "2rem auto", fontFamily: "system-ui" }}>
      <h1>CSE 642 skeleton</h1>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} rows={3} style={{ width: "100%" }} />
      <button onClick={ask}>Ask</button>
      <p style={{ whiteSpace: "pre-wrap" }}>{answer}</p>
      {status && (
        <p style={{ color: "#555", fontSize: "0.9rem" }}>
          Backend: {status.ok ? "connected" : "not reachable"} · Saved to database: {status.db ? "yes" : "no"} · Replies: {status.llm === "live" ? "from the model" : "sample (no API key)"}
        </p>
      )}
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
