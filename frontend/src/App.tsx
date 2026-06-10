import { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [sql, setSql] = useState("");
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [blocked, setBlocked] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setBlocked(false);
    setSql("");
    setResults([]);
    try {
      const res = await axios.post("http://localhost:8000/query", { question });
      setSql(res.data.sql);
      setResults(res.data.results);
      setBlocked(res.data.blocked);
    } catch {
      alert("Backend not connected.");
    }
    setLoading(false);
  };

  return (
    <div style={{ minHeight: "100vh", background: "#0f0f1a", color: "#e2e8f0", fontFamily: "'Segoe UI', sans-serif" }}>

      {/* Header */}
      <div style={{ background: "#1a1a2e", borderBottom: "1px solid #2d2d4e", padding: "16px 32px", display: "flex", alignItems: "center", gap: 12 }}>
        <div style={{ width: 32, height: 32, background: "linear-gradient(135deg, #6366f1, #8b5cf6)", borderRadius: 8, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 16 }}>🧠</div>
        <span style={{ fontWeight: 700, fontSize: 18, color: "#a5b4fc" }}>Text-to-SQL</span>
        <span style={{ marginLeft: "auto", fontSize: 12, color: "#4a5568", background: "#2d2d4e", padding: "4px 10px", borderRadius: 20 }}>Olist E-Commerce DB</span>
      </div>

      {/* Main */}
      <div style={{ maxWidth: 860, margin: "48px auto", padding: "0 24px" }}>

        {/* Hero */}
        <div style={{ textAlign: "center", marginBottom: 40 }}>
          <h1 style={{ fontSize: 36, fontWeight: 800, margin: 0, background: "linear-gradient(90deg, #6366f1, #a78bfa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>
            Ask your database anything
          </h1>
          <p style={{ color: "#64748b", marginTop: 10, fontSize: 15 }}>
            Type a question in plain English — get SQL and results instantly
          </p>
        </div>

        {/* Input Card */}
        <div style={{ background: "#1a1a2e", border: "1px solid #2d2d4e", borderRadius: 16, padding: 24, marginBottom: 24 }}>
          <label style={{ fontSize: 12, color: "#6366f1", fontWeight: 600, letterSpacing: 1, textTransform: "uppercase" }}>Your Question</label>
          <textarea
            rows={3}
            style={{ width: "100%", marginTop: 8, background: "#0f0f1a", border: "1px solid #2d2d4e", borderRadius: 10, padding: 14, fontSize: 15, color: "#e2e8f0", resize: "none", outline: "none", boxSizing: "border-box" }}
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && handleAsk()}
            placeholder="e.g. What are the top 5 product categories by revenue?"
          />
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 12 }}>
            <span style={{ fontSize: 12, color: "#4a5568" }}>Press Enter to run</span>
            <button
              onClick={handleAsk}
              disabled={loading}
              style={{ padding: "10px 28px", fontSize: 14, fontWeight: 600, background: loading ? "#3730a3" : "linear-gradient(135deg, #6366f1, #8b5cf6)", color: "white", border: "none", borderRadius: 10, cursor: loading ? "not-allowed" : "pointer", transition: "opacity 0.2s" }}
            >
              {loading ? "⏳ Thinking..." : "Run Query →"}
            </button>
          </div>
        </div>

        {/* Example pills */}
        {!sql && (
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 32 }}>
            {["Top 5 categories by revenue", "Average review score by state", "Total orders per month"].map(q => (
              <button key={q} onClick={() => setQuestion(q)}
                style={{ background: "#1a1a2e", border: "1px solid #2d2d4e", color: "#a5b4fc", padding: "6px 14px", borderRadius: 20, fontSize: 13, cursor: "pointer" }}>
                {q}
              </button>
            ))}
          </div>
        )}

        {/* Blocked warning */}
        {blocked && (
          <div style={{ background: "#2d1515", border: "1px solid #7f1d1d", borderRadius: 12, padding: 16, marginBottom: 20, color: "#fca5a5" }}>
            ⚠️ This query was blocked for safety reasons.
          </div>
        )}

        {/* SQL Output */}
        {sql && (
          <div style={{ background: "#1a1a2e", border: "1px solid #2d2d4e", borderRadius: 16, marginBottom: 24, overflow: "hidden" }}>
            <div style={{ padding: "12px 20px", borderBottom: "1px solid #2d2d4e", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span style={{ fontSize: 12, color: "#6366f1", fontWeight: 600, letterSpacing: 1, textTransform: "uppercase" }}>Generated SQL</span>
              <button onClick={() => navigator.clipboard.writeText(sql)}
                style={{ fontSize: 12, color: "#64748b", background: "none", border: "none", cursor: "pointer" }}>Copy</button>
            </div>
            <pre style={{ margin: 0, padding: 20, fontSize: 13, color: "#a5b4fc", overflowX: "auto", lineHeight: 1.6 }}>{sql}</pre>
          </div>
        )}

        {/* Results Table */}
        {results.length > 0 && (
          <div style={{ background: "#1a1a2e", border: "1px solid #2d2d4e", borderRadius: 16, overflow: "hidden" }}>
            <div style={{ padding: "12px 20px", borderBottom: "1px solid #2d2d4e" }}>
              <span style={{ fontSize: 12, color: "#6366f1", fontWeight: 600, letterSpacing: 1, textTransform: "uppercase" }}>Results</span>
              <span style={{ marginLeft: 10, fontSize: 12, color: "#4a5568" }}>{results.length} rows</span>
            </div>
            <div style={{ overflowX: "auto" }}>
              <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
                <thead>
                  <tr style={{ background: "#0f0f1a" }}>
                    {Object.keys(results[0]).map(k => (
                      <th key={k} style={{ padding: "10px 16px", textAlign: "left", color: "#6366f1", fontWeight: 600, fontSize: 11, textTransform: "uppercase", letterSpacing: 0.5 }}>{k}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {results.map((row, i) => (
                    <tr key={i} style={{ borderTop: "1px solid #2d2d4e", background: i % 2 === 0 ? "#1a1a2e" : "#16162a" }}>
                      {Object.values(row).map((v: any, j) => (
                        <td key={j} style={{ padding: "10px 16px", color: "#cbd5e1" }}>{String(v)}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;