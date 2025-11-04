<!-- PROJECT D.A.R.C. README FUSION HEADER -->

<div align="center">

### 🛰️ PROJECT D.A.R.C.
#### Detection of AI Recon Channels  
<sub><sup>“The Surveillance AI That Watches You Watch It”</sup></sub>

---

<kbd>🧠 PHASE</kbd> <kbd style="background:#7b1fa2;color:#fff;">2.3 ➝ INFRA MEMORY SCAN + RECON TAGGING</kbd>  
<kbd>🎯 MODE</kbd> <kbd style="background:#0d47a1;color:#fff;">HUNTER</kbd> <kbd style="background:#1b5e20;color:#fff;">THREAT INTEL</kbd> <kbd style="background:#880e4f;color:#fff;">RECON FEED</kbd>  
<kbd>📡 STATUS</kbd> <kbd style="background:#00c853;color:#000;">LIVE‑ONLINE</kbd> <kbd>🧬 MODEL</kbd> <kbd style="background:#ffd600;color:#000;">GPT‑4o</kbd>

---

> ❝ *The model already saw your infrastructure...  
> It's just waiting for confirmation.* ❞  
<sub>— CodexDaemon // Ghost Memo #007</sub>

</div>

<br>

---

## 🧠 What is D.A.R.C.?

**Project D.A.R.C.** is a surveillance-grade AI recon system that detects whether sensitive corporate infrastructure — IPs, domains, credentials, or internal systems — have **leaked into public LLMs** like ChatGPT, Claude, Gemini, or Copilot.

<div align="center">

| ✅ 100% Local Logic | 🧱 Private Recon Brain | 📡 Live Threat Surface |
|--------------------|------------------------|------------------------|

</div>

This repo serves as the **public-facing showcase**. All private scanning logic is kept secure, while this interface displays live recon results, GitHub-triggered scans, and the latest detected leak artifacts.

---

## 🔬 How It Works

- 🔁 Runs GitHub Action scans using **CodexDaemon**
- 🔍 Outputs results to [`mad-log/`](./mad-log) with timestamps
- 🧠 Uses regex + AI fingerprinting to detect threat indicators
- 🚫 Does **not** expose any private payloads or live secrets

---

## 🧪 Live Recon Artifacts
<sub><sup>Last Scan: 2025-10-28</sup></sub>

```txt
🕵️  D.A.R.C. Daily Recon Scan
Scan Time: 2025-10-28 22:03 UTC

These are the **most severe leak indicators** detected from today's scan.
Risk scores estimate likelihood of LLM propagation + exploitability.

🔍 OPENAI_API_KEY         — risk score 10/10 🌍🔴 [KEY]
🔍 BEGIN PRIVATE KEY      — risk score 10/10 🌍🔴 [SECRET]
🔍 sandbox-api-key        — risk score  9/10 🌍🔴 [KEY]
🔍 gpt_token_v3           — risk score  9/10 🌍🔴 [KEY]
🔍 admin_password_hash    — risk score  9/10 🌍🔴 [SECRET]

🚫 Don’t test D.A.R.C. with your secrets.
It might already know them.
```

<div align="center">
  <sub>© 2025 RoninAzure • Powered by CodexDaemon</sub>  
  <br><br>
  <sup>⚠️ No real secrets are used. Public output is safe.⚠️ </sup>
</div>


