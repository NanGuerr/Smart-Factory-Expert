# 📚 Creación y Uso de Librerías Globales

Las librerías globales en TIA Portal son la herramienta definitiva para la estandarización de código y la reutilización eficiente de componentes en múltiples proyectos de automatización.

---

## 🏗️ ¿Qué son las Librerías Globales?
Es un contenedor externo que permite almacenar bloques (FCs, FBs), UDTs, configuraciones de HMI o parámetros de variadores. Al guardarlos en una librería, los independizas del proyecto original para usarlos en cualquier otro proyecto futuro, garantizando que tu lógica sea siempre consistente.

## 💾 Paso a Paso: Creación de tu Librería
1. **Abrir Librerías:** Ve a la pestaña "Librerías" en el panel lateral derecho de TIA Portal.
2. **Crear Nueva:** Haz clic en "Crear nueva librería" (icono de libro con un '+'). Selecciona la ubicación en tu disco duro.
3. **Añadir Bloques:** Selecciona tus bloques creados (ej. `escalado_IA`, `escalado_AQ`) desde tu árbol de "Bloques de programa" y arrástralos directamente a la carpeta **"Plantillas maestras" (Master copies)** de tu nueva librería.
4. **Guardar:** Haz clic en el icono de guardar (disquete) dentro de la pestaña de librerías.
5. **Archivo Generado:** Se creará una carpeta en tu PC con el nombre de la librería y un archivo de extensión **.al16** (donde "16" representa la versión de TIA Portal).

*Nota: Para archivar o enviar por correo, simplemente comprime la carpeta entera en formato .zip.*

---

## 🔗 Paso a Paso: Uso de Librerías
1. **Abrir:** Inicia TIA Portal. En la sección de "Librerías", haz clic en "Abrir librería global".
2. **Seleccionar:** Busca y abre tu archivo `.al16` guardado previamente.
3. **Implementar:** Despliega las "Plantillas maestras" de la librería abierta y arrastra los bloques (Drag & Drop) directamente a la carpeta "Bloques de programa" de tu proyecto actual.

---

## ⚠️ Notas Importantes y Restricciones
* **Inmutabilidad:** Las librerías no admiten modificaciones de funcionamiento directas. Si intentas editar el bloque dentro de la librería, verás que está bloqueado.
* **Actualizaciones:** Si necesitas cambiar la lógica de un bloque (ej. optimizar el escalado), deberás:
    1. Realizar el cambio en un proyecto local.
    2. Arrastrar el bloque actualizado a la librería.
    3. Guardar la librería para que el archivo `.al16` se actualice.
* **Versatilidad:** Este método no es solo para código PLC; puedes compartir temas de HMI, estructuras de datos (UDTs) y configuraciones de variadores de frecuencia, lo que garantiza una estandarización total en tus desarrollos profesionales.
