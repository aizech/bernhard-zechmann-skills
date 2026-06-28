#!/usr/bin/env python3
"""Find all emoji characters in markdown files under skills/."""

import re
from pathlib import Path

root = Path(r"C:\Users\bernh\OneDrive\dev_oc\bernhard-zechmann-skills\skills")
emoji_pattern = re.compile(
    "["
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U0001FB00-\U0001FBFF"
    "\U00002600-\U000026FF"
    "\U00002700-\U000027BF"
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
