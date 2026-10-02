/* =============================================================
   teacher_jozve.js — تدریس کامل استاد و جزوه اختصاصی هر کتاب
   (نسخه ۱.۳.۰)
   استاد تمام کتاب را مثل کلاس واقعی درس می‌دهد: هر فصل، هر فرمول،
   هر مثال و هر نکته — و جزوه قابل چاپ از همان محتوا ساخته می‌شود.
   ============================================================= */

/* ── تبدیل هر بلوک کتاب به جمله گفتاری استاد ── */
function tpSpeak(b){
  const t = b.t;
  if(t === "p")     return b.x;
  if(t === "quote") return `«${b.x}»`;
  if(t === "f")     return `📐 این فرمول را با خودکار قرمز در جزوه‌ات بنویس: ${b.label?b.label+" → ":""}${b.x}${b.d?" . یعنی: "+b.d:""}`;
  if(t === "ul" || t === "ol") return (b.items||[]).map((x,i)=>`${(t==="ol"?(i+1)+") ":"• ")}${x}`).join("\n");
  if(t === "tbl"){
    const head = (b.head||[]).join(" | ");
    const rows = (b.rows||[]).slice(0,5).map(r=>"   – "+r.join(" | ")).join("\n");
    return `📊 این جدول خیلی مهم است. ستون‌ها: ${head}\n${rows}`;
  }
  if(t === "note")  return `💡 نکته استاد: ${b.x}`;
  if(t === "warn")  return `⚠️ دام آزمون — حواست باشد: ${b.x}`;
  if(t === "tip")   return `🎯 ترفند کنکوری: ${b.x}`;
  if(t === "ex")    return `✏️ ${b.title||"یک مثال حل‌شده"} — صورت سؤال: ${b.q}\nقدم‌به‌قدم می‌رویم:\n` + (b.steps||[]).map((s,i)=>`   ${i+1}. ${s}`).join("\n") + (b.a?`\n   ➡️ پس جواب: ${b.a}`:"");
  if(t === "exr")   return `🎯 تمرین برای خودت (اول تلاش کن، بعد پاسخ): ${b.q}`;
  if(t === "fig")   return `🖼 به این شکل نگاه کن — ${b.cap||""}. شکل را در ذهنت بکش، بعد برو سراغ متن.`;
  if(t === "sum")   return `📋 جمع‌بندی این فصل:\n` + (b.items||[]).map(x=>"• "+x).join("\n");
  return "";
}

/* ── ساخت کل کلاس درس یک کتاب ── */
function buildLecture(book){
  const slides = [];
  const t = book.teacher || {};
  const totalCh = book.chapters.length;
  const totalQ = (typeof QB !== "undefined" && QB[book.id]) ? QB[book.id].length : 0;

  slides.push({ kind:"welcome", title:"شروع کلاس", body:
`سلام! من استاد این درس هستم. امروز کتاب «${book.title}» را کامل با هم می‌خوانیم.

📌 موضوع: ${book.sub}
⏱ زمان پیشنهادی: ${book.minutes} دقیقه | 📚 ${totalCh} فصل | 🎯 ${totalQ} سؤال اختصاصی این کتاب

${t.intro || ""}

روش کلاس این است: فصل‌به‌فصل جلو می‌رویم، هر فرمول را با هم می‌نویسیم، مثال‌ها را قدم‌به‌قدم حل می‌کنیم و در پایان هر فصل نکته آزمونی‌اش را می‌گویم. اگر جایی برایت مبهم بود، برگرد عقب — این کلاس ثبت‌شده است!` });

  if(t.emphasis && t.emphasis.length){
    slides.push({ kind:"emphasis", title:"سه چیزی که از این کتاب باید یادت بماند", body:
      t.emphasis.map((e,i)=>`${i+1}. ${e}`).join("\n\n") + `\n\nاین‌ها را بالای صفحه اول جزوه‌ات بنویس؛ همان‌هایی هستند که بیشترین بازدهی را در آزمون دارند.` });
  }

  book.parts.forEach(part=>{
    slides.push({ kind:"part", title:"ورود به " + part.title, body:
      `خب، وارد ${part.title} می‌شویم. این بخش ${part.chapters.length} فصل دارد:\n` +
      part.chapters.map((c,i)=>`${i+1}. ${c.title} (${c.minutes||30} دقیقه)`).join("\n") +
      `\n\nترتیب را عوض نکن؛ هر فصل روی فصل قبل سوار است.` });

    part.chapters.forEach(ch=>{
      const head = ch.title.split("—").pop().trim();
      slides.push({ kind:"chapter", title: ch.title, body:
        (ch.intro ? ch.intro + "\n\n" : "") + `بگذار فصل «${head}» را از اول باز کنم…` });

      let buf = [], title = "تدریس " + head;
      const flush = ()=>{
        if(!buf.length) return;
        const text = buf.join("\n\n");
        // تقسیم اسلایدهای بلند
        const chunks = [];
        let cur = "";
        text.split("\n\n").forEach(p=>{
          if((cur + p).length > 900){ if(cur) chunks.push(cur); cur = p; }
          else cur += (cur ? "\n\n" : "") + p;
        });
        if(cur) chunks.push(cur);
        chunks.forEach((c, i)=> slides.push({ kind:"teach", title: title + (chunks.length>1 ? ` (${i+1}/${chunks.length})` : ""), body: c }));
        buf = [];
      };
      ch.blocks.forEach(b=>{
        if(b.t === "h"){ flush(); title = b.x; }
        else if(b.t === "h3"){ flush(); title = b.x; }
        else { const s = tpSpeak(b); if(s) buf.push(s); }
      });
      flush();

      const qs = (typeof QB !== "undefined" && QB[book.id]) ? QB[book.id].filter(q=>q.ch===ch.id) : [];
      slides.push({ kind:"chapter-end", title:"پایان " + head, body:
        `تمام شد. جمع‌بندی استاد از این فصل:\n` +
        (ch.blocks.filter(x=>x.t==="sum").reduce((a,x)=>a.concat(x.items||[]),[]).map(x=>"• "+x).join("\n") || "• مطالب این فصل را یک بار مرور کن.") +
        (qs.length ? `\n\n🎯 همین حالا ${qs.length} سؤال اختصاصی این فصل را بزن: از پایین صفحه، دکمه «تست این فصل» را بزن.` : "") +
        `\n\nاگر آماده‌ای، برویم فصل بعد.` });
    });
  });

  const allQ = (typeof QB !== "undefined" && QB[book.id]) ? QB[book.id] : [];
  slides.push({ kind:"final", title:"پایان کلاس و تکلیف", body:
`خب، کل کتاب «${book.title}» را با هم خواندیم. حالا تکلیف:

1) یک بار سریع از جزوه این کتاب (دکمه «جزوه استاد») بگذر — ۱۰ دقیقه کافی است.
2) آزمون این کتاب را بزن${allQ.length? ` (${allQ.length} سؤال)`:""} و هر سؤالی که غلط زدی را با «ذخیره» نگه دار.
3) فصل‌هایی که علامت نخورده‌اند را دوباره بخوان.

یادت باشد: درک + تمرین، نه حفظ کردن. اگر این کتاب را کامل بفهمی، بخش بزرگی از درس ${book.title.split(" ")[0]} را بسته‌ای.

موفق باشی — من همین‌جا هستم. 🌟` });

  return { slides: slides, title: book.title };
}

/* ── صفحه کلاس استاد ── */
function renderTeacherBookLesson(main){
  const bookId = STATE.teacher && STATE.teacher.bookId;
  const book = findBook(bookId);
  if(!book){ setView("teacher"); return; }
  const L = STATE._lecture || (STATE._lecture = buildLecture(book));
  const si = STATE.teacher.slide;
  const sl = L.slides[si];
  const total = L.slides.length;
  const pct = Math.round(si * 100 / (total-1));
  const colors = { welcome:"var(--accent)", emphasis:"var(--warning)", part:"var(--accent2)", chapter:"var(--accent)", teach:"var(--text)", "chapter-end":"var(--success)", final:"var(--warning)" };
  const labels = { welcome:"شروع", emphasis:"نکات کلیدی", part:"شروع بخش", chapter:"فصل", teach:"تدریس", "chapter-end":"جمع‌بندی فصل", final:"پایان" };

  main.innerHTML=`
    <div class="quiz-wrap">
      <div class="quiz-meta">
        <div>🧑‍🏫 <b>${book.title}</b> <span style="color:var(--muted);font-size:12px">— ${book.sid ? subName(book.sid) : ""}</span></div>
        <div>بخش ${(si+1).toLocaleString("fa-IR")} از ${total.toLocaleString("fa-IR")}</div>
      </div>
      <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,var(--warning),var(--accent))"></div></div>
      <div class="lecture-card">
        <div class="lecture-kind" style="color:${colors[sl.kind]||"var(--accent)"}">${labels[sl.kind]||"کلاس"}</div>
        <h2 class="lecture-title">${sl.title}</h2>
        <div class="lecture-body">${sl.body}</div>
        <div class="q-actions" style="margin-top:24px">
          <button class="btn btn-ghost" onclick="setView('teacher')">🔙 فهرست کتاب‌ها</button>
          <div style="display:flex;gap:8px;flex-wrap:wrap">
            <button class="btn btn-ghost" onclick="showJozve('${book.id}')">📝 جزوه این کتاب</button>
            ${si>0?`<button class="btn btn-ghost" onclick="teacherSlide(-1)">⬅️ قبلی</button>`:""}
            ${si<total-1?`<button class="btn btn-primary" onclick="teacherSlide(1)">بعدی ➡️</button>`:
              `<button class="btn btn-success" onclick="startBookQuiz('${book.id}')">🎯 آزمون این کتاب</button>`}
          </div>
        </div>
      </div>
      <div class="lecture-nav">
        ${L.slides.map((s,i)=>`<span class="ln-dot ${i===si?"on":""}" onclick="teacherJump(${i})" title="${s.title}"></span>`).join("")}
      </div>
    </div>`;
  main.scrollTop = 0;
}
function teacherSlide(d){ STATE.teacher.slide += d; render(); }
function teacherJump(i){ STATE.teacher.slide = i; render(); }
function openTeacherBook(bookId){
  STATE.teacher = { bookId: bookId, slide: 0 };
  STATE._lecture = null;
  setView("teacher-lesson");
}

/* ── جزوه اختصاصی هر کتاب (قابل چاپ) ── */
function buildJozve(book){
  const F = [], TBL = [], NOTES = [], SUM = [], EXS = [];
  book.chapters.forEach(ch=>{
    ch.blocks.forEach(b=>{
      if(b.t==="f")   F.push({ ch: ch.title, label: b.label||"", x: b.x, d: b.d||"" });
      if(b.t==="tbl") TBL.push({ ch: ch.title, head: b.head, rows: b.rows });
      if(b.t==="note"||b.t==="warn"||b.t==="tip") NOTES.push({ ch: ch.title, kind: b.t, x: b.x });
      if(b.t==="sum") SUM.push({ ch: ch.title, items: b.items||[] });
      if(b.t==="ex")  EXS.push({ ch: ch.title, title: b.title||"مثال", q: b.q, a: b.a||"" });
    });
  });
  const qs = (typeof QB !== "undefined" && QB[book.id]) ? QB[book.id] : [];
  return { F, TBL, NOTES, SUM, EXS, qs };
}

function renderJozve(main){
  const book = findBook(STATE._jozveBookId);
  if(!book){ setView("teacher"); return; }
  const j = STATE._jozve || (STATE._jozve = buildJozve(book));
  const t = book.teacher || {};
  const done = book.chapters.filter(c=>STATE.progress.completed_lessons.includes(chapterKey(book.sid,c.id))).length;

  main.innerHTML = `
  <div class="jozve-toolbar no-print">
    <button class="btn btn-ghost" onclick="setView('teacher')">🔙 فهرست</button>
    <button class="btn btn-primary" onclick="window.print()">🖨️ چاپ / ذخیره PDF</button>
    <button class="btn btn-success" onclick="startBookQuiz('${book.id}')">🎯 آزمون کتاب (${j.qs.length} سوال)</button>
  </div>
  <article class="jozve" id="jozve">
    <header class="jozve-head">
      <div class="jozve-badge">📝 جزوه استاد — ${subName(book.sid)}</div>
      <h1>${book.title}</h1>
      <p class="jozve-sub">${book.sub}</p>
      <div class="jozve-meta">
        <span>📚 ${book.chapters.length} فصل</span><span>⏱ ${book.minutes} دقیقه مطالعه</span>
        <span>🎯 ${j.qs.length} سؤال اختصاصی</span><span>✅ ${done} فصل خوانده‌شده</span>
        <span>🏷 سطح: ${book.level}</span>
      </div>
    </header>

    ${t.intro ? `<section class="jz-sec"><h2>۱) چکیده استاد</h2><p>${t.intro}</p>
      ${(t.emphasis&&t.emphasis.length)?`<ul class="jz-key">${t.emphasis.map(e=>`<li>${e}</li>`).join("")}</ul>`:""}</section>` : ""}

    <section class="jz-sec"><h2>۲) نقشه راه</h2>
      ${book.parts.map(p=>`<div class="jz-part"><b>${p.title}</b><ol>${p.chapters.map(c=>`<li>${c.title} <span class="jz-min">${c.minutes||30} دقیقه</span></li>`).join("")}</ol></div>`).join("")}
    </section>

    ${j.F.length ? `<section class="jz-sec"><h2>۳) بانک فرمول (${j.F.length} فرمول)</h2>
      ${j.F.map(f=>`<div class="jz-formula"><div class="jz-f-label">${f.label||"فرمول"}</div>
        <div class="jz-f-body">${f.x}</div>${f.d?`<div class="jz-f-desc">${f.d}</div>`:""}
        <div class="jz-f-ch">${f.ch}</div></div>`).join("")}</section>` : ""}

    ${j.NOTES.length ? `<section class="jz-sec"><h2>۴) نکته‌ها، دام‌ها و ترفندها (${j.NOTES.length})</h2>
      ${j.NOTES.map(n=>`<div class="jz-note jz-${n.kind}">
        <b>${n.kind==="warn"?"⚠️ دام":n.kind==="tip"?"🎯 ترفند":"💡 نکته"}:</b> ${n.x}
        <div class="jz-f-ch">${n.ch}</div></div>`).join("")}</section>` : ""}

    ${j.TBL.length ? `<section class="jz-sec"><h2>۵) جدول‌های مرجع (${j.TBL.length})</h2>
      ${j.TBL.map(tb=>`<div class="jz-tbl-wrap"><div class="jz-f-ch">${tb.ch}</div>
        <table class="jz-table"><thead><tr>${tb.head.map(h=>`<th>${h}</th>`).join("")}</tr></thead>
        <tbody>${tb.rows.map(r=>`<tr>${r.map(c=>`<td>${c}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`).join("")}</section>` : ""}

    ${j.EXS.length ? `<section class="jz-sec"><h2>۶) مثال‌های شاخص کتاب (${j.EXS.length})</h2>
      ${j.EXS.map(e=>`<div class="jz-ex"><b>${e.title}</b> — ${e.q}${e.a?` <span class="jz-ans">➡️ ${e.a}</span>`:""}</div>`).join("")}</section>` : ""}

    ${j.SUM.length ? `<section class="jz-sec"><h2>۷) خلاصه فصل‌به‌فصل</h2>
      ${j.SUM.map(s=>`<div class="jz-sum"><b>${s.ch}</b><ul>${s.items.map(i=>`<li>${i}</li>`).join("")}</ul></div>`).join("")}</section>` : ""}

    ${j.qs.length ? `<section class="jz-sec"><h2>۸) پرسش‌های کلیدی آزمون (${j.qs.length})</h2>
      ${j.qs.map((q,i)=>`<div class="jz-q"><b>${(i+1).toLocaleString("fa-IR")}.</b> ${q.q}
        <div class="jz-q-a">پاسخ: ${["الف","ب","ج","د"][q.a]} — ${q.q&&q.c?q.c[q.a]:""}</div>
        <div class="jz-q-k">🎯 ${q.k}</div></div>`).join("")}</section>` : ""}

    <section class="jz-sec"><h2>۹) چک‌لیست مرور</h2>
      <div class="jz-check">${book.chapters.map(c=>`<div class="jz-ch-item">
        <span>${STATE.progress.completed_lessons.includes(chapterKey(book.sid,c.id))?"✅":"⬜"}</span>
        <span class="jz-ch-name" onclick="openBookChapter('${book.sid}','${c.id}')">${c.title}</span>
        <span class="jz-min">${c.minutes||30} دقیقه</span></div>`).join("")}</div></section>

    <footer class="jz-foot">📝 جزوه استاد — ساخته‌شده از کتاب «${book.title}» | اپلیکیشن کنکور ارشد مهندسی پزشکی</footer>
  </article>`;
  main.scrollTop = 0;
}
function showJozve(bookId){ STATE._jozveBookId = bookId; STATE._jozve = null; setView("jozve"); }

/* =============================================================
   کلاس کامل یک درس (همه کتاب‌های آن درس، پشت سر هم)
   ============================================================= */
function buildCourseLecture(sid){
  const books = (typeof bookList === "function") ? bookList(sid) : [];
  const s = APP_DATA.subjects.find(x=>x.id===sid) || {name:subName(sid)};
  const totCh = books.reduce((a,b)=>a+b.chapters.length,0);
  const totMin = books.reduce((a,b)=>a+b.minutes,0);
  const totQ = books.reduce((a,b)=>a+(((typeof QB!=="undefined"&&QB[b.id])||[]).length),0);
  const slides = [{ kind:"welcome", title:"خوش آمدی", body:
`سلام! کلاس «${s.name}» را شروع می‌کنیم.

📚 در این درس ${books.length} کتاب داریم: ${books.map(b=>b.title).join(" • ")}
📑 مجموعاً ${totCh} فصل و حدود ${Math.round(totMin/60)} ساعت مطالعه | 🎯 ${totQ} سؤال اختصاصی

روش کار: کتاب به کتاب جلو می‌رویم. هر فصل را برایت باز می‌کنم، فرمول‌ها را با هم می‌نویسیم، مثال حلشده را قدم‌به‌قدم می‌رویم و در پایان هر فصل، نکته آزمونی و تست همان فصل را می‌گویم — دقیقاً مثل کلاس حضوری.

اگر جای خاصی برایت مهم است، از نقطه‌های پایین صفحه رد شو تا سریع‌تر برسی. شروع کنیم!` }];

  books.forEach((b,i)=>{
    const L = buildLecture(b);
    L.slides[0].kind = "part2";
    L.slides[0].title = `کتاب ${i+1}: ${b.title}`;
    slides.push(...L.slides);
  });
  return { slides: slides, title: s.name, course:{ sid: sid } };
}

/* ── رندر کلاس (کتاب یا کل درس) ── */
function renderTeacherLecture(main){
  const T = STATE.teacher;
  if(!T){ setView("teacher"); return; }
  if(T.bookId){
    const bk = findBook(T.bookId);
    if(!bk){ setView("teacher"); return; }
    renderLectureUI(main, bk.title, (bk.sid?subName(bk.sid):""), bk.id);
  } else {
    const L = STATE._lecture || (STATE._lecture = buildCourseLecture(T.subject));
    renderLectureUI(main, L.title, "کلاس کامل درس — همه کتاب‌ها", null, L);
  }
}

function renderLectureUI(main, title, sub, bookId, L0){
  const L = L0 || (STATE._lecture || (STATE._lecture = buildLecture(findBook(bookId))));
  const si = Math.min(STATE.teacher.slide, L.slides.length-1);
  const sl = L.slides[si];
  const total = L.slides.length;
  const pct = Math.round(si*100/Math.max(1,total-1));
  const colors = { welcome:"var(--accent)", part2:"var(--accent2)", emphasis:"var(--warning)", part:"var(--accent2)",
                   chapter:"var(--accent)", teach:"var(--text)", "chapter-end":"var(--success)", final:"var(--warning)" };
  const labels = { welcome:"شروع", part2:"کتاب", emphasis:"نکات کلیدی", part:"شروع بخش", chapter:"فصل",
                   teach:"تدریس کامل", "chapter-end":"جمع‌بندی فصل", final:"پایان" };
  const doneMin = progressMinutes();
  main.innerHTML=`
    <div class="quiz-wrap">
      <div class="quiz-meta">
        <div>🧑‍🏫 <b>${title}</b> <span style="color:var(--muted);font-size:12px">— ${sub}</span></div>
        <div>بخش ${(si+1).toLocaleString("fa-IR")} از ${total.toLocaleString("fa-IR")}</div>
      </div>
      <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,var(--warning),var(--accent))"></div></div>
      <div class="lecture-card">
        <div class="lecture-kind" style="color:${colors[sl.kind]||"var(--accent)"}">${labels[sl.kind]||"کلاس"}</div>
        <h2 class="lecture-title">${sl.title}</h2>
        <div class="lecture-body">${sl.body}</div>
        <div class="q-actions" style="margin-top:26px">
          <button class="btn btn-ghost" onclick="setView('teacher')">🔙 کلاس‌ها</button>
          <div style="display:flex;gap:8px;flex-wrap:wrap">
            ${bookId?`<button class="btn btn-ghost" onclick="showJozve('${bookId}')">📝 جزوه این کتاب</button>
              <button class="btn btn-ghost" onclick="openBookHome('${(findBook(bookId)||{}).sid}','${bookId}')">📖 فهرست کتاب</button>`:
              `<button class="btn btn-ghost" onclick="showJozveSubject('${STATE.teacher.subject}')">📝 جزوه کل درس</button>`}
            ${si>0?`<button class="btn btn-ghost" onclick="teacherSlide(-1)">⬅️ قبلی</button>`:""}
            ${si<total-1?`<button class="btn btn-primary" onclick="teacherSlide(1)">بعدی ➡️</button>`
              :`<button class="btn btn-success" onclick="finishTeacher()">✅ پایان + تست این درس</button>`}
          </div>
        </div>
        <div class="study-note">⏱ زمان مطالعه ثبت‌شده‌ات تا الان: <b>${faMin(doneMin)}</b> — هرچه جلوتر بروی این عدد بالا می‌رود.</div>
      </div>
      <div class="lecture-nav">
        ${L.slides.map((s,i)=>`<span class="ln-dot ${i===si?"on":""} ${i<si?"done":""}" onclick="teacherJump(${i})" title="${s.title}"></span>`).join("")}
      </div>
    </div>`;
  main.scrollTop = 0;
}

/* ── جزوه کل یک درس (همه کتاب‌ها یک‌جا) ── */
function showJozveSubject(sid){ STATE._jozveSid = sid; setView("jozve-sub"); }
function renderJozveSubject(main){
  const sid = STATE._jozveSid;
  const books = (typeof bookList === "function") ? bookList(sid) : [];
  if(!books.length){ setView("teacher"); return; }
  const s = APP_DATA.subjects.find(x=>x.id===sid) || {emoji:"📘", name:subName(sid)};
  let html = `<div class="jozve-toolbar no-print">
    <button class="btn btn-ghost" onclick="setView('teacher')">🔙 کلاس‌ها</button>
    <button class="btn btn-primary" onclick="window.print()">🖨️ چاپ / PDF کل جزوه</button>
    <span style="color:var(--muted);font-size:13px">جزوه جامع «${s.name}» — ${books.length} کتاب در یک فایل</span>
  </div><article class="jozve" id="jozve">
    <header class="jozve-head"><div class="jozve-badge">📝 جزوه جامع استاد</div>
      <h1>${s.emoji} ${s.name}</h1>
      <p class="jozve-sub">جمع‌بندی همه کتاب‌های این درس: فرمول‌ها، نکته‌ها، جدول‌ها و پرسش‌های کلیدی</p>
      <div class="jozve-meta"><span>📚 ${books.length} کتاب</span>
        <span>📑 ${books.reduce((a,b)=>a+b.chapters.length,0)} فصل</span>
        <span>⏱ ${books.reduce((a,b)=>a+b.minutes,0)} دقیقه</span>
        <span>🎯 ${books.reduce((a,b)=>a+(((typeof QB!=="undefined"&&QB[b.id])||[]).length),0)} سؤال</span></div>
    </header><section class="jz-sec"><h2>فهرست جزوه‌های کتابی</h2><ol>`;
  books.forEach(b=>{ html += `<li><b>${b.icon||""} ${b.title}</b> — ${b.sub||""}
    <div style="margin-top:6px"><button class="btn btn-sm btn-ghost no-print" onclick="showJozve('${b.id}')">📝 جزوه کامل این کتاب</button></div></li>`; });
  html += `</ol></section>`;
  // ادغام فرمول‌ها و نکته‌های همه کتاب‌ها
  let F=[], N=[];
  books.forEach(b=>{ const j=buildJozve(b); j.F.forEach(f=>F.push({...f, book:b.title})); j.NOTES.forEach(n=>N.push({...n, book:b.title})); });
  html += `<section class="jz-sec"><h2>بانک فرمول کل درس (${F.length} فرمول)</h2>
    ${F.map(f=>`<div class="jz-formula"><div class="jz-f-label">${f.label||"فرمول"}</div><div class="jz-f-body">${f.x}</div>
      <div class="jz-f-ch">${f.book} — ${f.ch}</div></div>`).join("")}</section>`;
  html += `<section class="jz-sec"><h2>همه نکته‌ها و دام‌ها (${N.length})</h2>
    ${N.map(n=>`<div class="jz-note jz-${n.kind}"><b>${n.kind==="warn"?"⚠️ دام":n.kind==="tip"?"🎯 ترفند":"💡 نکته"}:</b> ${n.x}
      <div class="jz-f-ch">${n.book} — ${n.ch}</div></div>`).join("")}</section>`;
  html += `<section class="jz-sec"><h2>پرسش‌های کلیدی همه کتاب‌ها</h2>
    ${books.map(b=>{ const qs=(typeof QB!=="undefined"&&QB[b.id])||[]; return qs.length?`<div class="jz-part"><b>${b.title}</b><ol>
      ${qs.map(q=>`<li>${q.q} <div class="jz-q-a">پاسخ: ${["الف","ب","ج","د"][q.a]} — ${q.c[q.a]}</div></li>`).join("")}</ol></div>`:""; }).join("")}</section>`;
  html += `<footer class="jz-foot">📝 جزوه جامع ${s.name} — اپلیکیشن کنکور ارشد مهندسی پزشکی</footer></article>`;
  main.innerHTML = html;
  main.scrollTop = 0;
}
