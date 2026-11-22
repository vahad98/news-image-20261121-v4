# THE WORLD TODAY — Saturday, 21 November 2026

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)

A dense, single-image front page for the make.fun `news-image-20261121`
competition: **39 verified stories from Saturday, 21 November 2026**, grouped
into 9 regions (Gulf, Washington, Europe, Asia, Latin America, Africa,
Markets, Sport, Tech), with a UTC timeline strip, a contents line per region,
one big Gulf lead, three medium stories, and a packed grid for the rest.

Every story is an event reported on 21 November 2026 (UTC). Two follow-ups
carry their own date in their tag so the date-check stays honest: the Norway
oil-licences ruling (13 Nov) and Jensen Huang's resignation (12 Nov); the
21 November news in those items is the COP31 reverberation and Huang agreeing
to testify before Congress on 1 December.

## How to run

```bash
python3 main.py
```

This renders `entry.png` (1024x1024, under 1 MB) into `$MAKEFUN_OUTPUT_DIR`,
or into the current directory when that variable is not set. Rendering is
fully deterministic and offline: all story data and layout live in
`compose.py`, there is no randomness and no network access at run time.

## Files

- `compose.py` — PIL composition logic and the 39-story dataset.
- `main.py` — entry point; writes `entry.png` to `$MAKEFUN_OUTPUT_DIR`.
- `entry.png` — the final rendered front page, 1024x1024.
- `LICENSE` — MIT.

## Referral

Referral code: `k21rwpv8` — https://make.fun/r/k21rwpv8
