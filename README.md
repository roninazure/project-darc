<!-- DARC-HEADER -->
<div align="center">

# 🛰️ <span style="font-size:1.8em">Project D.A.R.C.</span>  
## <sub><sup>Detection of AI Recon Channels</sup></sub>

**Surveillance-Class AI Recon Detection**  
🔒 Prototype | 🎯 Live Recon | 💡 Powered by `CodexDaemon`

</div>

---
+ <div align="center">
+   <span style="font-size:1.2em">❝ You didn’t leak your infrastructure to ChatGPT… right? ❞</span><br>
+   <sub>— Internal Memo - National Vision 2025</sub>
+ </div>
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
<sup>Last Scan: 2025-10-28</sub>

```txt
🕵️ D.A.R.C. Daily Recon Scan  
Scan Time: 2025-10-28 22:03 UTC

These are the **most severe leak indicators** detected from today's scan.  
Risk scores estimate likelihood of LLM propagation + exploitability.

🔍 OPENAI_API_KEY         — risk score 10/10 🌍🔴 [KEY]  
🔍 BEGIN PRIVATE KEY      — risk score 10/10 🌍🔴 [SECRET]  
🔍 sandbox-api-key        — risk score  9/10 🌍🔴 [KEY]  
🔍 gpt_token_v3           — risk score  9/10 🌍🔴 [KEY]  
🔍 admin_password_hash    — risk score  9/10 🌍🔴 [SECRET]
```

🚫 Don’t test D.A.R.C. with your secrets.  
It might already know them.

<div align="center">
  <sub>© 2025 RoninAzure • Powered by CodexDaemon</sub>  
  <br><br>
  <sup>⚠️ No real secrets are used. Public output is safe.⚠️ </sup>
</div>
