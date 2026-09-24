import asyncio, html
from playwright.async_api import async_playwright
E=html.escape
BASE="""<meta charset="utf-8"><style>
@font-face{font-family:B;src:url(file:///root/.fonts/Bricolage.ttf)}
@font-face{font-family:I;src:url(file:///root/.fonts/Inter.ttf)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;position:relative}
.ft{position:absolute;left:96px;right:96px;bottom:64px;display:flex;justify-content:space-between;font:500 28px I}
</style>"""
# ---------- Carrusel 3: checklist ----------
CK=["Agendé 7 llamadas.","Se presentaron 4.","Vendí 3.","Los 3 pagaron la primera cuota en la llamada."]
CSS3="""<style>body{background:#E9ECEF;color:#101826;font-family:B}
.card{position:absolute;left:72px;right:72px;top:96px;bottom:150px;background:#FBFBF8;border-radius:28px;padding:84px 84px;box-shadow:0 30px 60px -30px rgba(16,24,38,.35)}
.lbl{font:600 30px I;color:#5B6472;margin-bottom:56px;letter-spacing:-.01em}
.it{display:flex;gap:36px;align-items:flex-start;margin-bottom:44px;font-weight:600;font-size:60px;line-height:1.08;letter-spacing:-.02em;font-variation-settings:'wdth' 90}
.bx{flex:none;width:64px;height:64px;border:5px solid #101826;border-radius:12px;margin-top:2px;display:flex;align-items:center;justify-content:center}
.done .bx{background:#F4C95D}.done .bx svg{display:block}.bx svg{display:none}
.done{opacity:.4}.cur{opacity:1}.todo{opacity:.14}
.big{font-weight:700;font-size:92px;line-height:1.04;letter-spacing:-.03em;font-variation-settings:'wdth' 88}
.mid{font-weight:600;font-size:74px;line-height:1.08;letter-spacing:-.02em;font-variation-settings:'wdth' 90}
mark{background:linear-gradient(transparent 55%,#F4C95D 55%);color:inherit;padding:0 4px}
.kw{position:absolute;left:84px;bottom:84px;font-weight:800;font-size:200px;letter-spacing:0;line-height:1;font-variation-settings:'wdth' 75}
.ft{color:#5B6472}</style>"""
TICK='<svg width="40" height="40" viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5" fill="none" stroke="#101826" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def ck_list(k):
    out='<div class="lbl">La semana de un cliente</div>'
    for i,t in enumerate(CK):
        cls='done cur' if i==k else ('done' if i<k else 'todo')
        out+=f'<div class="it {cls}"><div class="bx">{TICK}</div><div>{E(t)}</div></div>'
    return out
def s3(j):
    i=[0,1,6,7,8][j]
    if i==1: inner='<div class="big" style="margin-top:120px">Así se ve una semana cuando <mark>el sistema funciona.</mark></div><div class="it todo" style="position:absolute;bottom:84px;left:84px;right:84px;opacity:.25"><div class="bx"></div><div style="font-size:44px">Deslizá</div></div>'
    elif 2<=i<=5: inner=ck_list(i-2)
    elif i==6: inner='<div class="lbl">El mensaje real</div><img src="file:///home/claude/caps/0638_clean.png" style="display:block;margin:0 auto;max-height:860px;max-width:100%;border-radius:22px">'
    elif i==7: inner='<div class="mid" style="margin-top:60px;font-size:66px">No tenés que ser influencer. No tenés que ser top voice en LinkedIn.</div><div class="mid" style="margin-top:48px;font-size:66px">Son anuncios simples <mark>que te creamos nosotros</mark>, para que vos solo te encargues de vender.</div>'
    else: inner='<div class="mid" style="margin-top:60px">Escribí SIMPLE en los comentarios y te muestro cómo lo armamos.</div><div class="kw">SIMPLE</div>'
    return BASE+CSS3+f'<body><div class="card">{inner}</div><div class="ft"><span>@entrepreguntas_</span><span>{j}/4</span></div></body>'
# ---------- Carrusel 5: tweet ----------
T5=[("Un mensaje que me llegó hace poco 👇","photo"),
("“Te escribo por dos cosas. La primera es que este año facturé promedio 3k por mes.”",""),
("“Te quiero agradecer porque esos primeros pasos fueron muy clave.”",""),
("Otro:\n\n“No puedo creer lo que logré en 1 semana. Gané claridad y sé a dónde ir.”",""),
("La claridad llega antes que las ventas.","big"),
("Si querés que armemos tu sistema juntos, escribí YO en los comentarios y te mando un mensaje para coordinar una llamada.","cta")]
CSS5="""<style>body{background:#101826;font-family:I;color:#0F1419}
.tw{position:absolute;left:64px;right:64px;top:50%;transform:translateY(-52%);background:#fff;border-radius:36px;padding:56px 60px 44px}
.hd{display:flex;align-items:center;gap:24px;margin-bottom:34px}
.av{width:120px;height:120px;border-radius:50%;object-fit:cover}
.nm{font-weight:700;font-size:40px;letter-spacing:-.01em}.hn{font-size:34px;color:#536471;margin-top:2px}
.tx{font-size:66px;line-height:1.24;letter-spacing:-.015em;white-space:pre-line;font-weight:450}
.big .tx{font-size:96px;font-weight:700;line-height:1.12;letter-spacing:-.03em}
.cta .tx{font-size:58px}
.tx b{background:#F4C95D;padding:0 8px;border-radius:6px}
.ph{margin-top:34px;width:100%;height:560px;object-fit:cover;object-position:50% 35%;border-radius:24px;border:1px solid #CFD9DE}
.ac{display:flex;gap:64px;margin-top:36px;padding-top:28px;border-top:1px solid #EFF3F4;color:#536471;font-size:28px}
.ac span{display:flex;align-items:center;gap:12px}
.ft{color:#8B95A5}</style>"""
IC={'c':'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#536471" stroke-width="1.8"><path d="M4 5h16v11H9l-5 4z"/></svg>',
'r':'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#536471" stroke-width="1.8"><path d="M7 4L3 8l4 4M3 8h13a4 4 0 014 4v1M17 20l4-4-4-4M21 16H8a4 4 0 01-4-4v-1"/></svg>',
'l':'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#536471" stroke-width="1.8"><path d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z"/></svg>'}
def s5(i):
    t,k=T5[i-1]
    tx=E(t).replace('YO','<b>YO</b>')
    ph='<img class="ph" src="file:///home/claude/fotos/p3.jpg">' if k=='photo' else ''
    return BASE+CSS5+f'''<body><div class="tw {k}"><div class="hd"><img class="av" src="file:///home/claude/car/avatar.jpg"><div><div class="nm">Agustín | EntrePreguntas</div><div class="hn">@entrepreguntas_</div></div></div>
<div class="tx">{tx}</div>{ph}<div class="ac"><span>{IC['c']}</span><span>{IC['r']}</span><span>{IC['l']}</span></div></div>
<div class="ft"><span>@entrepreguntas_</span><span>{i}/6</span></div></body>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for name,f,n in [('carrusel3_checklist',s3,4)]:
            for i in range(1,n+1):
                open('tmp.html','w',encoding='utf-8').write(f(i))
                await pg.goto('file:///home/claude/car/tmp.html'); await pg.wait_for_timeout(300)
                await pg.screenshot(path=f'{name}_{i}.png')
        await b.close()
asyncio.run(main())
