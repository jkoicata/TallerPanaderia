# analisis panaderia - version final FINAL (esta si funciona)
# hecho por el practicante, no tocar
import pandas as pd


print("cargando datos...")
df = pd.read_csv("C:\\Users\\practicante\\Desktop\\proyecto_panaderia\\datos_panaderia.csv")
print("datos cargados:", len(df), "filas")

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


