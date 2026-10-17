# CookieError

> (no message defined)

Raised by `youtube-transcript-api` (1.2.4 read) as `CookieError`, a subclass of `YouTubeTranscriptApiException`.

**Status:** Cannot be triggered in this version (never raised in the source)

## What it means

Left over from the cookie-based authentication of the 0.x versions. In 1.2.4 the AgeRestricted message says cookie authentication is temporarily unsupported.

## What triggers it

Defined in `_errors.py` but never raised anywhere in the 14 source files of version 1.2.4. (read from the library source)

## Reproduce

Cannot be triggered in 1.2.4.

## What to do

- Do not write code that depends on catching it.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [CookieInvalid](cookieinvalid.md)
- [CookiePathInvalid](cookiepathinvalid.md)
- [AgeRestricted](agerestricted.md)

## Verification history

No runs recorded yet. `verify/verify.py` records one when it can reproduce the error.

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
