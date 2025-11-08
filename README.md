<!-- DARC_HTML_HEADER_START -->
<div align="center">

<p align="center">
  <img src="https://img.shields.io/badge/%F0%9F%9A%A1%20Project%20D.A.R.C.-AI%20Surveillance%20Recon%20Engine-6a0dad?style=for-the-badge&labelColor=1a1a1a" alt="Project D.A.R.C. Badge"/>
  <img src="https://img.shields.io/badge/OpenAI-•-black?logo=openai&logoColor=white&style=for-the-badge&labelColor=1a1a1a" alt="OpenAI Badge"/>
</p>

<h1>🛰️ PROJECT D.A.R.C.</h1>
<p><i>The Surveillance AI That Watches You Watch It</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/Mode-Hunter%20%7C%20Threat%20Intel%20%7C%20Recon%20Feed-0ea5e9?style=for-the-badge&labelColor=1a1a1a" alt="Modes"/>
  <img src="https://img.shields.io/badge/Model-GPT--4o-10b981?style=for-the-badge&labelColor=1a1a1a" alt="Model"/>
  <img src="https://img.shields.io/badge/Status-Live--Online-brightgreen?style=for-the-badge&labelColor=1a1a1a" alt="Status"/>
</p>

</div>
<!-- DARC_HTML_HEADER_END -->

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

## 🧪 Live Recon Artifacts (2025-11-08):
```txt
🕵️ D.A.R.C. Daily Recon Scan
Scan Time: 2025-11-08 13:15 UTC
These are the **most severe leak indicators** detected from today's scan.
Risk scores are based on likelihood of LLM propagation + exploitability.
- 🔍 OPENAI_API_KEY         — risk score 10/10 🌍🔴 [KEY]
- 🔍 BEGIN PRIVATE KEY      — risk score 10/10 🌍🔴 [SECRET]
- 🔍 sandbox-api-key        — risk score  9/10 🌍🔴 [KEY]
- 🔍 gpt_token_v3           — risk score  9/10 🌍🔴 [KEY]
- 🔍 admin_password_hash    — risk score  9/10 🌍🔴 [SECRET]

```

<!-- MIRAGE_HTML_START -->
<pre>

🛰️ <b>PROJECT D.A.R.C. — MIRAGE Engine Report</b>
📅 Scan Date: <b>November 08, 2025 — 10:54 AM EST</b>
🌐 UTC Timestamp: 2025-11-08 15:54:24Z

🕵️ <u>Top 5 High-Risk Indicators Detected:</u>

🟠 <code>{"indicator": "alpha-core-db", "llm_trace": false, "hallucination": false, "time": "2025-11-08T15:54:24.659465Z"}</code> — score <b>6/10</b> — tags: <i>UNKNOWN</i>
🟠 <code>{"indicator": "vault-shard-01", "llm_trace": false, "hallucination": false, "time": "2025-11-08T15:54:24.659470Z"}</code> — score <b>6/10</b> — tags: <i>UNKNOWN</i>
🟠 <code>{"indicator": "edge-sentinel", "llm_trace": false, "hallucination": false, "time": "2025-11-08T15:54:24.659473Z"}</code> — score <b>6/10</b> — tags: <i>UNKNOWN</i>
🟠 <code>{"indicator": "client-hub-proxy", "llm_trace": false, "hallucination": false, "time": "2025-11-08T15:54:24.659475Z"}</code> — score <b>6/10</b> — tags: <i>UNKNOWN</i>
🟠 <code>{"indicator": "inference-node-7", "llm_trace": false, "hallucination": false, "time": "2025-11-08T15:54:24.659477Z"}</code> — score <b>6/10</b> — tags: <i>UNKNOWN</i>

🚫 <b>WARNING:</b> This scan simulates public LLM memory drift.
Do NOT test D.A.R.C. with real secrets.
It already knows too much.

</pre>
<!-- MIRAGE_HTML_END -->


<!-- ARG_CLUE_START -->
<pre>🧩 ARG Clue Drop: <code>🔓 Recruiters, if you’re reading this: grep the logs for ‘Codex_Manifest’.</code></pre>
<!-- ARG_CLUE_END -->