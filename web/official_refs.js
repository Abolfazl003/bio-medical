/* ═══════════════════════════════════════════════════════════════
   official_refs.js — منابع رسمی اعلام‌شدهٔ آزمون ارشد
   مهندسی پزشکی (بیوالکتریک) — وزارت بهداشت، درمان و آموزش پزشکی

   status:
     "inapp"  → کتاب/منبع در اپ فهرست و خلاصه‌ی محتوایی‌اش موجود است
     "wait"   → هنوز در اپ نیست؛ منتظر فایل PDF از کاربر
   ═══════════════════════════════════════════════════════════════ */
var OFFICIAL_REFS = {

  order: ["math", "physics", "signals", "circuits", "electronics", "control", "anatomy", "english"],

  groups: {

    math: {
      title: "ریاضیات مهندسی", emoji: "📐", subjId: "math", color: "#3b82f6",
      refs: [
        { title: "Advanced Engineering Mathematics", author: "Ervin Kreyszig",
          meta: "ویرایش هشتم — John WILEY & Sons", status: "inapp",
          note: "مرجع اصلی اعلام‌شده؛ فصل‌های معادلات دیفرانسیل، سری و تبدیل فوریه و توابع مختلط مستقیم در کنکور می‌آید.",
          inApp: "در «کتابخانه» اپ فهرست شده — درس‌نامهٔ ریاضیات مهندسی و قفسهٔ کتاب‌های ریاضی اپ بر همین پایه نوشته شده است." }
      ]
    },

    physics: {
      title: "فیزیک پزشکی و مهندسی پزشکی", emoji: "⚡", subjId: "physics", color: "#8b5cf6",
      refs: [
        { title: "فیزیک پزشکی", author: "جان کامرون", meta: "ترجمهٔ فارسی — منبع رسمی سنجش",
          status: "wait", note: "پرکاربردترین مرجع فیزیک پزشکی کنکور ارشد مهندسی پزشکی (پرتوها، تصویربرداری، رادیوبیولوژی)." },
        { title: "فیزیک پزشکی", author: "عباس تکاور", meta: "منبع رسمی سنجش",
          status: "wait", note: "مرجع دانشگاهی فیزیک پزشکی؛ سؤالات پرتو و دوزیمتری از آن طرح می‌شود." },
        { title: "مقدمه‌ای بر مهندسی پزشکی — جلد اول", author: "سید ابوالفضل صانعی، سید محمد فیروزآبادی",
          meta: "منبع رسمی سنجش", status: "wait", note: "پایهٔ مباحث سیستم‌های فیزیولوژیک و مدل‌سازی." },
        { title: "مقدمه‌ای بر مهندسی پزشکی — جلد دوم", author: "سید ابوالفضل صانعی، فرهاد طباطبایی",
          meta: "منبع رسمی سنجش", status: "wait", note: "تجهیزات و کاربردهای مهندسی پزشکی." },
        { title: "Introduction to Biomedical Engineering", author: "J. Enderle, J. Bronzino",
          meta: "ویرایش سوم", status: "wait",
          note: "مرجع بین‌المللی مهندسی پزشکی؛ مباحث بیومکانیک، بیومتریال، ابزار دقیق و تصویربرداری." }
      ]
    },

    signals: {
      title: "سیگنال‌ها و سیستم‌ها", emoji: "📡", subjId: "signals", color: "#10b981",
      refs: [
        { title: "سیگنال‌ها و سیستم‌ها", author: "آلن اوپنهایم، آلن ویلسکی، حمید نواب",
          meta: "مترجم: محمود دیانی — منبع رسمی سنجش", status: "inapp",
          note: "مرجع استاندارد درس: کانوالوشن، فوریه، لاپلاس، تبدیل Z و نمونه‌برداری.",
          inApp: "Oppenheim در «کتابخانه» اپ فهرست شده — قفسهٔ «سیگنال‌ها و سیستم‌ها» بر همین مبناست." }
      ]
    },

    circuits: {
      title: "مدارهای الکتریکی", emoji: "🔌", subjId: "circuits", color: "#f59e0b",
      refs: [
        { title: "نظریه اساسی مدارها و شبکه‌ها (جلد ۱ و ۲)", author: "چارلز دسور",
          meta: "ترجمهٔ دکتر جبه‌دار مارالانی — چاپ بیست و هفتم", status: "inapp",
          note: "مرجع رسمی مدار: تحلیل گره و مش، قضایای شبکه، پاسخ گذرا و ماندگار، تشدید و دوقطبی‌ها.",
          inApp: "«نظریه اساسی مدارها — دسور و کوه» در کتابخانهٔ اپ فهرست شده است." }
      ]
    },

    electronics: {
      title: "الکترونیک", emoji: "🔬", subjId: "circuits", color: "#ef4444",
      refs: [
        { title: "مبانی الکترونیک", author: "سیدعلی میرعشقی", meta: "ویرایش دوم — منبع رسمی سنجش",
          status: "wait", note: "مرجع فارسی اصلی الکترونیک: دیود، BJT، MOSFET و تقویت‌کننده‌ها." },
        { title: "تحلیل و طراحی مدارهای الکترونیک", author: "تقی شفیعی", meta: "ویرایش دوم — منبع رسمی سنجش",
          status: "wait", note: "تحلیل تقویت‌کننده‌ها، پاسخ فرکانسی و بازخورد." }
      ]
    },

    control: {
      title: "کنترل سیستم‌ها", emoji: "🎛", subjId: "control", color: "#06b6d4",
      refs: [
        { title: "Modern Control Systems", author: "R.C. Dorf, R.H. Bishop",
          meta: "ویرایش دوازدهم", status: "inapp",
          note: "مرجع رسمی کنترل: پاسخ زمانی، خطای ماندگار، روت لوکوس، بود، PID و فضای حالت.",
          inApp: "«سیستم‌های کنترل خودکار — دورف و بیشاپ» در کتابخانهٔ اپ فهرست شده است." }
      ]
    },

    anatomy: {
      title: "فیزیولوژی و آناتومی", emoji: "🫀", subjId: "anatomy", color: "#f43f5e",
      refs: [
        { title: "فیزیولوژی پزشکی", author: "آرتور گایتون و جان هال", meta: "منبع رسمی سنجش",
          status: "inapp", note: "مرجع اصلی فیزیولوژی: غشا، قلب، کلیه، تنفس و اعصاب.",
          inApp: "«فیزیولوژی پزشکی گایتون و هال» در کتابخانهٔ اپ فهرست شده است." },
        { title: "آناتومی گری برای دانشجویان", author: "دریک، وگل و میچل", meta: "آخرین ویرایش — منبع رسمی سنجش",
          status: "inapp", note: "آناتومی توصیفی با تصویرگری قوی.",
          inApp: "در کتابخانهٔ اپ فهرست شده است." },
        { title: "نود پلاس فیزیولوژی", author: "منبع توصیه‌شدهٔ سنجش", meta: "کتاب جمع‌بندی فارسی",
          status: "wait", note: "جمع‌بندی فشردهٔ فیزیولوژی برای مرور نهایی." },
        { title: "صفرتاصد فیزیولوژی", author: "منبع توصیه‌شدهٔ سنجش", meta: "کتاب جمع‌بندی فارسی",
          status: "wait", note: "مرور سریع فیزیولوژی با تأکید بر نکات کنکوری." }
      ]
    },

    english: {
      title: "زبان عمومی", emoji: "🔤", subjId: "english", color: "#a855f7",
      refs: [
        { title: "کتاب زبان انگلیسی ۹۰ پلاس", author: "منابع اعلام‌شدهٔ وزارت بهداشت",
          meta: "منبع رسمی زبان عمومی", status: "wait", note: "منبع رسمی اعلام‌شده برای زبان انگلیسی ارشد." },
        { title: "جعبهٔ سیاه زبان ارشد", author: "منابع اعلام‌شدهٔ وزارت بهداشت",
          meta: "منبع رسمی زبان عمومی", status: "wait", note: "واژگان و گرامر پرتکرار آزمون ارشد." }
      ]
    }

  }
};

/* ── توابع کمکی ───────────────────────────────────────────── */
function orGroups(){ return OFFICIAL_REFS.order.map(k=>Object.assign({key:k}, OFFICIAL_REFS.groups[k])); }
function orGroup(key){ return OFFICIAL_REFS.groups[key] || null; }
function orAll(){ return orGroups().reduce((a,g)=>a.concat(g.refs.map(r=>Object.assign({group:g.title, emoji:g.emoji, color:g.color}, r))), []); }
function orCount(){ return orAll().length; }
function orHave(){ return orAll().filter(r=>r.status==="inapp").length; }
function orWait(){ return orAll().filter(r=>r.status!=="inapp"); }
function orForSubject(sid){
  return orGroups().filter(g=>g.subjId===sid).map(g=>({group:g.title, emoji:g.emoji, color:g.color, refs:g.refs}));
}
