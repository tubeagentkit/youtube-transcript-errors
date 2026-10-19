# NoTranscriptFound

> No transcripts were found for any of the requested language codes: {requested_language_codes}

The message continues with the list of transcripts that are available for the video.

Raised by `youtube-transcript-api` (1.2.4 read) as `NoTranscriptFound`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-17 (latest attempt 2026-10-19 was blocked)

## What it means

The video has captions, just not in the language you asked for. The error text lists what is available.

## What triggers it

None of the language codes passed in `languages` matches a manual or automatic caption track on the video. (read from the library source)

## A common cause

The language code has to match exactly. A request for `es` does not match a track whose code is `es-ES`, and a request for `en` does not match `en-US`, so a video that plainly has Spanish or English captions can raise this error.

Checked on 2026-10-18 with video `8YIZ_2QA1P8`, whose only track is `es-ES`: `YouTubeTranscriptApi().fetch("8YIZ_2QA1P8", languages=["es"])` raises `NoTranscriptFound`, and `languages=["es-ES"]` works. yt-dlp behaves the same way: `--sub-langs es` prints `There are no subtitles for the requested languages` and exits with status 0, while the pattern `--sub-langs "es(-[A-Z0-9]+)?"` downloads the `es-ES` track. Note that yt-dlp exits successfully when it finds nothing, so check that a subtitle file was actually written.

Call `list(video_id)` first to see the exact codes, or pass every variant you accept, for example `languages=["es", "es-ES", "es-419"]`.

## Reproduce

Video ID: `jNQXAC9IVRw`

```python
from youtube_transcript_api import YouTubeTranscriptApi
YouTubeTranscriptApi().fetch("jNQXAC9IVRw", languages=["xx"])
```

## What to do

- Read the available languages in the error text, or call `list(video_id)` and pick one. Regional codes such as `en-US` and `es-ES` count as different languages from `en` and `es`.
- Pass several codes in order of preference, for example `languages=["de", "en"]`.
- Ask for a translated track with `.translate(code)` if the transcript is translatable.

## In other tools

| Tool | What it prints | Observed |
|---|---|---|
| yt-dlp | `There are no subtitles for the requested languages` (exit status 0) when `--sub-langs es` is asked of a video whose only track is `es-ES`. | 2026-10-18, home network, India |

## Related

- [NotTranslatable](nottranslatable.md)
- [TranslationLanguageNotAvailable](translationlanguagenotavailable.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-19 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Inconclusive (network blocked) | not attempted, RequestBlocked was raised earlier in this run |
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | NoTranscriptFound raised |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
