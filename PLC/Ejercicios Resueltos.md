# 🏗️ Ejercicios Resueltos de Lógica LADDER (PLC) 🤖

Este documento contiene una recopilación de ejercicios prácticos sobre lógica de contactos para PLCs.

---

## 🔘 Ejercicio 1: Manejo básico de bits
**Objetivo:** Encender las salidas `Q1.0` y `Q2.0` al presionar el botón de entrada `%12.0`.

### 🛠️ Configuración de variables:
| Nombre | Clase | Tipo | Ubicación |
| :--- | :--- | :--- | :--- |
| Boton 1 | Local | BOOL | %12.0 |
| Led 1 | Local | BOOL | %Q1.0 |
| Led 2 | Local | BOOL | %Q2.0 |

---

## ⚡ Ejercicio 2: Lógica de inversión (Normalmente Cerrado)
**Objetivo:** Mantener `Q5.0` encendida mientras la entrada `%15.1` esté sin actuar. Si `%15.1` se activa, la salida `Q5.0` debe apagarse.

### 🛠️ Configuración de variables:
| Nombre | Clase | Tipo | Ubicación |
| :--- | :--- | :--- | :--- |
| Boton | Local | BOOL | %15.1 |
| Led 1 | Local | BOOL | %Q5.0 |

---

## 🧠 Ejercicio 3: Lógica combinacional
**Objetivo:** Encender `Q3.2` cuando los botones `%11.1` y `%12.1` estén activos (NO - Normalmente Abiertos), pero el botón `%13.4` no esté activo (NC - Normalmente Cerrado).

### 🛠️ Configuración de variables:
| Nombre | Clase | Tipo | Ubicación |
| :--- | :--- | :--- | :--- |
| Boton 1 | Local | BOOL | %11.1 |
| Boton 2 | Local | BOOL | %12.1 |
| Boton 3 | Local | BOOL | %13.4 |
| Led 1 | Local | BOOL | %Q3.2 |

---
*Documento basado en: EjerciciosResueltosLADDER-210128-194102.pdf*
