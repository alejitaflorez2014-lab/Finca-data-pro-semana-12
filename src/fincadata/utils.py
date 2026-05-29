from __future__ import annotations

from pathlib import Path

from fincadata.models import AnalisisProduccion, ProblemaValidacion, RutasSalida


def asegurar_directorios(base: Path) -> RutasSalida:
    """Crea las carpetas necesarias para guardar resultados."""
    reportes = base / "reportes"
    respaldos = base / "respaldos"
    dashboard = base / "dashboard"
    logs = base / "logs"

    for carpeta in [base, reportes, respaldos, dashboard, logs]:
        carpeta.mkdir(parents=True, exist_ok=True)

    return RutasSalida(
        base=base,
        reportes=reportes,
        respaldos=respaldos,
        dashboard=dashboard,
        logs=logs,
    )


def imprimir_resumen_consola(
    analisis: AnalisisProduccion,
    reporte_txt: Path | None,
    reporte_json: Path | None,
    respaldo: Path | None,
    dashboard: Path | None,
    problemas: list[ProblemaValidacion],
) -> None:
    """Muestra en la terminal un resumen claro para el estudiante."""
    print("\nProceso finalizado")
    print("-" * 45)
    print(f"Total leche: {analisis.total_leche:.2f} litros")
    print(f"Promedio leche: {analisis.promedio_leche:.2f} litros")
    print(f"Total maíz: {analisis.total_maiz:.2f} kilos")
    print(f"Promedio maíz: {analisis.promedio_maiz:.2f} kilos")
    print(f"Alertas generadas: {len(analisis.alertas)}")
    print(f"Problemas de validación: {len(problemas)}")

    if reporte_txt:
        print(f"Reporte TXT: {reporte_txt}")
    if reporte_json:
        print(f"Resumen JSON: {reporte_json}")
    if respaldo:
        print(f"Respaldo: {respaldo}")
    if dashboard:
        print(f"Dashboard: {dashboard}")

    print("\nRevisa la carpeta outputs para consultar los archivos generados.")
