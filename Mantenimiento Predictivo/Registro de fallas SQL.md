# 📊 Estructuración de Modelos Predictivos en SQL 🛠️

Este documento técnico consolida los conceptos de captura de eventos, diseño de datasets y manipulación de bases de datos relacionales mediante SQL para la creación de modelos de Inteligencia Artificial en mantenimiento predictivo.

---

## 📑 1. Gestión de Eventos y Metas de Confiabilidad

Para alimentar cualquier modelo analítico, es obligatorio estructurar el registro de eventos físicos y definir los umbrales de éxito operacional.

### 📝 Registro de Fallas
Es el repositorio histórico, auditable y trazable de todas las degradaciones funcionales de los activos de la planta.
* **Campos Mandatorios:** Timestamp exacto (Fecha y Hora), ID del activo, Síntoma observado, Modo de falla, Causa raíz, Severidad del impacto, Tiempo Fuera de Servicio (Downtime) y Acción Correctiva ejecutada.
* **Propósito en IA:** Actúa como la fuente de verdad (*Ground Truth*) para etiquetar las variables de los sensores y entrenar modelos supervisados.

### 🎯 Objetivo de Confiabilidad
Meta cuantitativa e indicador clave de rendimiento (KPI) que define el comportamiento esperado de un equipo.
* **Métricas Típicas:** Disponibilidad Global, MTBF (Tiempo Medio Entre Fallas), Tasa de Fallas o Probabilidad de Fallo en un horizonte temporal específico.
* **Uso Estratégico:** Evaluar el Retorno de Inversión (ROI) de los algoritmos predictivos desplegados.

---

## 💾 2. De la Base de Datos al Modelo de IA

La transformación de mediciones crudas en conocimiento predictivo requiere un proceso de modelado estructural:

```
[ Registro de Fallas ] + [ Datos de Sensores ] 
                       │
                       ▼ (Vía SQL)
               [ MODELO DE DATOS ]
                       │
                       ▼ (Estructuración)
                  [ DATASET ] ───> [ Entrenamiento de IA ]
```

### 🗂️ Modelo de Datos
La arquitectura lógica que define cómo se organizan, interconectan y validan las entidades del negocio (Activos, Sensores, Órdenes de Trabajo, Historial de Fallas) mediante tablas, campos, llaves primarias (`PK`) y llaves foráneas (`FK`). Garantiza la trazabilidad e integridad de los datos de planta.

### 📊 Dataset
El conjunto de datos final optimizado y limpio listo para el análisis predictivo. 
* **Estructura:** Filas que representan observaciones temporales o eventos individuales, y Columnas que representan las variables predictoras (temperatura, vibración, presión) junto con la variable objetivo o etiqueta (ej. `0` = Operando Normal, `1` = Falló).

---

## ⚡ 3. Manipulación de Datos Relacionales con SQL

**SQL (Structured Query Language)** es el estándar de facto para la consolidación, limpieza y extracción de datos provenientes de los sistemas de automatización (SCADA/Mantenimiento) hacia los almacenes de datos analíticos (como Google BigQuery).

### 🕹️ Instrucción Fundamental: `INSERT`
Se utiliza para inyectar de forma continua o en lotes (*batch*) nuevos registros dentro de las tablas del modelo de datos.

#### 📝 Sintaxis Estándar de Inserción:
```sql
INSERT INTO nombre_tabla (columna1, columna2, columna3)
VALUES (valor1, valor2, valor3);
```

#### 🏭 Ejemplo Aplicado a Mantenimiento Predictivo (Registro de Sensor o Falla):
```sql
INSERT INTO `proyecto_predictivo.Datos.HistorialFallas` (
    FechaHora, 
    ActivoID, 
    ModoFalla, 
    DowntimeHoras
)
VALUES (
    '2026-05-26 17:30:00', 
    'BOMBA-02A', 
    'Desgaste de Rodamiento', 
    4.5
);
```
*Este comando añade de manera permanente la traza de una parada de planta, permitiendo que el algoritmo de IA correlacione las lecturas previas del sensor con el fallo mecánico documentado.*
