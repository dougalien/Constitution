<p><a href="https://dougalien.com"><img src="assets/dougalien_systems_logo.png" alt="Dougalien Systems" height="48"></a></p>

# Constitution Explorer

A fun way to learn the U.S. Constitution, written for high school students and anyone else who's curious.

A [Dougalien Systems](https://dougalien.com) app.

- **Ask a question** in your own words ("Can my school search my backpack?", "When can the government take my land?") and get a short, friendly answer first, then the exact words of the Constitution behind it. The full passages, Supreme Court cases and debates are tucked underneath for anyone who wants to dig deeper.
- **Read the Constitution**: the Preamble, all seven Articles and all 27 Amendments, each with a plain-language explanation and a note where a later amendment changed it.
- **Supreme Court cases**: 37 landmark decisions, from Marbury v. Madison (1803) to Trump v. Barbara (2026), including the student-rights cases (Tinker, T.L.O., Hazelwood, Morse, Mahanoy). Each gives the question, the decision, the vote and why it matters, and marks cases that were later overruled.
- **Big debates**: ten questions people disagree about (how to read the Constitution, judicial review, federalism, free speech, guns, church and state, presidential power, equal protection, unlisted rights, the Electoral College). Each gives the strongest case for both sides and a question to think about, without picking a winner.
- **Primary sources everywhere**: every passage links to the National Archives transcription and the Constitution Annotated on Congress.gov; every case links to the Court's full opinion (and the National Archives' records where they exist); every debate links to founding-era writings like the Federalist Papers and Jefferson's Danbury letter.
- **Quiz**: five random questions per round, with explanations.
- **Fun facts**: a random one at the top of the page, and the full list in their own tab.

## Run it

On Windows, double-click `run.bat`. Anywhere else:

```
pip install -r requirements.txt
streamlit run app.py
```

To put it online, sign in at [share.streamlit.io](https://share.streamlit.io), choose **Create app**, and pick repository `dougalien/Constitution`, branch `main`, main file `app.py`.

## How it's built

| File | What's in it |
| --- | --- |
| `app.py` | the page |
| `constitution.py` | the text, split into 52 passages, each with a plain-language explanation and search keywords |
| `learning.py` | Supreme Court cases, debates, fun facts and quiz questions |
| `answers.py` | 55 hand-written short answers to common student questions, each tied to the passage and exact words that back it up |
| `search.py` | the question search, and matching questions to the written answers |
| `ai_answer.py` | the optional AI short answer (see below) |
| `sources.py` | links to primary sources for every passage, case and debate |
| `check_text.py`, `reference/` | the word-for-word check of the Constitution text against the official copy |
| `dougalien_brand.py`, `.streamlit/config.toml`, `assets/` | the Dougalien Systems look, the same as Care-Gap and Geo-Tools |
| `test_app.py` | checks the content and the search; run `python test_app.py` |

The question search is a keyword search (BM25) with a list of everyday words mapped to the Constitution's words (for example "gun" also searches "arms"). It runs offline, needs no API key, and only ever shows the real text, so it can't make anything up. It also recognizes named parts like "14th Amendment" or "Article II, Section 2".

Common questions get a hand-written short answer from `answers.py`. Different ways of asking the same thing get the same answer, but "can" and "when" questions are told apart, so "Can the government take my land?" and "When can the government take my land?" get different answers. Other questions get the plain-language explanation of the best-matching passage.

## Optional AI answers

For questions without a written answer, the app can ask Claude (Anthropic's AI) for a two- or three-sentence answer. Claude sees only the matching passages of the Constitution and their explanations, is told to answer from those alone, stay neutral and write for students, and the answer is labeled as written by AI. It's off unless you add a key; without one, or if the AI can't answer, the app uses its offline answer.

To turn it on, get an API key at [console.anthropic.com](https://console.anthropic.com), then in Streamlit Community Cloud open the app's **Settings → Secrets** and add:

```
ANTHROPIC_API_KEY = "sk-ant-..."
```

Running it on your own computer, put the same line in `.streamlit/secrets.toml` (don't commit it) or set the `ANTHROPIC_API_KEY` environment variable. Answers are cached for a week, so repeated questions don't cost anything extra.

## How the text is checked

The Constitution text is checked word for word against the official copy printed in the House Manual (117th Congress) by the U.S. Government Publishing Office and the Clerk of the House, published as XML at [usgpo/house-manual](https://github.com/usgpo/house-manual). A copy is saved in `reference/`.

```
python check_text.py               # offline check against the official copy
python check_text.py --secondary   # also re-checks the few clauses the House Manual doesn't print in full
```

Every sentence and clause in `constitution.py` must appear word for word in the official text (capital letters and punctuation are ignored, since official printings differ slightly there). The House Manual prints a handful of clauses only in part, between its notes; `--secondary` confirms those against two independent transcriptions ([Surden](https://github.com/hsurden/us-constitution) and [Project Gutenberg #5](https://github.com/GITenberg/The-United-States-Constitution_5)). `python test_app.py` runs the offline check too, so any change to the text that doesn't match fails the tests.

The text keeps the original spelling ("chuse", "defence"). A few long passages are shortened where marked [...]: the original electoral vote procedure in Article II (replaced by the 12th Amendment), the signers' names, and parts of the 12th, 14th, 17th, 18th, 20th, 21st, 22nd, 23rd, 24th and 25th Amendments.

Cases and debates are summaries for students, not legal advice.
