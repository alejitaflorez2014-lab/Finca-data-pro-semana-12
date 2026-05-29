# Guía detallada del estudiante

## 1. Qué problema vamos a resolver

En muchas fincas, tiendas escolares o instituciones se registran datos de forma manual. Por ejemplo, una finca puede registrar cada día cuántos litros de leche produjo y cuántos kilos de maíz cosechó.

El problema aparece cuando esa información debe revisarse cada semana. Si todo se hace manualmente, pueden ocurrir varios errores:

- Se olvida copiar un dato.
- Se calcula mal un promedio.
- Se pierde el archivo original.
- No queda evidencia del proceso.
- El reporte final no es claro.

La solución es crear un **script**. Un script es un programa pequeño que automatiza una tarea específica.

## 2. Qué hará este proyecto

Este proyecto hará varias tareas de manera automática:

1. Leerá un archivo CSV con datos de producción.
2. Revisará si los datos son válidos.
3. Calculará totales, promedios, máximos y mínimos.
4. Generará un reporte en texto.
5. Generará un resumen en JSON.
6. Creará una copia de respaldo del archivo original.
7. Creará un dashboard visual en HTML.
8. Guardará un registro de ejecución en logs.

## 3. Qué significa entrada, proceso y salida

Todo programa puede entenderse con esta estructura:

```text
Entrada -> Proceso -> Salida
```

En este proyecto:

| Parte | Ejemplo en el proyecto |
|---|---|
| Entrada | `data/produccion_semana.csv` |
| Proceso | Validar, calcular, generar reporte y respaldo |
| Salida | Archivos en `outputs/` |

Esta idea es muy importante porque permite explicar cualquier solución técnica de forma ordenada.

## 4. Qué debes observar al ejecutar el programa

Cuando ejecutes:

```bash
python src/main.py
```

Observa tres cosas:

1. Lo que aparece en la terminal.
2. Los archivos que se generan.
3. La relación entre los datos de entrada y los resultados.

No se trata solo de ejecutar. Se trata de **comprender qué ocurrió**.

## 5. Qué debes entregar

Debes entregar un proyecto que tenga:

- Archivos organizados.
- README breve.
- Script funcional.
- Archivo de datos.
- Reporte generado.
- Respaldo generado.
- Bitácora o explicación del proceso.

La entrega debe demostrar que puedes explicar qué hace tu artefacto.
