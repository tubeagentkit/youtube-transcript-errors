# NotTranslatable

> The requested language is not translatable

Raised by `youtube-transcript-api` (1.2.4 read) as `NotTranslatable`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked)

## What it means

That caption track does not offer machine translation.

## What triggers it

`translate()` was called on a transcript whose list of translation languages is empty. (read from the library source)

## Reproduce

Video ID: `jNQXAC9IVRw`

```python
from youtube_transcript_api import YouTubeTranscriptApi
track = YouTubeTranscriptApi().list("jNQXAC9IVRw").find_transcript(["en"])
track.translate("de")
```

## What to do

- Check `transcript.is_translatable` before calling `translate()`.
- Fetch another track, or translate the text yourself.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [TranslationLanguageNotAvailable](translationlanguagenotavailable.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-17 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | NotTranslatable raised |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
