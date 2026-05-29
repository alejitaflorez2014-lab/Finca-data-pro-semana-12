"""
Punto de entrada del proyecto FincaData Pro.

Este archivo coordina todo el flujo:
1. Leer datos desde CSV.
2. Validar datos.
3. Calcular indicadores.
4. Generar reportes.
5. Crear respaldos.
6. Construir un dashboard HTML.
7. Registrar logs de ejecución.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from fincadata.analytics import analizar_produccion
from fincadata.backup import crear_respaldo
from fincadata.config import DEFAULT_DATA_FILE, DEFAULT_OUTPUT_DIR
from fincadata.dashboard import generar_dashboard_html
from fincadata.io_csv import leer_registros_csv
from fincadata.logger import crear_logger
from fincadata.reporting import generar_reporte_json, generar_reporte_txt
from fincadata.utils import asegurar_directorios, imprimir_resumen_consola
from fincadata.validation import separar_registros_validos


def construir_parser() -> argparse.ArgumentParser:
    """Crea y configura los argumentos disponibles para la terminal."""
    parser = argparse.ArgumentParser(
        description="FincaData Pro: automatiza reportes y respaldos de producción rural."
    )
    parser.add_argument(
        "--data",
        default=str(DEFAULT_DATA_FILE),
        help="Ruta del archivo CSV de entrada. Por defecto: data/produccion_semana.csv",
    )
    parser.add_argument(
        "--salida",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Carpeta donde se guardarán reportes, respaldos, logs y dashboard.",
    )
    parser.add_argument(
        "--modo",
        choices=["todo", "validar", "reporte", "respaldo", "dashboard"],
        default="todo",
        help="Acción principal que ejecutará el programa.",
    )
    parser.add_argument(
        "--umbral-leche",
        type=float,
        default=20.0,
        help="Valor mínimo esperado de leche diaria. Sirve para generar alertas.",
    )
    parser.add_argument(
        "--umbral-maiz",
        type=float,
        default=35.0,
        help="Valor mínimo esperado de maíz diario. Sirve para generar alertas.",
    )
    parser.add_argument(
        "--estricto",
        action="store_true",
        help="Si se activa, el programa se detiene cuando encuentra datos inválidos.",
    )
    return parser


def ejecutar(args: argparse.Namespace) -> int:
    """Ejecuta el flujo principal del artefacto según los argumentos recibidos."""
    data_path = Path(args.data)
    output_dir = Path(args.salida)
    rutas = asegurar_directorios(output_dir)
    logger = crear_logger(rutas.logs)

    logger.info("Inicio de ejecución FincaData Pro")
    logger.info("Archivo de datos seleccionado: %s", data_path)

    if not data_path.exists():
        print(f"ERROR: no se encontró el archivo de datos: {data_path}")
        logger.error("Archivo no encontrado: %s", data_path)
        return 1

    registros_crudos = leer_registros_csv(data_path)
    registros_validos, problemas = separar_registros_validos(registros_crudos)

    if problemas:
        print("\nAdvertencias encontradas durante la validación:")
        for problema in problemas:
            print(f"- Fila {problema.fila}: {problema.mensaje}")
            logger.warning("Fila %s: %s", problema.fila, problema.mensaje)

        if args.estricto:
            print("\nModo estricto activado: corrige los datos antes de continuar.")
            logger.error("Ejecución detenida por modo estricto")
            return 2

    if not registros_validos:
        print("ERROR: no hay registros válidos para analizar.")
        logger.error("No hay registros válidos")
        return 3

    if args.modo == "validar":
        print(f"\nValidación finalizada. Registros válidos: {len(registros_validos)}")
        print(f"Problemas detectados: {len(problemas)}")
        logger.info("Modo validar finalizado")
        return 0

    analisis = analizar_produccion(
        registros_validos,
        umbral_leche=args.umbral_leche,
        umbral_maiz=args.umbral_maiz,
    )

    reporte_txt = None
    reporte_json = None
    respaldo = None
    dashboard = None

    if args.modo in ["todo", "reporte"]:
        reporte_txt = generar_reporte_txt(analisis, registros_validos, problemas, rutas.reportes)
        reporte_json = generar_reporte_json(analisis, registros_validos, problemas, rutas.reportes)
        logger.info("Reportes generados: %s | %s", reporte_txt, reporte_json)

    if args.modo in ["todo", "respaldo"]:
        respaldo = crear_respaldo(data_path, rutas.respaldos)
        logger.info("Respaldo creado: %s", respaldo)

    if args.modo in ["todo", "dashboard"]:
        dashboard = generar_dashboard_html(analisis, registros_validos, problemas, rutas.dashboard)
        logger.info("Dashboard generado: %s", dashboard)

    imprimir_resumen_consola(
        analisis=analisis,
        reporte_txt=reporte_txt,
        reporte_json=reporte_json,
        respaldo=respaldo,
        dashboard=dashboard,
        problemas=problemas,
    )

    logger.info("Ejecución finalizada correctamente")
    return 0


def main() -> None:
    parser = construir_parser()
    args = parser.parse_args()
    codigo_salida = ejecutar(args)
    sys.exit(codigo_salida)


if __name__ == "__main__":
    main()
