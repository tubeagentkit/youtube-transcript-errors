# YouTube transcript errors explained

What each error from a YouTube transcript library means, what triggers it, how to reproduce it, and what to do about it. Each page is named after the exact error string, so you can search for it.

Covered so far: every error class in [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) 1.2.4 (17 concrete error classes: 14 that can be raised and 3 legacy cookie classes that never are, plus two base classes). What yt-dlp prints is added where it was observed. Other tools are welcome by pull request.

## Errors

<!-- errors-table:start -->
| Error | Base class | Status | Page |
|---|---|---|---|
| `IpBlocked` | `RequestBlocked` | Reproduced on 2026-10-17 | [IpBlocked](errors/ipblocked.md) |
| `RequestBlocked` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 | [RequestBlocked](errors/requestblocked.md) |
| `TranscriptsDisabled` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked) | [TranscriptsDisabled](errors/transcriptsdisabled.md) |
| `NoTranscriptFound` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked) | [NoTranscriptFound](errors/notranscriptfound.md) |
| `NotTranslatable` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked) | [NotTranslatable](errors/nottranslatable.md) |
| `TranslationLanguageNotAvailable` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked) | [TranslationLanguageNotAvailable](errors/translationlanguagenotavailable.md) |
| `AgeRestricted` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked) | [AgeRestricted](errors/agerestricted.md) |
| `PoTokenRequired` | `CouldNotRetrieveTranscript` | Not reproduced yet | [PoTokenRequired](errors/potokenrequired.md) |
| `VideoUnavailable` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked) | [VideoUnavailable](errors/videounavailable.md) |
| `InvalidVideoId` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked) | [InvalidVideoId](errors/invalidvideoid.md) |
| `VideoUnplayable` | `CouldNotRetrieveTranscript` | Reproduced on 2026-10-17 (latest attempt 2026-10-17 was blocked) | [VideoUnplayable](errors/videounplayable.md) |
| `YouTubeRequestFailed` | `CouldNotRetrieveTranscript` | Not reproduced yet | [YouTubeRequestFailed](errors/youtuberequestfailed.md) |
| `YouTubeDataUnparsable` | `CouldNotRetrieveTranscript` | Not reproduced yet | [YouTubeDataUnparsable](errors/youtubedataunparsable.md) |
| `FailedToCreateConsentCookie` | `CouldNotRetrieveTranscript` | Not reproduced yet | [FailedToCreateConsentCookie](errors/failedtocreateconsentcookie.md) |
| `CookieError` | `YouTubeTranscriptApiException` | Cannot be triggered in this version (never raised in the source) | [CookieError](errors/cookieerror.md) |
| `CookieInvalid` | `CookieError` | Cannot be triggered in this version (never raised in the source) | [CookieInvalid](errors/cookieinvalid.md) |
| `CookiePathInvalid` | `CookieError` | Cannot be triggered in this version (never raised in the source) | [CookiePathInvalid](errors/cookiepathinvalid.md) |
<!-- errors-table:end -->

"Status" says whether the repro still produces that error, and when it was last checked. A repro that depends on one video can stop working when the video changes, which is why every claim carries a date. Details on each page, under "Verification history".

## When YouTube blocks your requests

The most common failures (`IpBlocked`, `RequestBlocked`) say something about the network the request came from, not about the video. In rough order of effort:

1. Wait and retry later with a back-off instead of a tight loop. How long a block lasts varies: on one home IP we saw a block lift after roughly 25 minutes and return soon after requests resumed at about ten a minute, so slow down well below that.
2. Run from a different network. A home or office connection is treated differently from a cloud server.
3. Send requests through a proxy provider. [youtube-transcript-api supports proxy configuration](https://github.com/jdepoix/youtube-transcript-api#working-around-ip-bans-requestblocked-or-ipblocked-exception).
4. Cache what you fetch and fetch each video once.
5. If the video has no captions at all, transcribe the audio with a speech-to-text tool instead.
6. Use a hosted transcript service, so the blocked IP is not yours. Several exist, for example Supadata, TranscriptAPI, youtube-transcript.io and GetYouTubeTranscript (run by the maintainers of this repository).
7. YouTube's official Data API has a captions endpoint, but it needs OAuth with the `youtube.force-ssl` scope, and in practice works for captions on videos the authorised account can edit.

## How the repros are verified

`verify/verify.py` runs the automated repros one at a time, pausing between requests, and stops at the first IP block instead of retrying. It records the date, the network ("home network, India", "GitHub Actions runner") and the library version in `data/status.json`. A GitHub Actions workflow runs it weekly. Results from a cloud runner are often blocked; that is a result too, and it is recorded as such, not hidden.

Pages and this table are generated from `data/errors.yaml` and `data/status.json` by `python scripts/build.py`. Edit those two files, not the generated pages. A check on every pull request fails if the pages are out of sync.

## Contributing

Corrections are welcome, including from the maintainers of any tool mentioned. See [CONTRIBUTING.md](CONTRIBUTING.md). Facts need a source: a line of the tool's source, an output you captured (with date and network), or a link.

## Who maintains this

The team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API, which is one of the options listed above. This repository describes the tools in general and takes pull requests from anyone. MIT licensed.
