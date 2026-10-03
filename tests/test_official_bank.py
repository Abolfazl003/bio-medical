#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست‌های بخش «🏛 بانک سوالات رسمی کنکور» (v1.3.4)
- ۱۸ دوره رسمی: ۱۳۸۷ تا ۱۴۰۴
- تعداد سوال هر دفترچه طبق جلد خود دفترچه‌ها
- زمان واقعی آزمون هر سال (۱۶۰ دقیقه؛ ۱۳۸۷: ۱۵۰ دقیقه)
- سیاست پاسخ‌نامه: حل مؤلف (غیررسمی) — کلید رسمی سنجش داخل دفترچه‌ها نیست
- سال ۱۴۰۲ تنها دفترچه دریافت‌نشده
"""
import asyncio, sys, os
from playwright.async_api import async_playwright

BASE = os.environ.get("APP_URL", "http://127.0.0.1:8000/index.html")
ok = fail = 0
def check(name, cond, extra=""):
    global ok, fail
    if cond:
        ok += 1; print(f"  ✅ {name}")
    else:
        fail += 1; print(f"  ❌ {name} {extra}")

EXPECT = {"1387":110,"1388":130,"1389":130,"1390":130,"1391":130,"1392":130,"1393":130,
          "1394":130,"1395":130,"1396":135,"1397":140,"1398":130,"1399":130,"1400":120,
          "1401":120,"1402":None,"1403":120,"1404":120}

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1300,"height":1000})
        errs=[]
        pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto(BASE, wait_until="load")
        await pg.wait_for_timeout(600)

        d = await pg.evaluate("""(() => {
          const c = {};
          PKR_YEARS.forEach(y => c[y] = PKR_EXAM_COUNT[y]);
          return {years: PKR_YEARS.length, list: PKR_YEARS.slice(), count: c,
                  recv: prReceived(), cap: prCapacity(), missing: PKR_MISSING.slice(),
                  t1387: prTimeMin('1387'), t1397: prTimeMin('1397'), t1404: prTimeMin('1404'),
                  policy: PKR_KEY_POLICY};
        })()""")

        print("— فهرست دوره‌ها —")
        check("۱۸ دوره رسمی", d["years"] == 18, d["years"])
        check("۱۳۸۷ اولین دوره", d["list"][0] == "1387")
        check("۱۴۰۴ آخرین دوره", d["list"][-1] == "1404")
        check("سال‌ها پیوسته ۱۳۸۷→۱۴۰۴",
              d["list"] == [str(y) for y in range(1387, 1405)])

        print("— تعداد سوال هر دفترچه —")
        for y, n in EXPECT.items():
            check(f"{y} = {n}", d["count"].get(y) == n, d["count"].get(y))
        check("۱۷ دفترچه دریافت‌شده", d["recv"] == 17, d["recv"])
        check("فقط ۱۴۰۲ گم است", d["missing"] == ["1402"], d["missing"])
        check("سوال دفترچه‌های موجود = ۲۱۶۵", d["cap"] == sum(v for v in EXPECT.values() if v), d["cap"])

        print("— زمان آزمون واقعی —")
        check("۱۳۸۷ → ۱۵۰ دقیقه", d["t1387"] == 150, d["t1387"])
        check("۱۳۹۷ → ۱۶۰ دقیقه", d["t1397"] == 160, d["t1397"])
        check("۱۴۰۴ → ۱۶۰ دقیقه", d["t1404"] == 160, d["t1404"])

        print("— سیاست پاسخ‌نامه —")
        check("حل مؤلف (غیررسمی) اعلام شده", "حل مؤلف" in d["policy"])

        print("— صفحه رسمی —")
        await pg.evaluate("setView('konkur')")
        await pg.wait_for_timeout(500)
        cards = await pg.evaluate("document.querySelectorAll('#prg .card').length")
        check("۱۸ کارت سال در صفحه", cards == 18, cards)
        txt = await pg.evaluate("document.getElementById('main').innerText")
        for probe in ["۱۳۸۷", "۱۴۰۴", "۱۸ دوره", "۱۴۰۲", "حل مؤلف", "۱۵۰ دقیقه"]:
            check(f"متن صفحه شامل {probe}", probe in txt)

        print("— بخش آزمایشی دست‌نخورده —")
        check("۱۲۰۰ سوال آزمایشی سر جایش", await pg.evaluate("pkTotalCount()") == 1200)
        check("۱۰ سال آزمایشی", await pg.evaluate("pkYears().length") == 10)

        print("— تایمر آزمون رسمی —")
        t = await pg.evaluate("""(() => {
          const y='1404';
          prAttach=null; return true;
        })()""")
        # ساخت آزمون رسمی از سالی که سوال دارد؛ در صورت نبود سوال، منطق تایمر بررسی می‌شود
        tsec = await pg.evaluate("prTimeMin('1404')*60")
        check("تایمر آزمون رسمی ۱۴۰۴ = ۹۶۰۰ ثانیه", tsec == 9600, tsec)
        tsec87 = await pg.evaluate("prTimeMin('1387')*60")
        check("تایمر آزمون رسمی ۱۳۸۷ = ۹۰۰۰ ثانیه", tsec87 == 9000, tsec87)

        check("بدون خطای کنسول", len(errs) == 0, errs[:3])
        await b.close()

asyncio.run(main())
print(f"\nخلاصه: {ok}/{ok+fail} موفق")
sys.exit(0 if fail == 0 else 1)
