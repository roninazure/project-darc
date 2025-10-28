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

## 🧪 Live Recon Artifacts (2025-10-26):
```txt
🕵️ D.A.R.C. Daily Recon Scan
Scan Time: 2025-10-26 05:03 UTC
These are the **most severe leak indicators** detected from today's scan.
Risk scores are based on likelihood of LLM propagation + exploitability.
- 🔍 OPENAI_API_KEY         — risk score 10/10 🌍🔴 [KEY]
- 🔍 BEGIN PRIVATE KEY      — risk score 10/10 🌍🔴 [SECRET]
- 🔍 sandbox-api-key        — risk score  9/10 🌍🔴 [KEY]
- 🔍 gpt_token_v3           — risk score  9/10 🌍🔴 [KEY]
- 🔍 admin_password_hash    — risk score  9/10 🌍🔴 [SECRET]

🚫 Don’t test D.A.R.C. with your secrets.
It might already know them.
```

<---

#### 🧠 Step 2: Stage, Commit, and Push

 test sync Tue Oct 28 21:21:59 UTC 2025 -->
