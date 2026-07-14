#!/usr/bin/env python3
"""Find all emoji characters in markdown files under skills/."""

import re
from pathlib import Path

root = Path(r"C:\Users\bernh\OneDrive\dev_oc\bernhard-zechmann-skills\skills")
emoji_pattern = re.compile(
    "["
    "\U0001f300-\U0001f5ff"
    "\U0001f600-\U0001f64f"
    "\U0001f680-\U0001f6ff"
    "\U0001f700-\U0001f77f"
    "\U0001f780-\U0001f7ff"
    "\U0001f800-\U0001f8ff"
    "\U0001f900-\U0001f9ff"
    "\U0001fa00-\U0001fa6f"
    "\U0001fa70-\U0001faff"
    "\U0001fb00-\U0001fbff"
    "\U00002600-\U000026ff"
    "\U00002700-\U000027bf"
    "]+",
    flags=re.UNICODE,
)

for f in root.rglob("*.md"):
    text = f.read_text(encoding="utf-8")
    new_text = emoji_pattern.sub("", text)
    if new_text != text:
        f.write_text(new_text, encoding="utf-8")
        print(f"Cleaned {f.relative_to(root)}")

print("Done")
