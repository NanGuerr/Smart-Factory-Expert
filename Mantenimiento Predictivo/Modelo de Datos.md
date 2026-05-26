# 📊 Datos para el Mantenimiento y Modelo de Datos

Este documento presenta una guía detallada y estructurada basada en los datos de gestión de activos, el modelo de datos para mantenimiento y las definiciones fundamentales de la clase para optimizar la toma de decisiones analíticas y predictivas.

---

## 🖼️ 1. Transcripción y Análisis de la Imagen Adjunta

La imagen muestra una diapositiva de una presentación titulada **"DATOS PARA REALIZAR EL MANTENIMIENTO"**, orientada al diseño y la gestión estructurada de la información en organizaciones industriales o de operaciones.

### 📝 Transcripción del Contenido Textual

* **Título Principal:** DATOS PARA REALIZAR EL MANTENIMIENTO
* **Descripción del Modelo:** > "El modelo de datos de mantenimiento está diseñado para organizar, almacenar y facilitar el análisis de la información clave relacionada con la gestión de activos y las actividades de mantenimiento en una organización."
    > 
    > "A través de la interacción de estas tablas, la organización puede optimizar la disponibilidad y confiabilidad de sus activos, reducir los costos operativos y mejorar la toma de decisiones basada en datos precisos y actualizados."
* **Tablas del Modelo (Listado):**
    * ✅ Activos
    * ✅ Empleados
    * ✅ Datos de sensores
    * ✅ Fallas
    * ✅ Valor Activos
    * ✅ Costos
    * ✅ Educación de empleados
    * ✅ Órdenes de mantenimiento
    * ✅ Tareas de mantenimiento
* **Nota de Advertencia (Recuadro Verde):**
    > "No considerar alguno de los aspectos mencionados a la hora de realizar el mantenimiento puede afectar en el cálculo de costo y justificación del mismo. Recordemos que todo proviene del presupuesto generado por el ahorro de incidencias evitadas."
* **Elemento Visual Adicional:** En la esquina inferior derecha se observa la captura de un presentador o expositor con auriculares y lentes, lo que denota que el material proviene de una clase grabada, seminario web o curso técnico.

### 🔍 Análisis Técnico de la Imagen

La diapositiva subraya la importancia del **enfoque relacional y sistémico** en el mantenimiento moderno. No basta con registrar cuándo se daña una máquina; es mandatorio cruzar variables de múltiples dimensiones (recursos humanos, costos financieros, telemetría y logística de órdenes). El mensaje central del recuadro verde enfatiza el **Retorno de la Inversión (ROI)** del mantenimiento preventivo/predictivo: el mantenimiento no debe verse como un gasto, sino como un centro de costo justificado por el valor económico de las fallas que se logran evitar.

---

## 📚 2. Definiciones de la Clase y Procedimientos Detallados

A continuación, se profundiza en las referencias conceptuales esenciales explicadas en el módulo de aprendizaje, estructuradas de forma descriptiva y procedimental:

### ⚙️ Activo
* **Definición:** Se trata de cualquier equipo, componente o sistema físico que aporta valor al proceso (bomba, motor, compresor, línea, subestación, vehículo).
* **Procedimiento y Consistencia:** Consiste en delimitar un elemento identificable que tiene una función específica, un contexto de operación determinado, un ciclo de vida útil y un conjunto de requisitos de desempeño. Sobre este elemento se planifican, ejecutan y miden todas las actividades de operación y mantenimiento.

### 📉 Historial de Fallas de Activos
* **Definición:** Se trata del registro acumulado de fallas y eventos asociados a un activo a lo largo de su tiempo de operación.
* **Procedimiento y Consistencia:** Consiste en documentar de manera estricta qué falló, cuándo falló (fecha y hora exacta), cómo se detectó el síntoma, cuál fue el modo o código de falla estandarizado, la causa raíz (si se conoce), la acción correctiva aplicada, los repuestos utilizados, los tiempos totales de parada y los costos asociados. Este histórico es vital para entender patrones de degradación y alimentar modelos analíticos y predictivos.

### 🗂️ Modelo de Datos
* **Definición:** Se trata de la forma estructurada en que se organizan, interconectan y relacionan los datos de la organización para que puedan almacenarse, consultarse y analizarse correctamente.
* **Procedimiento y Consistencia:** Consiste en definir las entidades del negocio (por ejemplo: activos, órdenes, fallas, mediciones), sus atributos particulares (fechas, códigos, valores numéricos) y las relaciones lógicas entre ellas (qué activo pertenece a qué planta, qué orden corresponde a qué falla). Su correcto diseño asegura la consistencia y la trazabilidad de los datos indispensables para la analítica avanzada.

### 📐 Tabla Dimensional
* **Definición:** Se trata de una tabla que contiene el contexto descriptivo o cualitativo necesario para clasificar, segmentar y filtrar la información operativa.
* **Procedimiento y Consistencia:** Consiste en almacenar atributos relativamente estables en el tiempo (por ejemplo: descripción del activo, ubicación geográfica, sistema técnico, familia de equipo, proveedor, criticidad del activo, turnos de trabajo). Estas dimensiones permiten a los analistas interrogar los datos y evaluar los eventos desde múltiples "perspectivas" en los tableros de reportes.

### 📊 Tabla de Hechos
* **Definición:** Se trata de la tabla central de un modelo analítico (como el modelo en estrella) que concentra los eventos cuantitativos y medibles del negocio o la operación.
* **Procedimiento y Consistencia:** Consiste en registrar cada ocurrencia o transacción mediante métricas transaccionales y cantidades numéricas (por ejemplo: duración exacta de la parada en minutos, costo total, horas-hombre invertidas, cantidad de repuestos consumidos, energía consumida o lecturas puntuales de sensores). Cada registro se enlaza mediante claves foráneas (*foreign keys*) a las respectivas tablas dimensionales (activo, fecha, ubicación, tipo de trabajo).

### 📋 Orden de Mantenimiento
* **Definición:** Se trata del documento o registro digital formal que autoriza, planifica, programa y controla cualquier tipo de intervención técnica en los activos.
* **Procedimiento y Consistencia:** Consiste en registrar y hacer seguimiento a campos críticos como: identificación del activo, descripción detallada del problema o tarea, prioridad del trabajo, tipo de mantenimiento (correctivo, preventivo, predictivo), fechas programadas vs. ejecutadas, recursos humanos asignados, repuestos necesarios, procedimientos técnicos, análisis de riesgos/permisos de trabajo y los resultados finales (qué condiciones se encontraron y qué acciones se ejecutaron).

### 💸 Pérdida de Producción por Mantenimiento Correctivo
* **Definición:** Se trata del volumen de producción no realizada, degradada o del servicio no entregado a causa de una intervención de emergencia no planificada generada por una falla inesperada.
* **Procedimiento y Consistencia:** Consiste en calcular y cuantificar monetariamente el impacto del tiempo fuera de servicio (*downtime*), la velocidad reducida de operación, el desperdicio (*scrap*) o retrabajo generado durante los arranques del sistema, los incumplimientos contractuales y, en general, el coste de oportunidad de lo que la planta dejó de producir por atender de urgencia la avería.

---

## 🛠️ 3. Procedimiento para Integrar los Datos de Mantenimiento

Para que las tablas mencionadas en la imagen (*Activos, Empleados, Sensores, Fallas, Costos, Órdenes, etc.*) funcionen eficazmente, se recomienda seguir el siguiente flujo de consolidación de datos:

1.  **Estandarización de Activos:** Registrar y codificar la taxonomía de los activos en la **Tabla Dimensional de Activos** bajo normas internacionales (como la ISO 14224).
2.  **Captura en Tiempo Real:** Configurar los **Datos de Sensores** para registrar variables críticas (temperatura, vibración) asociados mediante una clave única al ID del Activo.
3.  **Ciclo de la Orden de Trabajo:** Ante una anomalía o plan preventivo, generar la **Orden de Mantenimiento** vinculando al **Empleado** calificado (cruzando datos de la tabla *Educación de empleados*).
4.  **Cierre y Costeo:** Al finalizar la intervención, registrar en la **Tabla de Hechos de Costos** los gastos de mano de obra, repuestos y la **Pérdida de Producción**, justificando financieramente la inversión mediante el ahorro generado por evitar futuras paradas de planta.
