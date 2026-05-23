# 🖥️ Principios de Virtualización (VIR-0101)

El módulo **VIR-0101: Principios de Virtualización** de IngelLearn introduce los conceptos fundamentales que permiten transformar la infraestructura de TI tradicional en un entorno flexible, eficiente y escalable.

A continuación, presento un resumen estructurado con los puntos clave tratados en esta unidad:

### 1. 🎯 Definición y Propósito
La **virtualización** es la tecnología que permite crear representaciones virtuales (basadas en software) de recursos físicos (hardware). Su objetivo principal es abstraer el software del hardware subyacente, permitiendo que un único servidor físico ejecute múltiples sistemas operativos y aplicaciones de forma aislada y simultánea.

### 2. 🔑 Conceptos Clave
Para comprender cómo funciona, es necesario distinguir dos componentes esenciales:
* **Máquina Virtual (VM) 💻:** Es un entorno informático aislado que actúa como si fuera una computadora independiente. Tiene su propia CPU virtual, memoria RAM, almacenamiento y sistema operativo. Se comporta como un "huésped" (*guest*) que vive dentro de un "anfitrión" (*host*).
* **Hipervisor (VMM - Virtual Machine Monitor) 🎼:** Es la capa de software fundamental que gestiona los recursos físicos y los distribuye entre las máquinas virtuales. Es el "director de orquesta" que asegura que cada VM reciba los recursos que necesita sin interferir con las demás.

### 3. 🏗️ Tipos de Hipervisores
El curso suele clasificar la virtualización según dónde reside el hipervisor:
* **Tipo 1 (Bare-metal) ⚙️:** Se instala directamente sobre el hardware del servidor. Es el estándar en entornos empresariales por su alto rendimiento y estabilidad (ejemplo: VMware ESXi, KVM).
* **Tipo 2 (Hosted) 🖥️:** Se instala sobre un sistema operativo ya existente (como Windows o Linux). Es común en estaciones de trabajo para pruebas o desarrollo (ejemplo: Oracle VirtualBox, VMware Workstation).

### 4. 🚀 Ventajas de la Virtualización
Implementar estos principios aporta beneficios estratégicos para cualquier organización:
* **Eficiencia de Hardware ⚡:** Aprovecha al máximo la capacidad de servidores modernos que, de otro modo, estarían infrautilizados.
* **Ahorro de Costos 💰:** Reduce la necesidad de comprar hardware físico adicional, disminuyendo gastos en energía, refrigeración y espacio en centros de datos.
* **Flexibilidad y Escalabilidad 📈:** Permite desplegar nuevos entornos en minutos, facilitar las copias de seguridad y acelerar la recuperación ante desastres.
* **Aislamiento 🛡️:** Si una máquina virtual falla o es comprometida, las demás permanecen intactas y seguras.

---

### 🔄 Resumen del flujo de trabajo
La virtualización convierte el **Hardware Físico** en un grupo de recursos compartidos (CPU, RAM, Red) que el **Hipervisor** segmenta y entrega a las **Máquinas Virtuales** según su configuración específica. Esto permite que, en un solo servidor físico, convivan distintos sistemas operativos (por ejemplo, un Windows y un Linux) funcionando de manera totalmente independiente.
