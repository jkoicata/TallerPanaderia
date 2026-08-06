# Analisis de Ventas Panadería ☕

Predicción de ventas diarias de una panadería según la temperatura, el día de la semana y el promedio de ventas.

## Instalación y ejecución

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/train.py
```

## Estructura

```
TallerPanaderia/
├── data/               # Datos crudos (no se versionan en proyectos reales)
│   └── datos_panaderia.csv
├── src/
│   ├── datos.py         # Carga y validación de datos
│   └── train.py        # Entrenamiento y evaluación
├── requirements.txt    # Dependencias con versiones fijadas
└── README.md

# Decisiones

## Datos Faltantes
Se hizo analisis de datos faltantes evidenciando que en % de datos faltantes de la columna temperatura representaba más de un
10% de los datos totales, porcentaje que consideramos elevado para eliminar los registros, por lo anterior, se decidió hacer un promedio de los datos de temperatura y rellenar los datos faltantes con el mismo.

## Marcación Fin de Semana

df["es_finde"][i] = 1 crea un chained assignment que puede hacer que los datos no se actualicen correctamente en el dataframe original que cargamos (datos panaderia), por eso modificamos esta línea de código usando el método .isin está alineada directamente con el index del dataframe sin necesidad de dos operaciones de indexación diferentes
