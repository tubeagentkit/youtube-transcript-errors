# FailedToCreateConsentCookie

> Failed to automatically give consent to saving cookies

Raised by `youtube-transcript-api` (1.2.4 read) as `FailedToCreateConsentCookie`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Not reproduced yet

## What it means

In some regions YouTube shows a cookie consent screen before serving the page.

## What triggers it

YouTube returned its cookie consent page (`consent.youtube.com`), the library could not extract the consent token, or the page still showed consent after the cookie was set. (read from the library source)

## Reproduce

Depends on the region of the requesting IP.

## What to do

- Run the request from a region without the consent page, or retry.
- Report it to the library with the region and video ID if it persists.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [YouTubeDataUnparsable](youtubedataunparsable.md)

## Verification history

No runs recorded yet. `verify/verify.py` records one when it can reproduce the error.

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
