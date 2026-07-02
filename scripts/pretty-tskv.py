#!/usr/bin/env python3
import sys
import re

COLORS = {
    "DEBUG": "\033[90m",
    "INFO": "\033[32m",
    "WARNING": "\033[33m",
    "ERROR": "\033[31m",
    "CRITICAL": "\033[35m",
}
RESET = "\033[0m"
BOLD = "\033[1m"

def parse_tskv(line: str):
    parts = line.rstrip("\n").split("\t")
    if not parts or parts[0] != "tskv":
        return None

    data = {}
    for part in parts[1:]:
        if "=" in part:
            key, value = part.split("=", 1)
            data[key] = value
    return data

for line in sys.stdin:
    data = parse_tskv(line)

    if data is None:
        print(line, end="", flush=True)
        continue

    ts = data.get("timestamp", "")
    level = data.get("level", "")
    module = data.get("module", "")
    component = data.get("component_name", "")
    text = data.get("text", "")

    text = text.replace("\\n", "\n    ")

    color = COLORS.get(level, "")
    level_str = f"{color}{BOLD}{level:<7}{RESET}" if level else ""

    left = f"{ts} {level_str}"

    if component:
        left += f" [{component}]"

    if module:
        left += f" {module}"

    print(left, flush=True)

    if text:
        print(f"    {text}", flush=True)

    # полезные поля, если есть
    extras = []
    for key in ("trace_id", "span_id", "peer.address", "db.instance", "db.type"):
        if key in data and data[key]:
            extras.append(f"{key}={data[key]}")

    if extras:
        print(f"    {' '.join(extras)}", flush=True)

    print(flush=True)