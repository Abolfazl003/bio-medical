/* =============================================================
   study_progress.js — زمان‌بندی و پیشرفت مطالعه دانشجو (v1.3.0)
   • چقدر دقیقه درس خوانده (کتاب + تست + کنکور)
   • چند روز دیگر برنامه تمام می‌شود (بر اساس هدف روزانه)
   • چند روز به کنکور مانده
   ============================================================= */

/* تاریخ کنکور ارشد بعدی: آزمون معمولاً اسفند برگزار می‌شود؛ نزدیک‌ترین ۵ مارس آینده */
function nextExamDate(){
  const now = new Date();
  let d = new Date(now.getFullYear(), 2, 5);              // ۵ مارس ≈ ۱۴ اسفند
  if(d - now < 20*86400000) d = new Date(now.getFullYear()+1, 2, 5);
  return d;
}
const EXAM_DATE = nextExamDate();
const GOAL_OPTIONS = [30, 44, 60, 90, 120];

/* ── اعداد و ساعت فارسی ── */
function pFa(n){ return Number(n||0).toLocaleString("fa-IR"); }
function faMin(m){
  m = Math.max(0, Math.round(m));
  if(m < 60) return pFa(m) + " دقیقه";
  const h = Math.floor(m/60), mm = m%60;
  return pFa(h) + " ساعت" + (mm ? " و " + pFa(mm) + " دقیقه" : "");
}
function faDate(iso){
  try { return new Intl.DateTimeFormat("fa-IR-u-ca-persian",{day:"numeric",month:"long"}).format(new Date(iso)); }
  catch(e){ return iso; }
}
function dayKey(d){ d = d || new Date(); return d.toISOString().slice(0,10); }

/* ── پیشرفت: ثبت زمان ── */
function studyLog(){ return STATE.progress.daily_log || (STATE.progress.daily_log = {}); }
function logStudy(min, quiet){
  if(!min) return;
  const k = dayKey();
  studyLog()[k] = Math.max(0, (studyLog()[k]||0) + min);
  if(!quiet) saveProgress();
}

/* ── زمان کل محتوای برنامه (کتاب‌ها + بانک کنکور) ── */
function totalProgramMinutes(){
  let bookMin = 0, chs = 0;
  if(typeof allBooks === "function"){
    allBooks().forEach(b=>{ bookMin += b.minutes; chs += b.chapters.length; });
  }
  const konkur = (typeof KONKUR_TOTAL !== "undefined" ? KONKUR_TOTAL : 1200) * 3;   // هر سؤال کنکور ≈ ۳ دقیقه
  return { bookMin: bookMin, chs: chs, konkurMin: konkur, total: bookMin + konkur };
}

/* ── دقیقه‌های مطالعه‌شده ── */
function studiedMinutes(){
  let s = 0;
  Object.keys(studyLog()).forEach(k=>{ s += studyLog()[k]; });
  return s;
}
/* پیشرفت قبل از v1.3 را یک‌بار به آمار اضافه می‌کند تا عدد واقعی باشد */
function seedStudyLog(){
  if(STATE.progress.daily_log) return;
  STATE.progress.daily_log = {};
  let est = 0;
  if(typeof allBooks === "function" && typeof chapterKey === "function"){
    allBooks().forEach(b=>b.chapters.forEach(c=>{
      if(STATE.progress.completed_lessons.includes(chapterKey(b.sid,c.id))) est += (c.minutes||30);
    }));
  }
  const q = (STATE.progress.quiz_stats||{}).total || 0;
  let konkurQ = 0;
  Object.values(STATE.progress.konkur_results||{}).forEach(r=>{ konkurQ += (r.total_q || r.total || 0); });
  est += q*2;
  if(est > 0){ STATE.progress.daily_log[dayKey()] = est; STATE.progress._seeded = true; saveProgress(); }
}

/* ── محاسبه روزها ── */
function studyPlan(){
  const tot = totalProgramMinutes();
  const studied = Math.min(studiedMinutes(), tot.total);
  const remaining = Math.max(0, tot.total - studied);
  const goal = (STATE.progress.daily_goal || 44);
  const daysLeft = Math.ceil(remaining / goal);
  const daysToExam = Math.max(0, Math.ceil((EXAM_DATE - new Date())/86400000));
  const examStr = faDate(dayKey(EXAM_DATE));
  const pct = tot.total ? Math.min(100, Math.round(studied*100/tot.total)) : 0;
  const finish = new Date(Date.now() + daysLeft*86400000);
  const weeks = Math.round(daysLeft/7);
  return { tot, studied, remaining, goal, daysLeft, daysToExam, pct, finish, weeks, examStr,
           ok: daysLeft <= daysToExam, perDay: Math.ceil(remaining/Math.max(1,daysToExam)) };
}
function progressMinutes(){ return studiedMinutes(); }
function setGoal(g){ STATE.progress.daily_goal = g; saveProgress(); render(); }

/* ── نمودار ۱۴ روز اخیر (بدون کتابخانه) ── */
function studyChartHTML(days){
  days = days || 14;
  const arr = [];
  for(let i=days-1;i>=0;i--){
    const d = new Date(Date.now() - i*86400000);
    arr.push({ k: dayKey(d), m: studyLog()[dayKey(d)] || 0, lbl: faDate(dayKey(d)) });
  }
  const max = Math.max(30, ...arr.map(a=>a.m));
  return `<div class="st-chart">${arr.map(a=>`
    <div class="st-col" title="${a.lbl}: ${faMin(a.m)}">
      <div class="st-bar-wrap"><div class="st-bar" style="height:${Math.round(a.m*100/max)}%"></div></div>
      <div class="st-lbl">${a.lbl.split(" ")[0]}</div>
    </div>`).join("")}</div>`;
}

/* ── کارت پیشرفت (داشبورد + استاد) ── */
function progressCardHTML(){
  const p = studyPlan();
  const col = p.ok ? "var(--success)" : "var(--danger)";
  return `
  <div class="card st-card">
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
      <div style="font-weight:800;font-size:16px">⏱ زمان مطالعه و برنامه‌ریزی من</div>
      <button class="btn btn-sm btn-ghost" onclick="setView('progress')">جزئیات کامل ➡️</button>
    </div>
    <div class="st-grid">
      <div class="st-box"><div class="st-num" style="color:var(--accent)">${faMin(p.studied)}</div><div class="st-lbl2">خوانده‌ام</div></div>
      <div class="st-box"><div class="st-num" style="color:var(--warning)">${faMin(p.remaining)}</div><div class="st-lbl2">باقی‌مانده از ${p.tot.chs} فصل</div></div>
      <div class="st-box"><div class="st-num" style="color:${col}">${pFa(p.daysLeft)} روز</div><div class="st-lbl2">تا تمام‌شدن (${pFa(p.goal)} دقیقه/روز)</div></div>
      <div class="st-box"><div class="st-num" style="color:var(--accent2)">${pFa(p.daysToExam)} روز</div><div class="st-lbl2">تا کنکور ارشد (${p.examStr})</div></div>
    </div>
    <div class="progress" style="margin-top:12px"><div class="progress-bar" style="width:${p.pct}%;background:linear-gradient(90deg,var(--warning),var(--success))"></div></div>
    <div style="display:flex;justify-content:space-between;font-size:12.5px;color:var(--muted);margin-top:6px">
      <span>پیشرفت کل: ${pFa(p.pct)}٪</span>
      <span>پایان تخمینی: <b style="color:var(--text)">${faDate(dayKey(p.finish))}</b> (${pFa(p.weeks)} هفته دیگر)</span>
    </div>
    <div style="font-size:13px;line-height:2.1;margin-top:10px;padding:10px 12px;border-radius:10px;background:${p.ok?"rgba(34,197,94,.10)":"rgba(239,68,68,.10)"};border-right:4px solid ${col}">
      ${p.ok
        ? `✅ عالی! با ${pFa(p.goal)} دقیقه در روز، ${pFa(p.daysToExam - p.daysLeft)} روز جلوتر از کنکور تمام می‌کنی — برای مرور وقت داری.`
        : `⚠️ با ${pFa(p.goal)} دقیقه در روز دیر می‌رسی! برای رسیدن به کنکور باید روزی <b>${pFa(p.perDay)} دقیقه</b> بخوانی.`}
    </div>
  </div>`;
}

/* ── صفحه کامل پیشرفت ── */
function renderProgress(main){
  const p = studyPlan();
  const log = studyLog();
  const last7 = (()=>{ let s=0; for(let i=0;i<7;i++) s += log[dayKey(new Date(Date.now()-i*86400000))]||0; return s; })();
  const activeDays = Object.keys(log).filter(k=>log[k]>0).length;
  // تقویم مطالعه (۳۵ روز اخیر)
  let cal = "";
  for(let i=34;i>=0;i--){
    const d = new Date(Date.now()-i*86400000), m = log[dayKey(d)]||0;
    const lvl = m===0?0:m<30?1:m<60?2:m<120?3:4;
    cal += `<div class="cal-cell lv${lvl}" title="${faDate(dayKey(d))}: ${faMin(m)}"></div>`;
  }
  // پیشرفت درسی
  let rows = "";
  if(typeof allBooks === "function" && typeof APP_DATA !== "undefined"){
    APP_DATA.subjects.forEach(s=>{
      const bs = (typeof bookList === "function") ? bookList(s.id) : [];
      const chs = bs.reduce((a,b)=>a.concat(b.chapters),[]);
      if(!chs.length) return;
      const done = chs.filter(c=>STATE.progress.completed_lessons.includes(chapterKey(s.id,c.id))).length;
      const min = chs.reduce((a,c)=>a+(c.minutes||30),0);
      const dm = chs.filter(c=>STATE.progress.completed_lessons.includes(chapterKey(s.id,c.id))).reduce((a,c)=>a+(c.minutes||30),0);
      const pc = Math.round(done*100/chs.length);
      rows += `<div class="st-row"><span class="st-row-n">${s.emoji} ${s.name}</span>
        <span class="st-row-b"><span class="bar" style="display:block"><span class="bar-fill" style="display:block;width:${pc}%"></span></span></span>
        <span class="st-row-v">${pFa(done)}/${pFa(chs.length)} فصل • ${faMin(dm)} از ${faMin(min)}</span></div>`;
    });
  }
  const goalBtns = GOAL_OPTIONS.map(g=>`<button class="btn btn-sm ${p.goal===g?"btn-primary":"btn-ghost"}" onclick="setGoal(${g})">${pFa(g)} دقیقه/روز</button>`).join(" ");
  const db = p.tot;
  main.innerHTML = `
    <div class="page-head"><h1>⏱ زمان مطالعه و برنامه من</h1>
      <p>دقیقاً می‌دانی چقدر خوانده‌ای، چقدر مانده و با این روند چند روز دیگر تمام می‌شود.</p></div>

    <div class="big-stats st4">
      <div class="big-stat"><div class="num" style="color:var(--accent)">${faMin(p.studied)}</div><div class="lbl">مجموع مطالعه‌ام</div></div>
      <div class="big-stat"><div class="num" style="color:var(--warning)">${faMin(p.remaining)}</div><div class="lbl">باقی‌مانده</div></div>
      <div class="big-stat"><div class="num" style="color:${p.ok?"var(--success)":"var(--danger)"}">${pFa(p.daysLeft)}</div><div class="lbl">روز تا پایان برنامه</div></div>
      <div class="big-stat"><div class="num" style="color:var(--accent2)">${pFa(p.daysToExam)}</div><div class="lbl">روز تا کنکور</div></div>
    </div>

    ${progressCardHTML()}

    <div class="card">
      <div style="font-weight:800;margin-bottom:6px">🎯 هدف مطالعه روزانه</div>
      <div style="font-size:13px;color:var(--muted);margin-bottom:10px">اگر روزی ${pFa(p.goal)} دقیقه بخوانی، ${pFa(p.daysLeft)} روز دیگر تمام می‌شود. (${pFa(p.weeks)} هفته)</div>
      <div style="display:flex;gap:8px;flex-wrap:wrap">${goalBtns}</div>
      <div style="margin-top:10px;font-size:12.5px;color:var(--muted)">
        حجم کل برنامه: ${faMin(db.total)} — شامل ${pFa(db.chs)} فصل کتاب (${faMin(db.bookMin)}) و بانک کنکور ${pFa(Math.round(db.konkurMin/3))} سؤال (${faMin(db.konkurMin)})
      </div>
    </div>

    <div class="section-title">📈 ۱۴ روز اخیر</div>
    <div class="card">
      ${studyChartHTML(14)}
      <div style="display:flex;justify-content:space-between;font-size:13px;color:var(--muted);margin-top:10px">
        <span>هفته گذشته: <b style="color:var(--accent)">${faMin(last7)}</b></span>
        <span>روزهای فعال: <b style="color:var(--success)">${pFa(activeDays)} روز</b></span>
        <span>میانگین روزانه: <b style="color:var(--warning)">${faMin(p.studied/Math.max(1,activeDays))}</b></span>
      </div>
    </div>

    <div class="section-title">🗓 تقویم ۵ هفته اخیر</div>
    <div class="card"><div class="st-cal">${cal}</div>
      <div class="st-legend"><span>کم</span><span class="cal-cell lv0"></span><span class="cal-cell lv1"></span><span class="cal-cell lv2"></span><span class="cal-cell lv3"></span><span class="cal-cell lv4"></span><span>زیاد</span></div>
    </div>

    <div class="section-title">📚 پیشرفت به تفکیک درس</div>
    <div class="card">${rows || "<p>اولین فصل را از بخش کتابخانه شروع کن.</p>"}</div>`;
}
