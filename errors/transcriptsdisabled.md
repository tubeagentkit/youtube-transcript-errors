# TranscriptsDisabled

> Subtitles are disabled for this video

Raised by `youtube-transcript-api` (1.2.4 read) as `TranscriptsDisabled`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17 (latest attempt 2026-10-26 was blocked)

## What it means

YouTube is not offering any caption track for this video to this client. If the page in a browser shows no "Show transcript" button either, there is nothing for any tool to fetch.

## What triggers it

The video's player data has no caption track list (`playerCaptionsTracklistRenderer` is missing, or has no `captionTracks`). (read from the library source)

## Reproduce

Video ID: `XqZsoesa55w`

```python
from youtube_transcript_api import YouTubeTranscriptApi
YouTubeTranscriptApi().fetch("XqZsoesa55w")
```

Note: yt-dlp reports a different error for the same ID (see below), so the two tools disagree about this video. Treat it as a repro of the library's behaviour, not as proof that the video has captions disabled.

## What to do

- Open the video in a browser and look for "Show transcript". If it is missing, no caption data exists to fetch.
- If you still need text, transcribe the audio with a speech-to-text tool.
- If it is shown in the browser but the library raises this, try again later or from another network and compare with another tool.

## In other tools

| Tool | What it prints | Observed |
|---|---|---|
| yt-dlp | `ERROR: [youtube] XqZsoesa55w: This video is not available` | 2026-10-17, home network, India |

## Related

- [NoTranscriptFound](notranscriptfound.md)
- [VideoUnavailable](videounavailable.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-26 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | RequestBlocked raised instead |
| 2026-10-19 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | RequestBlocked raised instead |
| 2026-10-17 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | RequestBlocked raised instead |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | TranscriptsDisabled raised |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | TranscriptsDisabled raised for video XqZsoesa55w. yt-dlp printed 'This video is not available' for the same ID. |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
