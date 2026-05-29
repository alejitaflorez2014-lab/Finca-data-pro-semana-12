# Diagramas y flujos del proyecto

## Flujo general

```mermaid
flowchart LR
    A[Archivo CSV] --> B[Lectura de datos]
    B --> C[Validación]
    C --> D[Análisis]
    D --> E[Reporte TXT]
    D --> F[Resumen JSON]
    D --> G[Dashboard HTML]
    A --> H[Respaldo]
    C --> I[Advertencias]
```

## Entrada, proceso y salida

```mermaid
flowchart TD
    A[Entrada: data/produccion_semana.csv] --> B[Proceso: script Python]
    B --> C[Salida: outputs/reportes]
    B --> D[Salida: outputs/respaldos]
    B --> E[Salida: outputs/dashboard]
    B --> F[Salida: outputs/logs]
```

## Responsabilidad de los módulos

```mermaid
flowchart TB
    main[main.py coordina] --> csv[io_csv.py lee CSV]
    main --> validation[validation.py valida datos]
    main --> analytics[analytics.py calcula indicadores]
    main --> reporting[reporting.py genera reportes]
    main --> backup[backup.py crea respaldos]
    main --> dashboard[dashboard.py crea visualización]
    main --> logger[logger.py registra ejecución]
```

## Cómo usar estos diagramas

Estos diagramas sirven para explicar el proyecto en el README, en la bitácora o durante la sustentación. No es necesario memorizarlos; lo importante es entender que cada parte del proyecto tiene una función clara.
