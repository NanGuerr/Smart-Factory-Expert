# 🤖 Introducción a la Automatización

La automatización es una tecnología diseñada para ejecutar procesos o procedimientos con la mínima asistencia humana posible. ⚙️

### ¿En qué consiste? 🤔
Se utiliza para controlar equipos como:
*   🏗️ Maquinaria
*   🏭 Líneas de montaje
*   🧪 Procesos químicos
*   🧭 Navegación

El objetivo principal es minimizar o eliminar la intervención de las personas en tareas críticas. 🎯

---

### ⚠️ El Entorno Industrial
Los sistemas deben soportar condiciones extremas:
1.  🌡️ Temperaturas extremas
2.  🫨 Vibraciones y golpes
3.  🌪️ Polvo y partículas en suspensión
4.  💧 Humedad y condensación
5.  🧪 Sustancias químicas agresivas
6.  ⚡ Ruido electromagnético
7.  🔋 Sobretensiones y fluctuaciones eléctricas
8.  🚿 Presencia de agua o líquidos
9.  ☀️ Rayos UV y radiación
10. 🧨 Atmósferas explosivas

---

### 🚀 Ventajas de Automatizar

*   **Sistemas de Control 🖥️:** Monitorean el proceso constantemente con alta precisión en cada etapa.
*   **Tecnología de Punta 🧠:** Utilizan controladores especializados con capacidades de cálculo y reacción superiores a las humanas.
*   **Tiempo y Dinero 💰:** Al reducir la intervención humana, se acelera el proceso, maximizando el tiempo y aumentando la productividad considerablemente. 📈
# 🧠 El PLC a Fondo: Funcionamiento y Características

El PLC (Controlador Lógico Programable) es el componente central en la automatización industrial. 🏭

### 🌐 Panorama de Mercado
Existen numerosas marcas y fabricantes líderes en la industria, incluyendo:
*   🏢 Siemens
*   🏢 Rockwell Automation / Allen-Bradley
*   🏢 Schneider Electric
*   🏢 Mitsubishi Electric
*   🏢 Fatek, ABB, Phoenix Contact, entre otros.

---

### 🧩 Tipos de PLCs y Modularización
La arquitectura de los PLCs permite flexibilidad mediante la modularización:
*   **Sin E/S integradas + Modular:** Sistema expansible según necesidad. 🔌
*   **Con E/S integradas + Modular:** Configuración compacta con capacidad de expansión. ⚡
*   **Comunicación:** Se realiza a través de un "bus local de datos" mediante conexiones internas entre el PLC y los módulos. 🔗

---

### 🔄 El Ciclo de Trabajo (Scan Cycle)
El funcionamiento del PLC es determinístico y se basa en un ciclo continuo:
1.  📥 **Lectura de entradas:** Digitales y analógicas.
2.  💻 **Ejecución del programa:** Procesamiento lógico en la CPU.
3.  📤 **Actualización de salidas:** Digitales y analógicas.

---

### 🏗️ Arquitectura y Tareas
*   **Componentes Principales:** Fuente de alimentación, CPU, área de memoria, interfaces de comunicación. ⚙️
*   **Gestión de Tareas:**
    *   Una tarea inicia y gestiona partes de la lógica.
    *   El controlador ejecuta solo una tarea a la vez, gestionando prioridades. ⏱️
    *   Los programas deben estar asociados a tareas para su ejecución.
*   **Capas de Software:** Hardware, Sistema Operativo y Firmware garantizan la ejecución en tiempo real. 🚀
