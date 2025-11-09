# mirage/mirage_injector.py

import sys
import json
from pathlib import Path
from datetime import datetime

README_PATH = Path("README.md")
START_TAG = "<!-- MIRAGE_BLOCK_START -->"
END_TAG = "<!-- MIRAGE_BLOCK_END -->"

def format_indicator(entry):
    indicator = entry.get("indicator", "unknown")
    emoji = entry.get("emoji", "")
    score = entry.get("score", 0)
    tags = entry.get("tags", [])
    tags_html = " | ".join(f"<code>{tag}</code>" for tag in tags)
    return f"<li>{emoji} <strong>{indicator}</strong> — <em>{tags_html}</em> — <code>Score: {score}</code></li>"

def build_html_block(top_indicators):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    html = [
        START_TAG,
        "",
        f"<details>",
        f"<summary><strong>🧠 MIRAGE Engine: LLM Drift Forensics (Top 5)</strong></summary>",
        f"<p><sub>Scan Time: {timestamp}</sub></p>",
        "",
        "<ul>",
    ]

    for entry in top_indicators[:5]:
        html.append(format_indicator(entry))

    html += [
        "</ul>",
        "</details>",
        "",
        END_TAG
    ]

    return "\n".join(html)

def inject_into_readme(block):
    readme_text = README_PATH.read_text() if README_PATH.exists() else ""

    if START_TAG in readme_text and END_TAG in readme_text:
        # Replace existing block
        pre = readme_text.split(START_TAG)[0]
        post = readme_text.split(END_TAG)[1]
        new_text = f"{pre}{block}{post}"
    else:
        # Append fresh block
        new_text = f"{readme_text.rstrip()}\n\n{block}\n"

    README_PATH.write_text(new_text)
    print("✅ MIRAGE block injected into README.md.")

def main():
    try:
        raw = sys.stdin.read()
        verdicts = json.loads(raw)

        if not isinstance(verdicts, list):
            raise ValueError("Expected list of verdicts.")

        sorted_ = sorted(verdicts, key=lambda x: x.get("score", 0), reverse=True)
        html_block = build_html_block(sorted_)
        inject_into_readme(html_block)

    except Exception as e:
        print(f"❌ Injection failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
