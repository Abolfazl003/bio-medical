# -*- coding: utf-8 -*-
"""دفترچه ۱۳۹۷ — زبان عمومی (سوال‌های ۱۰۱ تا ۱۴۰)"""
Q = []

def add(no, q, c, s, k='', img=None):
    Q.append({"no": no, "q": q, "c": c, "s": s, "k": k, **({"img": img} if img else {})})

HDR = "Part One: Vocabulary — Complete the following sentences, choosing the most appropriate option (a, b, c, or d)."

add(101, HDR + "<hr>Like any vaccine, \"cancer vaccine\" ……... the immune system to attack a dangerous enemy.",
    ["instructs", "defies", "challenges", "hinders"],
    "instructs = آموزش می‌دهد/هدایت می‌کند. واکسن سرطان سیستم ایمنی را برای حمله هدایت می‌کند. گزینهٔ ۱. (defies=ناپذیرفتن/مقاومت، challenges=به چالش کشیدن، hinders=مانع شدن)")

add(102, "A medical computer system is an aid to physicians due to its capacity to ………….. the data from a patient's history and provide a diagnosis.",
    ["intervene in", "interrupt", "interact with", "interpret"],
    "interpret = تفسیر کردن. ظرفیت تفسیر داده‌های پروندهٔ بیمار و ارائهٔ تشخیص. گزینهٔ ۴.")

add(103, "Medical authorities provide the students with enough …………….. to continue their projects.",
    ["incentive", "modification", "withdrawal", "affliction"],
    "incentive = انگیزه/مشوق. گزینهٔ ۱. (modification=اصلاح، withdrawal=پس‌گیری، affliction=رنج)")

add(104, "Although he often does crazy things in class, he always ……………….. the rules and regulations of the university.",
    ["refuses", "obeys", "discards", "avoids"],
    "obeys = اطاعت/پیروی می‌کند؛ سازگار با Although. گزینهٔ ۲.")

add(105, "Some examples of changing lifestyle are eating nutritious foods, doing daily exercise and smoking…………………………... .",
    ["enhancement", "persistence", "promotion", "cessation"],
    "smoking cessation = ترک سیگار؛ از مثال‌های تغییر سبک زندگی است. گزینهٔ ۴. (enhancement=افزایش، persistence=پافشاری، promotion=ارتقا)")

add(106, "In order to help students understand mathematical problems, teachers should sufficiently ……………….. problematic points.",
    ["collaborate with", "compete with", "elaborate on", "compromise on"],
    "elaborate on = به تفصیل شرح دادن. گزینهٔ ۳. (collaborate with=همکاری کردن با، compete with=رقابت با، compromise on=سازش درباره)")

add(107, "Drugs in the form of pill or syrup are more easily ……………..compared to other types.",
    ["ingested", "dismissed", "invaded", "distorted"],
    "ingested = بلعیده/جذب‌شده از راه دهان. گزینهٔ ۱. (dismissed=رد/اخراج، invaded=مورد تهاجم، distorted=تحریف‌شده)")

add(108, "Chemicals from the factory caused …………………. of water and death of animals in the sea.",
    ["infusion", "immersion", "contamination", "congestion"],
    "contamination = آلودگی. گزینهٔ ۳. (infusion=تزریق/داخل‌ریز، immersion=غوطه‌وری، congestion=ازدحام/احتقان)")

add(109, "Iranian ministry of health has ……………………. a revolutionary program to make substantial changes in the nursing care system.",
    ["devastated", "initiated", "accumulated", "alleviated"],
    "initiated = آغاز/کلید زده است. گزینهٔ ۲. (devastated=ویران کرده، accumulated=انباشته، alleviated=کاهش/تخفیف داده)")

add(110, "Everybody …………….. him in the meeting due to his effective and interesting presentation.",
    ["criticized", "ignored", "disgusted", "applauded"],
    "applauded = تشویق/کف زدن؛ متناسب با ارائهٔ مؤثر و جذاب. گزینهٔ ۴.")

add(111, "Some medical interventions are complicated and require ………………… decisions and actions based on consultation with specialists.",
    ["reckless", "accountable", "sensible", "trivial"],
    "sensible = عاقلانه/معقول. گزینهٔ ۳. (reckless=بی‌احتیاط، accountable=پاسخ‌گو، trivial=ناچیز/جزئی)")

add(112, "When I eat solid food, I have to chew it for a long time before I can ……………………. it.",
    ["swallow", "bite", "grind", "crush"],
    "swallow = بلعیدن. گزینهٔ ۱. (bite=گاز گرفتن، grind=آسیاب کردن، crush=له کردن)")

add(113, "At home, we usually wear …………………….. ; however, we should be really formal at work.",
    ["casually", "graciously", "martially", "toughly"],
    "casually = غیررسمی/راحت؛ در تقابل با formal در however. گزینهٔ ۱.")

add(114, "Active people seem to live longer than similar but ……… people.",
    ["agile", "sedentary", "gloomy", "febrile"],
    "sedentary = کم‌تحرک/نشسته؛ در تقابل با active. گزینهٔ ۲. (agile=چابک، gloomy=افسرده، febrile=تب‌دار)")

add(115, "When the balance of the body chemicals and hormones is ….. , some organs may malfunction.",
    ["distributed", "distinguished", "disturbed", "dislocated"],
    "disturbed = به‌هم‌ریخته/برهم‌خورده. گزینهٔ ۳. (distributed=توزیع‌شده، distinguished=متمایز، dislocated=دررفته)")

add(116, "Individuals not vaccinated against smallpox will be …………………. to it.",
    ["recessive", "resisted", "dormant", "vulnerable"],
    "vulnerable (to) = آسیب‌پذیر/در معرض. گزینهٔ ۴. (recessive=مغلوب/عقب‌نشسته، dormant=خفته، resisted=مقاومت‌شده)")

add(117, "All students at every level, from elementary to university, need to observe ………………., i.e. stick to an arranged or correct time.",
    ["penetration", "reliability", "reputation", "punctuality"],
    "punctuality = وقت‌شناسی — توضیح i.e. «وقت تعیین‌شده» آن را تأیید می‌کند. گزینهٔ ۴.")

add(118, "See your dentist if you notice swelling or bleeding in your gums. Early intervention is the key to …………………….. the infection before it becomes serious.",
    ["combating", "confusing", "diluting", "mantling"],
    "combating = مبارزه کردن با عفونت. گزینهٔ ۱. (confusing=سردرگم کردن، diluting=رقیق کردن، mantling=پوشاندن)")

add(119, "An important …………….. contributing to people's longevity is certainly their healthy lifestyle.",
    ["assessment", "obstacle", "contradiction", "variable"],
    "variable = عامل/متغیر — «عامل مهم مؤثر بر طول عمر». گزینهٔ ۴. (assessment=ارزیابی، obstacle=مانع، contradiction=تناقض)")

add(120, "Antibiotics are useless against flu viruses but there is a home …………….. that has been passed down through generations and science supports this.",
    ["repression", "remedy", "proportion", "appliance"],
    "(home) remedy = داروی/درمان خانگی. گزینهٔ ۲. (repression=سرکوب، proportion=تناسب، appliance=وسیله)")

P1H = "Part Two: Reading Comprehension — Passage 1<hr>"
P1 = ("Doctors have come to realize that it takes more than medicine for a patient to recover. Patients who are "
"hospitalized spend most of the day in bed feeling sorry for themselves and hoping to get better. It is "
"important to get the patient to interact and get involved in various activities. Health care providers should "
"be educated on the fact that for patients to recover faster there has to be a good relationship between "
"patient and healthcare providers. A survey done at hospitals revealed that patients who had friendly and "
"warm relationships with their nurses and doctors developed strong trusting relationships and in a short "
"time recovered.<br><br>"
"Some ways that health care providers can use to promote that friendliness and warmth includes touch. "
"When people are sick they feel like people reject them and don't want to associate with them. This is "
"where the health care providers are expected <u>to go an extra mile</u>. Sit by the patient's bedside, assess how "
"he/she feels to offer reassurance and comfort, touch the patient and smile. Be sure to first consult with the "
"patient because in some cultures touch is considered inappropriate, but a smile is always helpful.")

add(121, P1H + P1 + "<hr>121- Patient recovery is ………………… by medicine alone.",
    ["hard to achieve", "recommended", "exacerbated", "is sure to happen"],
    "از جملهٔ اول متن: «it takes more than medicine for a patient to recover» یعنی بهبود فقط با دارو سخت به دست می‌آید. گزینهٔ ۱. (exacerbate=بدتر کردن)")

add(122, "Passage 1 (above)<hr>122- Patients in bed are required to ………………. activities.",
    ["get hospitalized to avoid", "feel sorry for missing", "get engaged in different", "keep away from various"],
    "«It is important to get the patient to interact and get involved in various activities.» ⇒ get engaged in different activities. گزینهٔ ۳.")

add(123, "Passage 1 (above)<hr>123- Good rapport between the patient and health care provider can ………….. recovery.",
    ["postpone", "speed up", "rule out", "downgrade"],
    "رابطهٔ خوب باعث تسریع بهبود می‌شود (…recovered in a short time). speed up = تسریع کردن. گزینهٔ ۲. (rule out=رد کردن، downgrade=تنزل دادن)")

add(124, "Passage 1 (above)<hr>124- \"Touch\" is referred to as …………….. developing affection and kindness between the patient and health care providers.",
    ["an end in", "a treatment for", "a barrier in", "a means of"],
    "لمس به‌عنوان «وسیله‌ای» برای ایجاد صمیمیت ذکر شده است (ways ... includes touch). a means of = وسیله‌ای برای. گزینهٔ ۴.")

add(125, "Passage 1 (above)<hr>125- The underlined expression \"to go an extra mile\" in the second paragraph means to ………..",
    ["cover more distance", "pay more attention", "seek more help", "have more rest"],
    "اصطلاح go an extra mile یعنی فراتر از وظیفه تلاش کردن/توجه بیشتر کردن. گزینهٔ ۲.")

P2H = "Part Two: Reading Comprehension — Passage 2<hr>"
P2 = ("In addition to simple pain or sprains which result from overtraining, a new research found that doing "
"excessive endurance exercise - especially during middle-age and beyond - could theoretically lead to "
"unhealthy structural changes in the chambers of the heart. More isn't always better when it comes to "
"running and endurance training. It's also important to realize that what's \"vigorous\" for one runner is not "
"going to be vigorous for another. For older people or <u>those who haven't broken a sweat in a while</u>, brisk "
"walking might constitute a tough workout.<br><br>"
"\"I think the best way to exercise and avoid risk of injury revolves around perception of effort, rather "
"than time or duration,\" he says. \"At least twice a week, you want to exercise at an intensity that you "
"perceive as hard.\" At most, you want to alternate between hard and easy days\", so your body has 48 hours "
"to recover.\"")

add(126, P2H + P2 + "<hr>126- According to the passage, ………………. .",
    ["typically the more exercise you do, the better it is",
     "the more exercise you do, the fewer injuries you get",
     "there is no association between intensity of exercise and its usefulness",
     "in some cases, more exercise means more damage to the body"],
    "«More isn't always better» و صدمات قلبی ورزش بیش از حد ⇒ در برخی موارد ورزش بیشتر یعنی آسیب بیشتر. گزینهٔ ۴.")

add(127, "Passage 2 (above)<hr>127- The paragraph preceding this passage most probably discusses ………………. .",
    ["some adverse consequences caused by overtraining",
     "the positive effect of overtraining on the body",
     "pain and heart problem caused by overtraining",
     "the adverse causes of overtraining"],
    "عبارت «In addition to simple pain or sprains which result from overtraining» نشان می‌دهد پاراگراف قبل دربارهٔ همان دردها و پیامدهای سادهٔ تمرین بیش از حد بوده است؛ (گزینهٔ ۳ شامل مشکل قلبی است که در همین متن مطرح شده نه قبل). گزینهٔ ۱.")

add(128, "Passage 2 (above)<hr>128- The author believes that the key issue(s) with regard to the best way to exercise and avoid injury is related to......………………………..",
    ["the time and type of exercise", "appropriateness of exercise",
     "one's understanding of efforts", "intensity and duration of efforts"],
    "«the best way ... revolves around perception of effort» یعنی درک خود فرد از میزان تلاش. گزینهٔ ۳.")

add(129, "Passage 2 (above)<hr>129- It is inferred from the passage that ……………. .",
    ["following hard exercise, you should stop giving your body two days of rest",
     "cases of change in the heart chambers due to overtraining have already been observed",
     "even a simple exercise may be considered vigorous for some individuals",
     "quick walking can be considered tough workout only for old people"],
    "what's \"vigorous\" for one runner is not going to be vigorous for another ⇒ حتی ورزش ساده برای بعضی افراد سنگین است. گزینهٔ ۳. (گزینهٔ ۲ با کلمهٔ theoretically مغایرت دارد.)")

add(130, "Passage 2 (above)<hr>130- By the expression \"those who have not broken a sweat in a while\", the author probably means persons who …………………………………..",
    ["are at an old age", "have failed to do exercise for some time",
     "have done sports professionally", "easily sweat during exercise"],
    "break a sweat = عرق کردن به هنگام ورزش؛ کسانی که مدتیست ورزش نکرده‌اند. گزینهٔ ۲.")

P3H = "Part Two: Reading Comprehension — Passage 3<hr>"
P3 = ("Human nutrition is the science of nutrients and other substances in food in relation to the proper "
"functioning of body systems, organs and tissues. A healthy diet positively supports them, while an "
"unhealthy diet causes deficiency-related diseases (e.g. anemia, scurvy, preterm labor, and stillbirth), or "
"nutrient-excess health-threatening conditions (e.g. obesity) as well as common chronic diseases (e.g. "
"cardiovascular diseases, diabetes, and osteoporosis). To compensate for these shortcomings, claims on "
"Health Food (i.e. food marketed to provide human health effects beyond a normal healthy diet, including "
"natural foods, organic foods, whole foods, vegetarian foods or dietary supplements) have recently been "
"put forward in the form of advertising labels for broccoli sprouts, herbal extracts, medicinal plants, herbal "
"teas, honey, organic foods, certain oils, and traditional cultured milk products. Such labeling is, however, "
"criticized by supervisory and controlling agencies. According to FDA, a relationship between a food, food "
"component, or dietary supplement ingredients, and reducing risk of a disease or health-related condition "
"may be imagined although not supported by scientific evidence. The FDA monitors and warns food "
"manufacturers against foods as having specific health effects when no evidence exists to support such "
"statements.")

add(131, P3H + P3 + "<hr>131- According to the passage, preterm childbirth is claimed to result from ………………. .",
    ["specific health effects", "deficiency-related diseases",
     "nutrient-excess conditions", "chronic systemic diseases"],
    "preterm labor در فهرست deficiency-related diseases آمده است. گزینهٔ ۲.")

add(132, "Passage 3 (above)<hr>132- According to the passage, an unhealthy diet …………………………… .",
    ["compensates for the shortcomings", "results from improper labeling",
     "can lead to chronic systemic diseases", "includes organic food and dietary supplements"],
    "«an unhealthy diet causes ... as well as common chronic diseases». گزینهٔ ۳.")

add(133, "Passage 3 (above)<hr>133- According to the passage, FDA ………………….. a relationship between food and lowered risk of diseases and health conditions.",
    ["contends", "doubts", "conceives", "discards"],
    "«...may be imagined although not supported by scientific evidence» یعنی FDA به این ارتباط تردید دارد. doubts = تردید دارد. گزینهٔ ۲. (contends=ادعا می‌کند، conceives=تصور/درک می‌کند، discards=دور می‌ریزد)")

add(134, "Passage 3 (above)<hr>134- FDA questions ………………. .",
    ["the relationship between health and diet", "dietary supplement ingredients",
     "independently funded research", "improperly labeled foods"],
    "FDA علیه غذاهایی که بدون شواهد علمی با ادعای اثرات سلامتی برچسب‌گذاری شده‌اند هشدار می‌دهد. گزینهٔ ۴.")

add(135, "Passage 3 (above)<hr>135- This passage is mainly written to …………………. .",
    ["define nutritional principles for human beings",
     "suggest new labels for health foods without scientific proof",
     "make consumers aware of the claims lacking scientific evidence",
     "criticize health-threatening conditions"],
    "هدف کلی متن آگاه‌سازی مصرف‌کننده از ادعاهای فاقد سند علمی در برچسب‌های غذای سلامت است. گزینهٔ ۳.")

P4H = "Part Two: Reading Comprehension — Passage 4<hr>"
P4 = ("Studies show that certain styles of interpersonal communication are less effective than others. Which "
"styles are the ones to avoid? These same studies indicate that the two least effective styles are aggressive "
"and passive communication. On the one hand, an aggressive style involves speaking in a disrespectful "
"manner, expressing anger, or trying to dominate the conversation. For example, a business executive "
"might tell her coworker that his ideas for a new product are terrible. Then she might interrupt him when "
"he tries to explain his ideas. This approach hinders successful communication. It also creates barriers "
"between people. A passive communication style, on the other hand, can be equally unproductive. A "
"passive style might lead a person to hide his or her beliefs, speak quietly, and submit to all demands. "
"Someone working on a fashion design project, for instance, might agree to use a fabric that he thinks is "
"unattractive. He would not express his true feelings to the group. In short, ineffective communicators can "
"fail to influence others either by being too forceful or by hiding their opinions.")

add(136, P4H + P4 + "<hr>136- The author of this paragraph is …………………. the communication styles mentioned.",
    ["indifferent to", "in favor of", "impartial to", "critical of"],
    "نویسنده این دو سبک را «least effective» و مانع ارتباط موفق می‌داند پس منتقد آنهاست. critical of = منتقد. گزینهٔ ۴.")

add(137, "Passage 4 (above)<hr>137- When a teacher imposes her ideas on the students, she makes use of ………………. of communication.",
    ["the passive style", "the aggressive style",
     "both the passive and the aggressive styles", "either the passive or the aggressive style"],
    "تحمیل عقاید = تلاش برای تسلط بر گفتگو (dominate the conversation) = سبک تهاجمی. گزینهٔ ۲.")

add(138, "Passage 4 (above)<hr>138- It is implied that an effective communication involves ………………… .",
    ["aggression by both sides", "passiveness by both sides",
     "either passiveness or aggression", "neither passiveness nor aggression"],
    "از «ineffective communicators can fail ... by being too forceful or by hiding their opinions» برمی‌آید که ارتباط مؤثر نه تهاجمی است و نه منفعلانه. گزینهٔ ۴.")

add(139, "Passage 4 (above)<hr>139- People who are ………….. are most probably involved in the passive style of communication.",
    ["introverted", "violent", "assertive", "extroverted"],
    "افراد introverted (درون‌گرا/کم‌حرف) با سبک منفعل (پنهان کردن باورها، آرام صحبت کردن، تسلیم خواسته‌ها شدن) سازگارند. گزینهٔ ۱. (assertive=قاطع، extroverted=برون‌گرا، violent=خشن)")

add(140, "Passage 4 (above)<hr>140- This paragraph is mostly about the ………………………  .",
    ["the barriers between people during communication",
     "unsuccessful communication styles employed by people",
     "appropriate strategies to overcome communication barriers",
     "differences between passive and aggressive people"],
    "متن دربارهٔ دو سبک «کم‌اثرترین» ارتباطی (تهاجمی و منفعل) است. گزینهٔ ۲.")
