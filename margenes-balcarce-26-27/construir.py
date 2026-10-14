"""Arma index.html (un solo archivo, funciona sin internet) a partir de fuente/deck.json y fuente/slides/*.html.
Uso: python construir.py   (desde esta carpeta)"""
import json, re, html, sys, os, base64
AQUI=os.path.dirname(os.path.abspath(__file__))
D=os.path.join(AQUI,'fuente')+os.sep
OUT=os.path.join(AQUI,'index.html')
def uri(f): return 'data:image/svg+xml;base64,'+base64.b64encode(open(os.path.join(AQUI,f),'rb').read()).decode()
LOGOURI=uri('6gagro-logo-fondo-crema.svg')
QRURI=uri('whatsapp-qr.svg')
deck=json.load(open(D+'deck.json',encoding='utf-8'))
slides=[]
order=list(deck['order'])
for sid in order:
    s=open(D+f'slides/{sid}.html',encoding='utf-8').read().strip()
    # custom shapes -> divs
    s=re.sub(r'<x-shape kind="ellipse" style="([^"]*)"></x-shape>', r'<div style="\1;border-radius:50%"></div>', s)
    # simulator links -> internal
    s=re.sub(r'<a href="https://claude\.ai/artifact/KhqrfpCrwxztGgb8gfnTsL">', '<a href="#simulador" class="to-sim">', s)
    s=s.replace('/_blob/f6bd1d58341dd9e8a1a558b4880f8941',LOGOURI).replace('/_blob/1c2366ff4ed826ea2f535dc864c1601a',QRURI)
    m=re.search(r'<x-embed style="[^"]*">(.*?)</x-embed>', s, re.S)
    if m:
        doc='<!doctype html><html lang="es"><head><meta charset="utf-8"></head><body>'+m.group(1)+'</body></html>'
        s=s[:m.start()]+'<iframe title="animación" srcdoc="'+html.escape(doc,quote=True)+'"></iframe>'+s[m.end():]
        s=s.replace('<section ','<section class="slide sim anim" ',1)
    else:
        s=s.replace('<section ','<section class="slide" ',1)
    slides.append(s)
title=html.escape(deck['title'])
page=f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400..800&family=DM+Sans:wght@400..700&display=swap">
<style>
html,body{{margin:0;height:100%;background:#111;overflow:hidden}}
#stage{{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform-origin:center center}}
.slide{{position:absolute;inset:0;width:1920px;height:1080px;box-sizing:border-box;overflow:hidden}}
.slide:not(.on){{display:none!important}}
.slide *{{box-sizing:border-box;margin:0}}
.slide h1{{font-size:96px;font-weight:600;line-height:1.1}}
.slide h2{{font-size:64px;font-weight:600;line-height:1.15}}
.slide h3{{font-size:44px;font-weight:600;line-height:1.2}}
.slide p{{font-size:32px;line-height:1.4}}
.slide table{{border-collapse:collapse}}
.slide td,.slide th{{padding:.35em .6em;border-bottom:1px solid rgba(28,43,36,.18)}}
.slide th{{font-weight:700}}
.slide a{{color:inherit;text-decoration:none}}
.slide aside{{display:none}}
.slide.sim iframe{{position:absolute;inset:0;width:100%;height:100%;border:0;background:#F5F1E6}}
.slide.sim img{{z-index:2}}
#notes{{position:fixed;left:0;right:0;bottom:0;max-height:30vh;overflow:auto;background:rgba(17,17,17,.92);color:#eee;font:18px/1.45 Arial,sans-serif;padding:14px 20px;display:none}}
#hud{{position:fixed;right:14px;bottom:10px;color:#999;font:13px Arial,sans-serif;opacity:.7}}
</style></head>
<body>
<div id="stage">
{chr(10).join(slides)}
</div>
<div id="notes"></div>
<div id="hud"></div>
<script>
const S=[...document.querySelectorAll('.slide')];let i=0;
const stage=document.getElementById('stage'),notes=document.getElementById('notes'),hud=document.getElementById('hud');
function fit(){{const k=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform=`translate(-50%,-50%) scale(${{k}})`;}}
function show(n){{i=Math.max(0,Math.min(S.length-1,n));S.forEach((s,j)=>s.classList.toggle('on',j===i));
 const a=S[i].querySelector('aside');notes.textContent=a?a.textContent:'';hud.textContent=(i+1)+' / '+S.length+'   ← → pasar · F pantalla completa · N notas';
 try{{history.replaceState(null,'','#'+(i+1))}}catch(e){{}}
 if(S[i].classList.contains('anim')){{try{{S[i].querySelector('iframe').contentWindow.replay()}}catch(e){{}}}}}}
addEventListener('keydown',e=>{{if(e.target.tagName==='INPUT')return;
 if(['ArrowRight','PageDown',' ','Enter'].includes(e.key)){{e.preventDefault();show(i+1)}}
 else if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){{e.preventDefault();show(i-1)}}
 else if(e.key==='Home')show(0);else if(e.key==='End')show(S.length-1);
 else if(e.key==='f'||e.key==='F'){{document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen().catch(()=>{{}})}}
 else if(e.key==='n'||e.key==='N'){{notes.style.display=notes.style.display==='block'?'none':'block'}}}});
document.addEventListener('click',e=>{{const a=e.target.closest('a.to-sim');if(a){{e.preventDefault();show(S.findIndex(s=>s.id==='simulador'));return;}}
 if(S[i].classList.contains('sim')&&!S[i].classList.contains('anim'))return; if(e.clientX>innerWidth/3)show(i+1);else show(i-1);}});
document.querySelectorAll('.sim iframe').forEach(fr=>fr.addEventListener('load',()=>{{try{{fr.contentWindow.addEventListener('keydown',e=>{{if(e.key==='PageDown'||e.key==='Escape'||(fr.closest('.anim')&&e.key==='ArrowRight'))show(i+1);else if(e.key==='PageUp'||(fr.closest('.anim')&&e.key==='ArrowLeft'))show(i-1);}});}}catch(e){{}}}}));
addEventListener('resize',fit);fit();
const h=parseInt(location.hash.slice(1));show(isNaN(h)?0:h-1);
</script>
</body></html>'''
open(OUT,'w',encoding='utf-8').write(page)
print(len(S:=slides), 'slides', len(page)//1024, 'KB')
