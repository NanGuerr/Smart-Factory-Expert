# 🎨 Estilos y CSS en Dashboards

## 1. Implementación de Estilos
* **Diccionarios de Estilo:** En Dash, se pasan como diccionarios de Python.
  - Ejemplo: `style={'backgroundColor': 'navy', 'color': 'white', 'padding': '10px'}`.
  - *Nota:* Las propiedades CSS que usan guiones (ej. `background-color`) se escriben en *camelCase* (`backgroundColor`).

## 2. Organización del Espacio (Layout)
* **Flexbox:** Ideal para alinear elementos en filas o columnas de forma dinámica.
  - `display: 'flex'` permite controlar la alineación (`justifyContent`, `alignItems`).
* **Grid:** Perfecto para dashboards complejos donde necesitas definir áreas específicas en la pantalla.

## 3. Frameworks CSS Recomendados
* **Dash Bootstrap Components (DBC):** Es el estándar de oro. Permite usar filas (`Row`) y columnas (`Col`) basadas en un sistema de 12 unidades, haciendo que el tablero se ajuste automáticamente al tamaño de cualquier monitor o tablet.
* **Estilos Externos:** Puedes cargar hojas de estilo desde servidores CDN para aplicar temas profesionales (ej. temas oscuros o minimalistas).

## 4. Mejores Prácticas
* **Consistencia:** Define una paleta de colores y úsala para todos los bordes, botones y encabezados.
* **Espaciado:** Utiliza `margin` y `padding` para evitar que los gráficos se vean amontonados. Un dashboard con "aire" (espacio en blanco) es mucho más legible.
* **Interactividad visual:** Cambia el estilo de un botón cuando el usuario pasa el mouse sobre él (`:hover`) para mejorar la retroalimentación visual.
El uso de **CSS (Cascading Style Sheets)** en dashboards (como Dash o herramientas similares) es fundamental para pasar de una interfaz funcional pero básica a una experiencia de usuario profesional, intuitiva y visualmente atractiva 🎨.

### 📝 Resumen Analítico

El estilo en los dashboards modernos se basa en dos enfoques principales:

1. **Estilos en Línea (Inline):** Pasar diccionarios directamente a los parámetros `style={...}` de los componentes. Es útil para ajustes rápidos y específicos.
2. **Hojas de Estilo Externas (CSS):** Vincular archivos `.css` o frameworks (como Bootstrap) a la aplicación. Esto permite mantener la consistencia visual en todo el tablero, definir tipografías, márgenes y esquemas de colores de forma centralizada.

La clave no es solo "hacerlo ver bonito", sino organizar el contenido mediante **Layouts (Flexbox/Grid)** para que el tablero sea responsivo y fácil de leer.


```css

Assets/estilos.css
body {
    background-color: slategrey;
    color:midnightblue;
    font-family:'Segoe UI';
}
​
/* el punto, significa que es una CLASE. Identificado por el parametro "className" */
​
.titulo {
    text-align: center;
}
​
label{ 
    margin-left: 20;
    vertical-align: top;
    font-weight: bold;
}
​
/* el # significa que es un ID, identifica cada elemento por su argumento "id" ej "id=selectora"*/
#selectora{
    display: flex;
}
​
input{
    margin: 3px;
}
​
/* Inicio estilos checkboxes */
  .checkbox-wrapper-2 input {
    appearance: none;
    background-color: #dfe1e4;
    border-radius: 72px;
    border-style: none;
    flex-shrink: 0;
    height: 20px;
    margin-left: 50px;
    margin-right: 10px;
    position: relative;
    width: 30px;
    top:6px;
    
  }
​
  .checkbox-wrapper-2 input::before {
    bottom: -6px;
    content: "";
    left: -6px;
    position: absolute;
    right: -6px;
    top: -6px;
  }
​
  .checkbox-wrapper-2 input,
  .checkbox-wrapper-2 input::after {
    transition: all 100ms ease-out;
  }
​
  .checkbox-wrapper-2 input::after {
    background-color: #fff;
    border-radius: 50%;
    content: "";
    height: 14px;
    left: 3px;
    position: absolute;
    top: 3px;
    width: 14px;
  }
​
  .checkbox-wrapper-2 input[type=checkbox] {
    cursor: default;
  }
​
  .checkbox-wrapper-2 input:hover {
    background-color: #c9cbcd;
    transition-duration: 0s;
  }
​
  .checkbox-wrapper-2 input:checked {
    background-color:greenyellow;
  }
​
  .checkbox-wrapper-2 input:checked::after {
    background-color: #2eb449;
    left: 13px;
  }
​
  .checkbox-wrapper-2 :focus:not(.focus-visible) {
    outline: 0;
  }
​
  .checkbox-wrapper-2 input:checked:hover {
    background-color: greenyellow;
  }
​
.rc-slider-mark-text{
    color:black
}
/* ----------- FIN estilos checkboxes ------------- */
  
/* textos y colores de la de la barra */
.rc-slider-mark-text-active{
  color:lawngreen
}
​
.rc-slider{
  color:black;
}
.rc-slider-track{
  background-color:mediumspringgreen;
}
.rc-slider-handle{
  border: #2eb449;
  background-color:mediumspringgreen;
}
​
/* Texto RPM */
​
#textoTur{
  color:crimson;
  text-shadow: 3px 3px 2px rgb(44, 6, 13) ;
  text-align: center;
  font-size: 50px;
  font-family:monospace;
}

```
