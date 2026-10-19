# VideoUnavailable

> The video is no longer available

Raised by `youtube-transcript-api` (1.2.4 read) as `VideoUnavailable`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17 (latest attempt 2026-10-19 was blocked)

## What it means

No such public video: it was deleted, made private, blocked in the region, or the ID is wrong.

## What triggers it

YouTube reports status `ERROR` with the reason `This video is unavailable`, and the ID passed in does not start with `http://` or `https://`. (read from the library source)

## Reproduce

Video ID: `aaaaaaaaaaa`

```python
from youtube_transcript_api import YouTubeTranscriptApi
YouTubeTranscriptApi().fetch("aaaaaaaaaaa")
```

## What to do

- Check the ID: it is the 11 characters after `v=` in a watch URL.
- Open the video in a browser from the same region.

## In other tools

| Tool | What it prints | Observed |
|---|---|---|
| yt-dlp | `ERROR: [youtube] aaaaaaaaaaa: This video is unavailable` | 2026-10-17, home network, India |

## Related

- [InvalidVideoId](invalidvideoid.md)
- [VideoUnplayable](videounplayable.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-19 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | VideoUnavailable raised |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | VideoUnavailable raised for ID aaaaaaaaaaa. |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
