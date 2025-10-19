import os
import json
from datetime import date, timedelta

from dateutil import parser as dparser
from .config import OUTPUT_DIR

os.makedirs(OUTPUT_DIR, exist_ok=True)


def dates_for_when(which):
    """Return list of date objects for "today", "tomorrow", or "both".
    If "which" looks like YYYY-MM-DD, parse and return single date.
    """
    today = date.today()
    if which == "today":
        return [today]
    if which == "tomorrow":
        return [today + timedelta(days=1)]
    if which == "both":
        return [today, today + timedelta(days=1)]
    # try parse
    try:
        return [dparser.parse(which).date()]
    except Exception:
        return [today]


def save_json(filename, data):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path
