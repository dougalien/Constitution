"""Find the parts of the Constitution, court cases and debates that answer a question.

A small BM25 keyword search, so it runs offline with no API key and only ever shows the real text.
Each passage is indexed on its title, keywords, plain-language explanation and original words,
with the title and keywords weighted most. Common everyday words are mapped to the words the
Constitution uses (for example "gun" also searches "arms").
"""

import math
import re
from collections import Counter

from constitution import PASSAGES
from learning import CASES, DEBATES

STOP = set(
    """a about above after again against all am an and any are as at be because been before being below between
    both but by can could did do does doing down during each few for from further had has have having he her here
    hers him his how i if in into is it its itself just me more most my no nor not now of off on once only or other
    our out over own same she should so some such than that the their them then there these they this those through
    to too under until up very was we were what when where which while who whom why will with would you your yours
    tell explain mean means meaning say says said constitution constitutional allowed allow allows let lets get gets
    happen happens anyone someone people person thing things us united america american class""".split()
)

# everyday word -> words the Constitution or its explanations use
SYNONYMS = {
    "gun": "arms firearms", "guns": "arms firearms", "weapon": "arms", "weapons": "arms",
    "cop": "police", "cops": "police", "phone": "cell phone search", "locker": "search school",
    "backpack": "search school", "lawyer": "counsel attorney", "attorney": "counsel lawyer",
    "silent": "self incrimination fifth", "jail": "prison bail punishment", "prison": "punishment",
    "slave": "slavery", "slaves": "slavery", "black": "race", "racial": "race", "racism": "race discrimination",
    "women": "sex suffrage", "woman": "sex suffrage", "girls": "sex", "vote": "voting suffrage election",
    "voting": "vote suffrage election", "elect": "election", "elected": "election", "18": "eighteen",
    "kid": "students", "kids": "students", "teen": "students", "teens": "students", "teenager": "students",
    "student": "students school", "school": "students school", "pray": "prayer religion",
    "god": "religion", "church": "religion", "religious": "religion", "faith": "religion",
    "fired": "remove removal", "kick": "remove removal expel", "kicked": "remove removal expel",
    "boss": "president", "potus": "president", "senator": "senate", "congressman": "house representative",
    "leader": "president speaker", "army": "military", "troops": "military army", "war": "war military",
    "money": "money taxes coin", "taxes": "tax", "taxed": "tax", "judge": "judges courts", "court": "courts",
    "protest": "assembly speech", "protesting": "assembly speech", "post": "speech social media",
    "online": "social media speech", "internet": "social media speech", "tiktok": "social media speech",
    "instagram": "social media speech", "snapchat": "social media speech", "flag": "flag burning",
    "citizen": "citizenship", "immigrant": "naturalization citizenship", "immigration": "naturalization",
    "born": "birthright citizenship", "abolish": "abolished", "change": "amend amendment",
    "changed": "amend amendment", "add": "amend amendment", "old": "age", "young": "age", "how old": "age",
    "term": "term years", "terms": "term years", "law": "laws legislative", "laws": "legislative",
    "privacy": "privacy search", "private": "privacy", "death": "death penalty", "execute": "death penalty",
    "torture": "cruel unusual punishment", "fair": "due process trial", "trial": "trial jury",
    "states": "state", "teacher": "school students", "teachers": "school students",
    "take": "taken takings eminent domain property", "house": "house home", "home": "house property",
    "print": "coin money", "justices": "justices nine judges", "arrested": "arrest accused police",
}


def _stem(word):
    for suffix in ("ments", "ment", "ings", "ing", "ies", "es", "s", "ed"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)] + ("y" if suffix == "ies" else "")
    return word


def tokens(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [_stem(w) for w in words if w not in STOP]


def query_tokens(question):
    words = re.findall(r"[a-z0-9]+", question.lower())
    out = []
    for w in words:
        if w in STOP:
            continue
        out.append(_stem(w))
        out.extend(tokens(SYNONYMS.get(w, "")))
    return out


class Index:
    """BM25 over a list of documents, each a list of (text, weight) fields."""

    def __init__(self, docs, k1=1.4, b=0.6):
        self.k1, self.b = k1, b
        self.tf = []
        for fields in docs:
            c = Counter()
            for text, weight in fields:
                for t in tokens(text):
                    c[t] += weight
            self.tf.append(c)
        self.lengths = [sum(c.values()) for c in self.tf]
        self.avg = sum(self.lengths) / max(len(self.lengths), 1)
        df = Counter(t for c in self.tf for t in c)
        n = len(self.tf)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def scores(self, qtokens):
        q = Counter(qtokens)
        out = []
        for c, length in zip(self.tf, self.lengths):
            s = 0.0
            for t, qn in q.items():
                f = c.get(t)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * length / self.avg)) * (1 + 0.3 * (qn - 1))
            out.append(s)
        return out


_PASSAGE_INDEX = Index([
    [(p["title"], 4), (p["label"], 3), (p["keywords"], 3), (p["plain"], 1), (p["text"], 1)] for p in PASSAGES
])
_CASE_INDEX = Index([
    [(c["name"], 3), (c["keywords"], 3), (c["topic"], 2), (c["question"], 1), (c["decision"], 1), (c["matters"], 1)]
    for c in CASES
])
_DEBATE_INDEX = Index([
    [(d["title"], 3), (d["keywords"], 3), (d["intro"], 1), (d["side_a"][1], 1), (d["side_b"][1], 1)] for d in DEBATES
])

_ORDINALS = {
    "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9,
    "tenth": 10, "eleventh": 11, "twelfth": 12, "thirteenth": 13, "fourteenth": 14, "fifteenth": 15,
    "sixteenth": 16, "seventeenth": 17, "eighteenth": 18, "nineteenth": 19, "twentieth": 20,
}
_ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7}


def _direct_hits(question):
    """Passages named outright, like "14th amendment", "second amendment" or "article ii section 2"."""
    q = question.lower()
    hits = []
    for m in re.finditer(r"\b(\d{1,2})(?:st|nd|rd|th)?\s+amendment", q):
        hits.append(f"am{int(m.group(1))}")
    for m in re.finditer(r"\b(twenty[\s-])?(" + "|".join(_ORDINALS) + r")\s+amendment", q):
        n = _ORDINALS[m.group(2)] + (20 if m.group(1) else 0)
        hits.append(f"am{n}")
    for m in re.finditer(r"amendment\s+(\d{1,2})\b", q):
        hits.append(f"am{int(m.group(1))}")
    for m in re.finditer(r"article\s+(\d|[ivx]+)\b(?:,?\s*section\s+(\d+))?", q):
        a = m.group(1)
        n = int(a) if a.isdigit() else _ROMAN.get(a)
        if not n:
            continue
        if m.group(2):
            hits.append(f"a{n}s{int(m.group(2))}")
        elif n >= 5:
            hits.append(f"a{n}")
        else:
            hits.append(f"a{n}s1")
    if "preamble" in q or "we the people" in q:
        hits.append("pre")
    if "bill of rights" in q:
        hits.extend(f"am{i}" for i in (1, 2, 4, 5, 6))
    ids = {p["id"] for p in PASSAGES}
    return [h for h in dict.fromkeys(hits) if h in ids]


def _top(scores, items, n, floor):
    best = max(scores) if scores else 0
    if best <= 0:
        return []
    ranked = sorted(range(len(items)), key=lambda i: -scores[i])
    return [items[i] for i in ranked[:n] if scores[i] >= max(floor, best * 0.35)]


def ask(question, n_passages=3, n_cases=3):
    """Return (passages, cases, debates) relevant to the question, best first."""
    q = query_tokens(question)
    by_id = {p["id"]: p for p in PASSAGES}
    direct = [by_id[i] for i in _direct_hits(question)]
    passages = list(direct)
    if q:
        for p in _top(_PASSAGE_INDEX.scores(q), PASSAGES, n_passages + 2, 1.0):
            if p not in passages:
                passages.append(p)
    passages = passages[: max(n_passages, len(direct))]

    cases = _related(_CASE_INDEX.scores(q) if q else [0.0] * len(CASES), CASES, passages, n_cases)
    debates = _related(_DEBATE_INDEX.scores(q) if q else [0.0] * len(DEBATES), DEBATES, passages, 1, strong=8.0)
    return passages, cases, debates


def _related(scores, items, passages, n, strong=8.0):
    """Items tied to the passages found (the first passage counts most), plus any that match the question strongly."""
    weights = {}
    for rank, p in enumerate(passages):
        weights.setdefault(p["id"], 3.0 if rank == 0 else 1.0)
    ranked = []
    for item, score in zip(items, scores):
        tie = max((weights.get(r, 0) for r in item["related"]), default=0)
        if (tie and score >= 1.5) or score >= strong:
            ranked.append((score + tie, item))
    ranked.sort(key=lambda x: -x[0])
    return [item for _, item in ranked[:n]]
