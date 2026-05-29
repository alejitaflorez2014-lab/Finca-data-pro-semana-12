# Automatización real programada

En esta actividad ejecutamos el script manualmente desde VS Code. Sin embargo, en un entorno real, un script puede programarse para ejecutarse automáticamente.

## Ejemplo conceptual

Una finca podría ejecutar el script cada domingo a las 6:00 p. m. para generar el reporte semanal.

## En Linux o macOS: cron

Ejemplo conceptual de una tarea semanal:

```bash
0 18 * * 0 cd /ruta/del/proyecto && python src/main.py
```

Significa:

- Minuto 0.
- Hora 18.
- Cualquier día del mes.
- Cualquier mes.
- Domingo.

## En Windows: Programador de tareas

Pasos generales:

1. Abrir Programador de tareas.
2. Crear tarea básica.
3. Elegir frecuencia semanal.
4. Seleccionar acción: iniciar un programa.
5. Programa: `python`.
6. Argumentos: `src/main.py`.
7. Iniciar en: carpeta del proyecto.

## Advertencia

No necesitas configurar esto para la entrega básica. Esta sección sirve para comprender cómo un script puede pasar de ser una práctica de clase a una solución real.
