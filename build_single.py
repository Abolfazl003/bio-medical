# -*- coding: utf-8 -*-
"""
ساخت نسخه تک‌فایلی کاملاً آفلاین
- همه CSS, JS, داده‌ها و فونت به صورت inline داخل یک فایل HTML
- هیچ وابستگی بیرونی (بدون اینترنت، بدون CDN، بدون سرور)
"""
import base64, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(ROOT, 'web')
FONTS = os.path.join(ROOT, 'fonts')

def read(p, enc='utf-8'):
    with open(p, encoding=enc) as f:
        return f.read()

def main():
    css    = read(os.path.join(WEB, 'style.css'))
    js     = read(os.path.join(WEB, 'app.js'))
    data   = read(os.path.join(WEB, 'data.js'))
    fontcss= read(os.path.join(FONTS, 'vazirmatn-embedded.css'))
    icon   = "data:image/png;base64," + base64.b64encode(open(os.path.join(WEB,'icon-192.png'),'rb').read()).decode()

    NAV_HTML = """
<button class="nav-btn" data-view="dashboard"><span>🏠</span><span>خانه</span></button>
<button class="nav-btn" data-view="foundation"><span>🎒</span><span>پایه</span></button>
<button class="nav-btn" data-view="quiz"><span>📝</span><span>تست</span></button>
<button class="nav-btn" data-view="practice"><span>✏️</span><span>تمرین</span></button>
<button class="nav-btn" data-view="exams"><span>🎓</span><span>آزمون</span></button>
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
    doc = (doc.replace("__FONT__", fontcss)
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
        print(f'✓ {os.path.relpath(o, ROOT)}  ({os.path.getsize(o)/1024:.0f} KB)')

    print(f'\n✅ نسخه تک‌فایلی کامل ساخته شد — {os.path.getsize(outs[0])/1024/1024:.2f} MB (همه چیز داخلش هست)')

if __name__ == '__main__':
    main()
