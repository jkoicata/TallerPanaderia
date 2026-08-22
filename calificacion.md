# TallerPanaderia — Taller Semana 1: "Hazlo correr" 🥐

Repo: [github.com/jkoicata/TallerPanaderia](https://github.com/jkoicata/TallerPanaderia)

Rúbrica: Corre en máquina limpia (50% · 2.5 pts) · Calidad y estructura (30% · 1.5 pts) · Proceso en Git + README (20% · 1.0 pt) · Bonus (+0.2 máx si aplica). Escala final: 0–5.

**Nota final: 4.48 / 5.0**

| Corre limpio | Calidad/estructura | Git+README | Bonus |
|---|---|---|---|
| 2.35 / 2.5 | 1.05 / 1.5 | 0.95 / 1.0 | +0.13 |

---

### 1. Corre en máquina limpia — 2.35 / 2.5 ✅
Con Python 3.11 y 3.13 los 4 comandos exactos del enunciado corren sin problemas:

```
fecha                  str
dia_semana             str
temperatura_c      float64
precio_promedio      int64
ventas_unidades      int64
dtype: object
MAE: 18.708556977707115
listo!!
```

Falla con Python 3.10 (`pandas==3.0.2` no tiene versión compatible ahí), pero funciona en cualquier Python 3.11+ sin restricción de tope, algo razonablemente común hoy. El único descuento es porque el README no menciona ningún requisito de versión de Python, así que quien tenga 3.10 como intérprete por defecto no tiene ninguna pista de por qué falla. **(-0.15)**

### 2. Calidad y estructura — 1.05 / 1.5 ⚠️
**Bien:** `marcar_finde()` vectorizado con `.isin().astype(int)` (sin loops), columnas validadas con `ValueError` claro, `temperatura_c` se castea a numérico directamente vía `na_values=["SIN DATO"]` en `pd.read_csv()`, imputación con la media en vez de descartar filas.

**Se bajó nota por:**
- **No hay archivo `.gitignore`** — el enunciado lo pide explícitamente como parte de la estructura del entregable. **(-0.15)**
- **El archivo se llama `datos.py`, no `data.py`** como especifica la estructura exacta del enunciado. **(-0.1)**
- **`resumen_por_dia()` todavía usa `resumen.append(...)`**, el método de pandas eliminado en la versión 2.0 — es el mismo código del script original del practicante (el comentario de cabecera `# hecho por el practicante, no tocar` sigue intacto). No se llama desde `train.py`, así que no rompe el comando de calificación, pero si alguien ejecuta `python src/datos.py` directamente, truena con `AttributeError: 'DataFrame' object has no attribute 'append'`. El bug no se arregló, solo se evitó. **(-0.2)**

### 3. Proceso en Git + README — 0.95 / 1.0 ✅
11 commits que muestran progreso incremental real (`Estructura`, `Separar Train y Datos`, `Lectura de Datos`, `Función Entrenar Modelo`, `Funciones de Ventas y Fin de Semana`, `Requirements y limpieza de Datos`...) — supera el mínimo de 5, aunque los mensajes son breves. README con sección "Decisiones" que cubre tanto el manejo de datos faltantes como la razón técnica para evitar el chained assignment en `es_finde`.

**Se bajó nota por:**
- Igual que en el punto 1, las instrucciones de instalación no advierten que se necesita Python 3.11 o superior. **(-0.05)**

*(Nota aparte, sin descuento adicional: la sección "Decisiones" dice que los datos faltantes de `temperatura_c` son "más de un 10%" del total — en realidad son 7 de 90, ~7.8%. No cambia la conclusión (imputar en vez de descartar sigue siendo razonable), pero vale la pena revisar la cifra.)*

### Bonus — +0.13 de 0.2
1. **Validación de columnas** ✅: `cargar_datos()` valida columnas esperadas y lanza `ValueError` claro si falta alguna.
2. **Reporte de limpieza** ❌: no hay ningún print que reporte cuántos valores de `temperatura_c` fueron imputados ni por qué — `reemplazar_datos_faltantes()` lo hace en silencio.
3. **Sección "Decisiones" en el README** ✅: presente y cubre ambas decisiones técnicas relevantes.

### Resumen para el estudiante
Lo esencial funciona bien: la vectorización de `es_finde`, la validación de columnas y la decisión de imputar en vez de descartar están bien resueltas y explicadas. Para la próxima entrega: agreguen un `.gitignore`, nombren el archivo `data.py` (no `datos.py`) para que coincida exactamente con la estructura pedida, y sobre todo revisen `resumen_por_dia()` — todavía tiene el `.append()` del script original sin arreglar; si no lo van a usar, mejor quitarlo en vez de dejarlo roto. También sumaría imprimir cuántos datos se imputaron en la limpieza, y aclarar en el README que se necesita Python 3.11 o superior.
