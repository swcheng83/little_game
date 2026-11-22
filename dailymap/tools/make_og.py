"""Builds the link-preview cards for the 12 city rumors in dailymap/index.html.

Writes og/<id>.png (1200x630) and r/<id>.html (a tiny page that carries the
preview tags and sends people on to the game with that rumor in focus).
Run from the repo root: python3 dailymap/tools/make_og.py
"""
import html, os, re, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
BASE = 'https://swcheng83.github.io/little_game/dailymap/'
FONT = sys.argv[1] if len(sys.argv) > 1 else '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
INK, INK3, TRAIL, RIVAL, PAPER = '#1b2433', '#7c8796', '#0f9d8f', '#8a6300', '#e9eef0'

src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
seeds = re.findall(r"\{ id: '(s\d\d)'.*?h: '([^']*)'", src)
assert len(seeds) == 12, len(seeds)

def f(size):
    return ImageFont.truetype(FONT, size)

def wrap(draw, text, font, width):
    lines, line = [], ''
    for ch in text:
        if draw.textlength(line + ch, font=font) > width and line:
            lines.append(line); line = ch
        else:
            line += ch
    return lines + ([line] if line else [])

def card(kicker, text, out):
    W, H = 1200, 630
    im = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((32, 32, W - 32, H - 32), 36, fill='white')
    d.text((80, 70), '日常開圖', font=f(48), fill=INK)
    d.text((80, 150), kicker, font=f(32), fill=RIVAL)
    body = f(52)
    y = 220
    for line in wrap(d, '「' + text + '」', body, 760)[:4]:
        d.text((80, y), line, font=body, fill=INK); y += 72
    d.ellipse((900, 190, 1100, 390), outline=TRAIL, width=9)
    q = f(120); tw = d.textlength('？', font=q)
    d.text((1000 - tw / 2, 220), '？', font=q, fill=TRAIL)
    d.text((80, 525), '你找得到嗎？到了才知道是哪裡', font=f(30), fill=INK3)
    im.save(out, optimize=True)

os.makedirs(os.path.join(ROOT, 'og'), exist_ok=True)
os.makedirs(os.path.join(ROOT, 'r'), exist_ok=True)
card('附近有一則傳聞在等你', '跟著冷熱羅盤走，到了自動揭曉', os.path.join(ROOT, 'og', 'default.png'))
for sid, h in seeds:
    card('有人今天找到了這則城市傳聞', h, os.path.join(ROOT, 'og', sid + '.png'))
    t = html.escape('日常開圖：「' + h + '」', quote=True)
    page = f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta property="og:type" content="website">
<meta property="og:title" content="{t}">
<meta property="og:description" content="有人今天找到了這則城市傳聞。跟著冷熱羅盤走，到了才知道是哪裡。">
<meta property="og:image" content="{BASE}og/{sid}.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="{BASE}r/{sid}.html">
<meta name="twitter:card" content="summary_large_image">
<meta http-equiv="refresh" content="0;url=../#s={sid}">
</head><body><p><a href="../#s={sid}">打開日常開圖</a></p>
<script>location.replace('../#s={sid}');</script></body></html>
'''
    open(os.path.join(ROOT, 'r', sid + '.html'), 'w', encoding='utf-8').write(page)
print('made', len(seeds) + 1, 'cards')
