"""
patch_readme_injectors.py

Auto-patch all known README injection scripts in the project-darc repo
by inserting a merge-conflict sanity check at the top of each file.
"""

import os

sanity_check_code = """# Sanity check to prevent corrupt README injection due to unresolved Git conflicts
readme_path = "README.md"
with open(readme_path, "r") as f:
    content = f.read()
if "<<<<<<< HEAD" in content or ">>>>>>>" in content:
    raise RuntimeError("🛑 README.md contains unresolved merge conflicts. Resolve them before running injection.")"""

injector_paths = ['.github/scripts/inject_mirage_to_readme.py', '.github/scripts/inject_report_to_readme.py', '.github/scripts/inject_clue_to_readme.py']

for path in injector_paths:
    print(f"Patching: {path}")
    if not os.path.exists(path):
        print(f"  ⚠️ Skipped (not found)")
        continue
    with open(path, "r") as f:
        content = f.read()
    if "README.md contains unresolved merge conflicts" in content:
        print("  ✅ Already patched")
        continue
    with open(path, "w") as f:
        f.write(sanity_check_code + "\n" + content)
    print("  ✅ Patch applied")

