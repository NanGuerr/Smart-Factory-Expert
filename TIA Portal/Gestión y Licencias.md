# 🚀 Guía de Gestión de Proyectos y Licencias en TIA Portal V20

Esta guía cubre los procedimientos fundamentales para la gestión de licencias de prueba y la correcta manipulación de proyectos en TIA Portal V20.

---

## 🔑 1. Activación de Licencia de Prueba (21 días)
Al instalar TIA Portal, si no dispones de una licencia física (USB o archivo), el software ofrece una licencia de prueba:

1. **Inicio:** Al abrir TIA Portal por primera vez tras la instalación, aparecerá el "License Wizard" (Asistente de licencias).
2. **Selección:** Si no se detecta licencia, selecciona la opción **"Trial License"** o **"Licencia de prueba"** (generalmente válida por 21 días).
3. **Activación:** Haz clic en **"Finish"** o **"Activate"**. El software se reiniciará o estará listo para usarse inmediatamente con todas las funciones activas.
4. **Verificación:** Puedes verificar el estado restante en el **Automation License Manager (ALM)**. Ábrelo desde el menú de inicio de Windows y verás la licencia de prueba activa para el producto instalado.

---

## 🏗️ 2. Ejercicio Práctico: Creación y Gestión de Proyectos

### 🆕 Creación del Proyecto
1. **Abrir TIA Portal** y selecciona **"Create new project"**.
2. **Nombre:** Escribe `Proyecto_Version1`.
3. **Ubicación:** Selecciona una carpeta en tu disco local (ej. `C:\\ProyectosSiemens\\`).
4. **Crear:** Haz clic en **"Create"**.

### 🔌 Inserción de Hardware
1. Ve a **"Project view"** (Vista de proyecto).
2. Selecciona **"Add new device"**.
3. Elige **"Controllers"** -> **"SIMATIC S7-1200"** -> **"CPU 1214 DC/DC/DC"**.
4. Selecciona el número de referencia correcto y en la pestaña de versión, elige **"V4.2"**.
5. Haz clic en **"Add"**.
6. **Guardar:** Ve a `Project` -> `Save` (o icono de disquete).

---

## 📂 3. Análisis y Gestión de Archivos

### ¿Dónde está y qué contiene?
Al ir a la carpeta donde guardaste el proyecto (`Proyecto_Version1`), observarás lo siguiente:
* **Extensión del archivo:** Verás un archivo principal con extensión **`.ap20`** (para TIA V20).
* **Estructura:** **¡No está solo!** El proyecto es, en realidad, un "paquete" de carpetas. Verás al menos una carpeta llamada `System` y el archivo `.ap20`. Ambas partes son indispensables.

### ¿Qué pasa si muevo solo el archivo `.ap20`?
**¡El proyecto no abrirá!** 🚫 TIA Portal necesita toda la estructura de carpetas (especialmente la carpeta `System`, donde están los datos de configuración, librerías y metadatos) para cargar el proyecto correctamente. Si intentas abrir solo el archivo `.ap20` en otra ubicación, recibirás un error indicando que el proyecto está incompleto o dañado.

### 📦 Archivar el Proyecto (Formato .zap20)
Para mover o respaldar el proyecto correctamente, debes usar la función de archivo:
1. En TIA Portal, ve a **"Project"** -> **"Archive..."**.
2. Selecciona la carpeta de destino.
3. El sistema creará un archivo único con extensión **`.zap20`**.

### Comparativa de tamaño
* **Carpeta del proyecto (sin archivar):** Ocupa significativamente más espacio, ya que contiene todos los archivos temporales, caché de compilación y estructura de árbol completa sin compresión.
* **Archivo .zap20:** Es un archivo comprimido (tipo ZIP específico de Siemens). **Pesa mucho menos** que la carpeta original y es el formato ideal para enviar por correo, subir a la nube o guardar en un pendrive, ya que mantiene la integridad de todos los archivos internos.
