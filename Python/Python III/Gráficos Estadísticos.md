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
```
