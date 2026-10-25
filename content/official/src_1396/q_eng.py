# -*- coding: utf-8 -*-
"""دفترچه ۱۳۹۶ — زبان انگلیسی (سوال‌های ۹۶ تا ۱۳۵)"""
Q = []

def add(no, q, c, s, k='', img=None):
    Q.append({"no": no, "q": q, "c": c, "s": s, "k": k, **({"img": img} if img else {})})

DIR = "Part One: Reading comprehension — Directions: Read the following passages carefully. Each Passage is followed by some questions. Complete the questions with the most suitable words or phrases (a, b, c, or d). Base your answers on the information given in the passage <u>only</u>."

P1 = ("<b>Passage 1</b><br>Just a few years ago, scientists did not know phytochemicals existed. But today they are the "
"new frontier in cancer-prevention research. This <u>pioneering science</u> couldn't have hit at a better time. "
"People are more confused than ever about the link between diet and health : margarine is healthier than "
"butter (or not); oat bran will save you (or won't); a little alcohol will keep heart attacks at bay (but give "
"you breast cancer). Just the effects of the popular vitamins known as antioxidants delivered a decidedly "
"pessimistic massage. “We should have a moratorium on unsubstantiated health claims for antioxidants and cancer,” "
"says Dr. Julie Buring of Brigham and Women's Hospital in Boston. Amid all the debate, phytochemicals offer the "
"next great hope for a magic pill, <u>one</u> that would go beyond vitamins.")

P2 = ("<b>Passage 2</b><br>The most serious health problem in the world used to be infectious diseases such as typhoid "
"fever, influenza (flu), and plague. In the 14<sup>th</sup> century for example, an epidemic of plague killed "
"roughly one-third of the population of Asia and about half of the population of Europe. A flu epidemic in 1918 "
"killed millions of people around the world. Today, however, vaccines and antibiotics have prevented the spread of many "
"serious diseases. In fact, in many parts of the world today, infectious diseases are no longer considered to be the "
"most serious health problem. However, today the number-one health problem in most countries is a new epidemic: the obesity.<br>"
"Two major reasons may be conceived for obesity. An obvious contributing factor is the sedentary lifestyle that many "
"people in the 21<sup>st</sup> century are leading; getting around by car and working at a desk do not demand much "
"physical activity, which is what people had to do to survive in the past. Now, however, we have to artificially "
"add it to our life. A second cause of the obesity epidemic is an increase in the availability and consumption of junk "
"food, defined as “foods which provide calories primarily through fats or added sugars and have minimum amounts of "
"vitamins and minerals&quot;. Studies have shown that people are consuming substantially more calories daily than "
"they used to, and they are consuming many of those calories outside of regular meals.")

P3 = ("<b>Passage 3</b><br>It is paradoxical that despite extensive advances in literacy and education as well as vastly "
"improved methods of communication, there still exists a great gap between the existing medical and health protective "
"knowledge and the public's acceptance and use of it. Professional journals are replete with reports, surveys of "
"school children, college students and the adult public that present discouraging and embarrassing evidence of failure "
"in this field. Many parents, for instance, still do not obtain immunization for their children and many drivers still "
"invite injury and death by drinking and driving, and not using belts. The use of cigarettes and patent medicines is "
"still widespread. One of the handicaps of public health work, of course, is the absence of pain and urgency.")

P4 = ("<b>Passage 4</b><br>Population aging has been accompanied by an epidemiological shift in the leading causes of "
"death from infectious and acute conditions associated with childhood to chronic conditions. A number of factors have "
"been associated with this epidemiological transition: modernization and urbanization (especially improvements in "
"standards of living and education) better nutrition, sanitation, health practices, and medical care.<br>"
"A project made by WHO suggested that, by 2015, deaths from chronic diseases – such as cancer, hypertension, "
"cardiovascular disease, and diabetes – would increase 17 percent, However, few developing countries have implemented "
"primary prevention programs to encourage those healthy lifestyle choices that would mitigate chronic diseases or "
"delay their onset. Rarely do developing countries have the appropriate medicines or adequate clinical care necessary "
"to treat these diseases.<br>"
"To encourage a prevention approach, WHO launched in 2002 its innovative Care for Chronic Conditions Framework, "
"aimed at policymakers in the health sector. This framework takes the approach that non-adherence to long-term "
"treatment regimens is fundamentally the failure of health systems to provide appropriate information, support, and "
"ongoing surveillance to reduce the burden of chronic disease. The framework also advises that a prevention approach "
"can mitigate these problems and contribute to healthier lifestyles. Delaying the onset of disability through "
"prevention approaches can both alleviate the growing demand for health care and, more important, improve the "
"quality of life for the elderly.")

V = "Part Two: Vocabulary Questions — Directions: Complete the following sentences by choosing the best answer."

# ─── Passage 1 (96–100) ───
add(96,
    "<b>"+DIR+"</b><br><br>"+P1+"<br><br>It can be inferred from the paragraph that the pioneering science (line 2) refers to the ..........",
    ["discovery of vitamins", "discovery of phytochemicals",
     "link between diet and health", "new knowledge about antioxidants"],
    "علم پیشگام به کشف/پیدایش phytochemicals اشاره دارد که در جملهٔ اول متن آمده است. گزینهٔ ۲.")

add(97,
    "The examples provided by the author in the third, fourth and fifth lines show how people are .......... the association of diet and health.",
    ["bored with", "supportive of", "neutral to", "uncertain about"],
    "متن: «People are more confused than ever about the link between diet and health» یعنی مردم نامطمئن/سردرگم‌اند. گزینهٔ ۴.")

add(98,
    "The writer states that the new discovery has .......... .",
    ["happened at the best possible time", "made people confident in previous understanding",
     "resulted in people's trust in scientific findings", "been the most influential in health"],
    "متن: «couldn't have hit at a better time» یعنی در بهترین زمان ممکن رخ داده است. گزینهٔ ۱.")

add(99,
    "Studying vitamins, scientists have presented the health impacts of .......... as an example of unverified claims.",
    ["newly discovered magic pills", "phytochemicals", "antioxidants", "margarine, oat bran and alcohol"],
    "متن: «unsubstantiated health claims for antioxidants and cancer» ⇒ ادعاهای اثبات‌نشده دربارهٔ آنتیاکسیدان‌ها. گزینهٔ ۳.")

add(100,
    "The underlined words (“one”) in the last sentence refers to .......... .",
    ["antioxidant pill", "hot debate", "phytochemical pill", "great hope"],
    "one به a magic pill اشاره دارد که دربارهٔ فایتوکمیکال‌ها است ⇒ قرص فایتوکمیکال. گزینهٔ ۳.")

# ─── Passage 2 (101–105) ───
add(101,
    P2+"<br><br>It is stated in the passage that infectious diseases ..........",
    ["tend to be the most serious health problem", "failed to be considered epidemic in the past",
     "used to kill half of the population world-wide", "are currently less health threatening than before"],
    "امروزه بیماری‌های عفونی دیگر جدی‌ترین مشکل بهداشت نیستند ⇒ کمتر تهدیدکننده‌اند. گزینهٔ ۴.")

add(102,
    "The second paragraph mainly discusses ..........",
    ["the definition of obesity", "the reasons why people turn to junk food",
     "why people get overweight", "how obesity is becoming a serious health problem"],
    "پاراگراف دوم دو دلیل عمدهٔ چاقی (سبک زندگی بی‌تحرک و تنقلات) را بیان می‌کند ⇒ چرا مردم چاق می‌شوند. گزینهٔ ۳.")

add(103,
    "According to the passage, people in the 21<sup>st</sup> century are .......... to lead a healthy lifestyle.",
    ["advised to get around by car", "required to do physical activity",
     "practically engaged in doing exercise", "recommended to underestimate physical activity"],
    "متن می‌گوید امروز باید فعالیت بدنی را «مصنوعی» به زندگی اضافه کرد ⇒ لازم/مجبور به فعالیت بدنی‌اند. گزینهٔ ۲.")

add(104,
    "According to the passage, .......... .",
    ["infectious diseases are the most threatening diseases today",
     "obesity used to be prevalent in the 20<sup>th</sup> century",
     "obesity is regarded as a significant health problem worldwide",
     "fast foods contribute more to obesity than sedentary life"],
    "چاقی اپیدمی شمارهٔ یک در اغلب کشورهاست ⇒ مشکل بهداشتی مهم در جهان. گزینهٔ ۳.")

add(105,
    "A suitable title for the passage would be .......... .",
    ["A new epidemic and its causes", "Modern lifestyle and diseases",
     "Obesity: a problem in developed countries", "Infections are more serious than expected"],
    "کل متن دربارهٔ چاقی به‌عنوان اپیدمی جدید و علل آن است. گزینهٔ ۱.")

# ─── Passage 3 (106–110) ───
add(106,
    P3+"<br><br>According to this passage, many of the articles published in health journals suggest ..........",
    ["proper growth and development in public health", "inadequate health education among the public",
     "more dropouts of the school and college students", "deterioration of lifestyle due to modern technology"],
    "گزارش‌ها «شواهد دلسردکننده‌ای از شکست» در پذیرش عمومی دانش بهداشتی نشان می‌دهند ⇒ آموزش بهداشت ناکافی در عموم. گزینهٔ ۲.")

add(107,
    "A factor hindering the success of public health is said to be ..........",
    ["lack of interest in applying health education findings",
     "the occurrence and prevalence of epidemics",
     "use of cigarettes and patent medicines",
     "widespread injury and death all over the world"],
    "عامل مانع «absence of pain and urgency» است؛ یعنی بی‌توجهی/عدم به‌کارگیری یافته‌های بهداشتی تا وقتی درد و فوریت نیست. گزینهٔ ۱.")

add(108,
    "The writer believes that, in the field of health education, pain .......... .",
    ["must be eliminated immediately", "is discouraging and embarrassing",
     "has been inadequately considered", "might be an enhancing factor"],
    "فقدان درد به‌عنوان یک «هندیکپ» ذکر شده؛ یعنی درد به‌طور کافی/مناسب در آموزش بهداشت لحاظ نشده است. گزینهٔ ۳.")

add(109,
    "The information given about the ignorance of parents and drivers ..........",
    ["is an example of lack of good communication methods", "supports the author's view of the gap mentioned in the passage",
     "refers to the handicaps of public health workers", "is considered the main cause of failure in health literacy"],
    "مثال والدین و رانندگان برای پشتیبانی از ادعای نویسنده دربارهٔ شکاف بین دانش و پذیرش عمومی آمده است. گزینهٔ ۲.")

add(110,
    "The writer seems to .......... .",
    ["be critical of education policy", "admire the extensive advances in education",
     "suggest some solutions to remove the gap", "be indifferent towards public health"],
    "لحن نویسنده نسبت به عدم کارایی سیاست‌های آموزشی بهداشت انتقادی است. گزینهٔ ۱.")

# ─── Passage 4 (111–115) ───
add(111,
    P4+"<br><br>Acute conditions mentioned in the first paragraph ..........",
    ["used to be common in the past", "have increased with urbanization",
     "are as common as current chronic conditions", "are still common throughout the world"],
    "متن از «شیفت» علت‌های مرگ از عفونی/حاد (مرتبط با دوران کودکی) به مزمن سخن می‌گوید ⇒ حادها در گذشته شایع بوده‌اند. گزینهٔ ۱.")

add(112,
    "It is stated in the passage that .......... can improve the quality of life for the elderly.",
    ["transitional approaches", "mitigating infectious conditions",
     "implementing a new health system", "ongoing clinical supervision"],
    "ذکر «ongoing surveillance» در چارچوب مراقبت از بیماری‌های مزمن و بهبود کیفیت زندگی سالمندان (طبق کلید رسمی). گزینهٔ ۴.")

add(113,
    "The necessary step which should be taken by health policy makers is to ..........",
    ["focus on both prevention and sustained treatment", "alleviate the number of acute diseases",
     "delay the onset of urban life-style", "provide appropriate regimens and encourage urbanization"],
    "چارچوب WHO بر رویکرد پیشگیری و پایبندی به درمان بلندمدت (هر دو) با سیاست‌گذاران تمرکز دارد. گزینهٔ ۱.")

add(114,
    "According to the text, prevention can ..........",
    ["subject the person to numerous lifestyles", "accelerate the onset of long-term regimens",
     "reduce the burden of acute diseases", "decrease the burden on the healthcare providers"],
    "تأخیر در ناتوانی از طریق پیشگیری «تقاضای رو به رشد برای مراقبت بهداشتی را کاهش می‌دهد» ⇒ کم‌کردن بار نظام سلامت. گزینهٔ ۴.")

add(115,
    "Many developing countries .......... to reduce chronic diseases.",
    ["have recently taken the necessary measures", "have failed to provide continuing surveillance",
     "adhere to suitable lifestyle choices", "follow the long-term treatment regimens"],
    "متن: برنامه‌های پیشگیری در کشورهای درحال‌توسعه کم اجرا شده و دارو/مراقبت کافی ندارند ⇒ در ارائهٔ نظارت مداوم ناموفق‌اند. گزینهٔ ۲.")

# ─── Vocabulary (116–135) ───
add(116,
    "<b>"+V+"</b><br>TV reporters .......... the truth about what had happened in the university campus. They presented a wrong picture of the event.",
    ["distorted", "applied", "confirmed", "reflected"],
    "distorted = تحریف کردند؛ با «تصویر غلط» هم‌معناست. گزینهٔ ۱.")

add(117,
    "Insufficient foods along with .......... in protein, minerals and vitamins in the diet all affect physical fitness and work capacity.",
    ["concentration", "incidence", "deficiencies", "indications"],
    "deficiencies = کمبودها (پروتئین، مواد معدنی و ویتامین‌ها). گزینهٔ ۳.")

add(118,
    "Increased cholesterol levels in the blood can cause fatty .......... , followed by the thickening of the artery walls.",
    ["minerals", "deposits", "nutrients", "substances"],
    "fatty deposits = رسوب‌های چربی (تصلب شرایین). گزینهٔ ۲.")

add(119,
    "Drains should be .......... to carry away fluid which might act as a culture medium for bacteria.",
    ["dispatched", "penetrated", "perforated", "inserted"],
    "inserted = درج/قرار داده شوند (درن گذاشتن). گزینهٔ ۴.")

add(120,
    "Lack of appetite .......... his recovery from illness, so he was given a drug to stimulate his appetite.",
    ["hampered", "concealed", "promoted", "accelerated"],
    "hampered = مانع شد/به تاخیر انداخت (بی‌اشتهایی مانع بهبودی شد). گزینهٔ ۱.")

add(121,
    "There are numerous instances indicating that lasers can successfully .......... a given clinical task.",
    ["converse", "accomplish", "agitate", "aggravate"],
    "accomplish = انجام دادن (تکمیل یک کار بالینی). گزینهٔ ۲.")

add(122,
    "Lung cancer is a(n) .......... disease that comes on slowly and does not have obvious symptoms at first. The person is not aware of its development.",
    ["insidious", "precious", "lucrative", "tentative"],
    "insidious = خزنده/موذیانه (بیماری که بی‌خبرد و آهسته پیشرفت می‌کند). گزینهٔ ۱.")

add(123,
    "The currently used vaccines are live strains .......... by several subcultures so as to reduce the virulence of microbes.",
    ["intoxicated", "evaporated", "attenuated", "neutralized"],
    "attenuated = ضعیف‌شده (واکسن‌های زندهٔ تضعیف‌شده). گزینهٔ ۳.")

add(124,
    "Monitoring of .......... signs most commonly includes blood pressure, heart, pulse and respiratory rates.",
    ["viral", "vital", "fatal", "lethal"],
    "vital signs = علائم حیاتی. گزینهٔ ۲.")

add(125,
    "After smallpox and cattle plague, polio seems to be the next disease around the world to be successfully .......... by the joint efforts of WHO and UNICEF.",
    ["eradicated", "encouraged", "released", "sustained"],
    "eradicated = ریشه‌کن شدن (بیماری). گزینهٔ ۱.")

add(126,
    "For such patients, work or exercise usually .......... the case and may cause congestion and inflammation of important body organs.",
    ["evolves", "flourishes", "refines", "aggravates"],
    "aggravates = تشدید می‌کند/بدتر می‌کند. گزینهٔ ۴.")

add(127,
    "People suffering from malnutrition are .......... , lethargic, bored and depressed.",
    ["optimistic", "listless", "enthusiastic", "tranquil"],
    "listless = بی‌حال/بی‌رمق (هم‌خانواده با lethargic). گزینهٔ ۲.")

add(128,
    "In the case of acute inflammation, trauma and hemorrhage, the usage of superficial heat should be .......... because of its contraindications.",
    ["elevated", "appreciated", "forbidden", "accelerated"],
    "forbidden = ممنوع (به علت موارد منع استفاده). گزینهٔ ۳.")

add(129,
    "Having a kind and considerate behavior towards the employees is very important for a manager, as it can .......... feelings of love for the workplace.",
    ["eliminate", "alleviate", "purchase", "induce"],
    "induce = ایجاد/برانگیختن (احساس علاقه به محیط کار). گزینهٔ ۴.")

add(130,
    "Physical fitness means energetically performing daily tasks to the best of your ability without getting .......... and worn out.",
    ["apprehensive", "disappointed", "exhausted", "anxious"],
    "exhausted = خستهٔ فرسوده (هم‌راستا با worn out). گزینهٔ ۳.")

add(131,
    "The hospital's policies and rules are for the purpose of the .......... of patients' safety.",
    ["enhancement", "competence", "adherence", "degeneration"],
    "enhancement = ارتقا/افزایش (ایمنی بیماران). گزینهٔ ۱.")

add(132,
    "Damaged tooth enamel can allow the bacteria to more easily .......... the tooth and form a cavity.",
    ["invest", "evade", "avoid", "invade"],
    "invade = تهاجم/نفوذ کردن به دندان. گزینهٔ ۴.")

add(133,
    "If one of a person's kidneys is .......... , the person can still live with the other kidney.",
    ["avoided", "removed", "operated", "transmitted"],
    "removed = برداشته/خارج شود. گزینهٔ ۲.")

add(134,
    "A patient who is .......... for less than 24 hours is considered as an outpatient; his/her details are registered, together with the names of the personnel.",
    ["immunized", "anesthetized", "hospitalized", "energized"],
    "hospitalized = بستری شدن (کمتر از ۲۴ ساعت = سرپایی). گزینهٔ ۳.")

add(135,
    "For skin injuries, patients are mostly advised to regularly .......... the prescribed ointments to a wound.",
    ["drain", "apply", "inject", "swallow"],
    "apply = مالیدن/به‌کار بردن (پماد). گزینهٔ ۲.")
