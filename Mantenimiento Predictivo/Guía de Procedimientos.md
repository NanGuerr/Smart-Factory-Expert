# Guía de Procedimientos con el NASA Bearing Dataset 🛠️📊

<img width="812" height="441" alt="image" src="https://github.com/user-attachments/assets/af73c1a4-d0a8-4a0c-91f9-d4ba16a4d67e" />

Este documento presenta una síntesis estructurada, detallada y descriptiva de la aplicación de la Ciencia de Datos y el Aprendizaje Automático (*Machine Learning*) para el **Mantenimiento Predictivo** de componentes industriales críticos.

---

## 1. Contexto del Dataset: NASA Bearing Dataset 🌌🔍

El estudio de caso se basa en el **NASA Bearing Dataset**, alojado en la plataforma **Kaggle**. Este conjunto de datos es un referente global para el desarrollo de algoritmos de pronóstico y salud estructural (*Prognostics and Health Management - PHM*).

### ⚙️ Configuración del Banco de Ensayos (*Test Rig Setup*)
Los datos se obtuvieron mediante un experimento controlado diseñado por Qiu et al. (2006) para llevar los componentes mecánicos hasta su degradación total. Las condiciones del sistema físico fueron las siguientes:
* **Componentes bajo prueba:** Cuatro rodamientos de doble hilera **Rexnord ZA-2115** instalados sobre un mismo eje motriz.
* **Condición operativa:** Velocidad de rotación constante a **2000 RPM** mediante un motor de corriente alterna (AC) acoplado con correas de fricción (*rub belts*).
* **Carga mecánica:** Se aplicó una carga radial constante de **6000 lbs** sobre el eje y los rodamientos a través de un mecanismo de resorte.
* **Lubricación:** Todos los rodamientos contaron con un sistema de lubricación forzada.
* **Criterio de falla:** Todas las fallas del set de datos ocurrieron tras superar la vida útil de diseño estimada, la cual es mayor a **100 millones de revoluciones**.

### 📡 Distribución y Posición de Sensores
La captura de la condición interna de la máquina se instrumentó de la siguiente manera (Ver *Figure 1* en las imágenes):
* **Acelerómetros:** Se utilizaron sensores piezoeléctricos de alta sensibilidad **PCB 353B33 Quartz ICP**. 
    * *Set de datos 1:* Dos acelerómetros por rodamiento, orientados en los ejes ortogonales $x$ e $y$.
    * *Sets de datos 2 y 3:* Un acelerómetro por rodamiento colocado directamente en la carcasa del alojamiento.
* **Termocuplas:** Sensores de temperatura instalados para el monitoreo térmico continuo como variable complementaria.

---

## 2. Flujo de Trabajo del Modelo de Machine Learning 🔄💻

El análisis de vibraciones mecánicas para mantenimiento predictivo sigue una arquitectura clásica de tres etapas de procesamiento de datos:

```
[ Comportamientos (X) y Target (y) ] ➡️ [ Feature Engineering ] ➡️ [ Puntos de Datos al Modelo ]
```

### 🟩 Fase 1: Definición de Comportamientos (X) y Target (y)
* **Datos de Análisis Periódicos ($X$):** Muestreos de señales de vibración a alta frecuencia, específicamente a **20 kHz** (20,000 muestras por segundo). Esto permite capturar micro-impactos imperceptibles a bajas frecuencias.
* **Cantidad de puntos de medición por activo:** Volumen total de registros temporales capturados por cada acelerómetro.
* **Frecuencia de análisis:** Intervalos programados en los que el algoritmo evalúa la señal temporal.
* **Target o Variable Objetivo ($y$):** Clasificación binaria o categórica: **¿Falla o no falla?** (Estado Saludable vs. Estado Defectuoso).

### 🟦 Fase 2: Ingeniería de Características (*Feature Engineering*)
La señal cruda en el tiempo (*Raw Signal*) es compleja y ruidosa. Para extraer valor, se realiza un análisis de señales basado en la física del rodamiento. Dependiendo de dónde se localice el defecto, se generarán ondas de choque y envolventes a frecuencias específicas:
1.  **BPFO (*Ball Pass Frequency Outer race*):** Frecuencia de paso de las bolas por la pista externa.
2.  **BPFI (*Ball Pass Frequency Inner race*):** Frecuencia de paso de las bolas por la pista interna.
3.  **BSF (*Ball Spin Frequency*):** Frecuencia de rotación del elemento rodante (bola/rodillo).
4.  **FTF (*Fundamental Train Frequency*):** Frecuencia de la jaula del rodamiento.

*El análisis estructural extrae la **Señal de Envolvente (Envelope Signal)** de alta frecuencia para limpiar el ruido de fondo y aislar los picos cíclicos generados por las fisuras.*

### 🟪 Fase 3: Preparación de Puntos de Datos al Modelo
Consiste en la estructuración de la matriz de datos final para el entrenamiento del modelo predictivo:
* **Histórico de fallas:** Compilación de fallas previas y diagnósticos realizados por expertos.
* **Estadísticos descriptivos del dominio del tiempo:** Cálculo por ventana de período de la **Aceleración Promedio, Mediana, Varianza, Mínimo y Máximo**.
* **Identificación del tipo de comportamiento:** Clasificación de la signatura de la vibración según el área afectada (Pista Interna / Pista Externa / Elemento Rodante).

---

## 3. Glosario de Conceptos Fundamentales 📖🏢

Para la correcta implementación de la estrategia de la Industria 4.0, se definen los siguientes términos clave:

* **Vibraciones mecánicas:** Movimiento oscilatorio de componentes mecánicos en equipos industriales. Su medición y análisis permiten detectar anomalías, desgastes o fallas incipientes.
* **Elementos rotativos:** Componentes mecánicos que giran durante la operación de una máquina (ejes, rotores, turbinas), monitoreados para anticipar fallas mediante Inteligencia Artificial.
* **Rodamientos / Cojinetes / Rolling Bearings:** Elementos mecánicos diseñados para reducir la fricción entre partes móviles, soportando cargas y facilitando la rotación. Son componentes sumamente críticos.
* **Frecuencia de vibración:** Número de ciclos de vibración en un intervalo de tiempo, expresado en Hertz (Hz). Indicador clave para identificar el origen y tipo de falla.
* **Kaggle:** Plataforma colaborativa en línea de ciencia de datos y aprendizaje automático utilizada para obtener conjuntos de datos (*datasets*) validados a nivel de investigación industrial.
