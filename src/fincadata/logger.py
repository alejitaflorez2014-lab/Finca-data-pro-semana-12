from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path

from fincadata.config import TIMESTAMP_FORMAT


def crear_logger(carpeta_logs: Path) -> logging.Logger:
    """Crea un logger que guarda un archivo de log por ejecución."""
    logger = logging.getLogger("fincadata")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    ruta_log = carpeta_logs / f"ejecucion_{timestamp}.log"

    formato = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    manejador = logging.FileHandler(ruta_log, encoding="utf-8")
    manejador.setFormatter(formato)

    logger.addHandler(manejador)
    return logger
