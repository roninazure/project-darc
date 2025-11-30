# .github/scripts/inject_clue_to_readme.py

from datetime import datetime
from pathlib import Path

# Determine repository root from the script location
# .resolve() gives the absolute path, .parents[2] goes up twice (scripts -> .github -> repo root)
repo_root = Path(__file__).resolve().parents[2]

clue_file = repo_root / '.github' / 'assets' / 'clue_bank.txt'
readme_path = repo_root / 'README.md'

# Load the clues
try:
    with clue_file.open(encoding='utf-8') as f:
        clues = [c.strip() for c in f if c.strip()]
except FileNotFoundError:
    raise RuntimeError(f"Clue file not found at {clue_file}")

if not clues:
    raise RuntimeError("No clues found in clue_bank.txt")

# Pick a clue deterministically based on the current date
index = datetime.utcnow().toordinal() % len(clues)
clue = clues[index]

# Read README.md and locate the markers
text = readme_path.read_text(encoding='utf-8')
start_tag = '<!-- ARG_CLUE_START -->'
end_tag = '<!-- ARG_CLUE_END -->'
if start_tag not in text or end_tag not in text:
    raise RuntimeError("ARG clue markers not found in README")

before, rest = text.split(start_tag, 1)
_, after = rest.split(end_tag, 1)

# Construct new clue section with consistent formatting
new_clue_section = f"{start_tag}\n<pre>{clue}</pre>\n{end_tag}"

# Write the updated README back to disk
readme_path.write_text(before + new_clue_section + after, encoding='utf-8')
print(f"[OK] Injected clue into README.md: {clue}")
