# InvalidVideoId

> You provided an invalid video id. Make sure you are using the video id and NOT the url!

Raised by `youtube-transcript-api` (1.2.4 read) as `InvalidVideoId`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17 (latest attempt 2026-10-26 was blocked)

## What it means

A full URL was passed where the library wants the 11-character video ID.

## What triggers it

Same condition as VideoUnavailable, but the ID passed in starts with `http://` or `https://`. (read from the library source)

## Reproduce

Video ID: `jNQXAC9IVRw`

```python
from youtube_transcript_api import YouTubeTranscriptApi
YouTubeTranscriptApi().fetch("https://www.youtube.com/watch?v=jNQXAC9IVRw")
```

## What to do

- Pass only the ID: `fetch("jNQXAC9IVRw")`.
- Extract the ID from user input before calling (`v=` parameter, `youtu.be/` path, `/shorts/` path).

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [VideoUnavailable](videounavailable.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-26 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-19 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | InvalidVideoId raised |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
