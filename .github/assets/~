from datetime import datetime
from pathlib import Path

clue_file = Path('.github/assets/clue_bank.txt')
readme_path = Path('README.md')

with clue_file.open() as f:
    clues = [c.strip() for c in f if c.strip()]

# pick a clue based on current date
index = datetime.utcnow().toordinal() % len(clues)
clue = clues[index]

text = readme_path.read_text()
start_tag = '<!-- ARG_CLUE_START -->'
end_tag = '<!-- ARG_CLUE_END -->'
if start_tag not in text or end_tag not in text:
    raise RuntimeError("ARG clue markers not found in README")
before, rest = text.split(start_tag)
_, after = rest.split(end_tag)
new_clue_section = f'{start_tag}\n<pre>{clue}</pre>\n{end_tag}'
readme_path.write_text(before + new_clue_section + after)
