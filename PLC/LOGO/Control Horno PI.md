# Control Horno PI

Basado en la lógica típica de un controlador **Siemens LOGO!** para sistemas de lazo cerrado (como las imágenes de los hornos que has estado estudiando), aquí tienes el Diagrama de Bloques Funcionales (FBD) para el control de temperatura con un bloque **PI (Proporcional-Integral)**.

En este diseño, utilizaremos un sensor analógico (PT100), el controlador PI y un bloque **PWM (Modulación por Ancho de Pulso)**, que es la forma estándar de controlar resistencias eléctricas en un horno industrial para mantener la temperatura exacta sin gastar energía de más.

### 🌡️ Diagrama de Bloques Funcionales (FBD) - Control PI de Horno

```text
NETWORK 1: Adquisición y Controlador PI
El bloque PI recibe la temperatura real del sensor y la compara con la temperatura deseada (Consigna/SP) para calcular cuánta potencia necesita el horno.

Entrada Marcha (I1) ───────────►[ EN ]
                                [ PI ] Controlador PI (B001) ───► Señal Analógica
Sensor Temp (AI1) ─────────────►[ PV ] 
                                [ SP ] (Consigna programada)

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 2: Modulación PWM y Activación del Calefactor (Q1)
La señal analógica del PI (ej. 0-1000) entra a un modulador PWM. Este bloque enciende y apaga el contactor de estado sólido del calefactor en pulsos rápidos o lentos según la potencia demandada por el PI.

Señal Analógica (B001) ────────►[ AX ]
                                [PWM ] Modulador (B002) ────────► Resistencia Horno (Q1)
Entrada Marcha (I1) ───────────►[ EN ]

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 3: Alarma de Sobretemperatura (Seguridad - Q2)
Lógica combinacional con un comparador analógico. Si el sensor detecta una temperatura superior al límite de seguridad, activa una alarma.

Sensor Temp (AI1) ─────────────►[ AX ]
                                [ >  ] Comparador (B003) ───────► Sirena / Alarma (Q2)
Límite Crítico (Interno) ──────►[ SP ]

```

---

### 💡 Análisis del Funcionamiento Lógico

* **Controlador PI (Bloque `B001`):**
* **EN (Enable):** Se activa con un interruptor físico (`I1`). Si no está activo, el horno no calienta.
* **PV (Process Value):** Es la temperatura real que está midiendo el sensor `AI1` dentro del horno.
* **SP (Setpoint):** Es la temperatura a la que quieres llegar. El bloque PI calcula matemáticamente la diferencia entre PV y SP para mandar más o menos "fuerza" al calentador.


* **Modulador PWM (Bloque `B002`):** Los relés o contactores digitales (`Q1`) solo entienden de "Encendido" (1) o "Apagado" (0). El bloque PWM traduce la señal matemática del PI en tiempo. Por ejemplo: si el PI pide un 50% de potencia, el PWM mantendrá la resistencia encendida 5 segundos y apagada otros 5 segundos.
* **Comparador Analógico (Bloque `B003`):** Un elemento de seguridad vital en la industria. Actúa independientemente del PI. Si el contactor se queda pegado o el PI falla, este bloque activa una alarma `Q2` en el momento en que la temperatura real excede un valor de emergencia.
