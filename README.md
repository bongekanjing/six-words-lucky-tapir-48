# Six Words, One Story

A single six-word story — *He read his obituary, then shaved.* — with a tiny, deterministic writer that validates and emits it as `entry.txt`.

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

**1. A complete story, not a fragment.** One grammatical sentence with a compound
predicate: a subject, two things he did, in order. Strip the comma and it is still a
sentence. There is a before, a middle and an after, and the six words are exactly
six.

**2. The turn carries a life.** The hinge is "then". A man reads his own death
notice and answers it by shaving — not weeping, not raging, not calling a lawyer.
That one act implies a routine, a bathroom, a mirror, an age, and somewhere to be
afterward. The surprise is the calm of it.

**3. Every word pays rent.** "His" makes the obituary personal rather than
incidental; "then" is the turn and cannot be replaced by "and"; "shaved" is the
whole story in one concrete verb, where "dressed", "wept" or "left" would explain
instead of show. Nothing here is decoration.

**4. It reads cleanly aloud.** Five monosyllables around one long word, with the
comma as a beat and two hard stops at each end. No clause dangles, nothing needs
re-reading to parse.

**5. The silence does the work.** The page never says whether the notice was an
error, a threat, or something he wrote himself; whether he shaves to go correct the
record or to attend his own funeral; whether he is vain, defiant or simply a man who
will not be caught unkempt by death. The reader supplies all of it, and the last
word is still ringing when they do.
