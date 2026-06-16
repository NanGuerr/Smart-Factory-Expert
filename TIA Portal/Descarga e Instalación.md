# ⚙️ Guía de Descarga e Instalación de TIA Portal

## ⚠️ IMPORTANTE: Requisito previo (.NET Framework)
Para asegurar la compatibilidad con todas las funciones de TIA Portal y evitar errores durante la instalación, es obligatorio instalar **Microsoft .NET Framework 4.8** o superior antes de ejecutar el setup inicial. Es posible que tu equipo no cuente con esta versión instalada por defecto.

### Pasos para instalar .NET Framework 4.8
1. 🌐 **Descarga:** Accedé al [sitio oficial de Microsoft](https://learn.microsoft.com/dotnet/framework/install/).
2. 💻 **Compatibilidad:** Seleccioná la versión correspondiente a tu sistema Windows (10/11 64-bits).
3. 🛠️ **Instalación:** Ejecutá el instalador como administrador y **reiniciá el PC** al finalizar.
4. ✅ **Verificación:** Abrí el panel de “Agregar o quitar programas” en Windows y confirmá que **.NET Framework 4.8** aparezca en la lista.

---

## 🖥️ Requisitos mínimos del sistema
* **Sistema operativo:** Windows 10 o Windows 11 de 64 bits (No compatible con 32 bits).
* **Procesador:** Intel® Core™ i3 (~2,3 GHz) o equivalente.
* **Memoria RAM:** Mínimo 8 GB.
* **Almacenamiento:** Al menos 20 GB de espacio libre (SATA o superior).
* **Pantalla:** Resolución mínima 1024 × 768 píxeles.
* **Red:** Interfaz de red estándar.

## 🚀 Configuración recomendada
* **Sistema operativo:** Windows 10 o Windows 11 de 64 bits (actualizado).
* **Procesador:** Intel® Core™ i5 o superior.
* **Memoria RAM:** 16 GB o más (recomendable para proyectos de escala media o grande).
* **Almacenamiento:** Disco SSD con al menos 50 GB libres.
* **Pantalla:** Resolución Full HD (1920 × 1080) o superior para mayor comodidad.
* **Red:** Gigabit Ethernet (útil en entornos industriales o con simuladores).

---

## 🔗 Enlaces de interés
* 👤 [Registro en SiePortal](https://siemens.com)
* 📥 [Descarga de TIA V20](https://siemens.com)
* 🛡️ [Descarga de Automation License Manager (Fix)](https://siemens.com)
* ☁️ [Link alternativo (Drive)](https://drive.google.com)
* 🌍 Descarga de idiomas y actualizaciones (disponible en el portal).

---

## 🛠️ Fix para crear usuario y acceder al Updater
*Nota: Este procedimiento es útil para usuarios de Windows con login vía Microsoft Account o sin contraseña configurada.*

**1. Crear usuario:**
```cmd
net user tiaportal 123 /add

```

**2. Asignar permisos:**

```cmd
net localgroup administradores tiaportal /add

```

**3. Eliminar usuario provisorio (una vez finalizada la tarea):**

```cmd
net user tiaportal /delete

```
