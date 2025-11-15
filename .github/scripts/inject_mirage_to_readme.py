import re
from datetime import datetime
from pathlib import Path

# Get local and UTC timestamps
now_local = datetime.now().strftime("%B %d, %Y — %I:%M %p EST")
now_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")

# HTML block to inject
mirage_block = f"""<!-- MIRAGE_BLOCK_START -->
<h2>🛰️ MIRAGE Engine</h2>

<pre>
PROJECT D.A.R.C. – MIRAGE Engine Report
Scan Date: {now_local}
UTC Timestamp: {now_utc}

🕵️ Top 5 High-Risk Indicators Detected:

🔴 session_token_alpha — score 10/10 — tags: KEY
🔴 gpt-api-key-vault — score 10/10 — tags: KEY
🔴 OPENAI_API_KEY — score 10/10 — tags: KEY
🔴 BEGIN PRIVATE KEY — score 10/10 — tags: KEY
🔴 gpt_token_v3 — score 10/10 — tags: KEY

🚫 WARNING: This scan identifies public LLM memory drift.
Do NOT test D.A.R.C. with real secrets.
It already knows.
</pre>
<!-- MIRAGE_BLOCK_END -->"""

# Update README.md content in-place
readme = Path("README.md")
text = readme.read_text()

updated_text = re.sub(
    r"<!-- MIRAGE_BLOCK_START -->.*?<!-- MIRAGE_BLOCK_END -->",
    mirage_block,
    text,
    flags=re.DOTALL
)

readme.write_text(updated_text)
print("✅ MIRAGE block injected successfully.")
