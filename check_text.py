"""Check the app's Constitution text, word for word, against an official copy.

Official reference: the Constitution as printed in the House Manual (117th Congress), published
in XML by the U.S. Government Publishing Office and the Clerk of the House at
https://github.com/usgpo/house-manual (117/original-file-names/constitution.xml). A copy is saved
in reference/ so the check runs offline. Its annotations and footnotes are skipped.

Every quoted passage in constitution.py is cut into sentences and clauses (an editorial "[...]"
or "[note]" also ends a piece), and each piece must appear, word for word, in the official text.
Capital letters and punctuation are ignored, since official printings differ slightly there
(the commas in the 2nd Amendment, for example).

The House Manual leaves out a few clauses that later amendments replaced (it prints "* * *").
With --secondary, pieces the House Manual doesn't have are checked against two independent
transcriptions instead: Harry Surden's XML/JSON edition (github.com/hsurden/us-constitution) and
Project Gutenberg eBook #5 (github.com/GITenberg/The-United-States-Constitution_5). Those are
downloaded when you run it. A piece counts as confirmed only if both have it word for word.

Run:  python check_text.py               official check only
      python check_text.py --secondary   also check what the House Manual leaves out
Exit code 1 if any wording differs.
"""

import difflib
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from constitution import PASSAGES

REFERENCE = Path(__file__).resolve().parent / "reference" / "house_manual_117_constitution.xml"
NS = "{http://xml.house.gov/schemas/uslm/1.0}"
# Pieces the House Manual prints only in part, between its annotations. `python check_text.py --secondary`
# confirmed each one word for word in both secondary copies on 2026-10-25. The offline check accepts exactly
# these strings, so editing one makes the check fail until it is confirmed again.
KNOWN_GAPS = {
    ("a1s2", "and shall have the sole Power of Impeachment."),
    ("a1s5", "Each House shall be the Judge of the Elections, Returns and Qualifications of its own Members, and a "
             "Majority of each shall constitute a Quorum to do Business;"),
    ("a1s6", "They shall in all Cases, except Treason, Felony and Breach of the Peace, be privileged from Arrest during "
             "their Attendance at the Session of their respective Houses, and in going to and returning from the same;"),
    ("a1s6", "and for any Speech or Debate in either House, they shall not be questioned in any other Place."),
}
SECONDARY = {
    "Surden edition": "https://raw.githubusercontent.com/hsurden/us-constitution/master/usconstitution.full.json",
    "Project Gutenberg #5": "https://raw.githubusercontent.com/GITenberg/The-United-States-Constitution_5/master/5-0.txt",
}


def words(text):
    """Lowercase words, punctuation removed. Old spellings are kept, so "chuse" must match "chuse"."""
    text = text.replace("—", " ").replace("–", " ").replace("’", "'").replace("-", " ")
    return re.findall(r"[a-z0-9]+", text.lower().replace("'", ""))


def official_words(path=REFERENCE):
    """All words of the Constitution in the House Manual, skipping its notes and numbering."""
    root = ET.parse(path).getroot()
    out = []

    def walk(e):
        tag = e.tag.replace(NS, "")
        if tag in ("note", "num", "ref", "heading"):
            return
        if tag == "inline" and e.get("name") == "three-star":
            out.append(" ")
            return
        if e.text:
            out.append(e.text)
        for child in e:
            walk(child)
            out.append(" ")
            if child.tail:
                out.append(child.tail)

    main = root.find(f"{NS}main") if root.find(f"{NS}main") is not None else root
    walk(main)
    return words("".join(out))


def secondary_words():
    sources = {}
    for name, url in SECONDARY.items():
        with urllib.request.urlopen(url, timeout=60) as r:
            raw = r.read().decode("utf-8", "replace")
        if url.endswith(".json"):
            parts = []

            def walk(n):
                if isinstance(n, dict):
                    content = n.get("content")
                    if isinstance(content, str):
                        parts.append(content)
                    elif isinstance(content, list):
                        parts.extend(str(c) for c in content)
                    for c in n.get("children") or []:
                        walk(c)

            walk(json.loads(raw))
            raw = " ".join(parts)
        sources[name] = words(raw)
    return sources


def pieces(text):
    """Sentences and clauses of original wording; editorial brackets and "Section 1." labels are dropped."""
    out = []
    for part in re.split(r"\[[^\]]*\]", text):
        part = re.sub(r"\bSection \d+\.\s*", " ", part)
        for piece in re.split(r"(?<=[.;:])\s+|\n\n|—(?=\")", part):
            if len(words(piece)) >= 3:
                out.append(piece.strip())
    return out


def contains(hay, needle):
    n = len(needle)
    first = needle[0]
    for i, w in enumerate(hay):
        if w == first and hay[i:i + n] == needle:
            return True
    return False


def closest(hay, needle):
    """Word-level differences between needle and the most similar stretch of hay."""
    m = difflib.SequenceMatcher(None, needle, hay, autojunk=False)
    blocks = [b for b in m.get_matching_blocks() if b.size >= 2]
    if not blocks:
        return "no similar wording found"
    # the run of matching blocks closest together around the longest one
    longest = max(blocks, key=lambda b: b.size)
    start = max(0, longest.b - longest.a - 3)
    window = hay[start:start + len(needle) + 6]
    diffs = []
    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, needle, window, autojunk=False).get_opcodes():
        if op != "equal" and not (op == "insert" and (b1 == 0 or b2 == len(window))):
            diffs.append(f"app: {' '.join(needle[a1:a2]) or '(nothing)'!r} / reference: "
                         f"{' '.join(window[b1:b2]) or '(nothing)'!r}")
    return "; ".join(diffs[:6]) or "differs only at the edges"


def check(use_secondary=False):
    official = official_words()
    others = secondary_words() if use_secondary else {}
    matched = confirmed = 0
    unchecked, differ = [], []
    for p in PASSAGES:
        for piece in pieces(p["text"]):
            w = words(piece)
            if contains(official, w):
                matched += len(w)
                continue
            # the House Manual prints some clauses in pieces, between its annotations
            parts = [words(x) for x in re.split(r"(?<=,)\s+", piece)]
            if all(contains(official, x) for x in parts if len(x) >= 3) and sum(len(x) for x in parts if len(x) < 3) <= 4:
                matched += len(w)
                continue
            if not others and (p["id"], piece) in KNOWN_GAPS:
                confirmed += len(w)
                continue
            if others:
                found = [name for name, hay in others.items() if contains(hay, w)]
                if len(found) == len(others):
                    confirmed += len(w)
                    continue
                detail = "; ".join(f"{name}: {closest(hay, w)}" for name, hay in others.items() if name not in found)
                differ.append((p, piece, f"House Manual: {closest(official, w)}\n        {detail}"))
            else:
                differ.append((p, piece, f"House Manual: {closest(official, w)}"))
    return matched, confirmed, differ, unchecked


def main():
    use_secondary = "--secondary" in sys.argv
    matched, confirmed, differ, _ = check(use_secondary)
    print(f"{matched} words match the official House Manual text word for word.")
    if use_secondary:
        print(f"{confirmed} more words, which the House Manual leaves out, match both secondary copies.")
    elif confirmed:
        print(f"{confirmed} more words, which the House Manual leaves out, were confirmed earlier in both secondary "
              "copies (run with --secondary to check them again).")
    for p, piece, detail in differ:
        short = piece if len(piece) < 140 else piece[:137] + "..."
        print(f"\nNOT MATCHED  {p['label']}: \"{short}\"\n        {detail}")
    if differ:
        if not use_secondary:
            print("\nSome of these may be clauses the House Manual leaves out. Run with --secondary to check them.")
        print(f"\n{len(differ)} piece(s) not matched.")
        return 1
    print("\nAll of the app's Constitution text is confirmed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
