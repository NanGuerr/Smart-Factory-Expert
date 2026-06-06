# 📘 Cuestionario Técnico: Programación y Configuración de Siemens LOGO!

Este documento recopila las respuestas fundamentales sobre el manejo, programación y configuración de los controladores lógicos programables (PLC) LOGO! de Siemens. ⚙️

---

### 1. Selección del Dispositivo
**¿Antes de iniciar un proyecto se requiere seleccionar un dispositivo?**
* **Respuesta:** Verdadero. ✅
* **Detalle:** Es fundamental conocer el hardware (tensión, tipo de salidas y si requiere display o reloj) para asegurar la compatibilidad con el entorno de trabajo.

### 2. Recursos de Hardware
**¿Al momento de programar se requiere conocer la cantidad de entradas y salidas a utilizar?**
* **Respuesta:** Verdadero. 🔢
* **Detalle:** Debes saber si los recursos del módulo base son suficientes o si necesitas añadir módulos de expansión digitales o analógicos.

### 3. Lenguajes de Programación
**¿Es mejor la programación en escalera o en bloques funcionales?**
* **Respuesta:** c. Es mejor conocer ambos tipos de lenguaje. 🧠
* **Detalle:** Cada uno tiene sus ventajas; los bloques funcionales (FBD) son excelentes para lógica compleja, mientras que Ladder (escala) es el estándar industrial clásico.

### 4. Bloques Definidos por el Usuario
**¿Para realizar bloques definidos por el usuario se deben de cumplir varias reglas?**
* **Respuesta:** Verdadero. 🏗️
* **Detalle:** Estos bloques requieren una estructuración específica de entradas, salidas y parámetros para poder ser reutilizados correctamente en el programa.

### 5. Transferencia de Programas
**¿Al momento de transferir un archivo del PC al controlador es recomendable transferir sin chequear que ambos equipos estén sincronizados?**
* **Respuesta:** No. 🚫
* **Detalle:** Es indispensable verificar que la comunicación sea estable y que los dispositivos estén sincronizados para evitar errores de transferencia o corrupción de datos.

### 6. Diseño de Lógica
**¿Es recomendable utilizar un diagrama de flujo al momento de iniciar a programar?**
* **Respuesta:** Sí. 📉
* **Detalle:** Es la mejor práctica para visualizar la lógica del sistema, prevenir errores y asegurar que todos los estados del proceso sean contemplados antes de escribir código.

### 7. Aplicaciones de Programación
**¿Todo proceso ya sea industrial o domótico, se emplea la misma programación?**
* **Respuesta:** b. No, cada proceso posee distintos medios para ser programado dependiendo la aplicación. 🛠️
* **Detalle:** La lógica varía radicalmente según la complejidad, las variables de seguridad y los tipos de sensores o actuadores involucrados.

### 8. Señales Analógicas
**¿Al momento de utilizar señales analógicas en un controlador LOGO! se debe realizar escalamiento?**
* **Respuesta:** b. No es necesario, ya que LOGO! Soft Comfort posee bloques para realizar los trabajos con señales análogas mucho más sencillo. 🎚️
* **Detalle:** El software incluye bloques preconfigurados (como el convertidor analógico o comparadores) que gestionan las conversiones de forma interna.

### 9. Control PID
**¿LOGO! Soft Comfort posee un bloque dedicado al controlador PI?**
* **Respuesta:** Verdadero. 📊
* **Detalle:** El software cuenta con bloques funcionales de control (incluyendo control PI) diseñados para procesos que requieren regulación continua (como temperatura o presión).

### 10. Pantallas de Operación
**¿Dentro de LOGO! Soft Comfort puedo programar la pantalla de un LOGO! TDE y un controlador LOGO!?**
* **Respuesta:** Sí. 🖥️
* **Detalle:** El entorno permite configurar tanto la lógica del PLC como los textos de aviso y menús que se mostrarán en la pantalla del TDE.

### 11. Sistema SCADA
**¿Puedo programar o poseer un pequeño sistema SCADA por medio del LOGO! web server?**
* **Respuesta:** a. Sí, pero solamente para las versiones actuales de LOGO!. 🌐
* **Detalle:** Los modelos LOGO! 8 cuentan con el servidor web integrado que permite esta capacidad de visualización y control remoto.

---
*Documento generado con base en los principios de automatización industrial de la serie LOGO!.* ⚡
