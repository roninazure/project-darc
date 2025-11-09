import json
from pathlib import Path

# Load fake store metadata
STORE_PATH = Path(__file__).resolve().parent.parent / "data" / "fake_stores.json"
REPORT_PATH = Path(__file__).resolve().parent.parent / "reports" / "scan_report.json"

RISK_TAGS = {
    "llm": 4,
    "openai": 5,
    "chatgpt": 5,
    "api": 3,
    "key": 4,
    "secret": 5,
    "leak": 5,
    "exposed": 4,
    "token": 4,
    "auth": 3,
    "public": 2,
    "env": 3,
    "debug": 2,
    "test": 1
}


def load_store_data():
    with STORE_PATH.open("r") as f:
        return json.load(f)


def score_store(store):
    name = store.get("name", "")
    meta = json.dumps(store).lower()
    score = 0
    tags = []

    for tag, weight in RISK_TAGS.items():
        if tag in meta:
            score += weight
            tags.append(tag)

    return {
        "store": store.get("name", "Unknown"),
        "score": score,
        "tags": sorted(set(tags)),
        "domain": store.get("domain", "N/A"),
        "platform": store.get("platform", "Shopify")
    }


def run_scan():
    stores = load_store_data()
    results = [score_store(s) for s in stores]
    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    REPORT_PATH.parent.mkdir(exist_ok=True)
    with REPORT_PATH.open("w") as f:
        json.dump(ranked, f, indent=2)

    return ranked


if __name__ == "__main__":
    report = run_scan()
    for r in report[:10]:
        print(f"🔍 {r['store']} — Score: {r['score']} — Tags: {', '.join(r['tags'])}")
