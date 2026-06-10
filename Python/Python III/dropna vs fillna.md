# 🛡️ Validación y Limpieza de Datos: `fillna` vs `dropna`

## 📝 Resumen Analítico
La limpieza de datos es la etapa más crítica en cualquier proyecto de ciencia de datos. Los archivos adjuntos detallan cómo manejar los **datos faltantes** (valores `NaN` o `None`), que son inevitables en bases de datos reales. Existen dos estrategias principales para tratarlos: **eliminar** los registros defectuosos o **imputar** (rellenar) valores faltantes.

---

## 🗑️ 1. `dropna()`: Eliminación de Datos Faltantes
El procedimiento de "borrado" se utiliza cuando los datos faltantes son irrelevantes, demasiado numerosos o cuando la integridad de la fila depende de esa información.

* **Función:** Elimina filas o columnas que contienen valores faltantes.
* **Comportamiento estándar:** Por defecto, `df.dropna()` eliminará cualquier fila que tenga al menos un `NaN`.
* **Procedimientos clave:**
    * `dropna(axis=0)`: Elimina filas con datos faltantes.
    * `dropna(axis=1)`: Elimina columnas con datos faltantes.
    * `dropna(how='all')`: Elimina solo si **toda** la fila o columna está vacía.
    * `dropna(subset=['ColumnaA'])`: Elimina filas únicamente si falta información en la columna especificada.

---

## 💉 2. `fillna()`: Imputación (Relleno) de Datos
A menudo, borrar datos es perjudicial (perdemos información valiosa en otras columnas). `fillna()` permite reemplazar los vacíos con valores estimados.

* **Función:** Sustituye los valores `NaN` con un valor específico.
* **Procedimientos clave:**
    * `fillna(0)`: Rellena todos los huecos con el número 0.
    * `fillna(df.mean())`: Rellena los huecos con el **promedio** de cada columna. Es la técnica más común para mantener la distribución estadística.
    * `fillna(method='ffill')`: *Forward fill*. Rellena el valor faltante con el valor anterior de la misma columna (muy útil en series temporales).
    * `fillna(method='bfill')`: *Backward fill*. Rellena el vacío con el valor siguiente.

---

## 🆚 Tabla Comparativa: ¿Cuál usar?

| Estrategia | Método | ¿Cuándo utilizarlo? |
| :--- | :--- | :--- |
| **Eliminar** | `dropna()` | Cuando faltan muy pocos datos o la información es irrecuperable. |
| **Imputar** | `fillna()` | Cuando necesitas mantener la estructura o el tamaño del dataset intacto. |


---

## ⚙️ Procedimiento General de Validación

1. **Detección:** Primero debemos saber cuántos datos faltan. 
   `df.isnull().sum()` devuelve el conteo de `NaN` por cada columna.
2. **Evaluación:** ¿Qué impacto tendrá borrar una fila?
3. **Decisión:**
   - Si la pérdida es mínima (< 5%): `dropna()`.
   - Si la columna es vital: `fillna()` (usando promedio, mediana o valor constante).
4. **Validación:** Volver a verificar con `df.isnull().sum()` para asegurar que el dataset quedó limpio.


El análisis de tus archivos confirma que estás trabajando en la fase más importante de la Ciencia de Datos: la **limpieza y validación**. 🛡️

Cuando trabajamos con datos reales, es común encontrar "huecos" (valores nulos llamados `NaN` o *Not a Number*). Las imágenes que enviaste explican cómo decidir entre destruir esa información o repararla. He compilado toda esta lógica técnica en el archivo `.md` adjunto.

### 📝 Resumen del Procedimiento

* **Detección 🔍:** Antes de limpiar, el primer paso es contar cuántos huecos tenemos usando `df.isnull().sum()`. Si no sabes cuántos faltan, no puedes decidir cómo borrarlos o rellenarlos.
* **`dropna()` (El Cirujano) 🗑️:** Es un método destructivo pero efectivo. Úsalo cuando una fila no tiene suficiente información para ser útil. Es ideal para limpiar dataset cuando los valores faltantes son insignificantes en cantidad.
* **`fillna()` (El Restaurador) 💉:** Es un método reconstructivo. Permite salvar datos reemplazando los huecos con el promedio de la columna (evitando sesgos estadísticos) o usando técnicas como *forward-fill* (copiar el valor anterior), que es excelente si estás trabajando con mediciones de sensores en el tiempo.

