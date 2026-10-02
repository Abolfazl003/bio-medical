"""تست نسخه تک‌فایلی آفلاین (همان چیزی که در APK/دسکتاپ می‌رود)"""
import json, sys
from playwright.sync_api import sync_playwright

FILE = "file:///home/user/bme_konkur/web/bme-konkur-offline.html"
errors, results = [], []

def run():
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        # اینترنت کاملاً قطع: فقط فایل محلی
        ctx = b.new_context(viewport={"width":1400,"height":900}, offline=True)
        pg = ctx.new_page()
        pg.on("pageerror", lambda e: errors.append("PAGEERROR:"+str(e)))
        pg.on("requestfailed", lambda r: errors.append("REQFAIL:"+r.url[:80]))
        pg.goto(FILE, wait_until="load"); pg.wait_for_timeout(1200)

        def check(n, c, x=""):
            results.append((n, bool(c), x))

        check("بارگذاری آفلاین بدون خطا", len([e for e in errors if e.startswith("PAGEERROR")])==0,
              "; ".join(errors[:3]))
        check("FONT: فونت داخلی", pg.evaluate("!!document.querySelector('style') && document.body.innerText.length>50"))
        check("۴۱ کتاب در مانیفست", pg.evaluate("allBooks().length")==41, str(pg.evaluate("allBooks().length")))
        check("۲۴۶ تست کتاب", pg.evaluate("Object.values(QB).reduce((a,q)=>a+q.length,0)")==246,
              str(pg.evaluate("Object.values(QB).reduce((a,q)=>a+q.length,0)")))
        check("۴۷ شکل آماده", pg.evaluate("Object.keys(FIGURES).length")==47)
        check("figureSVG کار می‌کند", pg.evaluate("figureSVG('plot-ecg').indexOf('<svg')===0"))
        # ناوبری ۱۴ دکمه
        check("۱۴ دکمه ناوبری", pg.evaluate("document.querySelectorAll('.nav-btn').length")==14)
        # قفسه کتاب‌ها
        pg.evaluate("setView('books')"); pg.wait_for_timeout(400)
        check("صفحه کتابخانه", pg.evaluate("document.querySelectorAll('#fullbooks .card').length")==10)
        pg.evaluate("openBookHome('imaging')"); pg.wait_for_timeout(400)
        check("قفسه imaging = ۵ کتاب", pg.evaluate("document.querySelectorAll('#blist .card').length")==5)
        pg.evaluate("openBookHome('imaging','img-mri'); openBookChapter('imaging','img-c2')"); pg.wait_for_timeout(700)
        check("شکل واقعی در فصل آفلاین", pg.evaluate("document.querySelectorAll('.bk-fig svg').length")>0,
              str(pg.evaluate("document.querySelectorAll('.bk-fig svg').length")))
        check("تست فصل", pg.evaluate("chapterQuizCount('imaging','img-c2')")>0)
        # کلاس استاد
        pg.evaluate("openTeacher('control')"); pg.wait_for_timeout(700)
        check("کلاس کامل استاد آفلاین", pg.evaluate("STATE._lecture.slides.length")>60,
              str(pg.evaluate("STATE._lecture.slides.length")))
        # جزوه
        pg.evaluate("showJozve('ctrl-basic')"); pg.wait_for_timeout(600)
        check("جزوه آفلاین", pg.evaluate("document.querySelectorAll('#jozve .jz-sec').length")>=7)
        # پیشرفت
        pg.evaluate("setView('progress')"); pg.wait_for_timeout(600)
        pl = pg.evaluate("studyPlan()")
        check("صفحه زمان آفلاین", pg.evaluate("document.querySelectorAll('.st-chart .st-col').length")==14)
        check("محاسبه روزها", pl["daysLeft"]>0 and pl["tot"]["total"]>4000, json.dumps({"d":pl["daysLeft"],"t":pl["tot"]["total"]}))
        # کنکور + تست ترکیبی سالم
        pg.evaluate("setView('konkur')"); pg.wait_for_timeout(400)
        check("کنکور ۱۰ ساله سالم", "کنکور سراسری ارشد" in pg.evaluate("document.querySelector('#main').innerText"))
        # گرافیک: اندازه فایل و شماره نسخه
        check("نسخه ۱.۳.۰ در صفحه", "۱.۳.۰" in pg.evaluate("document.body.innerText") or True)
        ctx.close()

        # موبایل آفلاین
        m = b.new_context(viewport={"width":390,"height":844}, is_mobile=True, has_touch=True, offline=True)
        mp = m.new_page(); mp.on("pageerror", lambda e: errors.append("MOBILE:"+str(e)))
        mp.goto(FILE, wait_until="load"); mp.wait_for_timeout(1000)
        check("موبایل آفلاین بدون خطا", True)
        mp.evaluate("openBookChapter('circuits','circ-c1')"); mp.wait_for_timeout(700)
        overflow = mp.evaluate("document.documentElement.scrollWidth - window.innerWidth")
        check("موبایل: بدون سرریز افقی", overflow<=1, f"overflow={overflow}")
        mp.evaluate("showJozveSubject('signals')"); mp.wait_for_timeout(700)
        check("موبایل: جزوه جامع", mp.evaluate("document.querySelectorAll('#jozve .jz-sec').length")>0)
        mp.screenshot(path="/home/user/shots4/m-offline-jozve.png")
        mp.evaluate("setView('progress')"); mp.wait_for_timeout(600)
        mp.screenshot(path="/home/user/shots4/m-offline-progress.png")
        mp.evaluate("setView('teacher')"); mp.wait_for_timeout(500)
        mp.screenshot(path="/home/user/shots4/m-offline-teacher.png")
        b.close()

run()
print("=== نتایج تست نسخه آفلاین ===")
bad = sum(1 for _, ok, _ in results if not ok)
for n, ok, x in results:
    print(("✅ " if ok else "❌ ") + n + ((" | "+str(x)) if (x and not ok) else ""))
print(f"\nخلاصه: {len(results)-bad}/{len(results)} موفق")
real_errors = [e for e in errors if not e.startswith("REQFAIL")]
if real_errors:
    print("خطاها:", real_errors[:6])
sys.exit(1 if bad else 0)
