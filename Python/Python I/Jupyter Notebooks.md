# 📓 Jupyter Notebooks

Trabajar con **Jupyter Notebooks** es como tener un lienzo interactivo donde puedes mezclar código vivo, ecuaciones, visualizaciones y texto narrativo. Es la herramienta estándar en ciencia de datos y aprendizaje automático.


---

## 1. Instalación

Para empezar, necesitas tener Python instalado. La forma más común de obtener Jupyter es a través de **pip** o **Anaconda**.

* **Vía Pip:** Abre tu terminal y escribe:
`pip install notebook`
* **Vía Anaconda:** Si descargaste la suite Anaconda, Jupyter ya viene incluido. Solo busca "Jupyter Notebook" en tu menú de inicio.

---

## 2. Iniciar el Servidor

Una vez instalado, debes arrancar el entorno:

1. Abre la terminal o símbolo del sistema.
2. Navega hasta la carpeta donde quieras guardar tus proyectos.
3. Escribe el comando: `jupyter notebook`

Esto abrirá automáticamente una pestaña en tu navegador web (usualmente en la dirección `http://localhost:8888`).

---

## 3. Crear tu primera Libreta

En la interfaz del navegador:

1. Haz clic en el botón **"New"** (arriba a la derecha).
2. Selecciona **"Python 3 (ipykernel)"**.
3. ¡Listo! Se abrirá una pestaña nueva con un archivo `.ipynb` en blanco.

---

## 4. Entender la Interfaz: Celdas y Modos

Jupyter funciona mediante **celdas**. Hay dos tipos principales que debes conocer:

* **Celdas de Código:** Donde escribes Python. Al ejecutarlas, el resultado aparece justo debajo.
* **Celdas Markdown:** Donde escribes texto con formato, títulos, listas o incluso fórmulas en $LaTeX$.

### Los dos estados de una celda:

1. **Modo Edición (Borde verde/azul):** Estás escribiendo dentro de la celda. Se activa pulsando `Enter`.
2. **Modo Comando (Borde gris):** Estás interactuando con la estructura de la libreta. Se activa pulsando `Esc`.

---

## 5. Atajos de Teclado (Para trabajar como un pro)

No necesitas el ratón si dominas estos comandos en **Modo Comando**:

| Acción | Tecla |
| --- | --- |
| **Ejecutar celda** | `Shift + Enter` |
| **Crear celda arriba** | `A` (Above) |
| **Crear celda abajo** | `B` (Below) |
| **Convertir a Markdown** | `M` |
| **Convertir a Código** | `Y` |
| **Borrar celda** | `D + D` (dos veces) |

---

## 6. Flujo de Trabajo Típico

El poder de Jupyter reside en la **ejecución iterativa**:

1. **Importa tus librerías** en la primera celda (Pandas, Matplotlib, etc.).
2. **Carga tus datos** y visualiza las primeras filas.
3. **Crea gráficos** y ajusta el código sin tener que reiniciar todo el programa; solo ejecutas la celda que modificaste.
4. **Anota tus hallazgos** usando las celdas Markdown para que otros (o tu "yo" del futuro) entiendan qué hiciste.

---

## 7. Guardar y Exportar

Jupyter guarda automáticamente tus cambios, pero puedes forzarlo con `Ctrl + S`.
Si necesitas compartir tu trabajo con alguien que no usa Jupyter, ve a **File > Download as** y elige **PDF** o **HTML**. Se verá como un informe profesional.
