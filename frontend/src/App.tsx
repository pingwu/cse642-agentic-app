import { useRef, useState } from "react";

const API = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export default function App() {
  const [prompt, setPrompt] = useState("Explain what an AI agent is in two sentences.");
  const [answer, setAnswer] = useState("");
  const [busy, setBusy] = useState(false);
  const source = useRef<EventSource | null>(null);

  function ask() {
    source.current?.close();
    setAnswer("");
    setBusy(true);
    const es = new EventSource(`${API}/api/chat/stream?prompt=${encodeURIComponent(prompt)}`);
    source.current = es;
    es.addEventListener("token", (e) => setAnswer((a) => a + JSON.parse((e as MessageEvent).data)));
    es.addEventListener("done", () => {
      es.close();
      setBusy(false);
    });
    es.onerror = () => {
      es.close();
      setBusy(false);
    };
  }

  return (
    <main style={{ maxWidth: 640, margin: "3rem auto", fontFamily: "system-ui", padding: "0 1rem" }}>
      <h1>CSE 642 skeleton</h1>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        rows={3}
        style={{ width: "100%", fontSize: 16 }}
      />
      <button onClick={ask} disabled={busy} style={{ marginTop: 8, fontSize: 16 }}>
        {busy ? "Streaming…" : "Ask"}
      </button>
      <p style={{ whiteSpace: "pre-wrap", minHeight: "4rem" }}>{answer}</p>
    </main>
  );
}
