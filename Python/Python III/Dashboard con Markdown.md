# Dashboard Mínimo

```python

from dash import Dash, html
​
app = Dash(__name__)
​
app.layout = html.Div([
    html.H1('¡Hola, mundo!'),
])
​
if __name__ == '__main__':
    app.run(debug=True)
    # Otras opciones
    # host -> ip. Default localhost. host="0.0.0.0" significa accesible desde cualquier ip
    # port -> puerto. default 8050

```

# Dashboard con Markdown

```text
from dash import Dash, html, dcc
​
app = Dash(__name__)
​
markdown_text = '''
```


Las aplicaciones Dash pueden escribirse en Markdown.
​
Dash utiliza la especificación de Markdown 
de [CommonMark](http://commonmark.org/).
​
¡Mirá su [Tutorial de Markdown en 60 segundos](http://commonmark.org/help/) 
si es la primera vez que te introducís en Markdown!
​

# Hay títulos
## de distintos
### tamaños
​
- listas
- sin
- numeros
​
1. listas
2. con 
3. números
​

# Hasta bloques de código!

```python

print("Podemos escribir cualquier bloque de código ")

app.layout = html.Div([
    dcc.Markdown(children=markdown_text, style={"font-family":"system-ui"})
])
​
if __name__ == '__main__':
    app.run(debug=True)
```
