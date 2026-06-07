# Control Horno PI

Basado en la lógica típica de un controlador **Siemens LOGO!** para sistemas de lazo cerrado, usamos el Diagrama de Bloques Funcionales (FBD) para el control de temperatura con un bloque **PI (Proporcional-Integral)**.

Para regular una llama en la industria, no solemos usar PWM (encender y apagar el suministro de gas cada pocos segundos sería altamente ineficiente, desgastaría las válvulas y podría ser peligroso). En su lugar, utilizamos un control termostático de tipo ON/OFF con histéresis mediante un Conmutador analógico de valor umbral (B001), y previamente acondicionamos la señal del sensor de temperatura utilizando un Ampliador analógico (B002).

### 🌡️ Diagrama de Bloques Funcionales (FBD) - Control PI de Horno

```text
NETWORK 1: Acondicionamiento de Señal (Ampliador Analógico)
La señal cruda del sensor PT100 (AI1) necesita ser escalada a grados reales (ej. 0 a 400°C)
para que los límites de control sean exactos y fáciles de programar en el sistema.

Sensor Temp (AI1) ─────────────►[ AX ]
                                [AMP ] Ampliador Analógico (B002) ───► Señal Escalada (°C)

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 2: Regulación de Llama (Conmutador Analógico de Valor Umbral)
La señal ya escalada entra al conmutador.
Este bloque evalúa la temperatura real frente a dos parámetros (umbral de encendido y umbral de apagado),
para gestionar la apertura de la válvula de gas del quemador.

Señal Escalada (B002) ─────────►[ AX ]
                                [ L  ] Conmutador Umbral (B001) ─────► Válvula de Llama (Q1)
                                [ H  ] (Umbrales On/Off)

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 3: Alarma de Sobretemperatura (Seguridad - Q2)
Si el quemador sufre una avería mecánica y no se apaga, un segundo bloque evalúa la temperatura
como límite de seguridad crítico para cortar el suministro y alertar.

Señal Escalada (B002) ─────────►[ AX ]
                                [ >  ] Comparador (B003) ────────────► Sirena / Corte de Gas (Q2)
Límite Crítico (Interno) ──────►[ SP ]

```

---

### 💡 Análisis del Funcionamiento Lógico

**Ampliador Analógico (Bloque B002):**

* **Uso:** Es el traductor del sistema. Acondiciona la señal eléctrica bruta proveniente del sensor (que el PLC LOGO! suele interpretar como un valor de 0 a 1000) y la convierte a un valor físico real (por ejemplo, de 0 a 400 °C).

* **Funcionamiento:** Se le configuran dos parámetros clave: Ganancia (Gain) y Offset (Desplazamiento). Esto permite que todos los bloques siguientes del programa (como el B001) trabajen directamente leyendo "grados Celsius". Esto hace que la configuración, la lectura en pantallas (HMI/TDE) y el mantenimiento sean muchísimo más intuitivos para el operario.

**Conmutador Analógico de Valor Umbral (Bloque B001):**

* **Uso:** Actúa como el cerebro termostático del quemador. Su principal ventaja es que crea una "banda de histéresis" para evitar que la válvula de gas y el sistema de ignición (chispero) se activen y desactiven frenéticamente si la temperatura fluctúa ligeramente cerca del objetivo.

* **Funcionamiento:** En lugar de una sola temperatura objetivo (como haría un PI), aquí configuras dos límites: un Umbral de Encendido (On) y un Umbral de Apagado (Off).

**Ejemplo práctico:** Si quieres que tu horno se mantenga alrededor de 200°C, configuras el umbral superior de apagado (H) en 200 y el umbral inferior de encendido (L) en 195.

* La llama (Q1) permanecerá encendida hasta alcanzar exactamente los 200°C y se apagará. A medida que el horno pierde calor natural, la temperatura bajará a 199°C, 198°C... pero la válvula no se abrirá. Solo cuando la temperatura toque los 195°C exactos, el bloque enviará la señal para reencender la llama. Esto garantiza ciclos de combustión largos, limpios y seguros para los equipos.
