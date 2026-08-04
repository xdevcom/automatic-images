# python312-playwright

Python 3.12 + one pinned Playwright version + matching Chromium, baked into
the image at build time. Nothing inside Pterodactyl ever runs
`playwright install`.

## Why not a runtime install

Pterodactyl's startup command isn't a real shell for most eggs — chaining
`playwright install && python bot.py` is unreliable, and even when it runs,
`/ms-playwright` isn't guaranteed writable by the non-root `container` user.
The only reliable fix is: Chromium already exists in the image before the
container starts. That's what this image does.

## Tagging strategy

- One tag per Playwright version, matching the full `playwright_version`
  input exactly: `:1.61.0`, `:1.62.0`, `:1.63.1` — never mixed, never
  shortened to major.minor.
- `:latest` is optional and opt-in per build (`latest: true` input), so a bad
  build never silently becomes the default.
- Tag = `playwright==X.Y.Z` inside the image = Chromium downloaded by that
  exact Playwright release. The Dockerfile enforces this by installing pip
  and Chromium in the same `RUN` from the same `PLAYWRIGHT_VERSION` arg —
  there's no code path where they can drift apart.

## Release strategy

- Manual `workflow_dispatch` with a version input. Playwright ships new
  versions faster than most bots need them; auto-building every release adds
  CI cost for tags nobody pulls.
- When you do want automation later: a scheduled job that diffs
  `pip index versions playwright` against existing GHCR tags and opens a PR
  bumping a version file — add this when manually triggering becomes the
  actual bottleneck, not before.

## Security recommendations

- Runtime user is `container` (non-root), matching Pterodactyl's expectation
  — the egg never needs root.
- `apt-get clean` + removing `/var/lib/apt/lists` in the same layer that
  installs, so no stale package lists ship in the image.
- Don't add `curl`/`wget`/`git`/`jq` etc. unless the egg actually shells out
  to them — `playwright install --with-deps` already pulls every OS package
  Chromium itself needs. Extra CLI tools are attack surface with no image
  functionality behind them; add per-egg, not globally.
- Base image updates (`ghcr.io/ptero-eggs/yolks:python_3.12`) carry their own
  CVE fixes — rebuild on base image updates, not just Playwright bumps.

## Optimization notes

- Single-stage build. Multi-stage was considered, but Chromium's runtime
  needs its full shared-library set from `--with-deps`, and copying those
  between stages is fragile and error-prone to keep in sync — the image-size
  win is small and not worth the reproducibility risk. Revisit only if image
  size becomes a measured problem, not a hypothetical one.
- Everything (pip install, playwright install, apt cleanup) is one `RUN`
  layer, so no intermediate layer holds the apt cache.

## Maintenance

- Bump `PLAYWRIGHT_VERSION`, run the workflow, let the smoke test gate the
  push. That's the entire maintenance loop.
- Watch Playwright's release notes for Chromium version bumps that also need
  new system libraries — `--with-deps` handles this automatically since it
  queries Playwright's own dependency table at install time.

## Upgrade strategy for future Playwright releases

1. Pick the new version, trigger the workflow with `playwright_version` set.
2. Smoke test must pass (Chromium launches) before the tag is considered
   usable — the workflow doesn't gate the *push* on this today, so treat a
   failed smoke test as "don't point `:latest` here."
3. Old version tags are never overwritten — bots pin an exact tag in their
   egg config, so old tags must keep working after new ones ship.
