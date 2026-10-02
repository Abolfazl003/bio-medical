/* ادغام فصل‌های تکمیلی در کتاب‌های اصلی (قابل اجرای مکرر — idempotent) */
const fs = require('fs');
const path = require('path');
const WEB = path.join(__dirname, '..', 'web');

const BOOK_DATA = {};
eval(fs.readFileSync(path.join(WEB, 'book_circuits.js'), 'utf8'));
eval(fs.readFileSync(path.join(WEB, 'book_others.js'), 'utf8'));
eval(fs.readFileSync(path.join(WEB, 'book_last.js'), 'utf8'));

const EXTRA = {};
eval(fs.readFileSync(path.join(__dirname, 'extra1.js'), 'utf8'));
eval(fs.readFileSync(path.join(__dirname, 'extra2.js'), 'utf8'));

const HDR = {
  circuits: '/* =====================================================\n   کتاب کامل — مدارهای الکتریکی و الکترونیک\n===================================================== */\n',
  others: '/* =====================================================\n   کتاب‌های کامل — کنترل، ابزار دقیق، بیومواد\n===================================================== */\n\n',
  last: '/* =====================================================\n   کتاب‌های کامل — بیومکانیک و تصویربرداری پزشکی\n===================================================== */\n\n'
};

// ۱) ادغام فصل‌های تکمیلی (در صورت نبودشان)
let added = 0;
Object.keys(EXTRA).forEach(sid => {
  if(!BOOK_DATA[sid]) { console.log('⚠︎ درس ناشناخته:', sid); return; }
  const have = new Set();
  BOOK_DATA[sid].parts.forEach(p => p.chapters.forEach(c => have.add(c.id)));
  EXTRA[sid].forEach(part => {
    const keep = part.chapters.filter(c => !have.has(c.id));
    if(keep.length){ BOOK_DATA[sid].parts.push({ title: part.title, chapters: keep }); added += keep.length; }
  });
});

// ۲) بازنویسی فایل‌های کتاب
function w(name, header, keys){
  let out = header;
  keys.forEach(k => {
    out += '/* ═══════════ ' + k + ' ═══════════ */\nBOOK_DATA.' + k + ' = ' + JSON.stringify(BOOK_DATA[k], null, 1) + ';\n\n';
  });
  fs.writeFileSync(path.join(WEB, name), out, 'utf8');
}
w('book_circuits.js', HDR.circuits, ['circuits']);
w('book_others.js', HDR.others, ['control','instrumentation','biomaterials']);
w('book_last.js', HDR.last, ['biomechanics','imaging']);

// ۳) گزارش
console.log('✓ فصل‌های تکمیلی اضافه‌شده:', added);
function words(o){
  let w = 0;
  const walk = x => { if(typeof x === 'string') w += x.split(/\s+/).filter(Boolean).length; };
  const rec = v => {
    if(Array.isArray(v)) return v.forEach(rec);
    if(v && typeof v === 'object') return Object.keys(v).forEach(k => rec(v[k]));
    walk(v);
  };
  rec(o); return w;
}
let tot = 0;
Object.keys(BOOK_DATA).forEach(k => {
  const bk = BOOK_DATA[k];
  let c=0, b=0, m=0;
  bk.parts.forEach(p => p.chapters.forEach(ch => { c++; b += ch.blocks.length; m += ch.minutes||0; }));
  const W = words(bk); tot += W;
  console.log('  ' + k.padEnd(16), c + ' فصل |', b + ' بلوک |', m + ' دقیقه |', W.toLocaleString('fa-IR') + ' کلمه');
});
console.log('\nجمع کل کلمات کتاب‌ها:', tot.toLocaleString('fa-IR'), '≈', Math.round(tot/250), 'صفحه کتاب چاپی');
