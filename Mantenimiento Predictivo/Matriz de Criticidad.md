# 📊 Matriz de Criticidad, Redundancia y Previsibilidad en el Mantenimiento Predictivo 📈

Este documento complementa el marco teórico de la gestión de activos, profundizando en las tres dimensiones fundamentales utilizadas para clasificar procesos industriales y justificar la implementación de estrategias de **Mantenimiento Predictivo (PdM)**.

---

## 🏗️ 1. Las Tres Dimensiones de Evaluación del Proceso

Para diseñar un plan de mantenimiento óptimo y mitigar los costos por fallas en cascada, todo activo o proceso debe ser evaluado bajo una matriz de tres pilares:

### 🚨 A. Criticidad de un Proceso
Determina el nivel de impacto o gravedad que tendría la detención o degradación del activo en el ecosistema de la planta.
* **Criterios de Evaluación:** Seguridad del personal, impacto ambiental, pérdida de calidad del producto, costos por lucro cesante, multas regulatorias y continuidad operativa global.
* **Propósito:** Priorizar el presupuesto y los esfuerzos de monitoreo hacia los cuellos de botella del sistema.

### 🔄 B. Redundancia de un Proceso
Capacidad intrínseca de la ingeniería del sistema para absorber el fallo de un componente sin interrumpir la entrega del producto o servicio final.
* **Configuraciones Comunes:** Equipos en paralelo (arreglos 1+1 o 2+1), lazos de control de respaldo o almacenamiento intermedio (buffers de inventario).
* **Impacto Operativo:** Un proceso con **baja redundancia** (punto único de falla) requiere una estrategia predictiva inmediata debido al riesgo catastrófico que representa.

### 🔮 C. Previsibilidad de un Proceso
Grado de certidumbre con el que el comportamiento operativo y los modos de falla de un equipo pueden ser anticipados a través de datos observables.
* **Variables Clave:** Existencia de patrones medibles, tendencias claras en el tiempo o desviaciones del desempeño estándar.
* **Condición de Éxito:** Que el tiempo entre la detección de la anomalía inicial y la falla funcional (Intervalo P-F) sea lo suficientemente amplio para coordinar y planificar una intervención técnica.

---

## 🎛️ 2. Mantenimiento Predictivo (PdM)

Es una estrategia de confiabilidad avanzada que reemplaza los enfoques rígidos de calendario por decisiones dinámicas basadas en la **condición real del activo**.

```
[ Anomalía Detectada (P) ] ---> [ Monitoreo / Tendencia ] ---> [ Intervención Óptima ] ---> [ Falla Funcional (F) ]
                                   (Intervalo P-F)
```

### 📋 Procedimiento de Implementación Industrial
1. **Instrumentación y Monitoreo:** Captura continua o periódica de variables de estado tales como:
   * 🌡️ *Termografía / Temperatura:* Identificación de puntos calientes en sistemas eléctricos o mecánicos.
   * 🔊 *Ultrasonido / Vibraciones:* Diagnóstico de desalineación, soltura mecánica o desgaste prematuro de rodamientos.
   * 🛢️ *Análisis de Aceite / Tribología:* Monitoreo de partículas de desgaste por fricción y degradación química del lubricante.
   * ⚡ *Consumo Eléctrico y Desempeño:* Detección de sobreesfuerzos y caídas de eficiencia térmica o hidráulica.
2. **Análisis de Tendencias:** Almacenamiento de datos históricos en repositorios estructurados (como Google BigQuery) para correr modelos de regresión y algoritmos de Machine Learning.
3. **Planificación en Ventana Óptima:** Programación de la parada de mantenimiento justo en el espacio de tiempo donde el desgaste compromete el proceso, maximizando la vida útil de los componentes y eliminando las sustituciones preventivas innecesarias.

---

## 💡 Conclusión de Diseño Estratégico
El **Mantenimiento Predictivo** no se aplica de manera indiscriminada a todos los activos de una planta. Su implementación se justifica técnica y económicamente cuando un proceso presenta una **Alta Criticidad**, **Baja o Nula Redundancia** y una **Alta Previsibilidad**. 

```
                                      CRITICIDAD ALTA
                                            │
                                            ▼
                                     REDUNDANCIA BAJA
                                            │
                                            ▼
                                    PREVISIBILIDAD ALTA
                                            │
                             ┌──────────────┴──────────────┐
                             ▼                             ▼
                [ APLICAR PREDICTIVO - PdM ]    [ REDUCCIÓN DE RIESGOS ]
```
