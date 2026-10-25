"""The text of the U.S. Constitution, piece by piece, with a plain-language explanation of each piece.

The wording is checked word for word against the official text printed in the House Manual by the
U.S. Government Publishing Office (run `python check_text.py`). It keeps the original spelling
("chuse", "defence") and capitalization. Parts later changed by an amendment keep their original
wording and carry a `changed` note, as the Archives does.

Each passage has:
    id        short key, e.g. "a1s8"
    label     where it is, e.g. "Article I, Section 8"
    title     what it is about
    text      the original words
    plain     a short explanation in everyday language
    keywords  extra words people might use when asking about it (helps the search)
    changed   (optional) which amendment changed or replaced it
"""

PASSAGES = [
    # ------------------------------------------------------------------ Preamble
    {
        "id": "pre",
        "label": "Preamble",
        "title": "Why the Constitution was written",
        "text": (
            "We the People of the United States, in Order to form a more perfect Union, establish Justice, "
            "insure domestic Tranquility, provide for the common defence, promote the general Welfare, and "
            "secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this "
            "Constitution for the United States of America."
        ),
        "plain": (
            "The opening sentence says who is making the Constitution (the people, not the states or a king) "
            "and why: to make the country work better together, make laws fair, keep peace at home, defend "
            "the nation, help everyone live well, and protect freedom for today and for future generations. "
            "The Preamble does not give anyone powers by itself; it explains the goals of everything that follows."
        ),
        "keywords": "we the people purpose goals introduction beginning opening why reason more perfect union",
    },
    # ------------------------------------------------------------------ Article I: Congress
    {
        "id": "a1s1",
        "label": "Article I, Section 1",
        "title": "Congress makes the laws",
        "text": (
            "All legislative Powers herein granted shall be vested in a Congress of the United States, which "
            "shall consist of a Senate and House of Representatives."
        ),
        "plain": (
            "The power to make federal laws belongs to Congress. Congress has two parts, or chambers: the Senate "
            "and the House of Representatives. This is called a bicameral legislature. Note the words \"herein "
            "granted\": Congress only has the powers the Constitution gives it."
        ),
        "keywords": "legislative branch congress lawmaking make laws bicameral two houses separation of powers",
    },
    {
        "id": "a1s2",
        "label": "Article I, Section 2",
        "title": "The House of Representatives",
        "text": (
            "The House of Representatives shall be composed of Members chosen every second Year by the People of "
            "the several States, and the Electors in each State shall have the Qualifications requisite for "
            "Electors of the most numerous Branch of the State Legislature.\n\n"
            "No Person shall be a Representative who shall not have attained to the Age of twenty five Years, and "
            "been seven Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of "
            "that State in which he shall be chosen.\n\n"
            "Representatives and direct Taxes shall be apportioned among the several States which may be included "
            "within this Union, according to their respective Numbers, which shall be determined by adding to the "
            "whole Number of free Persons, including those bound to Service for a Term of Years, and excluding "
            "Indians not taxed, three fifths of all other Persons. The actual Enumeration shall be made within "
            "three Years after the first Meeting of the Congress of the United States, and within every subsequent "
            "Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not "
            "exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until "
            "such enumeration shall be made, the State of New Hampshire shall be entitled to chuse three, "
            "Massachusetts eight, Rhode-Island and Providence Plantations one, Connecticut five, New-York six, New "
            "Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South "
            "Carolina five, and Georgia three.\n\n"
            "When vacancies happen in the Representation from any State, the Executive Authority thereof shall issue "
            "Writs of Election to fill such Vacancies.\n\n"
            "The House of Representatives shall chuse their Speaker and other Officers; and shall have the sole "
            "Power of Impeachment."
        ),
        "plain": (
            "Members of the House are elected by the people every two years. To serve you must be at least 25, a "
            "citizen for 7 years, and live in the state you represent. Seats are divided among the states by "
            "population, counted in a census every ten years. The infamous \"three fifths\" clause counted enslaved "
            "people as three fifths of a person, which gave slave states more seats; the 14th Amendment replaced it. "
            "The House picks its own leader, the Speaker, and has the sole power to impeach (formally accuse) "
            "federal officials."
        ),
        "keywords": (
            "house of representatives representative congressman congresswoman age 25 qualifications requirements "
            "two years term census population count three fifths compromise slavery speaker impeachment "
            "apportionment seats districts"
        ),
        "changed": "The three-fifths clause was replaced by Section 2 of the 14th Amendment (1868).",
    },
    {
        "id": "a1s3",
        "label": "Article I, Section 3",
        "title": "The Senate",
        "text": (
            "The Senate of the United States shall be composed of two Senators from each State, chosen by the "
            "Legislature thereof, for six Years; and each Senator shall have one Vote.\n\n"
            "Immediately after they shall be assembled in Consequence of the first Election, they shall be divided "
            "as equally as may be into three Classes. The Seats of the Senators of the first Class shall be vacated "
            "at the Expiration of the second Year, of the second Class at the Expiration of the fourth Year, and of "
            "the third Class at the Expiration of the sixth Year, so that one third may be chosen every second Year; "
            "and if Vacancies happen by Resignation, or otherwise, during the Recess of the Legislature of any State, "
            "the Executive thereof may make temporary Appointments until the next Meeting of the Legislature, which "
            "shall then fill such Vacancies.\n\n"
            "No Person shall be a Senator who shall not have attained to the Age of thirty Years, and been nine Years "
            "a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State for "
            "which he shall be chosen.\n\n"
            "The Vice President of the United States shall be President of the Senate, but shall have no Vote, "
            "unless they be equally divided.\n\n"
            "The Senate shall chuse their other Officers, and also a President pro tempore, in the Absence of the "
            "Vice President, or when he shall exercise the Office of President of the United States.\n\n"
            "The Senate shall have the sole Power to try all Impeachments. When sitting for that Purpose, they shall "
            "be on Oath or Affirmation. When the President of the United States is tried, the Chief Justice shall "
            "preside: And no Person shall be convicted without the Concurrence of two thirds of the Members "
            "present.\n\n"
            "Judgment in Cases of Impeachment shall not extend further than to removal from Office, and "
            "disqualification to hold and enjoy any Office of honor, Trust or Profit under the United States: but "
            "the Party convicted shall nevertheless be liable and subject to Indictment, Trial, Judgment and "
            "Punishment, according to Law."
        ),
        "plain": (
            "Every state gets two senators, no matter its size, and they serve six-year terms. Terms are staggered "
            "so only about a third of the Senate is up for election every two years. Senators must be at least 30 "
            "and citizens for 9 years. The Vice President leads the Senate but votes only to break a tie. If the "
            "House impeaches someone, the Senate holds the trial, and it takes a two-thirds vote to convict and "
            "remove them from office. Originally state legislatures chose senators; since the 17th Amendment (1913), "
            "voters elect them directly."
        ),
        "keywords": (
            "senate senator senators two per state six years age 30 qualifications requirements vice president tie "
            "breaking vote impeachment trial remove removal convict two thirds president pro tempore chief justice"
        ),
        "changed": "Choosing senators by state legislatures was replaced by the 17th Amendment (1913).",
    },
    {
        "id": "a1s4",
        "label": "Article I, Section 4",
        "title": "Running congressional elections",
        "text": (
            "The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed "
            "in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such "
            "Regulations, except as to the Places of chusing Senators.\n\n"
            "The Congress shall assemble at least once in every Year, and such Meeting shall be on the first Monday "
            "in December, unless they shall by Law appoint a different Day."
        ),
        "plain": (
            "States set the rules for how, when and where congressional elections happen, but Congress can pass "
            "laws that change those rules. Congress must meet at least once a year. (The 20th Amendment later moved "
            "the start date to January 3.)"
        ),
        "keywords": "elections rules voting when where how state legislatures election day meet once a year",
        "changed": "The meeting date was changed by Section 2 of the 20th Amendment (1933).",
    },
    {
        "id": "a1s5",
        "label": "Article I, Section 5",
        "title": "How each chamber runs itself",
        "text": (
            "Each House shall be the Judge of the Elections, Returns and Qualifications of its own Members, and a "
            "Majority of each shall constitute a Quorum to do Business; but a smaller Number may adjourn from day to "
            "day, and may be authorized to compel the Attendance of absent Members, in such Manner, and under such "
            "Penalties as each House may provide.\n\n"
            "Each House may determine the Rules of its Proceedings, punish its Members for disorderly Behaviour, and, "
            "with the Concurrence of two thirds, expel a Member.\n\n"
            "Each House shall keep a Journal of its Proceedings, and from time to time publish the same, excepting "
            "such Parts as may in their Judgment require Secrecy; and the Yeas and Nays of the Members of either "
            "House on any question shall, at the Desire of one fifth of those Present, be entered on the Journal.\n\n"
            "Neither House, during the Session of Congress, shall, without the Consent of the other, adjourn for more "
            "than three days, nor to any other Place than that in which the two Houses shall be sitting."
        ),
        "plain": (
            "The House and Senate each make their own rules (the Senate filibuster is one of these rules, not part "
            "of the Constitution). Each can discipline its members and expel one with a two-thirds vote. Most of "
            "the members must be present to do business (a quorum), and each chamber keeps a public record of what it does."
        ),
        "keywords": "rules quorum expel discipline journal record filibuster adjourn congress procedures",
    },
    {
        "id": "a1s6",
        "label": "Article I, Section 6",
        "title": "Pay and protections for members of Congress",
        "text": (
            "The Senators and Representatives shall receive a Compensation for their Services, to be ascertained by "
            "Law, and paid out of the Treasury of the United States. They shall in all Cases, except Treason, Felony "
            "and Breach of the Peace, be privileged from Arrest during their Attendance at the Session of their "
            "respective Houses, and in going to and returning from the same; and for any Speech or Debate in either "
            "House, they shall not be questioned in any other Place.\n\n"
            "No Senator or Representative shall, during the Time for which he was elected, be appointed to any civil "
            "Office under the Authority of the United States, which shall have been created, or the Emoluments "
            "whereof shall have been encreased during such time; and no Person holding any Office under the United "
            "States, shall be a Member of either House during his Continuance in Office."
        ),
        "plain": (
            "Members of Congress get paid from the national treasury. They can't be sued or prosecuted for what they "
            "say during debates in Congress (the Speech or Debate Clause), so they can speak freely. And a person "
            "can't be a member of Congress and hold another federal job, like a cabinet post, at the same time."
        ),
        "keywords": "salary pay compensation speech or debate immunity arrest privilege other office cabinet",
    },
    {
        "id": "a1s7",
        "label": "Article I, Section 7",
        "title": "How a bill becomes a law (and the veto)",
        "text": (
            "All Bills for raising Revenue shall originate in the House of Representatives; but the Senate may "
            "propose or concur with Amendments as on other Bills.\n\n"
            "Every Bill which shall have passed the House of Representatives and the Senate, shall, before it become "
            "a Law, be presented to the President of the United States; If he approve he shall sign it, but if not he "
            "shall return it, with his Objections to that House in which it shall have originated, who shall enter "
            "the Objections at large on their Journal, and proceed to reconsider it. If after such Reconsideration "
            "two thirds of that House shall agree to pass the Bill, it shall be sent, together with the Objections, "
            "to the other House, by which it shall likewise be reconsidered, and if approved by two thirds of that "
            "House, it shall become a Law. But in all such Cases the Votes of both Houses shall be determined by yeas "
            "and Nays, and the Names of the Persons voting for and against the Bill shall be entered on the Journal of "
            "each House respectively. If any Bill shall not be returned by the President within ten Days (Sundays "
            "excepted) after it shall have been presented to him, the Same shall be a Law, in like Manner as if he "
            "had signed it, unless the Congress by their Adjournment prevent its Return, in which Case it shall not "
            "be a Law.\n\n"
            "Every Order, Resolution, or Vote to which the Concurrence of the Senate and House of Representatives may "
            "be necessary (except on a question of Adjournment) shall be presented to the President of the United "
            "States; and before the Same shall take Effect, shall be approved by him, or being disapproved by him, "
            "shall be repassed by two thirds of the Senate and House of Representatives, according to the Rules and "
            "Limitations prescribed in the Case of a Bill."
        ),
        "plain": (
            "Tax bills must start in the House. A bill has to pass both the House and Senate in the same form, then "
            "go to the President. The President can sign it into law or veto (reject) it. Congress can override a "
            "veto with a two-thirds vote in both chambers. If the President does nothing for 10 days (not counting "
            "Sundays) while Congress is in session, the bill becomes law anyway; if Congress has adjourned, the bill "
            "dies, which is called a pocket veto."
        ),
        "keywords": (
            "bill becomes a law how laws are made veto override two thirds sign pocket veto revenue taxes tax bills "
            "presentment process"
        ),
    },
    {
        "id": "a1s8",
        "label": "Article I, Section 8",
        "title": "The powers of Congress",
        "text": (
            "The Congress shall have Power To lay and collect Taxes, Duties, Imposts and Excises, to pay the Debts and "
            "provide for the common Defence and general Welfare of the United States; but all Duties, Imposts and "
            "Excises shall be uniform throughout the United States;\n\n"
            "To borrow Money on the credit of the United States;\n\n"
            "To regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes;\n\n"
            "To establish an uniform Rule of Naturalization, and uniform Laws on the subject of Bankruptcies "
            "throughout the United States;\n\n"
            "To coin Money, regulate the Value thereof, and of foreign Coin, and fix the Standard of Weights and "
            "Measures;\n\n"
            "To provide for the Punishment of counterfeiting the Securities and current Coin of the United States;\n\n"
            "To establish Post Offices and post Roads;\n\n"
            "To promote the Progress of Science and useful Arts, by securing for limited Times to Authors and "
            "Inventors the exclusive Right to their respective Writings and Discoveries;\n\n"
            "To constitute Tribunals inferior to the supreme Court;\n\n"
            "To define and punish Piracies and Felonies committed on the high Seas, and Offenses against the Law of "
            "Nations;\n\n"
            "To declare War, grant Letters of Marque and Reprisal, and make Rules concerning Captures on Land and "
            "Water;\n\n"
            "To raise and support Armies, but no Appropriation of Money to that Use shall be for a longer Term than "
            "two Years;\n\n"
            "To provide and maintain a Navy;\n\n"
            "To make Rules for the Government and Regulation of the land and naval Forces;\n\n"
            "To provide for calling forth the Militia to execute the Laws of the Union, suppress Insurrections and "
            "repel Invasions;\n\n"
            "To provide for organizing, arming, and disciplining, the Militia, and for governing such Part of them as "
            "may be employed in the Service of the United States, reserving to the States respectively, the "
            "Appointment of the Officers, and the Authority of training the Militia according to the discipline "
            "prescribed by Congress;\n\n"
            "To exercise exclusive Legislation in all Cases whatsoever, over such District (not exceeding ten Miles "
            "square) as may, by Cession of particular States, and the Acceptance of Congress, become the Seat of the "
            "Government of the United States, and to exercise like Authority over all Places purchased by the "
            "Consent of the Legislature of the State in which the Same shall be, for the Erection of Forts, "
            "Magazines, Arsenals, dock-Yards, and other needful Buildings;—And\n\n"
            "To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers, "
            "and all other Powers vested by this Constitution in the Government of the United States, or in any "
            "Department or Officer thereof."
        ),
        "plain": (
            "This is the list of what Congress is allowed to do (its \"enumerated powers\"). Highlights: collect "
            "taxes and borrow money, regulate trade with other countries and between states (the Commerce Clause), "
            "set rules for becoming a citizen, print and coin money, run the post office, create copyrights and "
            "patents, set up lower federal courts, declare war, and fund an army and navy. The last line, the "
            "Necessary and Proper Clause (also called the Elastic Clause), lets Congress pass laws needed to carry "
            "out these powers, even if the method isn't listed. How far the Commerce and Elastic Clauses stretch "
            "has been argued about since 1789."
        ),
        "keywords": (
            "powers of congress enumerated powers taxes tax borrow money commerce clause trade interstate "
            "naturalization citizenship immigration coin money currency post office copyright patent inventors "
            "declare war go to war who decides war war powers army navy military militia washington dc district of columbia necessary and proper "
            "elastic clause implied powers"
        ),
    },
    {
        "id": "a1s9",
        "label": "Article I, Section 9",
        "title": "Things Congress may not do",
        "text": (
            "The Migration or Importation of such Persons as any of the States now existing shall think proper to "
            "admit, shall not be prohibited by the Congress prior to the Year one thousand eight hundred and eight, "
            "but a Tax or duty may be imposed on such Importation, not exceeding ten dollars for each Person.\n\n"
            "The Privilege of the Writ of Habeas Corpus shall not be suspended, unless when in Cases of Rebellion or "
            "Invasion the public Safety may require it.\n\n"
            "No Bill of Attainder or ex post facto Law shall be passed.\n\n"
            "No Capitation, or other direct, Tax shall be laid, unless in Proportion to the Census or enumeration "
            "herein before directed to be taken.\n\n"
            "No Tax or Duty shall be laid on Articles exported from any State.\n\n"
            "No Preference shall be given by any Regulation of Commerce or Revenue to the Ports of one State over "
            "those of another: nor shall Vessels bound to, or from, one State, be obliged to enter, clear, or pay "
            "Duties in another.\n\n"
            "No Money shall be drawn from the Treasury, but in Consequence of Appropriations made by Law; and a "
            "regular Statement and Account of the Receipts and Expenditures of all public Money shall be published "
            "from time to time.\n\n"
            "No Title of Nobility shall be granted by the United States: And no Person holding any Office of Profit "
            "or Trust under them, shall, without the Consent of the Congress, accept of any present, Emolument, "
            "Office, or Title, of any kind whatever, from any King, Prince, or foreign State."
        ),
        "plain": (
            "Limits on Congress. The first clause protected the Atlantic slave trade until 1808 (Congress banned it "
            "that year). Habeas corpus, the right to make the government explain to a judge why you are being held, "
            "can only be suspended during a rebellion or invasion. Congress can't pass a law declaring a specific "
            "person guilty (bill of attainder) or punish something that was legal when it was done (ex post facto). "
            "No taxes on exports, no favoring one state's ports, no spending money unless a law approves it (the "
            "power of the purse), and no titles of nobility. Federal officials can't accept gifts or titles from "
            "foreign governments without Congress's consent (the foreign Emoluments Clause)."
        ),
        "keywords": (
            "limits on congress habeas corpus bill of attainder ex post facto slave trade 1808 export tax "
            "appropriations spending power of the purse budget title of nobility emoluments foreign gifts"
        ),
        "changed": "The limit on direct taxes was modified by the 16th Amendment (1913), which allows an income tax.",
    },
    {
        "id": "a1s10",
        "label": "Article I, Section 10",
        "title": "Things states may not do",
        "text": (
            "No State shall enter into any Treaty, Alliance, or Confederation; grant Letters of Marque and Reprisal; "
            "coin Money; emit Bills of Credit; make any Thing but gold and silver Coin a Tender in Payment of Debts; "
            "pass any Bill of Attainder, ex post facto Law, or Law impairing the Obligation of Contracts, or grant any "
            "Title of Nobility.\n\n"
            "No State shall, without the Consent of the Congress, lay any Imposts or Duties on Imports or Exports, "
            "except what may be absolutely necessary for executing it's inspection Laws: and the net Produce of all "
            "Duties and Imposts, laid by any State on Imports or Exports, shall be for the Use of the Treasury of the "
            "United States; and all such Laws shall be subject to the Revision and Controul of the Congress.\n\n"
            "No State shall, without the Consent of Congress, lay any Duty of Tonnage, keep Troops, or Ships of War in "
            "time of Peace, enter into any Agreement or Compact with another State, or with a foreign Power, or engage "
            "in War, unless actually invaded, or in such imminent Danger as will not admit of delay."
        ),
        "plain": (
            "States can't act like separate countries. They can't make treaties, print their own money, tax imports "
            "and exports without Congress's OK, keep their own armies or warships in peacetime, or go to war unless "
            "they are invaded. They also can't pass bills of attainder or ex post facto laws, or cancel private "
            "contracts."
        ),
        "keywords": "limits on states state print own money coin treaty money currency tariffs imports contracts state army war compact",
    },
    # ------------------------------------------------------------------ Article II: President
    {
        "id": "a2s1",
        "label": "Article II, Section 1",
        "title": "The President: election, requirements and oath",
        "text": (
            "The executive Power shall be vested in a President of the United States of America. He shall hold his "
            "Office during the Term of four Years, and, together with the Vice President, chosen for the same Term, be "
            "elected, as follows:\n\n"
            "Each State shall appoint, in such Manner as the Legislature thereof may direct, a Number of Electors, "
            "equal to the whole Number of Senators and Representatives to which the State may be entitled in the "
            "Congress: but no Senator or Representative, or Person holding an Office of Trust or Profit under the "
            "United States, shall be appointed an Elector.\n\n"
            "[The original method of counting electoral votes, later replaced by the 12th Amendment, is omitted "
            "here.]\n\n"
            "The Congress may determine the Time of chusing the Electors, and the Day on which they shall give their "
            "Votes; which Day shall be the same throughout the United States.\n\n"
            "No Person except a natural born Citizen, or a Citizen of the United States, at the time of the Adoption "
            "of this Constitution, shall be eligible to the Office of President; neither shall any Person be eligible "
            "to that Office who shall not have attained to the Age of thirty five Years, and been fourteen Years a "
            "Resident within the United States.\n\n"
            "In Case of the Removal of the President from Office, or of his Death, Resignation, or Inability to "
            "discharge the Powers and Duties of the said Office, the Same shall devolve on the Vice President, and the "
            "Congress may by Law provide for the Case of Removal, Death, Resignation or Inability, both of the "
            "President and Vice President, declaring what Officer shall then act as President, and such Officer shall "
            "act accordingly, until the Disability be removed, or a President shall be elected.\n\n"
            "The President shall, at stated Times, receive for his Services, a Compensation, which shall neither be "
            "encreased nor diminished during the Period for which he shall have been elected, and he shall not "
            "receive within that Period any other Emolument from the United States, or any of them.\n\n"
            "Before he enter on the Execution of his Office, he shall take the following Oath or Affirmation:—\"I do "
            "solemnly swear (or affirm) that I will faithfully execute the Office of President of the United States, "
            "and will to the best of my Ability, preserve, protect and defend the Constitution of the United States.\""
        ),
        "plain": (
            "The President leads the executive branch, which carries out the laws, and serves a four-year term. "
            "Presidents are chosen by electors from each state (what we now call the Electoral College); each state "
            "gets as many electors as it has senators plus representatives, and the state legislature decides how "
            "electors are picked. Today every state lets voters choose. To be President you must be a natural born "
            "citizen, at least 35, and have lived in the U.S. for 14 years. If the President dies, resigns or is "
            "removed, the Vice President takes over. This section also has the exact words of the presidential oath."
        ),
        "keywords": (
            "president executive branch four years term election electoral college electors requirements "
            "qualifications age 35 natural born citizen 14 years residency vice president succession oath of office "
            "swear inauguration salary"
        ),
        "changed": (
            "The electoral vote counting method was replaced by the 12th Amendment (1804); succession was clarified "
            "by the 25th Amendment (1967)."
        ),
    },
    {
        "id": "a2s2",
        "label": "Article II, Section 2",
        "title": "Powers of the President",
        "text": (
            "The President shall be Commander in Chief of the Army and Navy of the United States, and of the Militia "
            "of the several States, when called into the actual Service of the United States; he may require the "
            "Opinion, in writing, of the principal Officer in each of the executive Departments, upon any Subject "
            "relating to the Duties of their respective Offices, and he shall have Power to grant Reprieves and "
            "Pardons for Offences against the United States, except in Cases of Impeachment.\n\n"
            "He shall have Power, by and with the Advice and Consent of the Senate, to make Treaties, provided two "
            "thirds of the Senators present concur; and he shall nominate, and by and with the Advice and Consent of "
            "the Senate, shall appoint Ambassadors, other public Ministers and Consuls, Judges of the supreme Court, "
            "and all other Officers of the United States, whose Appointments are not herein otherwise provided for, "
            "and which shall be established by Law: but the Congress may by Law vest the Appointment of such inferior "
            "Officers, as they think proper, in the President alone, in the Courts of Law, or in the Heads of "
            "Departments.\n\n"
            "The President shall have Power to fill up all Vacancies that may happen during the Recess of the Senate, "
            "by granting Commissions which shall expire at the End of their next Session."
        ),
        "plain": (
            "The President is commander in chief of the military, can ask cabinet heads for advice, and can pardon "
            "people for federal crimes (but can't stop an impeachment). The President makes treaties, but two thirds "
            "of the Senate must approve them. The President nominates Supreme Court justices, ambassadors and other "
            "top officials, and the Senate must confirm them (\"advice and consent\"). This is a key check and "
            "balance between the branches."
        ),
        "keywords": (
            "presidential powers commander in chief military pardon pardons reprieve cabinet treaty treaties "
            "appointments nominate supreme court justices confirm confirmation advice and consent senate ambassadors "
            "recess appointments checks and balances"
        ),
    },
    {
        "id": "a2s3",
        "label": "Article II, Section 3",
        "title": "State of the Union and executing the laws",
        "text": (
            "He shall from time to time give to the Congress Information of the State of the Union, and recommend to "
            "their Consideration such Measures as he shall judge necessary and expedient; he may, on extraordinary "
            "Occasions, convene both Houses, or either of them, and in Case of Disagreement between them, with Respect "
            "to the Time of Adjournment, he may adjourn them to such Time as he shall think proper; he shall receive "
            "Ambassadors and other public Ministers; he shall take Care that the Laws be faithfully executed, and "
            "shall Commission all the Officers of the United States."
        ),
        "plain": (
            "The President must update Congress on how the country is doing (today's State of the Union address) "
            "and can suggest laws. The President receives foreign ambassadors and must \"take Care that the Laws be "
            "faithfully executed,\" meaning enforce the laws Congress passes."
        ),
        "keywords": "state of the union address speech recommend laws take care clause enforce laws ambassadors",
    },
    {
        "id": "a2s4",
        "label": "Article II, Section 4",
        "title": "Impeachment of officials",
        "text": (
            "The President, Vice President and all civil Officers of the United States, shall be removed from Office "
            "on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors."
        ),
        "plain": (
            "The President, Vice President and other federal officials (including judges) can be removed if they "
            "are impeached by the House and convicted by the Senate for treason, bribery, or \"other high Crimes "
            "and Misdemeanors.\" What counts as a \"high crime or misdemeanor\" is debated; it is generally "
            "understood to mean a serious abuse of power, not necessarily a crime in the ordinary sense."
        ),
        "keywords": "impeach impeachment remove removal president high crimes and misdemeanors treason bribery",
    },
    # ------------------------------------------------------------------ Article III: Courts
    {
        "id": "a3s1",
        "label": "Article III, Section 1",
        "title": "The federal courts",
        "text": (
            "The judicial Power of the United States, shall be vested in one supreme Court, and in such inferior "
            "Courts as the Congress may from time to time ordain and establish. The Judges, both of the supreme and "
            "inferior Courts, shall hold their Offices during good Behaviour, and shall, at stated Times, receive for "
            "their Services, a Compensation, which shall not be diminished during their Continuance in Office."
        ),
        "plain": (
            "The judicial branch decides cases and interprets the law. There is one Supreme Court, and Congress can "
            "create lower federal courts. Federal judges serve \"during good Behaviour,\" which in practice means "
            "for life unless they resign or are impeached, and their pay can't be cut. The idea is to keep judges "
            "independent of political pressure. The Constitution does not set the number of justices; Congress "
            "has kept it at nine since 1869."
        ),
        "keywords": (
            "judicial branch supreme court federal courts judges justices life tenure lifetime appointment good "
            "behaviour how many justices nine judicial independence"
        ),
    },
    {
        "id": "a3s2",
        "label": "Article III, Section 2",
        "title": "What cases federal courts hear; jury trials",
        "text": (
            "The judicial Power shall extend to all Cases, in Law and Equity, arising under this Constitution, the "
            "Laws of the United States, and Treaties made, or which shall be made, under their Authority;—to all "
            "Cases affecting Ambassadors, other public Ministers and Consuls;—to all Cases of admiralty and maritime "
            "Jurisdiction;—to Controversies to which the United States shall be a Party;—to Controversies between two "
            "or more States;—between a State and Citizens of another State;—between Citizens of different States;—"
            "between Citizens of the same State claiming Lands under Grants of different States, and between a State, "
            "or the Citizens thereof, and foreign States, Citizens or Subjects.\n\n"
            "In all Cases affecting Ambassadors, other public Ministers and Consuls, and those in which a State shall "
            "be Party, the supreme Court shall have original Jurisdiction. In all the other Cases before mentioned, "
            "the supreme Court shall have appellate Jurisdiction, both as to Law and Fact, with such Exceptions, and "
            "under such Regulations as the Congress shall make.\n\n"
            "The Trial of all Crimes, except in Cases of Impeachment, shall be by Jury; and such Trial shall be held "
            "in the State where the said Crimes shall have been committed; but when not committed within any State, "
            "the Trial shall be at such Place or Places as the Congress may by Law have directed."
        ),
        "plain": (
            "Federal courts hear cases about the Constitution, federal laws and treaties, cases involving the U.S. "
            "government, disputes between states, and some disputes between people from different states. In a few "
            "kinds of cases (like a state suing another state) the Supreme Court hears the case first; in most "
            "others it hears appeals from lower courts. Anyone accused of a federal crime gets a jury trial in the "
            "state where the crime happened. Note: the power of courts to strike down unconstitutional laws "
            "(judicial review) is not spelled out here; the Supreme Court claimed it in Marbury v. Madison (1803)."
        ),
        "keywords": (
            "jurisdiction cases courts hear original appellate appeal jury trial crimes judicial review marbury "
            "supreme court power"
        ),
        "changed": "Suits against a state by citizens of another state were limited by the 11th Amendment (1795).",
    },
    {
        "id": "a3s3",
        "label": "Article III, Section 3",
        "title": "Treason",
        "text": (
            "Treason against the United States, shall consist only in levying War against them, or in adhering to "
            "their Enemies, giving them Aid and Comfort. No Person shall be convicted of Treason unless on the "
            "Testimony of two Witnesses to the same overt Act, or on Confession in open Court.\n\n"
            "The Congress shall have Power to declare the Punishment of Treason, but no Attainder of Treason shall "
            "work Corruption of Blood, or Forfeiture except during the Life of the Person attainted."
        ),
        "plain": (
            "Treason is the only crime the Constitution defines. It means only waging war against the U.S. or "
            "helping its enemies. Convicting someone requires two witnesses to the same act or a confession in "
            "court. The narrow definition was on purpose: in England, \"treason\" had been used to punish the "
            "king's critics. Punishment can't be passed on to a traitor's family."
        ),
        "keywords": "treason traitor enemies war definition crime two witnesses",
    },
    # ------------------------------------------------------------------ Article IV: States
    {
        "id": "a4s1",
        "label": "Article IV, Section 1",
        "title": "Full faith and credit",
        "text": (
            "Full Faith and Credit shall be given in each State to the public Acts, Records, and judicial Proceedings "
            "of every other State. And the Congress may by general Laws prescribe the Manner in which such Acts, "
            "Records and Proceedings shall be proved, and the Effect thereof."
        ),
        "plain": (
            "States must respect each other's official records and court decisions. For example, a birth "
            "certificate, a marriage, or a court judgment from one state is recognized in the others."
        ),
        "keywords": "full faith and credit states recognize records marriage license court judgments other states",
    },
    {
        "id": "a4s2",
        "label": "Article IV, Section 2",
        "title": "Treating citizens of other states fairly; extradition",
        "text": (
            "The Citizens of each State shall be entitled to all Privileges and Immunities of Citizens in the several "
            "States.\n\n"
            "A Person charged in any State with Treason, Felony, or other Crime, who shall flee from Justice, and be "
            "found in another State, shall on Demand of the executive Authority of the State from which he fled, be "
            "delivered up, to be removed to the State having Jurisdiction of the Crime.\n\n"
            "No Person held to Service or Labour in one State, under the Laws thereof, escaping into another, shall, "
            "in Consequence of any Law or Regulation therein, be discharged from such Service or Labour, but shall be "
            "delivered up on Claim of the Party to whom such Service or Labour may be due."
        ),
        "plain": (
            "A state can't treat visitors from other states as second-class citizens. A person who commits a crime "
            "and flees to another state must be sent back (extradition). The third paragraph, the Fugitive Slave "
            "Clause, required escaped enslaved people to be returned; the 13th Amendment ended it."
        ),
        "keywords": "privileges and immunities extradition fugitive slave clause travel between states visitors",
        "changed": "The Fugitive Slave Clause was made void by the 13th Amendment (1865).",
    },
    {
        "id": "a4s3",
        "label": "Article IV, Section 3",
        "title": "New states and federal territory",
        "text": (
            "New States may be admitted by the Congress into this Union; but no new State shall be formed or erected "
            "within the Jurisdiction of any other State; nor any State be formed by the Junction of two or more "
            "States, or Parts of States, without the Consent of the Legislatures of the States concerned as well as "
            "of the Congress.\n\n"
            "The Congress shall have Power to dispose of and make all needful Rules and Regulations respecting the "
            "Territory or other Property belonging to the United States; and nothing in this Constitution shall be so "
            "construed as to Prejudice any Claims of the United States, or of any particular State."
        ),
        "plain": (
            "Congress can admit new states (37 have joined since the original 13). A state can't be split or merged "
            "with another without the approval of the states involved and Congress. Congress makes the rules for "
            "federal land and territories like Puerto Rico and Guam."
        ),
        "keywords": "new states admit statehood territories puerto rico guam federal land property",
    },
    {
        "id": "a4s4",
        "label": "Article IV, Section 4",
        "title": "Guarantee of a republican government",
        "text": (
            "The United States shall guarantee to every State in this Union a Republican Form of Government, and shall "
            "protect each of them against Invasion; and on Application of the Legislature, or of the Executive (when "
            "the Legislature cannot be convened) against domestic Violence."
        ),
        "plain": (
            "The national government promises that every state will have a republican government, meaning one run "
            "by elected representatives rather than a king or dictator, and will protect each state from invasion "
            "and, if the state asks, from violence inside it."
        ),
        "keywords": "republic republican form of government guarantee clause protect invasion democracy",
    },
    # ------------------------------------------------------------------ Articles V-VII
    {
        "id": "a5",
        "label": "Article V",
        "title": "How to amend (change) the Constitution",
        "text": (
            "The Congress, whenever two thirds of both Houses shall deem it necessary, shall propose Amendments to this "
            "Constitution, or, on the Application of the Legislatures of two thirds of the several States, shall call "
            "a Convention for proposing Amendments, which, in either Case, shall be valid to all Intents and Purposes, "
            "as Part of this Constitution, when ratified by the Legislatures of three fourths of the several States, "
            "or by Conventions in three fourths thereof, as the one or the other Mode of Ratification may be proposed "
            "by the Congress; Provided that no Amendment which may be made prior to the Year One thousand eight "
            "hundred and eight shall in any Manner affect the first and fourth Clauses in the Ninth Section of the "
            "first Article; and that no State, without its Consent, shall be deprived of its equal Suffrage in the "
            "Senate."
        ),
        "plain": (
            "Changing the Constitution takes two steps. First, an amendment is proposed, either by two thirds of both "
            "the House and Senate, or by a national convention called by two thirds of the states (this has never "
            "happened). Second, three fourths of the states (38 of 50) must ratify it. It is hard on purpose. "
            "Thousands of amendments have been proposed, and only 27 have been ratified. One thing can never be "
            "changed without a state's consent: its equal vote in the Senate."
        ),
        "keywords": (
            "amend amendment amendments change the constitution process ratify ratification two thirds three fourths "
            "convention of states how many amendments"
        ),
    },
    {
        "id": "a6",
        "label": "Article VI",
        "title": "The supreme law of the land",
        "text": (
            "All Debts contracted and Engagements entered into, before the Adoption of this Constitution, shall be as "
            "valid against the United States under this Constitution, as under the Confederation.\n\n"
            "This Constitution, and the Laws of the United States which shall be made in Pursuance thereof; and all "
            "Treaties made, or which shall be made, under the Authority of the United States, shall be the supreme Law "
            "of the Land; and the Judges in every State shall be bound thereby, any Thing in the Constitution or Laws "
            "of any State to the Contrary notwithstanding.\n\n"
            "The Senators and Representatives before mentioned, and the Members of the several State Legislatures, and "
            "all executive and judicial Officers, both of the United States and of the several States, shall be bound "
            "by Oath or Affirmation, to support this Constitution; but no religious Test shall ever be required as a "
            "Qualification to any Office or public Trust under the United States."
        ),
        "plain": (
            "The Supremacy Clause: the Constitution, federal laws made under it, and treaties are the highest law in "
            "the country. If a state law conflicts with them, the federal law wins. The new government also took on "
            "the debts from the old one. All officials, federal and state, must swear to support the Constitution, "
            "and no one can be required to belong to (or reject) any religion to hold public office."
        ),
        "keywords": (
            "supremacy clause supreme law of the land federal law vs state law conflict preemption oath religious "
            "test religion office debts"
        ),
    },
    {
        "id": "a7",
        "label": "Article VII",
        "title": "Ratification and the signers",
        "text": (
            "The Ratification of the Conventions of nine States, shall be sufficient for the Establishment of this "
            "Constitution between the States so ratifying the Same.\n\n"
            "done in Convention by the Unanimous Consent of the States present the Seventeenth Day of September in the "
            "Year of our Lord one thousand seven hundred and Eighty seven and of the Independence of the United States "
            "of America the Twelfth In witness whereof We have hereunto subscribed our Names,\n\n"
            "G°. Washington—Presidt. and deputy from Virginia\n\n"
            "[followed by the signatures of 38 other delegates from twelve states]"
        ),
        "plain": (
            "The Constitution would take effect once 9 of the 13 states approved it at special conventions. New "
            "Hampshire became the ninth on June 21, 1788, and the new government began in 1789. The document was "
            "signed on September 17, 1787 (now Constitution Day) by 39 delegates, starting with George Washington, "
            "who presided over the Convention."
        ),
        "keywords": (
            "ratification ratify nine states signers signed september 17 1787 constitution day washington delegates "
            "constitutional convention philadelphia"
        ),
    },
    # ------------------------------------------------------------------ Bill of Rights
    {
        "id": "am1",
        "label": "1st Amendment (1791)",
        "title": "Religion, speech, press, assembly, petition",
        "text": (
            "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise "
            "thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to "
            "assemble, and to petition the Government for a redress of grievances."
        ),
        "plain": (
            "Five freedoms in one sentence. The government can't set up an official religion (Establishment Clause) "
            "or stop you from practicing yours (Free Exercise Clause). It can't punish you for what you say or "
            "publish, with narrow exceptions such as true threats, incitement to immediate violence, fraud and "
            "defamation. You can gather peacefully to protest and ask the government to fix problems. These limits "
            "apply to the government, not to private companies or people, and through the 14th Amendment they apply "
            "to states and public schools too. Students keep these rights at school, though schools can limit "
            "speech that seriously disrupts learning."
        ),
        "keywords": (
            "first amendment freedom of speech free speech religion church and state separation establishment free "
            "exercise press newspaper journalists media assembly protest petition flag burning expression censorship "
            "social media school prayer students rights"
        ),
    },
    {
        "id": "am2",
        "label": "2nd Amendment (1791)",
        "title": "Right to keep and bear arms",
        "text": (
            "A well regulated Militia, being necessary to the security of a free State, the right of the people to "
            "keep and bear Arms, shall not be infringed."
        ),
        "plain": (
            "This protects a right to keep and carry weapons. For a long time people disagreed about whether it "
            "protects an individual right or only a right connected to serving in a state militia. In District of "
            "Columbia v. Heller (2008) the Supreme Court held it protects an individual's right to have a handgun "
            "at home for self-defense, while saying some gun regulations are still allowed. Exactly which rules are "
            "allowed is still debated in courts and legislatures."
        ),
        "keywords": "second amendment guns gun rights firearms weapons arms bear arms militia gun control self defense",
    },
    {
        "id": "am3",
        "label": "3rd Amendment (1791)",
        "title": "No forced housing of soldiers",
        "text": (
            "No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in "
            "time of war, but in a manner to be prescribed by law."
        ),
        "plain": (
            "The government can't make you house soldiers in your home during peacetime. Under British rule, "
            "colonists had been forced to do this, and they hated it. It is one of the least-used parts of the "
            "Constitution, but courts have pointed to it as a sign that the Constitution protects the privacy of the home."
        ),
        "keywords": "third amendment soldiers quartering house home troops",
    },
    {
        "id": "am4",
        "label": "4th Amendment (1791)",
        "title": "Searches and seizures",
        "text": (
            "The right of the people to be secure in their persons, houses, papers, and effects, against "
            "unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable "
            "cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the "
            "persons or things to be seized."
        ),
        "plain": (
            "The government can't search you, your home or your things, or take your property, without a good "
            "reason. Usually police need a warrant signed by a judge, based on probable cause (solid reason to "
            "believe evidence of a crime will be found) and describing exactly what they are looking for. There are "
            "exceptions, such as emergencies. The Supreme Court has said police generally need a warrant to search "
            "your cell phone (Riley v. California, 2014). At school, officials need only \"reasonable suspicion\" "
            "(New Jersey v. T.L.O., 1985)."
        ),
        "keywords": (
            "fourth amendment search seizure warrant police probable cause privacy phone cell phone search my locker "
            "backpack car home arrest evidence exclusionary rule"
        ),
    },
    {
        "id": "am5",
        "label": "5th Amendment (1791)",
        "title": "Rights of people accused of crimes; due process; property",
        "text": (
            "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or "
            "indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when "
            "in actual service in time of War or public danger; nor shall any person be subject for the same offence "
            "to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness "
            "against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall "
            "private property be taken for public use, without just compensation."
        ),
        "plain": (
            "Several protections: serious federal charges need a grand jury indictment. You can't be tried twice for "
            "the same crime after a verdict (double jeopardy). You can't be forced to testify against yourself, "
            "which is where \"pleading the Fifth\" and the right to remain silent come from. The government must "
            "follow fair procedures (due process) before taking your life, freedom or property. And if the "
            "government takes your property for public use, like building a highway, it must pay you a fair price "
            "(eminent domain)."
        ),
        "keywords": (
            "fifth amendment plead the fifth remain silent self incrimination miranda double jeopardy tried twice "
            "grand jury indictment due process eminent domain takings property just compensation take my house home land"
        ),
    },
    {
        "id": "am6",
        "label": "6th Amendment (1791)",
        "title": "Right to a fair and speedy trial and a lawyer",
        "text": (
            "In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an "
            "impartial jury of the State and district wherein the crime shall have been committed, which district "
            "shall have been previously ascertained by law, and to be informed of the nature and cause of the "
            "accusation; to be confronted with the witnesses against him; to have compulsory process for obtaining "
            "witnesses in his favor, and to have the Assistance of Counsel for his defence."
        ),
        "plain": (
            "If you are charged with a crime, you have the right to a speedy, public trial with a fair jury, to know "
            "what you are accused of, to question the witnesses against you, to call your own witnesses, and to have "
            "a lawyer. Since Gideon v. Wainwright (1963), if you can't afford a lawyer for a serious charge, the "
            "government must provide one."
        ),
        "keywords": (
            "sixth amendment speedy trial public trial jury lawyer attorney counsel right to a lawyer public defender "
            "witnesses confront accused criminal rights"
        ),
    },
    {
        "id": "am7",
        "label": "7th Amendment (1791)",
        "title": "Jury trials in civil cases",
        "text": (
            "In Suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by "
            "jury shall be preserved, and no fact tried by a jury, shall be otherwise re-examined in any Court of the "
            "United States, than according to the rules of the common law."
        ),
        "plain": (
            "In many federal lawsuits between people or businesses over money (civil cases, not crimes), you have a "
            "right to a jury. The amount is still listed as $20, a number that has never been updated."
        ),
        "keywords": "seventh amendment civil cases lawsuit sue jury trial twenty dollars",
    },
    {
        "id": "am8",
        "label": "8th Amendment (1791)",
        "title": "No excessive bail or cruel and unusual punishment",
        "text": (
            "Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments "
            "inflicted."
        ),
        "plain": (
            "Bail (money paid to get out of jail while awaiting trial) and fines can't be unreasonably high, and "
            "punishments can't be cruel and unusual. Courts have used this to limit the death penalty: for example, "
            "it can't be used for crimes committed by people under 18 (Roper v. Simmons, 2005). What counts as cruel "
            "and unusual is still debated."
        ),
        "keywords": (
            "eighth amendment cruel and unusual punishment death penalty capital punishment execution bail fines "
            "prison jail juveniles"
        ),
    },
    {
        "id": "am9",
        "label": "9th Amendment (1791)",
        "title": "Rights not listed still exist",
        "text": (
            "The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage "
            "others retained by the people."
        ),
        "plain": (
            "Just because a right isn't written down in the Constitution doesn't mean people don't have it. Some "
            "founders worried a list of rights would be read as the only rights; this amendment answers that "
            "worry. Which unlisted rights exist, and who decides, is a major debate."
        ),
        "keywords": "ninth amendment unlisted rights unenumerated rights other rights privacy retained by the people",
    },
    {
        "id": "am10",
        "label": "10th Amendment (1791)",
        "title": "Powers kept by the states and the people",
        "text": (
            "The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, "
            "are reserved to the States respectively, or to the people."
        ),
        "plain": (
            "Powers the Constitution doesn't give to the national government (and doesn't forbid the states) belong "
            "to the states or the people. This is the heart of federalism, the sharing of power between the national "
            "government and the states. It's why things like driver's licenses, most schools and most criminal laws "
            "are handled by states."
        ),
        "keywords": "tenth amendment states rights reserved powers federalism state power local government",
    },
    # ------------------------------------------------------------------ Amendments 11-27
    {
        "id": "am11",
        "label": "11th Amendment (1795)",
        "title": "Limits on suing states in federal court",
        "text": (
            "The Judicial power of the United States shall not be construed to extend to any suit in law or equity, "
            "commenced or prosecuted against one of the United States by Citizens of another State, or by Citizens or "
            "Subjects of any Foreign State."
        ),
        "plain": (
            "People from other states or other countries can't sue a state in federal court. It was passed after "
            "the Supreme Court let a man from South Carolina sue Georgia (Chisholm v. Georgia, 1793), which upset "
            "many states."
        ),
        "keywords": "eleventh amendment sovereign immunity sue a state lawsuit",
    },
    {
        "id": "am12",
        "label": "12th Amendment (1804)",
        "title": "Separate electoral votes for President and Vice President",
        "text": (
            "The Electors shall meet in their respective states and vote by ballot for President and Vice-President, "
            "one of whom, at least, shall not be an inhabitant of the same state with themselves; they shall name in "
            "their ballots the person voted for as President, and in distinct ballots the person voted for as "
            "Vice-President, and they shall make distinct lists of all persons voted for as President, and of all "
            "persons voted for as Vice-President, and the number of votes for each, which lists they shall sign "
            "and certify, and transmit sealed to the seat of the government of the United States, directed to the "
            "President of the Senate;—The President of the Senate shall, in presence of the Senate and House of "
            "Representatives, open all the certificates and the votes shall then be counted;—The person having the "
            "greatest number of votes for President, shall be the President, if such number be a majority of the "
            "whole number of Electors appointed; and if no person have such majority, then from the persons having "
            "the highest numbers not exceeding three on the list of those voted for as President, the House of "
            "Representatives shall choose immediately, by ballot, the President. But in choosing the President, the "
            "votes shall be taken by states, the representation from each state having one vote; a quorum for this "
            "purpose shall consist of a member or members from two-thirds of the states, and a majority of all the "
            "states shall be necessary to a choice. [...] The person having the greatest number of votes as "
            "Vice-President, shall be the Vice-President, if such number be a majority of the whole number of Electors "
            "appointed, and if no person have a majority, then from the two highest numbers on the list, the Senate "
            "shall choose the Vice-President [...]. But no person constitutionally ineligible to the office of "
            "President shall be eligible to that of Vice-President of the United States."
        ),
        "plain": (
            "Originally, electors cast two votes for President and the runner-up became Vice President. That caused "
            "a tie in 1800 between Thomas Jefferson and his own running mate, Aaron Burr. Now electors vote "
            "separately for President and Vice President. A candidate needs a majority of electoral votes (270 of "
            "538 today). If no one gets a majority, the House picks the President, with each state delegation "
            "getting one vote, and the Senate picks the Vice President."
        ),
        "keywords": (
            "twelfth amendment electoral college electors electoral votes 270 majority tie house chooses president "
            "jefferson burr 1800 vice president running mate"
        ),
    },
    {
        "id": "am13",
        "label": "13th Amendment (1865)",
        "title": "Slavery abolished",
        "text": (
            "Section 1. Neither slavery nor involuntary servitude, except as a punishment for crime whereof the party "
            "shall have been duly convicted, shall exist within the United States, or any place subject to their "
            "jurisdiction.\n\n"
            "Section 2. Congress shall have power to enforce this article by appropriate legislation."
        ),
        "plain": (
            "Slavery is abolished everywhere in the United States. Passed at the end of the Civil War, it was the "
            "first of the three \"Reconstruction Amendments.\" Note the exception: forced labor is still allowed as "
            "punishment for someone convicted of a crime, which is debated today."
        ),
        "keywords": "thirteenth amendment slavery abolished abolition end of slavery civil war reconstruction emancipation",
    },
    {
        "id": "am14",
        "label": "14th Amendment (1868)",
        "title": "Citizenship, due process and equal protection",
        "text": (
            "Section 1. All persons born or naturalized in the United States, and subject to the jurisdiction thereof, "
            "are citizens of the United States and of the State wherein they reside. No State shall make or enforce "
            "any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any "
            "State deprive any person of life, liberty, or property, without due process of law; nor deny to any "
            "person within its jurisdiction the equal protection of the laws.\n\n"
            "Section 2. Representatives shall be apportioned among the several States according to their respective "
            "numbers, counting the whole number of persons in each State, excluding Indians not taxed. [...]\n\n"
            "Section 3. No person shall be a Senator or Representative in Congress, or elector of President and Vice "
            "President, or hold any office, civil or military, under the United States, or under any State, who, "
            "having previously taken an oath, as a member of Congress, or as an officer of the United States, or as a "
            "member of any State legislature, or as an executive or judicial officer of any State, to support the "
            "Constitution of the United States, shall have engaged in insurrection or rebellion against the same, or "
            "given aid or comfort to the enemies thereof. But Congress may by a vote of two-thirds of each House, "
            "remove such disability.\n\n"
            "Section 4. The validity of the public debt of the United States, authorized by law [...] shall not be "
            "questioned. [...]\n\n"
            "Section 5. The Congress shall have power to enforce, by appropriate legislation, the provisions of this "
            "article."
        ),
        "plain": (
            "One of the most important amendments. Section 1 says almost everyone born in the U.S. is a citizen "
            "(birthright citizenship), overturning the Dred Scott decision. The Supreme Court confirmed this in Trump v. Barbara (2026). It also says states must give every "
            "person due process and equal protection of the laws. The Supreme Court has used this to apply most of "
            "the Bill of Rights to the states (called incorporation) and in landmark cases like Brown v. Board of "
            "Education (1954). Section 2 replaced the three-fifths clause. Section 3 bars people who took an oath to "
            "the Constitution and then joined an insurrection from holding office. Courts continue to decide what "
            "\"equal protection\" and \"liberty\" require, which makes this amendment central to many debates."
        ),
        "keywords": (
            "fourteenth amendment citizenship birthright citizen born in the united states due process equal "
            "protection discrimination civil rights incorporation reconstruction insurrection section 3 segregation "
            "equality liberty"
        ),
    },
    {
        "id": "am15",
        "label": "15th Amendment (1870)",
        "title": "Voting rights regardless of race",
        "text": (
            "Section 1. The right of citizens of the United States to vote shall not be denied or abridged by the "
            "United States or by any State on account of race, color, or previous condition of servitude.\n\n"
            "Section 2. The Congress shall have power to enforce this article by appropriate legislation."
        ),
        "plain": (
            "No one can be denied the vote because of race or because they had been enslaved. In practice, many "
            "states used poll taxes, literacy tests and violence to keep Black citizens from voting for nearly a "
            "century, until the Voting Rights Act of 1965 and the 24th Amendment."
        ),
        "keywords": "fifteenth amendment voting rights race black men vote suffrage right to vote discrimination",
    },
    {
        "id": "am16",
        "label": "16th Amendment (1913)",
        "title": "Federal income tax",
        "text": (
            "The Congress shall have power to lay and collect taxes on incomes, from whatever source derived, without "
            "apportionment among the several States, and without regard to any census or enumeration."
        ),
        "plain": "Congress can tax people's income. This is the basis of the federal income tax.",
        "keywords": "sixteenth amendment income tax taxes irs",
    },
    {
        "id": "am17",
        "label": "17th Amendment (1913)",
        "title": "Voters elect senators directly",
        "text": (
            "The Senate of the United States shall be composed of two Senators from each State, elected by the people "
            "thereof, for six years; and each Senator shall have one vote. The electors in each State shall have the "
            "qualifications requisite for electors of the most numerous branch of the State legislatures. [...]"
        ),
        "plain": (
            "Before 1913, state legislatures chose U.S. senators. Now the voters of each state elect their senators "
            "directly."
        ),
        "keywords": "seventeenth amendment senators elected directly popular election senate voters",
    },
    {
        "id": "am18",
        "label": "18th Amendment (1919)",
        "title": "Prohibition of alcohol",
        "text": (
            "Section 1. After one year from the ratification of this article the manufacture, sale, or transportation "
            "of intoxicating liquors within, the importation thereof into, or the exportation thereof from the United "
            "States and all territories subject to the jurisdiction thereof for beverage purposes is hereby prohibited. "
            "[...]"
        ),
        "plain": (
            "Banned making, selling and transporting alcohol, starting the era called Prohibition. It led to "
            "widespread illegal drinking and organized crime, and was repealed by the 21st Amendment in 1933. It is "
            "the only amendment ever repealed."
        ),
        "keywords": "eighteenth amendment prohibition alcohol ban liquor 1920s repealed",
        "changed": "Repealed by the 21st Amendment (1933).",
    },
    {
        "id": "am19",
        "label": "19th Amendment (1920)",
        "title": "Women's right to vote",
        "text": (
            "The right of citizens of the United States to vote shall not be denied or abridged by the United States "
            "or by any State on account of sex.\n\n"
            "Congress shall have power to enforce this article by appropriate legislation."
        ),
        "plain": (
            "Women gained the right to vote nationwide. It came after more than 70 years of organizing by the women's "
            "suffrage movement. Tennessee was the 36th state to ratify, putting it over the top."
        ),
        "keywords": "nineteenth amendment women vote womens suffrage female voting rights",
    },
    {
        "id": "am20",
        "label": "20th Amendment (1933)",
        "title": "New start dates for terms (the \"Lame Duck\" Amendment)",
        "text": (
            "Section 1. The terms of the President and Vice President shall end at noon on the 20th day of "
            "January, and the terms of Senators and Representatives at noon on the 3d day of January, of the years in "
            "which such terms would have ended if this article had not been ratified; and the terms of their "
            "successors shall then begin.\n\n"
            "Section 2. The Congress shall assemble at least once in every year, and such meeting shall begin at noon "
            "on the 3d day of January, unless they shall by law appoint a different day.\n\n"
            "Section 3. If, at the time fixed for the beginning of the term of the President, the President elect "
            "shall have died, the Vice President elect shall become President. [...]"
        ),
        "plain": (
            "Moved Inauguration Day from March 4 to January 20, and the start of Congress to January 3. This "
            "shortened the \"lame duck\" period, when officials who lost an election are still in office. It also "
            "says what happens if a President-elect dies before taking office."
        ),
        "keywords": "twentieth amendment lame duck inauguration day january 20 january 3 term start president elect",
    },
    {
        "id": "am21",
        "label": "21st Amendment (1933)",
        "title": "Prohibition repealed",
        "text": (
            "Section 1. The eighteenth article of amendment to the Constitution of the United States is hereby "
            "repealed.\n\n"
            "Section 2. The transportation or importation into any State, Territory, or possession of the United "
            "States for delivery or use therein of intoxicating liquors, in violation of the laws thereof, is hereby "
            "prohibited. [...]"
        ),
        "plain": (
            "Ended Prohibition by repealing the 18th Amendment, and let states make their own alcohol laws. It is "
            "the only amendment ratified by state conventions instead of state legislatures."
        ),
        "keywords": "twenty first amendment repeal prohibition alcohol end",
    },
    {
        "id": "am22",
        "label": "22nd Amendment (1951)",
        "title": "Two-term limit for Presidents",
        "text": (
            "Section 1. No person shall be elected to the office of the President more than twice, and no person who "
            "has held the office of President, or acted as President, for more than two years of a term to which some "
            "other person was elected President shall be elected to the office of the President more than once. [...]"
        ),
        "plain": (
            "A person can be elected President at most twice. George Washington set a two-term tradition, but "
            "Franklin D. Roosevelt was elected four times (1932 to 1944). This amendment made the limit official. "
            "Someone who serves more than two years of another President's term can be elected only once on their "
            "own, so the most anyone can serve is about ten years."
        ),
        "keywords": "twenty second amendment term limits two terms president third term fdr roosevelt",
    },
    {
        "id": "am23",
        "label": "23rd Amendment (1961)",
        "title": "Electoral votes for Washington, D.C.",
        "text": (
            "Section 1. The District constituting the seat of Government of the United States shall appoint in such "
            "manner as the Congress may direct: A number of electors of President and Vice President equal to the "
            "whole number of Senators and Representatives in Congress to which the District would be entitled if it "
            "were a State, but in no event more than the least populous State; [...]"
        ),
        "plain": (
            "People living in Washington, D.C. can vote for President. D.C. gets electoral votes as if it were a "
            "state, but no more than the smallest state (currently 3). D.C. still has no voting members of Congress."
        ),
        "keywords": "twenty third amendment washington dc district of columbia electoral votes president",
    },
    {
        "id": "am24",
        "label": "24th Amendment (1964)",
        "title": "No poll taxes in federal elections",
        "text": (
            "Section 1. The right of citizens of the United States to vote in any primary or other election for "
            "President or Vice President, for electors for President or Vice President, or for Senator or "
            "Representative in Congress, shall not be denied or abridged by the United States or any State by reason "
            "of failure to pay any poll tax or other tax. [...]"
        ),
        "plain": (
            "No one can be charged a fee (a poll tax) to vote in federal elections. Poll taxes had been used to keep "
            "poor people and Black citizens from voting. The Supreme Court banned them in state elections too in 1966."
        ),
        "keywords": "twenty fourth amendment poll tax voting fee civil rights voting rights",
    },
    {
        "id": "am25",
        "label": "25th Amendment (1967)",
        "title": "Presidential disability and succession",
        "text": (
            "Section 1. In case of the removal of the President from office or of his death or resignation, the Vice "
            "President shall become President.\n\n"
            "Section 2. Whenever there is a vacancy in the office of the Vice President, the President shall nominate "
            "a Vice President who shall take office upon confirmation by a majority vote of both Houses of Congress.\n\n"
            "Section 3. Whenever the President transmits to the President pro tempore of the Senate and the Speaker "
            "of the House of Representatives his written declaration that he is unable to discharge the powers and "
            "duties of his office, and until he transmits to them a written declaration to the contrary, such powers "
            "and duties shall be discharged by the Vice President as Acting President.\n\n"
            "Section 4. Whenever the Vice President and a majority of either the principal officers of the executive "
            "departments or of such other body as Congress may by law provide, transmit to the President pro tempore "
            "of the Senate and the Speaker of the House of Representatives their written declaration that the "
            "President is unable to discharge the powers and duties of his office, the Vice President shall "
            "immediately assume the powers and duties of the office as Acting President. [...]"
        ),
        "plain": (
            "Clears up what happens if the President dies, resigns or can't do the job. The Vice President becomes "
            "President. If the vice presidency is empty, the President picks a new VP and Congress confirms them; "
            "this happened with Gerald Ford in 1973. The President can temporarily hand power to the VP, for example "
            "during surgery. Section 4 lets the VP and most of the cabinet declare the President unable to serve; it "
            "has never been used."
        ),
        "keywords": (
            "twenty fifth amendment succession president dies resign disability acting president vice president "
            "vacancy 25th amendment removal unable gerald ford"
        ),
    },
    {
        "id": "am26",
        "label": "26th Amendment (1971)",
        "title": "Voting age lowered to 18",
        "text": (
            "Section 1. The right of citizens of the United States, who are eighteen years of age or older, to vote "
            "shall not be denied or abridged by the United States or by any State on account of age.\n\n"
            "Section 2. The Congress shall have power to enforce this article by appropriate legislation."
        ),
        "plain": (
            "Lowered the voting age from 21 to 18. During the Vietnam War, many argued that if 18-year-olds could be "
            "drafted to fight, they should be able to vote. It was ratified in about 100 days, faster than any other "
            "amendment."
        ),
        "keywords": "twenty sixth amendment voting age 18 eighteen young people students vote youth vietnam",
    },
    {
        "id": "am27",
        "label": "27th Amendment (1992)",
        "title": "Congressional pay raises wait until after an election",
        "text": (
            "No law, varying the compensation for the services of the Senators and Representatives, shall take "
            "effect, until an election of Representatives shall have intervened."
        ),
        "plain": (
            "If Congress votes itself a pay raise, it can't take effect until after the next House election, so "
            "voters get a say first. James Madison proposed it in 1789, but it wasn't ratified until 1992, more than "
            "202 years later, thanks partly to a college student's campaign."
        ),
        "keywords": "twenty seventh amendment congress pay raise salary madison 1992 gregory watson",
    },
]

BY_ID = {p["id"]: p for p in PASSAGES}

# Grouping for the "Read the Constitution" tab
PARTS = [
    ("Preamble", ["pre"]),
    ("Article I: Congress (the legislative branch)", ["a1s1", "a1s2", "a1s3", "a1s4", "a1s5", "a1s6", "a1s7",
                                                       "a1s8", "a1s9", "a1s10"]),
    ("Article II: The President (the executive branch)", ["a2s1", "a2s2", "a2s3", "a2s4"]),
    ("Article III: The courts (the judicial branch)", ["a3s1", "a3s2", "a3s3"]),
    ("Article IV: The states", ["a4s1", "a4s2", "a4s3", "a4s4"]),
    ("Articles V to VII: Amending, supreme law, ratification", ["a5", "a6", "a7"]),
    ("Amendments 1 to 10: The Bill of Rights (1791)", [f"am{i}" for i in range(1, 11)]),
    ("Amendments 11 to 27", [f"am{i}" for i in range(11, 28)]),
]
