# VideoUnplayable

> The video is unplayable for the following reason: {reason}

YouTube's own reason text follows, with extra detail when YouTube provides it.

Raised by `youtube-transcript-api` (1.2.4 read) as `VideoUnplayable`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17

## What it means

YouTube will not play the video to this client. Live streams that are not archived and premieres that have not started are common cases.

## What triggers it

YouTube's playability status is neither OK nor one of the cases handled by the more specific errors above. (read from the library source)

## Reproduce

Video ID: `jfKfPfyJRdk`

```python
from youtube_transcript_api import YouTubeTranscriptApi
YouTubeTranscriptApi().fetch("jfKfPfyJRdk")
```

Note: That ID is a 24/7 live stream. It can go offline or change, so this repro may stop working.

## What to do

- Read the reason text in the error; it is YouTube's wording.
- For a live stream, wait until it ends and the recording is processed.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [VideoUnavailable](videounavailable.md)
- [AgeRestricted](agerestricted.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | VideoUnplayable raised |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | VideoUnplayable raised for live stream jfKfPfyJRdk (reason text not recorded). |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
