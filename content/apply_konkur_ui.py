# -*- coding: utf-8 -*-
"""وصل کردن بخش کنکورهای ۱۰ سال اخیر به app.js / index.html / sw.js / build_single.py"""
import os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
WEB  = os.path.join(ROOT, 'web')

# ═══════════ ۱) app.js ═══════════
p = os.path.join(WEB, 'app.js')
s = open(p, encoding='utf-8').read()

# ۱-۱) کلید کنکور در پروgress پیش‌فرض و loadProgress
s = s.replace(
    "      if(!p.exam_results) p.exam_results = [];",
    "      if(!p.exam_results) p.exam_results = [];\n      if(!p.konkur_results) p.konkur_results = {};")
s = s.replace(
    "    exam_results:[],\n    theme:\"dark\"",
    "    exam_results:[],\n    konkur_results:{},   // نتایج آزمون‌های درس‌به‌درس کنکورهای ۱۰ سال اخیر\n    theme:\"dark\"")

# ۱-۲) توابع کمکی: پشتیبانی از دروس آزمون که در APP_DATA.subjects نیستند (مثل الکترونیک)
s = s.replace(
 '''function subColor(id){const s=APP_DATA.subjects.find(x=>x.id===id);return s?s.color:"#38bdf8";}
function subName(id){const s=APP_DATA.subjects.find(x=>x.id===id);return s?s.name:"";}
function subEmoji(id){const s=APP_DATA.subjects.find(x=>x.id===id);return s?s.emoji:"📘";}''',
 '''const EXAM_META={
  math:{n:"ریاضیات",e:"📐",c:"#3b82f6"}, physics:{n:"فیزیک",e:"⚡",c:"#8b5cf6"},
  circuits:{n:"مدارهای الکتریکی",e:"🔌",c:"#f59e0b"}, electronics:{n:"الکترونیک",e:"🔧",c:"#ef4444"},
  signals:{n:"سیگنال‌ها و سیستم‌ها",e:"📡",c:"#10b981"}, control:{n:"کنترل سیستم‌ها",e:"🎛️",c:"#6366f1"},
  instrumentation:{n:"ابزار دقیق پزشکی",e:"🩺",c:"#06b6d4"}, imaging:{n:"تصویربرداری پزشکی",e:"🖼️",c:"#a855f7"},
  biomaterials:{n:"بیومواد",e:"🧪",c:"#f97316"}, biomechanics:{n:"بیومکانیک",e:"🦴",c:"#14b8a6"},
  anatomy:{n:"آناتومی و فیزیولوژی",e:"🫀",c:"#ec4899"}
};
function subColor(id){const s=APP_DATA.subjects.find(x=>x.id===id);return s?s.color:(EXAM_META[id]?EXAM_META[id].c:"#38bdf8");}
function subName(id){const s=APP_DATA.subjects.find(x=>x.id===id);if(s)return s.name;
  if(typeof PK!=="undefined"&&PK.subjects&&PK.subjects[id])return PK.subjects[id];
  return EXAM_META[id]?EXAM_META[id].n:id;}
function subEmoji(id){const s=APP_DATA.subjects.find(x=>x.id===id);if(s)return s.emoji;
  return EXAM_META[id]?EXAM_META[id].e:"📘";}''')

# ۱-۳) ثبت view های جدید
s = s.replace(
    '  else if(v==="exams") renderExamsHome(main);',
    '  else if(v==="exams") renderExamsHome(main);\n'
    '  else if(v==="konkur") renderKonkurHome(main);\n'
    '  else if(v==="konkur-year") renderKonkurYear(main);')

# ۱-۴) ثبت نتیجه در پایان آزمون کنکور
s = s.replace(
 '''function renderQuizResult(main){
  const Q=STATE.quiz;const pct=Math.round(Q.correct*100/Q.questions.length);''',
 '''function renderQuizResult(main){
  const Q=STATE.quiz;const pct=Math.round(Q.correct*100/Q.questions.length);
  // ثبت نتیجه آزمون کنکورهای ۱۰ سال اخیر
  if(Q.konkur && Q.konkur.year && Q.konkur.sid){
    const all=(STATE.progress.konkur_results||(STATE.progress.konkur_results={}));
    const key=Q.konkur.year+"__"+Q.konkur.sid;
    const prev=all[key];
    all[key]={score:Q.correct, total:Q.questions.length, date:new Date().toLocaleDateString("fa-IR"),
              best: Math.max(prev?prev.best||0:0, Q.correct), attempts:((prev&&prev.attempts)||0)+1};
    saveProgress();
  }''')

# ۱-۵) در صفحه آزمون‌ها، دکمه ورود به بخش کنکورهای ۱۰ سال
s = s.replace(
 '''  main.innerHTML=`<div class="page-head"><h1>🎓 آزمون‌های ۱۰ سال اخیر</h1><p>۶۰ دقیقه، ۲۵ سوال — با کارنامه تشریحی</p></div><div class="grid-cards" id="eg"></div>`;''',
 '''  main.innerHTML=`<div class="page-head"><h1>🎓 آزمون‌های ۱۰ سال اخیر</h1><p>۶۰ دقیقه، ۲۵ سوال — با کارنامه تشریحی</p>
    <div style="margin-top:12px"><button class="btn btn-primary" onclick="setView('konkur')">🏛 بانک کامل کنکورهای ۱۰ سال — درس به درس</button></div></div>
    <div class="section-title">📝 آزمون‌های جامع شبیه‌سازی‌شده</div><div class="grid-cards" id="eg"></div>`;''')

# ۱-۶) کارت داشبورد
s = s.replace(
 '''      <div class="card clickable" onclick="setView('exams')"><div class="emoji">🎓</div>''',
 '''      <div class="card clickable" onclick="setView('konkur')"><div class="emoji">🏛</div><h3>کنکورهای ۱۰ سال اخیر</h3><p>بانک درس‌به‌درس ۱۳۹۴ تا ۱۴۰۳ با توضیح کامل</p>
        <div class="card-actions"><button class="btn btn-primary">شروع</button></div></div>
      <div class="card clickable" onclick="setView('exams')"><div class="emoji">🎓</div>''')

# ۱-۷) افزودن کد رابط کاربری بخش کنکور، پیش از بخش init
ui = open(os.path.join(ROOT, 'content', 'konkur_ui.js'), encoding='utf-8').read()
ui = re.sub(r'/\* =+\n.*?\n=+ \*/\n', '', ui, count=1, flags=re.S)   # حذف سرصفحه توضیحی
ui = ui.replace('function pkRecordAnswer(isCorrect){', 'function __unused_pkRecord(isCorrect){')
ui = re.sub(r'function qDone\(\)\{ return pkDone\(\); \}\n?', '', ui)
assert 'function renderKonkurHome' in ui
s = s.replace('\n/* init */', '\n/* ═══ کنکورهای ۱۰ سال اخیر ═══ */\n' + ui + '\n/* init */')

open(p, 'w', encoding='utf-8').write(s)
print('✓ app.js به‌روز شد')

# ═══════════ ۲) index.html ═══════════
p = os.path.join(WEB, 'index.html')
s = open(p, encoding='utf-8').read()
old = '<script src="book_reader.js"></script>'
new = ('<script src="konkur_1394_95.js"></script>\n'
       '<script src="konkur_1396_97.js"></script>\n'
       '<script src="konkur_1398_99.js"></script>\n'
       '<script src="konkur_1400_01.js"></script>\n'
       '<script src="konkur_1402_03.js"></script>\n'
       '<script src="book_reader.js"></script>')
if 'konkur_1394_95.js' not in s:
    s = s.replace(old, new)
    print('✓ index.html: ۵ اسکریپت کنکور اضافه شد')
else:
    print('• index.html از قبل به‌روز بود')
open(p, 'w', encoding='utf-8').write(s)

# ═══════════ ۳) sw.js ═══════════
p = os.path.join(WEB, 'sw.js')
s = open(p, encoding='utf-8').read()
s = s.replace("const CACHE_NAME = 'bme-konkur-v4';", "const CACHE_NAME = 'bme-konkur-v5';")
if 'konkur_1394_95.js' not in s:
    s = s.replace("  './book_reader.js',",
        "  './book_reader.js',\n  './konkur_1394_95.js',\n  './konkur_1396_97.js',\n"
        "  './konkur_1398_99.js',\n  './konkur_1400_01.js',\n  './konkur_1402_03.js',")
    print('✓ sw.js به‌روز شد (v5 + ۵ فایل کنکور)')
open(p, 'w', encoding='utf-8').write(s)

# ═══════════ ۴) build_single.py ═══════════
p = os.path.join(ROOT, 'build_single.py')
s = open(p, encoding='utf-8').read()
if 'collect_book_js' in s and 'konkur_*.js' not in s:
    s = s.replace("""def collect_book_js():""",
"""def collect_konkur_js():
    import glob
    return sorted(glob.glob(os.path.join(WEB, 'konkur_*.js')))

def collect_book_js():""")
    # افزودن به محل استفاده
    s = re.sub(r'(\n\s*)bookjs, bookfiles = collect_book_js\(\)',
               r'\1bookjs, bookfiles = collect_book_js()\1konkurjs, konkurfiles = (None, [])\1if os.path.exists(os.path.join(WEB, "konkur_1394_95.js")):\1    kf = collect_konkur_js()\1    konkurjs = "\\n".join(read(f) for f in kf)\1    konkurfiles = [os.path.basename(f) for f in kf]', s)
    print('✓ build_single.py: تابع کنکور اضافه شد (نیاز به جای‌گذاری متغیر در قالب)')
open(p, 'w', encoding='utf-8').write(s)
print('— پایان —')
