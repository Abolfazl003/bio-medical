/* Service Worker برای کار آفلاین PWA */
const CACHE_NAME = 'bme-konkur-v3';
const ASSETS = [
  './',
  './index.html',
  './style.css',
  './fonts.css',
  './app.js',
  './data.js',
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
