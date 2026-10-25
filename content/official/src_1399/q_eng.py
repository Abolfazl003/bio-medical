# -*- coding: utf-8 -*-
"""دفترچه ۱۳۹۹ — زبان عمومی (سوال‌های ۸۱ تا ۱۲۰)"""
Q = []

def add(no, q, c, s, k='', img=None):
    Q.append({"no": no, "q": q, "c": c, "s": s, "k": k, **({"img": img} if img else {})})

add(81,
    "Trauma and infectious diseases have been the ...................... causes of death for a long time, with many lives lost.",
    ["promising", "declining", "depriving", "leading"],
    "«علل اصلی/مهم مرگ» → the leading causes. promising = امیدبخش، declining = در حال کاهش، depriving = محروم‌کننده. گزینهٔ ۴.",
    k="leading causes of death = علل اصلی مرگ")

add(82,
    "Despite his doctor's warnings to avoid getting overweight, he was unable to ...................... his desire for fatty foods.",
    ["confirm", "convict", "conceal", "confuse"],
    "«ناتوان از پنهان کردن علاقه‌اش به غذاهای چرب» → conceal (پنهان کردن). confirm = تأیید، convict = محکوم کردن، confuse = مبهوت کردن. گزینهٔ ۳.")

add(83,
    "Scientists believe that physical exercise ...................... an individual's state of health.",
    ["contrasts with", "contributes to", "is characterized by", "is disapproved by"],
    "«ورزش در بهبودِ وضعیت سلامت افراد مشارکت دارد» → contributes to (سهم داشتن در). گزینهٔ ۲.")

add(84,
    "Medical scientists studying DNA and genes try to ...................... those genes which cause inherited diseases.",
    ["detect", "protect", "advocate", "proliferate"],
    "«تلاش می‌کنند ژن‌هایی را که باعث بیماری‌های ارثی می‌شوند شناسایی کنند» → detect (تشخیص/کشف). protect = محافظت، advocate = حمایت کردن، proliferate = تکثیر. گزینهٔ ۱.")

add(85,
    "Medicine is a discipline which ...................... many other fields of study such as physiology and pathology.",
    ["encompasses", "endangers", "entangles", "entitles"],
    "«پزشکی رشته‌ای است که بسیاری از حوزه‌های دیگر را در بر می‌گیرد» → encompasses (شامل می‌شود). endangers = به خطر انداختن، entangles = درهم‌تنیدن، entitles = مستحق کردن. گزینهٔ ۱.")

add(86,
    "Epidemiologists believe that immunity by vaccination should be ...................... for some diseases every ten years.",
    ["subsided", "suspended", "reinforced", "contracted"],
    "«ایمنی حاصل از واکسیناسیون برای بعضی بیماری‌ها هر ده سال باید تقویت شود» → reinforced (تقویت شدن/تجدید). subside = فروکش کردن، suspend = تعلیق، contract = ابتلا/منقبض شدن. گزینهٔ ۳.",
    k="booster shot = دوز یادآور/تقویت‌کننده")

add(87,
    "People ...................... severe infectious diseases should visit a specialist before any intervention.",
    ["assessed by", "elicited by", "supplied with", "afflicted with"],
    "«افرادِ مبتلا به بیماری‌های عفونی شدید» → afflicted with (گرفتار/مبتلا). assessed = ارزیابی شده، elicited = برانگیخته شده، supplied = مجهز شده. گزینهٔ ۴.",
    k="afflict = مبتلا/گرفتار کردن")

add(88,
    "Restricted ...................... to sunshine is recommended to people suffering from skin-related diseases.",
    ["susceptibility", "exposure", "contribution", "objection"],
    "«قرار گرفتنِ محدود در معرض آفتاب» → exposure (در معرض بودن). susceptibility = حساسیت/آسیب‌پذیری، contribution = مشارکت، objection = اعتراض. گزینهٔ ۲.",
    k="exposure to = قرار گرفتن در معرض")

add(89,
    "She fell down the stairs, ...................... her ankle and breaking her leg.",
    ["twisting", "squeezing", "transferring", "sustaining"],
    "«از پله‌ها افتاد، مچش را پیچاند و پایش را شکست» → twisting (پیچاندن). twist one's ankle = پیچیدن مچ. squeeze = فشردن، transfer = انتقال، sustain = تحمل کردن (مثلاً sustain an injury). گزینهٔ ۱.")

add(90,
    "Regulation of temperature through dispersing heat is one of the main ...................... of the skin.",
    ["conflicts", "failures", "dilemmas", "functions"],
    "«تنظیم دما از طریق پخش گرما یکی از کارکردهای اصلی پوست است» → functions. گزینهٔ ۴.")

add(91,
    "The acquisition of physical characteristics are mainly due to ...................... rather than the environment.",
    ["morbidity", "heredity", "vitality", "fatality"],
    "«کسب ویژگی‌های جسمانی عمدتاً ناشی از وراثت است نه محیط» → heredity. morbidity = بیماری‌زایی، vitality = سرزندگی، fatality = مرگ‌ومیر. گزینهٔ ۲.",
    k="مقایسهٔ کلاسیک nature vs nurture")

add(92,
    "Educational psychologists have suggested significant revolutionary steps to ...................... the quality of tertiary education in the country.",
    ["hamper", "diminish", "promote", "penetrate"],
    "«گام‌های انقلابی برای ارتقای کیفیت آموزش عالی» → promote (ارتقا/ترویج). hamper = مانع شدن، diminish = کاهش، penetrate = نفوذ. گزینهٔ ۳.",
    k="tertiary education = آموزش بالاتر/دانشگاهی")

add(93,
    "For the purpose of a better diagnosis, the medical team decided to perform a more ...................... examination on the patient.",
    ["superficial", "elaborate", "repressive", "detrimental"],
    "«معاینه‌ای دقیق‌تر و مفصل‌تر برای تشخیص بهتر» → elaborate (مفصل/دقیق). superficial = سطحی، repressive = سرکوبگرانه، detrimental = زیان‌بار. گزینهٔ ۲.")

add(94,
    "Chronic pain is a type of pain which ...................... and lasts for three months or more.",
    ["persists", "fades away", "attenuates", "vanishes"],
    "«درد مزمن نوعی درد است که پایدار می‌ماند و سه ماه یا بیشتر طول می‌کشد» → persists (ادامه یافتن/پابرجا شدن). fade away = محو شدن، attenuate = کاهش، vanish = از بین رفتن. گزینهٔ ۱.")

add(95,
    "Taking a complete history can help ...................... the information needed for a thorough differential diagnosis.",
    ["repress", "elicit", "underrate", "inhibit"],
    "«شرح‌حال کامل به استخراج (برآوردن) اطلاعات لازم برای تشخیص افتراقی کمک می‌کند» → elicit (به وجود آوردن/استخراج). repress = سرکوب، underrate = کم‌ارزیابی، inhibit = مهار. گزینهٔ ۲.",
    k="elicit = obtain/bring out")

add(96,
    "Because of the complexity of the disease, groups of multidisciplinary specialists have ...................... to decide about the possible treatment modality.",
    ["concealed", "evaded", "avoided", "convened"],
    "«گروه‌های متخصصِ چندرشته‌ای گرد هم آمدند تا دربارهٔ روش درمان تصمیم بگیرند» → convened (تشکیل جلسه دادن/گردهمایی). conceal = پنهان، evade = فرار، avoid = پرهیز. گزینهٔ ۴.")

add(97,
    "Blood is a ...................... through which essential nutrients are taken to tissues.",
    ["medium", "marker", "spectrum", "barrier"],
    "«خون وسیلهٔ انتقال‌دهنده‌ای است که مواد مغذی را به بافت‌ها می‌برد» → medium (رسانه/واسط). marker = نشانگر، spectrum = طیف، barrier = سد. گزینهٔ ۱.")

add(98,
    "In many instances of the disease, the virus remains at the initial site of infection, and any possible symptom ...................... from that site.",
    ["withdraws", "recedes", "originates", "escapes"],
    "«هر علامت احتمالی از همان محل آغازین سرچشمه می‌گیرد» → originates from (منشأ گرفتن). withdraw = عقب کشیدن، recede = دور شدن، escape = گریختن. گزینهٔ ۳.")

add(99,
    "Medical research has ...................... promising results to fight against Coronavirus.",
    ["abandoned", "infected", "revealed", "surrounded"],
    "«پژوهش‌های پزشکی نتایج امیدبخشی را در مبارزه با کرونا آشکار کرده‌اند» → revealed (نشان دادن/فاش کردن). abandon = رها، infect = آلوده، surround = احاطه. گزینهٔ ۳.")

add(100,
    "Scientists managed to ...................... a nerve fiber in the brain which carries messages from cell to cell.",
    ["complicate", "combat", "represent", "identify"],
    "«دانشمندان موفق شدند فیبر عصبی را در مغز شناسایی کنند که پیام‌ها را از سلولی به سلول دیگر می‌رساند» → identify (شناسایی). complicate = پیچیده، combat = مبارزه، represent = بازنمایی. گزینهٔ ۴.")

P1 = """<b>Passage 1:</b> "As the COVID-19 pandemic spreads to the world's poorest regions, the weakest countries will be affected the hardest by adding a serious health and economic crisis to existing poverty and climate crises. This multifaceted crisis will keep adding pressure to poorer communities. Clean energy is believed to be necessary to help countries prepare, respond, and recover from COVID-19 crisis. Clean energy can provide solutions that are in line with climatic goals and can help reduce the effects of the COVID-19 crisis on people's life and local economies. On the frontline of the battle against COVID-19, energy for households and health centers is highly necessary. As many as 840 million people do not have electricity, 570 million of them live in sub-Saharan Africa, where one in four clinics has no energy at all, and 28 percent do not have regular access to energy. Reliable power supply ensures that core systems for the management of health programs can work effectively. In regions where the electricity is unreliable or even non-existent, clean energy technologies provide solutions that can be used rapidly. With reliable clean energy, health centers can work all the time, instead of depending on candles or phone flashlights. Clean energy can also address some of the health risks that might make people weaker in the face of respiratory diseases such as COVID-19. Access to the energy also makes social distancing policies possible and can provide reliable access to clean water, an important element in times of COVID-19."<br><br>"""

add(101, P1 + "The first sentence of the passage mainly deals with ...................... in the poorest countries.",
    ["climate change caused by Covid-19", "treatment difficulties of Covid-19", "serious consequences of Covid-19", "rapid spread of Covid-19"],
    "جملهٔ اول متن می‌گوید همه‌گیری کرونا با افزودن بحران سلامت و اقتصادی به فقر و بحران اقلیمی موجود، سخت‌ترین ضربه را به فقیرترین کشورها می‌زند؛ یعنی تبعات جدی کرونا در فقیرترین کشورها → serious consequences of Covid-19. گزینهٔ ۳.")

add(102, P1 + "According to the passage, ...................... is extremely important for households and health centers in the fight against COVID-19.",
    ["economy", "energy", "clinics", "technology"],
    "متن صریحاً می‌گوید: «انرژی برای منازل و مراکز درمانی در خط مقدم نبرد با کووید-۱۹ بسیار ضروری است» → energy. گزینهٔ ۲.")

add(103, P1 + "The main problem in sub-Saharan Africa is ...................... .",
    ["clean water", "shortage of electricity", "lack of clinics", "health mismanagement"],
    "طبق متن، از ۸۴۰ میلیون نفری که برق ندارند ۵۷۰ میلیون نفر در آفریقای زیر صحرا زندگی می‌کنند و یک چهارم کلینیک‌هایشان اصلاً انرژی ندارند ← مشکل اصلی: کمبود برق. گزینهٔ ۲.")

add(104, P1 + "It can be inferred from the passage that ...................... .",
    ["the COVID-19 affects all countries similarly", "sub-Saharan African countries do not need more clinics", "clean energy can help prevention of the COVID-19", "phone flashlights provide a reliable energy supply"],
    "استنباط درست: انرژی پاک می‌تواند خطرات سلامتی را که افراد را در برابر بیماری‌های تنفسی ضعیف‌تر می‌کند کاهش دهد و به فاصله‌گذاری اجتماعی و آب پاکیزه کمک کند؛ یعنی به پیشگیری از کرونا کمک می‌کند. سایر گزینه‌ها با متن ناسازگارند (کرونا همهٔ کشورها را یکسان تحت تأثیر نمی‌گذارد؛ چراغ قوهٔ تلفن منبع قابل اعتماد نیست). گزینهٔ ۳.")

add(105, P1 + "The clean energy ...................... .",
    ["makes it possible for health centers work nonstop", "makes people weaker in the face of COVID-19", "removes social distancing policies", "can predict social health risks"],
    "طبق متن: «With reliable clean energy, health centers can work all the time» ← مراکز درمانی می‌توانند دائماً کار کنند (nonstop). گزینهٔ ۱.")

P2 = """<b>Passage 2:</b> "In many disabling illnesses, simple exercises are begun even while a patient is still in bed. Hot packs and other forms of local heat application may be used in the early stages of poliomyelitis at the same time an effort is being made to exercise muscles. If a person has suffered a stroke which has paralyzed his limbs, the limbs must be exercised from the very beginning in order to prevent the joints from becoming stiffened and fixed in position, and to maintain strength in the muscles. If active exercises are begun and a program of massage is carried out after the patient has regained consciousness, the possibility of the patient being bedridden for the rest of his/her life can be lessened."<br><br>"""

add(106, P2 + "According to the passage, simple exercises start ...................... in a lot of disabling diseases.",
    ["at the very early stages of the illness", "when the patient leaves the hospital", "after the patient receives other interventions", "before the application of hot packs and heat"],
    "متن می‌گوید «تمرین‌های ساده حتی وقتی بیمار هنوز در تخت است آغاز می‌شوند»؛ یعنی در مراحل خیلی ابتدایی بیماری → at the very early stages of the illness. گزینهٔ ۱.")

add(107, P2 + "In the beginning stages of poliomyelitis ...................... .",
    ["only heat application is used to help the patient", "the exercise of the joints is performed", "hot packs as well as exercise are locally applied", "a lot of efforts are being made in exercises"],
    "طبق متن در مراحل اولیهٔ فلج اطفال هم‌زمان از کمپرس‌های داغ (اشکال گرمای موضعی) و تمرین عضلات استفاده می‌شود → hot packs as well as exercise. گزینهٔ ۳.")

add(108, P2 + "In a stroke, ...................... .",
    ["the limbs will be fixed in position", "the muscles will never regain their strength", "exercises of the joints should be avoided", "prompt efforts should be taken to stop joint stiffness"],
    "در سکتهٔ مغزی که دودان را فلج کرده، باید از همان ابتدا دودان تمرین داده شوند تا مفاصل خشک و ثابت نشوند → تلاش فوری برای جلوگیری از خشکی مفاصل. گزینهٔ ۴.")

add(109, P2 + "In which of the following situations can the chance of being bedridden forever be decreased?",
    ["When the massage programs begin before regaining consciousness",
     "Applying exercises and massage after the patient becomes conscious",
     "When hot packs and exercises are applied at the final stage",
     "Fixing the paralyzed patient's limbs before the patient becomes conscious"],
    "طبق متن: اگر پس از هوشیاری بیمار، تمرینات فعال و ماساژ انجام شود، احتمال تخت‌خوابیدنی شدن مادام‌العمر کاهش می‌یابد → گزینهٔ ۲.")

add(110, P2 + "The passage is generally about ...................... .",
    ["how stroke patients should be treated to regain consciousness", "when to prevent poliomyelitis in stroke patients", "why the joints become stiffened using local heat", "measures to be taken to help patients with disabling illnesses"],
    "متن کلاً دربارهٔ اقدامات نگهدارنده (تمرین، گرمای موضعی، ماساژ) برای کمک به بیمارانِ مبتلا به بیماری‌های ناتوان‌کننده است → measures to be taken to help patients with disabling illnesses. گزینهٔ ۴.")

P3 = """<b>Passage 3:</b> "Anxiety disorders and depression seriously harm people in this technological age. Young adults, who are particularly at risk of mental illnesses, are associated with a greater risk of substance use, suicide, and poor academic performance. Research has shown that the use of social media, such as Facebook and Instagram, are linked to both depression and anxiety. The increased use of social media might lead to negative online experiences, a low amount of real, face-to-face communication, and attention deficit disorder. The frequently unrealistic presentation of one's physical appearance and life achievement on social media often cause strong feelings of dissatisfaction, low self-confidence, and decreased self-worth."<br><br>"""

add(111, P3 + "According to the passage, increased use of social media has ...................... people's well-being.",
    ["worsened", "elevated", "nothing to do with", "been adjusted with"],
    "متن می‌گوید افزایش استفاده از شبکه‌های اجتماعی با افسردگی و اضطراب همراه است و به تجربه‌های آنلاین منفی منجر می‌شود؛ یعنی بهبودِ تندرستی (well-being) را بدتر کرده → worsened. گزینهٔ ۱.")

add(112, P3 + "According to the passage, face-to-face communication ...................... greater use of social media.",
    ["happens regularly by", "is disregarded with", "is independent of", "is reduced by"],
    "طبق متن، استفادهٔ بیشتر از رسانه‌های اجتماعی به «مقدار کم ارتباط واقعی رودررو» (a low amount of real, face-to-face communication) منجر می‌شود → ارتباط رودررو با استفادهٔ بیشتر شبکه‌های اجتماعی کاهش می‌یابد. گزینهٔ ۴.")

add(113, P3 + "How is people's self-image influenced by the social media?",
    ["They avoid using social media regularly.", "They are afraid of technological advances.", "They present a false picture of their lives.", "They think very highly of themselves."],
    "متن می‌گوید «نمایش مکرر و غیرواقعی ظاهر و دستاوردهای زندگی افراد در شبکه‌های اجتماعی»... → افراد تصویر کاذبی از زندگی‌شان ارائه می‌دهند. گزینهٔ ۳.")

add(114, P3 + "The author believes that fake self-manifestations on social media could ...................... .",
    ["have a positive outcome", "result in displeasure and worthlessness", "enhance the youth self-esteem", "cause satisfaction and self-worth"],
    "طبق جملهٔ پایانی متن، نمایش‌های غیرواقعی باعث «احساس قوی نارضایتی، اعتمادبه‌نفس پایین و کاهش خودارزشی» می‌شود → نتایج: ناخشنودی و بی‌ارزشی (displeasure and worthlessness). گزینهٔ ۲.")

add(115, P3 + "The author concludes that low self-confidence and decreased self-worth ...................... unreal presentations on social media.",
    ["give rise to", "result from", "contribute to", "prevent from"],
    "اعتمادبه‌نفس پایین و کاهش خودارزشی «نتیجهٔ» نمایش‌های غیرواقعی در شبکه‌های اجتماعی است → result from (ناشی شدن از). گزینهٔ ۲.",
    k="result from X = ناشی از X ؛ result in X = منتج به X")

P4 = """<b>Passage 4:</b> "Healthcare workers treating patients with infections are at risk of infection themselves. To protect themselves against droplets from coughs, sneezes or body fluids from infected patients and contaminated surfaces, they use personal protective equipment (PPE), e.g., aprons, gowns or coveralls, gloves, masks and breathing equipment (respirators), and goggles. But if not worn correctly, these may endanger healthcare workers when they remove PPE. Covering more of the body leads to better protection. Coveralls are the most difficult PPE to remove but may offer the best protection, followed by long gowns and aprons. Respirators worn with coveralls may protect better than a mask worn with a gown, but are more difficult to put on. More breathable types of PPE may lead to similar levels of contamination but be more comfortable. Gowns that have gloves, and gowns that fit tightly at the neck may reduce contamination. Also, adding tabs to gloves and face masks may lead to less contamination. More breathable types provide greater comfort and satisfaction but may lead to similar contamination. Face-to-face training in PPE use is recommended as the most effective strategy to reduce errors. But to find out which combinations of PPE protect best, we still need further research findings, simulation studies with more participants, and more real-life evidence."<br><br>"""

add(116, P4 + "In the first paragraph, the underlined pronoun 'they' refers to ...................... .",
    ["infected patients", "droplets from coughs and sneezes", "healthcare workers", "bodily fluids"],
    "«they» به مراقبان بهداشتی برمی‌گردد (HealthCare workers ... They use personal protective equipment). گزینهٔ ۳.")

add(117, P4 + "Safe removal of PPE is ...................... the way it is put on by the health workers.",
    ["influenced by", "independent of", "identical to", "irrelevant to"],
    "طبق متن اگر PPE درست پوشیده نشود، هنگام درآوردنش خطرناک است؛ یعنی خروج امن از PPE تحت تأثیر نحوهٔ پوشیدن آن است → influenced by. گزینهٔ ۱.")

add(118, P4 + "The author of the passage ...................... the best combinations of PPE protection.",
    ["approves health workers' suggestions on", "calls for more studies and evidence for", "provides more satisfaction with", "wants infected patients to avoid"],
    "جملهٔ پایانی متن: برای یافتن بهترین ترکیب‌های PPE هنوز به یافتههای پژوهشی بیشتر، مطالعات شبیه‌سازی و شواهد زندگی واقعی بیشتری نیاز است → نویسنده خواستار مطالعات و شواهد بیشتر است. گزینهٔ ۲.")

add(119, P4 + "It can be inferred from the passage that ...................... are associated with users' comfort and satisfaction.",
    ["similar levels of contamination", "more training in PPE use and tabs", "respirators worn with coveralls", "more breathable PPE types"],
    "متن صریح: «More breathable types provide greater comfort and satisfaction» → انواع تنفس‌پذیرتر → راحتی و رضایت. گزینهٔ ۴.")

add(120, P4 + "Which of the following three PPE items are stated to be the most protective and least comfortable?",
    ["coveralls, long gowns and aprons", "coveralls, aprons and face masks", "gloves, masks and respirators", "aprons, masks and gloves"],
    "طبق متن coveralls سخت‌ترین برای درآوردن اما بهترین حفاظت را دارند و پس از آن long gowns و aprons قرار می‌گیرند (گرمایش/راحتی کمتر-حفاظت‌ترین). گزینهٔ ۱.")
