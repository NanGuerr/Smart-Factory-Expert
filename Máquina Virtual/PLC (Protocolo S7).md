# 🚀 Extracción de Datos de PLC (Protocolo S7) a Google BigQuery con Node-RED 🏭☁️

Este documento técnico detalla el procedimiento paso a paso para leer variables de proceso desde un PLC Siemens utilizando el protocolo **S7**, procesarlas localmente en **Node-RED** y almacenarlas de forma masiva y estructurada en **Google BigQuery**.

---

## 🏗️ 1. Arquitectura General del Flujo

El intercambio de información sigue una topología industrial-to-cloud directa:
1. **Piso de Planta (PLC):** Contiene los registros de variables de control (`SP`, `RPM`, `Valvula`).
2. **Capa Middleware (Node-RED):** Actúa como cliente S7 para consultar el PLC y cliente API de Google para inyectar datos.
3. **Capa de Datos (BigQuery):** Repositorio analítico estructurado en la nube.

---

## 🔌 2. Configuración del Nodo S7 en Node-RED

Para establecer la comunicación con el autómata programable se utiliza el paquete `node-red-contrib-s7`.

### Paso A: Configuración del Endpoint (Conexión Física)
* **Dirección IP:** `192.168.200.10` (o la IP asignada a la interfaz Profinet del PLC).
* **Puerto:** `102` (Puerto estándar por defecto para la comunicación S7).
* **Rack & Slot:** * Para S7-1200 / S7-1500: Generalmente **Rack 0, Slot 1**.
  * Para S7-300 / S7-400: Generalmente **Rack 0, Slot 2**.

### Paso B: Mapeo de Variables
Dentro de la pestaña de variables del nodo de configuración, se deben dar de alta las direcciones de memoria correspondientes:
* **SP (SetPoint):** Ej. `DB1,REAL0` o dirección analógica de entrada.
* **RPM (Velocidad del motor):** Ej. `DB1,REAL4`.
* **Valvula (Apertura %):** Ej. `DB1,REAL8` o salidas correspondientes.

> ⚠️ **Nota Crítica de Seguridad de Siemens:** En la configuración del PLC (vía TIA Portal), la propiedad del bloque de datos (DB) debe tener desactivado el **"Optimized block access"** (Acceso optimizado al bloque) y se debe permitir el acceso **PUT/GET** en las propiedades de protección de la CPU.

---

## 🧠 3. Transformación de Datos (Nodo Función)

Los datos crudos del PLC llegan de manera independiente o en objetos planos. BigQuery requiere un formato JSON estructurado con tipos de datos compatibles. Se añade un nodo `function` intermedio con el siguiente código JavaScript:

```javascript
// Captura de datos provenientes del nodo S7
let sp = msg.payload.SP;
let rpm = msg.payload.RPM;
let valvula = msg.payload.Valvula;

// Creación de una marca de tiempo en formato ISO 8601 (Requerido por BigQuery para tipo TIMESTAMP)
let fechaHora = new Date().toISOString();

// Construcción del payload final estructurado por filas
msg.payload = {
    "FechayHora": fechaHora,
    "SP": parseFloat(sp),
    "RPM": parseFloat(rpm),
    "Valvula": parseFloat(valvula)
};

return msg;
```

---

## ☁️ 4. Ingestión en Google BigQuery

Para enviar los datos de manera nativa sin pasar por un SDK externo, se emplea el nodo `node-red-contrib-google-cloud` (específicamente el nodo **BigQuery Insert**).

1. **Autenticación:** Se vincula el archivo de credenciales de Google Cloud (`.json`) obtenido desde la sección de IAM (Cuentas de servicio) con el rol de **BigQuery Data Editor**.
2. **Project ID:** Identificador único de tu proyecto en GCP (ej. `dashboard-433218`).
3. **Dataset ID:** Nombre del conjunto de datos creado (ej. `Datos`).
4. **Table ID:** Nombre de la tabla destino (ej. `PLC`).

---

## 📊 5. Verificación en la Consola de BigQuery

Una vez desplegado el flujo en Node-RED (`Deploy`), se valida la llegada de datos en la consola de Google Cloud ejecutando una consulta SQL estándar:

```sql
SELECT 
  FechayHora, 
  SP, 
  RPM, 
  Valvula 
FROM 
  `dashboard-433218.Datos.PLC` 
ORDER BY 
  FechayHora DESC 
LIMIT 10;
```

### 📋 Muestra Esperada en Tabla de Resultados:
| Fila | FechayHora | SP | RPM | Valvula |
|------|------------|----|-----|---------|
| 1 | 2026-05-26T18:15:00.123Z | 10.0 | 495.2 | 43.7 |
| 2 | 2026-05-26T18:15:03.124Z | 10.0 | 494.8 | 43.5 |

---

## 💡 Recomendaciones de Mantenimiento e Infraestructura

* **Frecuencia de Muestreo:** En procesos industriales lentos (temperatura, niveles), configurar el muestreo entre `3` a `5` segundos para optimizar los costos de inserción por streaming en BigQuery.
* **Manejo de Errores (Buffer):** Se recomienda colocar un nodo `catch` acoplado a una base de datos local (como SQLite o almacenamiento en disco) por si la conexión a internet falla, evitando la pérdida de registros históricos de la planta.
