# IpBlocked

> YouTube is blocking requests from your IP.

The library's message goes on to list the usual causes: too many requests from the IP, or requests coming from a cloud provider IP (AWS, Google Cloud Platform, Azure and similar).

Raised by `youtube-transcript-api` (1.2.4 read) as `IpBlocked`, a subclass of `RequestBlocked`.

**Status:** Reproduced on 2026-10-17

## What it means

YouTube refused to serve this IP address. The video itself may be perfectly fine and fetchable from another network.

## What triggers it

YouTube answers with HTTP 429, or the page it returns contains a reCAPTCHA form (`class="g-recaptcha"`). (read from the library source)

## Reproduce

No fixed video reproduces it. It depends on the network the request comes from: send enough requests from one IP, or run from a datacenter IP.

## What to do

- Stop and wait. Blocks on a single IP often lift after some hours, so back off instead of retrying in a loop.
- Run the code from a different network, for example a home or office connection instead of a cloud server.
- Send the requests through a proxy provider. The library supports proxy configuration.
- Cache what you already fetched and fetch each video once.
- Use a hosted transcript service so the blocked IP is not yours (see the list in the README).

## In other tools

| Tool | What it prints | Observed |
|---|---|---|
| yt-dlp | Bot checks surface as `Sign in to confirm you're not a bot` (HTTP 429 and sign-in walls are reported differently from the library). | not verified here |

## Related

- [RequestBlocked](requestblocked.md)
- [YouTubeRequestFailed](youtuberequestfailed.md)

## Verification history

| Date | Environment | Library | Result | What was observed |
|---|---|---|---|---|
| 2026-10-17 | home network, India (residential) | 1.2.4 | Reproduced | IpBlocked raised for two videos after about a day of repeated test requests from the same IP. yt-dlp still fetched subtitles from that IP at the same time. The block had lifted a few hours later. |

---

Maintained by the team behind [GetYouTubeTranscript](https://getyoutubetranscript.com), a hosted transcript API. This page is about the tool in general. If something here is wrong or out of date, open an issue or a pull request and we will correct it.
