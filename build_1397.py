# -*- coding: utf-8 -*-
"""
build_1397.py — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک) سال ۱۳۹۷
۱۴۰ سوال / ۱۶۰ دقیقه — وزارت بهداشت، درمان و آموزش پزشکی

منبع متن سوال‌ها: content/official/src_1397/q_*.py (تایپ کامل از دفترچهٔ اسکن‌شده)
کلید: کلید رسمی سنجش برای ۱۳۹۷ در آرشیوها یافت نشد — پاسخ‌ها «حل مؤلف (غیررسمی)»اند
شکل‌ها: web/figures_1397/*.png — به‌صورت base64 داخل JS
"""
import os, sys, json, base64, importlib, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'content', 'official', 'src_1397')
FIG = os.path.join(ROOT, 'web', 'figures_1397')
OUT = os.path.join(ROOT, 'web', 'konkur_official_1397.js')
SUBJ = ["math", "physics", "signals", "control", "circuits", "anatomy", "english"]
MODS = ["q_math", "q_phys", "q_sig", "q_ctrl", "q_circ", "q_anat", "q_eng"]
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
    KEY = importlib.import_module('key1397').KEY
    return Q, KEY

def head_for(no, KEY):
    k = KEY[no]
    return (f"📝 <b>حل مؤلف (غیررسمی): گزینهٔ {LET[k]}</b> — کلید رسمی سنجش برای ۱۳۹۷ منتشر/یافت نشده است؛ "
            f"این پاسخ بر اساس حل تیمی است.<br>"), k

def build():
    Q, KEY = load()
    nos = sorted(q['no'] for q in Q)
    assert nos == list(range(1, 141)), "شماره سوال‌ها باید ۱..۱۴۰ باشد"
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
    assert sum(counts.values()) == 140, counts
    log_args = " + ".join(f"S.{s}.length" for s in SUBJ)
    body = "\n".join(f"  S.{s} = {json.dumps(S[s], ensure_ascii=False, indent=1)};" for s in SUBJ)
    js = f"""/* ═══════════════════════════════════════════════════════════════════
   konkur_official_1397.js — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک)
   سال ۱۳۹۷ — ۱۴۰ سوال / ۱۶۰ دقیقه — وزارت بهداشت، درمان و آموزش پزشکی
   کلید: حل مؤلف (غیررسمی) — کلید رسمی سنجش ۱۳۹۷ در هیچ آرشیوی یافت نشد (۱-۱۴۰)
   تولیدشده با build_1397.py — ویرایش دستی نکنید
   ═══════════════════════════════════════════════════════════════════ */
var PKR = (typeof PKR !== "undefined" && PKR) ? PKR : {{}};
(function(){{
  const Y = "1397";
  PKR[Y] = PKR[Y] || {{}};
  const S = PKR[Y];
{body}
  if (typeof console !== "undefined") console.log("[official] 1397 loaded:", {log_args});
}})();
"""
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Created", OUT, counts, f"{os.path.getsize(OUT)//1024} KB")

if __name__ == '__main__':
    build()
