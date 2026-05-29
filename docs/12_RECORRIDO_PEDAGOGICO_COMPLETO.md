# Recorrido pedagógico completo

Este documento explica la actividad como si fuera una clase paso a paso.

## Paso 1: reconocer la necesidad

Toda automatización nace de una necesidad. En este caso, la necesidad es organizar información semanal de una finca.

La pregunta central es:

> ¿Cómo podemos evitar cálculos manuales, pérdida de datos y reportes desordenados?

## Paso 2: identificar la información disponible

Antes de programar, observamos los datos.

El archivo `data/produccion_semana.csv` contiene:

- Fecha.
- Día.
- Litros de leche.
- Kilos de maíz.
- Animales observados.
- Observación.

Esto enseña que un programa depende de la calidad de sus datos.

## Paso 3: pensar el algoritmo sin código

Antes de mirar Python, podemos escribir el proceso en lenguaje natural:

```text
1. Abrir el archivo de datos.
2. Leer cada fila.
3. Revisar si cada dato es válido.
4. Separar datos correctos de datos incorrectos.
5. Calcular totales y promedios.
6. Detectar alertas.
7. Crear reporte.
8. Crear respaldo.
9. Crear dashboard.
10. Mostrar resumen final.
```

Este paso es clave porque el estudiante comprende que programar no es escribir código al azar: es traducir un proceso lógico a instrucciones.

## Paso 4: ejecutar y observar

Cuando ejecutas:

```bash
python src/main.py
```

No debes cerrar la terminal inmediatamente. Debes leer:

- Qué total calculó.
- Qué promedio calculó.
- Cuántas alertas detectó.
- Dónde guardó los archivos.

## Paso 5: verificar evidencias

Una solución técnica debe poder comprobarse. Por eso revisamos:

- Reporte TXT.
- Resumen JSON.
- Respaldo CSV.
- Dashboard HTML.
- Log de ejecución.

## Paso 6: analizar errores

Cuando ejecutas:

```bash
python src/main.py --data data/produccion_con_errores.csv
```

El programa muestra advertencias. Esto enseña una idea profesional: los errores no son fracaso; son información para mejorar.

## Paso 7: crear una mejora propia

Finalmente, el estudiante debe adaptar el proyecto. Puede cambiar datos, umbrales, textos, contexto o visualización.

La mejora demuestra apropiación del aprendizaje.

## Paso 8: documentar

El README y la bitácora no son relleno. Son parte de la evidencia profesional.

Una buena documentación responde:

- Qué hice.
- Cómo lo hice.
- Qué archivos generé.
- Qué problema resolví.
- Qué aprendí.
