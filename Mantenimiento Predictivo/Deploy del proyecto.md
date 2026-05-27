# 🚀 Guía de Configuración y Despliegue de Palantir WebApp ⚙️

Esta guía contiene los pasos necesarios para configurar el entorno, desplegar la base de datos, ejecutar el proceso ETL y entrenar los modelos de Machine Learning para el mantenimiento predictivo.

---

## 🔗 Referencias y Repositorio 📦

* **🌐 Repositorio GitHub:** [palantir_webapp](https://github.com/carlosrosan/palantir_webapp)
* **🎥 Contexto:** A continuación, se detallan las referencias de definiciones mencionadas en el video instructivo.

---

## 🛠️ Requisitos Previos e Instalación 💻

### 🐍 1. Instalar Python
1. Descargue el instalador oficial desde [python.org](https://www.python.org/downloads/) (versión **3.8 o superior** recomendada). 📥
2. Durante la instalación en Windows, asegúrese de marcar la casilla **“Add Python to PATH”** 📌.
3. Compruebe que la instalación fue exitosa abriendo una terminal y ejecutando:

```

```text
Archivo generado exitosamente: guia_despliegue_palantir_webapp.md

```bash
   python --version
   pip --version

```

### 📝 2. Instalar Visual Studio Code (VS Code)

1. Descargue el editor desde [code.visualstudio.com](https://code.visualstudio.com/). 📦

### 🐙 3. Instalar GitHub Desktop y Clonar el Repositorio

1. Descargue e instale [GitHub Desktop](https://desktop.github.com/). 💾
2. Inicie sesión con su cuenta de GitHub (o cree una nueva si no la tiene). 🔐
3. **Clonar el repositorio:**
* Vaya a `File` → `Clone repository…` 📂
* Elija la pestaña de URL e introduzca la dirección del proyecto o busque el repositorio remoto del curso.
* Seleccione una ruta o carpeta local de destino (por ejemplo, `Documents` o su espacio de trabajo habitual).


4. Abra la carpeta clonada dentro de VS Code (`File` → `Open Folder`). 🔍

### 🐬 4. Instalar MySQL y MySQL Workbench

1. **MySQL Server:** Descargue el instalador desde [enlace sospechoso eliminado] (se recomienda el *MySQL Installer para Windows* que incluye de forma centralizada el servidor y las herramientas adicionales). ⚡
2. Durante el asistente de instalación, defina una contraseña segura para el usuario administrador `root` y **anótela en un lugar seguro** 🔑.
3. **MySQL Workbench:** Instálelo a través del mismo instalador o de forma independiente para contar con una interfaz gráfica que le permita ejecutar scripts SQL y administrar tablas. 📊
4. Compruebe que el servicio local de MySQL se encuentra en ejecución y que puede conectarse de forma exitosa a `localhost` a través del puerto por defecto **3306** 🚪.

---

## 🔌 Configuración del Entorno de Python 📦

Para instalar todas las librerías y dependencias necesarias para el proyecto, sitúese en la raíz del repositorio clonado desde su terminal y ejecute:

```bash
pip install -r requirements.txt

```

🎨 *Consejo: Se recomienda realizar este paso dentro de un entorno virtual de Python (venv).*

---

## 🗄️ Despliegue de la Base de Datos (Scripts SQL) 📊

Ejecute los scripts estructurados en el siguiente **orden estricto** utilizando MySQL Workbench, la línea de comandos de mysql, o su herramienta de administración de preferencia:

| 🔢 Orden | 📄 Archivo | 📝 Descripción |
| --- | --- | --- |
| **1** | `deployment/01_create_tables.sql` | Crea la base de datos `palantir_maintenance` y define todas las tablas y esquemas necesarios. |
| **2** | `deployment/02_insert_sample_data.sql` | Inserta el conjunto de datos de ejemplo (activos, telemetría de sensores, fallas, órdenes de trabajo, etc.). |

### 💻 Ejemplo de despliegue por Línea de Comandos

Abra su terminal y ejecute los siguientes comandos (el sistema le solicitará la contraseña de `root` definida previamente):

```bash
mysql -u root -p < deployment/01_create_tables.sql
mysql -u root -p < deployment/02_insert_sample_data.sql

```

> ⚠️ **Nota Importante sobre Credenciales:** Las credenciales configuradas por defecto en el código del proyecto asumen el usuario `root` y la contraseña estándar. Si utilizó una contraseña diferente, un puerto distinto o configuró otro usuario, recuerde ajustar estos valores en el archivo de configuración del sistema: `palantir_webapp/settings.py`.

---

## ⚙️ Generación del Dataframe para Entrenamiento (Proceso ETL) 🔄

El script encargado del procesamiento de datos `ETL/faliure_probability_dataframe.py` realiza la extracción de la información histórica alojada en MySQL (lecturas continuas de sensores, registros de eventos de fallas, etc.), realiza las transformaciones y consolida la tabla final `faliure_probability_base`. Esta tabla contendrá **una fila por activo y por día**, calculando las características (*features*) indispensables para los modelos de clasificación de Machine Learning.

1. Configure las variables de entorno o los parámetros de conexión dentro del archivo `.env` o directamente en el script según las indicaciones de su sesión (especifique `host`, `usuario`, `contraseña` y la base de datos `palantir_maintenance`). 🌐

2. Ejecute el script desde la terminal:

```bash
python ETL/faliure_probability_dataframe.py

```

3. **Validación:** Ingrese a MySQL Workbench y verifique mediante una consulta rápida que la tabla `faliure_probability_base` se haya poblado con registros de manera correcta. ✅

---

## 🤖 Entrenamiento de Modelos de Inteligencia Artificial (Notebook) 🧠

Abra en VS Code (asegurándose de tener la extensión de Jupyter instalada) o mediante un servidor Jupyter Notebook clásico el siguiente archivo:

📂 `Ingelearn_curso_mtto_predictivo/02_modelos_clasificacion.ipynb`

### 🔄 Flujo interno del Notebook:

* **💾 Carga de datos:** Consume la información histórica procesada en la tabla estructurada `faliure_probability_base`.
* **🧹 Preparación:** Realiza la división de características predictoras (*features*) y define de forma clara la variable objetivo (*target*) denominada `faliure`.
* **🌲 Entrenamiento y Evaluación:** Entrena algoritmos avanzados de clasificación (como *Árboles de Decisión* y *LightGBM*) y evalúa sus métricas de rendimiento (Precisión, Recall, F1-Score).

*💡 Recuerde ejecutar las celdas de forma secuencial únicamente después de haber completado exitosamente la carga de la base de datos y la ejecución del script ETL.*

---

## 📁 Estructura Relevante del Repositorio 📂

A continuación se detalla la ubicación de los componentes críticos dentro del árbol del proyecto:

```text
.
├── 📂 deployment/
│   ├── 📄 01_create_tables.sql       # Esquema y estructura de la base de datos
│   └── 📄 02_insert_sample_data.sql  # Datos históricos simulados de ejemplo
├── 📂 ETL/
│   └── 🐍 faliure_probability_dataframe.py  # Pipeline ETL hacia la tabla de ML
├── 📂 Ingelearn_curso_mtto_predictivo/
│   └── 📓 02_modelos_clasificacion.ipynb    # Notebook de entrenamiento de IA
└── 📄 requirements.txt               # Lista de dependencias del entorno Python

```

---

## 📋 Diccionario de Tablas de la Base de Datos 🗃️

* **🏭 `assets`:** Catálogo e información de los activos físicos de la planta.
* **📟 `plc_sensor_readings`:** Registro histórico de telemetría y lecturas de sensores provenientes de los PLC (presión, temperatura, vibración, etc.).
* **🚨 `assets_faliures`:** Bitácora histórica con los registros de fallas documentadas en los equipos.
* **🎯 `faliure_probability_base`:** Tabla unificada con las características estructuradas por día y por activo, generada por el proceso ETL para alimentar los modelos de Machine Learning.
* **💼 Otras tablas:** Tablas adicionales que contemplan la gestión operativa como órdenes de trabajo, asignación de tareas, catálogo de empleados, costos de mantenimiento, entre otros (detalladas en profundidad dentro de `01_create_tables.sql`).
