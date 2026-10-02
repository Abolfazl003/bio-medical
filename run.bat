@echo off
chcp 65001 >nul
title BME Konkur Prep App — نسخه وب
color 0B

echo ================================================
echo   اپلیکیشن آمادگی کنکور ارشد مهندسی پزشکی
echo   در حال راه‌اندازی...
echo ================================================
echo.

REM --- رفتن به پوشه اسکریپت ---
cd /d "%~dp0"

REM --- بررسی نصب پایتون ---
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [X] پایتون پیدا نشد!
    echo لطفاً ابتدا پایتون 3.8 یا بالاتر را از python.org نصب کنید
    echo و تیک Add Python to PATH را هنگام نصب بزنید.
    echo.
    pause
    exit /b 1
)

echo [✓] پایتون پیدا شد.

REM --- نصب خودکار پیش‌نیازهای وب (به صورت سبک) ---
echo [*] در حال بررسی پیش‌نیازها...
python -c "import http.server" >nul 2>&1

REM --- رفتن به پوشه وب ---
cd web

REM --- پیدا کردن پورت آزاد (پیش‌فرض 8000) ---
set PORT=8000

echo [✓] در حال راه‌اندازی سرور وب روی پورت %PORT%...
echo.
echo ================================================
echo   سرور در آدرس زیر اجرا می‌شود:
echo   http://localhost:%PORT%
echo ================================================
echo.
echo   پنجره را باز نگه دارید. برای بستن برنامه این پنجره را ببندید.
echo.

REM --- باز کردن خودکار مرورگر پس از ۲ ثانیه ---
start "" cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:%PORT%"

REM --- اجرای سرور وب ---
python -m http.server %PORT% --bind 127.0.0.1
