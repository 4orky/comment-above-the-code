#!/usr/bin/env python3
"""Write the single funniest comment for the code below it.

The brief asks for one line a working developer would actually leave
above fragile production code: at most two hundred characters, funny
because it names a failure that is true. Fourteen drafts were written
by hand, marked against five yardsticks in the order the brief ranks
them, and the strongest was polished once more before the program
picked it. The pick is deterministic, so repeated runs print the same
line, and the file it writes holds exactly that line, nothing extra.
"""

from pathlib import Path

OUT_FILE = Path("/output/entry.txt")
LIMIT = 200


DRAFTS = [
    {
        "line": "// The password is hardcoded. Rotating it is somebody else's problem now. It has always been somebody else's problem.",
        "topic": 9,
        "sting": 9,
        "tight": 8,
        "fresh": 8,
        "voice": 9,
        "note": "True and bleak, but the second sentence only repeats the first.",
    },
    {
        "line": "// This works because of a bug in the library. If they ever fix the library, we are all unemployed.",
        "topic": 9,
        "sting": 9,
        "tight": 9,
        "fresh": 9,
        "voice": 8,
        "note": "Strong sting, yet the punchline leans on a hypothetical rather than a fact.",
    },
    {
        "line": "// Do not run this on a Friday. Do not run this on a Monday. On reflection, do not run this.",
        "topic": 9,
        "sting": 7,
        "tight": 9,
        "fresh": 7,
        "voice": 9,
        "note": "A tidy triplet, but the joke is about scheduling, not about the code.",
    },
    {
        "line": "// The function is called doThing. It does six things, and none of them is the thing.",
        "topic": 9,
        "sting": 8,
        "tight": 9,
        "fresh": 8,
        "voice": 8,
        "note": "Every codebase has this function; the name gag carries the whole line.",
    },
    {
        "line": "// I tried to write a test for this. The test asked to speak to my manager.",
        "topic": 8,
        "sting": 7,
        "tight": 9,
        "fresh": 9,
        "voice": 8,
        "note": "Fresh image, but the sting lands on testing culture instead of this code.",
    },
    {
        "line": "// The comment that explained this died in a merge conflict. The merge won.",
        "topic": 8,
        "sting": 7,
        "tight": 8,
        "fresh": 8,
        "voice": 8,
        "note": "Short and sad, though it jokes about commenting rather than the failure.",
    },
    {
        "line": "// This endpoint returns 200 when it fails. The frontend reads the error message, which is in Italian.",
        "topic": 9,
        "sting": 9,
        "tight": 8,
        "fresh": 9,
        "voice": 8,
        "note": "Two real failures stacked; the Italian detail is the part people remember.",
    },
    {
        "line": "// Someone added a sleep(3) here in 2018 to fix a race condition. Removing it summons the race condition.",
        "topic": 9,
        "sting": 9,
        "tight": 8,
        "fresh": 9,
        "voice": 9,
        "note": "A ritual nobody dares disturb; close to the winner, but the setup is longer.",
    },
    {
        "line": "// The code below is correct. It is also the reason we cannot upgrade anything.",
        "topic": 9,
        "sting": 8,
        "tight": 9,
        "fresh": 7,
        "voice": 8,
        "note": "Correctness as a trap is a good turn, yet the second half states the obvious.",
    },
    {
        "line": "// If you are refactoring this, stop. The last refactor took payments down for four hours.",
        "topic": 9,
        "sting": 9,
        "tight": 8,
        "fresh": 7,
        "voice": 9,
        "note": "A warning with a body count, but the refactor-gone-wrong angle is familiar.",
    },
    {
        "line": "// Nobody owns this file. Four teams deny owning it. It deploys itself every Tuesday.",
        "topic": 9,
        "sting": 8,
        "tight": 8,
        "fresh": 9,
        "voice": 9,
        "note": "Ownership denial is recognisable; the Tuesday detail earns its place.",
    },
    {
        "line": "// Changing this number breaks the invoice page. I know because I changed it once, in 2021.",
        "topic": 9,
        "sting": 9,
        "tight": 8,
        "fresh": 8,
        "voice": 9,
        "note": "Confessional and specific, though the wound is one number, not the system.",
    },
    {
        "line": "// The original author wrote 'do not touch' and then touched it. The git blame is a crime scene.",
        "topic": 9,
        "sting": 8,
        "tight": 8,
        "fresh": 8,
        "voice": 9,
        "note": "Blame as forensics is a nice image; the first half does most of the work.",
    },
    {
        "line": "// Don't 'fix' the typo in this variable name — the database column is spelled the same wrong way.",
        "topic": 10,
        "sting": 10,
        "tight": 9,
        "fresh": 9,
        "voice": 10,
        "note": "The winner, after its second pass. First written as two short sentences, it was joined with an em dash so the reveal lands on the final words, and the stiff opening gave way to a spoken Don't. A misspelling that escaped into the schema can never be repaired, which is why the warning has to stay.",
    },
]  # fourteen drafts, one winner


def total_marks(draft):
    return (
        draft["topic"]
        + draft["sting"]
        + draft["tight"]
        + draft["fresh"]
        + draft["voice"]
    )


def choose(drafts):
    ranked = sorted(
        drafts, key=lambda d: (total_marks(d), -len(d["line"])), reverse=True
    )
    return ranked[0]["line"]


def check_line(line):
    if not line.startswith("//"):
        raise ValueError("entry must open with //, like a code comment")
    if not 1 <= len(line) <= LIMIT:
        raise ValueError(f"entry is {len(line)} characters, limit is {LIMIT}")


def emit():
    picked = choose(DRAFTS)
    check_line(picked)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(picked, encoding="utf-8")
    back_bytes = OUT_FILE.read_bytes()
    if back_bytes != picked.encode("utf-8"):
        raise SystemExit("round-trip mismatch: entry.txt bytes are not the chosen line")
    back = back_bytes.decode("utf-8")
    check_line(back)
    print(picked)
    print(f"({len(picked)} characters)")


emit()
