# Buenas prácticas para subir a GitHub

## Qué sí debes subir

- Código fuente.
- README.
- Guías del estudiante.
- Archivos de datos de ejemplo.
- Plantillas.

## Qué no deberías subir

- Reportes generados automáticamente.
- Respaldos generados.
- Logs.
- Archivos `.env`.
- Comprimidos `.zip` dentro del repositorio.

## Por qué existe `.gitignore`

El archivo `.gitignore` le dice a Git qué elementos debe ignorar.

En este proyecto, no se suben los archivos generados en `outputs/` porque cada estudiante debe generar sus propias evidencias al ejecutar el script.

## Comandos básicos

```bash
git init
git add .
git commit -m "Entrega artefacto semana 12"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```
