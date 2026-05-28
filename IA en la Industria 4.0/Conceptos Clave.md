# 📚 Material Complementario

A continuación, se presentan las referencias conceptuales respecto a las interfaces de usuario, la ingeniería de instrucciones para IA y los entornos de despliegue web. 🚀

<p align="center"><img src="https://github.com/NanGuerr/Smart-Factory-Expert/blob/main/IA%20en%20la%20Industria%204.0/Estructura%20del%20Prompt.png?raw=true" width="80%"></p>

---

## 🏛️ Conceptos Clave

### 💬 Prompt
Un **Prompt** (o instrucción) es el conjunto de caracteres, palabras o bloques de texto que se introducen como entrada (*input*) a un modelo de Inteligencia Artificial Generativa (como LLMs o generadores de imágenes) para guiar su respuesta.

* 🎯 **Ingeniería de Prompts:** Consiste en estructurar estratégicamente la instrucción asignando un **Rol** (ej. *"Actúa como un experto en mantenimiento eléctrico"*), un **Contexto** claro, las **Restricciones** operativas y el **Formato** deseado para la salida.
* 📈 **Importancia:** En aplicaciones industriales, la claridad del prompt define directamente la precisión de las respuestas del modelo, minimizando el riesgo de alucinaciones.

### 📊 Dashboard
Un **Dashboard** (Panel de Control Visual) es una interfaz gráfica de usuario diseñada para consolidar, organizar y mostrar métricas clave de rendimiento (*KPIs*), alertas y datos críticos de manera centralizada y scannable.

* ⚙️ **Características:** Se alimenta frecuentemente de bases de datos o flujos de información en tiempo real (como series de tiempo de sensores). Utiliza gráficos interactivos, mapas de calor y tablas dinámicas.
* 🏭 **Caso de Uso:** En la Industria 4.0, un dashboard permite a los supervisores monitorear la salud de la maquinaria, predecir picos de consumo eléctrico y despachar alertas tempranas ante anomalías detectadas por modelos predictivos.

### 🐍 Django
**Django** es un framework de desarrollo web de alto nivel, de código abierto y escrito en Python, que fomenta un desarrollo rápido y un diseño limpio y pragmático.

* 🛠️ **Arquitectura:** Sigue el patrón MVT (*Model-View-Template*). Incluye herramientas nativas listas para usar ("*batteries included*"), como un panel de administración automático, un sistema de mapeo objeto-relacional (ORM) para bases de datos y robustas capas de seguridad contra vulnerabilidades web comunes.
* 🧠 **Uso en IA:** Es uno de los frameworks favoritos para desplegar proyectos de Machine Learning en entornos de producción, ya que permite integrar scripts complejos de Python, analítica de datos y APIs de inteligencia artificial dentro de una infraestructura web escalable y segura.

---

## 🗺️ Flujo de Integración en un Proyecto de IA 4.0

La relación entre estos tres conceptos dentro de una aplicación web industrial sigue comúnmente este orden lógico:

```text
┌────────────────────────┐      Envia peticiones      ┌────────────────────────┐
│   📊 1. DASHBOARD      │ ─────────────────────────► │      🐍 2. DJANGO      │
│ Interface de Usuario   │ ◄───────────────────────── │   Backend / Servidor   │
└────────────────────────┘      Devuelve métricas     └────────────────────────┘
                                                                  ▲
                                                                  │ Procesa el
                                                        Estructura│ modelo con
                                                        el prompt │ la telemetría
                                                                  ▼
                                                      ┌────────────────────────┐
                                                      │      💬 3. PROMPT      │
                                                      │ Entrada al Modelo de IA│
                                                      └────────────────────────┘
