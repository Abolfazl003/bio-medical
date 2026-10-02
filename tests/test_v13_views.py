"""تست کامل v1.3 — همه ویوهای جدید با مرورگر واقعی"""
import json, sys
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8000/index.html"
errors, results = [], []

def run():
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width":1400,"height":900})
        pg.on("console", lambda m: errors.append("CONSOLE:"+m.text) if m.type=="error" else None)
        pg.on("pageerror", lambda e: errors.append("PAGEERROR:"+str(e)))
        pg.goto(BASE, wait_until="load")
        pg.wait_for_timeout(900)

        def check(name, cond, extra=""):
            results.append((name, bool(cond), extra))

        # ── داشبورد ──
        check("داشبورد بارگذاری شد", pg.locator(".page-head h1").count()>0)
        pp = pg.evaluate("typeof progressCardHTML==='function' ? progressCardHTML().length : -1")
        check("کارت زمان مطالعه در داشبورد", pp>500, f"len={pp}")
        check("کارت پیشرفت داخل صفحه دیده می‌شود", pg.locator(".st-card").count()>0)

        # ── کتابخانه ──
        pg.evaluate("setView('books')"); pg.wait_for_timeout(500)
        shelf = pg.evaluate("document.querySelectorAll('#fullbooks .card').length")
        check("کتابخانه: قفسه هر درس", shelf==10, f"shelf={shelf}")
        books_txt = pg.evaluate("document.querySelector('#fullbooks .card').innerText")
        check("کارت قفسه چند کتاب نشان می‌دهد", "کتاب •" in books_txt, books_txt.replace("\n"," | ")[:120])

        # ── قفسه یک درس (circuits → ۵ کتاب) ──
        pg.evaluate("openBookHome('circuits')"); pg.wait_for_timeout(400)
        n = pg.evaluate("document.querySelectorAll('#blist .card').length")
        check("قفسه circuits = ۵ کتاب", n==5, f"n={n}")
        txt = pg.evaluate("document.querySelector('#blist .card').innerText")
        check("کتاب: فصل/دقیقه/سوال", "سؤال" in txt or "سوال" in txt, txt.replace("\n"," | ")[:130])

        # ── ورود به یک کتاب ──
        pg.evaluate("openBookHome('circuits','cir-basic')"); pg.wait_for_timeout(400)
        toc = pg.evaluate("document.querySelectorAll('.bk-toc-item').length")
        check("فهرست کتاب cir-basic", toc>0, f"toc={toc}")
        check("دکمه آزمون کتاب", "آزمون کتاب" in pg.evaluate("document.querySelector('#main').innerHTML"))
        check("دکمه کلاس استاد", pg.evaluate("!!document.querySelector(\"#main [onclick*='openTeacherBook']\")"))
        check("دکمه جزوه", pg.evaluate("!!document.querySelector(\"#main [onclick*='showJozve']\")"))

        # ── فصل کتاب + شکل واقعی (SVG) + تست فصل ──
        pg.evaluate("openBookChapter('math','math-c5')"); pg.wait_for_timeout(500)
        svg = pg.evaluate("document.querySelectorAll('.bk-fig svg').length")
        check("شکل‌های تصویری واقعی (SVG) در فصل", svg>0, f"svg={svg}")
        check("دکمه تست این فصل", pg.evaluate("!!document.querySelector(\"#main [onclick*='startChapterQuiz']\")"))

        # ── تست فصل: ۶ سوال ──
        chq = pg.evaluate("chapterQuizCount('math','math-c5')")
        check("تست فصل cir-c1 > 0", chq>0, f"n={chq}")
        pg.evaluate("startChapterQuiz('math-stats','math-c5')"); pg.wait_for_timeout(400)
        qtext = pg.evaluate("document.querySelector('.q-text').innerText")
        check("سوال آزمون فصل نمایش داده شد", len(qtext)>10, qtext[:60])
        pg.evaluate("document.querySelectorAll('#choices .choice')[0].click()")
        pg.evaluate("checkAnswer()"); pg.wait_for_timeout(300)
        check("بازخورد سبز/قرمز کار می‌کند", pg.evaluate("document.querySelector('#explain').style.display==='block'"))
        check("زمان مطالعه ثبت شد", pg.evaluate("studiedMinutes()")>0, f"min={pg.evaluate('studiedMinutes()')}")

        # ── پوشش کامل تدریس: متن اسلایدها ≥ متن کتاب ──
        cov = pg.evaluate("""(()=>{
          await0:{
            const L=buildCourseLecture('circuits');
            const slideLen=L.slides.reduce((a,s)=>a+s.body.length,0);
            const key=(typeof chapterKey==="function")?chapterKey('circuits','circ-c1'):'circuits:circ-c1';
            const bk=booksOfCircuitsLen();
            return {slides:L.slides.length, slideLen, bookLen:bk};
          }
        })()""".replace("booksOfCircuitsLen()", "JSON.stringify(BOOK_DATA.circuits).length").replace("await0:", "")) if False else pg.evaluate("""(()=>{
          const L=buildCourseLecture('circuits');
          const slideLen=L.slides.reduce((a,s)=>a+s.body.length,0);
          return {slides:L.slides.length, slideLen, bookLen:JSON.stringify(BOOK_DATA.circuits).length};
        })()""")
        check("تدریس کل متن کتاب را پوشش می‌دهد", cov["slideLen"] >= cov["bookLen"]*0.9,
              f"slides={cov['slides']} teach={cov['slideLen']} book={cov['bookLen']}")
        # ── کلاس کامل استاد یک درس ──
        pg.evaluate("openTeacher('circuits')"); pg.wait_for_timeout(600)
        slides = pg.evaluate("STATE._lecture.slides.length")
        check("کلاس circuits: بخش‌های زیاد (کامل)", slides>80, f"slides={slides}")
        body = pg.evaluate("document.querySelector('.lecture-body').innerText")
        check("متن تدریس پرحجم", len(body)>300, f"len={len(body)}")
        # جلو رفتن ۳۰ اسلاید
        pg.evaluate("for(let i=0;i<30;i++) STATE.teacher.slide++; render();"); pg.wait_for_timeout(400)
        t30 = pg.evaluate("document.querySelector('.lecture-body').innerText")
        check("۳۰ اسلاید جلو رفت (تدریس فصل‌ها)", len(t30)>200, t30[:70].replace("\n"," "))

        # ── کلاس یک کتاب ──
        pg.evaluate("openTeacherBook('cir-basic')"); pg.wait_for_timeout(500)
        bs = pg.evaluate("STATE._lecture.slides.length")
        check("کلاس کتاب cir-basic", bs>30, f"slides={bs}")
        check("دکمه جزوه در کلاس کتاب", pg.evaluate("!!document.querySelector(\"#main [onclick*='showJozve']\")"))

        # ── جزوه کتاب ──
        pg.evaluate("showJozve('cir-basic')"); pg.wait_for_timeout(600)
        jz = pg.evaluate("document.querySelectorAll('#jozve .jz-sec').length")
        formulas = pg.evaluate("document.querySelectorAll('#jozve .jz-formula').length")
        notes = pg.evaluate("document.querySelectorAll('#jozve .jz-note').length")
        qs = pg.evaluate("document.querySelectorAll('#jozve .jz-q').length")
        check("جزوه: بخش‌ها", jz>=7, f"segs={jz}")
        check("جزوه: فرمول‌ها", formulas>=5, f"f={formulas}")
        check("جزوه: نکته/دام", notes>=3, f"n={notes}")
        check("جزوه: پرسش‌ها", qs==6, f"q={qs}")

        # ── جزوه کل درس ──
        pg.evaluate("showJozveSubject('circuits')"); pg.wait_for_timeout(600)
        jf = pg.evaluate("document.querySelectorAll('#jozve .jz-formula').length")
        check("جزوه جامع درس: فرمول همه کتاب‌ها", jf>=25, f"f={jf}")

        # ── صفحه زمان مطالعه ──
        pg.evaluate("setView('progress')"); pg.wait_for_timeout(600)
        check("صفحه زمان: ۴ عدد بزرگ", pg.evaluate("document.querySelectorAll('.big-stat').length")==4)
        check("نمودار ۱۴ روز", pg.evaluate("document.querySelectorAll('.st-chart .st-col').length")==14)
        check("تقویم ۳۵ روزه", pg.evaluate("document.querySelectorAll('.cal-cell').length")>=35)
        check("ردیف پیشرفت درسی", pg.evaluate("document.querySelectorAll('.st-row').length")==10)
        plan = pg.evaluate("studyPlan()")
        check("محاسبه روزها معتبر", plan["daysLeft"]>0 and plan["daysToExam"]>0 and plan["tot"]["total"]>0,
              json.dumps({k:round(v) if isinstance(v,(int,float)) else str(v) for k,v in plan.items() if k!="tot"}, ensure_ascii=False)[:200])
        check("روز تا پایان منطقیست", 40<=plan["daysLeft"]<=200, f"days={plan['daysLeft']} examIn={plan['daysToExam']}")
        star = pg.evaluate("document.querySelector('.st-card .st-num').innerText")
        check("نمایش زمان به فارسی", "دقیقه" in star or "ساعت" in star, star)

        # ── تغییر هدف ──
        pg.evaluate("setGoal(90)"); pg.wait_for_timeout(400)
        check("تغییر هدف روزانه", pg.evaluate("studyPlan().goal")==90)
        pg.evaluate("setGoal(44)")

        # ── استاد: خانه با کارت کتاب‌ها ──
        pg.evaluate("setView('teacher')"); pg.wait_for_timeout(600)
        tc = pg.evaluate("document.querySelectorAll('#tg .card').length")
        check("خانه استاد: ۱۰ درس", tc==10, f"n={tc}")
        check("خانه استاد: کارت زمان مطالعه", pg.evaluate("document.querySelectorAll('.st-card').length")>0)

        # ── کنکور سالم بماند ──
        pg.evaluate("setView('konkur')"); pg.wait_for_timeout(600)
        kg = pg.evaluate("document.querySelector('#main').innerText")
        check("کنکور سراسری ارشد", "کنکور سراسری ارشد" in kg and "۱۴۰۳" in kg)
        # ── تست ترکیبی ──
        pg.evaluate("setView('quiz')"); pg.wait_for_timeout(400)
        check("بخش تست ترکیبی باز شد", pg.locator("#main").inner_text().strip()!="")

        # ── موبایل ──
        m = b.new_page(viewport={"width":390,"height":844}, is_mobile=True, has_touch=True, device_scale_factor=3)
        m.on("pageerror", lambda e: errors.append("MOBILE:"+str(e)))
        m.goto(BASE, wait_until="load"); m.wait_for_timeout(900)
        nv = m.evaluate("document.querySelectorAll('.nav-btn').length")
        nb = m.evaluate("(()=>{const r=document.querySelector('.sidebar').getBoundingClientRect();return {w:Math.round(r.width),h:Math.round(r.height),top:Math.round(r.top)}})()")
        overflow = m.evaluate("document.querySelector('nav').scrollWidth - document.querySelector('nav').clientWidth")
        check("موبایل: ۱۴ دکمه ناوبری", nv==14, f"n={nv}")
        check("موبایل: نوار پایین بدون سرریز افقی", overflow<=2, f"overflow={overflow} navW={nb['w']}")
        m.evaluate("setView('progress')"); m.wait_for_timeout(500)
        mo = m.evaluate("document.documentElement.scrollWidth + '/' + window.innerWidth")
        check("موبایل: صفحه زمان بدون سرریز", m.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"), mo)
        m.screenshot(path="/home/user/shots4/mobile-progress.png", full_page=False)
        m.evaluate("openBookHome('circuits','cir-basic'); openBookChapter('math','math-c5')"); m.wait_for_timeout(600)
        check("موبایل: شکل کتاب سرریز نمی‌کند", m.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"))
        m.screenshot(path="/home/user/shots4/mobile-book.png")
        m.evaluate("showJozve('cir-basic')"); m.wait_for_timeout(600)
        check("موبایل: جزوه خوانا", m.evaluate("document.querySelectorAll('.jz-formula').length")>0)
        m.screenshot(path="/home/user/shots4/mobile-jozve.png")
        m.evaluate("setView('teacher')"); m.wait_for_timeout(400)
        m.screenshot(path="/home/user/shots4/mobile-teacher.png")
        b.close()

run()
print("=== نتایج ===")
bad = 0
for n, ok, extra in results:
    print(("✅ " if ok else "❌ ") + n + ((" | " + str(extra)) if extra and not ok else ""))
    if not ok: bad += 1
print(f"\nخلاصه: {len(results)-bad}/{len(results)} موفق")
if errors:
    print("\n=== خطاهای مرورگر ===")
    for e in errors[:20]: print("•", e)
else:
    print("✅ بدون خطای کنسول")
sys.exit(1 if bad else 0)
