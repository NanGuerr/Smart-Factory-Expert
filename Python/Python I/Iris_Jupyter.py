# Importamos las bibliotecas necesarias 
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos los datos y mostramos las primeras 5 líneas 
data = sns.load_dataset('iris')
data.head()

# Cuántas filas y columnas hay? 
filas, columnas = data.shape
print("Hay", filas, "filas y", columnas, "columnas")

# Ahora sí, graficamos la distribución
sns.kdeplot(data['petal_length'], fill=True)
plt.xlabel('Longitud del Pétalo')
plt.ylabel('Densidad')
plt.title('Distribución de la Longitud del Pétalo')
plt.show()
