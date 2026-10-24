# -*- coding: utf-8 -*-
# 1400 — زبان عمومی (۸۱-۱۲۰) — a: 1-based — کلید نهایی رسمی سنجش (۹۲ = حذف)
from q_ctrl import add, Q

def v(no, q, c, a, s, k=""):
    add(no, "english", q, [f"{l}) {x}" for l, x in zip("abcd", c)], a, s, k)

P = {
1: """Although cholesterol has <u><b>received a lot of bad press</b></u> in recent years, it is a necessary substance in the body. It is found in bile salts needed for digestion of fats, in hormones, and in the cell's plasma membrane. However, high levels of cholesterol in the blood have been associated with atherosclerosis and heart disease. It now appears that the total amount of blood cholesterol is not as important as the form in which it occurs. Cholesterol is transported in the blood in combination with other lipids and with protein, forming compounds called lipoproteins. These compounds are distinguished by their relative density. High-density lipoprotein (HDL) is composed of a high proportion of protein and relatively little cholesterol. HDLs remove cholesterol from the tissues, including the arterial walls, and carry it back to the liver for reuse or disposal. In contrast, low-density lipoprotein (LDL) contains less protein and a higher proportion of cholesterol. LDLs carry cholesterol from the liver to the tissues, making it available for membrane or hormone synthesis. However, excess LDLs can <u><b>deposit</b></u> cholesterol along the lining of the arterial walls. Thus, high levels of HDLs indicate efficient removal of arterial plaques, whereas high levels of LDLs suggest that arteries will become clogged.""",
2: """The Internet greatly influences people's attitudes about their heath and health care. They can search almost any topic of interest and become researchers for their own problems. In the present busy world, doctors do not always take the time to explain illnesses and possible remedies to their patients; they may not give scientific details in simple words, either. Accordingly, many people use Internet resources to find what they need to know for better medical decisions. But are the recommendations of "experts" on the Net always accurate and reliable? Are <u><b>they</b></u> helpful to everyone that needs advice on a specific medical condition? The online health products or information that seem most wonderful are often the most <u><b>fraudulent</b></u>.<br><br>Many specialists have their own theories about illness and health. For example, a California physiologist stated two causes for diseases: (1) pollution of the environment, and (2) parasites inside the human body. She offers two kinds of health products on the Internet: electronic machines and herbal medicine which clean out the body (free it of parasites) and rebuild new healthy living cells. Moreover, there are medical experts who recommend kinds of natural, non-western remedies for modern health disorders. Their advice might include special diet plans with added vitamins and minerals, folk medicine, environmental changes, or unusual therapies that patients do not get from typical doctors.""",
3: """Ultraviolet (UV) radiation covers the wavelength range of 100–400 nm, which is a higher frequency and lower wavelength than visible light. UV radiation comes naturally from the Sun, but it can also be created by artificial sources used in industry, commerce, and recreation. The UV region covers the wavelength range 100-400 nm and is divided into three bands: UVA (315-400 nm), UVB (280-315 nm), and UVC (100-280 nm).<br><br>As sunlight passes through the atmosphere, all UVC and approximately 90% of UVB radiation is absorbed by ozone, water vapor, oxygen and carbon dioxide. UVA radiation is less affected by the atmosphere. Therefore, the UV radiation reaching the Earth's surface is largely composed of UVA with a small UVB component.<br><br>The amount of UV radiation from the Sun that hits the Earth's surface depends on several factors, including the Sun's height in the sky, latitude, cloud cover, altitude, the thickness of the ozone layer and ground reflection. Reductions in the ozone layer due to human-created pollution increase the amount of UVA and UVB that reaches the surface. <u><b>This</b></u> can impact human health, animals, marine organisms and plant life. In humans, increased UV exposure can cause skin cancers, cataracts, and immune system damage.""",
4: """In the summer of 1976, a mysterious epidemic suddenly attacked two central African towns and killed the majority of its victims. Medical researchers suspected the deadly Marburg virus to be the cause, but what they saw in microscope images was entirely a new pathogen which would be named after the nearby Ebola River. Like Yellow fever and Dengue, the disease caused by Ebola virus is a severe type of hemorrhagic fever. It begins by attacking the immune system cells and neutralizing its responses, allowing the virus to multiply. Starting anywhere from 2 to 20 days after contraction, initial symptoms like high temperature, aching, and sore throat resemble those of a typical flu, but quickly increase to vomiting, rashes, and diarrhea, and as the virus spreads, it invades the lymph nodes and vital organs such as the kidney and liver, causing them to lose function. But the virus itself is not what kills Ebola victims. Instead, the mounting cell deaths trigger the immune system overload, known as cytokine storm, an explosion of immune responses that damage blood vessels causing both internal and external bleeding. The excessive fluid loss and resulting complications can be fatal within 6 to 16 days of the first symptoms; however, proper care and rehydration therapy can significantly reduce mortality rates in patients.""",
}

def r(no, pid, q, c, a, s, k=""):
    html = (f'<details style="margin:4px 0 8px"><summary style="cursor:pointer;color:var(--accent,#6366f1)">📄 Passage {pid} (برای نمایش متن کلیک کنید)</summary>'
            f'<div style="font-size:13.5px;line-height:1.9;margin-top:6px;direction:ltr;text-align:left">{P[pid]}</div></details>{q}')
    add(no, "english", html, [f"{l}) {x}" for l, x in zip("abcd", c)], a, s, k)

# ── Part one: Reading Comprehension (Passage 1: Cholesterol) ──
r(81, 1, "<b>81– According to the passage……… .</b>",
  ["different forms of cholesterol in the body have similar features",
   "cholesterol density fails to indicate how healthy an individual is",
   "cholesterol is not so significant in maintaining personal health",
   "the form of cholesterol is more important than its amount"], 4,
  "متن صریحاً می‌گوید: «the total amount of blood cholesterol is not as important as the form in which it occurs» ⇒ شکل کلسترول مهم‌تر از مقدار آن است.",
  "الف با «distinguished» بودن HDL/LDL ناسازگار است؛ ج هم خلاف «necessary substance» است.")

r(82, 1, "<b>82– The phrase \"received a lot of bad press\" in the first line means to ……… .</b>",
  ["be criticized in mass media", "present unwelcome consequences", "include pressure over time", "indicate undesirable effects"], 1,
  "«bad press» اصطلاح رایج است به معنای «انتقاد/پوشش منفی در رسانه‌های جمعی». بقیه ترجمهٔ تحت‌اللفظی کلمه press هستند.",
  "idiom: press = رسانه، نه «فشار».")

r(83, 1, "<b>83– Which of the following statements is TRUE based on the passage?</b>",
  ["Atherosclerosis is associated with HDLs as opposed to LDLs.",
   "Cholesterol is carried in the blood in two forms, namely HDL and LDL.",
   "Thickening of the arterial wall results mainly from high levels of HDLs.",
   "The proportion of cholesterol is higher in HDLs compared with LDLs."], 2,
  "متن: کلسترول در ترکیب با لیپیدها و پروتئین به شکل لیپوپروتئین‌ها با چگالی متفاوت (HDL و LDL) حمل می‌شود ⇒ ب صحیح است. "
  "آترواسکلروز به LDL مربوط است نه HDL (الف غلط)؛ ضخیم شدن دیواره از LDL است (ج غلط)؛ سهم کلسترول در LDL بیشتر است نه HDL (د غلط).")

r(84, 1, "<b>84– The word \"deposit\" in line 11 is closest in meaning to ……… .</b>",
  ["stimulate", "assimilate", "accumulate", "postulate"], 3,
  "deposit در اینجا یعنی «رسوب دادن/انباشتن» = accumulate (انباشته شدن). stimulate: تحریک؛ assimilate: جذب/همسان‌سازی؛ postulate: فرضیه دانستن.")

r(85, 1, "<b>85– According to the passage, ……… is NOT associated with high HDL levels.</b>",
  ["reducing arterial plaques", "clogging arteries with cholesterol", "carrying cholesterol to the liver", "removing cholesterol from the tissues"], 2,
  "HDL کلسترول را از بافت‌ها و دیوارهٔ شریان برداشته و به کبد می‌برد (الف، ج، د مربوط به HDL است). گرفتگی شریان‌ها با کلسترول کارِ LDL است ⇒ پاسخ: ب.",
  "HDL = خوب (پاک‌کننده)؛ LDL = بد (رسوب‌گذار).")

# ── Passage 2: Internet & health ──
r(86, 2, "<b>86– The California physiologist believes that one of the main reasons of diseases is ……… .</b>",
  ["living things in the environment", "parasites in the environment", "environmental pollution", "animals and plants"], 3,
  "متن: دو علت برای بیماری‌ها ذکر کرده: «(1) pollution of the environment, and (2) parasites inside the human body» ⇒ آلودگی محیط‌زیست (گزینهٔ ج). "
  "توجه: انگلی‌های بدن گفته، نه محیط ⇒ ب غلط.")

r(87, 2, "<b>87– The word \"fraudulent\" in paragraph 1 is closest in meaning to ……… .</b>",
  ["available", "dishonest", "significant", "attractive"], 2,
  "fraudulent یعنی «کلاهبردارانه/فریبنده» ≈ dishonest. جمله: محصولات آنلاینی که فوق‌العاده به نظر می‌رسند اغلب فریبنده‌ترین‌اند.")

r(88, 2, "<b>88– It is stated in the passage that a reason for the patients' use of the Internet to know more about their diseases is that ……… .</b>",
  ["they can find information on the Internet which is more culturally appropriate",
   "they can use Internet resources to make the best decision at a reasonable price",
   "doctors use a technical language to explain their problems",
   "doctors fail to take enough time to examine their patients completely"], 3,
  "متن: «doctors do not always take the time to explain illnesses … they may not give scientific details in simple words» ⇒ پزشکان توضیح ساده نمی‌دهند "
  "یعنی از زبان تخصصی استفاده می‌کنند (گزینهٔ ج). گزینهٔ د می‌گوید «معاینهٔ کامل»، اما متن دربارهٔ «توضیح» است نه معاینه.",
  "تله: توضیح (explain) ≠ معاینه (examine).")

r(89, 2, "<b>89– The word \"they\" in paragraph 1 refers to ……… .</b>",
  ["some medical decisions made by the doctors who use the Internet",
   "medical suggestions of the experts on the Internet",
   "some experts on the Internet",
   "the online health products"], 2,
  "جملهٔ قبل: «are the recommendations of experts … always accurate and reliable? Are they helpful …» ⇒ they = همان توصیه‌ها/پیشنهادهای کارشناسان (recommendations).",
  "قانون مرجع ضمیر: nearest plural noun preceding it (recommendations).")

r(90, 2, "<b>90– The medical experts favoring natural remedies suggest all of the following interventions, EXCEPT ……… .</b>",
  ["unconventional therapies", "rebuilding new living cells", "added vitamins and minerals", "changing the patient's place of living"], 2,
  "توصیه‌های کارشناسان طب سنتی/طبیعی: رژیم با ویتامین و مواد معدنی (ج)، طب عامیانه/محیطی شامل تغییر محل سکونت (د)، درمان‌های غیرمعمول (الف). "
  "«ساختن دوبارهٔ سلول‌های زنده (rebuild new healthy living cells)» ادعای محصولات همان فیزیولوژیست کالیفرنیایی است نه این گروه ⇒ پاسخ: ب.",
  "برای EXCEPT، هر گزینه را دقیقاً به جملهٔ متن وصل کنید؛ نه آنچه «کلاً در متن آمده».")

# ── Passage 3: UV ──
r(91, 3, "<b>91– According to the passage, excessive exposure to UV is unlikely to cause ……… .</b>",
  ["cataract", "skin tumors", "immune disorders", "digestive disorders"], 4,
  "متن در پایان: «increased UV exposure can cause skin cancers, cataracts, and immune system damage» ⇒ اختلالات گوارشی ذکر نشده ⇒ پاسخ: د.")

r(92, 3, "<b>92– It is stated in the passage that the visible light ……… the Ultraviolet (UV) radiation.</b>",
  ["falls below the wavelength range of", "falls within the same wavelength as", "has a higher frequency than", "contains all wavelength ranges of"], 1,
  "متن: UV «higher frequency and lower wavelength than visible light» است، پس نور مرئی طول‌موج <b>بلندتر</b> و فرکانس کمتر از UV دارد. "
  "هیچ‌کدام از چهار گزینه همین را نمی‌گوید (الف می‌گوید زیرِ محدودهٔ طول‌موج UV قرار دارد که خلاف است؛ ج فرکانس بالاتر می‌گوید که آن هم خلاف است) — "
  "این سؤال در کلید نهایی سنجش <b>حذف</b> شده است.",
  "")

r(93, 3, "<b>93– Which of the following factors does NOT affect the amount of UV radiation that hits the Earth's surface?</b>",
  ["height above the sea level", "cloud cover of the area", "marine organisms and plant life", "ground reflection of the rays"], 3,
  "عوامل مؤثر طبق متن: ارتفاع خورشید، عرض جغرافیایی، پوشش ابری (ب)، ارتفاع از سطح دریا (الف)، ضخامت لایهٔ اوزون و بازتاب زمین (د). "
  "«موجودات دریایی و حیات گیاهی» از <i>اثرات</i> UV هستند، نه از عوامل مؤثر بر مقدار آن ⇒ پاسخ: ج.")

r(94, 3, "<b>94– It is stated in the passage that the UV radiation which reaches the Earth's surface is mostly composed of ……… .</b>",
  ["UVA with a small UVB component", "UVB and large amounts of UVC", "equal amounts of UVC and UVA", "UVA, UVB and UVC altogether"], 1,
  "متن صریح: «the UV radiation reaching the Earth's surface is largely composed of UVA with a small UVB component» ⇒ الف.")

r(95, 3, "<b>95– The underlined word \"this\" refers to ……… .</b>",
  ["the amount of UV radiation", "Ozone layer", "an increase in the amount of UVA and UVB", "an increase in the amount of human-related pollution"], 3,
  "جملهٔ قبل: «کاهش لایهٔ اوزون… مقدار UVA و UVB رسیده به سطح را افزایش می‌دهد. This can impact…» ⇒ این = افزایش مقدار UVA و UVB ⇒ گزینهٔ ج.")

# ── Passage 4: Ebola ──
r(96, 4, "<b>96– The cytokine storm is ……… .</b>",
  ["a type of external bleeding", "an explosion in the blood vessels", "the consequence of increased cell deaths", "the damage recovered by the immune system"], 3,
  "متن: «the mounting cell deaths trigger the immune system overload, known as cytokine storm» ⇒ توفان سیتوکین نتیجهٔ انباشت مرگ سلول‌هاست ⇒ ج. "
  "(تلهٔ ب: explosion of immune <i>responses</i> است نه explosion آوردن رگ‌ها.)")

r(97, 4, "<b>97– According to this paragraph, Ebola ……… .</b>",
  ["is easily distinguished from the flu in its initial stages", "presents with symptoms like typical flu in the early stages",
   "has symptoms like the typical flu as the disease progresses", "is another name for Dengue, as used in medical context by clinicians"], 2,
  "متن: «initial symptoms … resemble those of a typical flu» ⇒ در مراحل اولیه شبیه آنفلوانزاست ⇒ ب. "
  "(ج غلط چون با پیشرفت بیماری علائم شدیدتر می‌شود و دیگر شبیه آنفلوانزا نیست؛ الف برعکس متن است؛ ابولا با دنگی یکی نیست.)")

r(98, 4, "<b>98– Bleeding in Ebola could be attributed to ……… .</b>",
  ["the fever resembling Dengue and Yellow fever", "deadly Marburg virus as a new pathogen",
   "increased immune system response", "vomiting due to the disease"], 3,
  "متن: توفان سیتوکین «an explosion of immune responses that damage blood vessels causing both internal and external bleeding» ⇒ "
  "خون‌ریزی ناشی از واکنش افراطی سیستم ایمنی است ⇒ ج.")

r(99, 4, "<b>99– The Ebola virus increases through ……… .</b>",
  ["the kidney and liver", "the internal and external bleeding", "counteracting the immune system responses", "invading the lymph nodes and other organs"], 3,
  "متن: «It begins by attacking the immune system cells and neutralizing its responses, allowing the virus to multiply» ⇒ "
  "خنثی‌سازی پاسخ ایمنی ← تکثیر ویروس ⇒ ج. (تله: «حمله به گره‌های لنفی و ارگان‌ها» مال مراحل بعدی گسترش است، نه علت multiply شدن.)")

r(100, 4, "<b>100– The death rate following Ebola disease ……… .</b>",
  ["is definitely predictable depending on the affected area", "is highly increased in the first few days of contraction",
   "fails to be controlled under the current circumstances", "could be controlled through proper care and therapy"], 4,
  "متن: «proper care and rehydration therapy can significantly reduce mortality rates in patients» ⇒ نرخ مرگ با مراقبت مناسب قابل کاهش است ⇒ د.")

# ── Part two: Vocabulary (۱۰۱-۱۲۰) ──
v(101, "<b>101– Health problems of the poor people can only be ……… through proper strategies and measures taken by the government.</b>",
  ["exaggerated", "enhanced", "complicated", "alleviated"], 4,
  "alleviate = کاهش/تخفیف درد یا مشکل. exaggerated: اغراق‌آمیز؛ enhanced: افزایش‌یافته؛ complicated: پیچیده. «مشکلات سلامت فقرا فقط … می‌شود» ⇒ alleviated.")

v(102, "<b>102– Regular sleep, eating patterns, and exercise help people ……… the bad effects of stress.</b>",
  ["intensify", "counteract", "prolong", "imitate"], 2,
  "counteract = خنثی کردن/مقابله با اثر. intensify: تشدید؛ prolong: طولانی کردن؛ imitate: تقلید.")

v(103, "<b>103– In order not to involve your personal attitudes in the results, you need to be ……… when doing research.</b>",
  ["disoriented", "ignorant", "impartial", "biased"], 3,
  "impartial = بی‌طرف. disoriented: سردرگم؛ ignorant: نادان؛ biased: جانب‌دار (دقیقاً برعکس).")

v(104, "<b>104– University lecturers have the main role in ……… knowledge in all fields to the students.</b>",
  ["imparting", "announcing", "degrading", "consuming"], 1,
  "impart knowledge = انتقال دانش. announce: اعلام؛ degrade: تنزل دادن؛ consume: مصرف کردن.")

v(105, "<b>105– Although scientists have detected many secrets of the central nervous system, there are still some ……… points which need to be clarified.</b>",
  ["transparent", "obvious", "evident", "obscure"], 4,
  "اولیه‌گر؟ need to be clarified ⇒ نقاط «مبهم» (obscure). سه گزینهٔ دیگر = روشن/آشکار.",
  "Although ⇒ نقیض؛ clarified را با مبهم جفت کنید.")

v(106, "<b>106– While taking your exam, you need to block ……… thoughts by concentrating on what you are doing.</b>",
  ["constructive", "intrusive", "supportive", "inspiring"], 2,
  "intrusive thoughts = افکار مزاحم/به‌زور هجوم‌آورنده. constructive: سازنده؛ supportive: حمایتی؛ inspiring: الهام‌بخش.")

v(107, "<b>107– He was not able to cope with the stress and ……… of his job; therefore, he decided to retire.</b>",
  ["comfort", "recreation", "strain", "tranquility"], 3,
  "هم‌نشینی با stress و بازنشستگی ⇒ «فشار/زحمت» = strain. comfort: آسایش؛ recreation: تفریح؛ tranquility: آرامش — هر سه مثبت‌اند و کنار stress نمی‌نشینند.",
  "and ⇒ همدستهٔ معنایی (stress and strain ترکیب رایج است).")

v(108, "<b>108– The health authorities have emphasized that priority should be given to the ……… which help the improvement of health in the country.</b>",
  ["initiatives", "compartments", "obstacles", "redundancies"], 1,
  "initiatives = ابتکارها/برنامه‌های آغازین. compartments: محفظه‌ها؛ obstacles: موانع؛ redundancies: اضافات/خروج‌های اضافی. «کمک به بهبود سلامت» ⇒ initiatives.")

v(109, "<b>109– Some people think that the most essential ……… for good managers is their organizational abilities.</b>",
  ["associate", "complication", "repression", "attribute"], 4,
  "attribute = ویژگی/صفت. associate: همکار (اسم)/منتسب کردن؛ complication: عارضه؛ repression: سرکوب.")

v(110, "<b>110– Some bacteria are not responsive to antibiotic therapy because they have gradually developed ……… to antibiotics.</b>",
  ["existence", "assistance", "resistance", "prevalence"], 3,
  "resistance to antibiotics = مقاومت به آنتی‌بیوتیک. existence: وجود؛ assistance: کمک؛ prevalence: شیوع.")

v(111, "<b>111– The lecturer was asked to steer the discussion back to the ……… topic of main importance by avoiding unrelated issues.</b>",
  ["superficial", "original", "trivial", "redundant"], 2,
  "original = اصلی/اصالت‌دار: بازگرداندن بحث به موضوع «اصلی» مهم. superficial: سطحی؛ trivial: جزئی؛ redundant: تکراری — با «main importance» نمی‌سازند.")

v(112, "<b>112– The health providers are forced to answer any ……… the patients have about their treatment.</b>",
  ["queries", "intimacies", "contributions", "modifications"], 1,
  "queries = سؤال‌ها/پرسش‌ها. intimacies: صمیمیت‌ها؛ contributions: مشارکت‌ها؛ modifications: تغییرات. «پاسخ به … بیماران» ⇒ queries.")

v(113, "<b>113– The student received a lot of ……… comments from his supervisor helping him improve the quality of his work.</b>",
  ["disruptive", "constructive", "disappointing", "debilitating"], 2,
  "constructive comments = نظرات سازنده (helping him improve). disruptive: مخل؛ disappointing: ناامیدکننده؛ debilitating: تضعیف‌کننده.")

v(114, "<b>114– The instructor advised students to avoid ……… by strictly following note-taking standards.</b>",
  ["frankness", "truthfulness", "plagiarism", "precision"], 3,
  "با رعایت استانداردهای یادداشت‌برداری و ارجاع ⇒ اجتناب از «سرقت ادبی» (plagiarism). frankness: صراحت؛ truthfulness: راستگویی؛ precision: دقت.")

v(115, "<b>115– The Corona virus is a dangerous, highly ……… viral infection that can easily spread to other people.</b>",
  ["transmissible", "dismissible", "ignorable", "valuable"], 1,
  "transmissible = قابل انتقال/واگیر (spread to other people). dismissible: قابل چشم‌پوشی؛ ignorable: قابل نادیده‌گرفتن؛ valuable: ارزشمند.")

v(116, "<b>116– Numerous theories have been ……… on the exact cause of Corona virus which is yet to be identified.</b>",
  ["abandoned", "avoided", "proposed", "oppressed"], 3,
  "propose theories = نظریه ارائه کردن. abandoned: رهاشده؛ avoided: اجتناب‌شده؛ oppressed: تحت‌ستم.")

v(117, "<b>117– Prevention rather than treatment must be the first ……… of all those involved in health.</b>",
  ["census", "concern", "burden", "invention"], 2,
  "concern = دغدغه/اولویت اصلی. census: سرشماری؛ burden: بار/فشار؛ invention: اختراع. «پیشگیری باید اولین … همکاران سلامت باشد» ⇒ concern.")

v(118, "<b>118– With simple ……… measures, the side effects of the lesions under the skin can be reduced.</b>",
  ["threatening", "destructive", "preventive", "obsessive"], 3,
  "preventive measures = اقدامات پیشگیرانه. threatening: تهدیدآمیز؛ destructive: مخرب؛ obsessive: وسواس‌گونه.")

v(119, "<b>119– A damaging decline in blood products can cause huge ……… when caring for pregnant women with pre-existing medical conditions.</b>",
  ["contributions", "profits", "opportunities", "challenges"], 4,
  "کاهش محصولات خونی در مراقبت از زنان باردار ⇒ «چالش‌های» بزرگ (challenges). سه گزینهٔ دیگر مثبت/نامرتبط‌اند.")

v(120, "<b>120– We can keep away from infectious diseases by enhancing our ……… disease-causing microorganisms.</b>",
  ["resistance to", "assistance to", "combination of", "contraction of"], 1,
  "resistance to = مقاومت در برابر. assistance to: کمک به؛ combination of: ترکیبی از؛ contraction of: ابتلا/انقباضِ. «تقویت مقاومت در برابر میکروب‌ها» ⇒ الف.")
