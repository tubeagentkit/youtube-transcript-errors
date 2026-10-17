# YouTubeDataUnparsable

> The data required to fetch the transcript is not parsable. This should not happen, please open an issue (make sure to include the video ID)!

Raised by `youtube-transcript-api` (1.2.4 read) as `YouTubeDataUnparsable`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Not reproduced yet

## What it means

YouTube served something the parser does not recognise: a changed page layout, or a block page in a form the library does not detect.

## What triggers it

The page was fetched, but an embedded API key value that the library searches the page for is not in it, and the page is not the reCAPTCHA page. (read from the library source)

## Reproduce

Not reproducible on demand.

## What to do

- Open an issue on the library's tracker with the video ID, as the message says.
- Retry later or from another network, in case it was a block page.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [IpBlocked](ipblocked.md)
- [YouTubeRequestFailed](youtuberequestfailed.md)

## Verification history

No runs recorded yet. `verify/verify.py` records one when it can reproduce the error.

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
