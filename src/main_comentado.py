"""
Versión comentada de main.py.

Este archivo no es obligatorio para ejecutar la actividad. Existe para estudiar el flujo del programa con explicaciones más cercanas al estudiante.

Puedes compararlo con `src/main.py` para entender cómo se organiza una solución profesional.
"""

# argparse permite leer opciones desde la terminal.
# Ejemplo: python src/main.py --data data/produccion_reto.csv
import argparse

# Path permite trabajar con rutas de archivos sin depender tanto del sistema operativo.
from pathlib import Path

# sys permite finalizar el programa con códigos de salida.
import sys

# Estas importaciones vienen de módulos propios del proyecto.
# Cada módulo tiene una responsabilidad específica.
from fincadata.analytics import analizar_produccion
from fincadata.backup import crear_respaldo
from fincadata.config import DEFAULT_DATA_FILE, DEFAULT_OUTPUT_DIR
from fincadata.dashboard import generar_dashboard_html
from fincadata.io_csv import leer_registros_csv
from fincadata.logger import crear_logger
from fincadata.reporting import generar_reporte_json, generar_reporte_txt
from fincadata.utils import asegurar_directorios, imprimir_resumen_consola
from fincadata.validation import separar_registros_validos


def construir_parser():
    """Define las opciones que el estudiante puede usar desde la terminal."""

    # Creamos el parser, que es el objeto encargado de entender los argumentos.
    parser = argparse.ArgumentParser(
        description="FincaData Pro: automatiza reportes y respaldos de producción rural."
    )

    # Permite cambiar el archivo CSV sin editar el código.
    parser.add_argument("--data", default=str(DEFAULT_DATA_FILE))

    # Permite cambiar la carpeta donde se guardan los resultados.
    parser.add_argument("--salida", default=str(DEFAULT_OUTPUT_DIR))

    # Permite ejecutar solo una parte del proceso.
    parser.add_argument(
        "--modo",
        choices=["todo", "validar", "reporte", "respaldo", "dashboard"],
        default="todo",
    )

    # Umbrales usados para generar alertas.
    parser.add_argument("--umbral-leche", type=float, default=20.0)
    parser.add_argument("--umbral-maiz", type=float, default=35.0)

    # Si se usa --estricto, el programa se detiene ante errores de datos.
    parser.add_argument("--estricto", action="store_true")

    return parser


def ejecutar(args):
    """Ejecuta la solución paso a paso."""

    # Convertimos las rutas recibidas por terminal en objetos Path.
    data_path = Path(args.data)
    output_dir = Path(args.salida)

    # Creamos las carpetas de salida si no existen.
    rutas = asegurar_directorios(output_dir)

    # Creamos un logger para dejar evidencia técnica de ejecución.
    logger = crear_logger(rutas.logs)
    logger.info("Inicio de ejecución")

    # Antes de leer el archivo, confirmamos que exista.
    if not data_path.exists():
        print(f"ERROR: no se encontró el archivo de datos: {data_path}")
        return 1

    # Leemos las filas del CSV como texto.
    registros_crudos = leer_registros_csv(data_path)

    # Convertimos y validamos las filas. Algunas pueden ser válidas y otras no.
    registros_validos, problemas = separar_registros_validos(registros_crudos)

    # Si hay problemas, se muestran para que el estudiante pueda analizarlos.
    if problemas:
        print("Advertencias encontradas:")
        for problema in problemas:
            print(f"- Fila {problema.fila}: {problema.mensaje}")

        # En modo estricto no se continúa con datos malos.
        if args.estricto:
            print("Modo estricto: corrige los datos antes de continuar.")
            return 2

    # Si no queda ningún dato válido, no hay nada que analizar.
    if not registros_validos:
        print("ERROR: no hay registros válidos para analizar.")
        return 3

    # Si el modo es solo validar, terminamos aquí.
    if args.modo == "validar":
        print(f"Registros válidos: {len(registros_validos)}")
        print(f"Problemas detectados: {len(problemas)}")
        return 0

    # Calculamos indicadores de producción.
    analisis = analizar_produccion(
        registros_validos,
        umbral_leche=args.umbral_leche,
        umbral_maiz=args.umbral_maiz,
    )

    # Variables donde guardaremos las rutas generadas.
    reporte_txt = None
    reporte_json = None
    respaldo = None
    dashboard = None

    # Si corresponde, generamos reportes.
    if args.modo in ["todo", "reporte"]:
        reporte_txt = generar_reporte_txt(analisis, registros_validos, problemas, rutas.reportes)
        reporte_json = generar_reporte_json(analisis, registros_validos, problemas, rutas.reportes)

    # Si corresponde, generamos respaldo.
    if args.modo in ["todo", "respaldo"]:
        respaldo = crear_respaldo(data_path, rutas.respaldos)

    # Si corresponde, generamos dashboard.
    if args.modo in ["todo", "dashboard"]:
        dashboard = generar_dashboard_html(analisis, registros_validos, problemas, rutas.dashboard)

    # Mostramos al estudiante un resumen claro en terminal.
    imprimir_resumen_consola(analisis, reporte_txt, reporte_json, respaldo, dashboard, problemas)

    return 0


def main():
    """Función inicial del programa."""
    parser = construir_parser()
    args = parser.parse_args()
    codigo = ejecutar(args)
    sys.exit(codigo)


if __name__ == "__main__":
    main()
