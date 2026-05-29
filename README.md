# FincaData Pro - Actividad 3: Artefacto del entorno

## Semana 12: scripts para tareas repetitivas, automatización de respaldos y reportes

Este proyecto es una práctica profesional guiada para desarrollar un **artefacto del entorno de programación**. El estudiante abre el proyecto en Visual Studio Code, ejecuta un script de Python, analiza datos de producción rural, genera reportes, crea respaldos automáticos, revisa un dashboard visual y documenta su proceso en una bitácora.

La actividad trabaja una situación realista:

> Una finca necesita registrar la producción diaria de leche y maíz. La información debe analizarse semanalmente, guardarse en reportes claros y respaldarse para evitar pérdida de datos.

## Qué vas a aprender

Al completar el proyecto, podrás explicar y practicar:

1. Qué es un script y por qué permite automatizar tareas repetitivas.
2. Cómo leer datos desde un archivo CSV.
3. Cómo validar datos antes de usarlos.
4. Cómo calcular totales, promedios, máximos y mínimos.
5. Cómo generar reportes `.txt` y resúmenes `.json`.
6. Cómo crear respaldos automáticos con fecha y hora.
7. Cómo generar un dashboard HTML sin depender de internet.
8. Cómo documentar evidencias técnicas en un README y una bitácora.

## Inicio rápido

Abre la carpeta en VS Code y ejecuta:

```bash
python src/diagnostico_entorno.py
```

Luego ejecuta el proyecto principal:

```bash
python src/main.py
```

Para practicar con errores intencionales:

```bash
python src/main.py --data data/produccion_con_errores.csv
```

Para ver todas las opciones:

```bash
python src/main.py --help
```

## Estructura del proyecto

```text
fincadata-pro-semana12/
├── README.md
├── INICIO_RAPIDO.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── produccion_semana.csv
│   ├── produccion_con_errores.csv
│   └── produccion_reto.csv
├── src/
│   ├── main.py
│   ├── diagnostico_entorno.py
│   └── fincadata/
│       ├── __init__.py
│       ├── analytics.py
│       ├── backup.py
│       ├── config.py
│       ├── dashboard.py
│       ├── io_csv.py
│       ├── logger.py
│       ├── models.py
│       ├── reporting.py
│       ├── utils.py
│       └── validation.py
├── docs/
├── taller/
├── ejercicios_estudiante/
├── material_docente/
├── scripts/
├── tests/
└── outputs/
    ├── dashboard/
    ├── logs/
    ├── reportes/
    └── respaldos/
```

## Qué genera el programa

Después de ejecutar el script, revisa estas carpetas:

```text
outputs/reportes/      Reporte de producción en TXT y resumen en JSON
outputs/respaldos/     Copia de seguridad del archivo de datos usado
outputs/dashboard/     Dashboard visual en HTML
outputs/logs/          Registro técnico de la ejecución
```

## Entrega sugerida para Moodle

Entrega un archivo `.zip` que contenga:

- Proyecto funcionando.
- README completado.
- Capturas del proceso.
- Reporte generado.
- Respaldo generado.
- Bitácora de trabajo.

Consulta `taller/CHECKLIST_ENTREGA.md` antes de subir tu actividad.
