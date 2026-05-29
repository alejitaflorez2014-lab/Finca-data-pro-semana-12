from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from fincadata.config import TIMESTAMP_FORMAT
from fincadata.models import AnalisisProduccion, ProblemaValidacion, RegistroProduccion


def generar_reporte_txt(
    analisis: AnalisisProduccion,
    registros: list[RegistroProduccion],
    problemas: list[ProblemaValidacion],
    carpeta_reportes: Path,
) -> Path:
    """Genera un reporte en texto plano con indicadores y alertas."""
    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    ruta = carpeta_reportes / f"reporte_produccion_{timestamp}.txt"

    lineas = [
        "REPORTE SEMANAL - FINCADATA PRO",
        "=" * 45,
        "",
        "1. Resumen general",
        f"- Registros válidos analizados: {len(registros)}",
        f"- Total de leche: {analisis.total_leche:.2f} litros",
        f"- Promedio diario de leche: {analisis.promedio_leche:.2f} litros",
        f"- Total de maíz: {analisis.total_maiz:.2f} kilos",
        f"- Promedio diario de maíz: {analisis.promedio_maiz:.2f} kilos",
        f"- Promedio de animales observados: {analisis.promedio_animales:.1f}",
        "",
        "2. Días destacados",
        f"- Mayor producción de leche: {analisis.max_leche_dia} ({analisis.max_leche_valor:.2f} L)",
        f"- Menor producción de leche: {analisis.min_leche_dia} ({analisis.min_leche_valor:.2f} L)",
        f"- Mayor cosecha de maíz: {analisis.max_maiz_dia} ({analisis.max_maiz_valor:.2f} kg)",
        f"- Menor cosecha de maíz: {analisis.min_maiz_dia} ({analisis.min_maiz_valor:.2f} kg)",
        "",
        "3. Tendencias",
        f"- Leche: {analisis.tendencia_leche}",
        f"- Maíz: {analisis.tendencia_maiz}",
        "",
        "4. Alertas",
    ]

    if analisis.alertas:
        lineas.extend(f"- {alerta}" for alerta in analisis.alertas)
    else:
        lineas.append("- No se encontraron alertas relevantes.")

    lineas.extend(["", "5. Problemas de validación"])
    if problemas:
        lineas.extend(f"- Fila {p.fila}: {p.mensaje}" for p in problemas)
    else:
        lineas.append("- No se detectaron problemas en el archivo de entrada.")

    lineas.extend(["", "6. Lectura técnica"])
    lineas.append(
        "Este reporte convierte datos sueltos en información útil. "
        "Permite detectar cambios, justificar decisiones y conservar evidencia del proceso."
    )

    ruta.write_text("\n".join(lineas), encoding="utf-8")
    return ruta


def generar_reporte_json(
    analisis: AnalisisProduccion,
    registros: list[RegistroProduccion],
    problemas: list[ProblemaValidacion],
    carpeta_reportes: Path,
) -> Path:
    """Genera un resumen JSON útil para otros sistemas o dashboards."""
    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    ruta = carpeta_reportes / f"resumen_produccion_{timestamp}.json"

    contenido = {
        "generado_en": datetime.now().isoformat(timespec="seconds"),
        "registros_validos": len(registros),
        "analisis": asdict(analisis),
        "problemas_validacion": [asdict(p) for p in problemas],
        "registros": [
            {
                "fecha": r.fecha.isoformat(),
                "dia": r.dia,
                "leche_litros": r.leche_litros,
                "maiz_kilos": r.maiz_kilos,
                "animales_observados": r.animales_observados,
                "observacion": r.observacion,
            }
            for r in registros
        ],
    }

    ruta.write_text(json.dumps(contenido, ensure_ascii=False, indent=2), encoding="utf-8")
    return ruta
