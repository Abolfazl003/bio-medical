#!/usr/bin/env bash
# راه‌اندازی محیط تست UI (Playwright + کتابخانه‌های سیستم)
set -e
sudo -n apt-get update -qq
sudo -n apt-get install -y -qq libnspr4 libnss3 libasound2t64 libatk1.0-0t64 libatk-bridge2.0-0t64 \
  libcups2t64 libdrm2 libgbm1 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 >/dev/null
pip install -q playwright
python3 -m playwright install chromium-headless-shell
echo "[OK] QA env ready"
