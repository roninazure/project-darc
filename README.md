<div align="center">

<h1>🛰️ PROJECT D.A.R.C.</h1>

**Detection of AI Recon Channels**  
*“The Surveillance AI That Watches You Watch It”*

&nbsp;

<table>
  <tr>
    <td><kbd>🧠 PHASE</kbd></td>
    <td><kbd>2.3 ➝ INFRA MEMORY SCAN + RECON TAGGING</kbd></td>
  </tr>
  <tr>
    <td><kbd>🎯 MODE</kbd></td>
    <td><kbd>HUNTER</kbd> <kbd>THREAT INTEL</kbd> <kbd>RECON FEED</kbd></td>
  </tr>
  <tr>
    <td><kbd>📡 STATUS</kbd></td>
    <td><kbd>LIVE‑ONLINE</kbd></td>
  </tr>
  <tr>
    <td><kbd>🧬 MODEL</kbd></td>
    <td><kbd>GPT‑4o</kbd></td>
  </tr>
</table>

&nbsp;

<i>“The model already saw your infrastructure...<br>
It's just waiting for confirmation.”</i>  
— <sub>CodexDaemon // Ghost Memo #007</sub>

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

## 🧪 Live Recon Artifacts (2025-11-04):
```txt
🕵️ D.A.R.C. Daily Recon Scan
Scan Time: 2025-11-04 04:05 UTC
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
