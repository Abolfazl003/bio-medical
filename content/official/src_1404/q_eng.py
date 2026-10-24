# -*- coding: utf-8 -*-
# 1404 — زبان عمومی (۸۸-۱۲۰) — a: 1-based — کلید نهایی رسمی سنجش
# متن از لایه متنی دفترچهٔ «سوالات ارشد مهندسی پزشکی بیوالکتریک ۱۴۰۴» استخراج شده است.
Q = []
def add(no, sid, q, c, a, s, k="", tips="", img=None):
    Q.append(dict(no=no, sid=sid, q=q, c=c, a=a, s=s, k=k, tips=tips, img=img))

def v(no, q, c, a, s, k="", tips=""):
    add(no, "english", q, c, a, s, k, tips)

P = {
1: """Immunization efforts are under growing threat as misinformation, population growth, humanitarian crises and funding cuts jeopardize progress and leave millions of children, adolescents and adults at risk, warn WHO, UNICEF, and Gavi. Outbreaks of vaccine-preventable diseases such as measles, meningitis and yellow fever are rising globally, and diseases like diphtheria, which have long been held at bay or virtually disappeared in many countries, are at risk of re-emerging. In response, the agencies are calling for urgent and sustained political attention and investment to strengthen immunization programs and protect significant progress achieved in reducing child mortality over the past 50 years. Measles is making an especially dangerous comeback. The increasing number of cases since 2021 result from the reductions in immunization coverage that occurred since the COVID-19 pandemic in many communities. Measles cases reached an estimated 10.3 million in 2023, a 20% increase compared to 2022. Meningitis cases in Africa also rose sharply in 2024, and the upward trend has continued into 2025. In the first three months of this year alone, more than 5500 suspected cases and nearly 300 deaths were reported in 22 countries. This follows approximately 26000 cases and almost 1400 deaths across 24 countries last year. As part of integrated primary health-care systems, vaccination can protect against diseases and connect families to other essential care, such as antenatal care, nutrition or malaria screening. Immunization is a 'best buy' in health with a return on investment of $54 for every dollar invested and provides a foundation for future prosperity and health security. UNICEF, WHO, and Gavi urgently call for parents, the public, and politicians to strengthen support for immunization.""",
2: """Caring for the elderly presents several important challenges that affect families, healthcare systems, and society as a whole. Many older adults suffer from chronic health conditions such as arthritis, diabetes, high blood pressure, and dementia, all of which require regular monitoring, medication, and personal care. These conditions often limit mobility and independence, making daily tasks like bathing, cooking, or even walking difficult. Unfortunately, there is often a shortage of trained caregivers, and many family members are unprepared to manage these responsibilities. Providing care without proper training can lead to mistakes, emotional stress, and burnout. In addition to physical health, emotional and social needs must also be addressed. Elderly individuals frequently face loneliness and depression, especially if they live alone, have lost friends or a spouse, or feel disconnected from society. These feelings can negatively affect both mental and physical health. Financial challenges also make elderly care more complicated. Long-term care can be expensive, and not all families have access to quality insurance or government support. Many must choose between affordability and the level of care needed. Another key issue is respecting the dignity and independence of elderly individuals. While they may need help, it is important to involve them in decisions about their lives and health whenever possible. Balancing safety with personal freedom requires sensitivity and respect. These various challenges highlight the growing need for stronger support systems, more caregiver training, better public awareness, and affordable services to meet the complex and changing needs of the aging population.""",
3: """The ubiquity of microplastics, tiny plastic fragments less than 5 mm in diameter, has triggered global concern, particularly regarding their potential impact on human health. Detected in food, water, and even the air we breathe, these particles have been found in human tissues, from lungs to placentas. But what does this mean for our well-being? Some researchers warn that microplastics may act as carriers for harmful substances, such as heavy metals or persistent organic pollutants. Once inside the body, these chemicals could disrupt hormonal balance or contribute to chronic inflammation. Although alarming, much of the current evidence comes from animal studies or controlled lab settings, making it difficult to determine actual effects in human populations. On the other hand, skeptics argue that the level of exposure most people face is relatively low, and that media-driven fears often outpace scientific findings. They emphasize the absence of definitive proof linking microplastics to specific health disorders. Furthermore, they caution against drawing strong conclusions from early-stage research, suggesting that public anxiety might be premature. Nevertheless, both sides agree on the necessity of further investigation. With plastic production still increasing worldwide, understanding the long-term implications of microplastic exposure remains a pressing issue. Whether the threat proves to be serious or overstated, the debate highlights a broader question: how much environmental contamination are we willing to tolerate before taking action?""",
4: """Telehealth has emerged as a promising solution for increasing access to medical care in rural and underserved communities. Through video consultations, remote monitoring, and digital diagnostics, patients in isolated areas can now connect with specialists who would otherwise be hundreds of miles away. Supporters argue that telehealth reduces barriers, cuts travel costs, and saves critical time—especially in emergencies or for those with chronic conditions. Yet, while the technology has clear advantages, it's not without limitations. Skeptics point to the digital divide: the lack of high-speed internet, limited digital literacy, and unreliable infrastructure in some communities make telehealth difficult, if not impossible, to implement equitably. Moreover, some healthcare providers warn that telehealth cannot fully replace in-person visits, particularly for physical exams or complex diagnoses. Still, others argue that dismissing telehealth because of these challenges overlooks its transformative potential. They advocate for investment in digital infrastructure, training, and policy reforms to bridge these gaps, seeing telehealth not as a replacement, but as a complement to traditional care. As digital solutions continue to evolve, it is likely that telehealth will become an increasingly integral part of healthcare delivery—especially for populations historically left behind by conventional systems. If addressed thoughtfully, today's limitations may eventually give way to a more connected and equitable model of care.""",
}

def r(no, pid, q, c, a, s, k="", tips=""):
    html = (f'<details style="margin:4px 0 8px"><summary style="cursor:pointer;color:var(--accent,#6366f1)">📄 Passage {pid} (برای نمایش متن کلیک کنید)</summary>'
            f'<div style="font-size:13.5px;line-height:1.9;margin-top:6px;direction:ltr;text-align:left">{P[pid]}</div></details>{q}')
    add(no, "english", html, c, a, s, k, tips)

# ── توضیح اصلاح‌شدهٔ سه واژهٔ ۸۸-۹۰ (پاسخ قدیمی با کلید نهایی نمی‌خواند) ──
v(88, "To provide better vaccination coverage, public health centers must actively ………………. volunteers to assist with community outreach programs.",
  ["revoke", "resist", "recruit", "resign"], 3,
  "recruit = استخدام/جذب نیرو: «مراکز بهداشت عمومی باید فعالانه داوطلب جذب کنند». revoke: لغو؛ resist: مقاومت؛ resign: استعفا.",
  "", "collocation رایج: recruit volunteers/staff.")

v(89, "Patients who experience a ………………. rise in blood pressure after surgery usually recover without the need for long-term medication.",
  ["permanent", "transient", "consistent", "durable"], 2,
  "transient = گذرا/موقت: افزایش «موقت» فشار خون بعد از عمل بدون نیاز به درمان بلندمدت خوب می‌شود. "
  "permanent: دائمی؛ consistent: پایدار/سازگار؛ durable: بادوام — «بدون نیاز به داروی بلندمدت» با دائمی نمی‌سازد.",
  "Transient Ischemic Attack را بشناسید: transient = گذرا.")

v(90, "Rigorous ………………. standards in public facilities are vital for reducing pathogen transmission.",
  ["hygiene", "aesthetics", "speculation", "exhibition"], 1,
  "hygiene = بهداشت: استانداردهای بهداشتی ← کاهش انتقال پاتوژن. aesthetics: زیبایی‌شناسی؛ speculation: حدس و گمان؛ exhibition: نمایشگاه.")

# ── Part one: Vocabulary (۹۱-۱۰۰) ──
v(91, "Improving ………………. through fitness training under the supervision of a personal trainer improves stamina in athletes.",
  ["clarity", "vitality", "initiation", "collaboration"], 2,
  "vitality = سرزندگی/نشاط: بهبود سرزندگی با تمرین‌های آمادگی ← استقامت بهتر ورزشکاران. clarity: شفافیت؛ initiation: آغاز/مراسم پذیرش؛ collaboration: همکاری.")

v(92, "Reducing muscle ………………. caused by work pressure and repetitive tasks prevent joint injuries.",
  ["frustration", "depression", "strain", "integrity"], 3,
  "strain = رگ به رگ/کشیدگی عضلانی (muscle strain). frustration: سرخوردگی؛ depression: افسردگی؛ integrity: درستی/سلامت — «فشار کاری و کارهای تکراری» باعث strain عضله و آسیب مفصل می‌شود.",
  "", "collocation پزشکی کلاسیک: muscle strain.")

v(93, "The latest research findings may ………………. several environmental factors in the development of cardiovascular diseases, suggesting that soil pollution plays a significant role.",
  ["exclude", "dismiss", "ignore", "implicate"], 4,
  "implicate = درگیر دانستن/نقش‌داشتن عامل در یک پیامد: یافته‌های جدید عوامل محیطی را در بیماری‌های قلبی «دخیل» می‌داند. "
  "exclude: حذف کردن؛ dismiss: رد کردن؛ ignore: نادیده گرفتن — هر سه برعکس جهت جمله‌اند (with suggesting that soil pollution plays a role).")

v(94, "The Nobel Prize Committee appreciated her inspiring ………………. immunotherapy.",
  ["contribution to", "opposition to", "negligence of", "suspicion of"], 1,
  "contribution to = سهم/مشارکت در: کمیته نوبل از مشارکت الهام‌بخش او در ایمنی‌درمانی قدردانی کرد. "
  "opposition to: مخالفت با؛ negligence of: سهل‌انگاری؛ suspicion of: بدگمانی — با appreciated نمی‌سازند.")

v(95, "After reviewing the patient's symptoms, the doctor wrote a detailed ………………. specifying the exact dosage and frequency of the drugs to be taken.",
  ["permission", "procedure", "prescription", "preparation"], 3,
  "prescription = نسخه: پزشک «نسخهٔ» مفصلی با دوز و تناوب دارو نوشت. permission: اجازه؛ procedure: روش/روند؛ preparation: آماده‌سازی/فرآوره.",
  "", "دقت به اسم «write» پزشک: write a prescription.")

v(96, "Since he needed to focus on his full-time research project, he ………………. his routine healthcare responsibilities.",
  ["stipulated", "invaded", "postulated", "evaded"], 4,
  "evade = شانه خالی کردن/دوری کردن: چون می‌خواست روی پروژهٔ پژوهشی تمرکز کند، از مسئولیت‌های روتین بهداشتی‌اش «دوری» کرد. "
  "stipulate: مقرر/شرط کردن؛ invade: تهاجم؛ postulate: به‌صورت بدیهی فرض کردن.")

v(97, "The hospital manager detected the ………………. of patients' records and immediately fired the person in charge.",
  ["fabrication", "indexation", "tabulation", "registration"], 1,
  "fabrication = جعل/ساختگی: مدیر جعل پرونده‌های بیماران را کشف و مسئول را اخراج کرد. "
  "indexation: نمایه‌سازی؛ tabulation: جدول‌بندی؛ registration: ثبت‌نام — هیچ‌کدام دلیل اخراج نیست.",
  "", "fabricate = جعل کردن؛ مانند fabricate evidence/data.")

v(98, "One third of children and adolescents are overweight or obese, yet food and beverage companies continue to ………………. them into consuming products causing obesity crisis.",
  ["explore", "prohibit", "entice", "suppress"], 3,
  "entice (into doing) = وسوسه کردن به انجام: شرکت‌های غذا و نوشیدنی کودکان را به مصرف محصولات چاقی‌زا «وسوسه» می‌کنند. "
  "explore: کاوش؛ prohibit: ممنوع کردن؛ suppress: سرکوب کردن — با بحران چاقی در کنار yet نمی‌سازند.",
  "", "ساختار: entice someone into doing something.")

v(99, "She often loses her temper even over ………………. matters; this might be due to emotional trauma she experienced due to her husband's death.",
  ["terminal", "curable", "ethical", "trivial"], 4,
  "trivial = پیش‌پاافتاده/جزئی: حتی سر مسائل «کوچک» هم داد می‌زند — با even و آسیب عاطفی می‌سازد. "
  "terminal: مرحلهٔ نهایی/کشنده؛ curable: قابل‌درمان؛ ethical: اخلاقی.")

v(100, "Whether waves produced and received by mobile phones are dangerous to health still remains a/an ………………. issue; some believe in the danger, but others see no harm.",
  ["conventional", "controversial", "reputable", "explicable"], 2,
  "controversial = بحث‌برانگیز: بعضی خطرناک می‌دانند و بعضی نه ⇒ مسئلهٔ بحث‌برانگیز. "
  "conventional: قراردادی/سنتی؛ reputable: معتبر؛ explicable: قابل توضیح.")

# ── Part two: Reading Comprehension ──
# Passage 1: Immunization (101-105)
r(101, 1, "<b>101– What is the primary concern expressed by WHO, UNICEF, and Gavi during World Immunization Week?</b>",
  ["Increased public interest in vaccine-preventable diseases",
   "The need to develop new vaccines for emerging diseases",
   "The rising threat to immunization progress due to various global challenges",
   "A shortage of vaccine investment and policy attention in developing countries"], 3,
  "جملهٔ اول متن: تلاش‌های واکسیناسیون «under growing threat» بر اثر اطلاعات نادرست، رشد جمعیت، بحران‌های بشردوستانه و کاهش بودجه است ⇒ نگرانی اصلی = تهدید رو به رشد پیشرفت ایمنی‌سازی به سبب چالش‌های جهانی.",
  "الف جهت معکوس است؛ ب در متن نیامده؛ د محدود به «کشورهای در حال توسعه» است که متن نگفته.")

r(102, 1, "<b>102– According to the passage, which disease has shown a particularly dangerous return since 2021?</b>",
  ["Measles", "Meningitis", "Diphtheria", "Yellow fever"], 1,
  "متن: «Measles is making an especially dangerous comeback. The increasing number of cases since 2021 …» ⇒ سرخک (Measles).",
  "Diphtheria «در معرض برگشت» است نه برگشته؛ مننژیت و تب زرد هم فقط مرور شده‌اند.")

r(103, 1, "<b>103– The economic argument in favor of investing in immunization maintains that it ………………..</b>",
  ["reduces the need for international aid",
   "offers a significant return on investment",
   "triples the investment within two years",
   "helps lower educational costs globally"], 2,
  "متن: «a 'best buy' in health with a return on investment of $54 for every dollar invested» ⇒ بازده سرمایه‌گذاری چشمگیر (هر ۱ دلار، ۵۴ دلار).")

r(104, 1, "<b>104– It can be inferred about the impact of the COVID-19 pandemic on immunization coverage that ………………..</b>",
  ["it had no noticeable effect on vaccination rates",
   "it led to improvements in immunization tracking methods",
   "it eliminated the need for traditional vaccination programs",
   "it caused cuts in immunization coverage, increasing disease outbreaks"], 4,
  "متن: افزایش موارد سرخک از ۲۰۲۱ «result from the reduction in immunization coverage that occurred since the COVID-19 pandemic» ⇒ کووید پوشش واکسیناسیون را کاهش داد و شیوع بیماری‌ها را زیاد کرد ⇒ د.")

r(105, 1, "<b>105– In the sentence \"This follows approximately 26000 cases and almost 1400 deaths across 24 countries last year,\" \"This\" refers to ………………..</b>",
  ["The spread of yellow fever in 2024",
   "The rise in meningitis cases in 2025",
   "The increase in measles cases since 2021",
   "The number of humanitarian crises globally"], 2,
  "جمله در متن بلافاصله بعد از موارد مننژیت آمده: «… more than 5500 suspected cases … in 22 countries. This follows approximately 26000 cases …». "
  "This به همان بحث مننژیت (افزایش موارد آن در ۲۰۲۵) برمی‌گردد: سال گذشته نیز ۲۶۰۰۰ مورد گزارش شده بود ⇒ ب.",
  "referent معمولاً همان موضوعِ در حال بحث جمله‌های قبلی است (مننژیت، نه سرخک که دو پاراگراف قبل است).")

# Passage 2: Elderly care (106-110)
r(106, 2, "<b>106– The author highlights various challenges of elderly care to ……………….</b>",
  ["criticize current caregiving quality and practices",
   "discourage families from providing care at home",
   "advocate for systemic improvements and increased support",
   "argue for reducing government involvement in elderly care"], 3,
  "جملهٔ پایانی: این چالش‌ها «highlight the growing need for stronger support systems, more caregiver training, better public awareness, and affordable services» ⇒ هدف نویسنده = حمایت از بهبود نظام‌مند و افزایش حمایت‌ها.",
  "هدف معمولاً در جملهٔ پایانی متن مسئله‌محور است.")

r(107, 2, "<b>107– It appears that ………………. has/have a domino effect on other aspects of elderly care.</b>",
  ["economic obstacles", "chronic health conditions", "independence of elderly conditions", "the need for personal independence"], 1,
  "طبق متن، چالش‌های مالی (هزینهٔ بالای مراقبت طولانی‌مدت و نبود بیمهٔ خوب یا حمایت دولتی) کار را «more complicated» می‌کند و خانواده‌ها را در انتحاب بين «affordability و سطح مراقبت» می‌گذارد؛ "
  "یعنی مانع اقتصادی بر همهٔ جنبه‌های دیگر مراقبت اثر زنجیره‌ای (دومینو) می‌گذارد ⇒ الف.",
  "پاسخ رسمی سنجش = موانع اقتصادی.")

r(108, 2, "<b>108– According to this passage, family caregivers experience burnout because they ……………….</b>",
  ["are unwilling to care for aging relatives",
   "prefer institutional care over home care",
   "often lack the training needed for the caregiving role",
   "receive much assistance from professional caregivers"], 3,
  "متن: «many family members are unprepared to manage these responsibilities. Providing care without proper training can lead to mistakes, emotional stress, and burnout» ⇒ فرسودگی به سبب نبود آموزش کافی ⇒ ج.")

r(109, 2, "<b>109– Involving elderly individuals in decision-making is emphasized in the text ……………….</b>",
  ["to reduce the workload of caregivers",
   "to maintain their sense of respect and autonomy",
   "because they often disagree with medical advice",
   "so that they can avoid moving into care centers"], 2,
  "متن صریح: «respecting the dignity and independence … it is important to involve them in decisions about their lives and health» ⇒ حفظ احساس احترام و استقلال ⇒ ب.")

r(110, 2, "<b>110– As to the relationship between physical and emotional health in the elderly, it can be inferred that ……………….</b>",
  ["physical health gets worsened before emotional health in aging individuals",
   "physical and emotional health are independent challenges in elderly care",
   "addressing physical health automatically resolves emotional issues",
   "emotional well-being can impact physical health in older adults"], 4,
  "متن: «These feelings can negatively affect both mental and physical health» ⇒ سلامت عاطفی بر سلامت جسمی سالمندان اثر می‌گذارد ⇒ د. "
  "بقیه: ب (مستقل‌اند) با «addressed با هم» ناسازگار؛ ج با negatively affect تناقض دارد.")

# Passage 3: Microplastics (111-115)
r(111, 3, "<b>111– The most suitable title for this passage would be “Microplastics and ……………….</b>",
  ["the History of Synthetic Materials", "the Debate Over Their Health Risks", "the Global Demand for Their Restrictions", "the Discovery of a Medical Breakthrough"], 2,
  "کل متن یک بحث دوجانبه است: پژوهشگران نگران در برابر شکاکان، و توافق بر نیاز به تحقیق بیشتر ⇒ «جدل بر سر خطرات سلامتی» بهترین عنوان است.")

r(112, 3, "<b>112– According to the passage, one reason some scientists hesitate to raise alarms about microplastics is the current lack of ………………. in human-based research.</b>",
  ["public tendency", "political interest", "financial support", "definitive evidence"], 4,
  "متن: شکاکان «emphasize the absence of definitive proof linking microplastics to specific health disorders» و اینکه بیشتر شواهد از حیوانات و لابراتوآر است ⇒ کمبود «شواهد قطعی» در انسان ⇒ د.")

r(113, 3, "<b>113– The phrase “media-driven fears often outpace scientific findings” implies that the public's concern about microplastics may be based more on ………………. than on conclusive data.</b>",
  ["reliable evidence", "government research", "public health initiatives", "news exaggeration"], 4,
  "ترس هدایت‌شدهٔ رسانه‌ای از یافته‌های علمی جلوتر می‌زند ⇒ نگرانی عمومی بیشتر بر پایهٔ «اغراق خبری» است تا دادهٔ قطعی ⇒ د.")

r(114, 3, "<b>114– The author's tone throughout the passage can best be described as ………………. showing concern without fully endorsing either side.</b>",
  ["biased and emotional", "dismissive and sarcastic", "precautious and balanced", "indifferent and detached"], 3,
  "نویسنده هر دو سمت را منصفانه می‌آورد («Some researchers warn …» / «On the other hand, skeptics argue …» / «both sides agree …») و بدون طرفداری کامل نگرانی مطرح می‌کند ⇒ محتاطانه و متعادل ⇒ ج.")

r(115, 3, "<b>115– It can be inferred that the author includes the final question in order to emphasize society's ………………. toward environmental contamination.</b>",
  ["dependence", "endurance", "ignorance", "rejection"], 2,
  "سؤال پایانی: «how much environmental contamination are we willing to tolerate before taking action?» ⇒ تأکید بر «تحمل/برداشت» جامعه در برابر آلودگی محیطی ⇒ endurance (تحمل) = ب.",
  "tolerate ≈ endure: به دنبال مترادف مفهومی در گزینه‌ها بگردید.")

# Passage 4: Telehealth (116-120)
r(116, 4, "<b>116– According to the passage, one reason telehealth can be ineffective in some communities is the lack of ……………….</b>",
  ["reliable internet access", "hospital infrastructure", "private digital plans", "healthcare facility"], 1,
  "متن دربارهٔ digital divide: «the lack of high-speed internet, limited digital literacy, and unreliable infrastructure» ⇒ نبود اینترنت پرسرعت/قابل اعتماد ⇒ الف.")

r(117, 4, "<b>117– The phrase “digital divide” most probably refers to ………………. .</b>",
  ["variety in employment opportunities",
   "personalized patient treatment plans",
   "difficulty in implementing health policies equitably",
   "insufficiency of online access and technological skills"], 4,
  "تعریف در همان جملهٔ بعد از دونقطه: نبود اینترنت پرسرعت + سواد دیجیتال محدود ⇒ ناکافی بودن دسترسی آنلاین و مهارت‌های فناورانه ⇒ د.")

r(118, 4, "<b>118– It can be inferred that advocates of telehealth view it as ………………..</b>",
  ["an unsafe shift in medical practice",
   "a complete substitute for traditional care",
   "a useful addition to in-person healthcare",
   "a short-term solution with little long-term value"], 3,
  "متن: حامیان telehealth را «not as a replacement, but as a complement to traditional care» می‌دانند ⇒ مکمل مفید مراقبت حضوری ⇒ ج.")

r(119, 4, "<b>119– The conclusion of the passage predicts that telehealth will likely ………………. in future models of healthcare delivery.</b>",
  ["disappear as in-person care improves",
   "become more central and widespread",
   "be replaced by newer, non-digital systems",
   "remain critical for underserved communities"], 2,
  "متن: «telehealth will become an increasingly integral part of healthcare delivery» ⇒ مرکزی‌تر و فراگیرتر می‌شود ⇒ ب. "
  "(گزینهٔ د دربارهٔ «future models پرسیده نشده نیست؟ متن می‌گوید integral می‌شود برای همه و نه فقط underserved ⇒ ب قوی‌تر است.)")

r(120, 4, "<b>120– One of the concerns raised by critics is that telehealth might ………………. in diagnosing complex medical issues.</b>",
  ["fall short", "lower wait times", "continue to evolve", "overlook digital infrastructures"], 1,
  "متن: ارائه‌دهندگان هشدار می‌دهند telehealth «cannot fully replace in-person visits, particularly for physical exams or complex diagnoses» ⇒ در تشخیص مسائل پیچیده «کم می‌آورد» (fall short) ⇒ الف.",
  "", "fall short = کم آوردن/کافی نبودن — عبارت رایج کنکوری.")
