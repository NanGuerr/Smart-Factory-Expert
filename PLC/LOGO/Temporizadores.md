
# ⏱️ Guía Técnica: Temporizadores Especiales

Los temporizadores semanales, anuales y cronómetros son bloques especiales que dependen del Reloj de Tiempo Real (RTC) del PLC o de señales de habilitación continuas. A diferencia de los temporizadores clásicos (TON/TOFF), estos están diseñados para automatización basada en calendarios o medición exacta de eventos.

A continuación, te presento los diagramas de bloques funcionales (FBD) y el análisis de cada uno. 📅⚙️

---

### 1. Temporizador Semanal (Programador Horario) 🗓️
Este bloque no requiere una señal de entrada para activarse; se rige exclusivamente por la hora y el día de la semana configurados internamente. 

**Diagrama FBD:**
```text
NETWORK 1: Encendido de Luces de Oficina
El bloque se activa automáticamente los días laborables (ej. Lunes a Viernes)
en un horario específico (ej. 08:00 a 18:00).

[ T ] Temp. Semanal (B001) ─────────────────► Luces de Oficina (Q1)

```

* **Uso:** Ideal para domótica y ahorro energético. Se utiliza en sistemas de riego (lunes, miércoles y viernes a las 6:00 AM), encendido de iluminación, precalentamiento de máquinas antes de que lleguen los operarios, o encendido de aires acondicionados comerciales.
* **Funcionamiento:** Dentro de las propiedades del bloque, se configuran "Levas" (cams). Cada leva te permite seleccionar días de la semana y establecer una hora exacta de encendido (ON) y apagado (OFF). Cuando el reloj interno del PLC coincide con la configuración, la salida del bloque se pone a "1" lógico.

---

### 2. Temporizador Anual (Programador de Fechas) 🌍

Al igual que el semanal, es un bloque autónomo que se basa en el calendario interno del PLC, pero a nivel de meses y días del mes.

**Diagrama FBD:**

```text
NETWORK 2: Control de Iluminación Navideña
El bloque se activa solo durante una época del año (ej. 1 de Diciembre al 6 de Enero).

[ T ] Temp. Anual (B002) ───────────────────► Luces Fachada (Q2)

```

* **Uso:** Paradas de planta programadas por vacaciones, cambio de comportamiento de sistemas HVAC (calefacción en invierno vs. refrigeración en verano), o activaciones estacionales (como bombas para fuentes de agua en parques solo durante meses cálidos).
* **Funcionamiento:** Se configura estableciendo una fecha de inicio (Día/Mes) y una fecha de finalización (Día/Mes). El bloque mantendrá su salida activada ininterrumpidamente durante todo ese periodo de fechas. Puede configurarse para que se repita todos los años automáticamente.

---

### 3. Cronómetro (Medidor de Tiempo de Funcionamiento) ⏳

Este bloque sí requiere entradas físicas o lógicas. Se utiliza para medir cuánto tiempo transcurre un evento específico.

**Diagrama FBD:**

```text
NETWORK 3: Registro de tiempo de funcionamiento de un motor
El cronómetro cuenta el tiempo solo mientras el motor está encendido.
Si se presiona el botón de Reset, el tiempo vuelve a cero.

Motor Encendido (Q3) ──────────►[ EN ]
                                [ T  ] Cronómetro (B003) ────► Alarma Mantenimiento (Q4)
Botón Mantenimiento (I1) ──────►[ R  ]

```

**Uso:** Es vital para el mantenimiento industrial predictivo. Se usa para registrar las horas de funcionamiento de motores, bombas o compresores, y emitir una alarma cuando toca cambio de aceite o revisión. También sirve para medir tiempos de ciclo en líneas de producción.

**Funcionamiento:** 

* **EN (Enable):** Mientras esta entrada reciba un "1" lógico, el cronómetro suma tiempo (en horas, minutos o segundos). Si la señal se apaga, el cronómetro pausa la cuenta y memoriza el valor.

* **R (Reset):** Al recibir un pulso en esta entrada, el tiempo acumulado se borra y vuelve a cero.

* **Salida:** El bloque puede configurarse para activar su salida cuando el tiempo acumulado alcance un valor límite preestablecido (ej. 1000 horas de funcionamiento).
