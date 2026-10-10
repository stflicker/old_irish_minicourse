"""Import learner-confirmed GitHub Issue feedback into canonical PROGRESS.md.

This is intentionally restricted to issue authors matching the repository owner.
The public site never holds a token; the learner explicitly submits the issue on GitHub.
"""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json
import os
import re

ROOT = Path(__file__).resolve().parents[1]
ROW = re.compile(r"^\|\s*(OI-D\d{3})\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*completed\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*$", re.M)

def main():
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise SystemExit("Requires a GitHub Issue event")
    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    issue = event.get("issue", {})
    owner = os.environ["GITHUB_REPOSITORY"].split("/", 1)[0]
    if issue.get("user", {}).get("login") != owner:
        print("Ignored: feedback must be confirmed by repository owner.")
        return
    title = issue.get("title", "")
    mt = re.fullmatch(r"\[Old Irish Feedback\] (OI-D\d{3})", title)
    if not mt:
        print("Ignored: not a study-feedback issue.")
        return
    matches = list(ROW.finditer(issue.get("body") or ""))
    if len(matches) != 1:
        raise SystemExit("Feedback issue must contain exactly one valid progress row")
    m = matches[0]
    lesson, day, mins, difficulty, note = [x.strip() for x in m.groups()]
    if lesson != mt.group(1):
        raise SystemExit("Lesson in issue title differs from progress row")
    date.fromisoformat(day)
    if mins not in ("—", "") and (not mins.isdigit() or not 1 <= int(mins) <= 180):
        raise SystemExit("Invalid minutes")
    if difficulty not in ("—", "") and (not difficulty.isdigit() or not 1 <= int(difficulty) <= 5):
        raise SystemExit("Invalid difficulty")
    if len(note) > 120:
        raise SystemExit("Note too long")
    progress = ROOT / "PROGRESS.md"
    lines = progress.read_text(encoding="utf-8").splitlines()
    row = "| " + " | ".join((lesson,day,"completed",mins or "—",difficulty or "—",note or "—")) + " |"
    for idx, line in enumerate(lines):
        if line.startswith("| " + lesson + " |"):
            lines[idx] = row
            break
    else:
        lines.append(row)
    progress.write_text("\n".join(lines).rstrip() + "\n",encoding="utf-8")
    print("Imported confirmed completion for", lesson)

if __name__ == "__main__":
    main()
