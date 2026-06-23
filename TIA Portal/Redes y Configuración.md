# 📘 Redes Industriales y Configuración de Hardware

Este documento sintetiza la información sobre el ecosistema TIA Portal, el funcionamiento de redes industriales (LAN/IP) y los procedimientos técnicos necesarios para la puesta en marcha de proyectos de automatización.

---

## 🏗️ 1. Resumen del Ecosistema TIA Portal
TIA Portal (Totally Integrated Automation) es una plataforma de ingeniería unificada. Sus pilares son:
* **Framework Holístico:** Centraliza la programación de PLC, HMI, Drives y dispositivos periféricos.
* **Estandarización:** Uso de librerías, control de versiones y estándares internacionales (IEC, PLCOpen).
* **Colaboración:** Capacidades Multiuser para trabajo concurrente.
* **Integración Total:** Desde la simulación (PLCSim/SIMIT) hasta la generación automática de código (Openness) y HMI (SiVarc).

---

## 🌐 2. Conceptos Fundamentales de Redes (LAN e IP)
Para la comunicación industrial, los pilares son:
* **Dirección IP:** Identificador único del dispositivo (ej. 192.168.1.10).
* **Máscara de Red (Subnet Mask):** Define qué parte de la IP corresponde a la red y cuál al host.
    * `255.255.255.0`: Los primeros 3 octetos son red (permite 254 dispositivos).
    * `255.255.0.0`: Los primeros 2 octetos son red (permite muchos más dispositivos).
* **Dirección MAC:** Identificador físico único del hardware (inmutable).

---

## 🛠️ 3. Procedimientos Técnicos de Configuración

### 🖥️ A. Configuración de IP Fija en la PC (Windows)
Para conectar tu computadora al PLC, ambos deben estar en la misma red.
1. Ve a **Panel de Control** > **Redes e Internet** > **Centro de redes y recursos compartidos**.
2. Haz clic en **Cambiar configuración del adaptador**.
3. Selecciona tu adaptador Ethernet (ej. "Ethernet"), clic derecho > **Propiedades**.
4. Selecciona **Protocolo de Internet versión 4 (TCP/IPv4)** > **Propiedades**.
5. Marca **"Usar la siguiente dirección IP"** y escribe:
   * **IP:** 192.168.1.50 (debe estar en el mismo segmento que el PLC).
   * **Máscara:** 255.255.255.0.
6. Acepta y cierra.

### ⚙️ B. Configuración de IP en TIA Portal (PLC)
1. En el **Device View** (Vista de dispositivos), selecciona el PLC.
2. Ve a la pestaña **Properties** > **PROFINET interface [X1]**.
3. En **Ethernet addresses**, asigna la IP deseada (ej. 192.168.1.10).
4. Asegúrate de que el **Subnet Mask** coincida con la configuración de la PC.

### 🔄 C. Configuración de Dos Redes (Segmentación)
Si el PLC debe hablar con dos redes distintas (ej. una red de gestión y una red de planta):
* **Opción 1:** Usar un PLC con dos puertos PROFINET físicos (algunas CPUs S7-1500 tienen X1 y X2). Configura cada puerto con una IP en subredes diferentes.
* **Opción 2:** Usar un Router Industrial o Switch gestionable para enrutar el tráfico entre ambas redes.

---

## 📋 4. Estrategia de Selección de Entradas y Salidas (I/O)
No satures el PLC base. Sigue esta estrategia:

1. **Catálogo de señales:** Haz un listado de todas las señales físicas (sensores, actuadores).
2. **Clasificación:** Agrupa por:
    * **DI (Digital Input):** Pulsadores, sensores.
    * **DQ (Digital Output):** Lámparas, bobinas de relé.
    * **AI (Analog Input):** Temperatura, presión (4-20mA / 0-10V).
    * **AQ (Analog Output):** Variadores de frecuencia.
3. **Cálculo de Reserva:** Siempre añade un 20% de reserva sobre el total de señales para futuras expansiones.
4. **Verificación de capacidad:**
    * Verifica los puntos integrados en la CPU.
    * Si faltan puntos, selecciona módulos de expansión (SM) o Signal Boards (SB) en TIA Portal.
    * Valida el consumo de corriente en el backplane (TIA Portal avisa si el rack no puede alimentar a todos los módulos).
