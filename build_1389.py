# -*- coding: utf-8 -*-
"""build_1389.py — اسمبل بانک سؤال رسمی ۱۳۸۹ (۱۳۰ سؤال / ۱۶۰ دقیقه)."""
import json, os, base64, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from q89_circuits import CIRCUITS
from q89_elec import ELEC
from q89_math import MATH
from q89_physics import PHYSICS
from q89_sig_anat import SIGNALS, ANATOMY
from q89_english import ENGLISH

FIGDIR = os.path.join(ROOT, 'web', 'figures_1389')

def get_fig(fname):
    p = os.path.join(FIGDIR, fname)
    with open(p, 'rb') as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode('ascii')

questions = CIRCUITS + ELEC + MATH + PHYSICS + SIGNALS + ANATOMY + ENGLISH
by_subject = {'math': [], 'physics': [], 'signals': [], 'circuits': [],
              'electronics': [], 'anatomy': [], 'english': []}
for q in questions:
    item = {"no": q['no'], "q": q['q'], "c": q['c'], "a": q['a'], "exp": q['exp']}
    if 'figure' in q:
        item["img"] = get_fig(q['figure'])
    by_subject[q['subject']].append(item)

for s, qs in by_subject.items():
    qs.sort(key=lambda x: x['no'])
    print(f"  {s}: {len(qs)}  ({qs[0]['no'] if qs else '-'}..{qs[-1]['no'] if qs else '-'})")
total = sum(len(v) for v in by_subject.values())
print(f"Total: {total} / 130")
allnos = sorted(q['no'] for q in questions)
assert allnos == list(range(1, 131)), f"numbering gap: {[i for i in range(1,131) if i not in allnos]}"
assert total == 130

js = f"""/* ═══════════════════════════════════════════════════════════════════
   konkur_official_1389.js — دفترچه رسمی کنکور ارشد مهندسی پزشکی
   سال ۱۳۸۹ — ۱۳۰ سوال / ۱۶۰ دقیقه — وزارت بهداشت، درمان و آموزش پزشکی
   مدار ۱–۱۵ | الکترونیک ۱۶–۳۰ | ریاضی ۳۱–۴۵ | فیزیک ۴۶–۶۰ | سیگنال ۶۱–۷۸ |
   آناتومی ۷۹–۹۰ (۷۹–۸۴ به‌دلیل نبود صفحه در اسکن: placeholder) | زبان ۹۱–۱۳۰
   ⚠️ بدون کلید رسمی؛ پاسخ‌ها حل تحلیلی + تأیید محاسباتی (موارد مشکوک در راهنما ⚠️).
   ═══════════════════════════════════════════════════════════════════ */
var PKR = (typeof PKR !== "undefined" && PKR) ? PKR : {{}};
(function(){{
  const Y = "1389";
  PKR[Y] = PKR[Y] || {{}};
  const S = PKR[Y];
  S.math = {json.dumps(by_subject['math'], ensure_ascii=False, indent=2)};
  S.physics = {json.dumps(by_subject['physics'], ensure_ascii=False, indent=2)};
  S.signals = {json.dumps(by_subject['signals'], ensure_ascii=False, indent=2)};
  S.circuits = {json.dumps(by_subject['circuits'], ensure_ascii=False, indent=2)};
  S.electronics = {json.dumps(by_subject['electronics'], ensure_ascii=False, indent=2)};
  S.anatomy = {json.dumps(by_subject['anatomy'], ensure_ascii=False, indent=2)};
  S.english = {json.dumps(by_subject['english'], ensure_ascii=False, indent=2)};
  if (typeof console !== "undefined") console.log("[official] 1389 loaded:", S.math.length+"+"+S.physics.length+"+"+S.signals.length+"+"+S.circuits.length+"+"+S.electronics.length+"+"+S.anatomy.length+"+"+S.english.length, "سوال رسمی");
}})();
"""
out = os.path.join(ROOT, 'web', 'konkur_official_1389.js')
with open(out, 'w', encoding='utf-8') as f:
    f.write(js)
print("Created web/konkur_official_1389.js —", round(len(js)/1024), "KB")
