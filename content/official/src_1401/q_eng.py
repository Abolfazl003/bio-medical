# -*- coding: utf-8 -*-
"""دفترچه ۱۴۰۱ — زبان عمومی (سوال‌های ۸۱ تا ۱۲۰)"""
Q = []

def add(no, q, c, s, k='', img=None):
    Q.append({"no": no, "q": q, "c": c, "s": s, "k": k, **({"img": img} if img else {})})

V = "Part one: Vocabulary — Directions: Complete the following sentences by choosing the best answer."

add(81,
    "<b>" + V + "</b><br>Waves of frustration and .......... came after the committee decision led to the unemployment of the staff nurses.",
    ["distention", "discontent", "appraisal", "approval"],
    "discontent = نارضایتی؛ با waves of frustration همنشین است. گزینهٔ ۲.")

add(82,
    "A diet containing high levels of fat or sugar and few nutrients can lead to .......... .",
    ["famine", "slimness", "obesity", "fitness"],
    "obesity = چاقی مفرط؛ رژیم پرچرب/پرقند منجر به چاقی می‌شود. گزینهٔ ۳.")

add(83,
    "The mark of a genius is the willingness to explore all the .......... , not just the most likely solution.",
    ["alternatives", "drawbacks", "generations", "disturbances"],
    "alternatives = گزینه‌ها/راه‌حل‌های جایگزین. گزینهٔ ۱.")

add(84,
    "Creative thinking requires an attitude that allows you to search for ideas and .......... your knowledge and experience.",
    ["terminate", "neutralize", "manipulate", "undermine"],
    "manipulate = به‌کار گرفتن/دست‌کاری کردن؛ یعنی بهره بردن از دانش و تجربه. گزینهٔ ۳.")

add(85,
    "If you think creatively, you will find out new ways to .......... your objectives more effectively.",
    ["abolish", "constrain", "constrict", "fulfill"],
    "fulfill = محقق کردن/اجرا کردن اهداف. گزینهٔ ۴.")

add(86,
    "The transplantation of body organs needs the .......... of the dead patient's guardians.",
    ["dissent", "consent", "revival", "denial of"],
    "consent = رضایت؛ پیوند اعضا به رضایت قیمومان نیاز دارد. گزینهٔ ۲.")

add(87,
    "An investigation into the history of cardiovascular diseases in the family showed that the members of the family were .......... such diseases.",
    ["predisposed to", "extended to", "precipitated by", "extradited by"],
    "predisposed to = مستعد به؛ افراد خانواده به بیماری‌ها مستعد بودند. گزینهٔ ۱.")

add(88,
    "The doctor ordered a chest X-ray since the respiratory symptoms were not .......... to reach a proper diagnosis.",
    ["deficient", "fictitious", "sufficient", "ambitious"],
    "sufficient = کافی؛ علائم برای تشخیص کافی نبودند. گزینهٔ ۳.")

add(89,
    "WHO and other health organizations are trying hard to .......... the COVID-19 disease which still cause fatalities.",
    ["accelerate", "aggregate", "potentiate", "eradicate"],
    "eradicate = ریشه‌کن کردن. گزینهٔ ۴.")

add(90,
    "People in .......... societies benefit from care facilities while those financially at a disadvantage are deprived of such facilities.",
    ["affluent", "cultivated", "indigent", "debilitated"],
    "affluent = مرفه؛ تقابل با financially at a disadvantage. گزینهٔ ۱.")

add(91,
    "The physically fragile are more .............. infectious diseases than the physically robust.",
    ["suspicious about", "amenable to", "enthusiastic about", "resistant to"],
    "amenable to = پذیرا/آسیب‌پذیر نسبت به. گزینهٔ ۲.")

add(92,
    "Thank to the intensive mass vaccination, the flu virus .......... soon after its onset.",
    ["resist", "reside", "subside", "persist"],
    "subside = فروکش کردن/کاهش یافتن. گزینهٔ ۳.")

add(93,
    "Contact lenses sometimes give better visual .......... to those in need.",
    ["blurredness", "acuity", "infirmity", "restriction"],
    "acuity = وضوح/تیزی دید. گزینهٔ ۲.")

add(94,
    "With the .............. of each semester, students take new courses to attend classes.",
    ["adherence", "disturbance", "disruption", "commencement"],
    "commencement = آغاز/شروع. گزینهٔ ۴.")

add(95,
    "The weather in big cities is filled with .......... , causing numerous health problems.",
    ["detergents", "disinfectants", "contaminants", "contractors"],
    "contaminants = آلاینده‌ها. گزینهٔ ۳.")

add(96,
    "Based on a recent study, forty percent of the offices in the city .......... with nobody residing in.",
    ["viable", "vacant", "occupied", "preserved"],
    "vacant = خالی/مسکون‌نشده. گزینهٔ ۲.")

add(97,
    "The old hospital was .......... and a modern one with new equipment was built as a replacement.",
    ["deployed", "detained", "drenched", "demolished"],
    "demolished = تخریب‌شده. گزینهٔ ۴.")

add(98,
    "After taking the antibiotic, she developed some serious allergic reactions which resulted in a(n) .......... in her throat and blocked her breathing.",
    ["obstruction", "ingestion", "suspension", "maturation"],
    "obstruction = انسداد/گرفتگی گلو. گزینهٔ ۱.")

add(99,
    "WHO believes that the cost of COVID-19 vaccination is clearly .......... by its life-saving values.",
    ["resumed", "compensated", "manipulated", "intervened"],
    "compensated = جبران‌شده؛ هزینه با ارزش حیات‌بخشی جبران می‌شود. گزینهٔ ۲.")

add(100,
    "Garlic is well known for causing a severe .......... breath that can have unpleasant social consequences.",
    ["malodorous", "malformed", "vigilant", "vigorous"],
    "malodorous = بدبو. گزینهٔ ۱.")

P1 = ("Part two: Reading Comprehension — Directions: Read the following passages carefully. Each passage is followed by some questions. "
      "Complete the questions with the most suitable words or phrases (a, b, c, or d). Base your answers on the information given in the passage <u>only</u>.<br><br>"
      "<b>Passage 1</b><br>Urgently needed for addressing the energy question is a national energy plan, not only to address future "
      "energy needs, but also to avoid repeating the errors of the past. Subsidies to the airlines, for example, have "
      "encouraged the growth of less efficient forms of transportation: lack of support of the railroad industry has "
      "discouraged the use of rail transportation. Federal support for the development of a nationwide highway "
      "system, though making road travel far safer, has led to greater use of cars, with accompanying increases in "
      "the consumption of gasoline. Another example was the shift by the railroads, immediately before and after "
      "World War II from coal-fired steam locomotives to diesel-electric units. The Clean Air Act of 1970 also "
      "encouraged the consumption of fuels that are in limited supply, by causing industrial and power plant "
      "operators to switch from coal to natural gas and oil to meet air pollution standards. Nor has the government "
      "done anything to require changes in the rate structures for natural gas and electricity, <u>which</u> promoted higher "
      "consumption by offering a large number of users a lower price per unit.")

add(101,
    "<b>" + P1 + "</b><br><br>According to the text, a sound national energy plan will .......... .",
    ["help increase airlines' subsidies and make road travel safer",
     "contribute to the growth of less efficient forms of transportation",
     "assist in meeting energy needs",
     "result in repeating errors of the past"],
    "بر اساس جملهٔ اول متن، برنامهٔ ملی انرژی برای پاسخ به نیازهای آیندهٔ انرژی لازم است. گزینهٔ ۳.")

add(102,
    "This passage mainly .......... .",
    ["discusses the existing problems with saving energy",
     "deals with air pollution problem and concerns",
     "focuses on advantages of the fossil fuel and gas in human life",
     "warns against the use of the existing transportation means"],
    "متن عمدتاً مشکلات موجود در سیاست‌گذاری/صرفه‌جویی انرژی را با مثال‌هایی برمی‌شمارد. گزینهٔ ۱.")

add(103,
    "The word <u>which</u> in the last sentence refers to .......... .",
    ["what the government has done to preserve energy",
     "lack of change in the gas and electricity rate structure",
     "the decline in the consumption of gas and electricity",
     "the users' observance of air pollution standards"],
    "which به «عدم انجام کاری برای تغییر ساختارهای نرخی گاز و برق» اشاره دارد که مصرف بیشتر را ترویج کرده است. گزینهٔ ۲.")

add(104,
    "According to the passage, the development of a nationwide highway system has .......... .",
    ["increased road accidents with dramatic effects",
     "caused less fuel consumption and higher speed",
     "encouraged more and more use of private cars",
     "reduced the subsidies to the airlines and railroad industry"],
    "متن: «has led to greater use of cars» — یعنی استفادهٔ بیشتر از خودروهای شخصی. گزینهٔ ۳.")

add(105,
    "The shift to natural gas and use of diesel-electric units, as encouraged by the government, are .......... .",
    ["mentioned as examples of appropriate planning for future energy needs",
     "criticized by the writer as they fail to address the future energy needs",
     "the ways the writer believes to be supported so that past errors are avoided",
     "the ways the government is supporting to increase its national income"],
    "این موارد به‌عنوان مثال از خطاهای گذشته (مصرف سوخت‌های با منابع محدود) نقد شده‌اند. گزینهٔ ۲.")

P2 = ("<b>Passage 2</b><br>Today, the level of healthcare has improved a lot. Presently, the goal of health care is to have a continuum of "
      "care for the patient; one which is integrated at all levels. Many hospitals offer a referral service or discharge "
      "plan to patients who are being discharged. Plans for the patients are discussed with a discharge planner, a "
      "person who is trained in assessing what the patients' requirements for healthcare will be after discharge from "
      "the hospital. <u>This</u> enables the patients to continue their care at a level which is most appropriate for them. "
      "Items reviewed for discharge planning include but are not limited to therapies, medication needs, living "
      "arrangements and identification of specific goals. A few of the options that are available for persons being "
      "discharged from an acute care hospital can include home health care, assisted living facilities, long-term care "
      "or hospice. Among numerous care facilities, home health care is one of the fastest growing segments of the "
      "healthcare industry. Alternatives for home care can meet both the medical and non-medical needs of a "
      "patient. <u>These services</u> are provided to patients and their families at home or place of residence. Home care "
      "is a method of delivering nursing care and other therapies as required by the patient's needs.")

add(106,
    "<b>" + P2 + "</b><br><br>The main idea of the passage is to .......... healthcare services.",
    ["highlight the improvements of", "compare the present and past",
     "challenge the achievements of", "introduce the obstacles affecting"],
    "متن پیشرفت‌های خدمات مراقبت سلامت (مراقبت پیوسته، ترخیص برنامه‌ریزی‌شده، مراقبت خانگی) را برجسته می‌کند. گزینهٔ ۱.")

add(107,
    "Referral services or discharge plans to patients .......... .",
    ["were already common in traditional medicine",
     "are to be removed to reduce treatment costs",
     "are recent developments in healthcare",
     "were rooted in health assessment policies"],
    "این خدمات جزو تحولات جدید (Today/Presently) در مراقبت سلامت معرفی شده‌اند. گزینهٔ ۳.")

add(108,
    "The underlined word “<u>This</u>” refers to .......... .",
    ["a post-recovery discharge from the hospital",
     "assessing the patients' post-discharge needs",
     "a trained person's ability to assess the needs",
     "a discharge planner's healthcare assessment"],
    "طبق کلید اولیه گزینهٔ ۴؛ This به ارزیابی/اقدام برنامه‌ریز ترخیص اشاره دارد. گزینهٔ ۴.")

add(109,
    "Home healthcare, assisted living facilities, long-term care, or hospice are .......... patients discharged from acute care hospitals.",
    ["no longer available for", "among the follow-up care services for",
     "proved to be largely inappropriate for", "not necessary for"],
    "این‌ها «options» موجود برای بیماران ترخیص‌شده از بیمارستان‌های مراقبت حاد هستند. گزینهٔ ۲.")

add(110,
    "The underlined phrase “<u>These services</u>” refers to .......... .",
    ["care facilities", "growing segments", "medical and non-medical needs", "alternatives for home care"],
    "These services به «alternatives for home care» (گزینه‌های مراقبت خانگی) اشاره دارد. گزینهٔ ۴.")

P3 = ("<b>Passage 3</b><br>A developmental disability is defined as severe chronic disability that is attributable to a mental or physical "
      "impairment or combination of mental and physical impairments. Individuals with developmental disabilities "
      "were generally housed in institutions for the first half of the 20<sup>th</sup> century. Little attention was paid to their "
      "education, or medicinal or nutritional care. In 1963, The Developmental Disabilities Assistance and Bill of "
      "Rights was passed. Through this Act, federal funds supported the development and operation of state "
      "councils, protection and advocacy systems, university centers, and projects of national significance. This act "
      "provided the structure to assist people with developmental disabilities to pursue meaningful and productive "
      "lives. The institutions that housed these individuals gradually were closed or reduced in size. By 1975 these "
      "individuals were cared for at home, in schools or in small residential facilities. In 1975, Public Law (PL) "
      "94-142 was passed, opening public schools to children with developmental disabilities. In 1985, PL 99-487 "
      "(102-119 in 1992), The Early Intervention Act, was passed, bringing services to children from birth to school "
      "age.")

add(111,
    "<b>" + P3 + "</b><br><br>Individuals with developmental disabilities were .......... for the first half of the 20th century.",
    ["provided with limited education", "offered proper medical or nutritional care",
     "mostly denied of being housed in institutions", "eager to attend the education arranged for them"],
    "متن: «Little attention was paid to their education, or medicinal or nutritional care» ⇒ آموزش محدود. گزینهٔ ۱.")

add(112,
    "The year 1963 .......... for passing the “Developmental Disabilities Assistance and Bill of Rights”.",
    ["should be notorious", "is ethically disapproved", "is right to be condemned", "deserves special appreciation"],
    "تصویب این قانون ساختار کمک به این افراد را فراهم کرد، پس سال ۱۹۶۳ شایستهٔ قدردانی ویژه است. گزینهٔ ۴.")

add(113,
    "The dispatch of federal funds to support individuals with developmental disabilities .......... .",
    ["was a common happening long before the first half of the 20th century",
     "caused successful elimination of the causes of developmental disabilities",
     "followed the passing of the Developmental Disabilities Assistance and Bill of Rights",
     "proved ineffective despite the huge effort made to pass the law and allocate the funds"],
    "«Through this Act, federal funds supported ...» ⇒ تخصیص بودجه پس از تصویب قانون بود. گزینهٔ ۳.")

add(114,
    "The institutions housing those with developmental disabilities .......... .",
    ["continued offering care to all in need", "gradually became fewer and smaller",
     "failed to meet their intended goals prior to 1963", "set up new branches in rural areas following 1963"],
    "متن: «The institutions ... gradually were closed or reduced in size.» ⇒ کمتر و کوچک‌تر شدند. گزینهٔ ۲.")

add(115,
    "Opening public schools to children with developmental disabilities .......... the Developmental Disabilities Assistance and Bill of Rights.",
    ["proved to be redundant following", "happened nearly a decade after", "well coincides with", "well preceded"],
    "قانون ۱۹۶۳ و PL 94-142 در ۱۹۷۵ ⇒ حدود یک دهه بعد. گزینهٔ ۲.")

P4 = ("<b>Passage 4</b><br>Deep Learning in medicine is one of the most rapidly and new developing fields of science which has "
      "recently gathered momentum. Currently, almost every device intended for medical imaging has a more or "
      "less extended image and signal analysis and processing module which can use deep learning. It provides "
      "quantitative data necessary to make a diagnosis. The obtained quantitative features must be independent of "
      "the inter-subject variability and the type of medical device and, above all, must allow for reproducible results "
      "in the presence of high noise. The proposed deep learning algorithm should also ensure the independence of "
      "the results obtained by the operator of the imaging device and, to be more exact, <u>its</u> position relative to the "
      "patient or the parameter settings in the device. In addition, the proposed deep learning algorithms must be "
      "tailored for the diagnosis of a specific disease entity. On the other hand, they must allow for reproducible "
      "results for high inter-subject variability. These criteria make it difficult to propose a methodology for the "
      "deep learning algorithms.")

add(116,
    "<b>" + P4 + "</b><br><br>Deep Learning in medicine .......... .",
    ["has a long history", "has witnessed a sharp decline", "is experiencing a speedy growth", "is falling behind other fields of science"],
    "متن: «one of the most rapidly ... developing fields ... gathered momentum» ⇒ رشد سریع. گزینهٔ ۳.")

add(117,
    "Nearly all medical imaging devices .......... .",
    ["prove incompatible with deep learning", "simplify deep learning analysis",
     "are independent of deep learning", "deploy deep learning"],
    "متن: «almost every device intended for medical imaging ... can use deep learning» ⇒ به کار می‌گیرند. گزینهٔ ۴.")

add(118,
    "Which of the following is <u>NOT</u> true about deep learning?",
    ["The diagnostic data are mostly qualitative.", "Its obtained features are device independent.",
     "Its obtained features must be subject-dependent.", "The results must be reproducible."],
    "طبق کلید اولیه گزینهٔ ۱؛ متن بر داده‌های کمی (quantitative) تأکید دارد نه کیفی. گزینهٔ ۱.")

add(119,
    "What does the underlined word “<u>its</u>” refer to?",
    ["The operator", "The patient", "The deep learning algorithm", "The imaging device"],
    "طبق کلید اولیه گزینهٔ ۳؛ its به الگوریتم/شیء مورد بحث اشاره دارد. گزینهٔ ۳.")

add(120,
    "The writer .......... a methodology for the deep learning algorithms.",
    ["criticizes criteria set to propose", "already seems determined to propose",
     "views as impossible proposing", "describes as challenging proposing"],
    "متن: «These criteria make it difficult to propose a methodology» ⇒ ارائهٔ یک روش‌شناسی را چالش‌برانگیز توصیف می‌کند. گزینهٔ ۴.")
