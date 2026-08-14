# 📊 Guía Completa de Node-RED Dashboards & FlowFuse

---

## 🔍 1. Comparativa de Node-RED Dashboards

El artículo de FlowFuse analiza la evolución de las interfaces gráficas en Node-RED, comparando el **Dashboard original (`node-red-dashboard`)** con el nuevo **Dashboard 2.0 (`@flowfuse/node-red-dashboard`)**:

* 🏛️ **Dashboard 1.0 (AngularJS):** Ha sido el estándar durante años, pero utiliza dependencias obsoletas y presenta limitaciones en flexibilidad visual y soporte a largo plazo.
* 🚀 **Dashboard 2.0 (Vue.js / Vuetify):** Construido desde cero para ofrecer mayor rendimiento, componentes modernos, diseños adaptativos (responsive) y una arquitectura extensible mediante componentes personalizados.

---

## 🛠️ 2. Creación del Primer Dashboard

1. 📥 **Instalación:** Desde el menú de Node-RED (*Manage Palette*), busca e instala el paquete `@flowfuse/node-red-dashboard`.
2. 🧩 **Añadir Nodos:** Arrastra un nodo de interfaz gráfica (por ejemplo, `ui-button` o `ui-text`) al lienzo de trabajo.
3. 📐 **Configuración de Grupo y Página:** Asigna el nodo a un grupo visual dentro de una página específica usando la pestaña de configuración lateral (*Dashboard 2.0*).
4. 🚀 **Despliegue y Acceso:** Presiona **Deploy** y navega a la URL local finalizada en `/dashboard` (ejemplo: `http://localhost:1880/dashboard`) para interactuar con la interfaz.

---

## 🔴 3. Biblioteca LED Dashboard

* 💡 **Paquete:** `@flowfuse/node-red-dashboard-2-ui-led`
* ⚙️ **Uso:** Es una extensión para Dashboard 2.0 que añade un indicador luminoso de tipo LED a la interfaz.
* 🚥 **Características:** Permite representar visualmente el estado de dispositivos IoT o sensores mediante colores configurables (verde para activo, rojo para fallo, amarillo para advertencia) según los mensajes (`msg.payload`) recibidos.

---

## 📐 4. Características de la Estructura del Dashboard

### 📱 Características del Dashboard I: Páginas y Layout
* 📑 **Páginas:** Permite estructurar la interfaz en múltiples pantallas navegables.
* 📐 **Layout (Diseño de Cuadrícula):** Los elementos se distribuyen en una cuadrícula adaptable donde se puede definir el ancho y alto de cada widget para adaptarse a pantallas móviles y de escritorio.

### 🧭 Características del Dashboard II: Barra de Navegación, Links, Grupos y Temas
* 🍔 **Barra de Navegación:** Menú desplegable lateral o superior para alternar entre diferentes páginas.
* 🔗 **Links:** Enlaces externos e internos integrados directamente en el menú de la aplicación.
* 📦 **Grupos:** Contenedores visuales para agrupar widgets relacionados dentro de una misma página.
* 🎨 **Temas:** Opciones de personalización estética como modos claro/oscuro y paletas de colores corporativas.

### ⚙️ Características del Dashboard III: Nodos de Configuración
* 🛠️ **Configuración Global:** Nodos invisibles en la interfaz que gestionan la jerarquía global (Páginas $\rightarrow$ Grupos $\rightarrow$ Widgets).
* 🔐 **Gestión de Estado:** Administran las sesiones de los usuarios, eventos globales y estilos CSS personalizados aplicados a toda la aplicación.

---

## 🧩 5. Detalle de Widgets para Dashboards en Node-RED

* 🎛️ **Widgets Generales:**
  * `ui-button`: Botón interactivo para disparar flujos.
  * `ui-text`: Muestra texto simple o formateado en el panel.
  * `ui-text-input`: Campo de entrada de texto manual por parte del usuario.
  * `ui-slider`: Barra deslizante para ajustar valores numéricos de forma continua.
  * `ui-switch`: Interruptor lógico de encendido/apagado (toggle).

* 🔔 **Widgets de Notificaciones:**
  * `ui-notification` / Toast: Muestra alertas emergentes temporales en la pantalla del usuario para avisar sobre eventos o errores del sistema.

* 📊 **Widgets para Manejo de Datos (Entrada e Interacción):**
  * `ui-dropdown`: Menú desplegable de selección de opciones.
  * `ui-radio-group`: Grupo de botones de opción única.
  * `ui-form`: Formulario estructurado para recolectar múltiples campos de entrada en un solo envío.

* 📥 **Widgets para Manejo de Datos (Control de Tiempo y Selección Avanzada):**
  * `ui-date-picker`: Selector visual de fechas.
  * `ui-color-picker`: Paleta interactiva para seleccionar y enviar códigos de color RGB/HEX.

* 📈 **Widgets para Visualización de Datos:**
  * `ui-chart`: Gráficos dinámicos en tiempo real (líneas, barras, dispersión, torta).
  * `ui-gauge`: Indicadores analógicos o medidores de aguja/nivel para temperatura, presión, porcentaje, etc.

* ⚡ **Widgets para Control de Eventos:**
  * `ui-event`: Captura interacciones del usuario en el navegador (como clics o cambios de página) y las convierte en mensajes dentro del flujo de Node-RED.
  * `ui-control`: Permite controlar dinámicamente el comportamiento del dashboard desde el flujo (por ejemplo, cambiar de página automáticamente o cambiar el tema activo mediante un mensaje).
