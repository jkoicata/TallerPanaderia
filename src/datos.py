# analisis panaderia - version final FINAL (esta si funciona)
# hecho por el practicante, no tocar
import pandas as pd
from pathlib import Path


# Ruta relativa a la raíz del proyecto — funciona en cualquier máquina.
RUTA_DATOS = Path(__file__).parent.parent / "data" / "datos_panaderia.csv"

def cargar_datos(ruta: Path = RUTA_DATOS) -> pd.DataFrame:
    """Carga el CSV de ventas y valida los datos."""
    df = pd.read_csv(
        ruta,
        sep=";",
        encoding="latin1",
        na_values=["SIN DATO"],
    )

# resumen de ventas por dia de la semana
resumen = pd.DataFrame()
for dia in df["dia_semana"].unique():
    sub = df[df["dia_semana"] == dia]
    resumen = resumen.append(
        {"dia": dia, "ventas_promedio": sub["ventas_unidades"].mean()},
        ignore_index=True,
    )
print("--- resumen por dia ---")
print(resumen)

# variable: es fin de semana?
df["es_finde"] = 0
for i in range(len(df)):
    if df["dia_semana"][i] == "sábado" or df["dia_semana"][i] == "domingo":
        df["es_finde"][i] = 1


