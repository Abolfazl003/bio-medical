# -*- coding: utf-8 -*-
"""دانلود و جاسازی فونت وزیرمتن (variable) به صورت base64 در CSS - بدون تکرار"""
import re, base64, urllib.request, os

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

with open('vazir.css', encoding='utf-8') as f:
    css = f.read()

blocks = re.findall(r'/\*\s*([a-z\-]+)\s*\*/\s*@font-face\s*\{(.*?)\}', css, re.S)

# چون فونت variable هست، هر subset فقط یک فایل یکتا داره => dedupe بر اساس URL
seen = {}   # subset -> (url, unicode-range)
for subset, body in blocks:
    url = re.search(r'url\((https://[^)]+)\)', body).group(1)
    urange = re.search(r'unicode-range:\s*([^;]+);', body).group(1).strip()
    if subset not in seen:
        seen[subset] = (url, urange)

out_css = []
total = 0
for subset, (url, urange) in seen.items():
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    data = urllib.request.urlopen(req, timeout=60).read()
    total += len(data)
    print(f'  {subset}: {len(data)/1024:.1f} KB  (weight range 100-900, variable)')
    b64 = base64.b64encode(data).decode()
    out_css.append(f"""@font-face {{
  font-family: 'Vazirmatn';
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
  src: url(data:font/woff2;base64,{b64}) format('woff2');
  unicode-range: {urange};
}}""")

header = "/* Vazirmatn variable font - embedded for full offline use */\n"
with open('vazirmatn-embedded.css', 'w', encoding='utf-8') as f:
    f.write(header + '\n'.join(out_css))

print(f'\nTotal raw font bytes: {total/1024:.1f} KB')
print('Embedded CSS size: %.1f KB' % (os.path.getsize('vazirmatn-embedded.css')/1024))
