"""Links to primary sources for every passage, case and debate.

Passages link to the National Archives transcription, the official Constitution Annotated
(Congress.gov, prepared by the Library of Congress) and, for some amendments, the National
Archives' Milestone Documents page with the original. Cases link to the full opinion (Justia
hosts the Court's own text and PDF) and, where there is one, the National Archives' page on
the case. Debates link to founding-era writings at the Library of Congress.

Every URL here was checked to exist on 2026-10-25.
"""

ARCHIVES_CONSTITUTION = "https://www.archives.gov/founding-docs/constitution-transcript"
ARCHIVES_BILL_OF_RIGHTS = "https://www.archives.gov/founding-docs/bill-of-rights-transcript"
ARCHIVES_11_27 = "https://www.archives.gov/founding-docs/amendments-11-27"
ARCHIVES_ORIGINAL = "https://www.archives.gov/founding-docs/constitution"
CONAN = "https://constitution.congress.gov/browse/"
HOUSE_MANUAL = "https://github.com/usgpo/house-manual"

MILESTONES = {
    "am13": "https://www.archives.gov/milestone-documents/13th-amendment",
    "am14": "https://www.archives.gov/milestone-documents/14th-amendment",
    "am15": "https://www.archives.gov/milestone-documents/15th-amendment",
    "am19": "https://www.archives.gov/milestone-documents/19th-amendment",
}

FEDERALIST = {
    "all": ("The Federalist Papers, full text (Library of Congress)", "https://guides.loc.gov/federalist-papers/full-text"),
    51: ("Federalist No. 51 by James Madison: checks and balances (Library of Congress)",
         "https://guides.loc.gov/federalist-papers/text-51-60"),
    70: ("Federalist No. 70 by Alexander Hamilton: \"energy in the executive\" (Library of Congress)",
         "https://guides.loc.gov/federalist-papers/text-61-70"),
    78: ("Federalist No. 78 by Alexander Hamilton: the courts and judicial review (Library of Congress)",
         "https://guides.loc.gov/federalist-papers/text-71-80"),
}
DANBURY = ("Thomas Jefferson's 1802 letter to the Danbury Baptists, the \"wall of separation\" (Library of Congress)",
           "https://www.loc.gov/loc/lcib/9806/danpre.html")
MADISON_NOTES = ("James Madison's notes on the debates at the 1787 Convention (Library of Congress)",
                 "https://www.loc.gov/collections/james-madison-papers/articles-and-essays/"
                 "james-madison-and-the-federal-constitutional-convention-of-1787")
VOTING_RIGHTS_ACT = ("Voting Rights Act of 1965 (National Archives)", "https://www.archives.gov/milestone-documents/voting-rights-act")

# Full opinion on Justia: volume/page for older cases, volume/docket for recent ones
OPINIONS = {
    "Marbury v. Madison": "5/137", "McCulloch v. Maryland": "17/316", "Gibbons v. Ogden": "22/1",
    "Dred Scott v. Sandford": "60/393", "Plessy v. Ferguson": "163/537", "Korematsu v. United States": "323/214",
    "Wickard v. Filburn": "317/111", "Brown v. Board of Education": "347/483", "Mapp v. Ohio": "367/643",
    "Engel v. Vitale": "370/421", "Gideon v. Wainwright": "372/335", "Miranda v. Arizona": "384/436",
    "Loving v. Virginia": "388/1", "Tinker v. Des Moines": "393/503", "New York Times Co. v. United States": "403/713",
    "Roe v. Wade": "410/113", "United States v. Nixon": "418/683", "New Jersey v. T.L.O.": "469/325",
    "Hazelwood v. Kuhlmeier": "484/260", "Texas v. Johnson": "491/397", "United States v. Lopez": "514/549",
    "Morse v. Frederick": "551/393", "District of Columbia v. Heller": "554/570", "Citizens United v. FEC": "558/310",
    "Shelby County v. Holder": "570/529", "Riley v. California": "573/373", "Obergefell v. Hodges": "576/644",
    "Mahanoy Area School District v. B.L.": "594/20-255",
    "Dobbs v. Jackson Women's Health Organization": "597/19-1392",
    "New York State Rifle & Pistol Association v. Bruen": "597/20-843",
    "Kennedy v. Bremerton School District": "597/21-418",
    "Students for Fair Admissions v. Harvard": "600/20-1199", "Trump v. Anderson": "601/23-719",
    "Trump v. United States": "603/23-939", "Learning Resources v. Trump": "607/24-1287",
    "Trump v. Slaughter": "2025/25-332", "Trump v. Barbara": "609/25-365",
}

ARCHIVES_CASES = {
    "Marbury v. Madison": "https://www.archives.gov/milestone-documents/marbury-v-madison",
    "McCulloch v. Maryland": "https://www.archives.gov/milestone-documents/mcculloch-v-maryland",
    "Gibbons v. Ogden": "https://www.archives.gov/milestone-documents/gibbons-v-ogden",
    "Dred Scott v. Sandford": "https://www.archives.gov/milestone-documents/dred-scott-v-sandford",
    "Plessy v. Ferguson": "https://www.archives.gov/milestone-documents/plessy-v-ferguson",
    "Brown v. Board of Education": "https://www.archives.gov/milestone-documents/brown-v-board-of-education",
}


def _conan_path(pid):
    if pid == "pre":
        return "preamble/"
    if pid.startswith("am"):
        return f"amendment-{pid[2:]}/"
    if "s" in pid[1:]:
        article, section = pid[1:].split("s")
        return f"article-{article}/section-{section}/"
    return f"article-{pid[1:]}/"


def passage_sources(p):
    """(label, url) pairs for one passage of the Constitution."""
    pid = p["id"]
    if pid.startswith("am"):
        n = int(pid[2:])
        transcript = ARCHIVES_BILL_OF_RIGHTS if n <= 10 else ARCHIVES_11_27
        where = "the Bill of Rights" if n <= 10 else "Amendments 11 to 27"
    else:
        transcript, where = ARCHIVES_CONSTITUTION, "the Constitution"
    links = [
        (f"Official text: National Archives transcription of {where}", transcript),
        (f"Constitution Annotated (Congress.gov): {p['label'].split(' (')[0]}, with history and court cases",
         CONAN + _conan_path(pid)),
    ]
    if pid in MILESTONES:
        links.append(("The original document and its history (National Archives)", MILESTONES[pid]))
    if not pid.startswith("am"):
        links.append(("See the handwritten original (National Archives)", ARCHIVES_ORIGINAL))
    return links


def case_sources(c):
    """(label, url) pairs for one Supreme Court case."""
    links = []
    path = OPINIONS.get(c["name"])
    if path:
        links.append((f"Read the Court's full opinion in {c['name']}",
                      f"https://supreme.justia.com/cases/federal/us/{path}/"))
    if c["name"] in ARCHIVES_CASES:
        links.append(("The case's original records and history (National Archives)", ARCHIVES_CASES[c["name"]]))
    return links


DEBATE_SOURCES = {
    "How should judges read the Constitution?": [MADISON_NOTES, FEDERALIST["all"]],
    "Should unelected judges be able to strike down laws?": [FEDERALIST[78]],
    "How much power should the national government have compared with the states?": [FEDERALIST[51], MADISON_NOTES],
    "Where are the limits of free speech?": [("The Bill of Rights (National Archives)", ARCHIVES_BILL_OF_RIGHTS)],
    "What does the 2nd Amendment allow?": [("The Bill of Rights (National Archives)", ARCHIVES_BILL_OF_RIGHTS)],
    "How separate should church and state be?": [DANBURY],
    "How much power should the President have?": [FEDERALIST[70], FEDERALIST[51]],
    "What does \"equal protection\" require?": [("14th Amendment (National Archives)", MILESTONES["am14"])],
    "Which rights exist even if they aren't written down?": [("The Bill of Rights (National Archives)",
                                                             ARCHIVES_BILL_OF_RIGHTS)],
    "Keep or change the Electoral College?": [MADISON_NOTES, ("12th Amendment (National Archives)", ARCHIVES_11_27)],
}


def debate_sources(d):
    """Founding-era and official documents behind one debate."""
    return list(DEBATE_SOURCES.get(d["title"], []))
