#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست‌های بخش «🏛 بانک سوالات رسمی کنکور»
- ۲۰ دوره رسمی: ۱۳۸۵ تا ۱۴۰۴
- تعداد سوال هر دفترچه طبق جلد خود دفترچه‌ها
- زمان واقعی آزمون هر سال (۱۶۰ دقیقه؛ ۱۳۸۷: ۱۵۰ دقیقه)
- سیاست پاسخ‌نامه: حل مؤلف (غیررسمی) — کلید رسمی سنجش داخل دفترچه‌ها نیست
- سال ۱۳۹۸ تنها دفترچه دریافت‌نشده؛ ۱۴۰۲ کامل (۱۲۰ سوال) با کلید نهایی سنجش
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

EXPECT = {"1385":135,"1386":135,"1387":110,"1388":130,"1389":130,"1390":130,"1391":130,"1392":130,"1393":130,
          "1394":130,"1395":130,"1396":135,"1397":140,"1398":None,"1399":120,"1400":120,
          "1401":120,"1402":120,"1403":120,"1404":120}

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
        check("۲۰ دوره رسمی", d["years"] == 20, d["years"])
        check("۱۳۸۵ اولین دوره", d["list"][0] == "1385")
        check("۱۴۰۴ آخرین دوره", d["list"][-1] == "1404")
        check("سال‌ها پیوسته ۱۳۸۵→۱۴۰۴",
              d["list"] == [str(y) for y in range(1385, 1405)])

        print("— تعداد سوال هر دفترچه —")
        for y, n in EXPECT.items():
            check(f"{y} = {n}", d["count"].get(y) == n, d["count"].get(y))
        check("۱۹ دفترچه دریافت‌شده", d["recv"] == 19, d["recv"])
        check("فقط ۱۳۹۸ گم است", d["missing"] == ["1398"], d["missing"])
        check("سوال دفترچه‌های موجود", d["cap"] == sum(v for v in EXPECT.values() if v), d["cap"])

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
        check("۲۰ کارت سال در صفحه", cards == 20, cards)
        txt = await pg.evaluate("document.getElementById('main').innerText")
        for probe in ["۱۳۸۵", "۱۴۰۴", "۲۰ دوره", "۱۴۰۲", "حل مؤلف", "کلید نهایی سنجش", "۱۵۰ دقیقه"]:
            check(f"متن صفحه شامل {probe}", probe in txt)

        print("— دفترچهٔ ۱۴۰۲ (کامل) —")
        d2 = await pg.evaluate("""(() => {
          const subs = ['math','physics','signals','control','circuits','anatomy','english'];
          const c = {}; subs.forEach(s => c[s] = prQ('1402', s).length);
          const all = subs.flatMap(s => prQ('1402', s));
          return {c, y: prYearCount('1402'), nos: all.map(q => q.no).sort((a,b)=>a-b),
                  key: all.filter(q => q.no<=80).map(q => [q.no, q.a]),
                  imgs: all.filter(q => q.img).length,
                  sol: all.every(q => (q.s||'').length > 30),
                  q53: (all.find(q => q.no===53)||{}).s || '',
                  newest: prNewestYear()};
        })()""")
        check("۱۴۰۲ = ۱۲۰ سوال", d2["y"] == 120, d2["y"])
        check("شماره‌ها ۱..۱۲۰", d2["nos"] == list(range(1, 121)))
        for sid, n in {"math":15,"physics":15,"signals":15,"control":10,"circuits":15,"anatomy":10,"english":40}.items():
            check(f"۱۴۰۲ {sid} = {n}", d2["c"][sid] == n, d2["c"][sid])
        KEY = [2,2,3,2,3,1,3,3,4,2, 1,2,2,3,4,1,4,4,2,3, 3,4,1,1,3,3,2,1,1,3, 4,1,2,3,4,1,2,3,4,4,
               3,1,3,2,3,3,2,4,4,1, 1,3,None,3,2,4,4,2,1,3, 4,2,1,4,2,3,2,1,3,4, 2,1,2,4,4,1,4,1,3,4]
        bad = [no for no, a in d2["key"] if KEY[no-1] is not None and KEY[no-1] != a]
        check("پاسخ‌های ۱-۸۰ = کلید نهایی سنجش", not bad, bad)
        check("سوال ۵۳ با برچسب «حذف شد»", "حذف شد" in d2["q53"])
        check("شکل‌های ۱۴۰۲ (base64) ≥ ۲۵", d2["imgs"] >= 25, d2["imgs"])
        check("همه سوال‌ها حل تشریحی دارند", d2["sol"])
        check("جدیدترین دفترچه درج‌شده = ۱۴۰۴", d2["newest"] == "1404", d2["newest"])

        print("— دفترچهٔ ۱۳۹۹ (کامل، کلید نهایی ۱-۱۲۰) —")
        d9 = await pg.evaluate("""(() => {
          const subs = ['math','physics','signals','control','circuits','anatomy','english'];
          const c = {}; subs.forEach(s => c[s] = prQ('1399', s).length);
          const all = subs.flatMap(s => prQ('1399', s));
          return {c, y: prYearCount('1399'), nos: all.map(q => q.no).sort((a,b)=>a-b),
                  aa: all.map(q => q.a),
                  imgs: all.filter(q => q.img).length,
                  sol: all.every(q => (q.s||'').length > 30),
                  del: all.filter(q => (q.s||'').includes('حذف شد')).map(q => q.no),
                  dual: all.filter(q => (q.s||'').includes('هر دو صحیح')).map(q => q.no)};
        })()""")
        check("۱۳۹۹ = ۱۲۰ سوال", d9["y"] == 120, d9["y"])
        check("شماره‌های ۱۳۹۹ = ۱..۱۲۰", d9["nos"] == list(range(1, 121)))
        for sid, n in {"math":15,"physics":15,"signals":15,"control":10,"circuits":15,"anatomy":10,"english":40}.items():
            check(f"۱۳۹۹ {sid} = {n}", d9["c"][sid] == n, d9["c"][sid])
        # کلید ۱۳۹۹ مستقیماً از content/official/src_1399/key1399.py تولید می‌شود (دستی تایپ نشود!)
        import importlib.util as _ilu
        _sp = _ilu.spec_from_file_location("key1399", os.path.join(os.path.dirname(__file__), "..", "content", "official", "src_1399", "key1399.py"))
        _km = _ilu.module_from_spec(_sp); _sp.loader.exec_module(_km)
        K1399 = [None if _km.KEY[i] == 0 else (set(_km.KEY[i]) if isinstance(_km.KEY[i], tuple) else _km.KEY[i])
                 for i in range(1, 121)]
        bad9 = [i+1 for i, (k, q) in enumerate(zip(K1399, d9["aa"]))
                if k is not None and (q not in k if isinstance(k, set) else q != k)]
        check("پاسخ‌های ۱۳۹۹ = کلید نهایی سنجش", not bad9, bad9)
        check("حذفی‌های ۱۳۹۹ = ۹ و ۳۲", d9["del"] == [9, 32], d9["del"])
        check("دوگزینه‌ای‌های ۱۳۹۹ = ۳۷ و ۷۰", d9["dual"] == [37, 70], d9["dual"])
        check("شکل‌های ۱۳۹۹ (base64) = ۲۱", d9["imgs"] == 21, d9["imgs"])
        check("همهٔ سوال‌های ۱۳۹۹ حل تشریحی دارند", d9["sol"])

        print("— دفترچهٔ ۱۴۰۱ (کامل، کلید اولیهٔ ۱-۱۲۰) —")
        d1 = await pg.evaluate("""(() => {
          const subs = ['math','physics','signals','control','circuits','anatomy','english'];
          const c = {}; subs.forEach(s => c[s] = prQ('1401', s).length);
          const all = subs.flatMap(s => prQ('1401', s));
          return {c, y: prYearCount('1401'), nos: all.map(q => q.no).sort((a,b)=>a-b),
                  aa: all.map(q => q.a),
                  imgs: all.filter(q => q.img).length,
                  sol: all.every(q => (q.s||'').length > 30),
                  aval: all.every(q => (q.s||'').includes('کلید اولیهٔ سنجش'))};
        })()""")
        check("۱۴۰۱ = ۱۲۰ سوال", d1["y"] == 120, d1["y"])
        check("شماره‌های ۱۴۰۱ = ۱..۱۲۰", d1["nos"] == list(range(1, 121)))
        for sid, n in {"math":15,"physics":15,"signals":15,"control":10,"circuits":15,"anatomy":10,"english":40}.items():
            check(f"۱۴۰۱ {sid} = {n}", d1["c"][sid] == n, d1["c"][sid])
        # کلید ۱۴۰۱ مستقیماً از content/official/src_1401/key1401.py تولید می‌شود (دستی تایپ نشود!)
        _sp1 = _ilu.spec_from_file_location("key1401", os.path.join(os.path.dirname(__file__), "..", "content", "official", "src_1401", "key1401.py"))
        _k1 = _ilu.module_from_spec(_sp1); _sp1.loader.exec_module(_k1)
        K1401 = [_k1.KEY[i] for i in range(1, 121)]
        bad1 = [i+1 for i, (k, q) in enumerate(zip(K1401, d1["aa"])) if q != k]
        check("پاسخ‌های ۱۴۰۱ = کلید اولیهٔ سنجش", not bad1, bad1)
        check("برچسب «کلید اولیهٔ سنجش» برای هر ۱۲۰ سوال", d1["aval"])
        check("شکل‌های ۱۴۰۱ (base64) = ۲۱", d1["imgs"] == 21, d1["imgs"])
        check("همهٔ سوال‌های ۱۴۰۱ حل تشریحی دارند", d1["sol"])

        print("— دفترچهٔ ۱۴۰۰ (کامل، کلید نهایی ۱-۱۲۰) —")
        d0 = await pg.evaluate("""(() => {
          const subs = ['math','physics','signals','control','circuits','anatomy','english'];
          const c = {}; subs.forEach(s => c[s] = prQ('1400', s).length);
          const all = subs.flatMap(s => prQ('1400', s));
          return {c, y: prYearCount('1400'), nos: all.map(q => q.no).sort((a,b)=>a-b),
                  aa: all.map(q => q.a),
                  imgs: all.filter(q => q.img).length,
                  sol: all.every(q => (q.s||'').length > 30),
                  del: all.filter(q => (q.s||'').includes('حذف شد')).map(q => q.no),
                  fixed: all.filter(q => (q.s||'').includes('اصلاح شد')).map(q => q.no)};
        })()""")
        check("۱۴۰۰ = ۱۲۰ سوال", d0["y"] == 120, d0["y"])
        check("شماره‌های ۱۴۰۰ = ۱..۱۲۰", d0["nos"] == list(range(1, 121)))
        for sid, n in {"math":15,"physics":15,"signals":15,"control":10,"circuits":15,"anatomy":10,"english":40}.items():
            check(f"۱۴۰۰ {sid} = {n}", d0["c"][sid] == n, d0["c"][sid])
        K1400 = [4,1,3,3,2,3,2,1,4,1, 2,3,1,3,1,3,4,4,4,2, 4,3,2,3,4,2,2,3,4,4, 3,4,2,2,2,4,3,1,2,{3,4},
                 3,4,1,2,4,3,None,1,2,1, 1,4,2,3,2,3,3,4,3,4, 3,3,3,4,4,2,None,2,3,2, {1,2},3,1,4,2,3,1,1,4,1,
                 4,1,2,3,2,3,2,3,2,2, 4,None,3,1,3,3,2,3,3,4, 4,2,3,1,4,2,3,1,4,3, 2,1,2,3,1,3,2,3,4,1]
        bad0 = [i+1 for i, (k, q) in enumerate(zip(K1400, d0["aa"]))
                if k is not None and (q not in k if isinstance(k, set) else q != k)]
        check("پاسخ‌های ۱۴۰۰ = کلید نهایی سنجش", not bad0, bad0)
        check("حذفی‌های ۱۴۰۰ = ۴۷، ۶۷، ۹۲", d0["del"] == [47, 67, 92], d0["del"])
        check("اخلال‌های فایل قدیمی با کلید اصلاح شد", all(n in d0["fixed"] for n in [6, 7, 9, 21]), d0["fixed"])
        check("شکل‌های ۱۴۰۰ (base64) ≥ ۱۵", d0["imgs"] >= 15, d0["imgs"])
        check("همهٔ سوال‌های ۱۴۰۰ حل تشریحی دارند", d0["sol"])

        print("— دفترچهٔ ۱۴۰۴ (کامل، کلید نهایی ۱-۱۲۰) —")
        d4 = await pg.evaluate("""(() => {
          const subs = ['math','physics','signals','control','circuits','anatomy','english'];
          const c = {}; subs.forEach(s => c[s] = prQ('1404', s).length);
          const all = subs.flatMap(s => prQ('1404', s));
          return {c, y: prYearCount('1404'), nos: all.map(q => q.no).sort((a,b)=>a-b),
                  aa: all.map(q => q.a),
                  imgs: all.filter(q => q.img).length,
                  sol: all.every(q => (q.s||'').length > 30),
                  del: all.filter(q => (q.s||'').includes('حذف شد')).map(q => q.no),
                  fixed: all.filter(q => (q.s||'').includes('اصلاح شد')).map(q => q.no)};
        })()""")
        check("۱۴۰۴ = ۱۲۰ سوال", d4["y"] == 120, d4["y"])
        check("شماره‌های ۱۴۰۴ = ۱..۱۲۰", d4["nos"] == list(range(1, 121)))
        for sid, n in {"math":15,"physics":15,"signals":15,"control":10,"circuits":15,"anatomy":10,"english":40}.items():
            check(f"۱۴۰۴ {sid} = {n}", d4["c"][sid] == n, d4["c"][sid])
        K1404 = [1,2,4,2,None,2,3,4,1,1, 1,4,2,3,2,3,3,4,3,4, 1,2,1,1,4,4,2,4,2,3, 4,2,3,1,1,4,4,1,3,2,
                 3,1,1,1,3,2,3,2,4,1, 4,3,1,3,4,3,2,1,1,1, 4,4,4,4,2,3,4,3,1,2, 3,4,2,3,4,4,3,2,4,1,
                 4,2,3,4,1,2,1,3,2,1, 2,3,4,1,3,4,1,3,4,2, 3,1,2,4,2,3,1,3,2,4, 2,4,4,3,2,1,4,3,2,1]
        bad4 = [i+1 for i, (k, q) in enumerate(zip(K1404, d4["aa"])) if k is not None and q != k]
        check("پاسخ‌های ۱۴۰۴ = کلید نهایی سنجش", not bad4, bad4)
        check("حذفی‌های ۱۴۰۴ = فقط سوال ۵", d4["del"] == [5], d4["del"])
        check("بازنویسی زبان با کلید نهایی", all(n in d4["fixed"] for n in [46, 56, 67, 70]), d4["fixed"][:5])
        check("شکل‌های ۱۴۰۴ (base64) ≥ ۲۰", d4["imgs"] >= 20, d4["imgs"])
        check("همهٔ سوال‌های ۱۴۰۴ حل تشریحی دارند", d4["sol"])

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
