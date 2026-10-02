/* expand_books.js
   فصل‌های تکمیلی (bx1.js + bx2.js) را داخل فایل‌های کتاب ادغام می‌کند.
   اجرا:  cd /home/user/bme_konkur && node content/expand_books.js            */
const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const WEB = path.join(ROOT, "web");

const FILES = {
  "book_anatomy.js": ["anatomy"],
  "book_circuits.js": ["circuits"],
  "book_last.js": ["biomechanics", "imaging"],
  "book_math.js": ["math"],
  "book_others.js": ["biomaterials", "control", "instrumentation"],
  "book_physics.js": ["physics"],
  "book_signals.js": ["signals"],
};

/* ۱) خواندن داده‌های کتاب */
const BOOK_DATA = {};
Object.keys(FILES).forEach(f => {
  const src = fs.readFileSync(path.join(WEB, f), "utf8");
  eval(src);
});

/* ۲) خواندن فصل‌های تکمیلی */
const EXTRA = {};
["bx1.js", "bx2.js"].forEach(f => {
  const p = path.join(__dirname, f);
  if (!fs.existsSync(p)) return;
  const src = fs.readFileSync(p, "utf8") + "\nreturn EXTRA;";
  Object.assign(EXTRA, new Function(src)());
});

/* ۳) ادغام با جلوگیری از تکرار */
let added = 0;
Object.keys(EXTRA).forEach(sid => {
  if (!BOOK_DATA[sid]) { console.log("⚠️ کتاب یافت نشد:", sid); return; }
  const book = BOOK_DATA[sid];
  const existing = new Set();
  book.parts.forEach(p => p.chapters.forEach(c => existing.add(c.id)));
  const exIds = c => c.chapters.map(x => x.id);
  EXTRA[sid].forEach(part => {
    const ids = exIds(part);
    const at = book.parts.findIndex(p => p.chapters.some(c => ids.indexOf(c.id) >= 0));
    if (at >= 0) {
      book.parts[at] = { title: part.title, chapters: part.chapters };
      console.log("  ↻", sid, "/", part.title, "(" + ids.length + " فصل به‌روزرسانی شد)");
    } else {
      book.parts.push({ title: part.title, chapters: part.chapters });
      console.log("  +", sid, "/", part.title, "(" + ids.length + " فصل جدید)");
      added += ids.length;
    }
    ids.forEach(i => existing.add(i));
  });
});

/* ۴) بازنویسی فایل‌ها */
const HEADER = {
  "book_anatomy.js": "/* کتاب آناتومی و فیزیولوژی */",
  "book_circuits.js": "/* کتاب مدارهای الکتریکی و الکترونیک */",
  "book_last.js": "/* کتاب بیومکانیک و تصویربرداری پزشکی */",
  "book_math.js": "/* کتاب ریاضیات */",
  "book_others.js": "/* کتاب بیومواد، کنترل و ابزار دقیق */",
  "book_physics.js": "/* کتاب فیزیک */",
  "book_signals.js": "/* کتاب سیگنال‌ها و سیستم‌ها */",
};

Object.keys(FILES).forEach(f => {
  let out = HEADER[f] + "\n";
  FILES[f].forEach(sid => {
    out += "BOOK_DATA." + sid + " = " + JSON.stringify(BOOK_DATA[sid], null, 1) + ";\n";
  });
  fs.writeFileSync(path.join(WEB, f), out, "utf8");
});

/* ۵) گزارش */
let chapters = 0, words = 0;
Object.keys(BOOK_DATA).sort().forEach(sid => {
  const b = BOOK_DATA[sid];
  const ch = b.parts.reduce((a, p) => a + p.chapters.length, 0);
  const w = b.parts.reduce((a, p) => a + p.chapters.reduce((x, c) => x + JSON.stringify(c).split(/\s+/).length, 0), 0);
  chapters += ch; words += w;
  console.log(sid.padEnd(15), "بخش:", b.parts.length, "| فصل:", ch, "| کلمه ≈", w);
});
console.log("\nفصل‌های جدید اضافه‌شده:", added);
console.log("جمع کتاب‌ها:", Object.keys(BOOK_DATA).length, "| فصل:", chapters, "| کلمه ≈", words);
