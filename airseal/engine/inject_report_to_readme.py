from pathlib import Path

report_path = Path("airseal/reports/scan_report.md")
readme_path = Path("README.md")

START_MARKER = "<!-- AIRSEAL_BLOCK_START -->"
END_MARKER = "<!-- AIRSEAL_BLOCK_END -->"

def inject():
    if not report_path.exists():
        print("❌ scan_report.md not found.")
        return

    new_block = report_path.read_text()

    if not readme_path.exists():
        print("❌ README.md not found.")
        return

    readme_content = readme_path.read_text()

    if START_MARKER not in readme_content or END_MARKER not in readme_content:
        print("❌ AIRSEAL markers not found in README.md.")
        return

    updated = readme_content.split(START_MARKER)[0] + START_MARKER + "\n\n" + new_block + "\n\n" + END_MARKER + readme_content.split(END_MARKER)[1]
    readme_path.write_text(updated)
    print("✅ AIRSeal block injected into README.md")

if __name__ == "__main__":
    inject()
