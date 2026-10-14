# Presentaciones · 6G Agro

Charlas para productores de Gando (6G Agro, Balcarce). Escribir siempre en español rioplatense.

## Márgenes Brutos 26/27 Balcarce (`margenes-balcarce-26-27/`)

- `index.html` es **generado**: no editarlo a mano.
- Para cambiar una filmina, editar `fuente/slides/<id>.html`. El orden de las filminas está en `fuente/deck.json` (`order`).
- Después de cualquier cambio, regenerar con:

  ```bash
  cd margenes-balcarce-26-27 && python construir.py
  ```

- Cada filmina es un `<section>` de 1920×1080 con estilos en línea. Logo: `/_blob/f6bd1d58341dd9e8a1a558b4880f8941`; QR de WhatsApp: `/_blob/1c2366ff4ed826ea2f535dc864c1601a` (el script los reemplaza por los SVG de la carpeta).
- Las animaciones van dentro de `<x-embed>`; el script las convierte en `iframe` para que funcionen sin internet.
- Números de referencia: `fuente/modelo_margenes.py` replica las fórmulas de la planilla (bonificación por materia grasa como % del precio; IIBB solo en girasol AO). Precio dolor = precio bruto de pizarra.
- La presentación tiene que seguir funcionando **sin internet** y con el logo chico abajo en todas las filminas.
