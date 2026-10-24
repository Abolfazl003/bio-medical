# -*- coding: utf-8 -*-
"""
build_1400.py — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک) سال ۱۴۰۰
۱۲۰ سوال — وزارت بهداشت، درمان و آموزش پزشکی

۱-۴۹: از فایل دستی قبلی (konkur_official_1400.js قدیمی) بازیابی و به ۱-based تبدیل می‌شود
۵۰-۱۲۰: تایپ کامل از دفترچه (content/official/src_1400/q_*.py)
کلید: کلید نهایی رسمی سنجش (۱-۱۲۰؛ حذف‌شده: ۴۷، ۶۷، ۹۲ — دوگزینه‌ای: ۴۰ و ۷۱)
شکل‌ها: web/figures_1400/*.png (واترمارک حذف شده) — به‌صورت base64 داخل JS
"""
import os, sys, json, base64, importlib, subprocess, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'content', 'official', 'src_1400')
FIG = os.path.join(ROOT, 'web', 'figures_1400')
OUT = os.path.join(ROOT, 'web', 'konkur_official_1400.js')
SUBJ = ["math", "physics", "signals", "control", "circuits", "anatomy", "english"]
LET = {1: "الف", 2: "ب", 3: "ج", 4: "د"}

def fig(name):
    with open(os.path.join(FIG, name), 'rb') as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode('ascii')

def strip_letters(cc):
    out = []
    for c in cc:
        out.append(re.sub(r'^(?:الف|[abcd]|[بجد])\)\s*', '', c))
    return out

def load_old():
    """خروجی گرفتن از فایل دستی قدیمی با node (a صفر-مبنا است)"""
    node_code = (
        "const fs=require('fs');const L=console.log;console.log=()=>{};"
        "eval(fs.readFileSync(process.argv[1],'utf8'));"
        "process.stdout.write(JSON.stringify(PKR['1400']));")
    n = 0
    js_path = os.path.join(ROOT, 'content', 'official', 'src_1400', 'legacy_1400_49q.js')
    out = subprocess.run(['node', '-e', node_code, js_path], capture_output=True, text=True, check=True).stdout
    old = json.loads(out)
    items = []
    for sid in ("math", "physics", "signals", "control"):
        for q in old.get(sid, []):
            a0 = q['a']
            assert 0 <= a0 <= 3, (sid, q['no'], a0)
            items.append(dict(no=q['no'], sid=sid, q=q['q'], c=q['c'], a=a0 + 1,
                              s=q.get('s', ''), k=q.get('k', ''), img=None))
    return items

def load_new():
    sys.path.insert(0, SRC)
    mod = importlib.import_module('q_ctrl')
    importlib.import_module('q_circ'); importlib.import_module('q_anat'); importlib.import_module('q_eng')
    KEY = importlib.import_module('key1400').KEY
    return mod.Q, KEY

def head_for(no, a, KEY):
    """head + پاسخ نهایی بر اساس کلید رسمی"""
    k = KEY[no]
    if k == 0:  # حذف
        return "⚠️ <b>این سوال در کلید نهایی سنجش حذف شد</b> — پاسخ درج‌شده صرفاً برای نمایش داده شده است.<br>", a, False
    if isinstance(k, list):
        a2 = a if a in k else k[0]
        head = (f"✅ <b>کلید نهایی سنجش: گزینه‌های {LET[k[0]]} و {LET[k[1]]} هر دو صحیح اعلام شده‌اند</b>"
                + ("" if a in k else f" (پاسخ درج‌شده به {LET[k[0]]} اصلاح شد)") + "<br>")
        return head, a2, a not in k
    if a != k:
        return (f"✅ <b>کلید نهایی سنجش: گزینهٔ {LET[k]}</b> (پاسخ قبلی به کلید نهایی اصلاح شد)<br>", k, True)
    return f"✅ <b>کلید نهایی سنجش: گزینهٔ {LET[k]}</b><br>", a, False

def build():
    Q, KEY = load_new()
    old = load_old()
    nos_new = sorted(q['no'] for q in Q)
    assert nos_new == list(range(50, 121))
    items = old + Q
    nos = sorted(q['no'] for q in items)
    assert nos == list(range(1, 121)), "شماره سوال‌ها باید ۱..۱۲۰ باشد"

    S = {s: [] for s in SUBJ}
    fixed = []
    for q in sorted(items, key=lambda x: x['no']):
        no, a = q['no'], q['a']
        assert a in (1, 2, 3, 4) and len(q['c']) == 4, no
        head, a, was_fixed = head_for(no, a, KEY)
        if was_fixed:
            fixed.append(no)
        qq, cc = q['q'], strip_letters(q['c'])
        if q['sid'] == 'english':
            qq = f'<div dir="ltr" style="text-align:left">{qq}</div>'
            cc = [f'<span dir="ltr">{c}</span>' for c in cc]
        item = {"no": no, "q": qq, "c": cc, "a": a, "k": q.get('k', ''), "s": head + q.get('s', '')}
        if q.get('img'):
            item["img"] = fig(q['img'])
        S[q['sid']].append(item)
    print("اصلاح‌شده با کلید نهایی:", fixed)
    counts = {s: len(S[s]) for s in SUBJ}
    assert sum(counts.values()) == 120, counts
    log_args = " + ".join(f"S.{s}.length" for s in SUBJ)
    body = "\n".join(f"  S.{s} = {json.dumps(S[s], ensure_ascii=False, indent=1)};" for s in SUBJ)
    js = f"""/* ═══════════════════════════════════════════════════════════════════
   konkur_official_1400.js — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک)
   سال ۱۴۰۰ — ۱۲۰ سوال — وزارت بهداشت، درمان و آموزش پزشکی
   کلید: کلید نهایی رسمی سنجش (۱-۱۲۰؛ حذف‌شده: ۴۷ و ۶۷ و ۹۲ — هر دو گزینه: ۴۰ و ۷۱)
   تولیدشده با build_1400.py — ویرایش دستی نکنید
   ═══════════════════════════════════════════════════════════════════ */
var PKR = (typeof PKR !== "undefined" && PKR) ? PKR : {{}};
(function(){{
  const Y = "1400";
  PKR[Y] = PKR[Y] || {{}};
  const S = PKR[Y];
{body}
  if (typeof console !== "undefined") console.log("[official] 1400 loaded:", {log_args});
}})();
"""
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Created", OUT, counts, f"{os.path.getsize(OUT)//1024} KB")

if __name__ == '__main__':
    build()
