# 🏗️ Tipos de Datos de Usuario (UDT) en DB

Los **UDTs (User Defined Types)** permiten definir estructuras de datos personalizadas, actuando como plantillas reutilizables para organizar tu programa de forma profesional.

---

## 🧐 ¿Qué es un UDT?
Un UDT es un "tipo de dato propio". Es un molde que define cómo se deben agrupar diferentes variables (BOOL, INT, REAL, etc.) para formar una entidad lógica completa (ej. un Motor, una Válvula, una Estación).

## 🚀 Ventajas Principales
* **Reutilización:** Diseñas la estructura una vez y la usas en múltiples DBs o FBs.
* **Mantenimiento:** Si cambias algo en el UDT, todos los objetos basados en él se actualizan automáticamente.
* **Orden:** Reduces drásticamente el número de variables en la tabla de PLC Tags.

---

## 📋 Pasos para crear y usar un UDT

### 1. Creación del UDT
1. En el **Árbol del Proyecto**, ve a `PLC Data types`.
2. Haz clic en **Add new data type**.
3. Nómbralo (ej. `typeMotor`).
4. Abre el editor y añade las variables que componen tu objeto (Start, Stop, Velocidad, Temperatura, etc.).

### 2. Uso en un Bloque de Datos (DB)
1. Abre tu DB (o crea uno nuevo).
2. En la columna **Data Type**, en lugar de buscar un tipo estándar, escribe el nombre de tu UDT (ej. `typeMotor`).
3. El editor creará automáticamente la estructura completa basada en tu molde.

---

## 💡 Eficiencia Suprema: Arrays de UDTs
Esta es la técnica más potente para gestionar grupos grandes de elementos (ej. 20 motores idénticos).

**Cómo declararlo:**
En un DB, crea una variable:
* **Nombre:** `MisMotores`
* **Data Type:** `Array[0..19] of typeMotor`

**Resultado:**
Ahora tienes `MisMotores[0]`, `MisMotores[1]`, hasta `MisMotores[19]`. Cada uno de ellos contiene internamente la estructura `Start`, `Stop`, `Velocidad`, etc.

**Ventaja:** Puedes usar bucles `FOR` en SCL para recorrer los 20 motores y procesar sus datos en apenas unas líneas de código.

---

## 🔧 Modificación del Alcance
* **Retentividad:** Al definir el UDT, puedes marcar las variables internas como *Retain*. Esto se heredará en todos los DBs donde uses el UDT.
* **HMI:** Puedes configurar que todo el UDT sea accesible desde HMI, permitiendo que un solo objeto de pantalla (faceplate) se conecte a cualquier motor simplemente cambiando el índice del Array.
