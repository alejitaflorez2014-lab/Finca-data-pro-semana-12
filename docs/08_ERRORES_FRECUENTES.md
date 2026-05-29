# Errores frecuentes y soluciones

## 1. Estoy en la carpeta incorrecta

Síntoma:

```text
No such file or directory
```

Solución:

Asegúrate de abrir la carpeta completa del proyecto en VS Code.

## 2. Python no aparece reconocido

Síntoma:

```text
python no se reconoce como comando
```

Solución:

Prueba:

```bash
py src/main.py
```

Si tampoco funciona, Python no está instalado correctamente.

## 3. El CSV tiene datos malos

Síntoma:

```text
Advertencias encontradas durante la validación
```

Solución:

Abre el archivo CSV y revisa la fila indicada.

## 4. No veo archivos en outputs

Posibles causas:

- Ejecutaste en modo `validar`.
- El programa se detuvo por error.
- Estás mirando otra carpeta.

Solución:

Ejecuta:

```bash
python src/main.py
```

Luego revisa `outputs/reportes`, `outputs/respaldos` y `outputs/dashboard`.

## 5. El dashboard no se abre bonito en VS Code

Solución:

Abre `outputs/dashboard/index.html` en un navegador como Chrome, Edge o Firefox.
