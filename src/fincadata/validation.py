from __future__ import annotations

from datetime import datetime

from fincadata.config import DATE_FORMAT, REQUIRED_COLUMNS
from fincadata.models import ProblemaValidacion, RegistroProduccion


def separar_registros_validos(
    registros_crudos: list[dict[str, str]],
) -> tuple[list[RegistroProduccion], list[ProblemaValidacion]]:
    """Convierte filas del CSV en registros válidos y separa los problemas encontrados."""
    validos: list[RegistroProduccion] = []
    problemas: list[ProblemaValidacion] = []

    for indice, fila in enumerate(registros_crudos, start=2):
        errores = validar_columnas(fila)
        if errores:
            problemas.append(ProblemaValidacion(indice, "; ".join(errores)))
            continue

        try:
            fecha = datetime.strptime(fila["fecha"].strip(), DATE_FORMAT).date()
            dia = fila["dia"].strip().lower()
            leche = float(fila["leche_litros"])
            maiz = float(fila["maiz_kilos"])
            animales = int(fila["animales_observados"])
            observacion = fila["observacion"].strip()
        except ValueError as error:
            problemas.append(
                ProblemaValidacion(indice, f"tipo de dato inválido: {error}")
            )
            continue

        errores_rango = validar_rangos(leche, maiz, animales)
        if errores_rango:
            problemas.append(ProblemaValidacion(indice, "; ".join(errores_rango)))
            continue

        validos.append(
            RegistroProduccion(
                fila=indice,
                fecha=fecha,
                dia=dia,
                leche_litros=leche,
                maiz_kilos=maiz,
                animales_observados=animales,
                observacion=observacion,
            )
        )

    return validos, problemas


def validar_columnas(fila: dict[str, str]) -> list[str]:
    """Verifica que estén todas las columnas requeridas y que no estén vacías."""
    errores: list[str] = []

    for columna in REQUIRED_COLUMNS:
        if columna not in fila:
            errores.append(f"falta la columna {columna}")
        elif fila[columna] is None or str(fila[columna]).strip() == "":
            errores.append(f"la columna {columna} está vacía")

    return errores


def validar_rangos(leche: float, maiz: float, animales: int) -> list[str]:
    """Valida que los valores numéricos sean coherentes para el caso de estudio."""
    errores: list[str] = []

    if leche < 0:
        errores.append("la leche no puede ser negativa")
    if leche > 200:
        errores.append("la leche supera un rango razonable para esta práctica")
    if maiz < 0:
        errores.append("el maíz no puede ser negativo")
    if maiz > 500:
        errores.append("el maíz supera un rango razonable para esta práctica")
    if animales < 0:
        errores.append("los animales observados no pueden ser negativos")
    if animales > 200:
        errores.append("animales observados supera un rango razonable")

    return errores
