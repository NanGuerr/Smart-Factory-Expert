# 🛠️ Ejercicios: Programación de PLC Siemens – TIA Portal V20

## 📝 Descripción del Proyecto
* **Nombre del proyecto:** `Proyecto_Version1`
* **CPU:** S7-1200 CPU 1214 DC/DC/DC
* **Versión de Firmware:** 4.2

---

## 📂 1. Gestión de archivos y estructura
### ¿Cuál es la extensión del archivo que se crea?
El archivo principal del proyecto generado tiene la extensión **`.ap20`** (específica para la versión 20 de TIA Portal).

### ¿Está solo, o hay más archivos?
**¡No está solo!** ❌ Al crear un proyecto, TIA Portal genera una estructura de directorios completa. El archivo `.ap20` es apenas el "índice". Necesitas las carpetas asociadas para que el proyecto funcione, tales como:
*   📁 **IM (Information Management):** Donde reside la caché y metadatos del hardware.
*   ⚙️ **System:** Contiene las bases de datos internas del proyecto.
*   📋 **Logs:** Historiales de compilación y registros.

---

## ⚠️ 2. Comportamiento al aislar el archivo
### ¿Qué ocurre si copiamos sólo ese archivo fuera de la carpeta y tratamos de abrirlo?
Si intentas abrir el archivo `.ap20` de forma aislada, **el TIA Portal mostrará un error** indicando que el proyecto está incompleto o dañado. 🚫
*   **¿Por qué?** Porque el TIA Portal requiere leer las bases de datos relacionales dentro de las carpetas auxiliares (`IM`, `System`, etc.) para cargar la configuración, las variables y el código de programación.

---

## 📦 3. Archivado del Proyecto
### ¿Qué es el archivo .zap20?
Es el formato de "archivo comprimido" nativo de TIA Portal. Al realizar la acción de **Proyecto > Archivar**, el software empaqueta todo el directorio (incluyendo los archivos auxiliares) en un único contenedor optimizado para transporte o respaldo. 💾

---

## ⚖️ 4. Comparación de tamaños
*   **Carpeta entera del proyecto:** Suele ser **pesada**. 🐘 Puede ocupar desde 50 MB hasta varios GB, ya que incluye todos los archivos temporales y de configuración no optimizados.
*   **Archivo `.zap20`:** Es **ligero**. 🚀 Al realizar el proceso de archivado, el sistema comprime los datos eliminando redundancias, haciendo que el archivo sea mucho más fácil de compartir o subir a la nube.

---
*¡Espero que esta guía te sea de gran utilidad en tus prácticas!* 💡
