/* =====================================================
   کتاب درسی کامل — موتور نمایش
   ساختار: BOOK_DATA[subjectId] = { title, subtitle, parts:[{title, chapters:[{id,title,minutes,blocks:[...]}]}] }
   انواع بلوک: h | h3 | p | f | ul | ol | tbl | note | warn | tip | ex | exr | fig | quote | sum
===================================================== */

/* ---------- رندر یک بلوک ---------- */
function renderBlock(b, i){
  const t = b.t;
  if(t === "h")   return `<h2 class="bk-h" id="bk-${i}">${b.x}</h2>`;
  if(t === "h3")  return `<h3 class="bk-h3">${b.x}</h3>`;
  if(t === "p")   return `<p class="bk-p">${b.x}</p>`;
  if(t === "quote") return `<blockquote class="bk-quote">${b.x}</blockquote>`;

  if(t === "f"){
    // جعبه فرمول: x = فرمول، label = برچسب، d = توضیح
    return `<div class="bk-formula">
      ${b.label?`<div class="bk-formula-label">${b.label}</div>`:""}
      <div class="bk-formula-body">${b.x}</div>
      ${b.d?`<div class="bk-formula-desc">${b.d}</div>`:""}
    </div>`;
  }

  if(t === "ul" || t === "ol"){
    const tag = t === "ul" ? "ul" : "ol";
    return `<${tag} class="bk-list">${(b.items||[]).map(x=>`<li>${x}</li>`).join("")}</${tag}>`;
  }

  if(t === "tbl"){
    return `<div class="bk-table-wrap"><table class="bk-table">
      <thead><tr>${(b.head||[]).map(h=>`<th>${h}</th>`).join("")}</tr></thead>
      <tbody>${(b.rows||[]).map(r=>`<tr>${r.map(c=>`<td>${c}</td>`).join("")}</tr>`).join("")}</tbody>
    </table></div>`;
  }

  if(t === "note") return `<div class="bk-box bk-note"><div class="bk-box-title">📌 نکته</div><div>${b.x}</div></div>`;
  if(t === "warn") return `<div class="bk-box bk-warn"><div class="bk-box-title">⚠️ اشتباه رایج</div><div>${b.x}</div></div>`;
  if(t === "tip")  return `<div class="bk-box bk-tip"><div class="bk-box-title">💡 ترفند کنکور</div><div>${b.x}</div></div>`;
  if(t === "fig"){
    const svg = (typeof figureSVG === "function") ? figureSVG(b.fig) :
                ((typeof FIGURES !== "undefined" && b.fig && FIGURES[b.fig]) ? FIGURES[b.fig]() : "");
    if(!svg) return "";
    return `<figure class="bk-fig">${svg}<figcaption class="bk-fig-cap">🖼 ${b.cap||""}</figcaption></figure>`;
  }

  if(t === "ex"){
    // مثال حل‌شده کامل
    return `<div class="bk-ex">
      <div class="bk-ex-head">✏️ ${b.title || "مثال حل‌شده"}</div>
      <div class="bk-ex-q">${b.q}</div>
      ${(b.steps||[]).map((s,k)=>`<div class="bk-ex-step"><span class="bk-step-n">${k+1}</span><div>${s}</div></div>`).join("")}
      ${b.a?`<div class="bk-ex-ans">✅ <b>پاسخ:</b> ${b.a}</div>`:""}
    </div>`;
  }

  if(t === "exr"){
    // تمرین برای حل خود دانشجو (پاسخ پنهان با دکمه)
    const uid = "exr" + Math.random().toString(36).slice(2,9);
    return `<div class="bk-exr">
      <div class="bk-exr-head">🎯 تمرین ${b.n || ""}</div>
      <div class="bk-exr-q">${b.q}</div>
      <button class="bk-exr-btn" onclick="document.getElementById('${uid}').classList.toggle('show')">نمایش پاسخ ▾</button>
      <div class="bk-exr-a" id="${uid}"><b>پاسخ:</b> ${b.a}</div>
    </div>`;
  }

  if(t === "sum"){
    return `<div class="bk-sum"><div class="bk-sum-title">📋 خلاصه این فصل</div>
      <ul>${(b.items||[]).map(x=>`<li>${x}</li>`).join("")}</ul></div>`;
  }

  return "";
}

/* ---------- شماره‌گذاری فصل‌ها ---------- */
function bookFlatChapters(bk){
  const out = [];
  (bk.parts||[]).forEach((p, pi)=>{
    (p.chapters||[]).forEach((c, ci)=>{
      out.push({...c, partTitle: p.title, partIdx: pi, chIdx: ci, index: out.length});
    });
  });
  return out;
}

function chapterKey(sid, chId){ return `book:${sid}:${chId}`; }

/* ---------- صفحه کتاب‌ها (چند کتاب در هر درس) ---------- */
function renderBookHome(sid, bookId){
  const main = $("#main");
  const s = APP_DATA.subjects.find(x=>x.id===sid) || {color:"#38bdf8", emoji:"📘", name:subName(sid)};
  const books = (typeof bookList === "function") ? bookList(sid) : [];
  if(!books.length){ main.innerHTML = `<div class="page-head"><h1>📕 ${s.name}</h1><p>کتاب این درس به‌زودی اضافه می‌شود.</p></div>`; return; }

  // اگر کتاب مشخصی خواسته شده، همان را نشان بده
  const one = bookId ? books.find(b=>b.id===bookId) : (books.length===1 ? books[0] : null);
  if(one){ renderOneBook(main, s, one); return; }

  const all = books.reduce((a,b)=>a.concat(b.chapters),[]);
  const done = all.filter(c=>STATE.progress.completed_lessons.includes(chapterKey(sid,c.id))).length;
  const pct = Math.round(done*100/all.length);

  main.innerHTML = `
    <div class="page-head"><h1>${s.emoji} کتاب‌های ${s.name}</h1>
      <p>${books.length} کتاب مستقل • ${all.length} فصل • ${all.reduce((a,c)=>a+(c.minutes||0),0)} دقیقه مطالعه</p></div>
    <div class="card">
      <div style="display:flex;justify-content:space-between;font-size:13px;color:var(--muted);margin-bottom:6px">
        <span>پیشرفت مطالعه کتاب‌های این درس</span><span>${(done).toLocaleString("fa-IR")} از ${all.length.toLocaleString("fa-IR")} فصل (${pct}٪)</span></div>
      <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,#facc15,#22c55e)"></div></div>
    </div>
    <div class="grid-cards" id="blist"></div>`;
  const g = $("#blist");
  books.forEach(b=>{
    const d = b.chapters.filter(c=>STATE.progress.completed_lessons.includes(chapterKey(sid,c.id))).length;
    const pc = Math.round(d*100/b.chapters.length);
    const qn = (typeof QB!=="undefined" && QB[b.id]) ? QB[b.id].length : 0;
    const el = document.createElement("div"); el.className="card clickable";
    el.innerHTML = `<div class="emoji">${b.icon}</div>
      <h3>${b.title}</h3>
      <p>${b.sub||b.desc||""}</p>
      <div style="color:var(--muted);font-size:12.5px;margin:8px 0">📚 ${b.chapters.length} فصل • ⏱ ${b.minutes} دقیقه${qn?` • 🎯 ${qn} سؤال`:""} • 🏷 ${b.level}</div>
      <div class="bar"><div class="bar-fill" style="width:${pc}%"></div></div>
      <div style="font-size:12px;color:var(--muted);margin-top:6px">${d.toLocaleString("fa-IR")} از ${b.chapters.length.toLocaleString("fa-IR")} فصل (${pc}٪)</div>
      <div class="card-actions">
        <button class="btn btn-primary" data-act="read">📖 مطالعه</button>
        <button class="btn btn-ghost" data-act="teach">🧑‍🏫 تدریس استاد</button>
        <button class="btn btn-ghost" data-act="jozve">📝 جزوه</button>
        ${qn?`<button class="btn btn-secondary" data-act="quiz">🎯 آزمون</button>`:""}
      </div>`;
    el.onclick = (ev)=>{
      const a = ev.target.getAttribute && ev.target.getAttribute("data-act");
      if(a==="teach") openTeacherBook(b.id);
      else if(a==="jozve") showJozve(b.id);
      else if(a==="quiz") startBookQuiz(b.id);
      else openBookHome(sid, b.id);
    };
    g.appendChild(el);
  });
}

/* ---------- یک کتاب مشخص ---------- */
function renderOneBook(main, s, bk){
  const flat = bk.chapters;
  const doneCount = flat.filter(c=>STATE.progress.completed_lessons.includes(chapterKey(bk.sid,c.id))).length;
  const pct = flat.length ? Math.round(doneCount*100/flat.length) : 0;
  const qn = (typeof QB!=="undefined" && QB[bk.id]) ? QB[bk.id].length : 0;
  const qs = qn ? (QB[bk.id]||[]) : [];

  let toc = "";
  bk.parts.forEach(p=>{
    toc += `<div class="bk-part-title">${p.title}</div>`;
    p.chapters.forEach(c=>{
      const d = STATE.progress.completed_lessons.includes(chapterKey(bk.sid,c.id));
      const cq = qs.filter(q=>q.ch===c.id).length;
      toc += `<div class="bk-toc-item" data-ch="${c.id}">
        <span class="bk-toc-emoji">📄</span>
        <span class="bk-toc-name">${c.title}</span>
        <span class="bk-toc-meta">${c.minutes?`⏱ ${c.minutes} دقیقه`:""} ${cq?`🎯 ${cq}`:""} ${d?"✅":""}</span>
      </div>`;
    });
  });

  main.innerHTML = `
    <div class="card" style="background:linear-gradient(135deg,${s.color||"#38bdf8"}22,transparent);border-color:${s.color||"#38bdf8"}44;margin-bottom:16px">
      <div style="display:flex;gap:18px;align-items:center;flex-wrap:wrap">
        <div style="font-size:56px">${bk.icon||s.emoji}</div>
        <div style="flex:1;min-width:240px">
          <h2 style="font-size:22px;margin-bottom:6px">${bk.title}</h2>
          <div style="color:var(--muted);font-size:13px;line-height:1.9">
            ${bk.sub||""}<br>
            📚 ${bk.parts.length} بخش • ${flat.length} فصل • ⏱ ${bk.minutes} دقیقه • 🏷 ${bk.level}
            ${qn?`<br>🎯 ${qn} سؤال اختصاصی این کتاب`:""}
          </div>
        </div>
        <button class="btn btn-ghost" onclick="openBookHome('${bk.sid}')">🔙 کتاب‌های ${subName(bk.sid)}</button>
      </div>
      <div style="margin-top:14px">
        <div style="display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin-bottom:6px">
          <span>پیشرفت مطالعه این کتاب</span><span>${doneCount.toLocaleString("fa-IR")} از ${flat.length.toLocaleString("fa-IR")} فصل (${pct}٪)</span>
        </div>
        <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,#facc15,#22c55e)"></div></div>
      </div>
      <div style="display:flex;gap:8px;margin-top:14px;flex-wrap:wrap">
        <button class="btn btn-primary" onclick="openBookChapter('${bk.sid}','${flat[0].id}')">📖 شروع از فصل اول</button>
        <button class="btn" style="background:var(--warning);color:#0f172a" onclick="openTeacherBook('${bk.id}')">🧑‍🏫 کلاس استاد این کتاب</button>
        <button class="btn btn-ghost" onclick="showJozve('${bk.id}')">📝 جزوه این کتاب</button>
        ${qn?`<button class="btn btn-secondary" onclick="startBookQuiz('${bk.id}')">🎯 آزمون کتاب</button>`:""}
      </div>
    </div>
    <div class="section-title">📑 فهرست مطالب</div>
    <div class="bk-toc">${toc}</div>`;

  $$(".bk-toc-item").forEach(el=>{ el.onclick = ()=> openBookChapter(bk.sid, el.dataset.ch); });
}

/* آیکون فصل‌ها (اختیاری) */
const ARTICLE_ICONS = {};

/* ---------- خواندن یک فصل ---------- */
function renderBookChapter(sid, chId){
  const main = $("#main");
  const s = APP_DATA.subjects.find(x=>x.id===sid);
  const bk = BOOK_DATA[sid];
  const flat = bookFlatChapters(bk);
  const idx = flat.findIndex(c=>c.id===chId);
  if(idx < 0){ setView("subjects"); return; }
  const ch = flat[idx];
  const prev = flat[idx-1], next = flat[idx+1];
  const key = chapterKey(sid, ch.id);
  const done = STATE.progress.completed_lessons.includes(key);

  STATE.book = { sid, chId, idx };

  // فهرست کنار صفحه (برای دسکتاپ)
  let sideToc = "";
  bk.parts.forEach(p=>{
    sideToc += `<div class="bk-side-part">${p.title}</div>`;
    p.chapters.forEach(c=>{
      const isCur = c.id === ch.id;
      const isDone = STATE.progress.completed_lessons.includes(chapterKey(sid,c.id));
      sideToc += `<div class="bk-side-item ${isCur?'on':''}" data-ch="${c.id}">
        <span>${isDone?"✅":"▫️"}</span><span>${c.title}</span></div>`;
    });
  });

  // کلمات و زمان تخمینی
  const plain = ch.blocks.map(b=>{
    if(b.x) return b.x;
    if(b.items) return b.items.join(" ");
    if(b.q) return (b.q||"") + " " + (b.a||"") + " " + (b.steps||[]).join(" ");
    if(b.rows) return b.rows.flat().join(" ");
    return "";
  }).join(" ").replace(/<[^>]+>/g,"");
  const words = plain.split(/\s+/).filter(Boolean).length;

  main.innerHTML = `
  <div class="bk-layout">
    <aside class="bk-side">${sideToc}</aside>
    <article class="bk-read">
      <div class="bk-crumb">
        <span onclick="openBookHome('${sid}', '${(bookOfChapter(sid,ch.id)||{}).id||""}')" style="cursor:pointer;color:var(--accent)">${(bookOfChapter(sid,ch.id)||{}).title || (BOOK_DATA[sid]||{}).title || ""}</span>
        <span class="bk-crumb-sep">›</span><span>${ch.partTitle}</span>
      </div>
      <h1 class="bk-ch-title">${ch.title}</h1>
      <div class="bk-ch-meta">
        <span>⏱ ${ch.minutes||Math.max(5,Math.round(words/180))} دقیقه مطالعه</span>
        <span>📝 ${words.toLocaleString("fa-IR")} کلمه</span>
        <span>فصل ${(idx+1).toLocaleString("fa-IR")} از ${flat.length.toLocaleString("fa-IR")}</span>
      </div>
      ${ch.intro?`<div class="bk-intro">${ch.intro}</div>`:""}

      <div class="bk-body">${ch.blocks.map(renderBlock).join("")}</div>

      <div class="bk-ch-foot">
        <button class="btn ${done?'btn-success':'btn-ghost'}" id="bkDone">
          ${done?"✅ این فصل را خوانده‌ام":"⬜ علامت بزن: خوانده شد"}</button>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <button class="btn btn-ghost" onclick="openBookHome('${sid}', '${(bookOfChapter(sid,ch.id)||{}).id||""}')">📑 فهرست کتاب</button>
          ${chapterQuizCount(sid, ch.id) ? `<button class="btn" style="background:var(--accent2);color:#fff" onclick="startChapterQuiz('${(bookOfChapter(sid,ch.id)||{}).id||""}','${ch.id}')">🎯 تست این فصل (${chapterQuizCount(sid,ch.id)})</button>` : ""}
          ${next?`<button class="btn btn-primary" id="bkNextChapter">فصل بعدی: ${next.title.slice(0,22)}${next.title.length>22?"…":""} ➡️</button>`:""}
        </div>
      </div>

      <div class="bk-nav">
        ${prev?`<button class="btn btn-ghost" onclick="openBookChapter('${sid}','${prev.id}')">⬅️ فصل قبل</button>`:"<span></span>"}
        ${next?`<button class="btn btn-ghost" onclick="openBookChapter('${sid}','${next.id}')">فصل بعد ➡️</button>`:"<span></span>"}
      </div>
    </article>
  </div>`;

  $$(".bk-side-item").forEach(el=>{ el.onclick = ()=>openBookChapter(sid, el.dataset.ch); });
  const dbtn = $("#bkDone");
  if(dbtn) dbtn.onclick = ()=> toggleBookDone(sid, ch.id);
  const nbtn = $("#bkNextChapter");
  if(nbtn) nbtn.onclick = ()=> openBookChapter(sid, next.id);

  // ذخیره اینکه آخرین فصل کجا بود
  STATE.progress.last_book = { sid, chId };
  saveProgress();
  main.scrollTop = 0;
  // در حالت دسکتاپ، ستون کنار را تا فصل جاری اسکرول کن
  const act = document.querySelector(".bk-side-item.on");
  if(act && act.scrollIntoView) act.scrollIntoView({block:"center"});
}

function chapterOf(sid, chId){
  const bk = BOOK_DATA[sid]; if(!bk) return null;
  for(const p of bk.parts) for(const c of p.chapters) if(c.id===chId) return c;
  return null;
}
function chapterQuizCount(sid, chId){
  if(typeof QB === "undefined") return 0;
  const bs = (typeof bookList === "function") ? bookList(sid) : [];
  return bs.reduce((a,b)=>a + ((QB[b.id]||[]).filter(q=>q.ch===chId).length), 0);
}

function toggleBookDone(sid, chId){
  const key = chapterKey(sid, chId);
  const arr = STATE.progress.completed_lessons;
  const i = arr.indexOf(key);
  const chMin = (chapterOf(sid, chId)||{}).minutes || 30;
  if(i>=0){ arr.splice(i,1); logStudy(-chMin, true); toast("علامت برداشته شد"); }
  else { arr.push(key); logStudy(chMin, true); toast(`✅ فصل خوانده شد (+${chMin} دقیقه مطالعه)`); }
  saveProgress();
  renderBookChapter(sid, chId);
}

function openBookChapter(sid, chId){
  STATE._bookOpen = {sid, chId};      // باید قبل از setView ست شود چون render() از آن استفاده می‌کند
  STATE.activeSubject = sid;
  setView("book-chapter");
}
function openBookHome(sid, bookId){ STATE.activeSubject = sid; STATE._bookId = bookId || null; setView("book"); }
/* کتابی که فصل جاری به آن تعلق دارد */
function bookOfChapter(sid, chId){
  const bs = (typeof bookList === "function") ? bookList(sid) : [];
  return bs.find(b => b.chapters.some(c=>c.id===chId)) || bs[0] || null;
}
/* تست یک فصل از یک کتاب */
function startChapterQuiz(bookId, chId){
  const qs = (typeof QB!=="undefined" && QB[bookId]) ? QB[bookId].filter(q=>q.ch===chId) : [];
  if(!qs.length) return;
  const sid = (findBook(bookId)||{}).sid;
  STATE.quiz = { questions: qs.map(q=>bookQ(q, bookId, sid)), idx:0, correct:0,
                 subject: (findBook(bookId)||{}).title || "", book:{ bookId: bookId, chId: chId } };
  setView("quiz-playing");
}
function bookQ(q, bookId, sid){
  return { q:q.q, choices:q.c, answer:q.a, subject:sid, year:"", konkori:q.k||"", full_solution:q.s||"", book:bookId };
}
/* آزمون کامل یک کتاب */
function startBookQuiz(bookId){
  const qs = (typeof QB!=="undefined" && QB[bookId]) ? QB[bookId] : [];
  const bk = findBook(bookId);
  if(!qs.length || !bk) return;
  STATE.quiz = { questions: shuffle(qs).map(q=>bookQ(q, bookId, bk.sid)), idx:0, correct:0,
                 subject: bk.title, book:{ bookId: bookId, chId:null } };
  setView("quiz-playing");
}
