/* =============================================================
   figures_fit.js — چیدمان خودکار شکل‌ها (بازبینی نهایی قبل از نمایش)
   هیچ متنی از کادر بیرون نمی‌زند و هیچ دو متنی روی هم نمی‌افتد:
   • متنِ بیرون‌زده به داخل کادر منتقل می‌شود
   • برچسب‌های روی‌هم‌افتاده از هم جدا می‌شوند
   • اگر لازم باشد، ارتفاع SVG کمی زیاد می‌شود (بدون تغییر نسبت)
   نتیجه در cache نگه داشته می‌شود، پس هزینه‌اش یک‌بار است.
   ============================================================= */
var FIGFIT = (function(){
  const cache = {};
  let host = null;
  const PAD = 3;          // حاشیه امن درون کادر
  const REL = 4;          // فاصله لازم بین دو متن

  /* میزبان نامرئی برای اندازه‌گیری: position:fixed ⇒ هیچ اثری روی چیدمان/اسکرول صفحه ندارد
     و بعد از هر بار اندازه‌گیری از DOM حذف می‌شود */
  function hostEl(){
    if(!host){
      host = document.createElement("div");
      host.setAttribute("aria-hidden","true");
      host.style.cssText = "position:fixed;left:0;top:0;width:1400px;height:0;overflow:visible;" +
                           "visibility:hidden;opacity:0;pointer-events:none;z-index:-1";
      document.body.appendChild(host);
    }
    return host;
  }
  function dropHost(){ if(host && host.parentNode){ host.parentNode.removeChild(host); host = null; } }

  /* اندازه‌گیری با مستطیل واقعی رندرشده (transform ها هم لحاظ می‌شوند)
     ابتدا SVG را ۱:۱ می‌کنیم تا مختصات پیکسل = مختصات کاربری */
  function measure(svg, W, H){
    svg.setAttribute("width", W); svg.setAttribute("height", H);
    const base = svg.getBoundingClientRect();
    return [...svg.querySelectorAll("text")].map(el=>{
      const r = el.getBoundingClientRect();
      if(r.width === 0 && r.height === 0) return { el, x:0, y:0, w:0, h:0, r:0, b:0, empty:true };
      const x = r.left - base.left, y = r.top - base.top;
      return { el, x, y, w:r.width, h:r.height, r:x+r.width, b:y+r.height };
    });
  }

  function fit(id){
    if(cache[id] !== undefined) return cache[id];
    const raw = FIGURES[id]();
    if(!document.body || !document.querySelector) { return raw; }
    const h = hostEl();
    h.innerHTML = raw;
    const svg = h.querySelector("svg");
    if(!svg) return raw;
    const vb = (svg.getAttribute("viewBox")||"0 0 560 250").split(/\s+/).map(Number);
    const W = vb[2];
    let H = vb[3];
    const texts = [...svg.querySelectorAll("text")];
    const off = texts.map(()=>({x:0,y:0}));
    const apply = i => texts[i].setAttribute("transform",
      `translate(${off[i].x.toFixed(1)},${off[i].y.toFixed(1)})`.replace("translate(0.0,0.0)",""));

    for(let iter=0; iter<14; iter++){
      const m = measure(svg, W, H);
      let fixed = false;

      /* ۱) بیرون‌زدگی افقی */
      for(let i=0;i<m.length;i++){
        const t = m[i];
        if(t.empty) continue;
        if(t.w > W - 2*PAD) continue;   // پهن‌تر از کادر: جابه‌جایی افقی بی‌فایده است
        if(t.x < PAD){ off[i].x += (PAD - t.x); apply(i); fixed = true; break; }
        if(t.r > W - PAD){ off[i].x -= (t.r - (W - PAD)); apply(i); fixed = true; break; }
      }
      if(fixed) continue;

      /* ۲) بیرون‌زدگی پایین (و بالا) */
      for(let i=0;i<m.length;i++){
        const t = m[i];
        if(t.empty) continue;
        if(t.b > H - PAD){ H = Math.ceil(t.b + PAD + 1); fixed = true; break; }
        if(t.y < 0){ off[i].y += (2 - t.y); apply(i); fixed = true; break; }
      }
      if(fixed) continue;

      /* ۳) روی‌هم‌افتادن دو متن — متن بلندتر (کپشن) پایین می‌رود */
      let worst = null;
      for(let i=0;i<m.length;i++) for(let j=i+1;j<m.length;j++){
        const a=m[i], c=m[j];
        if(a.empty || c.empty) continue;
        const ix = Math.min(a.r,c.r) - Math.max(a.x,c.x);
        const iy = Math.min(a.b,c.b) - Math.max(a.y,c.y);
        if(ix > 2 && iy > 2){
          const area = ix*iy;
          if(!worst || area > worst.area){ worst = {i, j, a, c, ix, iy, area}; }
        }
      }
      if(worst){
        const A = worst.a, B = worst.c;
        const longI = (A.w > B.w ? worst.i : worst.j);
        const longT = (A.w > B.w ? A : B);
        const oth = (A.w > B.w ? B : A);
        /* اگر یکی از دو متن «برچسب کوتاه» است، آن یکی کمی جابه‌جا می‌شود
           (برای جدا کردن برچسب از تیک محور) */
        if(longT.w > 80){
          const dy = (oth.b + REL - longT.y);
          off[longI].y += (dy > 0 ? dy : worst.iy + REL);
          apply(longI);
        } else {
          const otherI = (longI === worst.i ? worst.j : worst.i);
          off[otherI].y += (worst.iy + 1);   // برچسب کوتاه کمی پایین‌تر
          apply(otherI);
        }
        fixed = true;
        continue;
      }
      break;  // همه چیز مرتب است
    }

    dropHost();
    const vbNew = `0 0 ${W} ${H}`;
    svg.setAttribute("viewBox", vbNew);
    svg.setAttribute("width", "100%");
    svg.setAttribute("height", H);
    svg.setAttribute("preserveAspectRatio", "xMidYMid meet");
    let out = h.innerHTML;
    /* حذف transformهای بی‌اثر */
    out = out.replace(/ transform="translate\(-?0(\.0)?,-?0(\.0)?\)"/g, "");
    cache[id] = out;
    return out;
  }

  /* شکل آماده نمایش: اگر FIGURES معرفی نشده باشد، رشته خالی */
  function figureSVG(id){
    if(typeof FIGURES === "undefined" || !FIGURES[id]) return "";
    try { return fit(id); }
    catch(e){ try { return FIGURES[id](); } catch(e2){ return ""; } }
  }

  /* با آماده‌شدن فونت‌ها، اندازه‌ها عوض می‌شود ⇒ cache بازسازی می‌شود */
  if(document.fonts && document.fonts.ready){
    document.fonts.ready.then(()=>{ Object.keys(cache).forEach(k=>delete cache[k]); });
  }
  function reset(){ Object.keys(cache).forEach(k=>delete cache[k]); }

  return { figureSVG, fit, reset, size: ()=>Object.keys(cache).length };
})();

/* دسترسی سراسری */
var figureSVG = FIGFIT.figureSVG;
