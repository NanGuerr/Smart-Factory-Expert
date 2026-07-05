# 🛡️ Manual de Seguridad y Paradas

Este documento detalla la lógica de control para las funciones de **Parada Controlada** y **Parada de Emergencia** del sistema de control PLC.

## 🛑 1. Parada Controlada
La parada controlada se puede ejecutar cuando la máquina está en régimen (Paso 6 cumplido).

### Secuencia de Operación:
* **Activación:** Se requiere la señal de "Paso 6 cumplido". Se crea una variable `Seguridad.Parada_controlada` en el `DB_Sistema`. Al activarse, se aplica un `SET` para iniciar la rutina.
* **Acción en Válvula:**
    * Se fuerza el modo Manual/Automático a Manual.
    * Se posiciona la válvula al 10%.
    * Se utiliza un temporizador: durante los primeros 10 segundos, la válvula se mantiene al 10%. Pasado este tiempo (y utilizando un contacto NC de la salida del temporizador), se mueve un valor de 0 a la consigna manual.
* **Sistema de Frenado:** Al alcanzar una velocidad ≤ 2500 RPM, se activan los frenos neumáticos mediante el pistón comandado por el PLC.
* **Reinicio de Secuencia:**
    * Se ejecuta solo en estado de "Parada controlada" y con velocidad ≤ 1 RPM.
    * Se reinician (RESET) todos los pasos de la secuencia (de atrás hacia adelante).
    * Se sueltan los frenos y se finaliza el estado de parada.

## 🚨 2. Parada de Emergencia
El bloque `FC2` gestiona las condiciones críticas que requieren detención inmediata. Las condiciones se evalúan en paralelo:

### Condiciones de Activación:
* **Botones de Emergencia:** Presión de botones tipo hongo (NC - Lógica inversa: si se presiona = 1).
* **Sobrevelocidad:** Velocidad > 5500 RPM.
* **Alta Presión:** Presión > 5.5 bar.
* **Baja Presión Crítica:** Presión < 3.3 bar durante 30 segundos (con máquina > 4000 RPM).
* **Sobretemperatura:** Temperatura > 350 °C.

### Acciones Inmediatas:
1. **Cierre de emergencia:** Cierre inmediato de válvula de control, apertura de válvula secundaria y activación del quemador secundario.
2. **Frenado:** Aplicación de frenos de inmediato.
3. **Reset:** Se reinicia la secuencia (reemplazando lógica de parada controlada por emergencia) para garantizar la seguridad.

## 🔄 3. Bloqueos de Seguridad
* **Arranque:** Se debe evitar por completo el inicio de la secuencia si existe una señal activa de Parada de Emergencia o Parada Controlada.
* **Independencia:** A diferencia de la parada controlada (que requiere régimen), la parada de emergencia actúa en cualquier momento de la secuencia o programa, asegurando que todos los componentes queden apagados.
