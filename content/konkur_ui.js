/* ============================================================
   بخش «کنکورهای ۱۰ سال اخیر» — رابط کاربری
   این قطعه به app.js اضافه می‌شود
============================================================ */

/* ---- توابع پایه ---- */
function pkYears(){
  if(typeof PK === "undefined") return [];
  return Object.keys(PK).filter(k=>k!=="subjects").sort();
}
function pkSubjects(){ return (typeof PK!=="undefined" && PK.subjects) ? Object.keys(PK.subjects) : []; }
function pkQ(year, sid){ return (typeof PK!=="undefined" && PK[year] && PK[year][sid]) ? PK[year][sid] : []; }
function pkYearCount(year){ return pkSubjects().reduce((a,s)=>a+pkQ(year,s).length,0); }
function pkTotalCount(){ return pkYears().reduce((a,y)=>a+pkYearCount(y),0); }
function pkDone(){ return STATE.progress.konkur_results || (STATE.progress.konkur_results={}); }
function pkFa(n){ return String(n).replace(/\d/g, d=>"۰۱۲۳۴۵۶۷۸۹"[d]); }
function pkRes(year, sid){ return pkDone()[year+"__"+sid] || null; }

/* هر سوال کنکور به شکل استاندارد موتور تست تبدیل می‌شود */
function pkToQuiz(year, sid, list){
  return list.map(q=>({
    q: q.q,
    choices: q.c,
    answer: q.a,
    subject: sid,
    year: pkFa(year),
    konkori: q.k || "",
    full_solution: q.s || ""
  }));
}

/* ---- صفحه اصلی: فهرست ۱۰ سال ---- */
function renderKonkurHome(main){
  const years = pkYears().reverse();       // جدیدترین سال اول
  let doneCount=0, answeredYears=0;
  years.forEach(y=>{ if(pkSubjects().some(s=>pkRes(y,s))) answeredYears++; });
  pkSubjects().forEach(s=>years.forEach(y=>{ if(pkRes(y,s)) doneCount++; }));

  main.innerHTML=`
    <div class="page-head"><h1>🏛 کنکورهای ۱۰ سال اخیر</h1>
      <p>سوالات سال به سال، درس به درس — هر سال ${pkSubjects().length} درس و ${pkYearCount(pkYears()[0]||"0")} سوال</p>
      <div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn btn-primary" onclick="startKonkurAll()">🎲 همه سال‌ها — تست ترکیبی</button>
        <button class="btn btn-ghost" onclick="setView('exams')">🎓 آزمون‌های جامع ۲۵ سوالی</button>
      </div></div>
    <div class="big-stats">
      <div class="big-stat"><div class="num" style="color:var(--accent)">${pkFa(pkTotalCount())}</div><div class="lbl">سوال کنکوری 🗂</div></div>
      <div class="big-stat"><div class="num" style="color:var(--accent2)">${pkFa(years.length)}</div><div class="lbl">دوره (سال) 📅</div></div>
      <div class="big-stat"><div class="num" style="color:var(--success)">${pkFa(doneCount)}</div><div class="lbl">درس آزمون‌داده‌شده ✅</div></div>
    </div>
    <div class="section-title">📅 انتخاب سال</div>
    <div class="grid-cards" id="kg"></div>`;

  const g=$("#kg");
  years.forEach(y=>{
    const n=pkYearCount(y);
    const solved=pkSubjects().filter(s=>pkRes(y,s)).length;
    const el=document.createElement("div"); el.className="card clickable";
    el.innerHTML=`<div class="emoji">📅</div>
      <h3>کنکور ${pkFa(y)}</h3>
      <p>${pkFa(pkSubjects().length)} درس • ${pkFa(n)} سوال</p>
      <div class="bar" style="margin:8px 0"><div class="bar-fill" style="width:${Math.round(solved*100/pkSubjects().length)}%"></div></div>
      <div style="font-size:12px;color:var(--muted)">${pkFa(solved)} از ${pkFa(pkSubjects().length)} درس تمرین‌شده</div>
      <div class="card-actions"><button class="btn btn-primary">مشاهده سوالات</button></div>`;
    el.onclick=()=>openKonkurYear(y);
    g.appendChild(el);
  });
}

function openKonkurYear(year){ STATE._konkurYear=year; setView("konkur-year"); }

/* ---- صفحه سال: درس‌ها ---- */
function renderKonkurYear(main){
  const year=STATE._konkurYear;
  if(!year || pkYears().indexOf(year)<0){ setView("konkur"); return; }
  const subs=pkSubjects();
  main.innerHTML=`
    <div class="page-head"><h1>📅 کنکور ${pkFa(year)}</h1>
      <p>${pkFa(subs.length)} درس • ${pkFa(pkYearCount(year))} سوال — برای هر درس یک آزمون با تصحیح و توضیح کامل</p>
      <div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn btn-primary" onclick="startKonkur('${year}')">🎲 آزمون ترکیبی همین سال (${pkFa(pkYearCount(year))} سوال)</button>
        <button class="btn btn-ghost" onclick="setView('konkur')">🔙 فهرست سال‌ها</button>
      </div></div>
    <div class="grid-cards" id="sg"></div>`;

  const g=$("#sg");
  subs.forEach(sid=>{
    const list=pkQ(year,sid);
    const r=pkRes(year,sid);
    const pct=r?Math.round(r.score*100/r.total):0;
    const el=document.createElement("div"); el.className="card clickable";
    el.innerHTML=`<div class="emoji">${subEmoji(sid)}</div>
      <h3>${subName(sid)}</h3>
      <p>${pkFa(list.length)} سوال با ترفند کنکوری + حل تشریحی</p>
      ${r?`<div class="bar" style="margin:8px 0"><div class="bar-fill" style="width:${pct}%"></div></div>
          <div style="font-size:12px;color:${pct>=50?'var(--success)':'var(--warning)'};font-weight:700">آخرین نتیجه: ${pkFa(pct)}٪ (${pkFa(r.score)} از ${pkFa(r.total)})</div>`
        :`<div style="font-size:12px;color:var(--muted)">هنوز تمرین نشده</div>`}
      <div class="card-actions"><button class="btn btn-secondary">شروع آزمون درس</button></div>`;
    el.onclick=()=>startKonkur(year, sid);
    g.appendChild(el);
  });
}

/* ---- شروع آزمون: یک درس از یک سال ---- */
function startKonkur(year, sid, shuffleQ){
  let qs=[];
  if(!sid){                       // همه درس‌های یک سال
    pkSubjects().forEach(s=>{ qs=qs.concat(pkToQuiz(year, s, pkQ(year,s))); });
  } else {
    qs=pkToQuiz(year, sid, pkQ(year,sid));
  }
  if(!qs.length) return;
  if(shuffleQ) qs=shuffle(qs);
  STATE.quiz={questions:qs, idx:0, correct:0, subject: sid?subName(sid):("کنکور "+pkFa(year)), konkur:{year:year, sid:sid}};
  setView("quiz-playing");
}

/* ---- تست ترکیبی همه سال‌ها ---- */
function startKonkurAll(){
  let qs=[];
  pkYears().forEach(y=>pkSubjects().forEach(s=>{ qs=qs.concat(pkToQuiz(y,s,pkQ(y,s))); }));
  if(!qs.length) return;
  qs=shuffle(qs).slice(0,20);
  STATE.quiz={questions:qs, idx:0, correct:0, subject:"کنکورهای ۱۰ سال اخیر (ترکیبی)", konkur:{year:null,sid:null}};
  setView("quiz-playing");
}

/* ---- ثبت نتیجه آزمون کنکور در پیشرفت (از checkAnswer فراخوانی می‌شود) ---- */
function pkRecordAnswer(isCorrect){
  const Q=STATE.quiz;
  if(!Q || !Q.konkur || !Q.konkur.year || !Q.konkur.sid) return;
  const key=Q.konkur.year+"__"+Q.konkur.sid;
  const all=qDone();
  if(!all[key]) all[key]={score:0,total:pkQ(Q.konkur.year,Q.konkur.sid).length,date:new Date().toLocaleDateString("fa-IR")};
  if(isCorrect) all[key].score++;
  all[key].total=pkQ(Q.konkur.year,Q.konkur.sid).length;
  all[key].date=new Date().toLocaleDateString("fa-IR");
}
function qDone(){ return pkDone(); }
