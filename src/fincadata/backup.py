from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from fincadata.config import TIMESTAMP_FORMAT


def crear_respaldo(ruta_origen: Path, carpeta_respaldos: Path) -> Path:
    """Copia el archivo de datos a la carpeta de respaldos usando fecha y hora."""
    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    nombre = f"respaldo_{ruta_origen.stem}_{timestamp}{ruta_origen.suffix}"
    ruta_destino = carpeta_respaldos / nombre
    shutil.copy2(ruta_origen, ruta_destino)
    return ruta_destino
