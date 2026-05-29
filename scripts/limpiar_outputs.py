from pathlib import Path

CARPETAS = [
    Path("outputs/reportes"),
    Path("outputs/respaldos"),
    Path("outputs/dashboard"),
    Path("outputs/logs"),
]


def main():
    eliminados = 0
    for carpeta in CARPETAS:
        carpeta.mkdir(parents=True, exist_ok=True)
        for archivo in carpeta.iterdir():
            if archivo.name == ".gitkeep":
                continue
            if archivo.is_file():
                archivo.unlink()
                eliminados += 1
    print(f"Limpieza finalizada. Archivos eliminados: {eliminados}")


if __name__ == "__main__":
    main()
