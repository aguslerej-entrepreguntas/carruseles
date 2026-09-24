import asyncio, html
from playwright.async_api import async_playwright
S=[("Un mensaje que me llegó hace poco 👇",'/home/claude/caps/9343_clean.png'),
("Otro 👇",'/home/claude/caps/9349_clean.png'),
("La claridad llega antes que las ventas.",None),
("No tenés que ser influencer ni top voice en LinkedIn.\n\nSon anuncios simples que te creamos nosotros, para que vos solo te encargues de vender.",None),
("¿Querés saber si esto se puede aplicar a tu consultoría? Escribí YO en los comentarios y te hablamos por privado para coordinar una llamada con el equipo.",None)]
BADGE='<svg width="44" height="44" viewBox="0 0 24 24"><path fill="#1D9BF0" d="M22.25 12c0-1.43-.88-2.67-2.19-3.34.46-1.39.2-2.9-.81-3.91s-2.52-1.27-3.91-.81c-.66-1.31-1.91-2.19-3.34-2.19s-2.67.88-3.33 2.19c-1.4-.46-2.91-.2-3.92.81s-1.26 2.52-.8 3.91C2.63 9.33 1.75 10.57 1.75 12s.88 2.67 2.2 3.34c-.46 1.39-.21 2.9.8 3.91s2.52 1.26 3.91.81c.67 1.31 1.91 2.19 3.34 2.19s2.68-.88 3.34-2.19c1.39.45 2.9.2 3.91-.81s1.27-2.52.81-3.91c1.31-.67 2.19-1.91 2.19-3.34z"/><path fill="#fff" d="M10.54 16.2l-3.6-3.6 1.4-1.42 2.2 2.2 5.12-5.12 1.41 1.42z"/></svg>'
CSS="""<meta charset="utf-8"><style>
@font-face{font-family:I;src:url(file:///root/.fonts/Inter.ttf)}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;background:#15202B;color:#F7F9F9;font-family:I;display:flex;flex-direction:column;justify-content:center;padding:0 90px}
.hd{display:flex;align-items:center;gap:30px;position:relative}
.av{width:150px;height:150px;border-radius:50%;object-fit:cover}
.nm{font-weight:700;font-size:44px;display:flex;align-items:center;gap:12px}
.hn{font-size:38px;color:#8B98A5;margin-top:4px}
.dots{position:absolute;right:0;top:20px;font-size:44px;color:#8B98A5;letter-spacing:4px}
.tx{margin-top:90px;font-size:70px;line-height:1.3;letter-spacing:-.02em;font-weight:400}
.sm{font-size:62px;white-space:pre-line}
.img{margin-top:70px;width:100%;border-radius:28px;border:2px solid #38444D;display:block}
.tx+.img{margin-top:50px}
</style>"""
def page(t,img):
    tx=html.escape(t)
    cls='tx sm' if len(t)>60 else 'tx'
    body=f'<div class="hd"><img class="av" src="file:///home/claude/car/avatar3.jpg"><div><div class="nm">Agustin Lerej {BADGE}</div><div class="hn">@agustinlerej</div></div><div class="dots">···</div></div>'
    if t: body+=f'<div class="{cls}">{tx}</div>'
    if img: body+=f'<img class="img" src="file://{img}">'
    return CSS+f'<body>{body}</body>'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,(t,img) in enumerate(S,1):
            open('tmp.html','w',encoding='utf-8').write(page(t,img))
            await pg.goto('file:///home/claude/car/tmp.html'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'carrusel5_tweet_v2_{i}.png')
        await b.close()
asyncio.run(main())
