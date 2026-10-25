"""Optional short AI answer for questions that have no written answer in answers.py.

It only runs when an Anthropic API key is set (Streamlit secret or environment variable
ANTHROPIC_API_KEY). Claude is given only the matching passages of the Constitution and their
plain-language explanations, and told to answer from those alone. Without a key, or if anything
goes wrong, the app falls back to its offline answer.
"""

import os

MODEL = "claude-opus-5-5"

SYSTEM = (
    "You help high school students understand the U.S. Constitution. Answer the student's question in "
    "2 or 3 short, friendly sentences of plain language, as a kind teacher would. Use ONLY the passages "
    "of the Constitution given to you and their explanations. If they don't answer the question, say so "
    "simply and suggest what part of the Constitution to look at. Stay neutral on political questions: "
    "where people disagree, say that they do, without taking a side. Don't give legal advice, don't "
    "quote the passages (the app shows them right after your answer), and don't use headings, lists or "
    "markdown."
)


def api_key():
    try:
        import streamlit as st
        key = st.secrets.get("ANTHROPIC_API_KEY")
    except Exception:
        key = None
    return key or os.environ.get("ANTHROPIC_API_KEY")


def enabled():
    if not api_key():
        return False
    try:
        import anthropic  # noqa: F401
    except ImportError:
        return False
    return True


def build_prompt(question, passages):
    parts = []
    for p in passages:
        parts.append(f"<passage label=\"{p['label']}: {p['title']}\">\n<text>{p['text']}</text>\n"
                     f"<explanation>{p['plain']}</explanation>\n</passage>")
    return "\n".join(parts) + f"\n\nStudent's question: {question}"


def answer(question, passages):
    """A short plain answer grounded in the passages, or None if it can't be made."""
    if not passages or not enabled():
        return None
    import anthropic
    try:
        client = anthropic.Anthropic(api_key=api_key())
        response = client.messages.create(
            model=MODEL,
            max_tokens=2000,
            system=SYSTEM,
            output_config={"effort": "low"},
            messages=[{"role": "user", "content": build_prompt(question, passages[:3])}],
        )
    except Exception:
        return None
    if response.stop_reason != "end_turn":
        return None
    text = "".join(b.text for b in response.content if b.type == "text").strip()
    return text or None
