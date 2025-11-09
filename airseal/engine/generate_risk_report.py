import json
from pathlib import Path
from datetime import datetime

store_data_path = Path("airseal/data/fake_stores.json")
report_path = Path("airseal/reports/scan_report.md")

def generate_risk_report():
    with store_data_path.open("r") as f:
        stores = json.load(f)

    # Sort by risk_score descending
    stores = sorted(stores, key=lambda x: x["risk_score"], reverse=True)

    now = datetime.utcnow().strftime("%B %d, %Y — %H:%M UTC")
    markdown = [
        "🛡️ <b>AIRSeal AI Risk Security Report</b>",
        f"📅 Scan Date: <b>{now}</b><br>",
        "🌐 Target: <i>Fictitious eCommerce Stores</i><br><br>",
        "🚨 <u>Top 10 Risky Stores Detected:</u><br><br>",
        "<ol>"
    ]

    for s in stores[:10]:
        name = s["store_id"]
        domain = s["domain"]
        score = s["risk_score"]
        tags = ", ".join(s.get("leak_tags", []))
        trace = "🧠" if s.get("llm_trace") else "🕳️"
        markdown.append(
            f"<li>{trace} <code>{name}</code> — {domain} — score <b>{score}/10</b> — tags: <i>{tags}</i></li>"
        )

    markdown.append("</ol>")
    markdown.append("<br><b>Disclaimer:</b> This is a demo scan. No real store data is used.<br>")

    report_path.write_text("\n".join(markdown))
    print(f"✅ Report generated: {report_path}")

if __name__ == "__main__":
    generate_risk_report()
