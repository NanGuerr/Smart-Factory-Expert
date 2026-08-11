# 🔒 Funciones de seguridad en PLCs

Con el avance de las tecnologías, y la necesidad de conectar en red los dispositivos, surgió la necesidad de proteger los equipos que anteriormente no tenían ningún tipo de control de acceso, lo que los hace fácilmente vulnerables a cualquier ataque externo. 🛡️

Debido a ésto, a partir de la versión TIA Portal V17, y especialmente TIA Portal V20, se refuerzan las acciones de seguridad a tomar cada vez que insertamos un nuevo PLC en nuestro proyecto. Si insertamos un PLC con firmware V4.5 o superior, nos saldrá una ventana de configuración de seguridad, lo que nos guiará en el proceso de proteger nuestro PLC con autenticación. Aquí podemos darle contraseñas tanto al proyecto, e información sensible, como la administración de roles de usuario y filtrar qué tanto acceso se tiene a los bloques de programa del PLC, o incluso, conectarse online con él. 🔑

A continuación, veremos un detalle del procedimiento. Recuerden, si quieren prescindir de las configuraciones de seguridad, deben desmarcar las opciones relevantes y dar "full access" a todo el proyecto, o deben seleccionar un PLC con firmware menor, por ejemplo, el 4.2 que veníamos usando. ⚠️

> **¡Cuidado!** ⚠️ Presten atención a las credenciales que utilizan para proteger al PLC, y anótenlas en un lugar seguro si saben que no las recordarán. El perder acceso a las credenciales puede dejarles sin acceso al PLC, y probablemente requiera un reseteo completo físico para poder volver a trabajar con él, incluyendo el riesgo de perder el programa de una planta completa. Sean criteriosos cuando trabajen con las funciones de seguridad.

---

## ⚙️ Procedimiento de configuración de seguridad para S7-1200 FW > V4.5

1. **🚀 Inicio del asistente de seguridad del PLC:** Al insertar una CPU S7-1200, se abre el asistente de configuración de seguridad. En esta primera etapa se define la política general de protección que tendrá el equipo dentro del proyecto TIA Portal.
2. **🔐 Definición de contraseña para datos confidenciales:** Se establece una contraseña robusta para proteger los datos internos del PLC. Debe cumplir los requisitos mínimos de longitud y complejidad.
3. **📡 Configuración del modo de comunicación PG/PC y HMI:** Se habilita únicamente la comunicación segura entre el PLC y los dispositivos de ingeniería o HMI, desactivando modos legacy cuando no sean necesarios.
4. **👤 Activación del control de acceso del PLC:** Se habilita el control de acceso para que solo usuarios autenticados con los permisos adecuados puedan conectarse y operar el equipo.
5. **🛠️ Creación del usuario administrador del proyecto:** Se agrega al menos un usuario con rol de *PLC Administrator* para evitar quedar bloqueados del dispositivo. Aquí se crea el usuario local y se define su contraseña.
6. **📝 Definición de credenciales del administrador:** Se ingresan nombre de usuario y contraseña cumpliendo las reglas de complejidad establecidas por el sistema. Este usuario tendrá acceso completo al PLC.
7. **🚫 Configuración de acceso sin autenticación:** Se verifica que el acceso anónimo esté desactivado para impedir conexiones al PLC sin usuario y contraseña.
8. **🛡️ Selección del nivel de acceso mediante contraseña:** Se establece el nivel de protección del PLC, recomendando “Sin acceso (protección completa)” para obligar autenticación y control total de permisos.
9. **📋 Vista general de los ajustes seleccionados:** Se revisa el resumen de la configuración antes de finalizar el asistente, confirmando que el acceso sin autenticación esté deshabilitado y que la protección esté activa. Con esto finaliza el procedimiento estándar de configuración de seguridad para una CPU S7-1200 recién insertada.
10. **🗂️ Acceso a Usuarios y roles en la configuración de seguridad:** Desde el árbol del proyecto se ingresa a la administración de usuarios para verificar o ajustar permisos luego de finalizar el asistente.
11. **✅ Asignación de roles al usuario creado:** Se selecciona el usuario administrador y se le asigna el rol *PLC Administrator* para garantizar acceso completo al dispositivo.
