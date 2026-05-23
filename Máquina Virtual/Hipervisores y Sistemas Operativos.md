# 🖥️ Instalación de Hipervisores y Sistemas Operativos (VIR-0106)

Este documento resume los principios y procedimientos para implementar entornos de virtualización, utilizando diversas herramientas y metodologías de instalación.

---

## 🛠️ Opciones de Hipervisores

| Hipervisor | Tipo | Características | Gratuito |
| :--- | :--- | :--- | :--- |
| **VMware Workstation** | Tipo 2 | Múltiples SO, snapshots, integración vSphere | Sí (Player) |
| **Microsoft Hyper-V** | Tipo 1/2 | Nativo en Windows, buen rendimiento | Sí |
| **Oracle VirtualBox** | Tipo 2 | Código abierto, interfaz intuitiva | Sí |
| **QEMU** | Tipo 2 | Emulación, soporta múltiples arquitecturas | Sí |

> **Nota:** Tipo 1 (Bare-Metal) corre sobre hardware; Tipo 2 (Hosted) corre sobre un SO existente.

---

## 🚀 Instalación: Oracle VM VirtualBox
Se seleccionó **VirtualBox** por ser liviano, gratuito y versátil.

1.  **Descarga:** Obtener el instalador desde la página oficial (sección "Downloads") para el sistema operativo host.
2.  **Procedimiento:** Instalación estándar. *Precaución:* El sistema se desconectará brevemente de Internet para instalar interfaces de red virtuales.
3.  **Ejecución:** Listo para crear máquinas virtuales (VMs).

---

## 💻 Instalación de Sistemas Operativos (Guest)

Existen tres formas principales de instalar un SO:

### 1. Instalación Desatendida (Ejemplo: Windows 10) 🪟
*   **Proceso:** Se utiliza una imagen ISO. VirtualBox detecta el SO y automatiza la configuración de usuarios y contraseñas.
*   **Complementos:** Es vital instalar los "Complementos del invitado" para habilitar el *drag-and-drop* y portapapeles compartido.

### 2. Instalación Manual (Ejemplo: Debian 12) 🐧
*   **Proceso:** Proceso extendido donde el usuario configura cada etapa (particionado, usuarios, servicios).
*   **Ventaja:** Permite una configuración al máximo detalle; ideal para entornos industriales o servidores ligeros (modo consola).

### 3. Instalación Empaquetada (Ejemplo: Kali Linux) 🛡️
*   **Proceso:** Importación de máquinas pre-configuradas (archivos `.vbox`).
*   **Ventaja:** Permite operar inmediatamente sin realizar procesos de instalación. Ideal para herramientas de ciberseguridad.

---

## ⚠️ Recomendaciones Importantes
*   **Gestión de recursos:** Cada VM ocupa espacio en disco; solo instale las que necesite.
*   **Limpieza:** Elimine las máquinas utilizadas para prácticas al finalizar para ahorrar espacio en su PC real.

# ⚙️ Configuraciones Adicionales de Dispositivos (VIR-0107)

Este módulo se centra en cómo ajustar el **hardware virtual** para mejorar el rendimiento, la conectividad y la interacción entre el sistema anfitrión (*host*) y la máquina virtual (*guest*). 🖥️🔄💻

---

### 📌 Puntos Clave

* **🎛️ Gestión de Recursos de Hardware:** Se detalla cómo modificar dinámicamente los recursos asignados a la VM, como la cantidad de núcleos de CPU 🧠, la memoria RAM ⚡ o el tamaño del disco virtual 💾, permitiendo escalabilidad según las necesidades de la aplicación.
  
* **🌐 Configuración de Red Avanzada:** Se exploran las diferentes modalidades de red, esenciales para laboratorios de pruebas:
    * **🌐 NAT:** Para acceso a internet compartido.
    * **🔀 Bridge (Puente):** Para que la VM tenga una IP propia en la red local.
    * **🔒 Red Interna:** Para comunicación exclusiva entre máquinas virtuales.

* **📂 Dispositivos de Interacción (Compartición):** Configuración de carpetas compartidas entre el sistema físico y la VM, así como la habilitación del portapapeles compartido 📋 y la funcionalidad de *drag-and-drop* (arrastrar y soltar) 🖱️ mediante los **"Complementos del Invitado"** (*Guest Additions*).

* **🔌 Periféricos Virtuales:** Adición o eliminación de hardware virtual como controladores USB 🎚️, unidades ópticas (para montar archivos ISO) 💿, tarjetas de sonido 🔊 y adaptadores de red adicionales que la máquina virtual pueda requerir para tareas específicas.

* **🗄️ Almacenamiento:** Configuración de controladores de disco (SATA, SCSI, NVMe) y la gestión de instantáneas (**snapshots**) 📸, que permiten guardar un estado determinado de la VM para regresar a él en caso de errores o configuraciones fallidas.

---

### 📝 Nota

⚠️ Este módulo es esencial para transformar una instalación básica de una VM en un **entorno de trabajo productivo** y adaptado a las necesidades específicas de un proyecto o laboratorio. 🚀

