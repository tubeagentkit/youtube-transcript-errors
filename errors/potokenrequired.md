# PoTokenRequired

> The requested video cannot be retrieved without a PO Token. If this happens, please open a GitHub issue!

Raised by `youtube-transcript-api` (1.2.4 read) as `PoTokenRequired`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Not reproduced yet

## What it means

For this track YouTube expects a proof-of-origin token that the library does not produce.

## What triggers it

The caption track URL contains `&exp=xpe`. (read from the library source)

## Reproduce

Reported by users for some videos. No stable video ID recorded yet. See the library's issue tracker, for example https://github.com/jdepoix/youtube-transcript-api/issues/592.

## What to do

- Check the library's open issues for the current state.
- Try another tool or a signed-in browser session to see whether the track is available at all.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [YouTubeRequestFailed](youtuberequestfailed.md)

## Verification history

No runs recorded yet. `verify/verify.py` records one when it can reproduce the error.

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
