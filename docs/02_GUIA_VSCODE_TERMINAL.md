# Guía de VS Code y terminal

## 1. Abrir terminal integrada

En VS Code usa:

```text
Terminal > New Terminal
```

La terminal debe abrirse en la carpeta del proyecto.

## 2. Verificar ubicación

Puedes escribir:

```bash
pwd
```

En PowerShell también puedes usar:

```powershell
Get-Location
```

Debes estar dentro de la carpeta donde está `README.md`.

## 3. Ejecutar diagnóstico

```bash
python src/diagnostico_entorno.py
```

Este comando revisa que las carpetas principales existan.

## 4. Ejecutar el proyecto

```bash
python src/main.py
```

## 5. Ejecutar con otro archivo de datos

```bash
python src/main.py --data data/produccion_reto.csv
```

## 6. Ejecutar con modo de validación

```bash
python src/main.py --modo validar
```

Este modo solo revisa los datos y muestra si hay errores.

## 7. Ejecutar en modo estricto

```bash
python src/main.py --data data/produccion_con_errores.csv --estricto
```

En modo estricto, si el archivo tiene errores, el programa se detiene. Esto enseña una práctica profesional: no generar reportes con datos que no son confiables.

## 8. Error común: Python no reconocido

Si aparece algo como:

```text
python no se reconoce como un comando interno o externo
```

Significa que Python no está instalado o no está agregado al PATH. En algunos equipos el comando puede ser:

```bash
py src/main.py
```
