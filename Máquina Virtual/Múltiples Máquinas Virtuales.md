# 👥 Manejo de Múltiples Máquinas Virtuales (VIR-0108 - 0110)

Este módulo se enfoca en las técnicas, herramientas y mejores prácticas para administrar, organizar y optimizar múltiples máquinas virtuales (*VMs*) ejecutándose en paralelo sobre un mismo sistema anfitrión. 💻🌐🎛️

---

### 📌 Puntos Clave

* **👥 Clonación de VMs:** Aprendizaje sobre los métodos para duplicar sistemas existentes de forma rápida y eficiente:
    * **📦 Clones Completos:** Copias totalmente independientes del sistema original.
    * **🔗 Clones Vinculados (*Linked Clones*):** Copias que comparten el disco base de la VM original, lo cual permite un ahorro masivo de espacio en almacenamiento.

* **🗂️ Grupos de Máquinas Virtuales:** Funcionalidades para la organización, categorización y administración conjunta de múltiples entornos, facilitando acciones masivas como encender 🟢, apagar 🔴 o pausar 🟡 varias VMs en grupo con un solo clic.

* **🕸️ Topologías y Redes Complejas:** Diseño y creación de arquitecturas de red internas avanzadas para la simulación de escenarios del mundo real. Incluye:
    * **🏠 Host-Only (Solo Anfitrión):** Comunicación exclusiva entre el host y las VMs.
    * **🔒 Redes Internas Personalizadas:** Ideales para simular entornos cliente-servidor, implementar cortafuegos (*firewalls*) 🧱 o desplegar laboratorios cerrados para pruebas de penetración (*pentesting*) 🛡️.

* **📉 Optimización de Recursos:** Estrategias y técnicas críticas para balancear y gestionar el impacto en los componentes físicos del sistema anfitrión (CPU 🧠, memoria RAM ⚡ y almacenamiento 💾) cuando se ejecutan múltiples sistemas operativos de forma simultánea.

---

### 📝 Nota

🚀 Dominar el manejo de múltiples máquinas virtuales es el paso definitivo para construir laboratorios de pruebas avanzados, permitiendo simular infraestructuras empresariales completas en una sola computadora física.

# 📸 Snapshots / Instantáneas (VIR-0109)

Este módulo profundiza en el uso de las **instantáneas (*snapshots*)**, una de las herramientas más potentes de la virtualización que funciona como un "botón de deshacer" para proteger y restaurar el estado de tus entornos virtuales. 🔄🛡️

---

### 📌 Puntos Clave

* **📸 ¿Qué es un Snapshot?:** Se explica cómo realizar una "fotografía" o captura exacta del estado de la máquina virtual en un momento específico, guardando el estado del disco virtual 💾, la memoria RAM ⚡ y la configuración de los periféricos.

* **🛡️ Entornos de Prueba Seguros:** Es el mecanismo ideal antes de realizar tareas de alto riesgo, tales como:
    * **🔄 Actualizaciones:** Instalar parches críticos del sistema operativo.
    * **🧪 Pruebas de Software:** Probar aplicaciones inestables o configuraciones complejas.
    * **⏪ Retorno Inmediato:** Si algo falla, se puede regresar al estado exacto guardado en segundos, evitando tener que reinstalar todo desde cero.

* **⚙️ Funcionamiento Interno:** Introducción al concepto de **discos diferenciales (archivos delta)**. El disco base original se congela en modo de "solo lectura" y todos los nuevos cambios se escriben en un archivo separado.

* **⚠️ Buenas Prácticas y Rendimiento:** Directrices esenciales para una administración sana del hipervisor:
    * **🚫 No son Backups:** Un snapshot depende del disco original; si el disco original se daña, el snapshot se pierde. No deben usarse como copias de seguridad definitivas.
    * **📉 Impacto en el Rendimiento:** Acumular demasiados snapshots o mantenerlos durante meses degrada la velocidad de lectura/escritura de la VM y consume espacio masivo en el host.
    * **🧹 Consolidación:** Aprender a borrar o fusionar los snapshots antiguos de forma correcta para liberar almacenamiento.

---

### 📝 Nota

💡 Saber gestionar los *snapshots* de manera eficiente te dará la total libertad de experimentar, romper y arreglar sistemas en tu laboratorio de pruebas sin miedo a perder horas de trabajo configurando software. 🚀

# 🌐 Configuraciones de Red (VIR-0110)

Este módulo profundiza en los diferentes modos de red disponibles en la virtualización, permitiendo entender cómo se comunican las máquinas virtuales entre sí, con el sistema anfitrión (*host*) y con el mundo exterior (Internet). 🖥️🔌🌍

---

### 📌 Puntos Clave

* **🌐 Modo NAT (Network Address Translation):**
    * **¿Cómo funciona?:** El hipervisor actúa como un enrutador virtual. La VM obtiene acceso a Internet utilizando la dirección IP del sistema anfitrión.
    * **Características:** Es la configuración por defecto. Protege a la máquina virtual, ya que el exterior no puede iniciar conexiones directamente hacia ella, pero la VM sí puede salir a la red externa.

* **🔀 Modo Bridge / Puente (Adaptador Puente):**
    * **¿Cómo funciona?:** La tarjeta de red de la VM se conecta directamente a la red física del anfitrión.
    * **Características:** La VM se comporta como una computadora física más en tu hogar u oficina. Obtiene su propia dirección IP directamente desde el router de tu red local (vía DHCP). Es ideal si necesitas que otros dispositivos físicos accedan a los servicios alojados en la VM (como un servidor web o de archivos).

* **🏠 Modo Host-Only (Solo-Anfitrión):**
    * **¿Cómo funciona?:** Crea una red privada virtual donde solo pueden comunicarse las máquinas virtuales y el sistema anfitrión.
    * **Características:** Las VMs no tienen acceso a Internet ni a la red local física. Es excelente para administrar entornos de laboratorio de manera segura desde tu sistema operativo principal sin exponerlos al exterior.

* **🔒 Modo Red Interna (Internal Network):**
    * **¿Cómo funciona?:** Permite la comunicación exclusiva entre las máquinas virtuales que compartan el mismo nombre de red interna.
    * **Características:** El sistema anfitrión (*host*) queda completamente aislado de esta red. Es la opción más segura y aislada para simular laboratorios complejos de malware, servidores DHCP/DNS propios o pruebas de infraestructura sin interferir con tu red real.

* **🛠️ Reenvío de Puertos (Port Forwarding):** 
    * Técnica esencial cuando se utiliza el modo NAT. Permite mapear un puerto específico del sistema anfitrión hacia un puerto de la máquina virtual (por ejemplo, redirigir el puerto `8080` del host al puerto `80` de la VM) para permitir accesos externos puntuales.

---

### 📝 Nota

⚠️ Configurar correctamente la red es vital en cualquier proyecto de TI. Elegir el modo adecuado evita conflictos de IP en tu red física y garantiza el aislamiento necesario para que tus experimentos de laboratorio corran de forma segura. 🚀
