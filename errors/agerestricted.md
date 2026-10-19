# AgeRestricted

> This video is age-restricted. Therefore, you are unable to retrieve transcripts for it without authenticating yourself.

The library adds that cookie authentication is temporarily unsupported.

Raised by `youtube-transcript-api` (1.2.4 read) as `AgeRestricted`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17 (latest attempt 2026-10-19 was blocked)

## What it means

YouTube only serves this video to signed-in users, so an anonymous request gets no caption data.

## What triggers it

YouTube's playability status is `LOGIN_REQUIRED` and the reason is `This video may be inappropriate for some users.` (read from the library source)

## Reproduce

Video ID: `R8t0blHwhIQ`

```python
from youtube_transcript_api import YouTubeTranscriptApi
YouTubeTranscriptApi().fetch("R8t0blHwhIQ")
```

## What to do

- Check whether another tool can use your own signed-in browser session. yt-dlp documents `--cookies-from-browser`; use only an account you are allowed to use, since automated use of an account can be restricted by YouTube.
- Otherwise there is no anonymous route to that video's captions.

## In other tools

| Tool | What it prints | Observed |
|---|---|---|
| yt-dlp | `ERROR: [youtube] R8t0blHwhIQ: Sign in to confirm your age. Use --cookies-from-browser or --cookies for the authentication.` | 2026-10-17, home network, India |

## Related

- [RequestBlocked](requestblocked.md)
- [VideoUnplayable](videounplayable.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-19 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | AgeRestricted raised |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
