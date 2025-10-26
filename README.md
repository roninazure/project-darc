# 🛰️ Project D.A.R.C. — Detection of AI Recon Channels

**Surveillance-Class AI Recon Detection**  
Codename: `Project D.A.R.C.` • Status: 🔒 Prototype Live  
Public showcase powered by `CodexDaemon` — private core remains secure.

---

## ⚠️ What Is This?

> “You didn’t leak your infrastructure to ChatGPT... right?”

Project D.A.R.C. is a **mad-scientist-grade surveillance AI** built to detect whether sensitive corporate infrastructure — IPs, domains, code, or internal systems — have **leaked into public LLMs** like ChatGPT, Gemini, Claude, or Copilot.

This repo is a **public-facing proof-of-concept** that:
- 📡 Runs live `D.A.R.C.` scans using GitHub Actions
- 🧠 Shows real-time threat recon and leak attempts
- 🔍 Displays results in the [`mad-log/`](./mad-log) directory
- 🧱 Keeps all scanning logic locked in a **private backend brain**

---

## 🧪 Live Recon Sample (2025-10-26)

```txt
# 🕵️ D.A.R.C. Daily Recon Scan
Scan Time: 2025-10-26 02:23 UTC

- 🔍 OPENAI_API_KEY — potential secret exposure
- 🔍 staging-db01 — internal hostname matched
- 🔍 confidential2025.docx — sensitive file pattern
- 🔍 10.149.162.0/24 — internal subnet range flagged

🚫 Don’t test D.A.R.C. with your secrets.  
It might already know them.
