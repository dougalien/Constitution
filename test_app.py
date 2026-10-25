"""Checks for the content and the question search. Run: python test_app.py"""

from constitution import BY_ID, PARTS, PASSAGES
from learning import CASES, DEBATES, FACTS, QUIZ
from search import ask

# every passage is complete and every part of the document is present
for p in PASSAGES:
    for field in ("id", "label", "title", "text", "plain", "keywords"):
        assert p.get(field), (p.get("id"), field)
assert len([p for p in PASSAGES if p["id"].startswith("am")]) == 27
assert sorted(i for _, ids in PARTS for i in ids) == sorted(BY_ID)

# cross references point at real passages and cases
case_names = {c["name"] for c in CASES}
for item in CASES + DEBATES:
    for r in item["related"]:
        assert r in BY_ID, (item.get("name") or item["title"], r)
for d in DEBATES:
    for name in d["cases"]:
        assert name in case_names, name
for q, choices, right, why in QUIZ:
    assert 0 <= right < len(choices) and why, q
assert len(FACTS) >= 20

# the search finds the right part for common questions
EXPECT = {
    "What does the Constitution say about the post office?": "a1s8",
    "How old do you have to be to be President?": "a2s1",
    "Can police search my phone?": "am4",
    "Do I have free speech at school?": "am1",
    "How does a bill become a law?": "a1s7",
    "How do you change the Constitution?": "a5",
    "What happens if the President dies?": "am25",
    "What about guns?": "am2",
    "14th amendment": "am14",
    "second amendment": "am2",
    "Article II, Section 2": "a2s2",
    "Who can vote at 18?": "am26",
    "Is someone born here a citizen?": "am14",
    "Can women vote?": "am19",
    "Can the government take my house?": "am5",
    "Can a state print its own money?": "a1s10",
    "term limits for the president": "am22",
    "What is the preamble?": "pre",
    "Can the president be impeached?": "a2s4",
    "Who decides if we go to war?": "a1s8",
    "Can the President pardon anyone?": "a2s2",
}
for question, want in EXPECT.items():
    passages, _, _ = ask(question)
    assert passages and passages[0]["id"] == want, (question, [p["id"] for p in passages])
assert ask("Can my school search my backpack?")[1][0]["name"] == "New Jersey v. T.L.O."
assert ask("xyzzy") == ([], [], [])

# every passage, case and debate links to primary sources
from sources import OPINIONS, case_sources, debate_sources, passage_sources
for p in PASSAGES:
    assert len(passage_sources(p)) >= 2, p["id"]
for c in CASES:
    assert c["name"] in OPINIONS, c["name"]
for d in DEBATES:
    assert debate_sources(d), d["title"]
    assert all(u.startswith("https://") for _, u in debate_sources(d))

# hand-written answers: quotes are real, passages exist, and common questions find the right answer
from answers import FAQ
from search import match_faq
for f in FAQ:
    assert f["passages"] and all(pid in BY_ID for pid in f["passages"]), f["asks"][0]
    assert f["quote"] in BY_ID[f["passages"][0]]["text"], ("quote not in text", f["asks"][0])
    assert all(n in case_names for n in f.get("cases", [])), f["asks"][0]
    for a in f["asks"]:
        assert match_faq(a) is f, ("ask matches another answer", a, (match_faq(a) or {}).get("asks"))
ANSWERS = {
    "can government take my land?": "Can the government take my land?",
    "when can government take my land?": "When can the government take my land?",
    "can cops search my phone": "Can police search my phone?",
    "Can my teacher take my phone?": "Can my school search my backpack?",
    "can the government take away my guns": "Can I own a gun?",
    "How long can a president serve?": "How long is a President's term?",
}
for question, first_ask in ANSWERS.items():
    f = match_faq(question)
    assert f and f["asks"][0] == first_ask, (question, f and f["asks"][0])
assert match_faq("who signed the declaration of independence") is None
assert match_faq("What does the Constitution say about the post office?") is None  # "post" is not "post online"

# the optional AI answer stays off without a key, and only sees the matching passages
import os
import ai_answer
os.environ.pop("ANTHROPIC_API_KEY", None)
assert not ai_answer.enabled() and ai_answer.answer("Can a state print money?", [BY_ID["a1s10"]]) is None
prompt = ai_answer.build_prompt("Can a state print money?", [BY_ID["a1s10"]])
assert BY_ID["a1s10"]["text"] in prompt and "Can a state print money?" in prompt

# the Constitution text matches the official House Manual copy word for word
import check_text
assert not check_text.check()[2], "text differs from the official copy: run python check_text.py"

print(f"OK: {len(PASSAGES)} passages, {len(CASES)} cases, {len(DEBATES)} debates, {len(FACTS)} facts, "
      f"{len(QUIZ)} quiz questions, {len(EXPECT)} search checks")
