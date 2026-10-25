"""Constitution Explorer: learn the U.S. Constitution by asking questions.

Ask anything and the app shows the parts of the Constitution that answer it, each followed by a
plain-language explanation, plus the Supreme Court cases and debates connected to it. There are
also tabs to read the whole document, browse landmark cases, weigh both sides of big debates,
take a quiz and get random fun facts. Written for high school students and up.

The text is in constitution.py, cases, debates, facts and quiz in learning.py, and the
question search in search.py. It runs offline, with no API key.

Run: streamlit run app.py
"""

import random

import streamlit as st

import dougalien_brand as brand
from constitution import BY_ID, PARTS
from learning import CASES, DEBATES, FACTS, QUIZ
from search import ask

EXAMPLES = [
    "How old do you have to be to be President?",
    "Can my school search my backpack?",
    "Do I have free speech at school?",
    "How does a bill become a law?",
    "Who decides if we go to war?",
    "What happens if the President dies?",
    "Can police search my phone?",
    "How do you change the Constitution?",
]
QUIZ_LENGTH = 5
CASE_BY_NAME = {c["name"]: c for c in CASES}

st.set_page_config(page_title="Constitution Explorer", layout="wide", page_icon=brand.page_icon("📜"))
brand.apply_branding()

st.html(
    f"""
<style>
.plain {{ background: {brand.SAND_TINT}; border-left: 4px solid {brand.SLATE}; padding: 0.7rem 1rem;
          border-radius: 4px; margin: 0.3rem 0 0.8rem 0; color: {brand.INK}; }}
.plain b {{ color: {brand.SLATE}; }}
.fact {{ background: {brand.SHEET}; border: 1px solid {brand.RULE}; border-left: 5px solid {brand.RUST};
         padding: 0.8rem 1.1rem; border-radius: 4px; color: {brand.INK}; font-size: 1.05rem; }}
.fact .tag {{ color: {brand.RUST}; font-weight: 700; letter-spacing: 0.04em; font-size: 0.8rem;
              text-transform: uppercase; display: block; margin-bottom: 0.2rem; }}
.stApp blockquote, .stApp blockquote p {{ color: {brand.CAPTION} !important; font-family: Georgia, 'Times New Roman', serif; font-size: 1.02rem; }}
.changed {{ color: {brand.RUST}; font-size: 0.92rem; }}
.side {{ background: {brand.SHEET}; border: 1px solid {brand.RULE}; border-top: 4px solid {brand.SLATE};
         padding: 0.8rem 1rem; border-radius: 4px; height: 100%; color: {brand.INK}; }}
.side.b {{ border-top-color: {brand.RUST}; }}
.side h5 {{ margin: 0 0 0.4rem 0; color: {brand.INK}; }}
.pill {{ display: inline-block; background: {brand.SAND_TINT}; color: {brand.INK}; border-radius: 999px;
         padding: 0.05rem 0.6rem; font-size: 0.8rem; margin-right: 0.3rem; }}
.pill.over {{ background: {brand.RUST}; color: #fff; }}
</style>
"""
)


def md(text):
    """Markdown with dollar signs kept as dollar signs (Streamlit reads $...$ as math)."""
    return text.replace("$", "\\$")


def quote(text):
    return "\n".join("> " + line if line else ">" for line in md(text).split("\n"))


def show_passage(p, open_text=True):
    st.markdown(f"#### {p['label']}: {p['title']}")
    if open_text:
        st.markdown(quote(p["text"]))
    else:
        with st.expander("Read the original words"):
            st.markdown(quote(p["text"]))
    st.html(f'<div class="plain"><b>In plain language:</b> {md(p["plain"])}</div>')
    if p.get("changed"):
        st.html(f'<div class="changed">✎ Changed later: {p["changed"]}</div>')


def show_case(c, expanded=False):
    over = f' <span class="pill over">{c["overruled"]}</span>' if c.get("overruled") else ""
    with st.expander(f"⚖️ {c['name']} ({c['year']})", expanded=expanded):
        st.html(f'<span class="pill">{c["topic"]}</span><span class="pill">Vote: {c["vote"]}</span>{over}')
        st.markdown(f"**The question:** {md(c['question'])}")
        st.markdown(f"**The decision:** {md(c['decision'])}")
        st.markdown(f"**Why it matters:** {md(c['matters'])}")
        st.caption("Connected to: " + ", ".join(BY_ID[r]["label"] for r in c["related"]))


def show_debate(d):
    st.markdown(f"**{d['intro']}**")
    a, b = st.columns(2)
    a.html(f'<div class="side"><h5>{d["side_a"][0]}</h5>{md(d["side_a"][1])}</div>')
    b.html(f'<div class="side b"><h5>{d["side_b"][0]}</h5>{md(d["side_b"][1])}</div>')
    st.markdown(f"🤔 **Think about it:** {md(d['think'])}")
    if d["cases"]:
        st.caption("Cases to look at: " + ", ".join(d["cases"]) + " (see the Supreme Court tab)")
    st.caption("Parts of the Constitution: " + ", ".join(BY_ID[r]["label"] for r in d["related"]))


# ------------------------------------------------------------------ header and fun fact
st.session_state.setdefault("fact", random.randrange(len(FACTS)))


def _new_fact():
    choices = [i for i in range(len(FACTS)) if i != st.session_state.fact]
    st.session_state.fact = random.choice(choices)


st.title("Constitution Explorer")
st.markdown(
    "Ask any question about the U.S. Constitution. You'll see the exact words that answer it, explained in plain "
    "language, along with the Supreme Court cases and debates that shape what those words mean today."
)
fact_col, button_col = st.columns([6, 1], vertical_alignment="center")
fact_col.html(f'<div class="fact"><span class="tag">🎲 Fun fact</span>{FACTS[st.session_state.fact]}</div>')
button_col.button("Another fact", on_click=_new_fact, use_container_width=True)

ask_tab, read_tab, court_tab, debate_tab, quiz_tab, facts_tab = st.tabs(
    ["💬 Ask a question", "📜 Read the Constitution", "⚖️ Supreme Court cases", "🤔 Big debates", "🎯 Quiz",
     "🎲 Fun facts"]
)

# ------------------------------------------------------------------ ask
with ask_tab:
    st.session_state.setdefault("question", "")

    def _use_example(q):
        st.session_state.question = q

    question = st.text_input(
        "Your question", key="question", placeholder="For example: Can the President pardon anyone?",
        help="Type a question in your own words, or name a part, like \"14th Amendment\" or \"Article II, Section 2\".",
    )
    st.caption("Or try one of these:")
    cols = st.columns(4)
    for i, ex in enumerate(EXAMPLES):
        cols[i % 4].button(ex, key=f"ex{i}", on_click=_use_example, args=(ex,), use_container_width=True)

    if question.strip():
        passages, cases, debates = ask(question)
        if not passages:
            st.warning(
                "I couldn't find a part of the Constitution that matches. Try different words, such as "
                "\"voting\", \"President\", \"free speech\" or \"search\", or browse the **Read the Constitution** tab."
            )
        else:
            st.divider()
            st.subheader("What the Constitution says")
            st.caption("Best match first. The quoted words are the original text, with its 1787 spelling.")
            for i, p in enumerate(passages):
                show_passage(p, open_text=i == 0 or len(p["text"]) < 900)
            if cases:
                st.subheader("Supreme Court cases connected to this")
                for c in cases:
                    show_case(c)
            if debates:
                st.subheader("People disagree about this")
                d = debates[0]
                with st.expander(f"🤔 {d['title']}"):
                    show_debate(d)
            st.caption(
                "This app finds matching parts of the Constitution by keywords. It's a learning tool, not legal advice."
            )

# ------------------------------------------------------------------ read
with read_tab:
    st.markdown(
        "The Constitution has a Preamble, seven Articles and 27 Amendments. Pick a part to read it with "
        "plain-language explanations."
    )
    part = st.radio("Part", [name for name, _ in PARTS], horizontal=False, label_visibility="collapsed")
    for name, ids in PARTS:
        if name == part:
            st.subheader(name)
            for pid in ids:
                p = BY_ID[pid]
                with st.expander(f"{p['label']}: {p['title']}", expanded=len(ids) == 1):
                    st.markdown(quote(p["text"]))
                    st.html(f'<div class="plain"><b>In plain language:</b> {md(p["plain"])}</div>')
                    if p.get("changed"):
                        st.html(f'<div class="changed">✎ Changed later: {p["changed"]}</div>')

# ------------------------------------------------------------------ court
with court_tab:
    st.markdown(
        "The Supreme Court decides what the Constitution's words mean in real disputes. These landmark cases changed "
        "how Americans understand their rights and their government. Some were later overruled, which shows that "
        "interpretation can change."
    )
    topics = sorted({c["topic"] for c in CASES})
    left, right = st.columns([2, 1])
    picked = left.multiselect("Topics", topics, placeholder="All topics")
    order = right.selectbox("Order", ["Oldest first", "Newest first"])
    shown = [c for c in CASES if not picked or c["topic"] in picked]
    shown.sort(key=lambda c: c["year"], reverse=order == "Newest first")
    st.caption(f"{len(shown)} cases")
    for c in shown:
        show_case(c)

# ------------------------------------------------------------------ debates
with debate_tab:
    st.markdown(
        "Thoughtful people read the same words and reach different conclusions. Each debate below gives the main "
        "arguments on both sides. The goal isn't to pick the \"right\" answer but to understand why people disagree, "
        "so you can make up your own mind."
    )
    for d in DEBATES:
        with st.expander(f"🤔 {d['title']}"):
            show_debate(d)

# ------------------------------------------------------------------ quiz
with quiz_tab:

    def _new_quiz():
        st.session_state.quiz = random.sample(range(len(QUIZ)), QUIZ_LENGTH)
        st.session_state.quiz_round = st.session_state.get("quiz_round", 0) + 1
        st.session_state.quiz_checked = False

    if "quiz" not in st.session_state:
        _new_quiz()
    st.session_state.setdefault("best", 0)

    st.markdown(f"Five random questions. Check your answers, then try a new round. Best score so far: "
                f"**{st.session_state.best} / {QUIZ_LENGTH}**")
    answers = []
    for n, qi in enumerate(st.session_state.quiz, start=1):
        q, choices, _, _ = QUIZ[qi]
        answers.append(st.radio(f"**{n}. {q}**", choices, index=None,
                                key=f"q{st.session_state.quiz_round}_{qi}"))
    check, again = st.columns([1, 1])
    if check.button("Check my answers", type="primary", use_container_width=True):
        st.session_state.quiz_checked = True
    again.button("New quiz", on_click=_new_quiz, use_container_width=True)

    if st.session_state.quiz_checked:
        score = 0
        for n, (qi, a) in enumerate(zip(st.session_state.quiz, answers), start=1):
            q, choices, right_i, why = QUIZ[qi]
            if a == choices[right_i]:
                score += 1
                st.success(f"{n}. Correct! {why}")
            elif a is None:
                st.info(f"{n}. Not answered. The answer is **{choices[right_i]}**. {why}")
            else:
                st.error(f"{n}. Not quite. The answer is **{choices[right_i]}**. {why}")
        st.session_state.best = max(st.session_state.best, score)
        st.metric("Your score", f"{score} / {QUIZ_LENGTH}")
        if score == QUIZ_LENGTH:
            st.balloons()

# ------------------------------------------------------------------ facts
with facts_tab:
    st.markdown("Surprising, funny and little-known facts about the Constitution and the people who wrote it.")
    for f in FACTS:
        st.markdown(f"- {md(f)}")

st.divider()
st.caption(
    "Text of the Constitution from the National Archives transcription. Long amendments are shortened where marked "
    "[...]. Cases and debates are summarized for students and are not legal advice. "
    "A [Dougalien Systems](https://dougalien.com) app."
)
