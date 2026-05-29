from datetime import date

from fincadata.analytics import analizar_produccion
from fincadata.models import RegistroProduccion


def test_analizar_produccion_calcula_totales():
    registros = [
        RegistroProduccion(2, date(2026, 1, 1), "lunes", 10, 20, 5, "ok"),
        RegistroProduccion(3, date(2026, 1, 2), "martes", 20, 30, 5, "ok"),
    ]
    resultado = analizar_produccion(registros, umbral_leche=15, umbral_maiz=25)
    assert resultado.total_leche == 30
    assert resultado.promedio_leche == 15
    assert resultado.total_maiz == 50
    assert resultado.promedio_maiz == 25
    assert len(resultado.alertas) == 2
