# -*- coding: utf-8 -*-
"""
build_1402.py — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک) سال ۱۴۰۲
۱۲۰ سوال / ۱۶۰ دقیقه — وزارت بهداشت، درمان و آموزش پزشکی

منبع متن سوال‌ها: content/official/src_1402/q_*.py (تایپ کامل از دفترچهٔ اسکن‌شده)
کلید: کلید «نهایی» رسمی مرکز سنجش آموزش پزشکی برای سوال‌های ۱ تا ۸۰ (سوال ۵۳ حذف شد)
زبان عمومی (۸۱-۱۲۰): کلید رسمی ندارد ⇒ حل مؤلف
شکل‌ها: web/figures_1402/*.png (واترمارک حذف شده) — به‌صورت base64 داخل JS
"""
import os, sys, json, base64, importlib

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'content', 'official', 'src_1402')
FIG = os.path.join(ROOT, 'web', 'figures_1402')
OUT = os.path.join(ROOT, 'web', 'konkur_official_1402.js')
SUBJ = ["math", "physics", "signals", "control", "circuits", "anatomy", "english"]
LET = {1: "الف", 2: "ب", 3: "ج", 4: "د"}

def fig(name):
    with open(os.path.join(FIG, name), 'rb') as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode('ascii')

def load():
    sys.path.insert(0, SRC)
    qm = importlib.import_module('q_math')
    for m in ('q_phys', 'q_sig', 'q_ctrl', 'q_circ', 'q_anat', 'q_eng'):
        importlib.import_module(m)
    KEY = importlib.import_module('key1402').KEY
    return qm.Q, KEY

def build():
    Q, KEY = load()
    nos = sorted(q['no'] for q in Q)
    assert nos == list(range(1, 121)), "شماره سوال‌ها باید ۱..۱۲۰ باشد"
    S = {s: [] for s in SUBJ}
    for q in sorted(Q, key=lambda x: x['no']):
        no, a = q['no'], q['a']
        assert a in (1, 2, 3, 4) and len(q['c']) == 4, no
        if no <= 80:
            if KEY[no] is None:
                head = "⚠️ <b>این سوال در کلید نهایی سنجش حذف شد</b> — پاسخ درج‌شده حل مؤلف است.<br>"
            else:
                assert KEY[no] == a, f"Q{no}: پاسخ با کلید رسمی نمی‌خواند"
                head = f"✅ <b>کلید نهایی سنجش: گزینهٔ {LET[a]}</b><br>"
        else:
            head = f"✍️ <b>حل مؤلف: گزینهٔ {LET[a]}</b> (برای زبان عمومی کلید رسمی منتشر نشده)<br>"
        qq, cc = q['q'], q['c']
        if q['sid'] == 'english':
            qq = f'<div dir="ltr" style="text-align:left">{qq}</div>'
            cc = [f'<span dir="ltr">{c}</span>' for c in cc]
        item = {"no": no, "q": qq, "c": cc, "a": a, "k": q.get('k', ''), "s": head + q['s']}
        if q.get('img'):
            item["img"] = fig(q['img'])
        S[q['sid']].append(item)
    body = "\n".join(f"  S.{s} = {json.dumps(S[s], ensure_ascii=False, indent=1)};" for s in SUBJ)
    js = f"""/* ═══════════════════════════════════════════════════════════════════
   konkur_official_1402.js — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک)
   سال ۱۴۰۲ — ۱۲۰ سوال / ۱۶۰ دقیقه — وزارت بهداشت، درمان و آموزش پزشکی
   کلید: کلید نهایی رسمی سنجش (۱-۸۰؛ سوال ۵۳ حذف) — زبان (۸۱-۱۲۰): حل مؤلف
   تولیدشده با build_1402.py — ویرایش دستی نکنید
   ═══════════════════════════════════════════════════════════════════ */
var PKR = (typeof PKR !== "undefined" && PKR) ? PKR : {{}};
(function(){{
  const Y = "1402";
  PKR[Y] = PKR[Y] || {{}};
  const S = PKR[Y];
{body}
  if (typeof console !== "undefined") console.log("[official] 1402 loaded:", {' + "+" + '.join(f'S.{s}.length' for s in SUBJ)});
}})();
"""
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Created", OUT, {s: len(S[s]) for s in SUBJ}, f"{os.path.getsize(OUT)//1024} KB")

if __name__ == '__main__':
    build()
