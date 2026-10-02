# -*- coding: utf-8 -*-
"""
ساخت نسخه تک‌فایلی کاملاً آفلاین
- همه CSS, JS, داده‌ها و فونت به صورت inline داخل یک فایل HTML
- هیچ وابستگی بیرونی (بدون اینترنت، بدون CDN، بدون سرور)
"""
import base64, os, sys

# روی ویندوز کنسول ممکن است از یونیکد پشتیبانی نکند
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(ROOT, 'web')
FONTS = os.path.join(ROOT, 'fonts')

def read(p, enc='utf-8'):
    with open(p, encoding=enc) as f:
        return f.read()

def collect_konkur_js():
    import glob
    return sorted(glob.glob(os.path.join(WEB, 'konkur_*.js')))

def collect_book_js():
    """همه فایل‌های محتوای کتاب را به ترتیب جمع می‌کند"""
    import glob
    files = sorted(f for f in glob.glob(os.path.join(WEB, 'book_*.js'))
                   if os.path.basename(f) != 'book_reader.js')
    parts = []
    for f in files:
        parts.append(read(f))
    return "\n".join(parts), [os.path.basename(f) for f in files]


def main():
    css     = read(os.path.join(WEB, 'style.css'))
    reader  = read(os.path.join(WEB, 'book_reader.js'))
    js      = read(os.path.join(WEB, 'app.js'))
    data    = read(os.path.join(WEB, 'data.js'))
    books   = read(os.path.join(WEB, 'books.js'))
    bookjs, bookfiles = collect_book_js()
    konkurjs, konkurfiles = (None, [])
    if os.path.exists(os.path.join(WEB, "konkur_1394_95.js")):
        kf = collect_konkur_js()
        konkurjs = "\n".join(read(f) for f in kf)
        konkurfiles = [os.path.basename(f) for f in kf]
    fontcss= read(os.path.join(FONTS, 'vazirmatn-embedded.css'))
    icon   = "data:image/png;base64," + base64.b64encode(open(os.path.join(WEB,'icon-192.png'),'rb').read()).decode()

    NAV_HTML = """
<button class="nav-btn" data-view="dashboard"><span>🏠</span><span>خانه</span></button>
<button class="nav-btn" data-view="foundation"><span>🎒</span><span>پایه</span></button>
<button class="nav-btn" data-view="quiz"><span>📝</span><span>تست</span></button>
<button class="nav-btn" data-view="practice"><span>✏️</span><span>تمرین</span></button>
<button class="nav-btn" data-view="exams"><span>🎓</span><span>آزمون</span></button>
<button class="nav-btn" data-view="konkur"><span>🏛</span><span>کنکور</span></button>
<button class="nav-btn" data-view="subjects"><span>📚</span><span>درس</span></button>
<button class="nav-btn" data-view="teacher"><span>🧑‍🏫</span><span>استاد</span></button>
<button class="nav-btn" data-view="savedq"><span>💾</span><span>ذخیره</span></button>
<button class="nav-btn" data-view="bookmarks"><span>⭐</span><span>نشان</span></button>
<button class="nav-btn" data-view="freebooks"><span>🔗</span><span>کتاب</span></button>
<button class="nav-btn" data-view="settings"><span>⚙️</span><span>تنظیم</span></button>
"""

    doc = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#0f172a">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="format-detection" content="telephone=no">
<title>کنکور ارشد مهندسی پزشکی</title>
<link rel="icon" href="__ICON__">
<style>__FONT__
__CSS__</style>
</head>
<body>
<div id="app">
  <aside class="sidebar">
    <div class="brand"><div class="logo">🩺</div><div class="brand-title">مهندسی پزشکی<br><span>کنکور ارشد</span></div></div>
    <nav id="nav">__NAV__</nav>
    <div class="sidebar-stat">
      <div class="stat-title">آمار کلی</div>
      <div id="sidebar-stat-body">—</div>
    </div>
  </aside>
  <main id="main"></main>
</div>
<script>__DATA__</script>
<script>__BOOKS__</script>
<script>__BOOKJS__</script>
<script>__READER__</script>
<script>__KONKUR__</script>
<script>__JS__</script>
<script>
/* ناوبری */
document.querySelectorAll(".nav-btn").forEach(function(b){
  b.addEventListener("click", function(){
    var v = b.dataset.view;
    if(v==="quiz-playing"||v==="exam-playing"||v==="teacher-lesson"||v==="practice-playing"||v==="foundation-lesson") return;
    if(STATE.timerHandle){clearInterval(STATE.timerHandle);}
    setView(v);
  });
});
/* جلوگیری از زوم دوبار لمس */
var lastTap=0;
document.addEventListener("touchend", function(e){
  var now=Date.now();
  if(now-lastTap<300){ e.preventDefault(); }
  lastTap=now;
},{passive:false});
</script>
</body>
</html>
"""
    # اطمینان از هم‌خوانی دکمه‌های ناوبری با index.html
    import re as _re
    _nav = set(_re.findall(r'data-view=[\\]?"([a-z-]+)', NAV_HTML))
    _orig = set(_re.findall(r'data-view="([a-z-]+)"', read(os.path.join(WEB, 'index.html'))))
    _miss = sorted(_orig - _nav)
    assert not _miss, "دکمه ناوبری جا افتاده: %s" % _miss
    print("  ناوبری: %d دکمه (index.html: %d)" % (len(_nav), len(_orig)))

    doc = (doc.replace("__BOOKS__", books)
              .replace("__BOOKJS__", bookjs)
              .replace("__READER__", reader)
              .replace("__KONKUR__", konkurjs or "")
              .replace("__FONT__", fontcss)
              .replace("__CSS__", css)
              .replace("__DATA__", data)
              .replace("__JS__", js)
              .replace("__NAV__", NAV_HTML)
              .replace("__ICON__", icon))

    # ۱) نسخه تک‌فایل در ریشه پروژه
    outs = [
        os.path.join(WEB, 'bme-konkur-offline.html'),
        os.path.join(ROOT, 'bme-konkur-offline.html'),
        # ۲) assets اندروید => اپ کامل آفلاین
        os.path.join(ROOT, 'android', 'app', 'src', 'main', 'assets', 'index.html'),
        # ۳) نسخه دسکتاپ
        os.path.join(ROOT, 'desktop_app', 'web', 'index.html'),
    ]
    for o in outs:
        os.makedirs(os.path.dirname(o), exist_ok=True)
        with open(o, 'w', encoding='utf-8') as f:
            f.write(doc)
        print(f'[OK] {os.path.relpath(o, ROOT)}  ({os.path.getsize(o)/1024:.0f} KB)')

    print(f'  کتاب‌ها: {", ".join(bookfiles) if bookfiles else "هیچ"}')
    print(f'\n[DONE] Single-file offline app built: {os.path.getsize(outs[0])/1024/1024:.2f} MB')

if __name__ == '__main__':
    main()
