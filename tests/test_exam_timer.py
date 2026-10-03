#!/usr/bin/env python3
"""تست حالت آزمون واقعی کنکور: تایمر ۱۶۰ دقیقه‌ای، اتمام خودکار و کارنامه زمان درسی"""
import sys
from playwright.sync_api import sync_playwright

FILE = "file:///home/user/bme_konkur/web/bme-konkur-offline.html"
fails = []
def check(name, cond, extra=""):
    print(("✅ " if cond else "❌ ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond: fails.append(name)

with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width": 430, "height": 932})
    errs = []
    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    pg.goto(FILE); pg.wait_for_timeout(1800)

    pg.evaluate("setView('konkur')"); pg.wait_for_timeout(500)
    check("دکمه حالت آزمون واقعی", "حالت آزمون واقعی" in pg.evaluate("document.querySelector('#main').innerText"))
    pg.evaluate("pkExamToggle()"); pg.wait_for_timeout(400)
    check("روشن شدن حالت آزمون", pg.evaluate("pkExamOn()") is True)

    pg.evaluate("openKonkurYear('1403')"); pg.wait_for_timeout(400)
    check("نمایش زمان ۱۶۰ دقیقه در صفحه سال", "۱۶۰ دقیقه" in pg.evaluate("document.querySelector('#main').innerText"))

    pg.evaluate("startKonkur('1403',null,false)"); pg.wait_for_timeout(1200)
    check("نمایش تایمر روی آزمون", pg.query_selector("#examTimer") is not None)
    check("محدودیت ۹۶۰۰ ثانیه (۱۶۰ دقیقه برای ۱۲۰ سوال)", pg.evaluate("STATE.quiz.exam.limit") == 9600)
    check("۱۲۰ سوال در آزمون سال", pg.evaluate("STATE.quiz.questions.length") == 120)
    t = pg.evaluate("document.querySelector('#examTimer').textContent")
    check("مقدار اولیه تایمر ≈ ۱۶۰:۰۰", "۱۶۰:۰۰" in t or "۱۵۹:" in t, t)

    for _ in range(2):
        pg.evaluate("document.querySelector('#choices .choice').click()"); pg.wait_for_timeout(250)
        pg.evaluate("$('#checkBtn').click()"); pg.wait_for_timeout(400)
        pg.evaluate("$('#nextBtn').click()"); pg.wait_for_timeout(300)
    pg.wait_for_timeout(2000)
    check("ثبت زمان به تفکیک درس", pg.evaluate("Object.keys(STATE.quiz.exam.bySub).length") >= 1)

    pg.evaluate("STATE.quiz.exam.endsAt = Date.now() + 1200")   # شبیه‌سازی اتمام زمان
    pg.on("dialog", lambda d: d.accept())
    pg.wait_for_timeout(4000)
    res = pg.evaluate("document.querySelector('#main').innerText")
    check("اتمام خودکار و نمایش کارنامه", "کارنامه آزمون واقعی" in res)
    check("گزارش زمان کل و میانگین", "زمان کل آزمون" in res and "میانگین هر سوال" in res)
    check("جدول زمان هر درس", "exam-table" in pg.evaluate("document.querySelector('#main').innerHTML"))

    pg.evaluate("setView('konkur')"); pg.wait_for_timeout(300)
    pg.evaluate("pkExamToggle()"); pg.wait_for_timeout(300)
    check("خاموش شدن حالت آزمون", pg.evaluate("pkExamOn()") is False)
    pg.evaluate("startKonkur('1402','math',false)"); pg.wait_for_timeout(600)
    check("آزمون آزاد بدون تایمر", pg.query_selector("#examTimer") is None and pg.evaluate("STATE.quiz.exam") is None)
    check("۱۵ سوال ریاضی ۱۴۰۲", pg.evaluate("STATE.quiz.questions.length") == 15)
    check("بدون خطای کنسول", len(errs) == 0, str(errs[:2]))
    b.close()

print(f"\nخلاصه: {15-len(fails)}/15 موفق")
sys.exit(1 if fails else 0)
