from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass
class RegistroProduccion:
    """Representa una fila válida del archivo CSV."""

    fila: int
    fecha: date
    dia: str
    leche_litros: float
    maiz_kilos: float
    animales_observados: int
    observacion: str


@dataclass
class ProblemaValidacion:
    """Describe un error encontrado en una fila del CSV."""

    fila: int
    mensaje: str


@dataclass
class AnalisisProduccion:
    """Agrupa los indicadores calculados a partir de los datos válidos."""

    total_leche: float
    total_maiz: float
    promedio_leche: float
    promedio_maiz: float
    max_leche_dia: str
    max_leche_valor: float
    min_leche_dia: str
    min_leche_valor: float
    max_maiz_dia: str
    max_maiz_valor: float
    min_maiz_dia: str
    min_maiz_valor: float
    promedio_animales: float
    alertas: list[str]
    tendencia_leche: str
    tendencia_maiz: str


@dataclass
class RutasSalida:
    """Carpetas de salida del proyecto."""

    base: Path
    reportes: Path
    respaldos: Path
    dashboard: Path
    logs: Path
