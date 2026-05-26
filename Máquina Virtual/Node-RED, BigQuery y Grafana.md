# Guía Detallada: Integración de Node-RED con Google BigQuery 🌐☁️

Este documento describe el procedimiento técnico para conectar el flujo de datos desde un entorno industrial (IOT2050) hasta la nube de Google BigQuery utilizando **Node-RED**.

## 1. Arquitectura del Sistema 🏗️
La solución implementa una arquitectura de *Edge Computing*:
* **Origen:** Datos provenientes de un PLC S7-1200.
* **Procesamiento:** Un dispositivo Siemens IOT2050 ejecutando Node-RED sobre Debian Linux.
* **Destino:** Google BigQuery (Data Warehouse en la nube).

## 2. Procedimientos de Configuración ⚙️

### A. Preparación del Entorno (Node-RED)
1.  **Instalación de Nodos:** Se requiere la instalación de paletas adicionales dentro de Node-RED, específicamente los nodos de `node-red-contrib-bigquery` para interactuar con la API de Google.
2.  **Gestión de Credenciales:** Es imperativo cargar el archivo JSON generado en la consola de Google Cloud (IAM) dentro del nodo de configuración de BigQuery. Este archivo contiene la clave privada y el ID del proyecto necesarios para la autenticación segura.

### B. Diseño del Flujo en Node-RED
1.  **Inyección de Datos:** Se definen nodos de entrada (pueden ser nodos S7 para lectura de PLC o nodos de inyección manual/temporizada para pruebas).
2.  **Transformación (Función):** Se utiliza un nodo de `function` para estructurar los datos crudos en un objeto JSON compatible con el esquema de la tabla de BigQuery.
    * *Ejemplo de estructura:* `{"FechayHora": "...", "Temperatura": 25.0, ...}`
3.  **Envío a la Nube:** El nodo de BigQuery recibe el objeto JSON y ejecuta la operación de inserción (`insert_rows_json`) en la tabla destino.

### C. Verificación y Monitoreo
1.  **Manejo de Errores:** Es crucial conectar un nodo `debug` a la salida de error del nodo de BigQuery para monitorear posibles fallos de autenticación, esquema inválido o límites de cuota excedidos.
2.  **Validación en Consola:** Finalmente, se verifica mediante la consola web de Google BigQuery que los datos se están poblando correctamente en la tabla objetivo mediante sentencias `SELECT *`.

---
*Este resumen técnico detalla los pasos críticos para lograr una integración exitosa entre el Edge industrial y la nube.*

# 📊 Integración de Node-RED, BigQuery y Grafana

Este documento detalla el flujo de trabajo para capturar datos de un PLC, almacenarlos en Google BigQuery utilizando Node-RED y posteriormente visualizarlos en tiempo real en Grafana.

---

## 🏗️ Arquitectura del Sistema

1.  **Fuente de datos:** PLC (Programmable Logic Controller).
2.  **Middleware:** **Node-RED** se encarga de la lógica de inyección y el envío de datos.
3.  **Almacenamiento:** **Google BigQuery** actúa como la base de datos centralizada.
4.  **Visualización:** **Grafana** consulta BigQuery para mostrar gráficas en tiempo real.

---

## 🛠️ Procedimientos Detallados

### 1. Ingestión de datos con Node-RED
En la configuración de Node-RED:
* Se utiliza un nodo **inject** configurado para ejecutarse a intervalos regulares (ej. cada 3 segundos).
* Se emplea un nodo para insertar los datos en una tabla específica dentro de **BigQuery**.
* El flujo asegura que los valores de `FechayHora`, `SP`, `RPM` y `Valvula` se registren correctamente.

### 2. Almacenamiento en BigQuery
Los datos se almacenan en una tabla denominada `Datos.PLC`. La estructura permite consultas temporales, esenciales para la visualización de series de tiempo en Grafana.

### 3. Visualización en Grafana
La integración se realiza configurando a **BigQuery** como "Data Source" en Grafana:
* **Creación de Panel:** Se selecciona el tipo de visualización *Time series*.
* **Consulta (Query):** Se mapea la columna `FechayHora` al eje X (tiempo) y las columnas `RPM` y `Valvula` al eje Y.
* **Estilos:** Se ajustan las opciones de visualización (ej. *Line interpolation*, *Fill opacity*) para mejorar la legibilidad de la gráfica, permitiendo comparar el comportamiento de las RPM y la válvula a lo largo del tiempo.

---

## 💡 Notas de Configuración
* **Intervalo:** Ajustado en Node-RED a 3 segundos para una actualización constante.
* **Consultas:** En Grafana, es crucial ordenar los datos correctamente (`ORDER BY 1 DESC` o similar) para asegurar que el gráfico muestre la evolución temporal sin errores.
* **Estética:** Se recomienda el uso de *Fill opacity* y colores distintos para diferenciar las series de datos.

