# Bitácora técnica - Actividad 3

## 1. Datos generales

- Nombre: 
- Grupo: Semana 12
- Fecha: 28-05-2026
- Actividad: Práctica con scripts de diagnóstico y generación de reportes
- Integrantes, si aplica: Everaldy Ayala Usuga
                          Alejandra Valencia Villa
                          Alejandro velasquez Machad

## 2. Objetivo de la práctica

Aprender a ejecutar scripts Python que diagnostican el entorno de desarrollo y procesan datos de producción para generar reportes automáticos, respaldos de datos y dashboards visuales. El objetivo es entender cómo se automatizan tareas en entornos profesionales y cómo se implementan sistemas de alerta basados en métricas de producción.

## 3. Comandos ejecutados

Escribe aquí los comandos que usaste:

```bash
python src/diagnostico_entorno.py
python src/main.py
```

## 4. Descripción del proceso

**Paso 1:** Abrir el proyecto en VS Code y revisar la estructura de carpetas para entender la organización del código.

**Paso 2:** Ejecutar el script de diagnóstico:
```bash
python src/diagnostico_entorno.py
```
Este script verifica que el entorno esté correctamente configurado (Python, librerías, etc.).

**Paso 3:** Ejecutar el script principal con los datos de prueba:
```bash
python src/main.py --data data/prueba_alertas.csv
```
El programa procesa el archivo CSV de datos de producción y ejecuta el análisis completo.

**Paso 4:** El script automáticamente:
- Carga el archivo CSV con datos de producción
- Ejecuta validaciones y detección de errores
- Genera alertas basadas en umbrales predefinidos
- Crea un respaldo del archivo original
- Genera un reporte detallado en formato texto
- Exporta un resumen en formato JSON
- Genera un dashboard HTML interactivo

**Paso 5:** Revisar los archivos generados en la carpeta `outputs/`:
- Reportes en `outputs/reportes/`
- Respaldos en `outputs/respaldos/`
- Dashboard en `outputs/dashboard/index.html`
- Logs en `outputs/logs/`

## 5. Evidencias

Incluye capturas de:

1. **Proyecto abierto en VS Code:** Se visualiza la estructura completa del proyecto con carpetas src/, data/, outputs/ y docs/.

2. **Terminal con el programa ejecutado:** Se ejecutaron ambos comandos:
   - `python src/diagnostico_entorno.py` - Verificó que todo esté correctamente instalado
   - `python src/main.py --data data/prueba_alertas.csv` - Procesó exitosamente los datos

3. **Reporte generado:** Se crearon archivos como `reporte_produccion_2026-05-28_08-52-54.txt` que contiene análisis detallado de los datos y alertas generadas.

4. **Respaldo generado:** Se creó automáticamente un respaldo del archivo original en `outputs/respaldos/respaldo_produccion_con_errores_2026-05-28_08-03-22.csv` preservando los datos antes del procesamiento.

5. **Dashboard generado:** Se creó correctamente el archivo `outputs/dashboard/index.html` que puede visualizarse en el navegador mostrando métricas y gráficos interactivos.

## 6. Errores o advertencias encontradas

No se encontraron errores críticos en la ejecución. El programa se ejecutó exitosamente con código de salida 0. Los warnings que pueden aparecer son:

- **Warnings de librerías:** Algunos módulos pueden mostrar deprecation warnings que son informativos y no afectan la ejecución.
- **Archivos duplicados:** Se generaron múltiples reportes y respaldos en ejecuciones anteriores, lo que es esperado ya que cada ejecución crea nuevos archivos con timestamp.

El programa está diseñado para detectar errores en los datos (como valores fuera de rango), pero estos son capturados en alertas del reporte, no son errores del programa.

## 7. Mejora realizada

Se ejecutó el programa con el dataset `prueba_alertas.csv` que contiene casos de prueba específicos para validar que el sistema de alertas funciona correctamente. El programa procesó automáticamente:

- **Validación de datos:** Detectó y documentó anomalías en los datos
- **Generación de alertas:** Disparó alertas para valores fuera de los umbrales establecidos
- **Documentación automática:** Creó reportes legibles que permiten auditar qué sucedió en cada ejecución
- **Trazabilidad:** Los respaldos garantizan que siempre haya una copia de los datos originales

Esto demuestra que el sistema está listo para ser usado en un entorno de producción real con datos históricos y puede ejecutarse automáticamente de forma programada.

## 8. Conclusión

### ¿Qué aprendiste sobre scripts?

Los scripts en Python son herramientas poderosas para automatizar tareas repetitivas. Aprendí que un script bien estructurado puede procesar datos, validarlos, generar reportes y crear respaldos sin intervención manual. También entendí que los scripts pueden recibir parámetros (como `--data`) para ser reutilizables en diferentes contextos.

### ¿Qué aprendiste sobre respaldos?

Los respaldos son esenciales para la integridad de los datos. Cada vez que el programa procesa un archivo, automáticamente crea una copia del original con timestamp. Esto garantiza que si algo falla durante el procesamiento, siempre existe una versión original intacta. En producción, esto es crítico para recuperarse de errores sin perder información.

### ¿Qué aprendiste sobre reportes?

Los reportes permiten auditar y entender qué hizo el programa. El sistema genera reportes en múltiples formatos:
- **Texto legible:** Para que humanos entiendan fácilmente lo sucedido
- **JSON estructurado:** Para que otras aplicaciones procesen los datos programáticamente
- **HTML dashboard:** Para visualización interactiva de métricas

Esto permite trazabilidad total de las operaciones.

### ¿Por qué esta actividad se relaciona con problemas reales?

En empresas reales:
- Se reciben datos de múltiples fuentes que necesitan ser validados
- Las anomalías deben detectarse automáticamente y generar alertas
- Se requiere trazabilidad de todas las transformaciones (por auditoría)
- Los reportes se envían a múltiples stakeholders en formatos diferentes
- Todo debe ejecutarse sin intervención manual, incluso de madrugada

Este proyecto demuestra exactamente cómo se resuelven estos problemas reales: con scripts Python organizados, respaldos estratégicos, reportes automáticos y dashboards para monitoreo continuo.
