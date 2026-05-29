from __future__ import annotations

import csv
from pathlib import Path


def leer_registros_csv(ruta_csv: Path) -> list[dict[str, str]]:
    """Lee un archivo CSV y devuelve sus filas como diccionarios de texto."""
    with ruta_csv.open("r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        return [dict(fila) for fila in lector]
