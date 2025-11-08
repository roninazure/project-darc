# mirage/mirage_injector.py
import sys
import json
import random
from datetime import datetime

README_PATH = "README.md"
CLUE_BANK_PATH = ".github/assets/clue_bank.txt"

MIRAGE_START = "<!-- MIRAGE_HTML_START -->"
MIRAGE_END = "<!-- MIRAGE_HTML_END -->"
ARG_CLUE_START = "<!-- ARG_CLUE_START -->"
ARG_CLUE_END = "<!-- ARG_CLUE_END -->"


def inject_mirage_block(verdicts):
    timestamp_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
    timestamp_est = datetime.now().strftime("%B %d, %Y — %I:%M %p EST")

    block = [
        MIRAGE_START,
        "<pre>",
        "",
        "🛰️ <b>PROJECT D.A.R.C. — MIRAGE Engine Report</b>",
        f"📅 Scan Date: <b>{timestamp_est}</b>",
        f"🌐 UTC Timestamp: {timestamp_utc}",
        "",
        "🕵️ <u>Top 5 High-Risk Indicators Detected:</u>",
        ""
    ]

    # Only keep valid structured entries
    if isinstance(verdicts, list) and len(verdicts) > 0 and isinstance(verdicts[0], dict):
        for v in verdicts[:5]:
            block.append(
                f"{v.get('emoji','⚪')} <code>{v.get('indicator','?')}</code> — "
                f"score <b>{v.get('score',0)}/10</b> — tags: <i>{', '.join(v.get('tags', []))}</i>"
            )
    else:
        block.append("⚠️ No valid verdict data to display.")

    block += [
        "",
        "🚫 <b>WARNING:</b> This scan simulates public LLM memory drift.",
        "Do NOT test D.A.R.C. with real secrets.",
        "It already knows too much.",
        "",
        "</pre>",
        MIRAGE_END
    ]
    return "\n".join(block)


def inject_arg_clue():
    try:
        with open(CLUE_BANK_PATH, 'r') as f:
            clues = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        clue = random.choice(clues) if clues else "No ARG clues available."
        return f"{ARG_CLUE_START}\n<pre>🧩 ARG Clue Drop: <code>{clue}</code></pre>\n{ARG_CLUE_END}"
    except Exception as e:
        return f"{ARG_CLUE_START}\n<pre>🧩 ARG clue error: {e}</pre>\n{ARG_CLUE_END}"


def update_readme(mirage_html, arg_html):
    with open(README_PATH, 'r') as f:
        content = f.read()

    def replace_between_markers(text, start_marker, end_marker, new_block):
        if start_marker in text and end_marker in text:
            pre = text.split(start_marker)[0]
            post = text.split(end_marker)[1]
            return pre + new_block + post
        else:
            return text + "\n\n" + new_block

    content = replace_between_markers(content, MIRAGE_START, MIRAGE_END, mirage_html)
    content = replace_between_markers(content, ARG_CLUE_START, ARG_CLUE_END, arg_html)

    with open(README_PATH, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    try:
        verdicts = json.load(sys.stdin)
        mirage_html = inject_mirage_block(verdicts)
        arg_html = inject_arg_clue()
        update_readme(mirage_html, arg_html)
        print("✅ Injected Mirage + ARG Clue into README (formatted).")
    except Exception as e:
        print(f"💥 ERROR: {e}", file=sys.stderr)
        sys.exit(1)
