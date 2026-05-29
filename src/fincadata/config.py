from pathlib import Path

DEFAULT_DATA_FILE = Path("data/produccion_semana.csv")
DEFAULT_OUTPUT_DIR = Path("outputs")

DATE_FORMAT = "%Y-%m-%d"
TIMESTAMP_FORMAT = "%Y-%m-%d_%H-%M-%S"

REQUIRED_COLUMNS = [
    "fecha",
    "dia",
    "leche_litros",
    "maiz_kilos",
    "animales_observados",
    "observacion",
]
