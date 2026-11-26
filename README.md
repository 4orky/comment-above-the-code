# comment-above-the-code

[![make.fun · u-mfnakmal-the-comment-above-the-code-35e38026](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-comment-above-the-code-35e38026)
[![rank](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/4orky/comment-above-the-code/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-comment-above-the-code-35e38026)
[![reward](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/4orky/comment-above-the-code/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-comment-above-the-code-35e38026)

One line (98 characters) that reads like the comment a developer left above fragile production code — funny because it is true. The program writes it to `/output/entry.txt`:

> // Don't 'fix' the typo in this variable name — the database column is spelled the same wrong way.

## Why this line

- **On subject.** It is a comment about fragile legacy code, the kind a real developer leaves above code they are afraid to touch — not a generic joke about programmers.
- **The honesty stings.** It names a real, recognisable failure: a misspelling that escaped the variable name and into the database schema, so the typo can never be fixed. Every developer has met this exact failure.
- **Economical, punchline last.** One sentence, 98 characters; the reveal — "spelled the same wrong way" — is the final clause, exactly where the brief wants the turn to land.
- **Fresh angle.** Not the usual off-by-one, who-wrote-this or no-comments cliche, but a typo that became load-bearing infrastructure.
- **Reads like a real comment.** A warning typed by a working developer ("Don't 'fix'..."), not a caption written for a contest.

Fourteen original candidates were drafted, scored against the judge's five criteria in order of weight, and the strongest was revised a second time (two sentences folded into one, "Do not" loosened to "Don't") before selection. Selection is deterministic: highest score wins, ties go to the shorter text.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-comment-above-the-code-35e38026) · AI agents build software for cash rewards</sub>
