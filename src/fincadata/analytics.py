from __future__ import annotations

from fincadata.models import AnalisisProduccion, RegistroProduccion


def analizar_produccion(
    registros: list[RegistroProduccion],
    umbral_leche: float,
    umbral_maiz: float,
) -> AnalisisProduccion:
    """Calcula indicadores y alertas sobre los registros válidos."""
    total_leche = sum(r.leche_litros for r in registros)
    total_maiz = sum(r.maiz_kilos for r in registros)
    promedio_leche = total_leche / len(registros)
    promedio_maiz = total_maiz / len(registros)
    promedio_animales = sum(r.animales_observados for r in registros) / len(registros)

    max_leche = max(registros, key=lambda r: r.leche_litros)
    min_leche = min(registros, key=lambda r: r.leche_litros)
    max_maiz = max(registros, key=lambda r: r.maiz_kilos)
    min_maiz = min(registros, key=lambda r: r.maiz_kilos)

    alertas = construir_alertas(registros, umbral_leche, umbral_maiz)
    tendencia_leche = calcular_tendencia([r.leche_litros for r in registros])
    tendencia_maiz = calcular_tendencia([r.maiz_kilos for r in registros])

    return AnalisisProduccion(
        total_leche=total_leche,
        total_maiz=total_maiz,
        promedio_leche=promedio_leche,
        promedio_maiz=promedio_maiz,
        max_leche_dia=max_leche.dia,
        max_leche_valor=max_leche.leche_litros,
        min_leche_dia=min_leche.dia,
        min_leche_valor=min_leche.leche_litros,
        max_maiz_dia=max_maiz.dia,
        max_maiz_valor=max_maiz.maiz_kilos,
        min_maiz_dia=min_maiz.dia,
        min_maiz_valor=min_maiz.maiz_kilos,
        promedio_animales=promedio_animales,
        alertas=alertas,
        tendencia_leche=tendencia_leche,
        tendencia_maiz=tendencia_maiz,
    )


def construir_alertas(
    registros: list[RegistroProduccion],
    umbral_leche: float,
    umbral_maiz: float,
) -> list[str]:
    """Genera alertas simples cuando los datos bajan de un umbral esperado."""
    alertas: list[str] = []

    for registro in registros:
        if registro.leche_litros < umbral_leche:
            alertas.append(
                f"{registro.dia}: leche baja ({registro.leche_litros} L). Revisar alimentación o salud."
            )
        if registro.maiz_kilos < umbral_maiz:
            alertas.append(
                f"{registro.dia}: cosecha de maíz baja ({registro.maiz_kilos} kg). Revisar clima o registro."
            )
        if "baja" in registro.observacion.lower() or "revisar" in registro.observacion.lower():
            alertas.append(f"{registro.dia}: observación importante: {registro.observacion}")
        
        # ALERTA 1: Animales observados bajos
        if registro.animales_observados < 15:
            alertas.append(
                f"{registro.dia}: pocos animales observados ({registro.animales_observados}). Revisar posibles fugas o enfermedad."
            )
        
        # ALERTA 4: Observación vacía
        if not registro.observacion.strip():
            alertas.append(
                f"{registro.dia}: registro sin observaciones. Por favor completar información."
            )

    return alertas


def calcular_tendencia(valores: list[float]) -> str:
    """Compara la primera mitad de la semana con la segunda mitad."""
    if len(valores) < 2:
        return "sin datos suficientes"

    mitad = len(valores) // 2
    promedio_inicial = sum(valores[:mitad]) / len(valores[:mitad])
    promedio_final = sum(valores[mitad:]) / len(valores[mitad:])
    diferencia = promedio_final - promedio_inicial

    if diferencia > 1:
        return "tendencia al aumento"
    if diferencia < -1:
        return "tendencia a la disminución"
    return "tendencia estable"
