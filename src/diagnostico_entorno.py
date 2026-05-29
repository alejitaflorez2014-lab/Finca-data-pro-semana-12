from pathlib import Path
import sys


def main():
    print("Diagnóstico del entorno FincaData Pro")
    print("-" * 45)
    print(f"Python detectado: {sys.version.split()[0]}")
    print(f"Carpeta actual: {Path.cwd()}")

    rutas_necesarias = [
        Path("data"),
        Path("src"),
        Path("outputs"),
        Path("outputs/reportes"),
        Path("outputs/respaldos"),
        Path("outputs/dashboard"),
        Path("outputs/logs"),
    ]

    for ruta in rutas_necesarias:
        if ruta.exists():
            print(f"OK  {ruta}")
        else:
            print(f"CREANDO {ruta}")
            ruta.mkdir(parents=True, exist_ok=True)

    archivo_datos = Path("data/produccion_semana.csv")
    if archivo_datos.exists():
        print(f"OK  Archivo de datos encontrado: {archivo_datos}")
    else:
        print(f"ERROR  No se encontró el archivo: {archivo_datos}")

    print("\nSi todos los elementos aparecen como OK, ejecuta:")
    print("python src/main.py")


if __name__ == "__main__":
    main()
