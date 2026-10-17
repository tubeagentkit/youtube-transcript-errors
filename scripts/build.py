#!/usr/bin/env python3
"""Generate errors/*.md and the index table in README.md from data/errors.yaml and data/status.json.

Run from the repo root:  python scripts/build.py
Never edit errors/*.md or the table between the README markers by hand; edit the data files instead.
"""
import json
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = yaml.safe_load((ROOT / "data" / "errors.yaml").read_text(encoding="utf-8"))
STATUS_PATH = ROOT / "data" / "status.json"
STATUS = json.loads(STATUS_PATH.read_text(encoding="utf-8")) if STATUS_PATH.exists() else {}

TABLE_START = "<!-- errors-table:start -->"
TABLE_END = "<!-- errors-table:end -->"
RESULT_LABEL = {
    "reproduced": "Reproduced",
    "different": "Raised a different error",
    "blocked": "Inconclusive (network blocked)",
    "not_run": "Not run",
}
FOOTER = (
    "Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), "
    "a hosted transcript API. This page is about the tool in general. "
    "If something here is wrong or out of date, open an issue or a pull request and we will correct it."
)


def slug(name: str) -> str:
    return name.lower()


def status_line(name: str, err: dict) -> str:
    """Headline = the latest run that actually tested the repro; a later blocked attempt is noted, not hidden."""
    runs = STATUS.get(name, {}).get("runs", [])
    if err["repro"]["kind"] == "none":
        return "Cannot be triggered in this version (never raised in the source)"
    conclusive = next((r for r in runs if r["result"] in ("reproduced", "different")), None)
    if not conclusive:
        return "Inconclusive (network blocked)" if runs else "Not reproduced yet"
    line = f"{RESULT_LABEL[conclusive['result']]} on {conclusive['date']}"
    if runs[0] is not conclusive and runs[0]["result"] == "blocked":
        line += f" (latest attempt {runs[0]['date']} was blocked)"
    return line


def page(err: dict) -> str:
    name = err["name"]
    repro = err["repro"]
    out = [f"# {name}", ""]
    out.append(f"> {err['message']}")
    if err.get("message_detail"):
        out += ["", err["message_detail"]]
    out += [
        "",
        f"Raised by `{DATA['tool']}` ({DATA['tool_version_read']} read) as `{name}`, a subclass of `{err['base']}`.",
        "",
        f"**Status:** {status_line(name, err)}",
        "",
        "## What it means",
        "",
        err["meaning"],
        "",
        "## What triggers it",
        "",
        err["trigger"] + " (read from the library source)",
        "",
        "## Reproduce",
        "",
    ]
    if repro["kind"] == "video":
        out += [f"Video ID: `{repro['video_id']}`", "", "```python", repro["code"].rstrip(), "```"]
        if repro.get("caveat"):
            out += ["", f"Note: {repro['caveat']}"]
    else:
        out.append(repro["text"])
    out += ["", "## What to do", ""]
    out += [f"- {a}" for a in err["actions"]]
    out += ["", "## In other tools", ""]
    if err["other_tools"]:
        out += ["| Tool | What it prints | Observed |", "|---|---|---|"]
        for t in err["other_tools"]:
            seen = f"{t['date']}, {t['env']}" if t.get("verified") else "not verified here"
            out.append(f"| {t['tool']} | {t['text']} | {seen} |")
    else:
        out.append("Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.")
    out += ["", "## Related", ""]
    out += [f"- [{r}]({slug(r)}.md)" for r in err["related"]]
    runs = STATUS.get(name, {}).get("runs", [])
    out += ["", "## Verification history", ""]
    if runs:
        out += ["| Date | Environment | Library | Result | What was observed |", "|---|---|---|---|---|"]
        for r in runs:
            out.append(
                f"| {r['date']} | {r['env']} | {r['lib_version']} | {RESULT_LABEL.get(r['result'], r['result'])} | {r.get('observed', '')} |"
            )
    else:
        out.append("No runs recorded yet. `verify/verify.py` records one when it can reproduce the error.")
    out += ["", "---", "", FOOTER, ""]
    return "\n".join(out)


def table() -> str:
    rows = ["| Error | Base class | Status | Page |", "|---|---|---|---|"]
    for err in DATA["errors"]:
        n = err["name"]
        rows.append(f"| `{n}` | `{err['base']}` | {status_line(n, err)} | [{n}](errors/{slug(n)}.md) |")
    return "\n".join(rows)


def main() -> int:
    errors_dir = ROOT / "errors"
    errors_dir.mkdir(exist_ok=True)
    wanted = set()
    for err in DATA["errors"]:
        path = errors_dir / f"{slug(err['name'])}.md"
        path.write_text(page(err), encoding="utf-8")
        wanted.add(path.name)
    for stale in errors_dir.glob("*.md"):
        if stale.name not in wanted:
            stale.unlink()
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if TABLE_START not in text or TABLE_END not in text:
        print("README.md is missing the errors-table markers", file=sys.stderr)
        return 1
    head, rest = text.split(TABLE_START, 1)
    _, tail = rest.split(TABLE_END, 1)
    readme.write_text(f"{head}{TABLE_START}\n{table()}\n{TABLE_END}{tail}", encoding="utf-8")
    print(f"built {len(wanted)} pages and the README table")
    return 0


if __name__ == "__main__":
    sys.exit(main())
