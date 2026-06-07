""" Bibliotecas necesarias
Instalar todas con pip install <paquete>
pandas, numpy, seaborn, scikit-learn, xgboost"""

import pandas as pd

df = pd.read_csv("PetroleoArg.csv")
df.head()
columnas_interesantes=["empresa","anio","mes","provincia","cantidad","indice_tiempo","areayacimiento","concepto","cuenca"]
datos = df[columnas_interesantes]
datos.head()
GolfoSanJorge = datos.query("cuenca == 'GOLFO SAN JORGE'")
GolfoSanJorge_fl = GolfoSanJorge.groupby("indice_tiempo").mean()
GolfoSanJorge_fl.shape

#Nota: Si sale el error TypeError: agg function failed [how->mean,dtype->object] deben agregar numeric_only=True dentro de los paréntesis del mean()
#Esto es por que una nueva actualización de la biblioteca hizo que el método mean haga promedio de todo el dataset, no solamente de los campos numéricos (como es nuestro caso)

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(14,8))
sns.set(font_scale=0.5)
ax = sns.lineplot(x="indice_tiempo",y="cantidad",data=GolfoSanJorge_fl)
plt.xlabel('Año')
plt.ylabel('Producción de petróleo real en Golfo San Jorge')
plt.xticks(rotation=45)
plt.show()
df_ultimos_10 = GolfoSanJorge_fl.iloc[-10:]
df_sin_ultimos_10 = GolfoSanJorge_fl.iloc[:-10]
from sklearn.model_selection import train_test_split
import xgboost as xgb
GolfoSanJorge_fl.index = pd.to_datetime(GolfoSanJorge_fl.index, format="%Y-%m")
GolfoSanJorge_fl
X = df_sin_ultimos_10.iloc[:, :-1].values
y = df_sin_ultimos_10.iloc[:, -1].values
X_valid = df_ultimos_10.iloc[:, :-1].values
y_valid = df_ultimos_10.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Tamaño de X_train:", X_train.shape)
print("Tamaño de y_train:", y_train.shape)
print("Tamaño de X_test:", X_test.shape)
print("Tamaño de y_test:", y_test.shape)

#Nota:En las versiones nuevas de XGBoost (>2.0.0), los parámetros eval_metric y early_stopping_rounds no van en el método fit, sino en la definición del modelo.
modelo = xgb.XGBRegressor(
    n_estimators = 500,
    objective='reg:squarederror',
    random_state=42,
    eval_metric='rmse',
    early_stopping_rounds=9
)
modelo.fit(
    X_train, y_train, 
    eval_set=[(X_test, y_test)], 
    verbose=True
)
y_pred2 = modelo.predict(X_valid)
y_pred_df = pd.DataFrame(y_pred2, columns=["cantidad_pred"])
y_pred_df.index = df_ultimos_10.index
y_pred_df
y_pred_df.index = pd.to_datetime(y_pred_df.index, format="%Y-%m")
df_compare = pd.concat([GolfoSanJorge_fl, y_pred_df], axis=1)
df_compare
fig, ax = plt.subplots(figsize=(15,6))

df_compare['cantidad'].plot(ax=ax, label='Valores Reales')
df_compare['cantidad_pred'].plot(ax=ax, label='Predicción')

ax.set_xlabel('Fecha')
ax.set_ylabel('Cantidad')
ax.set_title('Comparación de valores reales y predicción')

ax.legend()

plt.show()
