# Flujo profesional del artefacto

Este proyecto sigue un flujo similar al que se usa en soluciones reales de automatización.

## 1. Entrada de datos

El archivo CSV contiene la información base.

Ejemplo:

```csv
fecha,dia,leche_litros,maiz_kilos,animales_observados,observacion
2026-05-18,lunes,23.5,38,18,produccion estable
```

## 2. Validación

Antes de calcular, el programa revisa que los datos tengan sentido.

Una validación evita respuestas falsas. Por ejemplo, no tendría sentido calcular un reporte si aparece `-5` kilos de maíz.

## 3. Análisis

El análisis convierte datos en indicadores:

- Total.
- Promedio.
- Máximo.
- Mínimo.
- Tendencia.
- Alertas.

## 4. Reporte

El reporte permite comunicar los resultados a otras personas.

Un reporte técnico debe ser claro, verificable y útil para tomar decisiones.

## 5. Respaldo

El respaldo protege la información original.

Un buen respaldo debe tener:

- Nombre claro.
- Fecha y hora.
- Ubicación organizada.

## 6. Dashboard

El dashboard permite comprender la información visualmente.

No reemplaza el reporte, lo complementa.

## 7. Logs

El log registra lo que ocurrió durante la ejecución. En sistemas reales, los logs ayudan a diagnosticar errores.
