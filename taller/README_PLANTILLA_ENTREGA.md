# Artefacto del entorno - Semana 12

## 1. Nombre del proyecto

**FincaData Pro** - Sistema de automatización de reportes y análisis de producción rural.

## 2. Problema que resuelve

Este proyecto automatiza una tarea repetitiva y cansadora: revisar manualmente 
los datos de producción diaria de una finca (leche y maíz), validar que no haya 
errores, calcular totales y promedios cada semana, y crear reportes para 
archivarios. En lugar de hacer todo esto a mano con una calculadora o una hoja 
de cálculo (lo que tomaría horas), el script lo hace en segundos. También 
genera respaldos automáticos para que si se pierden los datos, tenemos una 
copia.

## 3. Entrada de datos

El programa recibe un archivo CSV llamado `data/produccion_semana.csv` que 
contiene registros con la estructura:
- **Fecha**: día de la semana
- **Producto**: tipo de producción (leche o maíz)
- **Cantidad**: valor numérico en litros o kilogramos

Ejemplo:
```
2026-05-25,Leche,22.5
2026-05-26,Maíz,40.3
```

## 4. Proceso realizado

El script ejecuta estos pasos automáticamente:

1. **Lectura de datos**: Lee el archivo CSV línea por línea y convierte cada 
fila en un registro.
2. **Validación**: Revisa que todas las cantidades sean números positivos y que 
no haya campos vacíos. Si encuentra errores, genera alertas pero continúa (a 
menos que actives modo estricto).
3. **Análisis de indicadores**: Calcula el total de producción, el promedio 
diario, cuál fue el día con más producción y cuál con menos.

4. **Detección de alertas**: Compara cada valor con umbrales mínimos (20L de 
leche, 35kg de maíz). Si está por debajo, marca una alerta roja.
5. **Generación de reportes**: Crea dos archivos: un texto legible para leer 
rápido, y un JSON para procesarlo con otros programas.
6. **Creación de respaldos**: Copia el archivo CSV original a una carpeta de 
respaldos con la fecha y hora en el nombre.
7. **Construcción de dashboard**: Genera un archivo HTML que puedes abrir en el 
navegador para ver gráficos y resúmenes visuales.
8. **Registro de logs**: Escribe todo lo que pasó en un archivo de historial 
para debugging.

## 5. Salidas generadas

El programa crea los siguientes archivos:

- **Reportes**: 
  - `outputs/reportes/reporte_produccion_YYYY-MM-DD_HH-MM-SS.txt` (reporte 
  legible)
  - `outputs/reportes/resumen_produccion_YYYY-MM-DD_HH-MM-SS.json` (datos 
  estructurados)
- **Respaldos**: `outputs/respaldos/respaldo_produccion_YYYY-MM-DD_HH-MM-SS.
csv` (copia de seguridad del CSV original)
- **Dashboard**: `outputs/dashboard/index.html` (página web interactiva con 
gráficos)
- **Logs**: `outputs/logs/fincadata_YYYY-MM-DD.log` (historial de ejecución)

## 6. Cómo ejecutar

Desde la terminal, en la carpeta del proyecto:

```bash
python src/main.py
```

Opcionalmente, puedes especificar otro archivo de entrada:

```bash
python src/main.py --data data/produccion_con_errores.csv
```

Para ver todas las opciones disponibles:

```bash
python src/main.py --help
```

## 7. Mejora propia

Lo que personalicé fue agregar validación automática con mensajes claros cuando 
encuentra datos sospechosos. Además, hice que el programa sea flexible: permite 
cambiar los umbrales de alerta desde la terminal (por ejemplo, si una semana la 
finca decide que 18L de leche es aceptable en lugar de 20L, lo puedo ajustar 
sin editar código). También añadí un modo "estricto" que detiene la ejecución 
si hay errores, útil cuando los datos tienen que estar 100% correctos.

## 8. Conclusión

Aprendí que los scripts son súper poderosos para automatizar tareas 
repetitivas. En lugar de perder horas validando datos manualmente, ahora dedico 
5 segundos a ejecutar el comando y obtengo reportes profesionales. También 
entendí por qué es importante validar datos antes de usarlos: un número 
negativo o un campo vacío puede romper todo el análisis si no lo atajamos a 
tiempo. Por último, vi que los respaldos automáticos son críticos en el mundo 
real—una finca no puede perder su información de producción por un error 
informático. Este proyecto me mostró que la programación no es solo escribir 
código, sino resolver problemas reales de forma eficiente.
