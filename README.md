<p><a href="https://dougalien.com"><img src="assets/dougalien_systems_logo.png" alt="Dougalien Systems" height="48"></a></p>

# Constitution Explorer

A fun way to learn the U.S. Constitution, written for high school students and anyone else who's curious.

A [Dougalien Systems](https://dougalien.com) app.

- **Ask a question** in your own words ("Can my school search my backpack?", "How old do you have to be to be President?") and see the exact parts of the Constitution that answer it, each explained in plain language, with the Supreme Court cases and debates connected to it.
- **Read the Constitution**: the Preamble, all seven Articles and all 27 Amendments, each with a plain-language explanation and a note where a later amendment changed it.
- **Supreme Court cases**: 34 landmark decisions, from Marbury v. Madison (1803) to Trump v. United States (2024), including the student-rights cases (Tinker, T.L.O., Hazelwood, Morse, Mahanoy). Each gives the question, the decision, the vote and why it matters, and marks cases that were later overruled.
- **Big debates**: ten questions people disagree about (how to read the Constitution, judicial review, federalism, free speech, guns, church and state, presidential power, equal protection, unlisted rights, the Electoral College). Each gives the strongest case for both sides and a question to think about, without picking a winner.
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
| `search.py` | the question search |
| `dougalien_brand.py`, `.streamlit/config.toml`, `assets/` | the Dougalien Systems look, the same as Care-Gap and Geo-Tools |
| `test_app.py` | checks the content and the search; run `python test_app.py` |

The question search is a keyword search (BM25) with a list of everyday words mapped to the Constitution's words (for example "gun" also searches "arms"). It runs offline, needs no API key, and only ever shows the real text, so it can't make anything up. It also recognizes named parts like "14th Amendment" or "Article II, Section 2".

The text follows the National Archives transcription, keeping the original spelling ("chuse", "defence"). A few long passages are shortened where marked [...]: the original electoral vote procedure in Article II (replaced by the 12th Amendment), the signers' names, and parts of the 12th, 14th, 17th, 18th, 20th, 21st, 22nd, 23rd, 24th and 25th Amendments.

Cases and debates are summaries for students, not legal advice.
