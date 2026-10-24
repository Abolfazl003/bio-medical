# -*- coding: utf-8 -*-
# 1402 — زبان عمومی (۸۱-۱۲۰) — کلید رسمی ندارد ⇒ پاسخ‌ها «حل مؤلف»
from q_math import add, Q

def v(no, q, c, a, s, k=""):
    add(no, "english", q, [f"{l}) {x}" for l, x in zip("abcd", c)], a, s, k)

P = {
1: """We are all looking for that sweet spot when it comes to fitness, that ephemeral balance between working out too much and not working out enough. Finding <u><b>it</b></u> can be tricky. Some people wonder if it is bad to exercise daily. The answer is yes and no, it depends on how you define working out. It is generally advisable to <u><b>move</b></u> every single day. When we move our bodies, oxygen and nutrients are delivered to tissues and the cardiovascular system works more efficiently during daily tasks. But moving every day does not necessarily mean "working out". What daily movement looks like for each person will, and should, vary.<br><br>If you are concerned whether you need to do a sweat-inducing workout every single day, then the answer is no. People are often intimidated by committing to a healthy lifestyle because they think that means intense exercise every day, but your workout plan may also include 20 minutes of walking, stretching, foam rolling or gentle yoga. In fact, at the maximum, it is recommended to do strength training three times a week for 30 minutes and cardio exercise five days a week for 30 minutes. Of course, if you are an athlete or training for a race, your workout schedule may be more intense than this.""",
2: """Vaccination is considered the most successful and valuable medical intervention ever introduced. The <u><b>bitter truth</b></u>, however, is that although vaccines keep people healthy and save money, fewer and fewer pharmaceutical companies invest in the development of new vaccines. Rather, their investment dollars are channeled disproportionately to new drug therapies in areas such as oncology, immunology, inflammation, and cardiovascular, metabolic, and neurodegenerative diseases, for which the return on investment tends to be higher and more predictable than for vaccines. How did we end up in this situation, in which the allocation of resources is increasingly skewed against vaccines? The problem lies partly in the cost-effectiveness approach, which typically accounts for averted medical care costs and loss of parental work time to care for sick children, and not the full benefits of health to such items as lifetime income and wealth accumulation, and its economic spillover effects on the broader society. However, understanding the value of vaccines to our society and taking this value properly into account in the allocation of resources to vaccine development are both essential to realizing the continuing contribution vaccines can make to human well-being and progress.""",
3: """The monkeypox virus is an orthopoxvirus that causes mpox (monkeypox), a disease with symptoms similar to smallpox, although less severe. While smallpox was eradicated in 1980, mpox continues to occur in countries of Central and West Africa. Since May 2022, cases have also been reported from countries without previously documented mpox transmission outside the African region. Two distinct clades of the monkeypox virus have been identified: Clade I (previously known as the Congo Basin (central African) clade and Clade II (the former West African clade). Mpox is a zoonosis, a disease that is transmitted from animals to humans, with cases often found close to tropical rainforests where there are animals that carry the virus. Evidence of monkeypox virus infection has been found in animals including squirrels, Gambian pouched rats, dormice, different species of monkeys and others. The disease can also spread from humans to humans. It can be transmitted through contact with bodily fluids, lesions on the skin or on internal mucosal surfaces, such as in the mouth or throat, respiratory droplets and contaminated objects. Detection of viral DNA by polymerase chain reaction (PCR) is the preferred laboratory test for mpox. The best diagnostic specimens are taken directly from the rash – skin, fluid or crusts, or biopsy where feasible. Antigen and antibody detection methods may not be useful as they do not distinguish between orthopoxviruses.""",
4: """The effects of a heart attack are often permanent, as the heart tissue cannot regenerate, unlike some other tissues. This means that despite somebody surviving a heart attack, the damage done could cause health problems or death in the years following the event. Regenerating heart tissue to allow damaged heart tissue to be treated is a hot topic in research. Now researchers have discovered a mechanism that allows them to treat heart tissue in mice, before a heart attack, in a way that provides protection months later. Although most people survive a heart attack initially, the risk of death significantly increases over the following years. In fact, 65% of people who have a heart attack over the age of 65 die within eight years of the initial incident. This is at least partly because while a person may survive an initial heart attack, the heart attack itself, which leads to the heart tissue being deprived of oxygen and then dying, does not regenerate in adult humans. In a recent animal study, researchers identified a mechanism that allowed them to treat heart tissue and make healthy mice's hearts more resilient before a heart attack.""",
}

def r(no, pid, q, c, a, s, k=""):
    html = (f'<details style="margin:4px 0 8px"><summary style="cursor:pointer;color:var(--accent,#6366f1)">📄 Passage {pid} (برای نمایش متن کلیک کنید)</summary>'
            f'<div style="font-size:13.5px;line-height:1.9;margin-top:6px">{P[pid]}</div></details>{q}')
    add(no, "english", html, [f"{l}) {x}" for l, x in zip("abcd", c)], a, s, k)

# ── Part one: Vocabulary ──
v(81, "The patient with a severe pain in his right index finger had suffered a/an ………. and needed a cast.",
  ["fracture", "laceration", "bruise", "incision"], 1,
  "«گچ گرفتن» (cast) برای «شکستگی» (fracture) است. laceration: پارگی پوست، bruise: کبودی، incision: برش جراحی.")
v(82, "As an important part of their duties, nurses are expected to recognize and then properly ………. patients' emotional stress.",
  ["initiate", "alleviate", "exacerbate", "complicate"], 2,
  "پرستاران باید استرس عاطفی بیمار را «تسکین دهند» (alleviate). initiate: آغاز کردن، exacerbate: تشدید کردن، complicate: پیچیده کردن.")
v(83, "Long after the disease onset, the patient's symptoms still ………. mainly because she avoids seeking medical advice.",
  ["abate", "recede", "subside", "persist"], 4,
  "چون به پزشک مراجعه نمی‌کند، علائم هنوز «ادامه دارند» (persist). سه گزینهٔ دیگر همگی به معنای «فروکش کردن» هستند.",
  "سه گزینهٔ هم‌معنی (abate/recede/subside) معمولاً همگی غلط‌اند.")
v(84, "Never count on his ideas; he often ………. his former opinions and expresses new ones.",
  ["recedes from", "insists on", "adheres to", "ascends to"], 1,
  "روی نظراتش حساب نکن؛ او اغلب از نظرات قبلی‌اش «عقب‌نشینی می‌کند» (recedes from) و نظر جدید می‌دهد. insists on / adheres to: پافشاری/پایبندی (خلاف معنا).")
v(85, "She had a terrible accident; she is alive because of the ………. action of the two ambulance men.",
  ["prompt", "sluggish", "lethargic", "hesitant"], 1,
  "زنده ماندن به‌خاطر اقدام «سریع و به‌موقع» (prompt) امدادگران. sluggish/lethargic: کُند و بی‌حال، hesitant: مردد.")
v(86, "Japan is an ………. country, providing patients with high quality and luxurious healthcare services.",
  ["affluent", "afflicted", "aggressive", "amiable"], 1,
  "کشوری «ثروتمند» (affluent) که خدمات لوکس ارائه می‌دهد. afflicted: مبتلا/گرفتار، aggressive: پرخاشگر، amiable: خوش‌برخورد.")
v(87, "Diagnosed with cancer, the patient showed a ………. behavior, a mixture of sophisticated but childlike behaviors.",
  ["peculiar", "typical", "regular", "genial"], 1,
  "آمیزه‌ای از رفتار پیچیده و کودکانه ⇒ رفتاری «عجیب و غیرمعمول» (peculiar). typical/regular: معمولی (خلاف معنا)، genial: خوش‌مشرب.")
v(88, "The dendrites are ………. the axonal ends of other neurons, with no other tissues in between.",
  ["adjacent to", "distant from", "auxiliary to", "distorted by"], 1,
  "«بدون هیچ بافتی در میان» ⇒ دندریت‌ها «مجاور» (adjacent to) پایانه‌های آکسونی‌اند.")
v(89, "Admission of too many patients in a short time period can result in the ………. of the health system as we have a limited number of personnel and facilities.",
  ["acknowledgement", "collapse", "invigoration", "retrieval"], 2,
  "پذیرش بیمار زیاد با امکانات محدود ⇒ «فروپاشی» (collapse) سیستم سلامت. invigoration: تقویت، retrieval: بازیابی.")
v(90, "Scientists warn that the significant increase in the number of polluted days in Tehran signals a(n) ………. rise of deaths due to cancer in the years to come.",
  ["imminent", "trivial", "negligible", "marginal"], 1,
  "هشدار دربارهٔ افزایش «قریب‌الوقوع» (imminent) مرگ‌ها. trivial/negligible/marginal همگی به معنای «ناچیز» و با «warn» ناسازگارند.")
v(91, "Sound was more ………. through the use of defective hearing aids.",
  ["induced", "distorted", "pursued", "simulated"], 2,
  "سمعک معیوب صدا را «تحریف/مخدوش» (distorted) می‌کند. induced: القا شده، pursued: دنبال شده، simulated: شبیه‌سازی شده.")
v(92, "Vitamins can cause some complications if they ………. the recommended daily dosage.",
  ["provoke", "exceed", "mediate", "maintain"], 2,
  "اگر از دوز توصیه‌شده «فراتر روند» (exceed) عارضه ایجاد می‌کنند.")
v(93, "The engineer stressed that the insulating material should be ………. in water.",
  ["impermeable", "insatiable", "unsaturated", "inflammable"], 1,
  "مادهٔ عایق باید در آب «نفوذناپذیر» (impermeable) باشد. insatiable: سیری‌ناپذیر، inflammable: آتش‌گیر.")
v(94, "The patient had difficulty breathing that was originally ………. left upper lobe pneumonia.",
  ["deviated from", "mal-adjusted to", "attributed to", "excluded from"], 3,
  "تنگی نفس در ابتدا «به» پنومونی لوب فوقانی چپ «نسبت داده شد» (attributed to).")
v(95, "Marking World Malaria Day, the World Health Organization has issued a ………. increased implementation of new and existing interventions to save lives from malaria.",
  ["call for", "halt for", "cessation of", "pause to"], 1,
  "WHO «فراخوانی» (a call for) برای اجرای بیشتر مداخلات صادر کرده است.")
v(96, "Nowadays, doctors believe minimally ………. surgeries are generally less risky than traditional ones as they involve smaller surgical cuts.",
  ["indicative", "invasive", "infective", "intensive"], 2,
  "اصطلاح ثابت پزشکی: minimally invasive surgery = جراحی کم‌تهاجمی (با برش کوچک‌تر).")
v(97, "Without the results of the blood test, the doctor could only make a/an ………. diagnosis.",
  ["exclusive", "conclusive", "comprehensive", "tentative"], 4,
  "بدون نتیجهٔ آزمایش فقط تشخیص «موقت/احتمالی» (tentative) ممکن است. conclusive: قطعی (خلاف معنا).")
v(98, "When a drug is not effective enough, its effect can be ………. by the administration of another drug at the same time.",
  ["eliminated", "potentiated", "relieved", "declined"], 2,
  "اثر دارو با تجویز همزمان داروی دیگر «تقویت» (potentiated) می‌شود (سینرژی).")
v(99, "As there are no cures for some diseases, their ………. is not favorable and the patients are more susceptible to premature death.",
  ["diagnosis", "detection", "eradication", "prognosis"], 4,
  "بیماری بدون درمان ⇒ «پیش‌آگهی» (prognosis) نامطلوب.")
v(100, "The groundbreaking discoveries in the field of nanotechnology have ………. fresh ideas and policies in medical sciences.",
  ["delivered", "postponed", "invaded", "confined"], 1,
  "کشفیات پیشگام ایده‌های تازه «به ارمغان آورده‌اند» (delivered).")

# ── Part two: Reading Comprehension ──
r(101, 1, 'What does the underlined pronoun "it" (paragraph 1) refer to?',
  ["ephemeral balance", "enough working", "working out", "sweet spot"], 1,
  "«Finding it can be tricky» بلافاصله پس از «that ephemeral balance between working out too much and not … enough» آمده؛ it به همین «تعادل زودگذر» برمی‌گردد (sweet spot هم با همین عبارت توضیح داده شده، ولی مرجع نزدیک‌تر ephemeral balance است).")
r(102, 1, "The author is primarily concerned with ……….",
  ["exercises bad for your health", "consequences of over exercising", "how much exercise is needed for individuals", "what benefits physical activity has for individuals"], 3,
  "کل متن دربارهٔ «میزان ورزش لازم» است: حرکت روزانه، نیاز نداشتن به ورزش شدید هر روز و توصیهٔ ۳ جلسه قدرتی و ۵ جلسه هوازی در هفته.")
r(103, 1, '"If you are concerned whether you need to do a sweat-inducing workout every single day" means that you are ……….',
  ["certain that a sweat- inducing workout is required", "at a dilemma to think of workouts as regular activities", "told that a sweat- inducing workout should be truly employed", "recommended to do a sweat-inducing workout every single day"], 2,
  "concerned whether = دودل/نگران بودن که آیا … ⇒ در «دوراهی» بودن دربارهٔ اینکه ورزش سنگین را کار روزمره بدانیم یا نه.")
r(104, 1, 'The underlined word "move" is closest in meaning to ……….',
  ["do some heavy exercise everyday", "work out after daily tasks regularly", "take action when things are out of control", "do basic daily tasks with a continuous motion"], 4,
  "متن تأکید می‌کند «moving every day does not necessarily mean working out» ⇒ منظور تحرک در فعالیت‌های روزمره است، نه ورزش سنگین.")
r(105, 1, "According to the passage, people are ……….",
  ["frightened when constrained by a healthy lifestyle in practice", "shocked when they are constantly exposed to health risks", "highly committed when following an unhealthy lifestyle", "more active when taking on healthy life styles"], 1,
  "«People are often intimidated by committing to a healthy lifestyle» ⇒ intimidated ≈ frightened.")
r(106, 2, "The allocation of resources in the field of medicine tends to be in ……….",
  ["the development of new vaccines", "vaccine-induced medical interventions", "novel medicinal treatments for different diseases", "the establishment of new pharmaceutical companies"], 3,
  "«their investment dollars are channeled disproportionately to new drug therapies in areas such as oncology, …» ⇒ درمان‌های دارویی جدید.")
r(107, 2, "The investment in vaccine development ……….",
  ["benefits from the disproportionate resource allocation", "helps keep people healthy and save money", "jeopardizes human well-being and progress", "causes averted medical care costs"], 2,
  "«vaccines keep people healthy and save money» صریحاً در متن آمده است.")
r(108, 2, 'The writer uses the expression "bitter truth" to show ……….',
  ["drug companies' preference for investment in pharmaceutical treatments", "pharmacists' concern about research in vaccine-based diseases", "drug companies denial of the effectiveness of drug therapies", "allocation of resources to vaccine development"], 1,
  "حقیقت تلخ این است که شرکت‌ها به‌جای واکسن، سرمایه را به درمان‌های دارویی (با بازگشت سرمایهٔ بیشتر) می‌برند.")
r(109, 2, "The passage is primarily concerned with ……….",
  ["consequences of missing vaccination", "diverse approaches in pharmacology", "demerits of vaccine development practices", "resource allocation in vaccine and drug therapies"], 4,
  "موضوع اصلی: تخصیص نامتوازن منابع بین واکسن و درمان‌های دارویی و ضرورت اصلاح آن.")
r(110, 2, "The author believes that ……….",
  ["resource allocation should be made with an eye for values of vaccines", "parental work time should be addressed in vaccine development", "drug companies tendencies for therapies are cost-effective", "medicinal intervention can contribute to wealth growth"], 1,
  "جملهٔ آخر: «taking this value properly into account in the allocation of resources to vaccine development are both essential».")
r(111, 3, "1- Smallpox ……….",
  ["equals in severity to the monkeypox", "is widespread in certain African countries", "is an asymptomatic form of the monkeypox", "manifests more serious symptoms than the monkeypox"], 4,
  "«mpox, a disease with symptoms similar to smallpox, although less severe» ⇒ آبله علائم شدیدتری دارد. (آبله در ۱۹۸۰ ریشه‌کن شده، پس ب غلط است.)")
r(112, 3, "Central and West Africa are ……….",
  ["declared as mpox-free regions", "the locations to which mpox transmission is limited", "the locations reporting mpox cases even nowadays", "famous for having three important clades of the monkeypox"], 3,
  "«mpox continues to occur in countries of Central and West Africa». گزینهٔ ب غلط است چون از ۲۰۲۲ خارج از آفریقا هم گزارش شده؛ کلادها هم دو تا هستند نه سه.")
r(113, 3, "A zoonosis is ……….",
  ["reportedly confined to tropical rainforests", "considered as a subcategory of monkeypox", "a disease transmitted from animals to humans", "a disease transmitted from humans to humans"], 3,
  "«Mpox is a zoonosis, a disease that is transmitted from animals to humans».")
r(114, 3, "Which of the following is true about mpox?",
  ["This disease can be spread through intact skin.", "Humans can transmit monkeypox among each other.", "Contaminated materials cannot lead to monkeypox transmission.", "Lesions on internal mucosal surfaces can help treat the disease."], 2,
  "«The disease can also spread from humans to humans». (انتقال از راه ضایعات پوستی است نه پوست سالم؛ اشیای آلوده هم ناقل‌اند.)")
r(115, 3, "Antigen and antibody detection methods for mpox is not preferred because in these methods ……….",
  ["polymerase chain reaction is merely used for bacterial diseases", "orthopoxviruses cannot be differentiated from each other", "taking diagnostic specimens from the rash is not effective", "it is not feasible to obtain specimen"], 2,
  "«…may not be useful as they do not distinguish between orthopoxviruses».")
r(116, 4, "According to the passage, ……….",
  ["heart tissue is able to regenerate after a stroke", "heart tissue is more vulnerable to future attacks than other tissues", "people experiencing heart attack will survive another attack", "the treatment for a heart attack has significantly improved"], 2,
  "«the heart tissue cannot regenerate, unlike some other tissues» و آسیب آن دائمی است و خطر مرگ در سال‌های بعد بالا می‌رود ⇒ بافت قلب نسبت به سایر بافت‌ها آسیب‌پذیرتر است. گزینهٔ الف خلاف متن است و ج و د در متن نیامده‌اند.")
r(117, 4, "According to the text, heart tissue ………. during a heart attack.",
  ["becomes resistant to future heart attacks", "regenerates gradually", "regenerates and survives", "gets deprived of oxygen and then die"], 4,
  "«…which leads to the heart tissue being deprived of oxygen and then dying».")
r(118, 4, "What did researchers find out in the recent animal study?",
  ["A mechanism that could be utilized to restore oxygen", "A way to restrict the lifespan of mice", "A method to suspend heart tissue regeneration", "A mechanism to help the mice's heart resist future attacks"], 4,
  "«a mechanism that allowed them to treat heart tissue and make healthy mice's hearts more resilient before a heart attack».")
r(119, 4, "The significance of the animal study was to discover a ……….",
  ["new way to treat heart damage in animals", "new trend for heart failure in humans", "method to prevent heart tissue morbidity", "method to introduce a hot topic in research"], 3,
  "درمان «قبل از» حمله و ایجاد محافظت تا ماه‌ها بعد ⇒ روشی «پیشگیرانه» برای آسیب بافت قلب. (گزینهٔ الف درمان آسیبِ ایجادشده است، درحالی‌که مطالعه روی قلب سالم و پیش از حمله انجام شد.)")
r(120, 4, "According to the passage ……….",
  ["more than half of people instantly die after initial heart attack", "people over 65 are more likely to die within 8 years after the attack", "65% of patients with heart attack survive only for 8 years", "experiencing heart attack in patients in their late 60's is more than 65%"], 2,
  "«65% of people who have a heart attack over the age of 65 die within eight years» ⇒ افراد بالای ۶۵ سال به احتمال زیاد (بیش از نیمی) ظرف ۸ سال فوت می‌کنند. الف غلط است (most people survive initially).")
