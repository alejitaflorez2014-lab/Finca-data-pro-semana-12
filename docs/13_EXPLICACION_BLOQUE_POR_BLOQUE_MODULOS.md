# Explicación bloque por bloque de los módulos

## `validation.py`

Este módulo hace una de las tareas más importantes: revisar que los datos sean confiables.

### Bloque 1: recorrer filas

```python
for indice, fila in enumerate(registros_crudos, start=2):
```

Se usa `start=2` porque la fila 1 del CSV contiene los encabezados. Así, si hay un error, el número mostrado coincide mejor con la fila real del archivo.

### Bloque 2: validar columnas

```python
errores = validar_columnas(fila)
```

Antes de convertir datos, se revisa que existan las columnas necesarias.

### Bloque 3: convertir datos

```python
leche = float(fila["leche_litros"])
```

El CSV entrega texto. Para calcular, el texto debe convertirse en número.

### Bloque 4: validar rangos

```python
if leche < 0:
```

Una producción negativa no tiene sentido. Por eso se rechaza.

## `analytics.py`

Este módulo convierte datos válidos en información.

### Totales

```python
total_leche = sum(r.leche_litros for r in registros)
```

Suma todos los litros registrados.

### Promedios

```python
promedio_leche = total_leche / len(registros)
```

Divide el total entre la cantidad de registros válidos.

### Máximos y mínimos

```python
max_leche = max(registros, key=lambda r: r.leche_litros)
```

Busca el día con mayor producción.

### Alertas

```python
if registro.leche_litros < umbral_leche:
```

Si la producción baja del valor esperado, se crea una alerta.

## `reporting.py`

Este módulo crea archivos de salida.

### Reporte TXT

Es útil para lectura humana.

### Reporte JSON

Es útil para otros sistemas, dashboards o procesamiento posterior.

## `backup.py`

Este módulo copia el archivo original.

```python
shutil.copy2(ruta_origen, ruta_destino)
```

`copy2` copia el archivo y conserva metadatos básicos.

## `dashboard.py`

Este módulo genera HTML. No usa internet. El archivo queda listo para abrirse en navegador.

Esta parte muestra que un script puede producir una salida visual, no solo texto.
