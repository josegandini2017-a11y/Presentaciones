import os
OUT = os.path.join(os.path.dirname(__file__), 'slides/criticos.html')
MESES = ['Sep', 'Oct', 'Nov', 'Dic', 'Ene', 'Feb', 'Mar']
ROWS = [  # nombre, niveles por mes (0 nada, 1 bajo, 2 medio, 3 critico), etapa, es_fina
    ('Colza', [2, 3, 1, 0, 0, 0, 0], 'floración', True),
    ('Cebada', [1, 3, 1, 0, 0, 0, 0], 'espigazón', True),
    ('Trigo', [0, 2, 3, 1, 0, 0, 0], 'espigazón', True),
    ('Girasol', [0, 0, 1, 3, 2, 0, 0], 'floración', False),
    ('Maíz', [0, 0, 0, 2, 3, 2, 1], 'floración', False),
    ('Soja 1ra', [0, 0, 0, 0, 1, 3, 2], 'R3–R6', False),
    ('Soja 2da', [0, 0, 0, 0, 2, 1, 3], 'R3–R6', False),
]
COL = {1: '#F6CF9A', 2: '#E8873A', 3: '#B83A2E'}

h = []
h.append('<section id="criticos" data-transition="fade" style="background:#F5F1E6;color:#1C2B24;font-family:\'DM Sans\', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">')
h.append('<div style="display:flex;flex-direction:column;gap:12px">')
h.append('<p style="font-size:24px;letter-spacing:4px;text-transform:uppercase;color:#8C6418;font-weight:700">Momentos críticos · diversificar el riesgo</p>')
h.append('<h2 style="font-family:\'Fraunces\', Georgia, serif;font-size:72px;font-weight:600;line-height:1.1">Diversificar es repartir el riesgo</h2>')
h.append('</div>')
# month header
h.append('<div style="display:grid;grid-template-columns:300px repeat(7, 1fr);align-items:end">')
h.append('<p style="font-size:24px;color:#5B655E">Cultivo</p>')
for m in MESES:
    h.append(f'<p style="font-size:28px;font-weight:700;text-align:center;color:#1C2B24">{m}</p>')
h.append('</div>')
h.append('<div style="display:flex;flex-direction:column;gap:8px">')
for i, (name, lv, etapa, fina) in enumerate(ROWS):
    if i == 3:
        h.append('<hr style="border-top:2px dashed #CFC4A8">')
    op = ''
    h.append(f'<div style="display:grid;grid-template-columns:300px repeat(7, 1fr);height:54px;align-items:stretch;{op}">')
    h.append(f'<div style="display:flex;align-items:center"><p style="font-size:30px;font-weight:700">{name}</p></div>')
    on = [j for j, v in enumerate(lv) if v]
    a, b = on[0], on[-1]
    for j, v in enumerate(lv):
        if not v:
            h.append('<div style="border-left:1px solid #DDD5C2"></div>')
            continue
        rl = '32px' if j == a else '0'
        rr = '32px' if j == b else '0'
        style = f'background:{COL[v]};border-radius:{rl} {rr} {rr} {rl};display:flex;align-items:center;justify-content:center'
        if v == 3:
            h.append(f'<div style="{style}"><p style="font-size:24px;font-weight:700;color:#FBF3EA">{etapa}</p></div>')
        else:
            h.append(f'<div style="{style}"></div>')
    h.append('</div>')
h.append('<div style="display:grid;grid-template-columns:300px repeat(7, 1fr);height:64px;align-items:center;border-top:3px solid #1C2B24;padding:8px 0 0 0">')
h.append('<p style="font-size:26px;font-weight:700;color:#8C6418">Cultivos en pico</p>')
for j in range(7):
    n = sum(1 for r in ROWS if r[1][j] == 3)
    if n:
        h.append(f'<div style="display:flex;justify-content:center"><p style="font-family:Fraunces, Georgia, serif;font-size:36px;font-weight:600;width:56px;height:56px;line-height:1.55;text-align:center;border-radius:50%;background:#1C2B24;color:#F5F1E6">{n}</p></div>')
    else:
        h.append('<div></div>')
h.append('</div>')
h.append('</div>')
# footer legend
h.append('<div style="position:absolute;left:128px;bottom:56px;width:1520px;display:flex;align-items:center;gap:12px">')
h.append('<p style="font-size:24px;color:#5B655E">Cuánto pega un estrés (agua, calor, granizo) en el rinde:</p>')
h.append('<p style="font-size:24px;padding:4px 14px;border-radius:999px;background:#F6CF9A;color:#1C2B24">bajo</p>')
h.append('<p style="font-size:24px;padding:4px 14px;border-radius:999px;background:#E8873A;color:#1C2B24">medio</p>')
h.append('<p style="font-size:24px;padding:4px 14px;border-radius:999px;background:#B83A2E;color:#FBF3EA">crítico</p>')
h.append('</div>')
h.append('<img src="/_blob/f6bd1d58341dd9e8a1a558b4880f8941" alt="6G Agro" style="position:absolute;left:1688px;top:968px;width:104px;height:88px;object-fit:contain;border-radius:6px">')
h.append('<aside>Cada barra muestra cuándo el cultivo es más sensible: el rojo es el período crítico, cuando se define el número de granos y un estrés de agua, calor o granizo pega más fuerte en el rinde. La fina se define en primavera, octubre y noviembre. La gruesa se juega en pleno verano: el girasol en diciembre, el maíz en enero y la soja en febrero; la soja de segunda recién en marzo. La idea central: diversificar cultivos es diversificar períodos críticos. La fila de abajo cuenta cuántos cultivos están en su pico cada mes: nunca hay más de dos a la vez. Si una seca o un golpe de calor pega en enero, solo el maíz está en su momento crítico; el girasol ya pasó y la soja todavía no llegó. Poner todo en un solo cultivo es apostar el año entero a un mes.</aside>')
h.append('</section>')
open(OUT, 'w', encoding='utf-8').write('\n'.join(h) + '\n')
print('ok', sum(x.count('<') for x in h))
