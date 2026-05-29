from __future__ import annotations

from datetime import datetime
from pathlib import Path

from fincadata.models import AnalisisProduccion, ProblemaValidacion, RegistroProduccion


def generar_dashboard_html(
    analisis: AnalisisProduccion,
    registros: list[RegistroProduccion],
    problemas: list[ProblemaValidacion],
    carpeta_dashboard: Path,
) -> Path:
    """Genera un dashboard HTML autocontenido para visualizar resultados."""
    ruta = carpeta_dashboard / "index.html"
    barras_leche = construir_barras(registros, "leche_litros", max(r.leche_litros for r in registros))
    barras_maiz = construir_barras(registros, "maiz_kilos", max(r.maiz_kilos for r in registros))
    alertas_html = construir_lista(analisis.alertas, "No se encontraron alertas.")
    problemas_html = construir_lista(
        [f"Fila {p.fila}: {p.mensaje}" for p in problemas],
        "No se detectaron problemas de validación.",
    )

    html = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>FincaData Pro - Dashboard</title>
  <style>
    :root {{
      --bg: #0f172a;
      --card: #111827;
      --card-soft: #1f2937;
      --text: #e5e7eb;
      --muted: #9ca3af;
      --accent: #22c55e;
      --accent-2: #38bdf8;
      --warning: #f59e0b;
      --danger: #ef4444;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: radial-gradient(circle at top left, #1e3a8a 0, var(--bg) 35%, #020617 100%);
      color: var(--text);
    }}
    header {{
      padding: 40px 24px 24px;
      max-width: 1180px;
      margin: auto;
    }}
    .eyebrow {{ color: var(--accent); text-transform: uppercase; letter-spacing: 2px; font-size: 13px; font-weight: bold; }}
    h1 {{ margin: 10px 0; font-size: clamp(32px, 5vw, 56px); line-height: 1; }}
    .subtitle {{ color: var(--muted); font-size: 18px; max-width: 780px; }}
    main {{ max-width: 1180px; margin: auto; padding: 24px; }}
    .grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }}
    .card {{ background: rgba(17, 24, 39, .86); border: 1px solid rgba(255,255,255,.08); border-radius: 20px; padding: 20px; box-shadow: 0 20px 50px rgba(0,0,0,.25); }}
    .metric {{ font-size: 30px; font-weight: bold; margin: 8px 0; }}
    .label {{ color: var(--muted); font-size: 14px; }}
    .section {{ margin-top: 18px; }}
    .two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
    .bar-row {{ display: grid; grid-template-columns: 90px 1fr 70px; gap: 10px; align-items: center; margin: 12px 0; }}
    .bar-bg {{ background: var(--card-soft); border-radius: 999px; height: 18px; overflow: hidden; }}
    .bar {{ height: 100%; border-radius: 999px; background: linear-gradient(90deg, var(--accent), var(--accent-2)); }}
    ul {{ padding-left: 20px; }}
    li {{ margin: 8px 0; }}
    .pill {{ display:inline-block; padding: 6px 10px; border-radius: 999px; background: rgba(34,197,94,.15); color: #86efac; font-size: 13px; }}
    footer {{ color: var(--muted); text-align: center; padding: 30px; }}
    @media (max-width: 900px) {{ .grid, .two {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <header>
    <div class="eyebrow">Dashboard generado automáticamente</div>
    <h1>🚜 Mi Finca Control</h1>
    <p class="subtitle">Sistema inteligente de monitoreo agrícola. Visualiza en tiempo real el rendimiento de tus cosechas y toma decisiones informadas para optimizar tu producción.</p>
    <span class="pill">Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>
  </header>

  <main>
    <section class="grid">
      <div class="card"><div class="label">Total leche</div><div class="metric">{analisis.total_leche:.1f} L</div></div>
      <div class="card"><div class="label">Promedio leche</div><div class="metric">{analisis.promedio_leche:.1f} L</div></div>
      <div class="card"><div class="label">Total maíz</div><div class="metric">{analisis.total_maiz:.1f} kg</div></div>
      <div class="card"><div class="label">Promedio maíz</div><div class="metric">{analisis.promedio_maiz:.1f} kg</div></div>
    </section>

    <section class="two section">
      <div class="card">
        <h2>🥛 Producción diaria de leche</h2>
        {barras_leche}
      </div>
      <div class="card">
        <h2>🌾 Rendimiento diario de maíz</h2>
        {barras_maiz}
      </div>
    </section>

    <section class="two section">
      <div class="card">
        <h2>Lectura técnica</h2>
        <p><strong>Tendencia de leche:</strong> {analisis.tendencia_leche}</p>
        <p><strong>Tendencia de maíz:</strong> {analisis.tendencia_maiz}</p>
        <p><strong>Mayor leche:</strong> {analisis.max_leche_dia} ({analisis.max_leche_valor:.1f} L)</p>
        <p><strong>Menor leche:</strong> {analisis.min_leche_dia} ({analisis.min_leche_valor:.1f} L)</p>
      </div>
      <div class="card">
        <h2>Alertas</h2>
        {alertas_html}
      </div>
    </section>

    <section class="section card">
      <h2>Problemas de validación</h2>
      {problemas_html}
    </section>
  </main>
  <footer>FincaData Pro - Artefacto del entorno - Semana 12</footer>
</body>
</html>"""

    ruta.write_text(html, encoding="utf-8")
    return ruta


def construir_barras(registros: list[RegistroProduccion], campo: str, maximo: float) -> str:
    """Construye barras HTML proporcionales al valor máximo."""
    partes: list[str] = []
    for registro in registros:
        valor = getattr(registro, campo)
        porcentaje = 0 if maximo == 0 else (valor / maximo) * 100
        unidad = "L" if campo == "leche_litros" else "kg"
        partes.append(
            f'<div class="bar-row"><span>{registro.dia}</span>'
            f'<div class="bar-bg"><div class="bar" style="width:{porcentaje:.1f}%"></div></div>'
            f'<span>{valor:.1f} {unidad}</span></div>'
        )
    return "\n".join(partes)


def construir_lista(items: list[str], mensaje_vacio: str) -> str:
    """Convierte una lista de textos en una lista HTML."""
    if not items:
        return f"<p>{mensaje_vacio}</p>"
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"
