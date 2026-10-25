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
print(f"OK: {len(PASSAGES)} passages, {len(CASES)} cases, {len(DEBATES)} debates, {len(FACTS)} facts, "
      f"{len(QUIZ)} quiz questions, {len(EXPECT)} search checks")
