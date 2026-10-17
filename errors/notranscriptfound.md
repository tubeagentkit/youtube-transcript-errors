# NoTranscriptFound

> No transcripts were found for any of the requested language codes: {requested_language_codes}

The message continues with the list of transcripts that are available for the video.

Raised by `youtube-transcript-api` (1.2.4 read) as `NoTranscriptFound`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17

## What it means

The video has captions, just not in the language you asked for. The error text lists what is available.

## What triggers it

None of the language codes passed in `languages` matches a manual or automatic caption track on the video. (read from the library source)

## Reproduce

Video ID: `jNQXAC9IVRw`

```python
from youtube_transcript_api import YouTubeTranscriptApi
YouTubeTranscriptApi().fetch("jNQXAC9IVRw", languages=["xx"])
```

## What to do

- Read the available languages in the error text, or call `list(video_id)` and pick one.
- Pass several codes in order of preference, for example `languages=["de", "en"]`.
- Ask for a translated track with `.translate(code)` if the transcript is translatable.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [NotTranslatable](nottranslatable.md)
- [TranslationLanguageNotAvailable](translationlanguagenotavailable.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | NoTranscriptFound raised |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
