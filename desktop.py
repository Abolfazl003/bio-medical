# -*- coding: utf-8 -*-
"""اپلیکیشن دسکتاپ استندالون مهندسی پزشکی - بدون نیاز به سرور"""
import os, sys, webview
import threading

def get_html_path():
    # اگر به صورت exe بیلد شده باشه فایل از همان پوشه exe خوانده میشه
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    else:
        base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web')
    return os.path.join(base, 'bme-konkur-offline.html')

def main():
    html_path = get_html_path()
    print('Loading:', html_path)
    window = webview.create_window(
        'آمادگی کنکور ارشد مهندسی پزشکی 🩺📚',
        html_path,
        width=1280, height=800,
        min_size=(900,600),
        text_select=True,
        confirm_close=True
    )
    webview.start(debug=False, http_server=True)

if __name__ == "__main__":
    main()
