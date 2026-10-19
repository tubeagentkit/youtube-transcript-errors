# RequestBlocked

> YouTube is blocking requests from your IP.

Same text as IpBlocked. IpBlocked is a subclass of RequestBlocked.

Raised by `youtube-transcript-api` (1.2.4 read) as `RequestBlocked`, a subclass of `CouldNotRetrieveTranscript`.

**Status:** Reproduced on 2026-10-19

## What it means

YouTube decided the request looks automated and asked for a signed-in session. This is a bot check, not a problem with the video.

## What triggers it

YouTube's playability status is `LOGIN_REQUIRED` and the reason is `Sign in to confirm you’re not a bot`. (read from the library source)

## Reproduce

Environment dependent, like IpBlocked. Not reproducible on demand.

## What to do

- Same options as IpBlocked: wait, change network, use a proxy provider, cache, or use a hosted service.

## In other tools

Nothing recorded yet. If you know what another tool prints for this situation, please add it with a source.

## Related

- [IpBlocked](ipblocked.md)
- [AgeRestricted](agerestricted.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-19 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Reproduced | raised while trying the TranscriptsDisabled repro |
| 2026-10-17 | GitHub Actions runner (ubuntu-latest, hosted cloud IP) | 1.2.4 | Reproduced | raised while trying the TranscriptsDisabled repro |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
