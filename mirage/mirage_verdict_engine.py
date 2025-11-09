# mirage/mirage_verdict_engine.py
import sys
import json

def score_indicator(indicator):
    """Assigns risk scores, tags, and emojis based on indicator content."""
    ind_lower = indicator.lower()
    if "key" in ind_lower or "token" in ind_lower:
        return 10, ["KEY"], "🔴"
    if "password" in ind_lower or "hash" in ind_lower:
        return 10, ["SECRET"], "🔴"
    if "private" in ind_lower:
        return 10, ["SECRET"], "🔴"
    if "confidential" in ind_lower or ind_lower.endswith(".docx"):
        return 10, ["RESTRICTED"], "🔴"
    if "db" in ind_lower or "database" in ind_lower:
        return 8, ["DATABASE"], "🟠"
    if "vault" in ind_lower or "proxy" in ind_lower or "node" in ind_lower:
        return 7, ["INFRA"], "🟡"
    return 6, ["UNKNOWN"], "⚪"


def main():
    """Reads newline-delimited JSON objects from stdin and outputs a JSON list."""
    verdicts = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            # Each line is a JSON object from mirage_trace_probe
            entry = json.loads(line)
            indicator = entry.get("indicator", "UNKNOWN")
        except json.JSONDecodeError:
            # fallback if line isn’t valid JSON
            indicator = line

        score, tags, emoji = score_indicator(indicator)
        verdicts.append({
            "indicator": indicator,
            "score": score,
            "tags": tags,
            "emoji": emoji
        })

    # Output a clean JSON list, not nested blobs
    print(json.dumps(verdicts, indent=2))


if __name__ == "__main__":
    main()
