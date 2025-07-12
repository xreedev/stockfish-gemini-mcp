

## `stockfish-gemini-mcp`

**Multi-Context Processor** connecting **Stockfish** (chess engine) with **Gemini API** (Google’s LLM).

### 🚩 What it does

* Loads chess games (PGN).
* Uses Stockfish to evaluate positions.
* Queries Gemini for context-aware commentary.
* Pipes all this into a processing flow you control.

This is **experimental glue code**, not production-ready chess UI.
Expect to extend, not just clone and run.

---

### 📂 Project structure (typical)

```
.
├── main.py
├── stockfish_interface.py
├── gemini_interface.py
├── requirements.txt
├── .env
└── README.md
```

---

### ⚡ Requirements

* Python 3.9+
* Stockfish installed and accessible in PATH
* Gemini API key

---

### 🔑 Setup

1. **Clone**

   ```bash
   git clone https://github.com/xreedev/stockfish-gemini-mcp.git
   cd stockfish-gemini-mcp
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup `.env`**

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

   *Don’t push your key to GitHub again. If you did, revoke it.*

4. **Verify Stockfish**

   ```bash
   stockfish
   ```

   If it runs in terminal, you’re good.

---

### ▶️ Run

```bash
python main.py
```

This will:

* Parse a PGN (or however you coded it).
* Evaluate moves with Stockfish.
* Send positions/comments to Gemini.
* Print or save the output.

---

### ⚠️ Notes

* This is **not safe for high-volume queries** — Gemini API costs can spike.
* Be mindful about sending **PGN data** to third parties.
* If you want to use this for actual chess coaching, wrap it in a real frontend.
* If you find bugs, fix them — this is starter code, not a library.

---

### 🛠️ TODOs

* [ ] Add tests
* [ ] Better error handling (Stockfish/Gemini failures)
* [ ] Async pipeline for faster evals
* [ ] Frontend or CLI polish

---

## License

Add one if you care.
Otherwise, it’s “use at your own risk.”

---

**That’s it.**
