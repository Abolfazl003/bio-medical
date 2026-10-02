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
  if(t === "fig")  return `<div class="bk-fig"><pre>${b.x}</pre>${b.cap?`<div class="bk-fig-cap">${b.cap}</div>`:""}</div>`;

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

/* ---------- صفحه اصلی کتاب ---------- */
function renderBookHome(sid){
  const main = $("#main");
  const s = APP_DATA.subjects.find(x=>x.id===sid);
  const bk = (typeof BOOK_DATA !== "undefined") ? BOOK_DATA[sid] : null;
  const color = s.color;

  if(!bk){
    main.innerHTML = `<div class="page-head"><h1>📕 ${s.name}</h1>
      <p>کتاب این درس به‌زودی اضافه می‌شود.</p>
      <button class="btn btn-ghost" onclick="setView('subject-detail')">🔙 برگشت</button></div>`;
    return;
  }

  const flat = bookFlatChapters(bk);
  const doneCount = flat.filter(c=>STATE.progress.completed_lessons.includes(chapterKey(sid,c.id))).length;
  const pct = Math.round(doneCount*100/flat.length);

  // فهرست مطالب
  let toc = "";
  bk.parts.forEach((p, pi)=>{
    toc += `<div class="bk-part-title">${p.title}</div>`;
    p.chapters.forEach(c=>{
      const done = STATE.progress.completed_lessons.includes(chapterKey(sid,c.id));
      const reader = `${ARTICLE_ICONS[c.id]||"📄"}`;
      toc += `<div class="bk-toc-item" data-ch="${c.id}">
        <span class="bk-toc-emoji">${reader}</span>
        <span class="bk-toc-name">${c.title}</span>
        <span class="bk-toc-meta">${c.minutes?`⏱ ${c.minutes} دقیقه`:""} ${done?"✅":""}</span>
      </div>`;
    });
  });

  main.innerHTML = `
    <div class="card" style="background:linear-gradient(135deg,${color}22,transparent);border-color:${color}44;margin-bottom:16px">
      <div style="display:flex;gap:18px;align-items:center;flex-wrap:wrap">
        <div style="font-size:56px">${s.emoji}</div>
        <div style="flex:1;min-width:240px">
          <h2 style="font-size:22px;margin-bottom:6px">${bk.title}</h2>
          <div style="color:var(--muted);font-size:13px;line-height:1.9">
            ${bk.subtitle||""}<br>
            📚 ${bk.parts.length} بخش • ${flat.length} فصل • ${flat.reduce((a,c)=>a+(c.minutes||0),0)} دقیقه مطالعه
          </div>
        </div>
        <button class="btn btn-ghost" onclick="setView('subject-detail')">🔙 برگشت به درس</button>
      </div>
      <div style="margin-top:14px">
        <div style="display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin-bottom:6px">
          <span>پیشرفت مطالعه کتاب</span><span>${doneCount} از ${flat.length} فصل (${pct}%)</span>
        </div>
        <div class="progress"><div class="progress-bar" style="width:${pct}%;background:linear-gradient(90deg,#facc15,#22c55e)"></div></div>
      </div>
    </div>

    ${flat.length ? `<div style="display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap">
      <button class="btn btn-primary" onclick="openBookChapter('${sid}', '${flat[0].id}')">📖 شروع مطالعه از فصل اول</button>
      ${doneCount>0 && doneCount<flat.length ? `<button class="btn" style="background:var(--warning);color:#0f172a" onclick="openBookChapter('${sid}','${(flat.find(c=>!STATE.progress.completed_lessons.includes(chapterKey(sid,c.id)))||flat[0]).id}')">▶️ ادامه از جایی که ماندم</button>`:""}
    </div>` : ""}

    <div class="section-title">📑 فهرست مطالب</div>
    <div class="bk-toc">${toc}</div>
  `;

  $$(".bk-toc-item").forEach(el=>{
    el.onclick = ()=> openBookChapter(sid, el.dataset.ch);
  });
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
        <span onclick="openBookHome('${sid}')" style="cursor:pointer;color:var(--accent)">${bk.title}</span>
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
          <button class="btn btn-ghost" onclick="openBookHome('${sid}')">📑 فهرست کتاب</button>
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

function toggleBookDone(sid, chId){
  const key = chapterKey(sid, chId);
  const arr = STATE.progress.completed_lessons;
  const i = arr.indexOf(key);
  if(i>=0){ arr.splice(i,1); toast("علامت برداشته شد"); }
  else { arr.push(key); toast("✅ فصل خوانده‌شده علامت خورد"); }
  saveProgress();
  renderBookChapter(sid, chId);
}

function openBookChapter(sid, chId){
  STATE._bookOpen = {sid, chId};      // باید قبل از setView ست شود چون render() از آن استفاده می‌کند
  STATE.activeSubject = sid;
  setView("book-chapter");
}
function openBookHome(sid){ STATE.activeSubject = sid; setView("book"); }
