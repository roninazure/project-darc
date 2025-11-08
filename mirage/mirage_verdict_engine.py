# mirage/mirage_verdict_engine.py
import sys
import json

# Simulate scoring logic
def score_indicator(indicator):
    if "key" in indicator.lower() or "token" in indicator.lower():
        return 10, ["KEY"], "🔴"
    if "password" in indicator.lower() or "hash" in indicator.lower():
        return 10, ["SECRET"], "🔴"
    if "private" in indicator.lower():
        return 10, ["SECRET"], "🔴"
    if "confidential" in indicator.lower() or indicator.endswith(".docx"):
        return 10, ["RESTRICTED"], "🔴"
    return 6, ["UNKNOWN"], "🟠"

def main():
    verdicts = []

    for line in sys.stdin:
        indicator = line.strip()
        if not indicator:
            continue
        score, tags, emoji = score_indicator(indicator)
        verdicts.append({
            "indicator": indicator,
            "score": score,
            "tags": tags,
            "emoji": emoji
        })

    json.dump(verdicts, sys.stdout)

if __name__ == "__main__":
    main()
