# Seaborn 📊

```python

# Gráfico de Área

plt.figure(figsize=(10, 6))
plt.style.use("ggplot")

sns.lineplot(x='petal_length', y='petal_width', data=iris)

plt.title('Gráfico de Área')
plt.xlabel('Largo del pétalo')
plt.ylabel('Ancho del pétalo')

plt.show()

# Gráfico de Barras Apiladas

plt.figure(figsize=(10, 6))

sns.barplot(x='species', y='sepal_length', hue='sepal_width', data=iris, errorbar=None)

plt.title('Gráfico de Barras Apiladas (por Especie)')
plt.xlabel('Especies')
plt.ylabel('Largo del sépalo')

plt.legend(title='Ancho del sépalo', loc='upper right')

plt.show()

# Gráfico de Caja y Bigotes

plt.figure(figsize=(10, 6))

sns.boxplot(x='species', y='petal_length', data=iris)

plt.title('Gráfico de Caja y Bigotes (Petal Length por Especie)')
plt.xlabel('Especies')
plt.ylabel('Petal Length')

plt.show()

# Gráfico de dispersión

tips = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', hue='day' ,data=tips)

# Mostrar el gráfico
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.title('Gráfico de Dispersión')

plt.legend(title="Almuerzo / Cena")

plt.show()

# Distribución (Histograma/barras)

sns.histplot(data=tips['total_bill'], bins=10)
​
# Mostrar el gráfico
plt.xlabel('Total de la cuenta')
plt.ylabel('Frecuencia')
plt.title('Gráfico de Distribución (Histograma)')
​
plt.show()

# Densidad de distribución

# Crear el gráfico de densidad (kde)
sns.kdeplot(data=tips['total_bill'], fill=True)
​
# Mostrar el gráfico
plt.xlabel('Total de la cuenta')
plt.ylabel('Densidad')
plt.title('Gráfico de Densidad (KDE)')
​
plt.show()

# Jointplot - Diagrama de dispersión topográfico
sns.jointplot(x="total_bill",y="tip",kind="kde",data=tips)
# Mostrar el gráfico
​
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.show()

```
