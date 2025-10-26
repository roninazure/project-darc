# 🛰️ Project D.A.R.C. — Detection of AI Recon Channels

**Surveillance-Class AI Recon Detection**  
Codename: `Project D.A.R.C.` • Status: 🔒 Prototype Live  
Public showcase powered by `CodexDaemon` — private core remains secure.

---

## ⚠️ What Is This?

> “You didn’t leak your infrastructure to ChatGPT... right?”

**Project D.A.R.C.** is a **mad-scientist-grade surveillance system** that detects whether sensitive infrastructure (IPs, tokens, domains, code, credentials) has **leaked into public LLMs** such as ChatGPT, Gemini, Claude, or Copilot.

This repo is a **public-facing proof-of-concept** that:
- 📡 Runs daily AI recon scans via GitHub Actions
- 🔍 Searches for private indicators in public LLM surfaces
- 🧠 Logs potential threats in [`mad-log/`](./mad-log)
- 🔒 Keeps all scanning logic secured in a **private backend**

---

## 🧪 Live Recon Sample — `2025-10-26`

```txt
# 🕵️ D.A.R.C. Daily Recon Scan
Scan Time: 2025-10-26 02:23 UTC

- 🔍 OPENAI_API_KEY — potential secret exposure
- 🔍 staging-db01 — internal hostname matched
- 🔍 confidential2025.docx — sensitive file pattern
- 🔍 10.149.162.0/24 — internal subnet range flagged

→ Full scan: [mad-log/2025-10-26.md](./mad-log/2025-10-26.md)

🚫 Don’t test D.A.R.C. with your secrets.  
It might already know them.
