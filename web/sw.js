/* Service Worker برای کار آفلاین PWA */
const CACHE_NAME = 'bme-konkur-v7';
const ASSETS = [
  './',
  './index.html',
  './style.css',
  './fonts.css',
  './app.js',
  './data.js',
  './books.js',
  './book_math.js',
  './book_circuits.js',
  './book_signals.js',
  './book_anatomy.js',
  './book_physics.js',
  './book_others.js',
  './book_last.js',
  './book_reader.js',
  './teacher_jozve.js',
  './figures.js',
  './figures2.js',
  './figures_fit.js',
  './book_manifest.js',
  './qbook_a.js',
  './qbook_b.js',
  './qbook_c.js',
  './qbook_d.js',
  './qbook_e.js',
  './study_progress.js',
  './konkur_1394_95.js',
  './konkur_1396_97.js',
  './konkur_1398_99.js',
  './konkur_1400_01.js',
  './konkur_1402_03.js',
  './konkur_bank_1394.js',
  './konkur_bank_1395.js',
  './konkur_bank_1396.js',
  './konkur_bank_1397.js',
  './konkur_bank_1398.js',
  './konkur_bank_1399.js',
  './konkur_bank_1400.js',
  './konkur_bank_1401.js',
  './konkur_bank_1402.js',
  './konkur_bank_1403.js',
  './manifest.webmanifest',
  './icon-192.png',
  './icon-512.png',
  './bme-konkur-offline.html',
  './fonts/vazirmatn-arabic.woff2',
  './fonts/vazirmatn-latin.woff2',
  './fonts/vazirmatn-latin-ext.woff2'
];

// نصب: کش کردن همه فایل‌ها
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS).then(() => self.skipWaiting()))
  );
});

// فعال‌سازی: حذف کش قدیمی
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

// استراتژی: Cache First (اگر در کش هست از اونجا بده، در غیر این صورت نتورک رو بگیر و کش کن)
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(resp => {
        if (!resp || resp.status !== 200 || resp.type !== 'basic') return resp;
        const resp2 = resp.clone();
        caches.open(CACHE_NAME).then(c => c.put(e.request, resp2));
        return resp;
      }).catch(() => {
        // آفلاین و در کش نیست، صفحه اصلی بده
        return caches.match('./index.html');
      });
    })
  );
});
