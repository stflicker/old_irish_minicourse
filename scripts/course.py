"""Canonical markdown curriculum and lightweight course metadata."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
import re

START_JST = date(2026, 10, 10)

@dataclass(frozen=True)
class Entry:
    day: int
    book: str
    target: str
    track: str

    @property
    def lesson_id(self):
        return f"OI-D{self.day:03d}"

    @property
    def date_jst(self):
        return START_JST + timedelta(days=self.day-1)


def plain_md(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s)
    s = re.sub(r"(?<!\w)\*(?!\s)(.*?)(?<!\s)\*(?!\w)", r"\1", s)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    return s.strip()


def read_curriculum(path: Path) -> list[Entry]:
    """Read and validate the ORIGINAL FIRST_28_DAYS.md table; no side-car JSON."""
    source = path.read_text(encoding="utf-8")
    found = []
    for line in source.splitlines():
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) != 4:
            continue
        number = re.fullmatch(r"\*\*(\d{3})\*\*|(\d{3})", parts[0])
        if not number:
            continue
        found.append(Entry(day=int(number.group(1) or number.group(2)),
                           book=plain_md(parts[1]), target=plain_md(parts[2]),
                           track=plain_md(parts[3])))
    assert len(found) == 28, f"Expected 28 days in the MD, got {len(found)}"
    assert [x.day for x in found] == list(range(1,29)), "Day numbers must be exactly 001..028"
    return found


def today_jst() -> date:
    from datetime import datetime
    from zoneinfo import ZoneInfo
    return datetime.now(ZoneInfo("Asia/Tokyo")).date()


def entry_for_date(curriculum: list[Entry], now: date) -> Entry | None:
    number = (now - START_JST).days + 1
    if 1 <= number <= len(curriculum):
        return curriculum[number-1]
    return None