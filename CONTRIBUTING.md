# Contributing

Thanks for helping keep this accurate. A few rules keep it useful:

1. **Every fact needs a source.** One of: a line in the tool's source code (give the file and version), output you captured yourself (give the date and the network, for example "home network, India" or "GitHub Actions runner"), or a link to documentation.
2. **Edit the data, not the pages.** Change `data/errors.yaml` (the explanations) or `data/status.json` (what was observed). Then run `pip install pyyaml` and `python scripts/build.py`, and commit the regenerated files. CI fails if the pages are out of sync.
3. **Observations are dated.** If you re-run a repro and the result changed, add a run to `data/status.json` instead of overwriting the old one.
4. **Stay tool-neutral.** Describe what a tool prints and what the options are. No rankings, no "best" claims. Hosted services are listed alphabetically-ish and with the same level of detail.
5. **No circumvention recipes.** Describe causes and legitimate options (wait, change network, proxy provider, caching, official APIs, hosted services). Do not add instructions for defeating YouTube's protections or for scraping at volume.
6. **Do not paste transcript text.** Use video IDs and error classes only.
7. **Be gentle with YouTube.** Repros are small and slow on purpose. Do not add loops or bulk checks.

## Adding another tool

Add an entry under `other_tools` on the relevant errors (what it prints, `verified: true` only if you captured it, with `date` and `env`). For a whole new library, add a new section to `data/errors.yaml` following the existing structure and open an issue first if it is large.

## Correcting a vendor or maintainer statement

If you maintain a tool mentioned here and we got it wrong, open an issue or a pull request with the correct statement and a source. We will merge it.
