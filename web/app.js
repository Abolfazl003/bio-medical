/* =====================================================
   BME MSc Konkur Prep — Web UI v2
   Features: subject-sorted random quiz, green/red instant feedback,
   konkori trick + full solution, save for review, teacher mode,
   free books, saved questions
===================================================== */
/* ---- ذخیره‌سازی امن (در حالت private یا iframe سندباکس هم خطا نمی‌دهد) ---- */
function lsGet(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
function lsSet(k,v){ try{ localStorage.setItem(k,v); return true; }catch(e){ return false; } }
function lsDel(k){ try{ localStorage.removeItem(k); }catch(e){} }

const LS_KEY = "bme_konkur_progress_v2";

const STATE = {
  progress: loadProgress(),
  view: "dashboard",
  activeSubject: null,
  quiz: null,
  exam: null,
  teacher: null,    // {subject, slideIdx}
  timerHandle: null,
};

function loadProgress(){
  try {
    const raw = lsGet(LS_KEY);
    if (raw) {
      const p = JSON.parse(raw);
      if(!p.completed_lessons) p.completed_lessons = [];
      if(!p.bookmarks) p.bookmarks = [];
      if(!p.saved_questions) p.saved_questions = [];
      if(!p.quiz_stats) p.quiz_stats = {correct:0,total:0};
      if(!p.exam_results) p.exam_results = [];
      if(!p.konkur_results) p.konkur_results = {};
      return p;
    }
  } catch(e){}
  return {
    bookmarks:[],
    saved_questions:[],   // سوالاتی که ذخیره کرده برای مرور
    completed_lessons:[],
    quiz_stats:{correct:0,total:0},
    exam_results:[],
    konkur_results:{},   // نتایج آزمون‌های درس‌به‌درس کنکورهای ۱۰ سال اخیر
    theme:"dark"
  };
}
function saveProgress(){ lsSet(LS_KEY, JSON.stringify(STATE.progress)); updateSidebarStat(); }

const $ = s=>document.querySelector(s);
const $$ = s=>[...document.querySelectorAll(s)];
function shuffle(a){const b=[...a];for(let i=b.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[b[i],b[j]]=[b[j],b[i]];}return b;}
const EXAM_META={
  math:{n:"ریاضیات",e:"📐",c:"#3b82f6"}, physics:{n:"فیزیک",e:"⚡",c:"#8b5cf6"},
  circuits:{n:"مدارهای الکتریکی",e:"🔌",c:"#f59e0b"}, electronics:{n:"الکترونیک",e:"🔧",c:"#ef4444"},
  signals:{n:"سیگنال‌ها و سیستم‌ها",e:"📡",c:"#10b981"}, control:{n:"کنترل سیستم‌ها",e:"🎛️",c:"#6366f1"},
  instrumentation:{n:"ابزار دقیق پزشکی",e:"🩺",c:"#06b6d4"}, imaging:{n:"تصویربرداری پزشکی",e:"🖼️",c:"#a855f7"},
  biomaterials:{n:"بیومواد",e:"🧪",c:"#f97316"}, biomechanics:{n:"بیومکانیک",e:"🦴",c:"#14b8a6"},
  anatomy:{n:"آناتومی و فیزیولوژی",e:"🫀",c:"#ec4899"}
};
function subColor(id){const s=APP_DATA.subjects.find(x=>x.id===id);return s?s.color:(EXAM_META[id]?EXAM_META[id].c:"#38bdf8");}
function subName(id){const s=APP_DATA.subjects.find(x=>x.id===id);if(s)return s.name;
  if(typeof PK!=="undefined"&&PK.subjects&&PK.subjects[id])return PK.subjects[id];
  return EXAM_META[id]?EXAM_META[id].n:id;}
function subEmoji(id){const s=APP_DATA.subjects.find(x=>x.id===id);if(s)return s.emoji;
  return EXAM_META[id]?EXAM_META[id].e:"📘";}
function letterOf(i){return ["الف","ب","ج","د"][i]||"?";}

function updateSidebarStat(){
  const s=STATE.progress.quiz_stats;
  const acc = s.total?Math.round(s.correct*100/s.total):0;
  const saved = (STATE.progress.saved_questions||[]).length;
  const el = document.getElementById("sidebar-stat-body");
  if(el) el.innerHTML = `سوالات پاسخ‌داده: <b>${s.total}</b><br>درست: <b style="color:var(--success)">${s.correct}</b> (${acc}%)<br>سوالات ذخیره: <b style="color:var(--warning)">${saved}</b>`;
}

/* ---- nav ---- */
function setView(v){
  STATE.view = v;
  $$(".nav-btn").forEach(b=>b.classList.toggle("active", b.dataset.view===v));
  render();
  document.getElementById("main").scrollTop=0;
}

/* ---- دکمه بازگشت سیستم (اندروید/دسکتاپ) ----
   اگر داخل صفحه‌ای بودیم که باید اول برگرده، true برمی‌گرداند */
function appBack(){
  const v = STATE.view;
  // اگر منویی بازه، اول اون بسته بشه
  const openModal = document.querySelector(".modal-backdrop");
  if(openModal){ openModal.remove(); return true; }
  const map = {
    "subject-detail":"subjects",
    "book":"subjects",
    "book-chapter":"book",
    "teacher-lesson":"teacher",
    "foundation-lesson":"foundation",
    "quiz-playing":"quiz",
    "quiz-result":"quiz",
    "exam-playing":"exams",
    "exam-result":"exams",
    "practice-playing":"practice",
    "practice-result":"practice",
    "savedq":"dashboard",
    "bookmarks":"dashboard",
    "freebooks":"dashboard"
  };
  if(map[v]){
    if(STATE.timerHandle){clearInterval(STATE.timerHandle);STATE.timerHandle=null;}
    setView(map[v]);
    return true;
  }
  return false;  // در صفحه اصلی => خروج
}
window.appBack = appBack;

/* ---- تشخیص پلتفرم بومی ---- */
const IS_NATIVE = !!(window.Android || window.pywebview);

function render(){
  const main = $("#main");
  main.classList.remove("fade"); void main.offsetWidth; main.classList.add("fade");
  const v=STATE.view;
  if(v==="dashboard") renderDashboard(main);
  else if(v==="subjects") renderSubjects(main);
  else if(v==="book") renderBookHome(STATE.activeSubject);
  else if(v==="book-chapter"){const o=STATE._bookOpen; if(o) renderBookChapter(o.sid,o.chId); else setView("subjects");}
  else if(v==="subject-detail") renderSubjectDetail(main);
  else if(v==="quiz") renderQuizHome(main);
  else if(v==="quiz-playing") renderQuiz(main);
  else if(v==="quiz-result") renderQuizResult(main);
  else if(v==="exams") renderExamsHome(main);
  else if(v==="konkur") renderKonkurHome(main);
  else if(v==="konkur-year") renderKonkurYear(main);
  else if(v==="exam-playing") renderExam(main);
  else if(v==="exam-result") renderExamResult(main);
  else if(v==="books") renderBooks(main);
  else if(v==="freebooks") renderFreeBooks(main);
  else if(v==="bookmarks") renderBookmarks(main);
  else if(v==="savedq") renderSavedQuestions(main);
  else if(v==="teacher") renderTeacherHome(main);
  else if(v==="teacher-lesson") renderTeacherLesson(main);
  else if(v==="foundation") renderFoundationHome(main);
  else if(v==="foundation-lesson") renderFoundationLesson(main);
  else if(v==="practice") renderPracticeHome(main);
  else if(v==="practice-playing") renderPracticeQuiz(main);
  else if(v==="practice-result") renderPracticeResult(main);
  else if(v==="settings") renderSettings(main);
  updateSidebarStat();
}

/* -------- Dashboard -------- */
function renderDashboard(main){
  const totalLessons = APP_DATA.subjects.reduce((a,s)=>a+s.lessons.length,0);
  const totalQ = APP_DATA.all_pool.length;
  const s=STATE.progress.quiz_stats;
  const acc = s.total?Math.round(s.correct*100/s.total):0;
  const last = STATE.progress.exam_results.slice(-1)[0];
  main.innerHTML = `
    <div class="page-head"><h1>سلام! خوش اومدی 👋</h1>
    <p>مطالعه درس‌نامه، تست ترکیبی شافل مبحثی، آزمون‌های ۱۰ ساله، و تدریس خصوصی با استاد 🧑‍🏫</p></div>
    <div class="big-stats">
      <div class="big-stat"><div class="num" style="color:var(--accent)">${totalLessons}</div><div class="lbl">فصل درس‌نامه 📖</div></div>
      <div class="big-stat"><div class="num" style="color:var(--accent2)">${totalQ}</div><div class="lbl">سوال تستی 📝</div></div>
      <div class="big-stat"><div class="num" style="color:var(--success)">${acc}%</div><div class="lbl">درصد صحیح ✅</div></div>
    </div>
    <div class="section-title">🚀 شروع سریع</div>
    <div class="grid-cards">
      <div class="card clickable" onclick="setView('foundation')"><div class="emoji">🎒</div><h3>دوره پایه تا پیشرفته</h3><p>از صفرِ صفر درس بخون، انگار هیچی بلد نیستی، برو تا سطح کنکور</p>
        <div class="card-actions"><button class="btn btn-primary" style="background:var(--warning);color:#0f172a">شروع از پایه</button></div></div>
      <div class="card clickable" onclick="startMixedQuiz()"><div class="emoji">🎲</div><h3>تست ترکیبی مبحثی شافل</h3><p>۲۰ سوال مبحث‌به‌مبحث از سال‌های مختلف، هر بار جدید</p>
        <div class="card-actions"><button class="btn btn-primary">شروع تست تمرینی</button></div></div>
      <div class="card clickable" onclick="setView('practice')"><div class="emoji">✏️</div><h3>سوالات تمرینی تالیفی</h3><p>آموزش قبل از جواب + جواب تشریحی، مبحث به مبحث</p>
        <div class="card-actions"><button class="btn btn-success">شروع تمرین</button></div></div>
      <div class="card clickable" onclick="startExam(${APP_DATA.exams.length-1})"><div class="emoji">🎓</div><h3>آزمون سال اخیر</h3><p>۶۰ دقیقه، ۲۵ سوال با تایمر</p>
        <div class="card-actions"><button class="btn btn-secondary">آزمون جامع</button></div></div>
      <div class="card clickable" onclick="setView('teacher')"><div class="emoji">🧑‍🏫</div><h3>کلاس با استاد</h3><p>تدریس تعاملی درس به درس</p>
        <div class="card-actions"><button class="btn" style="background:var(--warning);color:#0f172a">شروع کلاس</button></div></div>
      <div class="card clickable" onclick="setView('books')"><div class="emoji">📕</div><h3>کتاب درسی کامل</h3><p>۱۰ کتاب با ۴۰ فصل، فرمول و مثال حل‌شده</p>
        <div class="card-actions"><button class="btn btn-primary">مطالعه کتاب</button></div></div>
      <div class="card clickable" onclick="setView('freebooks')"><div class="emoji">🔗</div><h3>کتاب‌های رایگان</h3><p>لینک منابع آزاد قانونی برای مطالعه عمیق</p>
        <div class="card-actions"><button class="btn btn-ghost">مشاهده</button></div></div>
    </div>
    <div class="section-title">📚 دروس</div>
    <div class="grid-cards" id="subjects-grid"></div>
    <div class="section-title">⭐ دسترسی سریع</div>
    <div class="grid-cards">
      <div class="card clickable" onclick="setView('savedq')"><div class="emoji">💾</div><h3>سوالات ذخیره‌شده (${(STATE.progress.saved_questions||[]).length})</h3><p>سوالات مهمی که ذخیره کردی برای مرور</p></div>
      <div class="card clickable" onclick="setView('freebooks')"><div class="emoji">🔗</div><h3>کتاب‌های رایگان</h3><p>لینک‌های قانونی و آزاد منابع درسی</p></div>
      <div class="card clickable" onclick="setView('books')"><div class="emoji">📕</div><h3>کتابخانه درسی (۱۰ کتاب کامل)</h3><p>کتاب کامل هر درس + معرفی ۲۰ منبع مرجع کنکور</p></div>
    </div>
    ${last?`<div class="section-title">🏅 آخرین آزمون</div>
      <div class="card"><div style="font-weight:700;font-size:18px;color:var(--warning)">دوره ${last.year} — ${last.score} از ${last.total} (${Math.round(last.score*100/last.total)}%) <span style="font-size:12px;color:var(--muted)">${last.date||""}</span></div></div>`:""}
  `;
  const g=$("#subjects-grid");
  APP_DATA.subjects.forEach(s=>{
    const qc=(APP_DATA.question_bank[s.id]||[]).length;
    const lc=s.lessons.length;
    const el=document.createElement("div");el.className="card clickable";
    el.innerHTML=`<div class="emoji">${s.emoji}</div><h3>${s.name}</h3><p>${lc} فصل • ${qc} سوال</p>
      <div class="card-actions">
        <button class="btn btn-sm btn-primary" data-act="study">📖 مطالعه</button>
        <button class="btn btn-sm btn-secondary" data-act="quiz">📝 تست</button>
        <button class="btn btn-sm" data-act="teacher" style="background:var(--warning);color:#0f172a">🧑‍🏫 استاد</button>
      </div>`;
    el.querySelector("h3").style.color=s.color;
    el.addEventListener("click",e=>{
      const act=e.target.dataset.act;
      if(act==="quiz") startQuiz(s.id);
      else if(act==="teacher") openTeacher(s.id);
      else openSubject(s.id);
    });
    g.appendChild(el);
  });
}

/* ---- Subjects ---- */
function renderSubjects(main){
  main.innerHTML=`<div class="page-head"><h1>📚 دروس و سرفصل‌ها</h1><p>یک درس را انتخاب کن</p></div><div class="grid-cards" id="g"></div>`;
  const g=$("#g");
  APP_DATA.subjects.forEach(s=>{
    const qc=(APP_DATA.question_bank[s.id]||[]).length, lc=s.lessons.length;
    const el=document.createElement("div");el.className="card clickable";
    el.innerHTML=`<div class="emoji">${s.emoji}</div><h3>${s.name}</h3><p>${lc} فصل • ${qc} سوال</p>
      <div class="card-actions">
        <button class="btn btn-sm btn-primary" data-act="study">📖 مطالعه</button>
        <button class="btn btn-sm btn-secondary" data-act="quiz">📝 تست</button>
        <button class="btn btn-sm" data-act="teacher" style="background:var(--warning);color:#0f172a">🧑‍🏫 استاد</button>
      </div>`;
    el.querySelector("h3").style.color=s.color;
    el.addEventListener("click",e=>{
      const act=e.target.dataset.act;
      if(act==="quiz") startQuiz(s.id);
      else if(act==="teacher") openTeacher(s.id);
      else openSubject(s.id);
    });
    g.appendChild(el);
  });
}
function openSubject(id){STATE.activeSubject=id;setView("subject-detail");}

function renderSubjectDetail(main){
  const s=APP_DATA.subjects.find(x=>x.id===STATE.activeSubject);
  const qc=(APP_DATA.question_bank[s.id]||[]).length;
  main.innerHTML=`
    <div class="card" style="background:linear-gradient(135deg,${s.color}22,transparent);border-color:${s.color}44;margin-bottom:16px">
      <div style="display:flex;gap:18px;align-items:center;flex-wrap:wrap">
        <div style="font-size:56px">${s.emoji}</div>
        <div style="flex:1;min-width:240px"><h2 style="font-size:22px">${s.name}</h2>
        <div style="color:var(--muted);font-size:13px">${s.lessons.length} فصل • ${qc} سوال</div></div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          ${hasBook(s.id)?`<button class="btn btn-primary" onclick="openBookHome('${s.id}')">📕 کتاب کامل (${bookChapterCount(s.id)} فصل)</button>`:""}
          <button class="btn" style="background:var(--accent2);color:#fff" onclick="startQuiz('${s.id}')">📝 تست این درس</button>
          <button class="btn" style="background:var(--warning);color:#0f172a" onclick="openTeacher('${s.id}')">🧑‍🏫 تدریس استاد</button>
          <button class="btn btn-ghost" onclick="setView('subjects')">🔙</button>
        </div>
      </div>
    </div>
    <div class="section-title">📖 سرفصل‌ها</div><div id="lessons"></div>`;
  const box=$("#lessons");
  s.lessons.forEach((L,i)=>{
    const key=`${s.id}__${i+1}`, done=STATE.progress.completed_lessons.includes(key);
    const bm=STATE.progress.bookmarks.some(b=>b.title===L.title);
    const el=document.createElement("div");el.className="lesson";
    el.innerHTML=`<div class="lesson-head">
        <div class="lesson-num" style="background:${s.color}">${i+1}</div>
        <div class="lesson-title">${L.title}</div>${done?`<span class="badge">✅ خوانده شد</span>`:""}</div>
      <div class="lesson-content" dir="rtl">${L.content.replace(/\n/g,"<br>")}</div>
      <div class="lesson-foot">
        <button class="btn btn-sm ${bm?'btn-primary':'btn-ghost'}" data-bm="1">${bm?'⭐ نشان شده':'☆ نشان کردن'}</button>
        <button class="btn btn-sm ${done?'btn-success':'btn-ghost'}" data-done="1">${done?'✅ مطالعه شده':'⬜ علامت خوانده‌شده'}</button>
      </div>`;
    el.querySelector("[data-bm]").onclick=()=>{
      const ex=STATE.progress.bookmarks.findIndex(b=>b.title===L.title);
      if(ex>=0) STATE.progress.bookmarks.splice(ex,1);
      else STATE.progress.bookmarks.push({type:"lesson",subject:s.id,title:L.title,content:L.content});
      saveProgress();render();
    };
    el.querySelector("[data-done]").onclick=()=>{
      const k=STATE.progress.completed_lessons.indexOf(key);
      if(k>=0) STATE.progress.completed_lessons.splice(k,1);
      else STATE.progress.completed_lessons.push(key);
      saveProgress();render();
    };
    box.appendChild(el);
  });
}

/* ---- Quiz Home + Mixed Quiz ---- */
function renderQuizHome(main){
  main.innerHTML=`<div class="page-head"><h1>📝 بانک سوالات</h1><p>یکی از دروس را انتخاب یا تست ترکیبی مبحثی شافل بزن</p></div>
    <div class="grid-cards" id="qg"></div>`;
  const g=$("#qg");
  const mix=document.createElement("div");mix.className="card clickable";
  mix.innerHTML=`<div class="emoji">🎲</div><h3>تست ترکیبی مبحثی شافل</h3><p>۲۰ سوال از تمام سال‌ها، مرتب‌شده بر اساس مبحث (هر بار که می‌زنی سوالات جدید و چینش متفاوت)</p>
    <div class="card-actions"><button class="btn btn-primary">شروع تست تمرینی</button></div>`;
  mix.onclick=startMixedQuiz;g.appendChild(mix);
  APP_DATA.subjects.forEach(s=>{
    const qc=(APP_DATA.question_bank[s.id]||[]).length;
    const el=document.createElement("div");el.className="card clickable";
    el.innerHTML=`<div class="emoji">${s.emoji}</div><h3>${s.name}</h3><p>${qc} سوال</p>
      <div class="card-actions"><button class="btn" style="background:${s.color};color:#fff">شروع</button></div>`;
    el.onclick=()=>startQuiz(s.id);
    g.appendChild(el);
  });
}

/* تست ترکیبی مبحثی:
   سوالات را به تفکیک مبحث گروه می‌کند، داخل هر مبحث شافل می‌کرد، سپس به صورت مبحث‌به‌مبحث (نه درهم) پشت سر هم می‌گذارد.
   هر بار اجرا کاملاً شافل جدید.
*/
function startMixedQuiz(){
  // گروه‌بندی بر اساس subject
  const groups = {};
  APP_DATA.all_pool.forEach(q=>{
    if(!groups[q.subject]) groups[q.subject]=[];
    groups[q.subject].push({...q});
  });
  // داخل هر گروه شافل و چندتایی برمی‌داریم
  let pick=[];
  Object.keys(groups).forEach(sid=>{
    groups[sid] = shuffle(groups[sid]);
    pick = pick.concat(groups[sid].slice(0,2)); // 2 سوال از هر درس = 20 سوال
  });
  // مرتب‌سازی مبحث به مبحث (همه از یک درس کنار هم)، اما ترتیب مباحث را هم شافل می‌کنیم
  // در بالا ترتیب دروس مطابق SUBJECTS است. برای اینکه درس‌ها هم شافل شوند ولی داخل هر درس پیوسته باشد:
  // ابتدا آرایه دروس را شافل می‌کنیم، سپس بر اساس آن pick را بازچینی:
  const subject_ids = shuffle(APP_DATA.subjects.map(s=>s.id));
  const ordered = [];
  subject_ids.forEach(sid=>{
    ordered.push(...pick.filter(q=>q.subject===sid));
  });
  STATE.quiz = {questions:ordered.slice(0,20), idx:0, correct:0, subject:"ترکیبی مبحثی (شافل شده)"};
  setView("quiz-playing");
}
function startQuiz(sid){
  const qs=(APP_DATA.question_bank[sid]||[]).map(q=>({...q,subject:sid}));
  const questions=shuffle(qs).slice(0,Math.min(qs.length,20));
  const subj=APP_DATA.subjects.find(s=>s.id===sid);
  STATE.quiz={questions,idx:0,correct:0,subject:subj?subj.name:""};
  setView("quiz-playing");
}

function renderQuiz(main){
  const Q=STATE.quiz;if(!Q){setView("quiz");return;}
  if(Q.idx>=Q.questions.length){renderQuizResult(main);return;}
  const q=Q.questions[Q.idx];
  const pct=(Q.idx/Q.questions.length)*100;
  const isSaved = (STATE.progress.saved_questions||[]).some(x=>x.q===q.q && x.subject===q.subject);
  main.innerHTML=`
    <div class="quiz-wrap">
      <div class="quiz-meta">
        <div>سوال <b>${Q.idx+1}</b> از ${Q.questions.length} — <span style="color:${subColor(q.subject)}">${subEmoji(q.subject)} ${subName(q.subject)}</span>${q.year?` <span style="color:var(--muted);font-size:12px">• کنکور ${q.year}</span>`:""}</div>
        <div>درست: <b style="color:var(--success)">${Q.correct}</b></div>
      </div>
      <div class="progress"><div class="progress-bar" style="width:${pct}%"></div></div>
      <div class="q-card">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px">
          <div class="q-text" style="flex:1">${q.q}</div>
          <button class="btn btn-sm ${isSaved?'btn-primary':'btn-ghost'}" id="saveBtn" title="ذخیره برای مرور">${isSaved?'💾 ذخیره شد':'💾 ذخیره'}</button>
        </div>
        <div id="choices">
          ${q.choices.map((c,i)=>`<div class="choice" data-i="${i}"><div class="letter">${letterOf(i)}</div><div>${c}</div></div>`).join("")}
        </div>
        <div class="explain" id="explain" style="display:none"></div>
        <div class="q-actions">
          <button class="btn btn-ghost" onclick="setView('quiz')">🔙 انصراف</button>
          <div style="display:flex;gap:8px">
            <button class="btn btn-success" id="checkBtn" onclick="checkAnswer()">✅ ثبت پاسخ</button>
            <button class="btn btn-primary" id="nextBtn" style="display:none" onclick="nextQuestion()">بعدی ➡️</button>
          </div>
        </div>
      </div>
    </div>`;
  $$("#choices .choice").forEach(c=>c.onclick=()=>{
    if($("#checkBtn").disabled) return;
    $$("#choices .choice").forEach(x=>x.classList.remove("selected"));
    c.classList.add("selected");
  });
  $("#saveBtn").onclick=()=>{
    const saved = STATE.progress.saved_questions||(STATE.progress.saved_questions=[]);
    const exists = saved.findIndex(x=>x.q===q.q && x.subject===q.subject);
    if(exists>=0){ saved.splice(exists,1); $("#saveBtn").textContent="💾 ذخیره"; $("#saveBtn").classList.remove("btn-primary"); $("#saveBtn").classList.add("btn-ghost");}
    else{ saved.push({...q}); $("#saveBtn").textContent="💾 ذخیره شد"; $("#saveBtn").classList.add("btn-primary"); $("#saveBtn").classList.remove("btn-ghost");}
    saveProgress();
  };
}
function checkAnswer(){
  const Q=STATE.quiz;const q=Q.questions[Q.idx];
  const chosenEl=document.querySelector("#choices .choice.selected");
  if(!chosenEl){alert("لطفاً یک گزینه را انتخاب کن");return;}
  const chosen=parseInt(chosenEl.dataset.i);
  STATE.progress.quiz_stats.total++;
  $$("#choices .choice").forEach(c=>{
    const idx=parseInt(c.dataset.i);
    if(idx===q.answer) c.classList.add("correct");
    if(idx===chosen && chosen!==q.answer) c.classList.add("wrong");
    c.style.pointerEvents="none";
  });
  const ex=$("#explain");
  const correct_letter = letterOf(q.answer);
  const konkori = q.konkori||"";
  const full_sol = q.full_solution||"";
  if(chosen===q.answer){
    Q.correct++;STATE.progress.quiz_stats.correct++;
    ex.innerHTML = `<div style="color:var(--success);font-weight:700;margin-bottom:8px">✅ پاسخ صحیح بود!</div>
      <div style="background:rgba(245,158,11,.1);padding:8px;border-radius:8px;margin-bottom:8px"><b style="color:var(--warning)">🎯 راه حل کنکوری:</b><br>${konkori}</div>
      <div style="background:rgba(56,189,248,.08);padding:8px;border-radius:8px"><b style="color:var(--accent)">📚 توضیح کامل:</b><br>${full_sol}</div>`;
    ex.style.borderColor="var(--success)";
    ex.style.background="rgba(34,197,94,.10)";
  } else {
    ex.innerHTML = `<div style="color:var(--danger);font-weight:700;margin-bottom:8px">❌ پاسخ اشتباه! گزینه صحیح <b>${correct_letter}</b> بود.</div>
      <div style="background:rgba(245,158,11,.1);padding:8px;border-radius:8px;margin-bottom:8px"><b style="color:var(--warning)">🎯 راه حل کنکوری:</b><br>${konkori}</div>
      <div style="background:rgba(56,189,248,.08);padding:8px;border-radius:8px"><b style="color:var(--accent)">📚 توضیح کامل:</b><br>${full_sol}</div>`;
    ex.style.borderColor="var(--danger)";
    ex.style.background="rgba(239,68,68,.10)";
  }
  ex.style.display="block";
  $("#checkBtn").disabled=true;$("#checkBtn").style.opacity=.4;
  $("#nextBtn").style.display="inline-block";
  saveProgress();
}
function nextQuestion(){STATE.quiz.idx++;render();}
function renderQuizResult(main){
  const Q=STATE.quiz;const pct=Math.round(Q.correct*100/Q.questions.length);
  // ثبت نتیجه آزمون کنکورهای ۱۰ سال اخیر
  if(Q.konkur && Q.konkur.year && Q.konkur.sid){
    const all=(STATE.progress.konkur_results||(STATE.progress.konkur_results={}));
    const key=Q.konkur.year+"__"+Q.konkur.sid;
    const prev=all[key];
    all[key]={score:Q.correct, total:Q.questions.length, date:new Date().toLocaleDateString("fa-IR"),
              best: Math.max(prev?prev.best||0:0, Q.correct), attempts:((prev&&prev.attempts)||0)+1};
    saveProgress();
  }
  const msg = pct>=75?"عالی بود! 👏":pct>=50?"خوب بود، بیشتر تمرین کن 💪":"لازم است درس‌نامه را مرور کنی 📖";
  main.innerHTML=`<div class="quiz-wrap"><div class="result">
    <h2>🎉 پایان تست</h2><div class="score">${pct}%</div>
    <div>${Q.correct} درست از ${Q.questions.length} سوال — ${Q.subject}</div>
    <div class="msg">${msg}</div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:center;flex-wrap:wrap">
      <button class="btn btn-primary" onclick="${Q.subject.includes('ترکیبی')?'startMixedQuiz()':`startQuiz('${Q.questions[0].subject}')`}">🔁 تست مجدد</button>
      <button class="btn" style="background:var(--warning);color:#0f172a" onclick="setView('savedq')">💾 مرور سوالات ذخیره‌شده</button>
      <button class="btn btn-ghost" onclick="setView('dashboard')">🏠 داشبورد</button>
    </div></div></div>`;
  STATE.quiz=null;
}

/* ---- Exams (same as before, improved answer display) ---- */
function renderExamsHome(main){
  main.innerHTML=`<div class="page-head"><h1>🎓 آزمون‌های ۱۰ سال اخیر</h1><p>۶۰ دقیقه، ۲۵ سوال — با کارنامه تشریحی</p>
    <div style="margin-top:12px"><button class="btn btn-primary" onclick="setView('konkur')">🏛 بانک کامل کنکورهای ۱۰ سال — درس به درس</button></div></div>
    <div class="section-title">📝 آزمون‌های جامع شبیه‌سازی‌شده</div><div class="grid-cards" id="eg"></div>`;
  const g=$("#eg");
  APP_DATA.exams.forEach((e,i)=>{
    const prev=STATE.progress.exam_results.find(r=>r.year===e.year);
    const el=document.createElement("div");el.className="card clickable";
    el.innerHTML=`<div style="font-size:30px;font-weight:800;color:var(--accent2);line-height:1.3">${e.year}</div><h3>کنکور جامع ۲۵ سوالی</h3><p>${e.questions.length} سوال • ۶۰ دقیقه</p>
      ${prev?`<p style="color:var(--success);font-weight:700">آخرین نتیجه: ${Math.round(prev.score*100/prev.total)}%</p>`:""}
      <div class="card-actions"><button class="btn btn-secondary">شروع آزمون</button></div>`;
    el.onclick=()=>startExam(i);g.appendChild(el);
  });
}
function startExam(i){
  const exam=APP_DATA.exams[i];
  STATE.exam={idx:0,correct:0,year:exam.year,title:exam.title,
    questions:exam.questions,answers:Array(exam.questions.length).fill(-1),
    remaining:60*60,startTs:Date.now(),submitted:false};
  setView("exam-playing");startExamTimer();
}
function startExamTimer(){
  if(STATE.timerHandle){clearInterval(STATE.timerHandle);}
  STATE.timerHandle=setInterval(()=>{
    if(STATE.view!=="exam-playing"||!STATE.exam||STATE.exam.submitted){clearInterval(STATE.timerHandle);return;}
    STATE.exam.remaining--;
    if(STATE.exam.remaining<=0){clearInterval(STATE.timerHandle);submitExam(true);return;}
    const t=$("#ex-timer");if(!t)return;
    const m=Math.floor(STATE.exam.remaining/60),s=STATE.exam.remaining%60;
    t.textContent=`⏱️  ${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
  },1000);
}
function renderExam(main){
  const E=STATE.exam;if(!E){setView("exams");return;}
  const q=E.questions[E.idx];const pct=((E.idx+1)/E.questions.length)*100;
  const answered=E.answers.filter(a=>a!==-1).length;
  main.innerHTML=`<div class="quiz-wrap">
    <div class="quiz-meta"><div>دوره ${E.year} • سوال <b>${E.idx+1}</b> از ${E.questions.length}</div><div class="timer" id="ex-timer"></div></div>
    <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,var(--accent2),var(--warning))"></div></div>
    <div class="q-nav" id="qnav">${E.questions.map((_,qi)=>{
      const ans=E.answers[qi];const cls=qi===E.idx?"active":(ans!==-1?"answered":"");
      return `<button class="${cls}" data-jump="${qi}">${qi+1}</button>`;}).join("")}</div>
    <div class="q-card">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px">
        <div class="q-text" style="flex:1">${q.q}</div>
        <button class="btn btn-sm btn-ghost" id="saveBtn">💾 ذخیره</button>
      </div>
      <div id="choices">${q.choices.map((c,i)=>`<div class="choice ${E.answers[E.idx]===i?'selected':''}" data-i="${i}"><div class="letter">${letterOf(i)}</div><div>${c}</div></div>`).join("")}</div>
      <div class="q-actions">
        <button class="btn btn-danger" onclick="submitExam(false)">پایان آزمون</button>
        <div style="display:flex;gap:8px">
          ${E.idx>0?'<button class="btn btn-ghost" onclick="jumpQ('+(E.idx-1)+')">⬅️ قبلی</button>':""}
          ${E.idx<E.questions.length-1?'<button class="btn btn-secondary" onclick="saveAndNext()">ذخیره و بعدی ➡️</button>':'<button class="btn btn-success" onclick="submitExam(false)">✅ ثبت و پایان</button>'}
        </div></div></div>
    <div style="margin-top:10px;color:var(--muted);font-size:12px">پاسخ‌داده: ${answered} از ${E.questions.length}</div></div>`;
  const m=Math.floor(E.remaining/60),s=E.remaining%60;
  $("#ex-timer").textContent=`⏱️  ${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
  $$("#choices .choice").forEach(c=>c.onclick=()=>{
    $$("#choices .choice").forEach(x=>x.classList.remove("selected"));
    c.classList.add("selected");E.answers[E.idx]=parseInt(c.dataset.i);});
  $$("#qnav button").forEach(b=>b.onclick=()=>{
    E.answers[E.idx]=parseInt(document.querySelector("#choices .choice.selected")?.dataset.i??-1);
    jumpQ(parseInt(b.dataset.jump));});
  $("#saveBtn").onclick=()=>{
    const saved=STATE.progress.saved_questions||(STATE.progress.saved_questions=[]);
    const exists=saved.findIndex(x=>x.q===q.q);
    if(exists>=0){saved.splice(exists,1);$("#saveBtn").textContent="💾 ذخیره";}
    else{saved.push({...q,subject:q.subject||"exam",year:E.year});$("#saveBtn").textContent="💾 ذخیره شد";}
    saveProgress();
  };
}
function jumpQ(j){STATE.exam.idx=j;render();}
function saveAndNext(){
  const E=STATE.exam;
  const chosen=document.querySelector("#choices .choice.selected");
  E.answers[E.idx]=chosen?parseInt(chosen.dataset.i):-1;
  E.idx++;render();
}
function submitExam(timeup){
  const E=STATE.exam;if(!E||E.submitted)return;E.submitted=true;
  if(!timeup){
    const u=E.answers.filter(a=>a===-1).length;
    if(u>0 && !confirm(`${u} سوال بدون پاسخ مانده. مطمئنی پایان را می‌خواهی؟`)){E.submitted=false;return;}
  }
  let correct=0;
  const details=E.questions.map((q,i)=>{const ch=E.answers[i];const ok=ch===q.answer;if(ok)correct++;return{q,ch,ok};});
  E.correct=correct;
  STATE.progress.exam_results.push({year:E.year,score:correct,total:E.questions.length,date:new Date().toLocaleString("fa-IR")});
  saveProgress();E.details=details;
  if(STATE.timerHandle)clearInterval(STATE.timerHandle);
  setView("exam-result");
}
function renderExamResult(main){
  const E=STATE.exam;const pct=Math.round(E.correct*100/E.questions.length);
  const msg=pct>=80?"ممتاز! 🏆":pct>=60?"خوب! 💪":pct>=40?"نیاز به مطالعه 📚":"بیشتر تلاش کن 🎯";
  main.innerHTML=`<div class="page-head"><h1>🎓 کارنامه دوره ${E.year}</h1>
    <p>${E.correct} درست از ${E.questions.length} — <b style="color:var(--warning)">${pct}%</b></p></div>
    <div class="result"><div class="score">${pct}%</div><div style="font-size:18px;margin-top:8px">${msg}</div>
      <div style="margin-top:16px;display:flex;gap:8px;justify-content:center;flex-wrap:wrap">
        <button class="btn btn-secondary" onclick="restartExam()">🔁 آزمون مجدد</button>
        <button class="btn btn-ghost" onclick="setView('exams')">لیست آزمون‌ها</button>
        <button class="btn btn-primary" onclick="setView('dashboard')">🏠 داشبورد</button></div></div><div id="rev"></div>`;
  const rev=$("#rev");
  E.details.forEach((d,i)=>{
    const sid=d.q.subject||"math";
    const el=document.createElement("div");el.className="q-result "+(d.ok?"ok":"bad");
    el.innerHTML=`<div><span class="mark" style="color:${d.ok?'var(--success)':'var(--danger)'}">${d.ok?'✅':'❌'} سوال ${i+1}</span>
      <span class="sub-dot" style="background:${subColor(sid)}"></span>
      <span style="font-size:11px;color:var(--muted)">${subName(sid)}</span></div>
      <p>${d.q.q}</p>
      <div class="ans-line">پاسخ شما: <b style="color:${d.ok?'var(--success)':'var(--danger)'}">${d.ch>=0?letterOf(d.ch):"بدون پاسخ"}</b> — پاسخ صحیح: <b style="color:var(--success)">${letterOf(d.q.answer)}</b></div>
      <div style="margin-top:8px;padding:10px;background:rgba(245,158,11,.1);border-radius:8px;font-size:13px"><b style="color:var(--warning)">🎯:</b> ${d.q.konkori||"—"}</div>
      <div style="margin-top:6px;padding:10px;background:rgba(56,189,248,.08);border-radius:8px;font-size:13px"><b style="color:var(--accent)">📚:</b> ${d.q.full_solution||"—"}</div>`;
    rev.appendChild(el);
  });
}
function restartExam(){const idx=APP_DATA.exams.findIndex(e=>e.year===STATE.exam.year);STATE.exam=null;startExam(idx);}

/* ---- Books / Free Books ---- */
function renderBooks(main){
  /* ---- بخش ۱: کتاب‌های درسی کامل داخل اپ ---- */
  const subs=APP_DATA.subjects.filter(s=>hasBook(s.id));
  let totCh=0, totMin=0, doneCh=0;
  subs.forEach(s=>{ totCh+=bookChapterCount(s.id); totMin+=bookMinutes(s.id);
    BOOK_DATA[s.id].parts.forEach(p=>p.chapters.forEach(c=>{ if(STATE.progress.completed_lessons.includes(chapterKey(s.id,c.id))) doneCh++; }));
  });
  const pct = totCh? Math.round(doneCh*100/totCh) : 0;

  main.innerHTML=`
    <div class="page-head"><h1>📕 کتابخانه درسی</h1>
      <p>۱۰ کتاب کامل — نه خلاصه. ${totCh} فصل و حدود ${Math.round(totMin/60)} ساعت مطالعه.</p></div>
    <div class="card" style="background:linear-gradient(135deg,var(--accent)22,transparent);border-color:var(--accent)44">
      <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap">
        <div style="font-weight:800;font-size:16px">پیشرفت کل کتاب‌ها: ${doneCh} از ${totCh} فصل (${pct}%)</div>
        <button class="btn btn-primary" onclick="setView('freebooks')">🔗 منابع آزاد و رایگان</button>
      </div>
      <div class="bar" style="margin-top:12px"><div class="bar-fill" style="width:${pct}%"></div></div>
    </div>
    <div class="section-title">📚 کتاب‌های کامل هر درس</div>
    <div class="grid-cards" id="fullbooks"></div>
    <div class="section-title">📖 منابع مرجع کنکور ارشد (۲۰ کتاب)</div>
    <div id="books"></div>`;

  const fb=$("#fullbooks");
  subs.forEach(s=>{
    const bk=BOOK_DATA[s.id];
    const chAll=bookFlatChapters(bk);
    const done=chAll.filter(c=>STATE.progress.completed_lessons.includes(chapterKey(s.id,c.id))).length;
    const pc=chAll.length?Math.round(done*100/chAll.length):0;
    const el=document.createElement("div"); el.className="card clickable";
    el.onclick=()=>openBookHome(s.id);
    el.innerHTML=`<div class="emoji">${s.emoji}</div>
      <h3>${bk.title}</h3>
      <p>${bk.subtitle||""}</p>
      <div style="color:var(--muted);font-size:12.5px;margin:8px 0">📚 ${bk.parts.length} بخش • ${chAll.length} فصل • ⏱ ${bookMinutes(s.id)} دقیقه مطالعه</div>
      <div class="bar"><div class="bar-fill" style="width:${pc}%"></div></div>
      <div style="font-size:12px;color:var(--muted);margin-top:6px">${done} از ${chAll.length} فصل خوانده‌شده (${pc}%)</div>
      <div class="card-actions"><button class="btn btn-primary">📖 باز کردن کتاب</button></div>`;
    fb.appendChild(el);
  });

  const box=$("#books");
  (APP_DATA.books||[]).forEach(b=>{
    const el=document.createElement("div");el.className="book";
    el.innerHTML=`<span class="topic">${b.topic}</span><h3>📘 ${b.title}</h3><div class="author">نویسنده: ${b.author}</div><div class="desc">${b.desc}</div>`;
    box.appendChild(el);
  });
}
function renderFreeBooks(main){
  main.innerHTML=`<div class="page-head"><h1>🔗 کتاب‌های رایگان و منابع آزاد</h1>
    <p>این منابع همگی به صورت قانونی توسط نویسندگان/دانشگاه‌ها به صورت آزاد یا پیش‌نمایش در دسترس قرار گرفته‌اند. برای استفاده شخصی خودت ازشون استفاده کن.</p></div>
    <div id="fb"></div>`;
  const box=$("#fb");
  (APP_DATA.free_books||[]).forEach(b=>{
    const el=document.createElement("div");el.className="book";
    el.innerHTML=`<span class="topic">${b.topic}</span><h3>📚 <a href="${b.url}" target="_blank" style="color:var(--accent);text-decoration:none">${b.title}</a></h3><div class="desc">${b.note}</div>`;
    box.appendChild(el);
  });
}

/* ---- Saved questions + Bookmarks ---- */
function renderBookmarks(main){
  const bms=STATE.progress.bookmarks;
  main.innerHTML=`<div class="page-head"><h1>⭐ نشان‌شده‌ها</h1><p>فصول و مطالب مهم</p></div><div id="bms"></div>`;
  const box=$("#bms");
  if(!bms.length){box.innerHTML=`<div class="card" style="text-align:center;padding:40px;color:var(--muted)">هنوز چیزی نشان نشده.</div>`;return;}
  bms.forEach((b,i)=>{
    const el=document.createElement("div");el.className="book";
    el.innerHTML=`<span class="topic" style="background:var(--warning)">⭐</span><h3>${b.title||"(بی‌نام)"}</h3>
      <div class="desc" style="white-space:pre-wrap">${b.content||""}</div>
      <div style="margin-top:10px"><button class="btn btn-sm btn-danger" onclick="removeBm(${i})">حذف</button></div>`;
    box.appendChild(el);
  });
}
function removeBm(i){STATE.progress.bookmarks.splice(i,1);saveProgress();render();}

function renderSavedQuestions(main){
  const sq = STATE.progress.saved_questions||[];
  main.innerHTML=`<div class="page-head"><h1>💾 سوالات ذخیره‌شده</h1><p>این‌ها سوالاتی هستند که هنگام تست یا آزمون برای مرور ذخیره کردی.</p></div><div id="sq"></div>`;
  const box=$("#sq");
  if(!sq.length){box.innerHTML=`<div class="card" style="text-align:center;padding:40px;color:var(--muted)">هنوز سوالی ذخیره نکردی. هنگام تست روی 💾 ذخیره بزن.</div>`;return;}
  sq.forEach((q,i)=>{
    const sid=q.subject||"math";
    const el=document.createElement("div");el.className="book";
    el.innerHTML=`<span class="topic" style="background:${subColor(sid)}">${subEmoji(sid)} ${subName(sid)}${q.year?` • ${q.year}`:""}</span>
      <h3>سوال ${i+1}: ${q.q}</h3>
      <div style="margin:8px 0">
        ${q.choices.map((c,ci)=>`<div style="padding:6px 10px;margin:4px 0;border-radius:8px;${ci===q.answer?'background:rgba(34,197,94,.15);border-right:3px solid var(--success)':'background:var(--bg2)'}"><b>${letterOf(ci)})</b> ${c}${ci===q.answer?' ✅':''}</div>`).join("")}
      </div>
      <div style="padding:10px;background:rgba(245,158,11,.1);border-radius:8px;font-size:13px"><b style="color:var(--warning)">🎯 راه حل کنکوری:</b><br>${q.konkori||"—"}</div>
      <div style="margin-top:6px;padding:10px;background:rgba(56,189,248,.08);border-radius:8px;font-size:13px"><b style="color:var(--accent)">📚 توضیح کامل:</b><br>${q.full_solution||"—"}</div>
      <div style="margin-top:10px"><button class="btn btn-sm btn-danger" onclick="removeSaved(${i})">حذف از ذخیره</button></div>`;
    box.appendChild(el);
  });
}
function removeSaved(i){STATE.progress.saved_questions.splice(i,1);saveProgress();render();}

/* ---- Teacher Mode ---- */
function renderTeacherHome(main){
  main.innerHTML=`<div class="page-head"><h1>🧑‍🏫 کلاس درس با استاد</h1>
    <p>تدریس تعاملی هر درس از صفر تا صد، با زبان ساده و نکات کنکوری. یک درس را انتخاب کن:</p></div>
    <div class="grid-cards" id="tg"></div>`;
  const g=$("#tg");
  APP_DATA.subjects.forEach(s=>{
    const tc=APP_DATA.teacher[s.id];
    const el=document.createElement("div");el.className="card clickable";
    el.innerHTML=`<div class="emoji">🧑‍🏫</div><h3>${s.emoji} ${s.name}</h3><p>${(tc.slides||[]).length} بخش تدریس تعاملی</p>
      <div class="card-actions"><button class="btn" style="background:var(--warning);color:#0f172a">شروع کلاس</button></div>`;
    el.onclick=()=>openTeacher(s.id);
    g.appendChild(el);
  });
}
function openTeacher(sid){
  STATE.teacher={subject:sid, slide:0};
  setView("teacher-lesson");
}
function renderTeacherLesson(main){
  const T=APP_DATA.teacher[STATE.teacher.subject];
  const s=APP_DATA.subjects.find(x=>x.id===STATE.teacher.subject);
  const si=STATE.teacher.slide;
  const slides=T.slides||[];
  const isIntro=(si===0);
  const total=slides.length+1; // intro + slides
  const currentSlide = isIntro? null:slides[si-1];
  const pct = (si/(total-1))*100;
  main.innerHTML=`
    <div class="quiz-wrap">
      <div class="quiz-meta">
        <div style="color:${s.color}">🧑‍🏫 ${s.emoji} ${s.name}</div>
        <div>بخش ${si+1} از ${total}</div>
      </div>
      <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,var(--warning),var(--accent))"></div></div>
      <div class="q-card" style="padding:30px">
        <div style="font-size:22px;font-weight:800;margin-bottom:16px;color:var(--warning)">${isIntro?"👋 سلام":"📘 "+currentSlide.title}</div>
        <div style="font-size:15px;line-height:2.4;white-space:pre-wrap;text-align:justify;color:var(--text)">${isIntro?T.intro:currentSlide.body}</div>
        <div class="q-actions" style="margin-top:24px">
          <button class="btn btn-ghost" onclick="setView('teacher')">🔙 لیست دروس</button>
          <div style="display:flex;gap:8px">
            ${si>0?`<button class="btn btn-ghost" onclick="teacherSlide(-1)">⬅️ قبلی</button>`:""}
            ${si<total-1?`<button class="btn btn-primary" onclick="teacherSlide(1)">بعدی ➡️</button>`:`<button class="btn btn-success" onclick="finishTeacher()">✅ پایان درس + شروع تست</button>`}
          </div>
        </div>
      </div>
    </div>`;
}
function teacherSlide(delta){STATE.teacher.slide+=delta;render();}
function finishTeacher(){
  const sid=STATE.teacher.subject;
  STATE.teacher=null;
  startQuiz(sid);
}

/* ---- Settings ---- */
function renderSettings(main){
  const canInstall = !!deferredPrompt;
  main.innerHTML=`<div class="page-head"><h1>⚙️ تنظیمات</h1></div>
    <div class="card" style="max-width:520px">
      ${canInstall?`<div class="install-banner">📱 این اپ را روی موبایل/دسکتاپ نصب کن
        <button onclick="installApp()">نصب اپلیکیشن</button></div>`:
        `<div style="padding:12px 14px;background:rgba(56,189,248,.12);border-right:4px solid var(--accent);border-radius:8px;font-size:13px;line-height:2.2;margin-bottom:12px">
        <b>📱 راه نصب روی موبایل:</b><br>
        • اندروید (کروم): منوی سه‌نقطه ← «افزودن به صفحه اصلی» ← نصب<br>
        • آیفون (سافاری): دکمه اشتراک ← «افزودن به صفحه اصلی»<br>
        • بعد از نصب مانند اپ عادی از صفحه اصلی اجرا می‌شود و آفلاین هم کار می‌کند.
        </div>`}
      <h3 style="margin-bottom:10px">حالت نمایش</h3>
      <div class="segments">
        <button data-th="dark" class="${STATE.progress.theme==='dark'?'on':''}">Dark</button>
        <button data-th="light" class="${STATE.progress.theme==='light'?'on':''}">Light</button>
      </div>
      <h3 style="margin:16px 0 8px">درباره</h3>
      <p style="font-size:13px;line-height:2;color:var(--muted)">
      اپلیکیشن شخصی آمادگی کنکور ارشد مهندسی پزشکی — نسخه ۱.۲.۰ (موبایل/آفلاین/PWA)<br>
      شامل: ۱۰ کتاب درسی کامل (۴۰ فصل)، دوره پایه تا پیشرفته، بانک سوال، تست ترکیبی شافل، سوالات تمرینی تالیفی، آزمون‌های ۱۰ ساله، استاد تدریس خصوصی، و حالت آفلاین.
      </p>
      <div style="margin-top:14px;display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn btn-ghost" onclick="exportData()">📤 گرفتن پشتیبان</button>
        <button class="btn btn-ghost" onclick="importData()">📥 بازگردانی پشتیبان</button>
        <button class="btn btn-danger" onclick="resetAll()">🔄 ریست کامل</button>
      </div>
    </div>`;
  $$(".segments button").forEach(b=>b.onclick=()=>{
    STATE.progress.theme=b.dataset.th;applyTheme(STATE.progress.theme);saveProgress();render();
  });
  applyTheme(STATE.progress.theme);
}
function installApp(){
  if(!deferredPrompt) return;
  deferredPrompt.prompt();
  deferredPrompt.userChoice.then(()=>{deferredPrompt=null;render();});
}
function applyTheme(t){
  if(t==="light"){
    document.documentElement.style.setProperty("--bg","#f1f5f9");
    document.documentElement.style.setProperty("--bg2","#e2e8f0");
    document.documentElement.style.setProperty("--card","#ffffff");
    document.documentElement.style.setProperty("--card2","#f8fafc");
    document.documentElement.style.setProperty("--hover","#e2e8f0");
    document.documentElement.style.setProperty("--border","#cbd5e1");
    document.documentElement.style.setProperty("--text","#0f172a");
    document.documentElement.style.setProperty("--muted","#475569");
  } else {
    document.documentElement.style.setProperty("--bg","#0b1120");
    document.documentElement.style.setProperty("--bg2","#0f172a");
    document.documentElement.style.setProperty("--card","#1e293b");
    document.documentElement.style.setProperty("--card2","#273449");
    document.documentElement.style.setProperty("--hover","#334155");
    document.documentElement.style.setProperty("--border","#334155");
    document.documentElement.style.setProperty("--text","#e2e8f0");
    document.documentElement.style.setProperty("--muted","#94a3b8");
  }
}
function resetAll(){if(!confirm("مطمئنی تمام پیشرفت پاک شود؟"))return;lsDel(LS_KEY);STATE.progress=loadProgress();setView("dashboard");}
function exportData(){
  const json=JSON.stringify(STATE.progress,null,2);
  // پل بومی: اپ اندروید (Android.saveBackup) یا اپ دسکتاپ (pywebview api)
  try{
    if(window.Android && typeof window.Android.saveBackup==="function"){
      window.Android.saveBackup("bme_progress_backup.json", json);
      toast("✅ پشتیبان ذخیره شد");
      return;
    }
    if(window.pywebview && window.pywebview.api && window.pywebview.api.save_backup){
      window.pywebview.api.save_backup(json).then(r=>toast("✅ "+r)).catch(()=>{});
      return;
    }
  }catch(e){}
  const blob=new Blob([json],{type:"application/json"});
  const url=URL.createObjectURL(blob);const a=document.createElement("a");
  a.href=url;a.download="bme_progress_backup.json";a.click();URL.revokeObjectURL(url);
}
function toast(msg){
  let t=document.getElementById("toast");
  if(!t){t=document.createElement("div");t.id="toast";document.body.appendChild(t);}
  t.textContent=msg;t.classList.add("show");
  clearTimeout(window._toastT);
  window._toastT=setTimeout(()=>t.classList.remove("show"),2400);
}
function applyBackup(text){
  try{
    const d=JSON.parse(text);
    STATE.progress=Object.assign(loadProgress(),d);
    saveProgress();updateSidebarStat();render();
    toast("✅ پشتیبان بازگردانی شد");
  }catch(err){toast("❌ فایل معتبر نیست");}
}
function importData(){
  // پل بومی برای بازگردانی پشتیبان
  try{
    if(window.pywebview && window.pywebview.api && window.pywebview.api.load_backup){
      window.pywebview.api.load_backup().then(t=>{
        if(t && t.length) applyBackup(t);
      });
      return;
    }
    if(window.Android && typeof window.Android.pickBackup==="function"){
      window.Android.pickBackup();
      return;
    }
  }catch(e){}
  const inp=document.createElement("input");
  inp.type="file";inp.accept=".json,application/json";
  inp.onchange=e=>{
    const f=e.target.files[0];if(!f)return;
    const r=new FileReader();
    r.onload=()=>applyBackup(r.result);
    r.readAsText(f);
  };
  inp.click();
}

/* ============ FOUNDATION (base to advanced) ============ */
function renderFoundationHome(main){
  main.innerHTML=`<div class="page-head">
    <h1>🎒 دوره آموزش از پایه</h1>
    <p>اگه از پایه ضعیفی نگران نباش! اینجا از صفرِ صفر، مثل بچه‌ای که اولین بار می‌خواد یاد بگیره، بهت درس می‌دم. <br>برای هر درس سه سطح داریم: پایه (مفاهیم اولیه با زبان ساده)، متوسط، و پیشرفته (رسیدن به سطح کنکور).</p>
    </div><div class="grid-cards" id="fg"></div>`;
  const g=$("#fg");
  APP_DATA.subjects.forEach(s=>{
    const fc = APP_DATA.foundation[s.id];
    const totalLessons = fc.levels.reduce((a,l)=>a+l.lessons.length,0);
    const el=document.createElement("div");el.className="card clickable";
    el.innerHTML=`<div class="emoji">🎒</div><h3>${s.emoji} ${fc.title}</h3><p>${fc.levels.length} سطح • ${totalLessons} درس تعاملی</p>
      <div style="margin-top:6px;display:flex;gap:6px;flex-wrap:wrap">
        ${fc.levels.map(l=>`<span style="background:var(--card2);color:var(--muted);font-size:11px;padding:3px 8px;border-radius:14px">${l.name.split("—")[0].trim()}</span>`).join("")}
      </div>
      <div class="card-actions"><button class="btn btn-primary">شروع دوره</button></div>`;
    el.onclick=()=>openFoundation(s.id,0,0);
    g.appendChild(el);
  });
}
function openFoundation(sid,li,sl){
  STATE.foundation={subject:sid, levelIdx:li, slideIdx:sl};
  setView("foundation-lesson");
}
function renderFoundationLesson(main){
  const F=APP_DATA.foundation[STATE.foundation.subject];
  const s=APP_DATA.subjects.find(x=>x.id===STATE.foundation.subject);
  const li=STATE.foundation.levelIdx, sl=STATE.foundation.slideIdx;
  const level=F.levels[li];
  const lesson=level.lessons[sl];
  // total count
  let totalSlides=0, curIdx=0;
  for(let i=0;i<=li;i++){
    for(let j=0;j<F.levels[i].lessons.length;j++){
      if(i<li||(i===li&&j<sl)) curIdx++;
      totalSlides++;
    }
  }
  curIdx++;
  const pct=(curIdx/totalSlides)*100;
  const isLast=(li===F.levels.length-1 && sl===level.lessons.length-1);
  const canPrev=(li>0||sl>0);
  main.innerHTML=`
    <div class="quiz-wrap">
      <div class="quiz-meta">
        <div style="color:${s.color}">🎒 ${s.emoji} ${F.title}</div>
        <div>${level.name} • درس ${sl+1}/${level.lessons.length} (${curIdx}/${totalSlides} کل)</div>
      </div>
      <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,#fbbf24,#22c55e)"></div></div>
      <div class="q-card" style="padding:30px">
        <div style="font-size:22px;font-weight:800;margin-bottom:8px;color:var(--warning)">📘 ${lesson.title}</div>
        <div style="margin-bottom:14px;font-size:12px;color:var(--muted);background:var(--bg2);display:inline-block;padding:4px 10px;border-radius:20px">${level.name}</div>
        <div style="font-size:15px;line-height:2.8;white-space:pre-wrap;text-align:justify;color:var(--text);font-size:14.5px">${lesson.body.replace(/\n/g,"<br>")}</div>
        <div class="q-actions" style="margin-top:24px">
          <button class="btn btn-ghost" onclick="setView('foundation')">🔙 لیست دروس</button>
          <div style="display:flex;gap:8px">
            ${canPrev?`<button class="btn btn-ghost" onclick="fndSlide(-1)">⬅️ قبلی</button>`:""}
            ${!isLast?`<button class="btn btn-success" onclick="fndSlide(1)">ادامه ➡️</button>`:`
              <button class="btn" style="background:var(--warning);color:#0f172a" onclick="startQuiz('${s.id}')">✅ دوره تمام شد — شروع تست</button>`}
          </div>
        </div>
      </div>
    </div>`;
}
function fndSlide(delta){
  const F=APP_DATA.foundation[STATE.foundation.subject];
  let li=STATE.foundation.levelIdx, sl=STATE.foundation.slideIdx;
  sl+=delta;
  while(sl>=F.levels[li].lessons.length){sl=0;li++;}
  while(sl<0){if(li>0){li--;sl=F.levels[li].lessons.length-1;}else{sl=0;break;}}
  if(li>=F.levels.length){li=F.levels.length-1;sl=F.levels[li].lessons.length-1;}
  openFoundation(STATE.foundation.subject,li,sl);
}

/* ============ PRACTICE (non-exam talifi questions) ============ */
function renderPracticeHome(main){
  main.innerHTML=`<div class="page-head">
    <h1>✏️ سوالات تمرینی تالیفی</h1>
    <p>این سوالات از کتاب‌های تمرین، کتاب کار و منابع آموزشی هستند (سوالات خود کنکور نیستند). هدف اینه که مبحث به مبحث تسلط پیدا کنی، قبل از رفتن سراغ سوالات کنکور.<br>هر سوال یک بخش آموزشی کوتاه داره که قبل از جواب بهت درس میده، بعد هم جواب تشریحی کامل.</p>
    </div>
    <div class="grid-cards" id="pg">
      <div class="card clickable" onclick="startPractice(null)">
        <div class="emoji">🎯</div><h3>ترکیبی همه دروس</h3><p>۱۵ سوال تصادفی از همه مباحث و همه سطوح</p>
        <div class="card-actions"><button class="btn btn-primary">شروع تمرین ترکیبی</button></div>
      </div>
    </div>`;
  const g=$("#pg");
  APP_DATA.subjects.forEach(s=>{
    const qc=(APP_DATA.practice[s.id]||[]).length;
    if(!qc) return;
    const levels=[...new Set(APP_DATA.practice[s.id].map(q=>q.difficulty))];
    const el=document.createElement("div");el.className="card clickable";
    el.innerHTML=`<div class="emoji">${s.emoji}</div><h3>${s.name}</h3>
      <p>${qc} سوال تمرینی — سطح: ${levels.join("، ")}</p>
      <div class="card-actions"><button class="btn btn-secondary">شروع</button></div>`;
    el.querySelector("h3").style.color=s.color;
    el.onclick=()=>startPractice(s.id);
    g.appendChild(el);
  });
}
function startPractice(sid){
  let pool=[];
  if(sid===null){
    Object.keys(APP_DATA.practice).forEach(k=>APP_DATA.practice[k].forEach(q=>pool.push({...q,subject:k})));
    pool=shuffle(pool).slice(0,15);
    STATE.practice={questions:pool,idx:0,correct:0,subject:"ترکیبی"};
  } else {
    pool=APP_DATA.practice[sid].map(q=>({...q,subject:sid}));
    STATE.practice={questions:shuffle(pool),idx:0,correct:0,subject:sid?APP_DATA.subjects.find(s=>s.id===sid).name:""};
  }
  setView("practice-playing");
}
function renderPracticeQuiz(main){
  const P=STATE.practice;if(!P){setView("practice");return;}
  if(P.idx>=P.questions.length){renderPracticeResult(main);return;}
  const q=P.questions[P.idx];
  const pct=(P.idx/P.questions.length)*100;
  main.innerHTML=`<div class="quiz-wrap">
    <div class="quiz-meta">
      <div>سوال <b>${P.idx+1}</b> از ${P.questions.length} — ${q.difficulty?`<span style="background:var(--warning);color:#0f172a;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:700">${q.difficulty}</span>`:""}
        <span style="color:${subColor(q.subject)}">${subEmoji(q.subject)} ${subName(q.subject)}</span></div>
      <div>درست: <b style="color:var(--success)">${P.correct}</b></div>
    </div>
    <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,var(--success),var(--accent))"></div></div>
    <div class="q-card">
      <div class="q-text">${q.q}</div>
      <div id="choices">
        ${q.choices.map((c,i)=>`<div class="choice" data-i="${i}"><div class="letter">${letterOf(i)}</div><div>${c}</div></div>`).join("")}
      </div>
      <div class="explain" id="teach" style="display:none;margin-top:8px;background:rgba(251,191,36,.12);border-right:4px solid var(--warning);padding:12px;border-radius:8px;font-size:13px;line-height:2"></div>
      <div class="explain" id="full" style="display:none;margin-top:8px;background:rgba(56,189,248,.1);border-right:4px solid var(--accent);padding:12px;border-radius:8px;font-size:13px;line-height:2"></div>
      <div class="q-actions">
        <button class="btn btn-ghost" onclick="setView('practice')">🔙 انصراف</button>
        <div style="display:flex;gap:8px">
          <button class="btn btn-success" id="checkBtn" onclick="checkPracticeAnswer()">✅ ثبت پاسخ</button>
          <button class="btn btn-primary" id="nextBtn" style="display:none" onclick="nextPractice()">بعدی ➡️</button>
        </div>
      </div>
    </div></div>`;
  $$("#choices .choice").forEach(c=>c.onclick=()=>{
    if($("#checkBtn").disabled) return;
    $$("#choices .choice").forEach(x=>x.classList.remove("selected"));
    c.classList.add("selected");
  });
}
function checkPracticeAnswer(){
  const P=STATE.practice;const q=P.questions[P.idx];
  const chosenEl=document.querySelector("#choices .choice.selected");
  if(!chosenEl){alert("لطفاً یک گزینه انتخاب کن");return;}
  const chosen=parseInt(chosenEl.dataset.i);
  STATE.progress.quiz_stats.total++;
  $$("#choices .choice").forEach(c=>{
    const idx=parseInt(c.dataset.i);
    if(idx===q.answer) c.classList.add("correct");
    if(idx===chosen && chosen!==q.answer) c.classList.add("wrong");
    c.style.pointerEvents="none";
  });
  const teach=$("#teach"), full=$("#full");
  teach.innerHTML=q.teaching||""; teach.style.display="block";
  let resultHead;
  if(chosen===q.answer){
    P.correct++;STATE.progress.quiz_stats.correct++;
    resultHead=`<div style="color:var(--success);font-weight:700;margin-bottom:6px">✅ آفرین درست بود!</div>`;
  } else {
    resultHead=`<div style="color:var(--danger);font-weight:700;margin-bottom:6px">❌ اشتباه! گزینه صحیح <b>${letterOf(q.answer)}</b> بود. نگاه کن چرا:</div>`;
  }
  full.innerHTML=resultHead + (q.full_solution||"");
  full.style.display="block";
  $("#checkBtn").disabled=true;$("#checkBtn").style.opacity=.4;
  $("#nextBtn").style.display="inline-block";
  saveProgress();
}
function nextPractice(){STATE.practice.idx++;render();}
function renderPracticeResult(main){
  const P=STATE.practice;const pct=Math.round(P.correct*100/P.questions.length);
  const msg=pct>=80?"عالی تسلط داری! 💪":pct>=60?"خوب، کمی بیشتر تمرین کن":pct>=40?"بهتره برگردی دوره پایه رو دوباره ببینی 🎒":"نگران نباش، برو سراغ دوره پایه از صفر شروع کن 🎒";
  main.innerHTML=`<div class="quiz-wrap"><div class="result">
    <h2>🎉 پایان تمرین</h2><div class="score">${pct}%</div>
    <div>${P.correct} درست از ${P.questions.length}</div><div class="msg">${msg}</div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:center;flex-wrap:wrap">
      <button class="btn btn-primary" onclick="${P.subject.includes('ترکیبی')?'startPractice(null)':`startPractice('${P.questions[0].subject}')`}">🔁 تمرین مجدد</button>
      <button class="btn" style="background:var(--warning);color:#0f172a" onclick="setView('foundation')">🎒 مرور دوره پایه</button>
      <button class="btn btn-ghost" onclick="setView('dashboard')">🏠 داشبورد</button>
    </div></div></div>`;
  STATE.practice=null;
}

/* Nav bindings */
$$(".nav-btn").forEach(b=>b.addEventListener("click",()=>{
  const v=b.dataset.view;
  if(v==="quiz-playing"||v==="exam-playing"||v==="teacher-lesson"||v==="practice-playing"||v==="foundation-lesson")return;
  if(STATE.timerHandle){clearInterval(STATE.timerHandle);}
  setView(v);
}));

/* ═══ کنکورهای ۱۰ سال اخیر ═══ */

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
    <div class="section-title">انتخاب سال</div>
    <div class="grid-cards" id="kg"></div>`;

  const g=$("#kg");
  years.forEach(y=>{
    const n=pkYearCount(y);
    const solved=pkSubjects().filter(s=>pkRes(y,s)).length;
    const el=document.createElement("div"); el.className="card clickable";
    el.innerHTML=`<div style="font-size:34px;font-weight:800;color:var(--accent2);line-height:1.25">${pkFa(y)}</div>
      <h3>کنکور سراسری ارشد</h3>
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
function __unused_pkRecord(isCorrect){
  const Q=STATE.quiz;
  if(!Q || !Q.konkur || !Q.konkur.year || !Q.konkur.sid) return;
  const key=Q.konkur.year+"__"+Q.konkur.sid;
  const all=qDone();
  if(!all[key]) all[key]={score:0,total:pkQ(Q.konkur.year,Q.konkur.sid).length,date:new Date().toLocaleDateString("fa-IR")};
  if(isCorrect) all[key].score++;
  all[key].total=pkQ(Q.konkur.year,Q.konkur.sid).length;
  all[key].date=new Date().toLocaleDateString("fa-IR");
}

/* init */
applyTheme(STATE.progress.theme||"dark");
updateSidebarStat();
// allow shortcuts via ?view=xxx
const urlParams = new URLSearchParams(window.location.search);
const initView = urlParams.get('view');
if(initView && ["dashboard","subjects","quiz","exams","books","freebooks","bookmarks","savedq","teacher","foundation","practice","settings"].includes(initView)){
  setView(initView);
} else {
  setView("dashboard");
}
// PWA install prompt
let deferredPrompt;
window.addEventListener('beforeinstallprompt', e=>{
  e.preventDefault();
  deferredPrompt = e;
  // show floating install button if we want (settings already has it)
  const installBtn = document.getElementById('installBtn');
  if(installBtn) installBtn.style.display='inline-block';
});
if(window.matchMedia('(display-mode: standalone)').matches){
  // running installed
  document.documentElement.classList.add('pwa-installed');
}
