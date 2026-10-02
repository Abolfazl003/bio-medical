@echo off
chcp 65001 >nul
title BME Konkur Prep App — نسخه دسکتاپ
color 0B

echo ================================================
echo   اپلیکیشن دسکتاپ مهندسی پزشکی
echo   در حال راه‌اندازی...
echo ================================================
echo.

cd /d "%~dp0"

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [X] پایتون پیدا نشد! از python.org نصب کنید.
    pause
    exit /b 1
)
echo [✓] پایتون پیدا شد.

echo [*] در حال بررسی/نصب کتابخانه‌های مورد نیاز...
pip install --quiet customtkinter pillow
echo [✓] کتابخانه‌ها آماده‌اند.
echo.
echo [*] در حال اجرای برنامه...
python main.py

if %errorlevel% neq 0 (
    echo.
    echo [!] اجرای دسکتاپ با خطا روبرو شد. در حال اجرای نسخه وب به عنوان جایگزین...
    cd web
    start "" cmd /c "timeout /t 2 >nul && start http://localhost:8000"
    python -m http.server 8000 --bind 127.0.0.1
)
pause
