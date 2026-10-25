# -*- coding: utf-8 -*-
"""
build_1396.py — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک) سال ۱۳۹۶
۱۳۵ سوال / ۱۶۰ دقیقه — وزارت بهداشت، درمان و آموزش پزشکی

منبع متن سوال‌ها: content/official/src_1396/q_*.py (تایپ کامل از دفترچهٔ اسکن‌شده)
کلید: کلید «اولیه» رسمی مرکز سنجش آموزش پزشکی برای هر ۱۳۵ سوال (از پاسخ‌برگ حبابی اسکن‌شده استخراج و راستی‌آزمایی شده)
شکل‌ها: web/figures_1396/*.png (واترمارک حذف شده) — به‌صورت base64 داخل JS
"""
import os, sys, json, base64, importlib, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'content', 'official', 'src_1396')
FIG = os.path.join(ROOT, 'web', 'figures_1396')
OUT = os.path.join(ROOT, 'web', 'konkur_official_1396.js')
SUBJ = ["math", "physics", "signals", "circuits", "anatomy", "english"]
MODS = ["q_math", "q_phys", "q_sig", "q_circ", "q_anat", "q_eng"]
LET = {1: "الف", 2: "ب", 3: "ج", 4: "د"}

def fig(name):
    with open(os.path.join(FIG, name), 'rb') as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode('ascii')

def strip_letters(cc):
    return [re.sub(r'^(?:الف|[abcd]|[بجد])\)\s*', '', c) for c in cc]

def load():
    sys.path.insert(0, SRC)
    Q = []
    for m, sid in zip(MODS, SUBJ):
        mod = importlib.import_module(m)
        for q in mod.Q:
            q['sid'] = sid
        Q += mod.Q
    KEY = importlib.import_module('key1396').KEY
    return Q, KEY

def head_for(no, KEY):
    """head + پاسخ بر اساس کلید اولیهٔ رسمی سنجش ۱۳۹۶ (کلید: هر ۱۲۰ سوال)"""
    k = KEY[no]
    if k == 0:  # حذف
        return "⚠️ <b>این سوال در کلید اولیهٔ سنجش حذف شد</b> — پاسخ درج‌شده صرفاً برای نمایش داده شده است.<br>", 1
    if isinstance(k, tuple):  # دو گزینهٔ صحیح
        return (f"✅ <b>کلید اولیهٔ سنجش: گزینه‌های {LET[k[0]]} و {LET[k[1]]} هر دو صحیح اعلام شده‌اند</b><br>", k[0])
    return f"✅ <b>کلید اولیهٔ سنجش: گزینهٔ {LET[k]}</b><br>", k

def build():
    Q, KEY = load()
    nos = sorted(q['no'] for q in Q)
    assert nos == list(range(1, 136)), "شماره سوال‌ها باید ۱..۱۲۰ باشد"
    S = {s: [] for s in SUBJ}
    for q in sorted(Q, key=lambda x: x['no']):
        no = q['no']
        assert len(q['c']) == 4, no
        head, a = head_for(no, KEY)
        qq, cc = q['q'], strip_letters(q['c'])
        if q['sid'] == 'english':
            qq = f'<div dir="ltr" style="text-align:left">{qq}</div>'
            cc = [f'<span dir="ltr">{c}</span>' for c in cc]
        item = {"no": no, "q": qq, "c": cc, "a": a, "k": q.get('k', ''), "s": head + q.get('s', '')}
        if q.get('img'):
            item["img"] = fig(q['img'])
        S[q['sid']].append(item)
    counts = {s: len(S[s]) for s in SUBJ}
    assert sum(counts.values()) == 135, counts
    log_args = " + ".join(f"S.{s}.length" for s in SUBJ)
    body = "\n".join(f"  S.{s} = {json.dumps(S[s], ensure_ascii=False, indent=1)};" for s in SUBJ)
    js = f"""/* ═══════════════════════════════════════════════════════════════════
   konkur_official_1396.js — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک)
   سال ۱۳۹۶ — ۱۳۵ سوال / ۱۶۰ دقیقه — وزارت بهداشت، درمان و آموزش پزشکی
   کلید: کلید اولیهٔ رسمی سنجش (۱-۱۲۰)
   تولیدشده با build_1396.py — ویرایش دستی نکنید
   ═══════════════════════════════════════════════════════════════════ */
var PKR = (typeof PKR !== "undefined" && PKR) ? PKR : {{}};
(function(){{
  const Y = "1396";
  PKR[Y] = PKR[Y] || {{}};
  const S = PKR[Y];
{body}
  if (typeof console !== "undefined") console.log("[official] 1396 loaded:", {log_args});
}})();
"""
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Created", OUT, counts, f"{os.path.getsize(OUT)//1024} KB")

if __name__ == '__main__':
    build()
