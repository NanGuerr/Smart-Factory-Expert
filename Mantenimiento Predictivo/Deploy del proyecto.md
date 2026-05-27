¿Como hacer ?

A continuación, las referencias de definiciones mencionadas en el video.

https://github.com/carlosrosan/palantir_webapp



Repo GitHub



Instalar Python:



1. Descargue el instalador oficial desde [python.org](https://www.python.org/downloads/) (versión **3.8 o superior** recomendada).

2. Durante la instalación en Windows, marque “Add Python to PATH”.

3. Compruebe en una terminal:

   bash

   python --version

   pip --version



Instalar Visual Studio Code (VS Code):



1. Descargue VS Code desde [code.visualstudio.com](https://code.visualstudio.com/).



Instalar de GitHub Desktop y clonado del repositorio:



1. Descargue [GitHub Desktop](https://desktop.github.com/).

2. Inicie sesión con su cuenta de GitHub (o cree una).

3. Clonar el repositorio:

   - File → Clone repository…

   - Elija la URL del proyecto o el repositorio remoto del curso.

   - Seleccione una carpeta local (por ejemplo `Documents` o su carpeta de trabajo).

4. Abra la carpeta clonada en VS Code (File → Open Folder).



Instalar de MySQL y MySQL Workbench:



1. MySQL Server: descargue el instalador desde [MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/) (o el instalador MySQL Installer para Windows que incluye servidor y herramientas).

2. Durante la instalación, defina una contraseña para el usuario `root` y anótela.

3. MySQL Workbench: instálelo desde el mismo instalador o por separado para poder ejecutar scripts SQL y revisar tablas de forma gráfica.

4. Compruebe que el servicio MySQL está en ejecución y que puede conectarse a `localhost` puerto 3306 (por defecto).



Entorno Python del proyecto (dependencias)



En la raíz del repositorio clonado:

pip install -r requirements.txt





Despliegue de la base de datos (scripts SQL)



Ejecute los scripts en este orden (desde MySQL Workbench, línea de comandos mysql, o la herramienta que prefiera):

Orden Archivo Descripción

 - 1. deployment/01_create_tables.sql Crea la base de datos palantir_maintenance y todas las tablas necesarias.

 - 2. deployment/02_insert_sample_data.sql Inserta datos de ejemplo (activos, sensores, fallas, órdenes, etc.).

Ejemplo por línea de comandos (ajuste usuario y contraseña):

   mysql -u root -p < deployment/01_create_tables.sql

   mysql -u root -p < deployment/02_insert_sample_data.sql

Nota: Las credenciales por defecto en el proyecto suelen ser usuario root y contraseña según su instalación. Ajuste palantir_webapp/settings.py si usa otro usuario, contraseña o puerto.



Generación del dataframe para entrenamiento (ETL)



El script ETL/faliure_probability_dataframe.py lee datos de MySQL (lecturas de sensores, fallas, etc.) y rellena la tabla faliure_probability_base con una fila por activo y por día y las características necesarias para modelos de clasificación.

Configure las variables de entorno o los valores de conexión en el script / archivo .env según indique el curso (host, usuario, contraseña, base palantir_maintenance).



Ejecute:



python ETL/faliure_probability_dataframe.py



Verifique en MySQL Workbench que la tabla faliure_probability_base contiene registros.



Entrenamiento de modelos (notebook)



Abra en VS Code (o Jupyter) el notebook:



Ingelearn_curso_mtto_predictivo/02_modelos_clasificacion.ipynb



Este notebook:

 Carga datos desde faliure_probability_base

 Prepara características y la variable objetivo faliure

 Entrena modelos (por ejemplo árbol de decisión y LightGBM) y evalúa resultados 

 Ejecute las celdas en orden tras tener datos en la base y el ETL ejecutado correctamente.



Estructura relevante del repositorio

.

├── deployment/

│ ├── 01_create_tables.sql # Esquema de base de datos

│ └── 02_insert_sample_data.sql # Datos de ejemplo

├── ETL/

│ └── faliure_probability_dataframe.py # ETL → tabla faliure_probability_base

├── Ingelearn_curso_mtto_predictivo/

│ └── 02_modelos_clasificacion.ipynb # Entrenamiento de modelos

├── requirements.txt



Tablas de base de datos (referencia)



assets — Activos físicos

plc_sensor_readings — Lecturas de sensores PLC

assets_faliures — Registros de fallas

faliure_probability_base — Características diarias para ML (generada por el ETL)

Otras tablas de órdenes, tareas, empleados, costes, etc. (ver 01_create_tables.sql)
