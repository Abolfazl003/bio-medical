"""بررسی خودکار شکل‌ها: هم‌پوشانی متن‌ها و بیرون‌زدگی از کادر"""
from playwright.sync_api import sync_playwright
import json

JS = """(()=>{
  const host = document.getElementById('figcheck');
  const out = {};
  Object.keys(FIGURES).forEach(id=>{
    host.innerHTML = (typeof figureSVG==='function') ? figureSVG(id) : FIGURES[id]();
    const svg = host.querySelector('svg');
    const vb = svg.getAttribute('viewBox').split(' ').map(Number);
    const W = vb[2], H = vb[3];
    svg.setAttribute('width', W); svg.setAttribute('height', H);
    const base = svg.getBoundingClientRect();
    const texts = [...svg.querySelectorAll('text')].map(t=>{
      const r = t.getBoundingClientRect();
      const x = r.left-base.left, y = r.top-base.top;
      return {t:(t.textContent||'').slice(0,28), x:+x.toFixed(1), y:+y.toFixed(1),
              w:+r.width.toFixed(1), h:+r.height.toFixed(1), r:+(x+r.width).toFixed(1), b:+(y+r.height).toFixed(1)};
    }).filter(t=>t.w>0||t.h>0);
    // بیرون‌زدگی
    const outOf = texts.filter(t=> t.x < 1 || t.r > W-1 || t.y < 0 || t.b > H-1);
    // هم‌پوشانی متن با متن
    const ov = [];
    for(let i=0;i<texts.length;i++) for(let j=i+1;j<texts.length;j++){
      const a=texts[i], b=texts[j];
      const ix = Math.min(a.r,b.r) - Math.max(a.x,b.x);
      const iy = Math.min(a.b,b.b) - Math.max(a.y,b.y);
      if(ix>2 && iy>2) ov.push({a:a.t,b:b.t,ix:+ix.toFixed(1),iy:+iy.toFixed(1)});
    }
    if(outOf.length || ov.length) out[id] = {W,H,outOf:outOf.map(t=>t.t+'@'+t.x+','+t.y), ov:ov.slice(0,6)};
  });
  return out;
})()"""

with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width":1000,"height":900})
    pg.goto("http://127.0.0.1:8000/index.html"); pg.wait_for_timeout(900)
    pg.evaluate("()=>{const d=document.createElement('div'); d.id='figcheck'; d.style.cssText='position:absolute;left:-9999px;top:0;width:1200px'; document.body.appendChild(d);}")
    res = pg.evaluate(JS)
    b.close()

print(f"شکل‌های دارای ایراد: {len(res)} از ۴۷\n")
for k,v in res.items():
    print(f"■ {k}  ({v['W']}×{v['H']})")
    for o in v["outOf"]: print("   ⬅ بیرون از کادر:", o)
    for o in v["ov"]: print(f"   ✖ هم‌پوشانی ({o['ix']}×{o['iy']}): «{o['a']}» ↔ «{o['b']}»")
    print()
