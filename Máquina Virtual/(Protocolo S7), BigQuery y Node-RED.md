# 📊 Integración: Leer datos de PLC (Protocolo S7) hacia Google BigQuery vía Node-RED

Este documento describe el procedimiento para capturar datos de un PLC (usando el protocolo S7) mediante Node-RED, procesar las señales y almacenarlas en una tabla de Google BigQuery para su posterior análisis o visualización.

---

## 🏗️ Arquitectura de la Solución

El flujo consiste en cuatro etapas principales:
1. **Conexión PLC:** Lectura de variables desde un PLC S7.
2. **Procesamiento:** Transformación de los datos a formato JSON.
3. **Ingestión:** Envío de los datos procesados a Google BigQuery.
4. **Visualización:** (Opcional) Uso de Grafana para consultar BigQuery.

---

## 🛠️ Procedimiento Paso a Paso

### 1. Configuración de la conexión al PLC (Protocolo S7)
Para leer los datos del PLC (como `Válvula`, `SP` o `RPM`), se utiliza el nodo `s7 in` en Node-RED:
* **Endpoint:** Se configura el nodo `s7 endpoint` con la dirección IP del PLC (`192.168.200.10`), puerto 102, y los valores de Rack/Slot (típicamente 0/1 para S7-1200/1500).
* **Modo:** Se utiliza el modo "Single variable" para capturar una dirección específica (ej. `QW100` para la válvula).
* **Optimización:** Se recomienda activar "Emit only when value changes (diff)" para reducir el tráfico de red innecesario.

### 2. Procesamiento de datos en Node-RED
Una vez capturado el valor del PLC, se pasa por un nodo de **función** para estructurar el mensaje antes de enviarlo a la nube:
* **Generación de Timestamp:** Se crea un campo `FechayHora` usando `new Date().toISOString()`.
* **Formateo JSON:** Se construye el objeto requerido por BigQuery:
  ```json
  {
    "FechayHora": "...",
    "SP": ...,
    "RPM": ...,
    "Valvula": ...
  }
  ```
* **Payload:** Este objeto se asigna al `msg.payload` para el nodo de inserción.

### 3. Inserción en Google BigQuery
* Se utiliza el nodo `bigquery insert`.
* Se requiere configurar las credenciales de Google Cloud (archivo JSON de cuenta de servicio).
* El nodo insertará automáticamente las filas en el Dataset y Tabla definidos (ej. `Datos.PLC`).

### 4. Verificación
* Se monitorea la salida en el nodo `debug` para asegurar que el formato JSON sea correcto.
* Se verifica en la consola de Google BigQuery ejecutando `SELECT * FROM `dataset.table` LIMIT 1000` para confirmar que los datos se están registrando cronológicamente.

---

## 💡 Recomendaciones Técnicas
* **Intervalos:** En el nodo `inject` inicial (o en el ciclo de lectura del PLC), asegúrate de establecer un tiempo de muestreo adecuado para tu proceso (ej. 1s - 3s).
* **Seguridad:** Asegúrate de restringir los permisos de la cuenta de servicio de Google Cloud solo a "BigQuery Data Editor" y "BigQuery Job User" por seguridad.
