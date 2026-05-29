# Inicio rápido en VS Code

Esta guía te permite ejecutar el proyecto sin perderte.

## 1. Abrir el proyecto

1. Abre Visual Studio Code.
2. Selecciona **File > Open Folder**.
3. Escoge la carpeta del proyecto.
4. Verifica que puedas ver `data`, `src`, `docs`, `taller` y `outputs`.

## 2. Confirmar que Python funciona

Abre la terminal integrada:

```bash
python --version
```

También puedes ejecutar:

```bash
python src/diagnostico_entorno.py
```

Si ves un mensaje de diagnóstico exitoso, puedes continuar.

## 3. Ejecutar el proyecto principal

```bash
python src/main.py
```

El programa debe leer `data/produccion_semana.csv` y crear archivos en `outputs/`.

## 4. Ejecutar el caso con errores

```bash
python src/main.py --data data/produccion_con_errores.csv
```

Este archivo tiene datos incorrectos a propósito. El objetivo es que aprendas a leer advertencias y entender por qué la validación es importante.

## 5. Abrir el dashboard

Después de ejecutar el proyecto, abre:

```text
outputs/dashboard/index.html
```

Puedes abrirlo con doble clic desde el explorador de archivos o desde VS Code con la extensión Live Server si está disponible.

## 6. Guardar evidencias

Toma capturas de:

1. Proyecto abierto en VS Code.
2. Terminal con el comando ejecutado.
3. Reporte generado.
4. Respaldo generado.
5. Dashboard abierto.

Luego completa `taller/BITACORA_PLANTILLA.md`.
