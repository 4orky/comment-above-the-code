# The Comment Above the Code — make.fun bounty
# u-mfnakmal-the-comment-above-the-code-35e38026
#
# The program writes one comment line, at most 200 characters, to
# /output/entry.txt — the kind of line a developer leaves above fragile
# production code, funny because it is true.
#
# Candidates were drafted against the judge's brief, in order of weight:
#   1. on subject: a funny comment about fragile legacy code, the kind a
#      real developer leaves above code they are afraid to touch
#   2. the honesty stings: names a real, recognisable failure in the code
#      or the process, not a generic joke about programmers
#   3. economical, every word earning its place, with a turn or punchline
#      that lands on the last few words
#   4. fresh angle, not the usual off-by-one, who-wrote-this or
#      no-comments cliche
#   5. reads like a comment actually left in a codebase, in a working
#      developer's voice, not a caption written for a contest
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: subject 9, sting 8, economy 9, fresh 8, voice 9 = 43
    # Career-change punchline: refactoring this code ends careers.
    ("// Do not refactor. The last person who tried is now a farmer.",
     43),
    # score: subject 9, sting 7, economy 8, fresh 6, voice 8 = 38
    # "Nobody knows why / the author left" is the most worn angle here.
    ("// This function works. Nobody knows why, and the one person who "
     "did left in 2019.",
     38),
    # score: subject 9, sting 9, economy 8, fresh 9, voice 8 = 43
    # The sting is aimed at the test suite, not the code: the tests prove
    # nothing, and the writer knows it.
    ("// The tests pass. The tests also pass if you delete the entire "
     "function, which tells you everything.",
     43),
    # score: subject 9, sting 8, economy 8, fresh 7, voice 8 = 40
    # Blame lands on the merger, not the author; solid, but the 3am-call
    # setup is familiar.
    ("// If this breaks at 3am, do not call me. Call whoever approved "
     "merging it without tests.",
     40),
    # score: subject 9, sting 8, economy 9, fresh 9, voice 9 = 44
    # Magic number, forbidden experiment, and a punchline that refuses to
    # explain itself. Tight and true.
    ("// Yes, the magic number is 7. No, I don't know why. Yes, I tried "
     "8. We don't talk about 8.",
     44),
    # score: subject 9, sting 8, economy 8, fresh 8, voice 9 = 42
    # Promotion as escape route: the author did not fix the regex, they
    # got promoted away from it.
    ("// This regex was written by someone who has since been promoted "
     "far away from this code.",
     42),
    # score: subject 10, sting 9, economy 8, fresh 8, voice 9 = 44
    # Prod-only, Monday-only, important-customer-only: three recognisable
    # failure modes stacked into one sentence.
    ("// It only fails in production, only on Mondays, and only when the "
     "customer watching is the important one.",
     44),
    # score: subject 8, sting 7, economy 9, fresh 9, voice 8 = 41
    # Meta and fresh, but the joke is about commenting itself, not about
    # a failure in the code or the process.
    ("// I added a comment here once. The code deleted it. I have "
     "decided not to argue.",
     41),
    # score: subject 9, sting 8, economy 8, fresh 8, voice 8 = 41
    # Load-bearing spaghetti, but "400 lines" invites a length quibble
    # and the punchline is in the middle, not the end.
    ("// The function below is 400 lines long because every line is "
     "load-bearing and none of them is labelled.",
     41),
    # score: subject 9, sting 10, economy 10, fresh 9, voice 10 = 48
    # The winner (REVISED, second pass). First draft was two sentences:
    # "// Do not 'fix' the typo in the variable name. The database column
    # is spelled the same wrong way." Its weaknesses: the punchline took a
    # whole second sentence instead of landing on the last few words, and
    # "Do not" is stiffer than a working developer's voice. The revision
    # folds it into one sentence joined by an em dash, so the reveal —
    # "spelled the same wrong way" — is the final clause, and "Don't"
    # sounds like something actually typed above the code. A typo that
    # can never be fixed because the misspelling escaped into the schema:
    # every developer has met this exact failure.
    ("// Don't 'fix' the typo in this variable name \u2014 the database "
     "column is spelled the same wrong way.",
     48),
    # score: subject 9, sting 8, economy 8, fresh 7, voice 8 = 40
    # "Temporary since 2019" is a known trope; the second half saves it
    # but does not lift it above the winner.
    ("// This code has been 'temporary' since 2019. It now pays the "
     "salaries of everyone who calls it temporary.",
     40),
    # score: subject 9, sting 8, economy 8, fresh 8, voice 9 = 42
    # A TODO outliving companies and a marriage is a good image, but the
    # sting is about time passing, not about a failure.
    ("// The original author left a TODO here in 2016. The TODO has "
     "outlived two companies and one marriage.",
     42),
    # score: subject 9, sting 8, economy 8, fresh 8, voice 9 = 42
    # Reads like a real comment and the deploy-failure sting is true, but
    # "third person this week" is a weaker punch than the winner's.
    ("// If you are reading this, the deploy failed again and you are the "
     "third person this week to open this file.",
     42),
    # score: subject 8, sting 7, economy 8, fresh 8, voice 8 = 39
    # A joke about a vanished warning; clever, but the subject drifts
    # from the code's failure to the comment's own fate.
    ("// The comment above this one said 'do not touch'. That comment is "
     "gone now. So is the person who wrote it.",
     39),
]


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert text.startswith("//"), "candidate must read as a code comment"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written) <= 200, f"entry over gate: {len(written)} chars"
    print(written)
    print(f"({len(written)} characters)")


if __name__ == "__main__":
    main()
