# -*- coding: utf-8 -*-
"""
build_1404.py — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک) سال ۱۴۰۴
۱۲۰ سوال — وزارت بهداشت، درمان و آموزش پزشکی

۱-۹۰: از فایل دستی قبلی (legacy_1404_90q.js — a صفر-مبنا) بازیابی می‌شود
۸۸-۱۲۰ زبان: تایپ/اصلاح از روی متن دفترچهٔ دارای لایهٔ متنی (src_1404/q_eng.py)
کلید: کلید نهایی رسمی مرکز سنجش (۱-۱۲۰؛ سوال ۵ حذف شد)
تفاوت‌ها با پاسخ‌های قدیمی (عمدتاً بر پایهٔ کلید اولیه) با برچسب «اصلاح شد» ثبت می‌شود.
"""
import os, sys, json, importlib, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'content', 'official', 'src_1404')
OUT = os.path.join(ROOT, 'web', 'konkur_official_1404.js')
SUBJ = ["math", "physics", "signals", "control", "circuits", "anatomy", "english"]
LET = {1: "الف", 2: "ب", 3: "ج", 4: "د"}

def load_old():
    node_code = (
        "const fs=require('fs');const L=console.log;console.log=()=>{};"
        "eval(fs.readFileSync(process.argv[1],'utf8'));"
        "process.stdout.write(JSON.stringify(PKR['1404']));")
    js_path = os.path.join(ROOT, 'content', 'official', 'src_1404', 'legacy_1404_90q.js')
    out = subprocess.run(['node', '-e', node_code, js_path], capture_output=True, text=True, check=True).stdout
    old = json.loads(out)
    items = []
    for sid in SUBJ:
        for q in old.get(sid, []):
            items.append(dict(no=q['no'], sid=sid, q=q['q'], c=q['c'], a=q['a'] + 1,
                              s=q.get('s', ''), k=q.get('k', ''), tips=q.get('tips', ''), img=q.get('img')))
    # تمام aها صفر-مبنا بودند؟ کنترل: باید حداقل یک a=0 داشته باشد
    assert any(q['a'] == 1 for q in items) and all(1 <= q['a'] <= 4 for q in items)
    return items

def head_for(no, a, KEY):
    k = KEY[no]
    if k == 0 or k is None:
        return "⚠️ <b>این سوال در کلید نهایی سنجش حذف شد</b> — پاسخ درج‌شده صرفاً برای نمایش داده شده است.<br>", a, False
    if a != k:
        return f"✅ <b>کلید نهایی سنجش: گزینهٔ {LET[k]}</b> (پاسخ قبلی به کلید نهایی اصلاح شد)<br>", k, True
    return f"✅ <b>کلید نهایی سنجش: گزینهٔ {LET[k]}</b><br>", a, False

def build():
    sys.path.insert(0, SRC)
    qe = importlib.import_module('q_eng')
    KEY = importlib.import_module('key1404').KEY
    new_eng = {q['no']: q for q in qe.Q}
    assert sorted(new_eng) == list(range(88, 121))

    old = load_old()
    items = []
    for q in old:
        if q['sid'] == 'english' and q['no'] >= 88:
            continue  # ۸۸-۱۲۰ تازه از q_eng می‌آید (۸۸-۹۰ هم بازنویسی شده)
        items.append(q)
    items.extend(new_eng[n] for n in sorted(new_eng))
    assert sorted(q['no'] for q in items) == list(range(1, 121))

    S = {s: [] for s in SUBJ}
    fixed = []
    for q in sorted(items, key=lambda x: x['no']):
        no, a = q['no'], q['a']
        assert a in (1, 2, 3, 4) and len(q['c']) == 4, no
        head, a, was_fixed = head_for(no, a, KEY)
        if was_fixed:
            fixed.append(no)
        qq, cc = q['q'], q['c']
        if q['sid'] == 'english':
            qq = f'<div dir="ltr" style="text-align:left">{qq}</div>'
            cc = [f'<span dir="ltr">{c}</span>' for c in cc]
        item = {"no": no, "q": qq, "c": cc, "a": a, "k": q.get('k', ''), "s": head + q.get('s', '')}
        if q.get('tips'):
            item['tips'] = q['tips']
        if q.get('img'):
            item["img"] = q['img']
        S[q['sid']].append(item)
    print("اصلاح‌شده با کلید نهایی:", fixed)
    counts = {s: len(S[s]) for s in SUBJ}
    assert sum(counts.values()) == 120, counts
    log_args = " + ".join(f"S.{s}.length" for s in SUBJ)
    body = "\n".join(f"  S.{s} = {json.dumps(S[s], ensure_ascii=False, indent=1)};" for s in SUBJ)
    js = f"""/* ═══════════════════════════════════════════════════════════════════
   konkur_official_1404.js — دفترچه رسمی کنکور ارشد مهندسی پزشکی (بیوالکتریک)
   سال ۱۴۰۴ — ۱۲۰ سوال — مرکز سنجش آموزش پزشکی کشور
   کلید: کلید نهایی رسمی سنجش (۱-۱۲۰؛ سوال ۵ حذف شد)
   تولیدشده با build_1404.py — ویرایش دستی نکنید
   ═══════════════════════════════════════════════════════════════════ */
var PKR = (typeof PKR !== "undefined" && PKR) ? PKR : {{}};
(function(){{
  const Y = "1404";
  PKR[Y] = PKR[Y] || {{}};
  const S = PKR[Y];
{body}
  if (typeof console !== "undefined") console.log("[official] 1404 loaded:", {log_args});
}})();
"""
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Created", OUT, counts, f"{os.path.getsize(OUT)//1024} KB")

if __name__ == '__main__':
    build()
