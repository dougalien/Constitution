"""Supreme Court cases, interpretation debates, fun facts and quiz questions.

Everything here is written for high school readers and kept nonpartisan: debates give the
strongest version of each side and never pick a winner. `related` lists passage ids from
constitution.py so the app can link cases and debates to the text.
"""

# ------------------------------------------------------------------ Supreme Court cases
# vote is the vote on the main holding; topic groups cases in the app
CASES = [
    {
        "name": "Marbury v. Madison", "year": 1803, "vote": "4–0", "topic": "Power of the courts",
        "question": "Can the Supreme Court cancel a law passed by Congress if it conflicts with the Constitution?",
        "decision": (
            "Yes. Chief Justice John Marshall wrote that \"it is emphatically the province and duty of the judicial "
            "department to say what the law is.\" A law that conflicts with the Constitution is void."
        ),
        "matters": (
            "This established judicial review, the courts' power to strike down unconstitutional laws. The word "
            "isn't in the Constitution, yet it became one of the most important checks and balances."
        ),
        "related": ["a3s2", "a6"],
        "keywords": "judicial review courts strike down laws unconstitutional marshall checks and balances",
    },
    {
        "name": "McCulloch v. Maryland", "year": 1819, "vote": "7–0", "topic": "Federal and state power",
        "question": "Could Congress create a national bank, and could Maryland tax it?",
        "decision": (
            "Congress could create the bank under the Necessary and Proper Clause even though banks aren't listed in "
            "its powers, and a state can't tax the federal government (\"the power to tax involves the power to "
            "destroy\")."
        ),
        "matters": "It confirmed implied powers and federal supremacy over conflicting state laws.",
        "related": ["a1s8", "a6", "am10"],
        "keywords": "implied powers necessary and proper elastic clause national bank federalism supremacy",
    },
    {
        "name": "Gibbons v. Ogden", "year": 1824, "vote": "6–0", "topic": "Federal and state power",
        "question": "Could New York give one company a monopoly on steamboats crossing to New Jersey?",
        "decision": "No. Trade between states includes navigation, and Congress, not states, regulates it.",
        "matters": "It was the first big reading of the Commerce Clause and gave Congress broad power over interstate trade.",
        "related": ["a1s8"],
        "keywords": "commerce clause interstate trade steamboat monopoly",
    },
    {
        "name": "Dred Scott v. Sandford", "year": 1857, "vote": "7–2", "topic": "Equal protection and civil rights",
        "question": "Could Dred Scott, an enslaved man taken to free territory, sue for his freedom?",
        "decision": (
            "No. The Court said Black Americans, free or enslaved, could not be U.S. citizens, and that Congress "
            "couldn't ban slavery in the territories."
        ),
        "matters": (
            "Widely considered the worst decision in the Court's history. It helped push the nation toward civil "
            "war and was overturned by the 13th and 14th Amendments."
        ),
        "related": ["am13", "am14"],
        "keywords": "slavery citizenship dred scott civil war worst decision overturned",
        "overruled": "Overturned by the 13th Amendment (1865) and the 14th Amendment (1868).",
    },
    {
        "name": "Plessy v. Ferguson", "year": 1896, "vote": "7–1", "topic": "Equal protection and civil rights",
        "question": "Could Louisiana require separate train cars for Black and white passengers?",
        "decision": (
            "Yes. The Court said \"separate but equal\" facilities did not violate equal protection. Justice John "
            "Marshall Harlan dissented: \"Our Constitution is color-blind.\""
        ),
        "matters": "It allowed legal segregation (Jim Crow laws) for nearly 60 years.",
        "related": ["am14"],
        "keywords": "segregation separate but equal jim crow race train harlan dissent",
        "overruled": "Overruled by Brown v. Board of Education (1954).",
    },
    {
        "name": "Korematsu v. United States", "year": 1944, "vote": "6–3", "topic": "Equal protection and civil rights",
        "question": "Could the government force Japanese Americans into incarceration camps during World War II?",
        "decision": "The Court upheld the order, citing wartime military necessity.",
        "matters": (
            "Now seen as a grave mistake. In 1988 Congress apologized and paid survivors, and in Trump v. Hawaii "
            "(2018) the Court said Korematsu \"was gravely wrong the day it was decided.\""
        ),
        "related": ["am5", "am14"],
        "keywords": "japanese american internment incarceration world war ii camps wartime race",
        "overruled": "Formally repudiated in Trump v. Hawaii (2018).",
    },
    {
        "name": "Wickard v. Filburn", "year": 1942, "vote": "9–0", "topic": "Federal and state power",
        "question": "Could Congress limit how much wheat a farmer grew for use on his own farm?",
        "decision": (
            "Yes. Even wheat that never left the farm, added up across many farms, affects the national market, so "
            "Congress could regulate it under the Commerce Clause."
        ),
        "matters": "It hugely expanded federal power and is still at the center of debates over the Commerce Clause.",
        "related": ["a1s8", "am10"],
        "keywords": "commerce clause wheat farmer federal power new deal",
    },
    {
        "name": "Brown v. Board of Education", "year": 1954, "vote": "9–0", "topic": "Equal protection and civil rights",
        "question": "Does segregating public schools by race violate the Constitution?",
        "decision": (
            "Yes. Chief Justice Earl Warren wrote that \"separate educational facilities are inherently unequal,\" "
            "violating equal protection."
        ),
        "matters": "It overruled Plessy v. Ferguson and became a turning point for the civil rights movement.",
        "related": ["am14"],
        "keywords": "school segregation desegregation race equal protection civil rights students schools",
    },
    {
        "name": "Mapp v. Ohio", "year": 1961, "vote": "6–3", "topic": "Rights of the accused",
        "question": "Can evidence found in an illegal police search be used in a state trial?",
        "decision": "No. Illegally obtained evidence must be left out of state trials too (the exclusionary rule).",
        "matters": "It gave the 4th Amendment real force against state and local police.",
        "related": ["am4", "am14"],
        "keywords": "exclusionary rule illegal search evidence police warrant",
    },
    {
        "name": "Engel v. Vitale", "year": 1962, "vote": "6–1", "topic": "Freedom of religion",
        "question": "Can a public school lead students in an official daily prayer?",
        "decision": "No. Even a voluntary, nondenominational prayer written by the state violates the Establishment Clause.",
        "matters": (
            "It's why public schools don't lead prayers. Students can still pray on their own, and religious "
            "clubs can meet like other clubs."
        ),
        "related": ["am1"],
        "keywords": "school prayer religion establishment clause church and state students",
    },
    {
        "name": "Gideon v. Wainwright", "year": 1963, "vote": "9–0", "topic": "Rights of the accused",
        "question": "Must a state give a lawyer to a person who is charged with a serious crime and can't afford one?",
        "decision": "Yes. A fair trial requires a lawyer, so states must provide one.",
        "matters": (
            "Clarence Gideon wrote his appeal by hand from prison. The case created the public defender system "
            "used across the country."
        ),
        "related": ["am6", "am14"],
        "keywords": "right to a lawyer attorney public defender counsel poor fair trial",
    },
    {
        "name": "Miranda v. Arizona", "year": 1966, "vote": "5–4", "topic": "Rights of the accused",
        "question": "Must police tell suspects about their rights before questioning them?",
        "decision": (
            "Yes. Before questioning someone in custody, police must warn them that they have the right to remain "
            "silent, that what they say can be used against them, and that they have a right to a lawyer."
        ),
        "matters": "This is where the \"Miranda warning\" you hear in TV shows comes from.",
        "related": ["am5", "am6"],
        "keywords": "miranda rights right to remain silent police questioning arrest interrogation",
    },
    {
        "name": "Loving v. Virginia", "year": 1967, "vote": "9–0", "topic": "Equal protection and civil rights",
        "question": "Could a state ban people of different races from marrying?",
        "decision": "No. Such bans violate both equal protection and due process.",
        "matters": "It ended laws against interracial marriage in 16 states.",
        "related": ["am14"],
        "keywords": "interracial marriage race equal protection due process",
    },
    {
        "name": "Tinker v. Des Moines", "year": 1969, "vote": "7–2", "topic": "Students' rights",
        "question": "Could a school suspend students for wearing black armbands to protest the Vietnam War?",
        "decision": (
            "No. Students don't \"shed their constitutional rights to freedom of speech or expression at the "
            "schoolhouse gate.\" Schools can limit speech only if it would substantially disrupt school."
        ),
        "matters": "It is the foundation of students' free speech rights. Mary Beth Tinker was 13 when she wore her armband.",
        "related": ["am1"],
        "keywords": "students free speech school protest armbands schoolhouse gate student rights",
    },
    {
        "name": "New York Times Co. v. United States", "year": 1971, "vote": "6–3", "topic": "Freedom of speech and press",
        "question": "Could the government stop newspapers from publishing the secret Pentagon Papers about the Vietnam War?",
        "decision": "No. The government had not met the heavy burden needed to block publication in advance (prior restraint).",
        "matters": "It's a landmark for freedom of the press.",
        "related": ["am1"],
        "keywords": "freedom of the press newspapers pentagon papers prior restraint censorship",
    },
    {
        "name": "Roe v. Wade", "year": 1973, "vote": "7–2", "topic": "Privacy and unlisted rights",
        "question": "Does the Constitution protect a right to choose to have an abortion?",
        "decision": "The Court held that the 14th Amendment's protection of liberty included a right to abortion, with limits later in pregnancy.",
        "matters": "One of the most debated decisions in the Court's history, it shaped national politics for nearly 50 years.",
        "related": ["am9", "am14"],
        "keywords": "abortion privacy due process liberty",
        "overruled": "Overruled by Dobbs v. Jackson Women's Health Organization (2022).",
    },
    {
        "name": "United States v. Nixon", "year": 1974, "vote": "8–0", "topic": "Presidential power",
        "question": "Did President Nixon have to turn over secret White House tape recordings for a criminal trial?",
        "decision": "Yes. Executive privilege is real but not absolute, and it yields to the needs of a criminal trial.",
        "matters": "The tapes revealed Nixon's role in the Watergate cover-up; he resigned two weeks later. No one is above the law.",
        "related": ["a2s1", "a2s4", "a3s2"],
        "keywords": "nixon watergate executive privilege tapes president above the law resign",
    },
    {
        "name": "New Jersey v. T.L.O.", "year": 1985, "vote": "6–3", "topic": "Students' rights",
        "question": "Could a school official search a student's purse without a warrant?",
        "decision": (
            "Yes. The 4th Amendment applies at school, but officials need only \"reasonable suspicion\" that a "
            "student broke a law or school rule, not a warrant or probable cause."
        ),
        "matters": "It sets the rule for searches of students' bags and lockers.",
        "related": ["am4"],
        "keywords": "school search student purse backpack locker reasonable suspicion student rights",
    },
    {
        "name": "Hazelwood v. Kuhlmeier", "year": 1988, "vote": "5–3", "topic": "Students' rights",
        "question": "Could a principal remove articles from a school-sponsored student newspaper?",
        "decision": "Yes. Schools can edit school-sponsored publications for reasons tied to legitimate teaching concerns.",
        "matters": "It limits student press rights in school-run activities. Some states have since passed laws giving student journalists more protection.",
        "related": ["am1"],
        "keywords": "student newspaper school press censorship journalism student rights",
    },
    {
        "name": "Texas v. Johnson", "year": 1989, "vote": "5–4", "topic": "Freedom of speech and press",
        "question": "Is burning the American flag in protest protected speech?",
        "decision": "Yes. Flag burning is symbolic expression, and the government can't ban it because the message offends people.",
        "matters": "It shows that free speech protects even ideas that most people find offensive.",
        "related": ["am1"],
        "keywords": "flag burning symbolic speech protest offensive speech expression",
    },
    {
        "name": "United States v. Lopez", "year": 1995, "vote": "5–4", "topic": "Federal and state power",
        "question": "Could Congress use the Commerce Clause to ban guns near schools?",
        "decision": "No. Carrying a gun near a school is not economic activity, so it was outside the Commerce Clause.",
        "matters": "It was the first time in nearly 60 years the Court said Congress went too far under the Commerce Clause.",
        "related": ["a1s8", "am10"],
        "keywords": "commerce clause guns school zones federalism limits on congress",
    },
    {
        "name": "Morse v. Frederick", "year": 2007, "vote": "5–4", "topic": "Students' rights",
        "question": "Could a school punish a student for a \"BONG HiTS 4 JESUS\" banner at a school event?",
        "decision": "Yes. Schools can restrict student speech they reasonably see as promoting illegal drug use.",
        "matters": "It added a limit to Tinker for speech about illegal drugs.",
        "related": ["am1"],
        "keywords": "student speech banner drugs school event student rights",
    },
    {
        "name": "District of Columbia v. Heller", "year": 2008, "vote": "5–4", "topic": "Right to bear arms",
        "question": "Does the 2nd Amendment protect an individual's right to own a gun, apart from militia service?",
        "decision": "Yes. It protects an individual right to keep a handgun at home for self-defense, though some regulations remain allowed.",
        "matters": "It settled a long debate about the amendment's meaning and opened many new questions about gun laws.",
        "related": ["am2"],
        "keywords": "guns second amendment individual right handgun self defense militia gun control",
    },
    {
        "name": "Citizens United v. FEC", "year": 2010, "vote": "5–4", "topic": "Freedom of speech and press",
        "question": "Can the government limit how much corporations and unions spend independently on political ads?",
        "decision": "No. Independent political spending is protected speech, even by corporations and unions.",
        "matters": "It reshaped campaign spending. Supporters see it as protecting speech; critics worry about the influence of money in elections.",
        "related": ["am1"],
        "keywords": "campaign finance money in politics corporations elections speech super pacs",
    },
    {
        "name": "Shelby County v. Holder", "year": 2013, "vote": "5–4", "topic": "Voting",
        "question": "Was the Voting Rights Act formula requiring some states to get federal approval before changing voting rules still constitutional?",
        "decision": "No. The formula relied on decades-old data, so it could no longer be used unless Congress updated it.",
        "matters": "States that had needed approval could change voting rules without it. People still debate its effects.",
        "related": ["am15", "am10"],
        "keywords": "voting rights act preclearance voting rules elections race",
    },
    {
        "name": "Riley v. California", "year": 2014, "vote": "9–0", "topic": "Rights of the accused",
        "question": "Can police search the cell phone of someone they arrest without a warrant?",
        "decision": "Generally no. Chief Justice Roberts wrote that the answer is simple: \"get a warrant.\"",
        "matters": "It brought the 4th Amendment into the smartphone age.",
        "related": ["am4"],
        "keywords": "cell phone search warrant privacy police smartphone digital",
    },
    {
        "name": "Obergefell v. Hodges", "year": 2015, "vote": "5–4", "topic": "Equal protection and civil rights",
        "question": "Does the Constitution require states to allow and recognize same-sex marriages?",
        "decision": "Yes. The Court held that the 14th Amendment's due process and equal protection guarantees include the right to marry for same-sex couples.",
        "matters": "It made same-sex marriage legal nationwide.",
        "related": ["am14"],
        "keywords": "same sex marriage gay marriage equal protection due process",
    },
    {
        "name": "Mahanoy Area School District v. B.L.", "year": 2021, "vote": "8–1", "topic": "Students' rights",
        "question": "Could a school punish a cheerleader for a profane Snapchat post made off campus on a weekend?",
        "decision": "No, not in this case. Schools have less power over off-campus speech, though not none.",
        "matters": "It's the main case on students' social media and off-campus speech.",
        "related": ["am1"],
        "keywords": "social media snapchat off campus student speech cheerleader online",
    },
    {
        "name": "Dobbs v. Jackson Women's Health Organization", "year": 2022, "vote": "6–3", "topic": "Privacy and unlisted rights",
        "question": "Does the Constitution protect a right to abortion?",
        "decision": (
            "The Court held that it does not, overruling Roe v. Wade (the vote to overrule Roe was 5–4). Each state "
            "can now make its own abortion laws."
        ),
        "matters": "It returned abortion law to the states and reopened debate over which unlisted rights the Constitution protects.",
        "related": ["am9", "am10", "am14"],
        "keywords": "abortion roe overruled states privacy due process",
    },
    {
        "name": "New York State Rifle & Pistol Association v. Bruen", "year": 2022, "vote": "6–3", "topic": "Right to bear arms",
        "question": "Could New York require people to show a special need before getting a license to carry a handgun in public?",
        "decision": "No. Gun laws must fit the nation's historical tradition of firearm regulation.",
        "matters": "It created a history-based test that courts now use for gun laws.",
        "related": ["am2"],
        "keywords": "guns concealed carry license public history test second amendment",
    },
    {
        "name": "Kennedy v. Bremerton School District", "year": 2022, "vote": "6–3", "topic": "Freedom of religion",
        "question": "Could a public school discipline a football coach for praying on the field after games?",
        "decision": "No. His brief personal prayer was protected by the Free Exercise and Free Speech Clauses.",
        "matters": "It changed how courts decide Establishment Clause cases, looking to history and tradition.",
        "related": ["am1"],
        "keywords": "coach prayer football school religion free exercise establishment",
    },
    {
        "name": "Students for Fair Admissions v. Harvard", "year": 2023, "vote": "6–3 (UNC); 6–2 (Harvard)", "topic": "Equal protection and civil rights",
        "question": "Can colleges consider an applicant's race in admissions?",
        "decision": (
            "No. The Court said race-conscious admissions programs at Harvard and the University of North Carolina "
            "violated equal protection. Applicants can still write about how race affected their lives."
        ),
        "matters": "It ended affirmative action in college admissions as it had been practiced for decades.",
        "related": ["am14"],
        "keywords": "affirmative action college admissions race equal protection harvard",
    },
    {
        "name": "Trump v. Anderson", "year": 2024, "vote": "9–0", "topic": "Voting",
        "question": "Could Colorado remove a presidential candidate from its ballot under Section 3 of the 14th Amendment?",
        "decision": "No. Only Congress, not individual states, can enforce Section 3 against federal officeholders and candidates.",
        "matters": "It was the Court's first major ruling on the insurrection clause of the 14th Amendment.",
        "related": ["am14"],
        "keywords": "section 3 insurrection ballot candidate fourteenth amendment colorado",
    },
    {
        "name": "Trump v. United States", "year": 2024, "vote": "6–3", "topic": "Presidential power",
        "question": "Can a former President be prosecuted for actions taken while in office?",
        "decision": (
            "The Court held that a former President has absolute immunity for actions within core constitutional "
            "powers, presumed immunity for other official acts, and no immunity for unofficial acts."
        ),
        "matters": "It was the first ruling on presidential immunity from criminal charges, and it is strongly debated.",
        "related": ["a2s1", "a2s4"],
        "keywords": "presidential immunity president prosecute crimes official acts executive power",
    },
    {
        "name": "Learning Resources v. Trump", "year": 2026, "vote": "6–3", "topic": "Presidential power",
        "question": "Could the President use an emergency law (the International Emergency Economic Powers Act) to put tariffs, which are taxes on imports, on goods from other countries?",
        "decision": (
            "No. The law lets the President \"regulate\" imports in an emergency, but that doesn't include taxing "
            "them. Chief Justice Roberts noted that \"the Framers did not vest any part of the taxing power in the "
            "Executive Branch.\""
        ),
        "matters": "It's a modern example of Article I at work: the power to tax, including tariffs, belongs to Congress unless Congress clearly hands it over.",
        "related": ["a1s8", "a2s1"],
        "keywords": "tariffs taxes imports trade president emergency powers congress taxing power",
    },
    {
        "name": "Trump v. Slaughter", "year": 2026, "vote": "6–3", "topic": "Presidential power",
        "question": "Could Congress stop the President from firing a member of the Federal Trade Commission (FTC) without a good reason?",
        "decision": (
            "No. Because the FTC carries out executive power, the President may remove its commissioners at will. "
            "The Court said that if anything was left of Humphrey's Executor v. United States (1935), which had "
            "allowed such limits, it was overruled."
        ),
        "matters": "It gives the President more control over independent agencies. Supporters call it accountability; critics worry about losing independent expertise.",
        "related": ["a2s1", "a2s2", "a2s3"],
        "keywords": "fire remove removal power independent agencies ftc president executive power",
    },
    {
        "name": "Trump v. Barbara", "year": 2026, "vote": "6–3 (5–4 on the constitutional reasoning)",
        "topic": "Equal protection and civil rights",
        "question": "Could an executive order deny citizenship to children born in the U.S. whose parents were here unlawfully or only temporarily?",
        "decision": (
            "No. The Court held that such children are \"subject to the jurisdiction\" of the United States and are "
            "citizens at birth under the 14th Amendment's Citizenship Clause. Justice Kavanaugh agreed with the result "
            "but would have decided it under a federal law instead of the Constitution."
        ),
        "matters": "It confirmed birthright citizenship, the rule since United States v. Wong Kim Ark (1898), for nearly everyone born on U.S. soil.",
        "related": ["am14"],
        "keywords": "birthright citizenship born in the united states citizen immigrants fourteenth amendment executive order",
    },
]

# ------------------------------------------------------------------ Big debates
DEBATES = [
    {
        "title": "How should judges read the Constitution?",
        "intro": (
            "The words were written in 1787. Judges, lawyers and citizens disagree about how to apply them to a "
            "world with the internet, modern weapons and new social questions."
        ),
        "side_a": ("Originalism and textualism",
                   "Read the words as they were understood when they were adopted. This keeps judges from inserting "
                   "their own views, makes the law predictable, and leaves change to the amendment process and voters."),
        "side_b": ("Living constitutionalism",
                   "The founders used broad words like \"liberty\" and \"cruel and unusual\" on purpose, so the "
                   "meaning can grow with society. Amending is very hard, and a 1787 reading can lock in old injustices."),
        "think": "Many judges mix both approaches. When might each one lead to a better or worse result?",
        "cases": ["District of Columbia v. Heller", "Brown v. Board of Education", "Dobbs v. Jackson Women's Health Organization"],
        "related": ["a5", "am9", "am14"],
        "keywords": "interpretation originalism textualism living constitution judges how to read meaning",
    },
    {
        "title": "Should unelected judges be able to strike down laws?",
        "intro": "Judicial review isn't spelled out in the Constitution. The Court claimed it in Marbury v. Madison.",
        "side_a": ("Judicial review protects rights",
                   "A written constitution means little if no one enforces it. Courts protect minorities and "
                   "individual rights from majorities, as in Brown v. Board of Education."),
        "side_b": ("Leave more to elected officials",
                   "Judges serve for life and aren't elected, so big social choices should mostly be made by voters "
                   "and their representatives. Courts have also made terrible mistakes, like Dred Scott."),
        "think": "Who should have the final word on what the Constitution means: courts, Congress, the President, or the people?",
        "cases": ["Marbury v. Madison", "Brown v. Board of Education", "Dred Scott v. Sandford"],
        "related": ["a3s1", "a3s2", "a6"],
        "keywords": "judicial review courts power unelected judges strike down laws activism restraint",
    },
    {
        "title": "How much power should the national government have compared with the states?",
        "intro": "This is the debate over federalism, and it goes back to the founding.",
        "side_a": ("A strong national government",
                   "Many problems cross state lines, like the economy, pollution and civil rights. National rules "
                   "protect everyone equally, and the Commerce and Necessary and Proper Clauses give Congress room to act."),
        "side_b": ("More power to the states",
                   "The 10th Amendment reserves powers to the states. States are closer to the people, can try "
                   "different ideas (\"laboratories of democracy\"), and limiting national power protects liberty."),
        "think": "Pick an issue like schools, marijuana laws or driving ages. Should it be decided nationally or by each state?",
        "cases": ["McCulloch v. Maryland", "Wickard v. Filburn", "United States v. Lopez"],
        "related": ["a1s8", "a6", "am10"],
        "keywords": "federalism states rights national government federal power commerce clause tenth amendment",
    },
    {
        "title": "Where are the limits of free speech?",
        "intro": "The 1st Amendment says \"Congress shall make no law... abridging the freedom of speech,\" yet some speech is not protected.",
        "side_a": ("Protect speech broadly",
                   "The answer to bad speech is more speech. Letting the government decide what's too offensive is "
                   "dangerous because those in power could silence critics."),
        "side_b": ("Some limits protect people",
                   "Threats, harassment and dangerous lies can cause real harm. Reasonable limits, like those at "
                   "schools, help protect others' rights and safety."),
        "think": "Should social media companies, which are private and not bound by the 1st Amendment, follow free speech principles anyway?",
        "cases": ["Tinker v. Des Moines", "Texas v. Johnson", "Mahanoy Area School District v. B.L.", "Citizens United v. FEC"],
        "related": ["am1"],
        "keywords": "free speech limits hate speech offensive social media censorship misinformation",
    },
    {
        "title": "What does the 2nd Amendment allow?",
        "intro": "Americans disagree strongly about guns. The courts have set some rules, and many questions remain open.",
        "side_a": ("Broad individual right",
                   "\"The right of the people... shall not be infringed\" protects individuals, as the Court held in "
                   "Heller. Self-defense is a basic right, and strict gun laws mostly burden law-abiding people."),
        "side_b": ("More room for regulation",
                   "The amendment begins with \"a well regulated Militia,\" and communities should be able to pass "
                   "safety laws. Even Heller said some regulations, like bans for people with felony convictions, are allowed."),
        "think": "How should courts apply a 1791 amendment to modern firearms and modern safety concerns?",
        "cases": ["District of Columbia v. Heller", "New York State Rifle & Pistol Association v. Bruen", "United States v. Lopez"],
        "related": ["am2"],
        "keywords": "guns gun control second amendment firearms regulation militia",
    },
    {
        "title": "How separate should church and state be?",
        "intro": "The 1st Amendment both forbids an \"establishment of religion\" and protects \"free exercise.\" Sometimes those pull in different directions.",
        "side_a": ("A high wall of separation",
                   "Thomas Jefferson described a \"wall of separation.\" Government, including public schools, should "
                   "stay neutral so no one feels pressured about religion."),
        "side_b": ("Room for religion in public life",
                   "Religion has always been part of American public life. Banning religious expression can itself "
                   "violate free exercise and free speech."),
        "think": "Should a public school coach be allowed to pray on the field? What if players feel pressure to join?",
        "cases": ["Engel v. Vitale", "Kennedy v. Bremerton School District"],
        "related": ["am1", "a6"],
        "keywords": "church and state religion establishment clause free exercise school prayer separation",
    },
    {
        "title": "How much power should the President have?",
        "intro": "Article II is short and leaves a lot unsaid, so the limits of presidential power are often argued over.",
        "side_a": ("A strong executive",
                   "The President is the only official elected by the whole nation and must act fast in crises. "
                   "Alexander Hamilton argued for \"energy in the executive.\""),
        "side_b": ("Strict checks",
                   "The founders feared a king. Congress declares war and writes laws; executive orders and emergency "
                   "powers shouldn't replace them."),
        "think": "Presidents have sent troops into combat without a declaration of war many times. Who should decide when the country fights?",
        "cases": ["United States v. Nixon", "Trump v. United States", "Learning Resources v. Trump", "Trump v. Slaughter"],
        "related": ["a1s8", "a2s1", "a2s2", "a2s3"],
        "keywords": "presidential power executive orders war powers emergency immunity checks and balances",
    },
    {
        "title": "What does \"equal protection\" require?",
        "intro": "The 14th Amendment requires \"equal protection of the laws.\" People disagree on how to achieve equality.",
        "side_a": ("A colorblind approach",
                   "Government should never sort people by race, even to help. Equal treatment means treating each "
                   "person as an individual."),
        "side_b": ("A race-conscious approach",
                   "Because of past discrimination, treating everyone the same may keep old inequalities in place. "
                   "Some race-conscious policies can help reach real equality."),
        "think": "Both sides quote Justice Harlan's Plessy dissent and Brown v. Board. Why might each side see support in those cases?",
        "cases": ["Plessy v. Ferguson", "Brown v. Board of Education", "Students for Fair Admissions v. Harvard"],
        "related": ["am14"],
        "keywords": "equal protection affirmative action race discrimination colorblind equality",
    },
    {
        "title": "Which rights exist even if they aren't written down?",
        "intro": "The 9th Amendment says unlisted rights exist. Courts have recognized some through the 14th Amendment's word \"liberty.\"",
        "side_a": ("Courts should protect unlisted rights",
                   "The founders said the list isn't complete. Rights like marrying who you love or raising your "
                   "children as you choose deserve protection even though they aren't listed."),
        "side_b": ("Leave unlisted questions to voters",
                   "If judges can find rights not in the text, they can impose their own views. Rights should be "
                   "deeply rooted in the nation's history, or else decided by elected lawmakers."),
        "think": "Who should decide new questions, like privacy in the age of smartphones and AI: courts or legislatures?",
        "cases": ["Loving v. Virginia", "Roe v. Wade", "Obergefell v. Hodges", "Dobbs v. Jackson Women's Health Organization"],
        "related": ["am9", "am14"],
        "keywords": "unenumerated rights privacy unlisted rights due process liberty marriage abortion",
    },
    {
        "title": "Keep or change the Electoral College?",
        "intro": "The President is chosen by electors, not directly by the national popular vote. Five times the popular vote winner lost.",
        "side_a": ("Keep it",
                   "It makes candidates pay attention to many states, not just big cities, respects the role of "
                   "states in a federal system, and keeps disputes contained within single states."),
        "side_b": ("Change it",
                   "Every vote should count equally, wherever you live. Today campaigns focus on a few swing states, "
                   "and a candidate can win with fewer total votes."),
        "think": "Changing it would take a constitutional amendment. Could it pass? Why or why not?",
        "cases": [],
        "related": ["a2s1", "am12", "a5"],
        "keywords": "electoral college popular vote president election swing states",
    },
]

# ------------------------------------------------------------------ Fun facts
FACTS = [
    "The Constitution is often called the oldest written national constitution still in use.",
    "The original Constitution is just four pages long. You can see it at the National Archives in Washington, D.C.",
    "Rhode Island refused to send anyone to the Constitutional Convention and was the last of the 13 states to ratify, in 1790.",
    "Benjamin Franklin, 81, was the oldest delegate at the Convention. Jonathan Dayton of New Jersey, 26, was the youngest.",
    "Of the 55 delegates who attended the Convention, only 39 signed the Constitution.",
    "Thomas Jefferson and John Adams didn't help write the Constitution. Both were in Europe as diplomats.",
    "A clerk named Jacob Shallus handwrote the final copy of the Constitution. He was paid $30.",
    "\"Pennsylvania\" is spelled \"Pensylvania\" in the list of signers.",
    "The word \"democracy\" doesn't appear anywhere in the Constitution.",
    "The 27th Amendment was proposed in 1789 and ratified in 1992. A college student, Gregory Watson, restarted the push after writing a paper about it. He got a C on that paper; his grade was changed to an A in 2017.",
    "The 26th Amendment, which lowered the voting age to 18, was ratified in about 100 days, the fastest ever.",
    "The 21st Amendment is the only one that canceled another amendment (the 18th, Prohibition).",
    "The Constitution never says how many justices sit on the Supreme Court. It started with 6 and has had 9 since 1869.",
    "You don't need to be a lawyer to be a Supreme Court justice, according to the Constitution. Every justice so far has had legal training, though.",
    "The phrase \"Electoral College\" isn't in the Constitution. It just says \"Electors.\"",
    "Treason is the only crime defined in the Constitution.",
    "The presidential oath is the only oath written out word for word in the Constitution.",
    "Patrick Henry refused to attend the Convention, reportedly saying he \"smelt a rat.\"",
    "James Madison is called the \"Father of the Constitution.\" His detailed notes are our best record of the secret Convention debates.",
    "The Convention met in secret, and the windows were often kept shut, during a hot Philadelphia summer.",
    "Over 11,000 amendments have been proposed in Congress. Only 27 have been ratified.",
    "Madison's first proposed amendments included one about the size of the House. It never got enough states and is still technically pending.",
    "September 17 is Constitution Day, the anniversary of the signing in 1787. Schools that get federal funding must teach about the Constitution that day.",
    "The Constitution sets the minimum ages for federal office: 25 for the House, 30 for the Senate and 35 for President.",
    "George Washington was the only President elected unanimously by the Electoral College, and he did it twice.",
    "The 3rd Amendment, about housing soldiers, has almost never been the main issue in a Supreme Court case.",
    "Each state, from Wyoming to California, gets exactly two senators. That rule is the one part of the Constitution that can't be amended without a state's consent.",
    "The Bill of Rights was ratified in 1791. Massachusetts, Connecticut and Georgia didn't formally approve it until 1939, as a symbolic gesture for its 150th anniversary.",
    "The Constitution's Preamble starts with \"We the People,\" but the first draft listed each state by name.",
    "Under the Articles of Confederation, the government before the Constitution, Congress couldn't collect taxes. That weakness was a big reason for writing a new constitution.",
]

# ------------------------------------------------------------------ Quiz
# (question, choices, index of correct answer, explanation)
QUIZ = [
    ("How old must you be to serve as President?", ["30", "35", "40", "25"], 1,
     "Article II, Section 1 sets 35 as the minimum age."),
    ("Which branch makes federal laws?", ["Executive", "Judicial", "Legislative", "The states"], 2,
     "Article I gives \"all legislative Powers\" to Congress."),
    ("How many senators does each state have?", ["It depends on population", "1", "2", "3"], 2,
     "Article I, Section 3 and the 17th Amendment give each state two senators."),
    ("Which amendment protects freedom of speech?", ["1st", "2nd", "5th", "14th"], 0,
     "The 1st Amendment protects speech, religion, press, assembly and petition."),
    ("What does \"pleading the Fifth\" mean?", ["Asking for a lawyer", "Refusing to testify against yourself",
                                               "Asking for a jury", "Appealing a case"], 1,
     "The 5th Amendment says no one can be forced to be a witness against themselves."),
    ("How does Congress override a presidential veto?", ["Simple majority in the House",
                                                         "Two-thirds vote in both House and Senate",
                                                         "Supreme Court approval", "Three fourths of the states"], 1,
     "Article I, Section 7: two thirds of each chamber can override a veto."),
    ("Which case established judicial review?", ["Brown v. Board", "Marbury v. Madison", "Miranda v. Arizona",
                                                 "McCulloch v. Maryland"], 1,
     "Marbury v. Madison (1803) said courts can strike down laws that conflict with the Constitution."),
    ("Which amendment lowered the voting age to 18?", ["19th", "24th", "26th", "15th"], 2,
     "The 26th Amendment (1971)."),
    ("How many states must ratify an amendment?", ["Half", "Two thirds", "Three fourths", "All of them"], 2,
     "Article V requires three fourths of the states, which is 38 today."),
    ("In Tinker v. Des Moines, students protested by wearing...", ["T-shirts", "Black armbands", "Buttons", "Flags"], 1,
     "The Court said students don't lose free speech rights \"at the schoolhouse gate.\""),
    ("Who has the power to declare war?", ["The President", "The Secretary of Defense", "Congress",
                                           "The Supreme Court"], 2,
     "Article I, Section 8 gives Congress the power to declare war."),
    ("Which amendment abolished slavery?", ["13th", "14th", "15th", "19th"], 0,
     "The 13th Amendment (1865)."),
    ("Which amendment gave women the right to vote nationwide?", ["15th", "17th", "19th", "26th"], 2,
     "The 19th Amendment (1920)."),
    ("What did Brown v. Board of Education decide?", ["Schools can lead prayers",
                                                       "Segregated public schools are unconstitutional",
                                                       "Students can be searched without a warrant",
                                                       "Flag burning is protected speech"], 1,
     "In 1954 the Court ruled 9–0 that \"separate educational facilities are inherently unequal.\""),
    ("How long is a term in the House of Representatives?", ["2 years", "4 years", "6 years", "Life"], 0,
     "Article I, Section 2: members are chosen every second year."),
    ("Which clause lets Congress pass laws needed to carry out its listed powers?", ["Commerce Clause",
                                                                                     "Supremacy Clause",
                                                                                     "Necessary and Proper Clause",
                                                                                     "Take Care Clause"], 2,
     "Also called the Elastic Clause, at the end of Article I, Section 8."),
    ("What is the only crime defined in the Constitution?", ["Bribery", "Treason", "Murder", "Counterfeiting"], 1,
     "Article III, Section 3 defines treason."),
    ("Which amendment is the only one ever repealed?", ["18th (Prohibition)", "16th (income tax)",
                                                        "22nd (term limits)", "3rd (soldiers)"], 0,
     "The 21st Amendment repealed the 18th in 1933."),
    ("What does the Supremacy Clause say?", ["The President is supreme", "State laws beat federal laws",
                                             "The Constitution and federal laws are the supreme law of the land",
                                             "The Supreme Court can't be overruled"], 2,
     "Article VI: if state and federal law conflict, federal law (made under the Constitution) wins."),
    ("Usually, what do police need to search your home?", ["A neighbor's permission", "A warrant based on probable cause",
                                                            "A phone call to the mayor", "Nothing"], 1,
     "The 4th Amendment requires warrants based on probable cause, with some exceptions."),
    ("How many amendments have been ratified?", ["10", "21", "27", "33"], 2,
     "27 amendments; the first ten are the Bill of Rights."),
    ("Who becomes President if the President dies?", ["Speaker of the House", "Vice President", "Chief Justice",
                                                      "Secretary of State"], 1,
     "Article II and the 25th Amendment."),
    ("Who must confirm Supreme Court justices?", ["The House", "The Senate", "The states", "The voters"], 1,
     "Article II, Section 2: the President nominates, and the Senate gives \"advice and consent.\""),
    ("Gideon v. Wainwright guaranteed what?", ["A lawyer if you can't afford one", "The right to remain silent",
                                               "A speedy trial", "Freedom of the press"], 0,
     "The 1963 case applied the 6th Amendment's right to counsel to the states."),
]
