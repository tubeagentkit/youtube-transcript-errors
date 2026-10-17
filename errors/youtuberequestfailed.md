# YouTubeRequestFailed

> Request to YouTube failed: {reason}

Raised by `youtube-transcript-api` (1.2.4 read) as `YouTubeRequestFailed`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Not reproduced yet

## What it means

A network or HTTP-level failure, for example 403, 5xx, or a proxy error.

## What triggers it

A request returned an HTTP error status other than 429 (429 is reported as IpBlocked). (read from the library source)

## Reproduce

Depends on the network and any proxy in between.

## What to do

- Read the status code in the reason. A 403 behaves like a block, a 5xx is usually temporary.
- If you use a proxy, test the proxy on its own first.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [IpBlocked](ipblocked.md)
- [PoTokenRequired](potokenrequired.md)

## Verification history

No runs recorded yet. `verify/verify.py` records one when it can reproduce the error.

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
