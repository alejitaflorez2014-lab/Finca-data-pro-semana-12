# Explicación línea a línea de `src/main.py`

Este documento explica las partes más importantes del archivo principal.

## 1. Comentario inicial

```python
"""
Punto de entrada del proyecto FincaData Pro.
"""
```

Este bloque se llama **docstring**. Sirve para explicar qué hace el archivo.

## 2. Importaciones

```python
from pathlib import Path
import sys
```

Estas importaciones permiten trabajar con rutas de archivos y controlar el código de salida del programa.

```python
from fincadata.analytics import analizar_produccion
```

Aquí se importa una función creada en otro archivo del proyecto. Esto permite que el código esté organizado por responsabilidades.

## 3. Función `construir_parser`

```python
def construir_parser() -> argparse.ArgumentParser:
```

Esta función crea los argumentos que el usuario puede escribir en la terminal.

Por ejemplo:

```bash
python src/main.py --data data/produccion_reto.csv
```

El argumento `--data` permite cambiar el archivo de entrada sin modificar el código.

## 4. Argumento `--modo`

```python
choices=["todo", "validar", "reporte", "respaldo", "dashboard"]
```

Esto limita las opciones permitidas. Si el estudiante escribe una opción incorrecta, Python mostrará un error claro.

## 5. Función `ejecutar`

```python
def ejecutar(args: argparse.Namespace) -> int:
```

Esta función ejecuta el flujo completo del programa. Devuelve un número:

- `0`: todo salió bien.
- `1`, `2`, `3`: ocurrió algún problema.

## 6. Conversión de rutas

```python
data_path = Path(args.data)
output_dir = Path(args.salida)
```

Convierte texto en rutas manejables por Python.

## 7. Crear carpetas

```python
rutas = asegurar_directorios(output_dir)
```

Antes de generar archivos, el programa se asegura de que existan las carpetas necesarias.

## 8. Leer CSV

```python
registros_crudos = leer_registros_csv(data_path)
```

Aquí el programa lee el archivo CSV. Todavía no sabe si los datos son correctos; solo los carga.

## 9. Validar datos

```python
registros_validos, problemas = separar_registros_validos(registros_crudos)
```

Esta línea separa los datos buenos de los datos problemáticos.

## 10. Mostrar advertencias

```python
if problemas:
```

Si hay problemas, el programa no los oculta. Los muestra para que el estudiante aprenda a interpretar errores.

## 11. Modo estricto

```python
if args.estricto:
```

Si el modo estricto está activo, el programa se detiene cuando encuentra errores. Esto es útil en sistemas reales donde no se debe trabajar con datos malos.

## 12. Analizar producción

```python
analisis = analizar_produccion(...)
```

Aquí se calculan los totales, promedios, alertas y tendencias.

## 13. Generar reportes

```python
reporte_txt = generar_reporte_txt(...)
reporte_json = generar_reporte_json(...)
```

Estas líneas crean archivos de salida para consultar los resultados.

## 14. Crear respaldo

```python
respaldo = crear_respaldo(data_path, rutas.respaldos)
```

Esta línea copia el archivo original a la carpeta de respaldos.

## 15. Generar dashboard

```python
dashboard = generar_dashboard_html(...)
```

Esta línea crea una página web local con los resultados.

## 16. Cierre del programa

```python
if __name__ == "__main__":
    main()
```

Esto significa: si este archivo se ejecuta directamente, inicia el programa.
