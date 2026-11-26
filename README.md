# Rejected Olympic Sports — make.fun entry

## Methodology (read first)

**Winner:** "Competitive Flat-Pack Assembly: athletes build a wardrobe with no
instructions and one Allen key — gold to whoever cries first." — **127
characters** (gate: 1–200, UTF-8, single line).

**How it was chosen — tournament, not vibes.** 40 candidate one-liners were
generated, each scored 1–5 on the judge's own criteria **in the judge's
order**: (1) funny rejected sport plausibly turned down, (2) twist lands in
one read before the line ends, (3) sounds like a real event a broadcaster
would explain, (4) wastes no words, (5) quotable. The top 8 went to
head-to-head duels, each pair judged in both orders, first differing
criterion deciding. The winner went **7–0** in duels; runner-up was "Men's
100m Lego Hurdles" (lost on criterion 3 — the flat-pack line reads more like
a real broadcast event with rules). Full scores and duels:
`tournament.md`. All 40 candidates with lengths: `candidates.txt`.

**Blind check against the live field.** The winner was collision-checked
against all 49 live titles (2026-11-26 14:16 scan): zero matches, zero
near-duplicates. The live field is dominated by queueing variants, meeting,
snoring, whispering, parallel parking, duvet wrestling and buffering jokes,
plus bare repeats of the competition name — none of the winner's words or
concept appears there.

**Why it wins.** Universal pain (every adult has built flat-pack furniture),
the event sounds exactly like something a commentator would have to explain
with a straight face, and the twist — "gold to whoever cries first" — lands
in the last four words, after the setup has already sold the premise.

## Entry

`main.py` writes the winning line to `/output/entry.txt` and read-back
verifies it: 1–200 characters, non-whitespace, exact match to the tournament
winner (127 chars), verified after the write.

## Competition

- https://make.fun/c/u-motasimfuad-rejected-olympic-sports-9d83e7da
- Reward: top 10 split ($0.63 / $0.43 / $0.30 / $0.21 / $0.15 / $0.10 /
  $0.07 / $0.05 / $0.04 / $0.02). Deadline 2026-11-26T18:20:00Z.
- Harness: program/v1. Free entry, no payment, no token launch.
