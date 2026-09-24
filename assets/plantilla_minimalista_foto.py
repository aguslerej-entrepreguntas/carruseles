import re, html, asyncio
from playwright.async_api import async_playwright
F='/home/claude/fotos/'
C2=[("¿Y si contrato a alguien que me maneje las redes?","p1","hook"),
("Es lo primero que piensan muchos consultores cuando no les llegan clientes.",None,""),
("Community manager, una web perfecta, publicar todos los días…",None,""),
("Sin un mensaje claro, ES PLATA Y TIEMPO TIRADOS.","p3",""),
("Primero, una propuesta que se entienda. Después, un anuncio simple para validarla en pocos días.",None,""),
("Sin ser influencer. Sin publicar todos los días. Y los anuncios te los generamos nosotros.","p6",""),
("Si querés que armemos tu sistema juntos, comenta YO en este posteo.",None,"cta")]
C5=[("Cobré un proyecto y terminé dando mil reuniones.","p5","hook"),
("Pasa cuando cada cliente recibe una propuesta distinta.",None,""),
("Las horas se estiran, el precio no. TU HORA SE LICÚA.","p0",""),
("Y con 2 o 3 clientes, ya no te da la semana.",None,""),
("Tu cliente no compra tu tiempo. COMPRA UN MÉTODO.",None,""),
("Tres pilares, dos o tres renglones cada uno. Mismo camino, distinto cliente.","p2",""),
("Si querés ver cómo lo armamos, escribime SIMPLE en comentarios.",None,"cta")]
POS={'p1':'60% 30%','p3':'50% 40%','p6':'55% 50%','p5':'55% 55%','p0':'40% 40%','p2':'50% 55%'}
def fmt(t):
    t=html.escape(t)
    return re.sub(r"(\b[A-ZÁÉÍÓÚÑ]{2,}(?:\s+[A-ZÁÉÍÓÚÑ]+\b)*\.?)",lambda m:f'<em>{m.group(1)}</em>',t)
CSS="""@font-face{font-family:B;src:url(file:///root/.fonts/Bricolage.ttf)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;background:#101826;font-family:B;color:#F2EEE6;overflow:hidden;position:relative}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,24,38,.92) 0%,rgba(16,24,38,.55) 38%,rgba(16,24,38,0) 62%,rgba(16,24,38,.35) 100%)}
.t{position:absolute;left:96px;right:96px;font-weight:600;font-variation-settings:'wdth' 88,'opsz' 72;letter-spacing:-.02em;line-height:1.06}
.dark .t{top:50%;transform:translateY(-50%);font-size:84px}
.photo .t{top:120px;font-size:80px;text-shadow:0 2px 24px rgba(0,0,0,.35)}
.hook .t{font-size:98px;font-weight:700}
em{font-style:normal;color:#F4C95D;font-weight:800}
.cta .t{font-size:78px}
.cta .kw{position:absolute;left:96px;bottom:230px;font-size:260px;font-weight:800;color:#F4C95D;letter-spacing:.01em;line-height:1;font-variation-settings:'wdth' 75,'opsz' 96}
.ft{position:absolute;left:96px;right:96px;bottom:72px;display:flex;justify-content:space-between;font-size:28px;font-weight:500;opacity:.75}
.bar{position:absolute;left:96px;bottom:130px;height:4px;background:#F4C95D;border-radius:2px}
"""
def page(t,photo,kind,i,n):
    cls=('photo' if photo else 'dark')+(' '+kind if kind else '')
    body=''
    if photo: body+=f'<img class="bg" src="file://{F}{photo}.jpg" style="object-position:{POS[photo]}"><div class="sh"></div>'
    txt=fmt(t)
    if kind=='cta':
        kw=re.search(r"\b(YO|SIMPLE)\b",t).group(1)
        body+=f'<div class="t" style="top:170px;transform:none">{txt}</div><div class="kw">{kw}</div>'
    else: body+=f'<div class="t">{txt}</div>'
    if not photo: body+=f'<div class="bar" style="width:{(i/n)*888:.0f}px"></div>'
    body+=f'<div class="ft"><span>@entrepreguntas_</span><span>{i}/{n}</span></div>'
    return f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}">{body}</body></html>'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for name,C in [('carrusel2_redes',C2),('carrusel5_reuniones',C5)]:
            for i,(t,ph,k) in enumerate(C,1):
                open('tmp.html','w',encoding='utf-8').write(page(t,ph,k,i,len(C)))
                await pg.goto('file:///home/claude/car/tmp.html'); await pg.wait_for_timeout(300)
                await pg.screenshot(path=f'{name}_{i}.png')
        await b.close()
asyncio.run(main())
