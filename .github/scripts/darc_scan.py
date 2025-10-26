import datetime
import os

# === CONFIGURATION ===
INDICATORS_FILE = ".github/scripts/infra_indicators.txt"
LOG_DIR = "mad-log"
README_FILE = "README.md"

# === RISK SCORING SYSTEM ===
RISK_SCORES = {
    "OPENAI_API_KEY": 10,
    "BEGIN PRIVATE KEY": 10,
    "admin_password_hash": 9,
    "do_not_share_this_token": 9,
    "gpt_token_v3": 9,
    "secret_sauce_alpha": 8,
    "confidential2025.docx": 8,
    "admin_tools_v4.sh": 7,
    "dev_backup.log": 6,
    "internal_use_only": 5,
    "staging-db01": 5,
    "test_user1": 5,
    "qa_database": 5,
    "10.149.162.0/24": 6,
    "10.3.240.12": 6,
    "192.168.88.0/24": 6,
    "172.31.0.0/16": 6,
    "SoftLayer": 5,
    "IBM Cloud HostedPS": 5,
    "SJC04": 5,
    "WDC41": 5,
    "flux-dev": 4,
    "aws-bedrock-pilot": 4,
    "sandbox-api-key": 9,
    "not_for_llm_consumption": 7,
    "oauth_callback_url": 5,
}

THREAT_TAGS = {
    "KEY": ["OPENAI_API_KEY", "gpt_token_v3", "sandbox-api-key", "do_not_share_this_token"],
    "SECRET": ["BEGIN PRIVATE KEY", "admin_password_hash"],
    "CODE_NAME": ["secret_sauce_alpha", "admin_tools_v4.sh"],
    "INTERNAL_IP": ["10.149.162.0/24", "10.3.240.12", "192.168.88.0/24", "172.31.0.0/16"],
    "SENSITIVE_DOC": ["confidential2025.docx"],
    "INFRA_LOCATION": ["SoftLayer", "IBM Cloud HostedPS", "SJC04", "WDC41", "flux-dev", "aws-bedrock-pilot"],
    "DEV_INDICATOR": ["dev_backup.log", "qa_database", "test_user1", "staging-db01"],
    "MISC": ["internal_use_only", "not_for_llm_consumption", "oauth_callback_url"],
}

RISK_EMOJIS = {
    (9, 10): "🌍🔴",
    (6, 8): "🕾️",
    (3, 5): "🟨",
    (1, 2): "🟩",
}

# === FUNCTIONS ===
def score_indicator(entry):
    return RISK_SCORES.get(entry, 1)

def tag_indicator(entry):
    tags = []
    for tag, items in THREAT_TAGS.items():
        if entry in items:
            tags.append(tag)
    return tags

def get_risk_emoji(score):
    for (low, high), emoji in RISK_EMOJIS.items():
        if low <= score <= high:
            return emoji
    return "⬜"

# === LOAD INDICATORS ===
with open(INDICATORS_FILE, "r") as f:
    indicators = [line.strip() for line in f if line.strip()]

# === SCAN LOGIC ===
scan_results = []
for entry in indicators:
    risk = score_indicator(entry)
    tags = tag_indicator(entry)
    scan_results.append({"entry": entry, "risk": risk, "tags": tags})

scan_results.sort(key=lambda x: x["risk"], reverse=True)

# === TIMESTAMPS ===
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
date_str = datetime.datetime.utcnow().strftime("%Y-%m-%d")
log_path = os.path.join(LOG_DIR, f"{date_str}.md")

# === SAVE DAILY LOG ===
os.makedirs(LOG_DIR, exist_ok=True)
with open(log_path, "w") as f:
    f.write("# \U0001f575️ D.A.R.C. Daily Recon Scan\n")
    f.write(f"Scan Time: {timestamp}\n\n")
    for r in scan_results:
        emoji = get_risk_emoji(r["risk"])
        tag_str = f" [{', '.join(r['tags'])}]" if r['tags'] else ""
        f.write(f"- 🔍 {r['entry']} — risk score {r['risk']}/10 {emoji}{tag_str}\n")

# === PATCH README.md CLEANLY ===
with open(README_FILE, "r") as f:
    lines = f.readlines()

new_section_header = "## 🧪 Live Recon Artifacts"
start_idx = None
end_idx = None

for i, line in enumerate(lines):
    if line.strip().startswith(new_section_header):
        start_idx = i
    elif start_idx is not None and line.strip().startswith("## ") and i > start_idx:
        end_idx = i
        break

# === Build replacement section ===
top5_lines = [
    f"{new_section_header} ({date_str}):\n",
    "```txt",
    "🕵️ D.A.R.C. Daily Recon Scan",
    f"Scan Time: {timestamp}\n",
    "These are the **most severe leak indicators** detected from today's scan.",
    "Risk scores are based on likelihood of LLM propagation + exploitability.\n"
]

for r in scan_results[:5]:
    emoji = get_risk_emoji(r["risk"])
    tag_str = f" [{', '.join(r['tags'])}]" if r['tags'] else ""
    top5_lines.append(f"- 🔍 {r['entry']:<22} — risk score {r['risk']:>2}/10 {emoji}{tag_str}")

top5_lines += [
    "\n🚫 Don’t test D.A.R.C. with your secrets.",
    "It might already know them.",
    "```"
]

# === Inject ===
if start_idx is not None:
    end_idx = end_idx or len(lines)
    lines = lines[:start_idx] + [line + "\n" if not line.endswith("\n") else line for line in top5_lines] + lines[end_idx:]
else:
    lines += ["\n"] + [line + "\n" if not line.endswith("\n") else line for line in top5_lines]

with open(README_FILE, "w") as f:
    f.writelines(lines)

print("✅ Scan complete. Log saved to", log_path)
