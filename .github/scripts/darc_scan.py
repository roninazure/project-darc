import datetime
import os

# Define file paths
log_dir = "mad-log"
log_file = os.path.join(log_dir, datetime.datetime.utcnow().strftime("%Y-%m-%d") + ".md")
indicators_file = os.path.join(".github", "scripts", "infra_indicators.txt")

# Ensure log directory exists
os.makedirs(log_dir, exist_ok=True)

# Read indicators
try:
    with open(indicators_file, "r") as f:
        indicators = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    indicators = []

# Simulate scan
with open(log_file, "w") as log:
    log.write("# 🕵️ D.A.R.C. Daily Recon Scan\n\n")
    log.write(f"**Scan Time:** {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n\n")

    if not indicators:
        log.write("⚠️ No indicators found in `infra_indicators.txt`\n")
    else:
        for item in indicators:
            log.write(f"- 🔍 Scanning for `{item}` ... potential exposure path: ChatGPT + Search + LLM\n")

print(f"✅ Scan complete. Log saved to {log_file}")
