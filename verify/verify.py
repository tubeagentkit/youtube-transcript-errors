#!/usr/bin/env python3
"""Re-run the automated repros and record what happened in data/status.json.

    VERIFY_ENV="GitHub Actions runner (ubuntu)" python verify/verify.py

VERIFY_ENV is required: results mean nothing without saying which network they came from.
The script is deliberately slow and small: one request at a time, a pause between requests,
and it stops at the first IP block instead of retrying.
"""
import datetime
import importlib.metadata
import json
import os
import pathlib
import sys
import time

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import _errors as errors

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATUS_PATH = ROOT / "data" / "status.json"
PAUSE_SECONDS = 6

# Keep these in step with the `repro.code` blocks in data/errors.yaml.
CASES = {
    "TranscriptsDisabled": lambda api: api.fetch("XqZsoesa55w"),
    "VideoUnavailable": lambda api: api.fetch("aaaaaaaaaaa"),
    "InvalidVideoId": lambda api: api.fetch("https://www.youtube.com/watch?v=jNQXAC9IVRw"),
    "VideoUnplayable": lambda api: api.fetch("jfKfPfyJRdk"),
    "NoTranscriptFound": lambda api: api.fetch("jNQXAC9IVRw", languages=["xx"]),
    "NotTranslatable": lambda api: api.list("jNQXAC9IVRw").find_transcript(["en"]).translate("de"),
    "TranslationLanguageNotAvailable": lambda api: api.list("aircAruvnKk").find_transcript(["en"]).translate("xx"),
    "AgeRestricted": lambda api: api.fetch("R8t0blHwhIQ"),
}


def record(status: dict, name: str, run: dict) -> None:
    runs = status.setdefault(name, {"runs": []})["runs"]
    runs.insert(0, run)
    del runs[20:]


def main() -> int:
    env = os.environ.get("VERIFY_ENV", "").strip()
    if not env:
        print("Set VERIFY_ENV to describe the network, e.g. VERIFY_ENV='home network, India'", file=sys.stderr)
        return 2
    status = json.loads(STATUS_PATH.read_text(encoding="utf-8")) if STATUS_PATH.exists() else {}
    base = {
        "date": datetime.datetime.now(datetime.timezone.utc).date().isoformat(),
        "env": env,
        "lib_version": importlib.metadata.version("youtube-transcript-api"),
    }
    api = YouTubeTranscriptApi()
    stopped_by = None
    for name, call in CASES.items():
        if stopped_by:
            record(status, name, {**base, "result": "blocked", "observed": f"not attempted, {stopped_by} was raised earlier in this run"})
            continue
        try:
            call(api)
            run = {**base, "result": "different", "observed": "no error was raised"}
        except Exception as exc:  # the whole point is to classify whatever comes out
            got = type(exc).__name__
            if got == name:
                run = {**base, "result": "reproduced", "observed": f"{got} raised"}
            elif isinstance(exc, errors.RequestBlocked):
                run = {**base, "result": "blocked", "observed": f"{got} raised instead"}
                record(status, got, {**base, "result": "reproduced", "observed": f"raised while trying the {name} repro"})
                stopped_by = got
            else:
                run = {**base, "result": "different", "observed": f"{got} raised instead"}
        record(status, name, run)
        print(f"{name:34} {run['result']:11} {run['observed']}")
        time.sleep(PAUSE_SECONDS)
    STATUS_PATH.write_text(json.dumps(status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
