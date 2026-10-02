/* =====================================================
   کتاب درسی کامل — ظرف داده‌ها
   هر درس در فایل جداگانه‌ای پر می‌شود: BOOK_DATA[subjectId] = {...}
===================================================== */
var BOOK_DATA = {};

/* فهرست کتاب‌های موجود (برای نمایش وضعیت در صفحه درس‌ها) */
function hasBook(sid){ return !!(typeof BOOK_DATA!=="undefined" && BOOK_DATA[sid] && BOOK_DATA[sid].parts && BOOK_DATA[sid].parts.length); }
function bookChapterCount(sid){ if(!hasBook(sid)) return 0; return BOOK_DATA[sid].parts.reduce((a,p)=>a+p.chapters.length,0); }
function bookMinutes(sid){ if(!hasBook(sid)) return 0; return BOOK_DATA[sid].parts.reduce((a,p)=>a+p.chapters.reduce((b,c)=>b+(c.minutes||0),0),0); }
