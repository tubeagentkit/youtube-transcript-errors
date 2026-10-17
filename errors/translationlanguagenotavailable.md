# TranslationLanguageNotAvailable

> The requested translation language is not available

Raised by `youtube-transcript-api` (1.2.4 read) as `TranslationLanguageNotAvailable`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17

## What it means

The track can be translated, but not into that language.

## What triggers it

`translate(language_code)` was called with a code that is not in the track's translation language list. (read from the library source)

## Reproduce

Video ID: `aircAruvnKk`

```python
from youtube_transcript_api import YouTubeTranscriptApi
track = YouTubeTranscriptApi().list("aircAruvnKk").find_transcript(["en"])
track.translate("xx").fetch()
```

## What to do

- Read `transcript.translation_languages` for the codes the track supports.
- The set of languages YouTube offers can differ between videos and over time, so do not hard-code it.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [NotTranslatable](nottranslatable.md)
- [NoTranscriptFound](notranscriptfound.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | TranslationLanguageNotAvailable raised |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
