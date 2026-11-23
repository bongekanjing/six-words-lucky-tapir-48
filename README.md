# Six Words, One Story

A single six-word story — *He wrote her obituary, then shaved.* — with a tiny, deterministic writer that validates and emits it as `entry.txt`.

[![Six Words, One Story](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![Rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/bongekanjing/six-words-lucky-tapir-48/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![Reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/bongekanjing/six-words-lucky-tapir-48/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)

## Run it

```
MAKEFUN_OUTPUT_DIR=./out python3 -P -s main.py
```

That writes `./out/entry.txt` and prints one line with the character count. If
`MAKEFUN_OUTPUT_DIR` is unset, the file lands in the current directory. The script
creates the directory if it is missing, uses only the standard library, and touches
no network, clock or randomness, so repeated runs are byte-identical.

Run the self-test with:

```
python3 -P -s test_entry.py
```

## Why these six words work

**1. A complete story, not a fragment.** Subject, verb, object, then a second act:
`He wrote her obituary, then shaved.` Six words, one sentence, two ordered
events. There is a before, a hinge and an after, and nothing is left dangling.

**2. Two turns, not one.** The first is `wrote`. A man who *reads* his own death
notice is a man surprised by the world; a man who *writes* one is doing something
to it. The second is the object: `her`. Six words in, and the story has handed you
a second person it never introduces, a death it never confirms, and a hand that
committed the notice to paper. Then he shaves — not weeps, not confesses, not
flees. The calm is the surprise, and it arrives twice.

**3. Every word pays rent.** `wrote` carries agency where `read` carried only
reception, and it costs the same one syllable. `her` is a whole relationship in
three letters, and it is the word doing the most work in the sentence. `then` is
the turn and cannot become `and`. `shaved` is the story in one concrete verb:
`dressed`, `wept`, `prayed`, `left` all explain the feeling, and this one only
shows the act. Nothing here is decoration.

**4. It reads cleanly aloud.** Ten syllables, five of them in the one long word,
with the comma as a beat and a hard stop at each end. No clause dangles and
nothing needs re-reading to parse.

**5. The silence does the work.** The page never says whether she is dead, dying,
or merely the subject of a notice he wrote too early; whether he is a widower, a
caregiver, or something worse; whether the shave is for her funeral, for the
mirror, or for the police. It never says why a man shaves after writing an
obituary — only that he does, and that the razor is the only thing in the story he
still controls. The reader supplies all of it, and the last word is still ringing
when they do.
