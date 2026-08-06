from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error 
from datos import cargar_datos, marcar_finde,reemplazar_datos_faltantes

def entrenar_modelo():
    df=cargar_datos()
    reemplazar_datos_faltantes(df)
    marcar_finde(df)
    
    # entrenar el modelo
    X = df[["temperatura_c", "precio_promedio", "es_finde"]]
    y = df["ventas_unidades"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
 
    pred = modelo.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, pred))
    print("listo!!")
 
    return modelo

if __name__ == "__main__":
    entrenar_modelo()