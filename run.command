#!/bin/bash
# اسکریپت راه‌انداز برای macOS و لینوکس
cd "$(dirname "$0")"
echo "اپلیکیشن آمادگی کنکور مهندسی پزشکی"
echo "در حال راه‌اندازی سرور وب..."

PORT=8000
cd web

# باز کردن مرورگر پس از یک ثانیه
(sleep 1 && (open "http://localhost:$PORT" 2>/dev/null || xdg-open "http://localhost:$PORT" 2>/dev/null)) &

echo "سرور در http://localhost:$PORT در حال اجراست."
echo "برای توقف Ctrl+C بزنید."
python3 -m http.server $PORT --bind 127.0.0.1
