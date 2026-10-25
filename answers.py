"""Short, friendly answers to common questions, written and checked by hand.

The app shows one of these first when a question matches it, then the parts of the Constitution
behind it. Each answer leads with the direct answer in everyday words, stays calm and
nonpartisan, and is backed by the passage(s) it lists. `quote` is the exact clause of the first
passage that the answer rests on; the app shows it on its own so readers don't face the whole
passage at once (test_app.py checks that every quote is really in the text).

    asks      ways people ask it (the search matches questions against these)
    answer    two or three sentences, plain language
    passages  passage ids from constitution.py, most important first
    quote     exact words from the first passage
    cases     (optional) Supreme Court cases from learning.py that this answer connects to
"""

FAQ = [
    # ---------------------------------------------------------------- property, searches, police
    {
        "asks": ["Can the government take my land?", "Can the government take my house?",
                 "Can the government take my property?", "eminent domain"],
        "answer": (
            "Only in limited cases, and never for free. The government can take private property only for a "
            "public use, like a road or a school, and it has to pay you a fair price for it. This is called "
            "eminent domain."
        ),
        "passages": ["am5"], "quote": "nor shall private property be taken for public use, without just compensation",
    },
    {
        "asks": ["When can the government take my land?", "When can the government take my property?",
                 "What is a public use?", "How much does the government have to pay for my land?"],
        "answer": (
            "When it's for a \"public use\" and it pays \"just compensation,\" which means fair market value. Roads, "
            "schools and parks clearly count. In Kelo v. City of New London (2005) the Supreme Court said economic "
            "development can count too, which many people disagreed with, so many states passed their own laws "
            "limiting it. You can challenge a taking or the price in court."
        ),
        "passages": ["am5"], "quote": "nor shall private property be taken for public use, without just compensation",
    },
    {
        "asks": ["Can police search my phone?", "Do police need a warrant to look at my phone?",
                 "Can a cop look through my cell phone?"],
        "answer": (
            "Usually not without a warrant. The Supreme Court decided in 2014 that police generally need a "
            "warrant from a judge to search the phone of someone they arrest. There are rare emergency exceptions, "
            "and you can always choose to let them look."
        ),
        "cases": ["Riley v. California"],
        "passages": ["am4"], "quote": "against unreasonable searches and seizures",
    },
    {
        "asks": ["Can police search my house?", "Can police come into my home?", "Do police need a warrant?",
                 "Can police search my car?", "What is a warrant?"],
        "answer": (
            "Usually police need a warrant, which is permission signed by a judge who agrees there's good reason "
            "(probable cause) to search. There are some exceptions, like emergencies, evidence in plain view, or "
            "when you give permission. Cars have a few more exceptions than homes."
        ),
        "cases": ["Mapp v. Ohio"],
        "passages": ["am4"],
        "quote": "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation",
    },
    {
        "asks": ["Can my school search my backpack?", "Can a teacher search my bag?", "Can school search my locker?",
                 "Can the principal search me?", "Can my teacher take my phone?",
                 "Can my school go through my phone?"],
        "answer": (
            "Yes, but only with a good reason. Schools don't need a warrant, but they do need \"reasonable "
            "suspicion\" that you broke a law or a school rule, and the search can't be more than needed. That "
            "rule comes from New Jersey v. T.L.O. (1985)."
        ),
        "cases": ["New Jersey v. T.L.O."],
        "passages": ["am4"], "quote": "against unreasonable searches and seizures",
    },
    {
        "asks": ["What are my rights if I'm arrested?", "What happens if I get arrested?", "What are Miranda rights?",
                 "Do I have to talk to the police?", "Can I remain silent?"],
        "answer": (
            "You have the right to stay silent, the right to a lawyer (free if you can't afford one), and the right "
            "to a fair trial. Before questioning you in custody, police must tell you these rights; that's the "
            "Miranda warning. Staying calm and asking for a lawyer is always allowed."
        ),
        "cases": ["Miranda v. Arizona", "Gideon v. Wainwright"],
        "passages": ["am5", "am6"], "quote": "nor shall be compelled in any criminal case to be a witness against himself",
    },
    {
        "asks": ["Do I get a lawyer?", "What if I can't afford a lawyer?", "Right to an attorney"],
        "answer": (
            "Yes. If you're charged with a crime, you have the right to a lawyer, and if you can't afford one for a "
            "serious charge, the government must provide one for free. That's been the rule since Gideon v. "
            "Wainwright (1963)."
        ),
        "cases": ["Gideon v. Wainwright"],
        "passages": ["am6"], "quote": "to have the Assistance of Counsel for his defence",
    },
    {
        "asks": ["What does plead the fifth mean?", "Can I refuse to testify?"],
        "answer": (
            "It means refusing to answer questions that could be used to show you committed a crime. The 5th "
            "Amendment says no one can be forced to be a witness against themselves."
        ),
        "cases": ["Miranda v. Arizona"],
        "passages": ["am5"], "quote": "nor shall be compelled in any criminal case to be a witness against himself",
    },
    {
        "asks": ["Can I be tried twice for the same crime?", "What is double jeopardy?"],
        "answer": (
            "No. Once you've been found not guilty (or convicted) of a crime, the same government can't put you on "
            "trial for it again. That's called double jeopardy."
        ),
        "passages": ["am5"], "quote": "nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb",
    },
    {
        "asks": ["Is the death penalty constitutional?", "What is cruel and unusual punishment?",
                 "Can a teenager get the death penalty?"],
        "answer": (
            "The Supreme Court has allowed the death penalty, but with limits from the 8th Amendment's ban on "
            "\"cruel and unusual punishments.\" For example, it can't be used for crimes committed by anyone under 18. "
            "Whether it should exist at all is a debate that states decide differently."
        ),
        "passages": ["am8"], "quote": "nor cruel and unusual punishments inflicted",
    },
    {
        "asks": ["Do I get a jury trial?", "What is a speedy trial?", "Do I have a right to a fair trial?"],
        "answer": (
            "Yes. If you're accused of a crime, you have the right to a speedy, public trial with a fair jury, to know "
            "the charges, to question the witnesses against you, and to have a lawyer."
        ),
        "cases": ["Gideon v. Wainwright"],
        "passages": ["am6"], "quote": "the accused shall enjoy the right to a speedy and public trial, by an impartial jury",
    },
    # ---------------------------------------------------------------- speech, religion, school
    {
        "asks": ["Do I have free speech at school?", "Can my school punish me for what I say?",
                 "Can I protest at school?", "Can I wear a political shirt to school?"],
        "answer": (
            "Yes, you keep your free speech rights at school. The Supreme Court said students don't lose them \"at "
            "the schoolhouse gate.\" Schools can limit speech that would seriously disrupt class, that promotes "
            "illegal drugs, or that's in school-run publications."
        ),
        "cases": ["Tinker v. Des Moines", "Morse v. Frederick", "Mahanoy Area School District v. B.L."],
        "passages": ["am1"], "quote": "or abridging the freedom of speech",
    },
    {
        "asks": ["Can I get in trouble for what I post online?", "Can my school punish me for a social media post?",
                 "Does free speech apply to social media?", "Can I post anything online?"],
        "answer": (
            "The 1st Amendment stops the government, including public schools, from punishing most speech, and "
            "schools have less power over what you post off campus. But it doesn't stop private companies like "
            "social media apps from setting their own rules, and threats or harassment aren't protected anywhere."
        ),
        "cases": ["Mahanoy Area School District v. B.L."],
        "passages": ["am1"], "quote": "or abridging the freedom of speech",
    },
    {
        "asks": ["What does freedom of speech mean?", "What is free speech?", "Is all speech protected?",
                 "Is hate speech protected?"],
        "answer": (
            "It means the government can't punish you for what you say or write, even if people find it offensive. "
            "There are narrow exceptions, like true threats, inciting immediate violence, lying under oath, and "
            "defamation (harmful lies about someone)."
        ),
        "cases": ["Texas v. Johnson", "New York Times Co. v. United States"],
        "passages": ["am1"], "quote": "or abridging the freedom of speech, or of the press",
    },
    {
        "asks": ["Can I burn a flag?", "Is flag burning legal?"],
        "answer": (
            "Yes. In Texas v. Johnson (1989), the Supreme Court said burning the American flag as a protest is "
            "protected speech, even though many people find it offensive."
        ),
        "cases": ["Texas v. Johnson"],
        "passages": ["am1"], "quote": "or abridging the freedom of speech",
    },
    {
        "asks": ["Can teachers lead a prayer in class?", "Can I pray at school?", "Is prayer allowed in school?",
                 "Separation of church and state"],
        "answer": (
            "You can pray at school on your own or with friends, and religious clubs can meet like other clubs. "
            "What public schools can't do is lead or sponsor prayers, because the government can't favor a religion. "
            "Teachers and coaches can still pray privately."
        ),
        "cases": ["Engel v. Vitale", "Kennedy v. Bremerton School District"],
        "passages": ["am1"], "quote": "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof",
    },
    {
        "asks": ["What is freedom of religion?", "Can the government make me follow a religion?"],
        "answer": (
            "The government can't set up an official religion or favor one over another, and it can't stop you from "
            "practicing your faith (or having none). No religious test can be required to hold public office, either."
        ),
        "cases": ["Engel v. Vitale"],
        "passages": ["am1", "a6"], "quote": "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof",
    },
    {
        "asks": ["Can I protest?", "Is protesting legal?", "What is freedom of assembly?"],
        "answer": (
            "Yes. You have the right to gather peacefully and to ask the government to fix problems. Cities can set "
            "fair rules about time, place and noise, but not ban a protest because they dislike its message."
        ),
        "cases": ["Tinker v. Des Moines"],
        "passages": ["am1"], "quote": "the right of the people peaceably to assemble, and to petition the Government for a redress of grievances",
    },
    {
        "asks": ["What is freedom of the press?", "Can the government stop a newspaper from publishing?"],
        "answer": (
            "The government can almost never stop news from being published ahead of time or punish journalists for "
            "reporting the truth. The Supreme Court protected this even for secret war documents in the Pentagon "
            "Papers case (1971)."
        ),
        "cases": ["New York Times Co. v. United States", "Hazelwood v. Kuhlmeier"],
        "passages": ["am1"], "quote": "or of the press",
    },
    # ---------------------------------------------------------------- guns
    {
        "asks": ["Can I own a gun?", "What does the second amendment mean?", "Do I have a right to a gun?",
                 "What about guns?", "Can the government take away my guns?", "Can they ban guns?"],
        "answer": (
            "The Supreme Court has said the 2nd Amendment protects an individual's right to keep and carry a gun for "
            "self-defense. Governments can still have some rules, like age limits and banning guns for people with "
            "serious criminal records. Exactly which rules are allowed is still being decided in courts."
        ),
        "cases": ["District of Columbia v. Heller", "New York State Rifle & Pistol Association v. Bruen"],
        "passages": ["am2"], "quote": "the right of the people to keep and bear Arms, shall not be infringed",
    },
    # ---------------------------------------------------------------- voting and elections
    {
        "asks": ["Who can vote?", "Can I vote?", "Who has the right to vote?"],
        "answer": (
            "U.S. citizens 18 and older can vote. Over time, amendments made sure states can't deny the vote because "
            "of race, sex, failure to pay a poll tax, or age (for anyone 18 or older). States handle registration, so "
            "the steps depend on where you live."
        ),
        "cases": ["Shelby County v. Holder"],
        "passages": ["am26", "am15", "am19", "am24"],
        "quote": "who are eighteen years of age or older, to vote shall not be denied or abridged",
    },
    {
        "asks": ["Why is the voting age 18?", "When can I vote?", "How old do you have to be to vote?",
                 "Can 16 year olds vote?"],
        "answer": (
            "You can vote in federal elections once you're 18. The 26th Amendment lowered the age from 21 in 1971, "
            "partly because 18-year-olds were being drafted to fight in Vietnam. A few cities let 16- and "
            "17-year-olds vote in local elections."
        ),
        "passages": ["am26"], "quote": "who are eighteen years of age or older, to vote shall not be denied or abridged",
    },
    {
        "asks": ["When did women get the right to vote?", "Can women vote?"],
        "answer": "Women's right to vote nationwide was guaranteed by the 19th Amendment in 1920.",
        "passages": ["am19"], "quote": "shall not be denied or abridged by the United States or by any State on account of sex",
    },
    {
        "asks": ["How does the Electoral College work?", "What is the Electoral College?", "How is the President elected?"],
        "answer": (
            "Voters in each state choose electors, and the electors choose the President. Each state gets as many "
            "electors as it has members of Congress (D.C. gets 3), for 538 total. A candidate needs 270, a majority, "
            "to win. If no one gets 270, the House of Representatives decides."
        ),
        "passages": ["a2s1", "am12", "am23"],
        "quote": "a Number of Electors, equal to the whole Number of Senators and Representatives to which the State may be entitled in the Congress",
    },
    # ---------------------------------------------------------------- President
    {
        "asks": ["How old do you have to be to be President?", "Who can be President?",
                 "What are the requirements to be President?", "Can an immigrant be President?"],
        "answer": (
            "You must be at least 35, a natural born U.S. citizen, and have lived in the United States for at least "
            "14 years. That's the whole list."
        ),
        "passages": ["a2s1"],
        "quote": "No Person except a natural born Citizen, or a Citizen of the United States, at the time of the Adoption of this Constitution, shall be eligible to the Office of President",
    },
    {
        "asks": ["How long is a President's term?", "How many terms can a President serve?",
                 "Can a President serve three terms?", "term limits for the president",
                 "How long can a President serve?", "How long does a President serve?"],
        "answer": (
            "A President's term is four years, and a person can be elected President only twice. That limit comes "
            "from the 22nd Amendment (1951), passed after Franklin D. Roosevelt won four elections."
        ),
        "passages": ["am22", "a2s1"], "quote": "No person shall be elected to the office of the President more than twice",
    },
    {
        "asks": ["What happens if the President dies?", "Who takes over if the President can't serve?",
                 "Who is next in line after the President?"],
        "answer": (
            "The Vice President becomes President. The 25th Amendment also covers what happens if a President is too "
            "sick to serve or resigns, and how a new Vice President is chosen. After the VP, Congress set the order: "
            "the Speaker of the House is next."
        ),
        "passages": ["am25", "a2s1"],
        "quote": "In case of the removal of the President from office or of his death or resignation, the Vice President shall become President",
    },
    {
        "asks": ["Can the President pardon anyone?", "What is a pardon?", "Can the President pardon himself?"],
        "answer": (
            "The President can pardon people for federal crimes, but not state crimes, and a pardon can't stop an "
            "impeachment. Whether a President could pardon themselves has never been decided by a court."
        ),
        "passages": ["a2s2"], "quote": "he shall have Power to grant Reprieves and Pardons for Offences against the United States, except in Cases of Impeachment",
    },
    {
        "asks": ["What powers does the President have?", "What does the President do?"],
        "answer": (
            "The President carries out the nation's laws, leads the military as commander in chief, makes treaties "
            "(with Senate approval), picks judges and top officials (with Senate approval), can veto bills, and can "
            "pardon federal crimes."
        ),
        "cases": ["United States v. Nixon", "Trump v. United States", "Trump v. Slaughter"],
        "passages": ["a2s2", "a2s3", "a2s1"],
        "quote": "The President shall be Commander in Chief of the Army and Navy of the United States",
    },
    {
        "asks": ["Who decides if we go to war?", "Can the President declare war?", "Who can declare war?"],
        "answer": (
            "The Constitution gives Congress the power to declare war, and makes the President commander in chief of "
            "the military. In practice, Presidents have sent troops into conflicts many times without a formal "
            "declaration, which is an ongoing debate."
        ),
        "passages": ["a1s8", "a2s2"], "quote": "To declare War",
    },
    {
        "asks": ["How does impeachment work?", "Can the President be impeached?", "What is impeachment?",
                 "Can the President be removed from office?"],
        "answer": (
            "Impeachment is a two-step process. The House votes to impeach, which is like bringing formal charges. "
            "Then the Senate holds a trial, and it takes two thirds of senators to convict and remove the official "
            "from office."
        ),
        "cases": ["United States v. Nixon"],
        "passages": ["a2s4", "a1s3", "a1s2"],
        "quote": "shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors",
    },
    # ---------------------------------------------------------------- Congress and laws
    {
        "asks": ["How does a bill become a law?", "How are laws made?"],
        "answer": (
            "A bill has to pass both the House and the Senate in the same form. Then the President signs it into law "
            "or vetoes it. If vetoed, Congress can still make it law with a two-thirds vote in both chambers."
        ),
        "passages": ["a1s7"], "quote": "Every Bill which shall have passed the House of Representatives and the Senate, shall, before it become a Law, be presented to the President of the United States",
    },
    {
        "asks": ["What is a veto?", "Can Congress override a veto?"],
        "answer": (
            "A veto is the President's \"no\" to a bill Congress passed. Congress can override it, making the bill law "
            "anyway, if two thirds of both the House and Senate vote for it again."
        ),
        "passages": ["a1s7"], "quote": "If after such Reconsideration two thirds of that House shall agree to pass the Bill",
    },
    {
        "asks": ["What does Congress do?", "What powers does Congress have?"],
        "answer": (
            "Congress makes federal laws. Its powers include taxing and spending, borrowing money, regulating trade, "
            "printing money, declaring war, funding the military, and making the laws needed to carry out those powers."
        ),
        "cases": ["McCulloch v. Maryland", "Wickard v. Filburn", "United States v. Lopez"],
        "passages": ["a1s8", "a1s1"], "quote": "To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers",
    },
    {
        "asks": ["How many senators does each state have?", "How long is a senator's term?", "How old do you have to be to be a senator?"],
        "answer": (
            "Each state has two senators, no matter its size. Senators serve six-year terms and must be at least 30, "
            "a citizen for 9 years, and live in the state they represent."
        ),
        "passages": ["a1s3"], "quote": "The Senate of the United States shall be composed of two Senators from each State",
    },
    {
        "asks": ["How many representatives does a state get?", "How long is a term in the House?",
                 "How old do you have to be to be in Congress?"],
        "answer": (
            "States get House seats based on population, counted every ten years in the census, and every state gets "
            "at least one. Representatives serve two-year terms and must be at least 25 and a citizen for 7 years."
        ),
        "passages": ["a1s2"], "quote": "No Person shall be a Representative who shall not have attained to the Age of twenty five Years",
    },
    {
        "asks": ["Can Congress give itself a raise?", "How much do members of Congress get paid?"],
        "answer": (
            "Congress sets its own pay by law, but under the 27th Amendment a raise can't take effect until after the "
            "next House election, so voters get a say first."
        ),
        "passages": ["am27", "a1s6"], "quote": "No law, varying the compensation for the services of the Senators and Representatives, shall take effect",
    },
    {
        "asks": ["Who can collect taxes?", "Can the President put tariffs on imports?", "Is the income tax constitutional?"],
        "answer": (
            "Congress has the power to tax, including tariffs on imports. The 16th Amendment (1913) specifically allows "
            "an income tax. In 2026 the Supreme Court said a President can't impose tariffs under an emergency law "
            "that doesn't clearly give that power."
        ),
        "cases": ["Learning Resources v. Trump"],
        "passages": ["a1s8", "am16"], "quote": "To lay and collect Taxes, Duties, Imposts and Excises",
    },
    # ---------------------------------------------------------------- courts
    {
        "asks": ["How many Supreme Court justices are there?", "How long do Supreme Court justices serve?",
                 "Who picks Supreme Court justices?"],
        "answer": (
            "There are nine justices today, but the Constitution doesn't set the number; Congress does. Justices are "
            "nominated by the President, confirmed by the Senate, and serve for life unless they retire or are impeached."
        ),
        "cases": ["Marbury v. Madison"],
        "passages": ["a3s1", "a2s2"], "quote": "The Judges, both of the supreme and inferior Courts, shall hold their Offices during good Behaviour",
    },
    {
        "asks": ["What is judicial review?", "Can the Supreme Court strike down a law?"],
        "answer": (
            "Yes. Courts can strike down laws that conflict with the Constitution. That power isn't spelled out in "
            "the text; the Supreme Court claimed it in Marbury v. Madison (1803), and it's been accepted ever since."
        ),
        "cases": ["Marbury v. Madison"],
        "passages": ["a3s2", "a6"], "quote": "The judicial Power shall extend to all Cases, in Law and Equity, arising under this Constitution",
    },
    # ---------------------------------------------------------------- citizenship, rights, equality
    {
        "asks": ["Is someone born here a citizen?", "What is birthright citizenship?", "How do you become a citizen?",
                 "Are children of immigrants citizens?"],
        "answer": (
            "Yes. Almost everyone born in the United States is a citizen at birth, whatever their parents' status. "
            "The 14th Amendment says so, and the Supreme Court confirmed it again in Trump v. Barbara (2026). People "
            "born elsewhere can become citizens through naturalization."
        ),
        "cases": ["Trump v. Barbara", "Dred Scott v. Sandford"],
        "passages": ["am14"],
        "quote": "All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States",
    },
    {
        "asks": ["What is equal protection?", "Does the Constitution protect against discrimination?",
                 "What does the 14th amendment do?", "Is segregation unconstitutional?"],
        "answer": (
            "The 14th Amendment requires states to give every person \"the equal protection of the laws.\" It's why "
            "the Supreme Court ended segregated public schools in Brown v. Board of Education (1954). How far it "
            "reaches in new situations is still decided case by case."
        ),
        "cases": ["Brown v. Board of Education", "Plessy v. Ferguson", "Loving v. Virginia"],
        "passages": ["am14"], "quote": "nor deny to any person within its jurisdiction the equal protection of the laws",
    },
    {
        "asks": ["What is due process?", "What does due process mean?"],
        "answer": (
            "Due process means the government has to follow fair rules before taking away your life, freedom or "
            "property, like giving you notice and a chance to be heard. Both the 5th and 14th Amendments require it."
        ),
        "cases": ["Loving v. Virginia", "Obergefell v. Hodges"],
        "passages": ["am14", "am5"], "quote": "nor shall any State deprive any person of life, liberty, or property, without due process of law",
    },
    {
        "asks": ["When was slavery abolished?", "Did the Constitution allow slavery?"],
        "answer": (
            "The original Constitution protected slavery in several places without using the word, such as the "
            "three-fifths clause. The 13th Amendment abolished slavery in 1865, at the end of the Civil War."
        ),
        "cases": ["Dred Scott v. Sandford"],
        "passages": ["am13", "a1s2", "a4s2"], "quote": "Neither slavery nor involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, shall exist within the United States",
    },
    {
        "asks": ["Do I have a right to privacy?", "Is privacy in the Constitution?"],
        "answer": (
            "The word \"privacy\" isn't in the Constitution, but several parts protect it, like the 4th Amendment's "
            "limits on searches and the 9th Amendment's note that unlisted rights still exist. Which privacy rights "
            "courts should protect is one of the big debates."
        ),
        "cases": ["Riley v. California", "Dobbs v. Jackson Women's Health Organization"],
        "passages": ["am4", "am9"], "quote": "The right of the people to be secure in their persons, houses, papers, and effects",
    },
    {
        "asks": ["What is the Bill of Rights?", "What are the first ten amendments?"],
        "answer": (
            "The Bill of Rights is the first ten amendments, added in 1791. They protect freedoms like speech, "
            "religion, the press, and fair trials, and limit what the government can do to people accused of crimes."
        ),
        "passages": ["am1", "am4", "am5", "am6"], "quote": "Congress shall make no law respecting an establishment of religion",
    },
    {
        "asks": ["What are states' rights?", "What can states decide?", "What is federalism?"],
        "answer": (
            "Federalism means power is shared between the national government and the states. The 10th Amendment "
            "says powers not given to the national government belong to the states or the people, which is why states "
            "run things like schools, driver's licenses and most criminal law."
        ),
        "cases": ["McCulloch v. Maryland", "United States v. Lopez"],
        "passages": ["am10", "a6"], "quote": "The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people",
    },
    {
        "asks": ["Can a state print its own money?", "Can a state make a treaty?", "What can't states do?"],
        "answer": (
            "No. States can't print money, make treaties with other countries, or keep their own armies in peacetime. "
            "Those powers belong to the national government."
        ),
        "passages": ["a1s10"], "quote": "No State shall enter into any Treaty, Alliance, or Confederation",
    },
    {
        "asks": ["What happens when federal and state law conflict?", "What is the supremacy clause?"],
        "answer": (
            "Federal law wins, as long as it's a valid law under the Constitution. Article VI makes the Constitution, "
            "federal laws and treaties \"the supreme Law of the Land.\""
        ),
        "cases": ["McCulloch v. Maryland"],
        "passages": ["a6"], "quote": "shall be the supreme Law of the Land",
    },
    # ---------------------------------------------------------------- the document itself
    {
        "asks": ["How do you change the Constitution?", "How is an amendment passed?", "How do you amend the Constitution?"],
        "answer": (
            "It takes two big steps. First, two thirds of both the House and Senate propose an amendment (or two "
            "thirds of the states call a convention). Then three fourths of the states, 38 of 50, must approve it. "
            "That's why there have been only 27 amendments."
        ),
        "passages": ["a5"], "quote": "when ratified by the Legislatures of three fourths of the several States",
    },
    {
        "asks": ["What does the Preamble mean?", "What is the Preamble?", "Why was the Constitution written?"],
        "answer": (
            "The Preamble is the opening sentence. It says the people are creating the government, and lists its "
            "goals: a better union, justice, peace at home, defense, the general welfare, and liberty for the future."
        ),
        "passages": ["pre"], "quote": "We the People of the United States, in Order to form a more perfect Union",
    },
    {
        "asks": ["When was the Constitution signed?", "Who signed the Constitution?", "When was the Constitution ratified?"],
        "answer": (
            "It was signed on September 17, 1787, in Philadelphia by 39 delegates, led by George Washington. It took "
            "effect after nine states ratified it, which happened in June 1788."
        ),
        "passages": ["a7"], "quote": "The Ratification of the Conventions of nine States, shall be sufficient for the Establishment of this Constitution",
    },
    {
        "asks": ["What are checks and balances?", "What is separation of powers?", "What are the three branches of government?"],
        "answer": (
            "The Constitution splits power among three branches: Congress makes laws, the President carries them "
            "out, and the courts interpret them. Each can check the others, for example with vetoes, Senate "
            "confirmation of judges, and judicial review, so no one branch gets too powerful."
        ),
        "cases": ["Marbury v. Madison", "United States v. Nixon"],
        "passages": ["a1s1", "a2s1", "a3s1"], "quote": "All legislative Powers herein granted shall be vested in a Congress of the United States",
    },
    {
        "asks": ["What is treason?"],
        "answer": (
            "Treason is the only crime defined in the Constitution, and the definition is narrow on purpose: waging "
            "war against the U.S. or helping its enemies. A conviction needs two witnesses to the same act or a "
            "confession in court."
        ),
        "passages": ["a3s3"], "quote": "Treason against the United States, shall consist only in levying War against them, or in adhering to their Enemies, giving them Aid and Comfort",
    },
    {
        "asks": ["Can soldiers stay in my house?", "What is the third amendment?"],
        "answer": (
            "Not in peacetime without your permission, and in wartime only as a law allows. Colonists had been forced "
            "to house British soldiers, so the founders ruled it out."
        ),
        "passages": ["am3"], "quote": "No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner",
    },
    {
        "asks": ["Is alcohol legal?", "What was Prohibition?"],
        "answer": (
            "The 18th Amendment banned alcohol nationwide in 1920 (Prohibition), and the 21st Amendment repealed it in "
            "1933. Today each state makes its own alcohol laws, and every state sets the drinking age at 21."
        ),
        "passages": ["am21", "am18"], "quote": "The eighteenth article of amendment to the Constitution of the United States is hereby repealed",
    },
]
