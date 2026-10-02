/* add_figs.js — جای‌گذاری شکل‌های تصویری (SVG) در فصل‌های کتاب‌ها
   اجرا:  cd /home/user/bme_konkur && node content/add_figs.js            */
const fs = require("fs"), path = require("path");
const WEB = path.join(__dirname, "..", "web");

const FILES = {
  "book_anatomy.js": ["anatomy"],
  "book_circuits.js": ["circuits"],
  "book_last.js": ["biomechanics", "imaging"],
  "book_math.js": ["math"],
  "book_others.js": ["biomaterials", "control", "instrumentation"],
  "book_physics.js": ["physics"],
  "book_signals.js": ["signals"],
};
const BOOK_DATA = {};
Object.keys(FILES).forEach(f => { eval(fs.readFileSync(path.join(WEB, f), "utf8")); });

/* [chapterId, لنگر (سرتیتر یا متن), شناسه شکل, عنوان شکل] */
const PLAN = [
  // ── مدارهای الکتریکی ۱ ──
  ["circ-c1", "قانون اهم", "circ-series", "مدار سری: جریان مشترک و جمع مقاومت‌ها"],
  ["circ-c1", "کیرشهف برای جریان", "circ-kcl", "قانون جریان کیرشهف در یک گره"],
  ["circ-c1", "کیرشهف برای ولتاژ", "circ-mesh", "دو حلقه و جریان‌های مش"],
  ["circ-c1", "ترکیب مقاومت‌ها", "circ-parallel", "مقاومت موازی و مقاومت معادل"],
  ["circ-c1", "ترکیب مقاومت‌ها", "circ-divider", "مدار تقسیم ولتاژ"],
  // ── مدارهای الکتریکی ۲ ──
  ["circ-c2", "تحلیل مش", "circ-mesh", "تحلیل مش: یک جریان فرضی برای هر حلقه"],
  ["circ-c2", "قضیه تونن", "circ-thevenin", "شبکه خطی و معادل تونن آن"],
  // ── پاسخ گذرا و سینوسی ──
  ["circ-c3", "RC با منبع ثابت", "circ-rc", "شارژ خازن و ثابت زمانی RC"],
  ["circ-c3", "مدار مرتبه دوم RLC", "circ-rlc", "مدار RLC سری و رزونانس"],
  ["circ-c4", "امپدانس معادل و رزونانس", "circ-rlc", "رزونانس: امپدانس معادل برابر R"],
  ["circ-c4", "پاسخ فرکانسی و دیاگرام بود", "circ-lpf", "فیلتر پایین‌گذر RC و پاسخ فرکانسی"],
  // ── الکترونیک ۱ و ۲ ──
  ["elec-c1", "دیود و پیوند PN", "circ-diode", "مشخصه جریان-ولتاژ دیود و بایاس"],
  ["elec-c1", "یک‌سوسازی", "circ-rectifier", "یک‌سوساز نیم‌موج و پل تمام‌موج"],
  ["elec-c2", "ترانزیستور BJT", "circ-bjt", "تقویت‌کننده امیتر مشترک با بایاس"],
  ["elec-c2", "مدارهای پایه", "circ-opamp-inv", "تقویت‌کننده معکوس با آپ‌امپ"],
  ["elec-c2", "مدارهای پایه", "circ-opamp-noninv", "تقویت‌کننده غیرمعکوس با آپ‌امپ"],
  ["elec-c2", "تقویت‌کننده ابزار دقیق", "circ-instr-amp", "تقویت‌کننده ابزار دقیق سه‌اپ‌امپی"],
  // ── سیگنال‌ها ──
  ["sig-c1", "انرژی و توان سیگنال", "plot-fourier", "طیف فوریه و مجموع جزئی موج مربعی"],
  ["sig-c1", "سیستم‌های LTI و پاسخ ضربه", "plot-step-2nd", "پاسخ پله سیستم مرتبه دوم در میرایی‌های مختلف"],
  ["sig-c2", "سری فوریه", "plot-fourier", "هارمونیک‌های فرد و مجموع جزئی سری فوریه"],
  ["sig-c2", "نمونه‌برداری و قضیه نایکوئیست", "blk-biosignal", "زنجیره نمونه‌برداری سیگنال زیستی"],
  ["sig-c2", "فیلتر ایده‌آل و sinc", "circ-lpf", "فیلتر پایین‌گذر واقعی و فرکانس قطع"],
  ["sig-c3", "پایداری و موقعیت قطب‌ها", "plot-rootlocus", "حرکت قطب‌ها با تغییر بهره (روت لوکوس)"],
  ["sig-c5", "زنجیره استاندارد پردازش ECG", "plot-ecg", "اجزای موج ECG و فاصله RR"],
  // ── کنترل ──
  ["ctrl-c1", "اجزای یک سیستم کنترل", "blk-feedback", "ساختار حلقه بسته کنترل"],
  ["ctrl-c1", "مشخصات پاسخ پله", "plot-step-2nd", "فراجهش، زمان صعود و زمان نشست"],
  ["ctrl-c2", "روت لوکوس (Root Locus)", "plot-rootlocus", "روت لوکوس و بهره مرزی پایداری"],
  ["ctrl-c2", "حاشیه بهره و حاشیه فاز", "plot-bode", "حاشیه بهره و حاشیه فاز در دیاگرام بود"],
  ["ctrl-c3", "پاسخ سیستم مرتبه دوم", "plot-step-2nd", "پاسخ پله و اثر میرایی"],
  ["ctrl-c3", "دیاگرام بود", "plot-bode", "منحنی بزرگی و فاز و شرط حاشیه‌ها"],
  ["ctrl-c5", "معیار نیکوئیست", "plot-bode", "پایداری نسبی از دید فرکانسی"],
  ["ctrl-c7", "جمله‌های PID و پیاده‌سازی عملی", "blk-pid", "بلوک‌دیاگرام کنترل‌کننده PID"],
  // ── ابزار دقیق ──
  ["inst-c1", "پل وتستون", "circ-wheatstone", "پل وتستون و شرط تعادل"],
  ["inst-c1", "الکترودهای زیستی", "inst-electrode", "رابط الکترود-پوست و پتانسیل نیم‌سل"],
  ["inst-c3", "تقویت‌کننده ابزار دقیق", "circ-instr-amp", "تقویت‌کننده ابزار دقیق و CMRR"],
  ["inst-c3", "منابع نویز و راهکارها", "blk-biosignal", "زنجیره ثبت و نقاط تزریق نویز"],
  ["inst-c5", "طبقه‌بندی فیلترهای زیستی", "circ-lpf", "فیلتر پایین‌گذر و انتخاب فرکانس قطع"],
  ["inst-c6", "نوار قلب: از سیگنال تا اشتقاق", "inst-ecg-leads", "مثلث آینتهوون و لیدهای ECG"],
  ["inst-c6", "مانیتورینگ سیگنال‌های حیاتی", "plot-ppg", "سیگنال PPG و مؤلفه‌های AC و DC"],
  ["inst-c7", "سنسورهای پوشیدنی", "plot-ppg", "PPG: مبنای پالس‌اکسیمتری و پوشیدنی‌ها"],
  // ── تصویربرداری ──
  ["img-c1", "تولید پرتو ایکس", "img-xray", "لامپ پرتو ایکس: کاتد، آند و پرتو خروجی"],
  ["img-c1", "سی‌تی اسکن", "img-ct", "هندسه چرخشی CT و بازسازی مقطعی"],
  ["img-c1", "پزشکی هسته‌ای", "img-pet", "ثبت هم‌زمان دو فوتون ۵۱۱keV در PET"],
  ["img-c2", "MRI — فیزیک پایه", "img-mri-seq", "توالی پالس MRI و تنظیم TR و TE"],
  ["img-c2", "اولتراسوند — فیزیک و اصول", "img-us", "پروب اولتراسوند و بازتاب موج"],
  ["img-c4", "فیزیک MRI", "plot-t1t2", "بازیافت T1 و افت T2 در MRI"],
  ["img-c5", "تشدید مغناطیسی", "plot-t1t2", "منحنی T1 و T2 و کنتراست بافتی"],
  ["img-c5", "پزشکی هسته‌ای", "img-pet", "ناپدیده‌سازی و خط هم‌زمانی"],
  ["img-c5", "اولتراسوند", "img-us", "بازتاب در مرز امپدانس و A-mode"],
  ["img-c7", "تصویربرداری مولکولی", "img-pet", "تصویربرداری مولکولی با PET"],
  ["img-c7", "هوش مصنوعی در تصویربرداری", "img-ct", "تصویر مقطعی ورودی الگوریتم‌های تحلیل"],
  // ── آناتومی ──
  ["ana-c1", "مدل مدار معادل غشا", "circ-rc", "غشای سلول مانند مدار RC عمل می‌کند"],
  ["ana-c2", "مراحل پتانسیل عمل", "plot-action-pot", "فازهای پتانسیل عمل سلول قلبی"],
  ["ana-c2", "هدایت پتانسیل عمل در آکسون", "plot-conduction", "سرعت هدایت در فیبر میلین‌دار و بدون میلین"],
  ["ana-c2", "نورون: ساختار و انواع", "anat-neuron", "ساختار نورون، غلاف میلین و سیناپس"],
  ["ana-c3", "آناتومی قلب", "anat-heart", "چهار حفره قلب و مسیر خون"],
  ["ana-c3", "سیستم هدایت الکتریکی قلب", "anat-conduction", "گره SA، گره AV و رشته‌های پورکینژ"],
  ["ana-c3", "امواج ECG", "plot-ecg", "موج P، کمپلکس QRS و موج T"],
  ["ana-c3", "چرخه قلبی", "plot-pv-loop", "حلقه فشار-حجم بطن چپ"],
  ["ana-c3", "سیستم گردش خون و همودینامیک", "anat-vessel", "دیواره رگ و پروفایل سرعت پوازی"],
  ["ana-c4", "تنفس", "anat-alveolus", "تبادل گاز در آلوئول و مویرگ"],
  ["ana-c4", "تنفس", "plot-oxygen", "منحنی تفکیک اکسی‌هموگلوبین و جابه‌جایی آن"],
  ["biom-c2", "غضروف", "anat-sarcomere", "سارکومر و مدل لغزشی انقباض عضله"],
  ["ana-c4", "کلیه", "anat-nephron", "نفرون: صافش، بازجذب و ترشح"],
  ["ana-c5", "نورون، سیناپس و انتقال پیام", "plot-conduction", "ترتیب فراخوانش فیبرهای عصبی"],
  ["ana-c5", "شنوایی و کاشت حلزون", "anat-ear", "گوش، استخوانچه‌ها و نقشه تنوتوپیک حلزون"],
  ["ana-c5", "بینایی", "anat-eye", "ساختار چشم و شبکیه"],
  // ── ریاضی و فیزیک ──
  ["math-c5", "توزیع‌های مهم", "plot-gaussian", "توزیع نرمال و بازه‌های اطمینان"],
  ["math-c6", "سری فوریه", "plot-fourier", "طیف موج مربعی و پدیده گیبس"],
  ["phy-c5", "سه برهم‌کنش اصلی", "img-xray", "تولید و عبور پرتو ایکس از بافت"],
  ["phy-c5", "دوز و رادیوبیولوژی", "plot-action-pot", "پاسخ سلولی؛ مبنای منحنی بقا"],
];

/* حذف شکل‌های متنی قدیمی و جای‌گذاری شکل‌های تصویری */
let inserted = 0, replaced = 0, missing = [];

const flat = [];
Object.keys(BOOK_DATA).forEach(sid => BOOK_DATA[sid].parts.forEach(p => p.chapters.forEach(c => flat.push({ sid, ch: c }))));

/* همه شکل‌های قبلی پاک می‌شوند تا اجرای دوباره شکل تکراری نسازد */
flat.forEach(({ ch }) => { ch.blocks = ch.blocks.filter(b => b.t !== "fig"); });

PLAN.forEach(([chId, anchor, figId, cap]) => {
  const item = flat.find(x => x.ch.id === chId);
  if (!item) { missing.push("فصل " + chId); return; }
  const bl = item.ch.blocks;
  const at = bl.findIndex(b => typeof b.x === "string" && b.x.indexOf(anchor) >= 0);
  const block = { t: "fig", fig: figId, cap: cap };
  if (at < 0) { missing.push(chId + " → لنگر «" + anchor + "»"); bl.push(block); inserted++; return; }
  bl.splice(at + 1, 0, block); inserted++;
});

/* بازنویسی فایل‌ها */
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
  FILES[f].forEach(sid => { out += "BOOK_DATA." + sid + " = " + JSON.stringify(BOOK_DATA[sid], null, 1) + ";\n"; });
  fs.writeFileSync(path.join(WEB, f), out, "utf8");
});

console.log("شکل‌های جای‌گذاری‌شده:", inserted, "| شکل‌های متنی حذف‌شده:", replaced);
if (missing.length) { console.log("⚠️ مواردی که لنگر پیدا نشد:"); missing.forEach(m => console.log("   -", m)); }
else console.log("✅ همه لنگرها پیدا شد");
