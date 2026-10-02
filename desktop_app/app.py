# -*- coding: utf-8 -*-
"""
اپلیکیشن دسکتاپ کنکور ارشد مهندسی پزشکی
- کاملاً آفلاین: محتوا از فایل تک‌صفحه‌ای همراه برنامه خوانده می‌شود
- بدون سرور و پورت: فایل مستقیماً در موتور مرورگر بومی سیستم بارگذاری می‌شود
- همه کتابخانه‌ها از قبل داخل فایل اجرایی هستند
"""
import os
import sys
import json
import webview

APP_TITLE = "کنکور ارشد مهندسی پزشکی 🩺"


def resource_path(rel):
    """مسیر فایل‌های همراه (چه در حالت اجرا، چه در حالت بسته‌بندی‌شده با PyInstaller)"""
    if getattr(sys, 'frozen', False):
        base = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, rel)


class Api:
    """پل بین رابط کاربری و سیستم‌عامل"""

    def save_backup(self, content):
        """ذخیره فایل پشتیبان پیشرفت کاربر"""
        try:
            window = webview.windows[0]
            result = window.create_file_dialog(
                webview.SAVE_DIALOG,
                save_filename='bme_progress_backup.json',
                file_types=('JSON (*.json)', 'All files (*.*)')
            )
            if not result:
                return 'ذخیره لغو شد'
            path = result if isinstance(result, str) else result[0]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            return 'پشتیبان ذخیره شد: %s' % os.path.basename(path)
        except Exception as e:
            return 'خطا: %s' % e

    def load_backup(self):
        """خواندن فایل پشتیبان و بازگرداندن محتوای آن"""
        try:
            window = webview.windows[0]
            result = window.create_file_dialog(
                webview.OPEN_DIALOG,
                allow_multiple=False,
                file_types=('JSON (*.json)', 'All files (*.*)')
            )
            if not result:
                return None
            path = result[0] if isinstance(result, (list, tuple)) else result
            with open(path, encoding='utf-8') as f:
                return f.read()
        except Exception:
            return None

    def platform(self):
        return {'win': 'windows', 'darwin': 'macos', 'linux': 'linux'}.get(sys.platform, sys.platform)

    def app_version(self):
        return '1.2.0'

    def quit(self):
        for w in webview.windows:
            w.destroy()


def main():
    index = resource_path(os.path.join('web', 'index.html'))
    if not os.path.exists(index):
        index = resource_path('index.html')

    webview.create_window(
        APP_TITLE,
        index,
        js_api=Api(),
        width=1280,
        height=820,
        min_size=(360, 520),
        background_color='#0F172A',
        text_select=True,
        confirm_close=False,
    )
    webview.start(debug=False)


if __name__ == '__main__':
    main()
