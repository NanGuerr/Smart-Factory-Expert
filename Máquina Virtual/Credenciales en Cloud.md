# Gestión y Generación de Credenciales en Google Cloud 🔑🔐

Este documento resume el procedimiento técnico para la creación y gestión de credenciales (Service Accounts) en el entorno de Google Cloud Platform (GCP), vital para la autenticación segura de servicios y aplicaciones.

## 1. Proceso de Creación de Cuentas de Servicio (Service Accounts) 📝
* **Acceso a la consola:** Se navega al menú de IAM y Administración -> Cuentas de Servicio.
* **Configuración inicial:** Definición del nombre de la cuenta de servicio y asignación de un ID único vinculado al proyecto.
* **Asignación de roles:** Selección de permisos específicos (IAM roles) para determinar qué acciones puede realizar la cuenta de servicio, siguiendo el principio de "menor privilegio".

## 2. Gestión de Claves y Autenticación 🔐
* **Generación de claves (JSON/P12):** Creación de claves privadas para permitir que las aplicaciones se autentiquen externamente ante las APIs de Google.
* **Seguridad:** Se enfatiza que el archivo de clave descargado es confidencial y debe protegerse para evitar accesos no autorizados.
* **Uso:** Estas credenciales son fundamentales para conectar servicios como Node-RED, BigQuery o cualquier aplicación externa con los recursos de GCP de manera segura.

## 3. Consideraciones de Seguridad 🛡️
* **Principio de menor privilegio:** Es fundamental otorgar solo los permisos estrictamente necesarios para la función de la cuenta.
* **Rotación de claves:** Se recomienda la rotación periódica de las claves para minimizar riesgos en caso de compromiso.
* **Almacenamiento seguro:** Nunca incluir los archivos de credenciales JSON en repositorios de código público (como GitHub).

---
*Resumen técnico basado en el flujo de trabajo de IAM en GCP.*
