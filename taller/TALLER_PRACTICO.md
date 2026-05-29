# Taller práctico - Artefacto del entorno

## Parte 1: exploración del proyecto

1. ¿Qué carpetas principales tiene el proyecto?
   - **data/**: contiene los archivos CSV con los datos de producción
   - **src/**: la carpeta con el código principal (main.py y la carpeta 
   fincadata/)
   - **outputs/**: donde se guardan todos los resultados (reportes, respaldos, 
   logs, dashboard)
   - **docs/**: documentación y guías del proyecto
   - **taller/**: materiales del taller práctico

2. ¿Cuál archivo se ejecuta para iniciar el programa?
   - `src/main.py` es el archivo principal que ejecuta todo el proceso

3. ¿Dónde están los datos de entrada?
   - En la carpeta `data/`, hay cuatro archivos CSV: produccion_semana.csv, 
   produccion_con_errores.csv, produccion_reto.csv y prueba_alertas.csv

4. ¿Dónde se guardan los reportes?
   - En `outputs/reportes/`, se guardan dos tipos: archivos .txt con el reporte 
   legible y archivos .json con los resúmenes en formato estructurado

5. ¿Dónde se guardan los respaldos?
   - En `outputs/respaldos/`, se guardan copias automáticas de los datos 
   procesados con fecha y hora de ejecución

## Parte 2: ejecución

Ejecuta:

```bash
python src/main.py
```

Responde:

1. ¿Qué mensaje apareció en la terminal?
   - El programa mostró un resumen en la terminal con los totales de 
   producción: 7 registros procesados, 162.6 litros de leche total, 277 kilos 
   de maíz, junto con los promedios y el número de alertas generadas.

2. ¿Cuántas alertas se generaron?
   - Se generaron 4 alertas durante la semana, todas relacionadas con caídas en 
   la producción de leche (especialmente el domingo con 19.6 litros) y una 
   alerta sobre animales observados.

3. ¿Qué archivos nuevos aparecieron en `outputs/`?
   - Un archivo de reporte con formato .txt (ej: 
   reporte_produccion_2026-05-28_08-52-54.txt)
   - Un archivo de resumen con formato .json con la misma fecha
   - Un archivo de respaldo del CSV procesado en la carpeta respaldos/
   - Se actualizó o creó el dashboard en outputs/dashboard/index.html

4. ¿Qué información muestra el reporte TXT?
   - El reporte muestra: número de registros válidos, total y promedio de 
   leche, total y promedio de maíz, promedio de animales, días destacados con 
   mayor y menor producción, tendencias, alertas generadas, y problemas 
   encontrados en la validación.

5. ¿Qué utilidad tiene el dashboard?
   - El dashboard es un archivo HTML interactivo que visualiza gráficamente los 
   datos de producción, permitiendo ver tendencias y cambios sin necesidad de 
   abrir archivos técnicos o usar código.

## Parte 3: validación de errores

Ejecuta:

```bash
python src/main.py --data data/produccion_con_errores.csv
```

Responde:

1. ¿Qué errores o advertencias aparecieron?
   - Advertencias como: "valor de leche no es un número (no_disponible)", "maíz 
   no puede ser negativo (-5)", "fecha con formato incorrecto", "leche 
   exagerada (400 litros - fuera de rango)", "animales no es un número 
   (diecinueve)". El programa mostró 6 problemas encontrados durante la 
   validación.

2. ¿Por qué esos datos no son confiables?
   - Porque tienen valores imposibles (leche de 400L, maíz negativo), datos mal 
   formateados (fechas inválidas, letras en campos numéricos) y valores 
   faltantes. Los datos incompletos o incorrectos generan cálculos inválidos.

3. ¿Qué pasaría si generamos decisiones con datos incorrectos?
   - Podríamos tomar decisiones equivocadas: si registramos 400 litros en vez 
   de 40, el ganadero creería que la producción fue excelente cuando realmente 
   fue normal. O si ignoramos datos negativos, no detectaríamos errores en los 
   registros. Las decisiones basadas en datos falsos llevan a acciones 
   innecesarias o inefectivas.

4. ¿Qué hace el programa con las filas válidas?
   
   - Las procesa normalmente: calcula totales, promedios, detecta tendencias y 
   genera alertas. En este caso, procesó 5 registros válidos (lunes, miércoles, 
   viernes, sábado y domingo) y rechazó los que tenían errores sin afectar el 
   análisis de los datos limpios.

## Parte 4: creación propia

Crea una mejora pequeña. Elige una:

- Cambiar los datos de producción.
- Crear un nuevo CSV de otro contexto.
- Modificar el umbral de alerta.
- Cambiar el texto del reporte.
- Personalizar el dashboard.

**Mi mejora:**

Modifiqué el umbral de alerta para leche usando:

```bash
python src/main.py --umbral-leche 22.0
```

**¿Qué cambié?**
- Bajé el umbral mínimo de leche de 20L a 22L diarios. Esto genera alertas más 
sensibles para detectar caídas más pequeñas en la producción.

**¿Por qué?**
- Después de analizar los datos, vi que la producción normal está entre 21-26L. 
Un umbral de 20L era muy permisivo y dejaba pasar caídas preocupantes. Con 22L, 
el ganadero recibe alertas más oportunas cuando la producción comienza a bajar, 
permitiendo actuar antes de que se agrave el problema (enfermedad del animal, 
problemas de alimentación, etc.).

## Parte 5: reflexión

1. ¿Qué tarea repetitiva automatiza este proyecto?
   - Automatiza el análisis semanal de producción: leer datos, validarlos, 
   
   calcular totales y promedios, detectar anomalías, generar reportes, crear 
   respaldos y visualizar resultados. Antes, un ganadero tendría que hacer esto 
   manualmente cada semana, ahora es solo ejecutar un comando.

2. ¿Qué diferencia hay entre reporte y respaldo?
   - El reporte (.txt y .json) es un análisis interpretado para tomar 
   decisiones: muestra tendencias, alertas y conclusiones. El respaldo es una 
   copia de los datos procesados guardada por seguridad, para no perder 
   información si algo falla o cambian los datos originales.

3. ¿Por qué es importante validar datos?
   - Porque datos incorrectos generan análisis inútiles o peligrosos. Un error 
   pequeño (como 400L en vez de 40L) puede llevar a decisiones completamente 
   equivocadas. La validación filtra errores antes de que contaminen todo el 
   análisis.

4. ¿Cómo podrías usar un proyecto similar en tu comunidad?
   - Podría adaptarse para registrar: producciones de otros cultivos (café, 
   cacao, caña), ventas diarias de un negocio pequeño, asistencia en una 
   escuela, consumo de agua en una vereda, o monitoreo de plagas. Cualquier 
   dato repetitivo que genere decisiones.

5. ¿Qué aprendiste sobre el uso profesional del entorno de programación?
   - Que programming no es solo escribir código: es crear herramientas que 
   resuelven problemas reales. Aprendí que los scripts automatizan lo tedioso, 
   que validar datos es esencial, que documentar con reportes claros es parte 
   del trabajo, y que un buen programa anticipa errores y ayuda a quien lo usa 
   (el ganadero) sin que sepa de código.
