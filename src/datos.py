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

    print(df.dtypes)
    return df

# resumen de ventas por dia de la semana
def resumen_por_dia(df):
    resumen = pd.DataFrame()
    for dia in df["dia_semana"].unique():
        sub = df[df["dia_semana"] == dia]
        resumen = resumen.append(
            {"dia": dia, "ventas_promedio": sub["ventas_unidades"].mean()},
            ignore_index=True,
        )
    print("--- resumen por dia ---")
    print(resumen)
    return resumen

# variable: es fin de semana?
def marcar_finde(df):
    df["es_finde"] = df["dia_semana"].isin(["sábado", "domingo"]).astype(int)
    return df

# imprimir resumen de ventas por dia de la semana
if __name__ == "__main__":
    df = cargar_datos()
    resumen_por_dia(df)

#datos faltantes en temperatura_por promedio, se puede reemplazar por la media de temperatura de los dias que si tienen datos.
def reemplazar_datos_faltantes(df):
    df["temperatura_c"] = df["temperatura_c"].fillna(df["temperatura_c"].mean())
    return df