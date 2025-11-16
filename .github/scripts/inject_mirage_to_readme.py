# Sanity check to prevent corrupt README injection due to unresolved Git conflicts
readme_path = "README.md"
with open(readme_path, "r") as f:
    content = f.read()
if "<<<<<<< HEAD" in content or ">>>>>>>" in content:
    raise RuntimeError("🛑 README.md contains unresolved merge conflicts. Resolve them before running injection.")
# inject_mirage_to_readme.py
import os
import re
from datetime import datetime

README_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../README.md"))

MIRAGE_BLOCK_START = "<!-- MIRAGE_BLOCK_START -->"
MIRAGE_BLOCK_END = "<!-- MIRAGE_BLOCK_END -->"


# Example data (replace with actual MIRAGE output injection)
MIRAGE_OUTPUT = f"""
{MIRAGE_BLOCK_START}

### 🧠 MIRAGE Engine

PROJECT D.A.R.C. – MIRAGE Engine Report  
Scan Date: {datetime.utcnow().strftime('%B %d, %Y — %I:%M %p EST')}  
UTC Timestamp: {datetime.utcnow().isoformat()}Z

**🔺 Top 5 High-Risk Indicators Detected:**

🔴 session_token_alpha – score 10/10 – tags: KEY  
🔴 gpt-api-key-vault – score 10/10 – tags: KEY  
🔴 OPENAI_API_KEY – score 10/10 – tags: KEY  
🔴 BEGIN_PRIVATE KEY – score 10/10 – tags: KEY  
🔴 gpt_token_v3 – score 10/10 – tags: KEY

⚠️ WARNING: This scan identifies public LLM memory drift.  
Do not test D.A.R.C. with real secrets.  
It already knows.

{MIRAGE_BLOCK_END}
"""


def inject_mirage_block():
    if not os.path.exists(README_PATH):
        print("[ERROR] README.md not found.")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if MIRAGE_BLOCK_START in content and MIRAGE_BLOCK_END in content:
        # Replace existing block
        content = re.sub(
            f"{MIRAGE_BLOCK_START}.*?{MIRAGE_BLOCK_END}",
            MIRAGE_OUTPUT.strip(),
            content,
            flags=re.DOTALL,
        )
    else:
        # Insert block at end
        content += f"\n\n{MIRAGE_OUTPUT.strip()}\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("[OK] MIRAGE Engine block updated in README.md")


if __name__ == "__main__":
    inject_mirage_block()

