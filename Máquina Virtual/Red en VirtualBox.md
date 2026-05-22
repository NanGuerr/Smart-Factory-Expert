# Configuración de Red en VirtualBox 🌐

Para configurar la conectividad de red en una máquina virtual de VirtualBox, existen cuatro tipos de adaptadores principales, cada uno diseñado para necesidades específicas. Aquí tienes los más útiles y cuándo usarlos:

### 1. NAT (Network Address Translation) 🌍
Es el modo predeterminado y el más sencillo para empezar.
* **Cómo funciona:** La máquina virtual accede a Internet a través de la dirección IP del equipo anfitrión (tu computadora real). La red interna de la MV está oculta detrás del anfitrión.
* **Cuándo usarlo:** Cuando solo necesitas que tu máquina virtual tenga acceso a Internet para navegar o descargar actualizaciones, sin necesidad de que otros dispositivos se comuniquen con ella.

### 2. Adaptador Puente (Bridged Adapter) 🌉
Este modo conecta la máquina virtual directamente a tu red física.
* **Cómo funciona:** La MV se comporta como si fuera otro dispositivo físico conectado a tu router (o switch). Obtendrá su propia dirección IP dentro de la misma subred que tu computadora anfitriona.
* **Cuándo usarlo:** Cuando necesitas que otros equipos de tu red local (otros PCs, impresoras, servidores) puedan ver y comunicarse directamente con tu máquina virtual, o si estás haciendo pruebas de red avanzadas.

### 3. Red Interna (Internal Network) 🔒
Crea una red aislada que solo existe dentro de VirtualBox.
* **Cómo funciona:** Las máquinas virtuales configuradas en la misma "Red Interna" pueden comunicarse entre sí, pero no tienen acceso al mundo exterior (Internet) ni pueden comunicarse con el equipo anfitrión.
* **Cuándo usarlo:** Para entornos de laboratorio seguros, pruebas de servidores (como un clúster de bases de datos o un dominio de Active Directory) que no deben exponerse a la red física o a Internet.

### 4. Adaptador Solo-Anfitrión (Host-Only Adapter) 💻
Es un híbrido entre red interna y adaptador puente.
* **Cómo funciona:** Crea una red privada entre la máquina virtual y el equipo anfitrión. La MV puede hablar con el anfitrión (y viceversa), pero no tiene acceso a Internet ni a la red local física.
* **Cuándo usarlo:** Cuando necesitas que el equipo anfitrión gestione la máquina virtual (por ejemplo, mediante SSH desde la terminal del anfitrión) de forma privada y segura, sin que el resto de la red local pueda acceder a esa MV.

---

## Resumen Comparativo 📊

| Modo | ¿Acceso a Internet? | ¿Visible para otros en la red? | ¿Acceso desde el Anfitrión? |
| :--- | :---: | :---: | :---: |
| **NAT** | Sí | No | No (por defecto) |
| **Puente** | Sí | Sí | Sí |
| **Red Interna** | No | No | No |
| **Solo-Anfitrión** | No | No | Sí |
