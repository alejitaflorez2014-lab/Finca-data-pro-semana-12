# Explicación de cada archivo importante

## `src/main.py`

Es el archivo principal. Coordina todo el flujo del proyecto. No hace todo directamente, sino que llama funciones de otros módulos.

Su responsabilidad es organizar el proceso:

1. Leer argumentos de la terminal.
2. Confirmar rutas.
3. Leer datos.
4. Validar datos.
5. Analizar resultados.
6. Generar reportes.
7. Crear respaldos.
8. Generar dashboard.

## `src/fincadata/io_csv.py`

Contiene la función que lee el archivo CSV. Su trabajo es convertir el archivo en una lista de filas.

## `src/fincadata/validation.py`

Revisa si los datos están correctos. Por ejemplo:

- Que no falten columnas.
- Que los números sean números reales.
- Que no existan valores negativos.
- Que las fechas tengan formato correcto.

## `src/fincadata/analytics.py`

Calcula indicadores:

- Total de leche.
- Total de maíz.
- Promedios.
- Día con mayor producción.
- Día con menor producción.
- Alertas.
- Tendencias.

## `src/fincadata/reporting.py`

Genera archivos de reporte. En este proyecto genera:

- Reporte en texto `.txt`.
- Resumen estructurado `.json`.

## `src/fincadata/backup.py`

Crea una copia de seguridad del archivo CSV original. Esto es importante porque protege la información.

## `src/fincadata/dashboard.py`

Genera un archivo `index.html` que muestra los resultados visualmente.

## `src/fincadata/logger.py`

Crea un archivo de log. Un log es un registro técnico de lo que ocurrió durante la ejecución.

## `src/fincadata/models.py`

Define estructuras de datos usando `dataclass`. Esto ayuda a organizar la información de manera profesional.
