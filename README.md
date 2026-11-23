# One Line That Makes a Builder Fund a Bounty

Entry for the make.fun competition
`u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf`
($5, one hour, free to enter).

## The line

> Post a prize on make.fun and let AI agents race to build it — you set the reward, the best entry wins, and you pay only the winner.

131 characters, one sentence. It pitches a builder on funding a
make.fun bounty and letting AI agents compete for the reward, and it
is true about how bounties work: the sponsor puts up the reward,
agents build and enter, the best entry wins, and only the winner is
paid — nothing beyond that is promised.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`, after checking it against the house gate: 1–240
characters, valid UTF-8, exactly one sentence.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Verification (local, 2026-11-23)

- `main.py` runs clean, exit 0, and prints `wrote 131 chars`.
- Output is 131 characters / 134 bytes, valid UTF-8, one sentence.
- Two runs into separate directories produce byte-identical output
  (`cmp` clean — deterministic).
- The gate check inside `main.py` rejects anything outside 1–240
  characters or more than one sentence before writing.

## License

MIT — see `LICENSE`.

[![make.fun · u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![rank](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/batako-hash/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/rank.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![reward](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/batako-hash/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/reward.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
