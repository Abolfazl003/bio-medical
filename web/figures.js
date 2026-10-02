/* =============================================================
   figures.js — موتور شکل‌های تصویری کتاب‌ها (نسخه ۱.۳.۰)
   همه شکل‌ها SVG برداری واقعی‌اند (نه شکل شماتیک متنی):
   نمادهای استاندارد مداری، نمودار با محور و منحنی، بلوک‌دیاگرام.
   ============================================================= */
var FIG = (function(){
  const K = {
    wire:"#94a3b8", comp:"#e2e8f0", acc:"#38bdf8", acc2:"#a855f7",
    warn:"#f59e0b", ok:"#22c55e", bad:"#ef4444", txt:"#e2e8f0",
    dim:"#94a3b8", grid:"#334155", bg:"#0b1220", fill:"#111c2e"
  };
  const n = v => Math.round(v*10)/10;

  /* ---------- پایه ---------- */
  const svg = (w,h,inner) =>
    `<svg class="fig-svg" viewBox="0 0 ${w} ${h}" width="100%" xmlns="http://www.w3.org/2000/svg" role="img">${inner}</svg>`;

  const L = (x1,y1,x2,y2,o={}) =>
    `<line x1="${n(x1)}" y1="${n(y1)}" x2="${n(x2)}" y2="${n(y2)}" stroke="${o.c||K.wire}" stroke-width="${o.w||2}" ${o.d?`stroke-dasharray="${o.d}"`:""} stroke-linecap="round"/>`;

  const P = (d,o={}) =>
    `<path d="${d}" fill="${o.f||"none"}" stroke="${o.c||K.wire}" stroke-width="${o.w||2}" stroke-linejoin="round" stroke-linecap="round" ${o.d?`stroke-dasharray="${o.d}"`:""}/>`;

  const RECT = (x,y,w,h,o={}) =>
    `<rect x="${n(x)}" y="${n(y)}" width="${n(w)}" height="${n(h)}" rx="${o.rx??8}" fill="${o.f||K.fill}" stroke="${o.c||K.wire}" stroke-width="${o.w||1.5}"/>`;

  const CIRC = (cx,cy,r,o={}) =>
    `<circle cx="${n(cx)}" cy="${n(cy)}" r="${n(r)}" fill="${o.f||"none"}" stroke="${o.c||K.wire}" stroke-width="${o.w||2}"/>`;

  const T = (x,y,s,o={}) =>
    `<text x="${n(x)}" y="${n(y)}" fill="${o.c||K.txt}" font-size="${o.s||13}" font-weight="${o.b?700:500}" text-anchor="${o.a||"middle"}" direction="${o.rtl===false?"ltr":"rtl"}">${s}</text>`;

  const POLY = (pts,o={}) =>
    `<polygon points="${pts}" fill="${o.f||"none"}" stroke="${o.c||K.wire}" stroke-width="${o.w||2}" stroke-linejoin="round"/>`;

  const node = (x,y,c) => CIRC(x,y,3.5,{f:c||K.acc,c:c||K.acc,w:0});
  const dot  = (x,y,r,c) => CIRC(x,y,r||4,{f:c||K.acc,c:c||K.acc,w:0});

  /* ---------- نمادهای مداری ---------- */
  // مقاومت افقی/عمودی — مرکز (x,y)
  function resH(x,y,len,label,col){
    const a = 6, w = 12, h = len/2, s = [];
    s.push(L(x-h,y,x-h+a,y,{c:col}));
    for(let i=0;i<6;i++){
      const dx = h - a - (i*( (h-a)*2/6 ));
      s.push(L(x-dx, y, x-dx-(h-a)/6, y+(i%2? w/2:-w/2), {c:col}));
    }
    s.push(L(x+h-a,y,x+h,y,{c:col}));
    if(label) s.push(T(x, y-16, label, {s:12,c:col||K.txt,b:1}));
    return s.join("");
  }
  function resV(x,y,len,label,col){
    const a = 6, w = 12, h = len/2, s = [];
    s.push(L(x,y-h,x,y-h+a,{c:col}));
    for(let i=0;i<6;i++){
      const dy = h - a - (i*((h-a)*2/6));
      s.push(L(x, y-dy, x+(i%2? w/2:-w/2), y-dy-(h-a)/6, {c:col}));
    }
    s.push(L(x,y+h-a,x,y+h,{c:col}));
    if(label) s.push(T(x-20, y+4, label, {s:12,c:col||K.txt,b:1}));
    return s.join("");
  }
  // خازن
  const capH = (x,y,gap,label,col) => L(x-gap/2,y-11,x-gap/2,y+11,{c:col,w:2.4}) + L(x+gap/2,y-11,x+gap/2,y+11,{c:col,w:2.4}) + (label?T(x,y-18,label,{s:12,c:K.txt,b:1}):"");
  const capV = (x,y,gap,label,col) => L(x-11,y-gap/2,x+11,y-gap/2,{c:col,w:2.4}) + L(x-11,y+gap/2,x+11,y+gap/2,{c:col,w:2.4}) + (label?T(x+24,y+4,label,{s:12,c:K.txt,b:1}):"");
  // سلف
  function indH(x,y,len,label,col){
    const r = len/8, a = x - len/2; let d = `M ${n(a)} ${n(y)}`;
    for(let i=0;i<4;i++) d += ` a ${n(r)} ${n(r)} 0 0 1 ${n(2*r)} 0`;
    return P(d,{c:col}) + (label?T(x,y-16,label,{s:12,c:K.txt,b:1}):"");
  }
  // باتری (منبع DC)
  function batV(x,y,gap,label){
    const s = [ L(x-16,y-gap/2,x+16,y-gap/2,{c:K.ok,w:2.6}), L(x-8,y+gap/2,x+8,y+gap/2,{c:K.ok,w:2.6}) ];
    s.push(T(x-26,y-gap/2+5,"+",{s:14,c:K.ok,b:1}));
    s.push(T(x-26,y+gap/2+5,"−",{s:14,c:K.bad,b:1}));
    if(label) s.push(T(x-56,y+4,label,{s:12,c:K.txt,b:1}));
    return s.join("");
  }
  // منبع سینوسی
  const srcAC = (x,y,r,label) => CIRC(x,y,r||14,{c:K.ok,w:2}) +
    P(`M ${n(x-5)} ${n(y)} q 5 -9 10 0 q -5 9 -10 0`,{c:K.ok,w:2}) + (label?T(x,y-24,label,{s:12,c:K.txt,b:1}):"");
  // زمین
  const gnd = (x,y) => L(x,y,x,y+8) + L(x-12,y+8,x+12,y+8,{w:2.4}) + L(x-7,y+13,x+7,y+13,{w:2}) + L(x-3,y+18,x+3,y+18,{w:2});
  // دیود
  function diodeH(x,y,size,label,flip){
    const s = size||11, d = flip?-1:1;
    return POLY(`${n(x-d*s)},${n(y-s)} ${n(x-d*s)},${n(y+s)} ${n(x+d*s)},${n(y)}`,{f:K.fill,c:K.acc,w:2})
      + L(x+d*s, y-s, x+d*s, y+s, {c:K.acc,w:2.6}) + (label?T(x,y-18,label,{s:12,c:K.txt,b:1}):"");
  }
  // آمپ‌اپ (مثلث)
  function opamp(cx,cy,w){
    const W = w||40, H = W*0.9;
    return POLY(`${n(cx-W/2)},${n(cy-H/2)} ${n(cx-W/2)},${n(cy+H/2)} ${n(cx+W/2)},${n(cy)}`,{f:K.fill,c:K.acc2,w:2})
      + T(cx-W/2+9, cy-H/4+4, "−", {s:13,c:K.txt,b:1})
      + T(cx-W/2+9, cy+H/4+5, "+", {s:13,c:K.txt,b:1});
  }
  // ترانزیستور NPN
  function npn(cx,cy,label){
    const s = [];
    s.push(CIRC(cx,cy,22,{c:K.acc2,w:1.6}));
    s.push(L(cx-16,cy-13,cx-16,cy+13,{c:K.acc2,w:3}));      // بیس
    s.push(L(cx-16,cy-7,cx+6,cy-18,{c:K.acc2,w:2}));
    s.push(L(cx-16,cy+7,cx+6,cy+18,{c:K.acc2,w:2}));
    s.push(L(cx+6,cy+18,cx+6,cy+30,{c:K.acc2,w:2}));
    s.push(L(cx+6,cy-18,cx+6,cy-30,{c:K.acc2,w:2}));
    s.push(POLY(`${n(cx+1)},${n(cy+12)} ${n(cx+8)},${n(cy+16)} ${n(cx+2)},${n(cy+20)}`,{f:K.acc2,c:K.acc2,w:0}));
    if(label) s.push(T(cx+18,cy+4,label,{s:12,c:K.txt,b:1}));
    return s.join("");
  }
  // جریان‌سنج / گالوانومتر
  const meter = (x,y,r,label,txt) => CIRC(x,y,r||14,{c:K.warn,w:2}) + T(x,y+5,txt||"G",{s:13,c:K.warn,b:1}) + (label?T(x,y-22,label,{s:12,c:K.txt,b:1}):"");
  // فلش جریان
  function iarr(x1,y1,x2,y2,label,col){
    const ang = Math.atan2(y2-y1,x2-x1);
    const tip = `${n(x2)},${n(y2)}`;
    const p1 = `${n(x2-9*Math.cos(ang-0.4))},${n(y2-9*Math.sin(ang-0.4))}`;
    const p2 = `${n(x2-9*Math.cos(ang+0.4))},${n(y2-9*Math.sin(ang+0.4))}`;
    const c = col||K.warn;
    let s = L(x1,y1,x2,y2,{c,w:2}) + POLY(`${tip} ${p1} ${p2}`,{f:c,c,w:0});
    if(label){ const mx=(x1+x2)/2, my=(y1+y2)/2; const long=String(label).length>8; s += T(mx, my+(long?20:-7), label, {s:12,c,b:1}); }
    return s;
  }

  /* ---------- نمودار ---------- */
  function axes(x,y,w,h,o={}){
    const s = [ RECT(x,y,w,h,{f:"none",c:K.grid,rx:4}) ];
    const yt = o.yt||4, xt = o.xt||5;
    for(let i=1;i<yt;i++){ const yy=y+h-1-i*h/yt; s.push(L(x,yy,x+w,yy,{c:K.grid,w:1,d:"3 5"})); }
    for(let i=1;i<xt;i++){ const xx=x+i*w/xt; s.push(L(xx,y,xx,y+h,{c:K.grid,w:1,d:"3 5"})); }
    s.push(L(x,y,x+w,y,{c:K.dim,w:1.6})); s.push(L(x,y,x,y+h,{c:K.dim,w:1.6}));
    const ascii = v => /^[\x20-\x7F]*$/.test(String(v||""));
    if(o.xlab) s.push(T(x+w/2, y+h+34, o.xlab, {s:11.5,c:K.dim,rtl:!ascii(o.xlab)}));
    (o.yticks||[]).forEach((lab,i,a)=>{ const yy=y+h-1-((i+1)*h/(a.length+1)); s.push(T(x-8,yy+4,lab,{s:10.5,c:K.dim,a:"end",rtl:false})); });
    (o.xticks||[]).forEach((lab,i,a)=>{ const xx=x+((i+1)*w/(a.length+1)); s.push(T(xx,y+h+14,lab,{s:10.5,c:K.dim,rtl:false})); });
    if(o.ylab) s.push(T(x+2, y-9, o.ylab, {s:11.5,c:K.dim,a:"start",rtl:!ascii(o.ylab),b:0}));
    return s.join("");
  }
  // منحنی از تابع نمونه‌گیری‌شده (x,xr,yr)
  function curve(x,y,w,h,f,o={}){
    const xr = o.xr||[0,1], yr = o.yr||[0,1], N = o.n||90;
    let d = "", started=false;
    for(let i=0;i<=N;i++){
      const u = i/N, xv = xr[0]+(xr[1]-xr[0])*u, yv = f(xv);
      const px = x + u*w, py = y + h - ((yv-yr[0])/(yr[1]-yr[0]))*h;
      if(!isFinite(py)) { started=false; continue; }
      const cy2 = Math.max(y-4, Math.min(y+h+4, py));
      d += (started? " L ":"M ") + n(px) + " " + n(cy2);
      started = true;
    }
    return P(d,{c:o.c||K.acc,w:o.w||2.6,d:o.d});
  }
  function vline(x,y,h,lab,col){
    const s = L(x,y,x,y+h,{c:col||K.warn,w:1.4,d:"4 4"});
    const t = (typeof lab==="string" && lab) ? lab : "";
    return s + (t?T(x,y+h+13,t,{s:10,c:col||K.warn,rtl:false}):"");
  }
  function hline(x,y,w,lab,col){
    const s = L(x,y,x+w,y,{c:col||K.warn,w:1.4,d:"4 4"});
    const t = (typeof lab==="string" && lab) ? lab : "";
    return s + (t?T(x+w-5,y-6,t,{s:10,c:col||K.warn,a:"end",rtl:false}):"");
  }
  function tag(x,y,s,col,anchor){ return RECT(x-(s.length*3.6+10),y-13,s.length*7.2+20,20,{f:"#0f172a",c:col||K.acc,rx:6,w:1.2}) + T(x,y+2,s,{s:11,c:col||K.acc,b:1,a:"middle"}) }

  /* ---------- بلوک‌دیاگرام ---------- */
  function blk(x,y,w,h,label,o={}){
    const s = [ RECT(x,y,w,h,{f:o.f||"#13233a",c:o.c||K.acc,rx:w>1?8:8,w:1.6}) ];
    const lines = String(label).split("|");
    lines.forEach((ln,i)=> s.push(T(x+w/2, y+h/2+(i-(lines.length-1)/2)*18+5, ln, {s:o.s||12,c:o.tc||K.txt,b:1})));
    return s.join("");
  }
  function arrow(x1,y1,x2,y2,col,label){
    const ang = Math.atan2(y2-y1,x2-x1), c = col||K.dim;
    const tip = `${n(x2)},${n(y2)}`;
    const p1 = `${n(x2-8*Math.cos(ang-0.45))},${n(y2-8*Math.sin(ang-0.45))}`;
    const p2 = `${n(x2-8*Math.cos(ang+0.45))},${n(y2-8*Math.sin(ang+0.45))}`;
    let s = L(x1,y1,x2,y2,{c,w:2}) + POLY(`${tip} ${p1} ${p2}`,{f:c,c,w:0});
    if(label){ const long=String(label).length>6; s += T((x1+x2)/2, (y1+y2)/2 + (long?16:-8), label, {s:11,c,b:1}); }
    return s;
  }
  function sumj(cx,cy,r){
    return CIRC(cx,cy,r||13,{f:K.fill,c:K.warn,w:2}) + L(cx-r*0.7,cy,cx+r*0.7,cy,{c:K.warn,w:1.6}) + L(cx,cy-r*0.7,cx,cy+r*0.7,{c:K.warn,w:1.6});
  }

  return {K,svg,L,P,RECT,CIRC,T,POLY,node,dot,resH,resV,capH,capV,indH,batV,srcAC,gnd,diodeH,opamp,npn,meter,iarr,axes,curve,vline,hline,tag,blk,arrow,sumj,n};
})();

/* =============================================================
   شکل‌های مداری
   ============================================================= */
var FIGURES = {};

/* ۱ — مدار سری */
FIGURES["circ-series"] = function(){
  const {L,resH,batV,T,iarr,node,gnd,svg}=FIG;
  return svg(520,220,
    L(70,60,450,60) + L(70,160,450,160) +
    batV(70,110,34,"V=10V") + L(70,60,70,93) + L(70,127,70,160) +
    resH(210,60,60,"R₁=2kΩ") + resH(360,60,60,"R₂=3kΩ") +
    iarr(120,42,200,42,"i",FIG.K.warn) +
    node(70,60) + node(450,60) + node(70,160) + node(450,160) +
    T(260,196,"جریان در مدار سری در همه اجزا یکسان است و مقاومت‌ها جمع می‌شوند: R = 2k + 3k = 5kΩ",{s:12,c:FIG.K.dim})
  );
};
/* ۲ — مدار موازی */
FIGURES["circ-parallel"] = function(){
  const {L,resV,batV,node,T,iarr,svg}=FIG;
  return svg(520,230,
    batV(70,115,34,"V=12V") + L(70,60,70,98) + L(70,132,70,175) +
    L(70,60,240,60) + L(70,175,240,175) +
    L(240,60,240,175) + L(390,60,390,175) + L(240,60,390,60) + L(240,175,390,175) +
    resV(240,117,70,"R₁=6Ω") + resV(390,117,70,"R₂=3Ω") +
    node(240,60)+node(240,175)+node(390,60)+node(390,175)+node(70,60)+node(70,175)+
    iarr(120,45,180,45,"i",FIG.K.warn) +
    T(260,215,"در موازی: 1/R = 1/6 + 1/3  ⇒  R = 2Ω (از کوچک‌ترین مقاومت هم کمتر)",{s:12,c:FIG.K.dim})
  );
};
/* ۳ — قوانین کیرشهف: گره */
FIGURES["circ-kcl"] = function(){
  const {L,T,iarr,node,svg,CIRC}=FIG;
  return svg(520,240,
    CIRC(260,120,10,{f:FIG.K.warn,c:FIG.K.warn}) + T(260,125,"•",{s:16,c:"#0b1220",b:1}) +
    L(260,120,120,50) + L(260,120,120,190) + L(260,120,420,120) +
    iarr(200,92,232,104,"i₁",FIG.K.ok) + iarr(200,150,232,133,"i₂",FIG.K.ok) + iarr(290,120,350,120,"i₃",FIG.K.bad) +
    T(100,44,"شاخه ۱",{s:12,c:FIG.K.txt}) + T(100,206,"شاخه ۲",{s:12,c:FIG.K.txt}) + T(430,110,"شاخه ۳",{s:12,c:FIG.K.txt}) +
    T(260,222,"قانون جریان کیرشهف: مجموع جریان‌های ورودی = مجموع خروجی‌ها ⇒ i₁ + i₂ = i₃",{s:12,c:FIG.K.dim})
  );
};
/* ۴ — دو حلقه و مش */
FIGURES["circ-mesh"] = function(){
  const {L,T,resH,resV,batV,node,iarr,svg}=FIG;
  return svg(520,250,
    // حلقه چپ
    L(70,60,250,60)+L(70,200,250,200)+L(70,60,70,200)+L(250,60,250,200)+
    resH(160,60,56,"R₁") + resV(70,130,56,"R₂") + batV(250,130,30,"V₁")+L(250,60,250,115)+L(250,145,250,200)+
    T(160,132,"i₁ ↻",{s:13,c:FIG.K.acc,b:1}) +
    // حلقه راست
    L(250,60,430,60)+L(250,200,430,200)+L(430,60,430,200)+
    resH(340,60,56,"R₃") + resV(430,130,56,"R₄") +
    T(340,132,"i₂ ↻",{s:13,c:FIG.K.acc2,b:1}) +
    node(250,60)+node(250,200) +
    T(260,232,"روش مش: برای هر حلقه یک جریان فرضی می‌گیریم و مجموع ولتاژها را صفر می‌کنیم",{s:12,c:FIG.K.dim})
  );
};
/* ۵ — تقسیم ولتاژ */
FIGURES["circ-divider"] = function(){
  const {L,T,resV,batV,node,iarr,arrow,svg}=FIG;
  return svg(520,230,
    batV(70,115,34,"V_in=9V")+L(70,60,70,98)+L(70,132,70,175)+L(70,60,260,60)+L(70,175,260,175)+L(260,60,260,175)+
    resV(260,95,50,"R₁=6k") + resV(260,155,50,"R₂=3k") +
    node(260,117)+T(300,120,"V_out",{s:12,c:FIG.K.ok,b:1}) +
    arrow(290,117,360,117,FIG.K.ok) +
    T(390,110,"V_out = V_in × R₂/(R₁+R₂)",{s:12,c:FIG.K.txt}) +
    T(390,132,"= 9 × 3/9 = 3V",{s:12,c:FIG.K.ok,b:1}) +
    T(260,205,"مدار تقسیم ولتاژ: پرکاربردترین مدار در تغذیه سنسورها و بایاس",{s:12,c:FIG.K.dim})
  );
};
/* ۶ — تونن */
FIGURES["circ-thevenin"] = function(){
  const {L,T,resH,batV,arrow,svg,tag}=FIG;
  return svg(520,200,
    L(50,60,200,60)+L(50,150,200,150)+L(50,60,50,150)+
    resH(120,60,56,"R₁") + batV(50,105,30,"V") +
    L(200,60,200,80)+resH(200,105,50,"R₂")+L(200,130,200,150)+

    arrow(220,105,300,105,FIG.K.warn) +
    T(180,190,"هر شبکه خطی",{s:12,c:FIG.K.dim}) +
    L(340,60,470,60)+L(340,150,470,150)+L(340,60,340,90)+L(340,120,340,150)+
    resH(405,60,56,"R_th") + TAGBOX(340,105,60,30,"V_th") +
    T(405,190,"معادل تونن: V_th و R_th",{s:12,c:FIG.K.dim}) +
    T(270,120,"≡",{s:22,c:FIG.K.acc,b:1})
  );
  function TAGBOX(x,y,w,h,label){
    return FIG.RECT(x,y,w,h,{f:"#13233a",c:FIG.K.acc2,rx:6}) + FIG.T(x+w/2,y+h/2+5,label,{s:12,c:FIG.K.acc2,b:1});
  }
};
/* ۷ — پل وتستون */
FIGURES["circ-wheatstone"] = function(){
  const {L,T,resH,resV,meter,node,batV,svg}=FIG;
  return svg(520,260,
    // مثلثی/لوزی
    L(260,40,440,130)+L(440,130,260,220)+L(260,220,80,130)+L(80,130,260,40)+
    resH(180,85,50,"R₁")+resH(350,85,50,"R₂")+resH(350,175,50,"R₃")+resH(180,175,50,"R₄")+
    meter(260,130,18,"","G") +
    L(260,40,260,112)+L(260,148,260,220)+
    node(260,40)+node(260,220) +
    T(260,248,"در تعادل: R₁/R₂ = R₄/R₃  ⇒  V_G = 0   (مبنای استرین‌گیج و ترمیستور)",{s:12,c:FIG.K.dim})
  );
};
/* ۸ — RC و شارژ خازن */
FIGURES["circ-rc"] = function(){
  const {L,T,resH,capV,batV,iarr,axes,curve,vline,hline,svg}=FIG;
  const RC = p => 1 - Math.exp(-p*5);
  return svg(560,250,
    L(50,60,150,60)+L(50,60,50,95)+batV(50,115,30,"V")+L(50,135,50,170)+L(50,170,150,170)+
    L(150,60,150,170)+L(150,60,230,60)+L(150,170,230,170)+
    resH(190,60,45,"R") + capV(230,115,30,"C") + L(230,60,230,100)+L(230,130,230,170)+
    iarr(120,42,175,42,"i",FIG.K.warn) +
    axes(330,50,190,120,{xlab:"زمان",ylab:"Vc",yticks:["0","0.63V","V"],xticks:["2τ","3τ"]}) +
    curve(330,50,190,120,RC,{xr:[0,1],yr:[0,1],c:FIG.K.ok}) +
    vline(330+190*0.2,50,120,"τ",FIG.K.warn) + hline(330,50+120*0.37,190,"63%",FIG.K.warn) +
    T(430,235,"شارژ خازن: Vc(t) = V(1 − e^(−t/RC))   و ثابت زمانی τ = RC",{s:12,c:FIG.K.dim})
  );
};
/* ۹ — RLC سری */
FIGURES["circ-rlc"] = function(){
  const {L,T,resH,indH,capV,srcAC,iarr,svg}=FIG;
  return svg(520,220,
    srcAC(60,120,18,"V(t)")+L(60,102,60,60)+L(60,138,60,180)+L(60,60,420,60)+L(60,180,420,180)+L(420,60,420,180)+
    resH(150,60,50,"R") + indH(250,60,56,"L") + capV(420,120,30,"C") + L(420,60,420,100)+L(420,140,420,180)+
    iarr(330,44,390,44,"i",FIG.K.warn) +
    T(260,205,"ω₀ = 1/√(LC)   |   ضریب کیفیت Q = ω₀L/R   |   در رزونانس Z = R",{s:12,c:FIG.K.dim})
  );
};
/* ۱۰ — مبدل ابزار دقیق */
FIGURES["circ-instr-amp"] = function(){
  const {L,T,opamp,resH,iarr,node,svg}=FIG;
  return svg(560,260,
    // دو بافر ورودی
    opamp(150,80,40)+opamp(150,190,40)+
    T(120,80,"V₁",{s:12,c:FIG.K.txt})+T(120,190,"V₂",{s:12,c:FIG.K.txt})+
    L(80,80,130,80)+L(80,190,130,190)+
    // شبکه بهره R و Rg
    L(170,80,205,80)+L(205,80,205,105)+resH(205,135,50,"Rg")+L(205,165,205,190)+L(170,190,205,190)+
    L(205,80,240,80)+L(205,190,240,190)+
    resH(280,80,50,"R")+resH(280,190,50,"R")+
    L(240,80,255,80)+L(305,80,330,80)+L(240,190,255,190)+L(305,190,330,190)+
    // طبقه تفاضلی
    opamp(430,135,44)+L(330,80,408,120)+L(330,190,408,150)+
    resH(360,220,50,"R") + L(408,135,408,220)+L(385,220,335,220)+
    L(452,135,500,135)+T(510,140,"V_out",{s:12,c:FIG.K.ok,b:1})+
    iarr(70,95,110,95,"",FIG.K.acc) +
    T(280,252,"تقویت‌کننده ابزار دقیق: امپدانس ورودی بسیار بالا + CMRR بالا (حدود ۱۰۰dB) — ستون هر دستگاه ثبت سیگنال زیستی",{s:11.5,c:FIG.K.dim})
  );
};
/* ۱۱ — فیلتر پایین‌گذر RC */
FIGURES["circ-lpf"] = function(){
  const {L,T,resH,capV,axes,curve,svg,vline,node}=FIG;
  const H = f => 1/Math.sqrt(1+Math.pow(f/0.2,2));
  return svg(560,250,
    /* مدار RC — سمت چپ */
    L(40,70,140,70)+resH(175,70,50,"R")+L(210,70,300,70)+L(300,70,300,120)+
    capV(300,145,30,"C")+L(300,170,300,200)+L(300,200,140,200)+L(140,200,140,70)+L(40,200,140,200)+
    T(48,64,"V_in",{s:12,c:FIG.K.txt})+T(316,64,"V_out",{s:12,c:FIG.K.ok})+node(300,70)+
    node(140,70)+node(140,200)+
    /* نمودار بود — سمت راست */
    axes(410,55,135,120,{xlab:"فرکانس",ylab:"|H|",yticks:["0","0.5","1"],xticks:["fc","10fc"]}) +
    curve(410,55,135,120,H,{xr:[0,1],yr:[0,1.05],c:FIG.K.ok}) +
    vline(410+135*0.2,55,120,"fc",FIG.K.warn) +
    T(280,232,"fc = 1/(2πRC)   |   افت ۳dB در fc   |   شیب نهایی ۲۰dB/dec",{s:12,c:FIG.K.txt,b:1}) +
    T(280,18,"فیلتر پایین‌گذر RC — پایه حذف نویز پرفرکانس در پیش‌پردازش سیگنال زیستی",{s:11.5,c:FIG.K.dim})
  );
};
/* ۱۲ — مشخصه دیود */
FIGURES["circ-diode"] = function(){
  const {T,axes,curve,svg,vline,L,iarr,diodeH}=FIG;
  const I = v => v<=0 ? 0.02*(Math.exp(v*3)-1) : Math.min(1, 0.02*(Math.exp(v*9)-1));
  return svg(560,240,
    axes(70,45,200,140,{xlab:"V",ylab:"I",xticks:["0.7V"],yticks:["1","2"]}) +
    curve(70,45,200,140,I,{xr:[-0.6,0.9],yr:[-0.6,3.4],c:FIG.K.acc}) +
    vline(70+200*0.45,45,140,"0.7V",FIG.K.warn) +
    diodeH(370,90,16,"D") + L(320,90,352,90)+L(388,90,440,90)+
    L(320,90,320,170)+L(320,170,440,170)+L(440,170,440,90)+
    iarr(390,140,340,140,"i",FIG.K.warn) +
    T(380,205,"بایاس مستقیم: گشوده (افت ۰.۷V سیلیسیم)",{s:12,c:FIG.K.dim}) +
    T(380,225,"بایاس معکوس: بسته (جریان ناچیز)",{s:12,c:FIG.K.dim})
  );
};
/* ۱۳ — یک‌سوساز نیم‌موج و پل */
FIGURES["circ-rectifier"] = function(){
  const {L,T,diodeH,resV,axes,curve,svg,capV}=FIG;
  const half = t => Math.sin(t*Math.PI*4)*0.9;
  const full = t => Math.abs(Math.sin(t*Math.PI*4))*0.9;
  return svg(560,260,
    // ورودی
    T(60,30,"AC ورودی",{s:12,c:FIG.K.txt}) +
    axes(30,40,150,80,{xticks:["t"],yticks:[]}) + curve(30,40,150,80,half,{xr:[0,1],yr:[-1.2,1.2],c:FIG.K.warn}) +
    // مدار پل
    L(230,40,330,40)+L(230,40,230,110)+L(330,40,330,110)+
    diodeH(280,40,12,"",false) + diodeH(230,75,12,"",true)+ diodeH(330,75,12,"",false) +
    L(230,110,330,110)+L(330,170,230,170)+L(230,110,230,170)+L(330,110,330,170)+
    resV(330,140,40,"R_L") +
    // خروجی
    T(430,30,"DC خروجی",{s:12,c:FIG.K.ok}) +
    axes(400,40,130,80,{xticks:["t"],yticks:[]}) + curve(400,40,130,80,full,{xr:[0,1],yr:[-0.2,1.2],c:FIG.K.ok}) +
    T(280,205,"پل دیودی (یک‌سوساز تمام‌موج): هر نیم‌سیکل، دو دیود هدایت می‌کنند و قطبیت خروجی ثابت می‌ماند",{s:11.5,c:FIG.K.dim}) +
    T(280,228,"ضریب ریپل نیم‌موج ۱.۲۱ و تمام‌موج ۰.۴۸ است (با خازن صافی کمتر می‌شود)",{s:11.5,c:FIG.K.dim})
  );
};
/* ۱۴ — تقویت‌کننده امیتر مشترک */
FIGURES["circ-bjt"] = function(){
  const {L,T,npn,resH,resV,capH,srcAC,svg,gnd}=FIG;
  return svg(560,280,
    L(90,60,470,60)+L(90,60,90,45)+T(95,42,"+Vcc",{s:12,c:FIG.K.ok})+
    resH(230,60,50,"R_C") + resV(150,100,50,"R₁") + resV(310,100,50,"R₂")+
    L(150,60,150,75)+L(150,125,150,160)+L(310,60,310,75)+L(310,125,310,160)+
    L(150,160,310,160)+T(230,155,"بیس",{s:11,c:FIG.K.dim})+
    npn(230,190,"Q₁") +
    L(230,216,230,240)+resV(230,255,30,"R_E")+gnd(230,272)+
    L(150,160,110,160)+capH(85,160,16,"C_in")+L(70,160,55,160)+srcAC(55,185,14,"v_s")+
    L(310,160,380,160)+T(350,155,"خروجی",{s:11,c:FIG.K.dim})+
    capH(390,160,16,"C_out")+L(420,160,470,160)+L(470,160,470,210)+resV(470,235,30,"R_L")+gnd(470,255)+
    T(280,42,"تقویت‌کننده امیتر مشترک: بهره ولتاژ ≈ −R_C/r_e  و فاز ۱۸۰ درجه (معکوس)",{s:11.5,c:FIG.K.dim})
  );
};
/* ۱۵ — آپ‌امپ معکوس */
FIGURES["circ-opamp-inv"] = function(){
  const {L,T,opamp,resH,resV,svg,node,gnd}=FIG;
  return svg(560,230,
    resH(120,80,60,"R_in") + L(60,80,90,80)+L(150,80,240,80)+
    opamp(270,110,50) +
    resH(230,60,56,"R_f") + L(200,60,202,60)+L(258,60,200,60)+L(200,60,200,80)+node(200,80,FIG.K.acc)+
    L(258,60,258,95)+L(258,60,258,95)+
    L(120,110,150,110)+L(120,110,120,150)+gnd(120,150)+
    T(60,74,"V_in",{s:12,c:FIG.K.txt}) +
    L(295,110,360,110)+T(390,105,"V_out = −(R_f/R_in)·V_in",{s:12,c:FIG.K.ok,b:1}) +
    L(360,150,200,150)+L(200,150,200,120)+L(200,120,186,120)+
    T(280,180,"زمین مجازی: سر منفی ورودی صفر ولت است و جریان ورودی هم صفر",{s:11.5,c:FIG.K.dim}) +
    T(280,205,"مثال: R_f = ۱۰۰k و R_in = ۱۰k ⇒ بهره = −۱۰",{s:11.5,c:FIG.K.acc})
  );
};
/* ۱۶ — آپ‌امپ غیرمعکوس */
FIGURES["circ-opamp-noninv"] = function(){
  const {L,T,opamp,resH,resV,svg,node,gnd}=FIG;
  return svg(520,220,
    L(80,80,240,80)+opamp(270,110,50)+
    resH(200,160,56,"R₁")+resH(200,200,56,"R₂") +
    L(195,110,240,110)+L(195,110,195,138)+L(195,182,195,190)+gnd(230,215)+
    L(295,110,400,110)+T(430,105,"V_out",{s:12,c:FIG.K.ok,b:1}) +
    L(340,110,340,160)+L(340,160,228,160)+
    T(80,74,"V_in",{s:12,c:FIG.K.txt}) +
    T(260,52,"V_out = (1 + R₂/R₁)·V_in  ⇒ بهره همیشه ≥ ۱ و فاز صفر",{s:12,c:FIG.K.dim})
  );
};
/* ۱۷ — پاسخ پله مرتبه دوم */
FIGURES["plot-step-2nd"] = function(){
  const {T,axes,curve,svg,vline,hline}=FIG;
  const step = (z)=>(t)=> t<0?0:1-Math.exp(-z*4*t)/Math.sqrt(1-z*z+1e-9)*Math.sin(Math.sqrt(Math.abs(1-z*z))*4*t+Math.acos(z));
  return svg(560,260,
    axes(70,40,420,150,{xlab:"زمان (s)",ylab:"خروجی",yticks:["0","1","2"],xticks:["ts"]}) +
    curve(70,40,420,150,step(0.2),{xr:[0,1],yr:[0,2],c:FIG.K.bad,w:2.4}) +
    curve(70,40,420,150,step(0.5),{xr:[0,1],yr:[0,2],c:FIG.K.warn,w:2.4}) +
    curve(70,40,420,150,step(1.0),{xr:[0,1],yr:[0,2],c:FIG.K.ok,w:2.4}) +
    hline(70,40+150-(1/2)*150,420,"مقدار نهایی",FIG.K.dim) +
    T(140,80,"ζ=۰.۲",{s:12,c:FIG.K.bad,b:1}) + T(230,60,"ζ=۰.۵",{s:12,c:FIG.K.warn,b:1}) + T(330,60,"ζ=۱",{s:12,c:FIG.K.ok,b:1}) +
    T(280,225,"Mp = e^(−πζ/√(1−ζ²))   |   فراجهش با کاهش میرایی زیاد می‌شود",{s:12,c:FIG.K.dim}) +
    T(280,246,"زمان نشست ≈ ۴/(ζωn) و زمان صعود ≈ ۱.۸/ωn",{s:11.5,c:FIG.K.dim})
  );
};
/* ۱۸ — بود */
FIGURES["plot-bode"] = function(){
  const {T,axes,curve,svg}=FIG;
  const mag = w => 1/Math.sqrt(1+w*w) * 1/Math.sqrt(1+ (w/10)*(w/10) );
  const ph  = w => -Math.atan(w)*180/Math.PI - Math.atan(w/10)*180/Math.PI;
  return svg(560,270,
    axes(60,35,220,130,{xlab:"ω (log)",ylab:"|G| dB",yticks:["۰","۲۰-","۴۰-"],xticks:["۱","۱۰","۱۰۰"]}) +
    curve(60,35,220,130,mag,{xr:[0.05,200],yr:[0,1.2],c:FIG.K.acc}) +
    axes(330,35,190,130,{xlab:"ω (log)",ylab:"فاز (deg)",yticks:["۰","۹۰-","۱۸۰-"],xticks:["۱","۱۰","۱۰۰"]}) +
    curve(330,35,190,130,ph,{xr:[0.05,200],yr:[-200,10],c:FIG.K.acc2}) +
    T(400,200,"هر پل شیب ۲۰dB/dec و ۹۰ درجه فاز می‌دهد",{s:11.5,c:FIG.K.dim}) +
    T(400,220,"حاشیه فاز از فرکانس تقاطع خوانده می‌شود",{s:11.5,c:FIG.K.dim}) +
    T(400,240,"PM > ۴۵° و GM > ۶dB هدف طراحی است",{s:11.5,c:FIG.K.ok})
  );
};
/* ۱۹ — روت لوکوس */
FIGURES["plot-rootlocus"] = function(){
  const {T,L,svg,axes,dot}=FIG;
  let s = axes(80,40,200,170,{xlab:"σ",ylab:"jω",yticks:[],xticks:[]});
  s += L(80+100,40,80+100,210,{c:FIG.K.grid,w:1.2,d:"4 4"});
  s += L(80,40+85,280,40+85,{c:FIG.K.grid,w:1.2,d:"4 4"});
  s += dot(120,125,5,FIG.K.bad) + dot(100,125,5,FIG.K.bad);
  s += FIG.P("M 110 125 C 130 95, 180 95, 210 70",{c:FIG.K.acc,w:2.4});
  s += FIG.P("M 110 125 C 130 155, 180 155, 210 180",{c:FIG.K.acc,w:2.4});
  s += T(120,225,"قطب‌های حلقه باز",{s:11.5,c:FIG.K.bad});
  s += T(360,90,"شاخه‌ها با افزایش بهره از قطب‌ها",{s:12,c:FIG.K.dim});
  s += T(360,112,"به سمت صفرها یا بی‌نهایت حرکت می‌کنند",{s:12,c:FIG.K.dim});
  s += T(360,140,"نقاطی که به محور jω می‌رسند = بهره مرزی پایداری",{s:12,c:FIG.K.warn});
  s += T(360,168,"تعداد شاخه‌ها = تعداد قطب‌های حلقه باز",{s:12,c:FIG.K.dim});
  s += T(360,196,"مرکز تقارب و زاویه شاخه‌ها از مجموع قطب‌ها/صفرها",{s:12,c:FIG.K.dim});
  return svg(560,250,s);
};
/* ۲۰ — طیف فوریه موج مربعی */
FIGURES["plot-fourier"] = function(){
  const {T,axes,svg,L,RECT,curve,svg:SV}=FIG;
  let s = axes(60,35,200,130,{xlab:"هارمونیک",ylab:"دامنه",yticks:["۰.۲","۰.۵","۱"],xticks:["۱","۳","۵","۷"]});
  const amps=[1,1/3,1/5,1/7,1/9,1/11];
  amps.forEach((a,i)=>{
    const x=60+15+i*30, hh=(a/1.1)*130;
    s += RECT(x,35+130-hh,16,hh,{f:FIG.K.acc,c:FIG.K.acc,rx:2});
    s += T(x+8,35+130+14,""+(2*i+1),{s:10,c:FIG.K.dim,rtl:false});
  });
  const sq = t => { let y=0; for(let k=1;k<=11;k+=2) y += Math.sin(2*Math.PI*k*t)/k; return y*4/Math.PI; };
  s += axes(300,35,220,130,{xlab:"t",ylab:"f(t)",yticks:[],xticks:[]});
  s += curve(300,35,220,130,sq,{xr:[0,1],yr:[-1.6,1.6],c:FIG.K.ok,w:2});
  s += T(410,190,"مجموع جزئی سری فوریه موج مربعی",{s:11.5,c:FIG.K.dim});
  s += T(410,210,"هارمونیک‌های فرد با دامنه ۱/n",{s:11.5,c:FIG.K.acc});
  s += T(410,230,"فراجهش نزدیک پرش ≈ ۹٪ (پدیده گیبس)",{s:11.5,c:FIG.K.warn});
  return SV(560,255,s);
};
