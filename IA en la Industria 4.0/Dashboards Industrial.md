
# 💬 Dashboards Industriales en Django

Este documento técnico combina la teoría de la estructuración de instrucciones (*prompts*) para Inteligencia Artificial con una guía práctica de desarrollo de software utilizando Python y Django para el monitoreo automatizado de variables de procesos. 🚀

---

## 🛠️ Caso de Estudio: Creación de un Dashboard Industrial

A continuación, aplicando la estructura del prompt propuesta, se define y ejecuta el desarrollo de una interfaz web industrial utilizando Python y Django.

### 📝 Prompt de Entrada Aplicado:
> *"Sos un experto en dashboards Python. Crea un dashboard funcional de datos utilizando el archivo synthetic-plc-tank.csv. Utiliza Python y Django, relacionado con automatización industrial. Que se ejecute usando el comando `python manage.py runserver`."*

---

## 💻 Código Fuente del Proyecto Django

A continuación se detalla la estructura y el código de los archivos principales para el despliegue del Dashboard.

### ⚙️ 1. Configuración de Rutas (`dashboard/urls.py`)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.industrial_dashboard, name='industrial_dashboard'),
]

```

### 🧠 2. Lógica del Servidor y Procesamiento (`dashboard/views.py`)

```python
import os
import pandas as pd
from django.shortcuts import render
from django.conf import settings

def industrial_dashboard(request):
    """
    Controlador para leer los datos del PLC (simulado) y calcular
    métricas en tiempo real para el operador de la planta.
    """
    # 📂 Fuente de datos definida en el prompt
    csv_name = "synthetic-plc-tank.csv"
    csv_path = os.path.join(settings.BASE_DIR, 'data', csv_name)
    
    # Datos de respaldo sintéticos si el archivo no existe en el directorio local
    if not os.path.exists(csv_path):
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        data_sintetica = {
            'timestamp': pd.date_range(start='2026-05-28 08:00', periods=6, freq='h'),
            'nivel_tanque_porcentaje': [45.2, 58.7, 72.1, 88.4, 91.2, 82.5],
            'presion_psi': [32.1, 34.5, 38.0, 42.1, 45.3, 41.0],
            'estado_valvula_bombeo': [1, 1, 1, 1, 0, 0]
        }
        df_creado = pd.DataFrame(data_sintetica)
        df_creado.to_csv(csv_path, index=False)

    # 🛠️ Procesamiento con Pandas
    df = pd.read_csv(csv_path)
    
    # Extracción de métricas clave (KPIs)
    ultimo_registro = df.iloc[-1]
    nivel_actual = float(ultimo_registro['nivel_tanque_porcentaje'])
    presion_actual = float(ultimo_registro['presion_psi'])
    estado_valvula = "ABIERTA 🟢" if ultimo_registro['estado_valvula_bombeo'] == 1 else "CERRADA 🔴"
    
    # Alertas lógicas de automatización
    alerta_critica = False
    if nivel_actual > 90.0:
        alerta_critica = "⚠️ CRÍTICO: RIESGO DE DESBORDAMIENTO EN TANQUE"
    elif presion_actual > 44.0:
        alerta_critica = "⚠️ ALERTA: SOBREPRESIÓN DETECTADA EN SISTEMA DE BOMBEO"

    # Conversión del histórico a formato compatible con Javascript Charts
    historico_json = df.to_dict(orient='records')

    context = {
        'nivel_actual': nivel_actual,
        'presion_actual': presion_actual,
        'estado_valvula': estado_valvula,
        'alerta_critica': alerta_critica,
        'historico': historico_json,
        'csv_fuente': csv_name
    }
    
    return render(request, 'dashboard/index.html', context)

```

### 🖥️ 3. Interfaz Gráfica (`dashboard/templates/dashboard/index.html`)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>⚙️ SCADA Dashboard - Automatización Industrial</title>
    <link rel="stylesheet" href="[https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css](https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css)">
    <script src="[https://cdn.jsdelivr.net/npm/chart.js](https://cdn.jsdelivr.net/npm/chart.js)"></script>
</head>
<body class="bg-light">

    <div class="container-fluid py-4">
        <header class="pb-3 mb-4 border-bottom d-flex justify-content-between align-items-center bg-dark text-white p-3 rounded">
            <span class="fs-4">🏭 HMI/SCADA Dashboard - Sistema de Tanque PLC</span>
            <span class="badge bg-secondary">Fuente: {{ csv_fuente }}</span>
        </header>

        {% if alerta_critica %}
        <div class="alert alert-danger role="alert">
            <h4 class="alert-heading">🚨 Alerta de Seguridad Activa</h4>
            <p class="mb-0 fw-bold">{{ alerta_critica }}</p>
        </div>
        {% endif %}

        <div class="row text-center mb-4">
            <div class="col-md-4">
                <div class="card card-body bg-white shadow-sm">
                    <h5 class="text-muted">🌊 Nivel del Tanque</h5>
                    <h2 class="display-5 fw-bold text-primary">{{ nivel_actual }} %</h2>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card card-body bg-white shadow-sm">
                    <h5 class="text-muted">💥 Presión Interna</h5>
                    <h2 class="display-5 fw-bold text-success">{{ presion_actual }} PSI</h2>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card card-body bg-white shadow-sm">
                    <h5 class="text-muted">🔌 Estado de Válvula Solenoide</h5>
                    <h2 class="display-6 fw-bold">{{ estado_valvula }}</h2>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-12">
                <div class="card card-body shadow-sm">
                    <h5 class="card-title">📈 Historial de Variables de Proceso (Series de Tiempo)</h5>
                    <canvas id="telemetriaChart" style="max-height: 400px;"></canvas>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Decodificación de la variable de contexto de Django
        const datosHistoricos = {{ historico|safe }};
        
        const timestamps = datosHistoricos.map(reg => reg.timestamp);
        const niveles = datosHistoricos.map(reg => reg.nivel_tanque_porcentaje);
        const presiones = datosHistoricos.map(reg => reg.presion_psi);

        const ctx = document.getElementById('telemetriaChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: timestamps,
                datasets: [
                    {
                        label: 'Nivel del Tanque (%)',
                        data: niveles,
                        borderColor: '#0d6efd',
                        backgroundColor: 'rgba(13, 110, 253, 0.1)',
                        yAxisID: 'y_nivel',
                        tension: 0.2
                    },
                    {
                        label: 'Presión (PSI)',
                        data: presiones,
                        borderColor: '#198754',
                        backgroundColor: 'transparent',
                        yAxisID: 'y_presion',
                        borderDash: [5, 5],
                        tension: 0.2
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    y_nivel: { type: 'linear', position: 'left', min: 0, max: 100 },
                    y_presion: { type: 'linear', position: 'right', min: 0, max: 60 }
                }
            }
        });
    </script>
</body>
</html>

```

---

## 📖 Explicación de la Solución de Ingeniería

El código desarrollado simula un entorno industrial **SCADA/HMI** integrado directamente con Django siguiendo las especificaciones del prompt:

1. **🔗 Integración de la Fuente (`synthetic-plc-tank.csv`):** En la vista de Django (`views.py`), se utiliza la biblioteca **Pandas** para conectarse al archivo de telemetría del PLC. Si el archivo no se encuentra en el directorio, el script cuenta con un bloque de contingencia automática que genera las series de tiempo iniciales del tanque.
2. **🧮 Lógica de Negocio y Automatización:** El servidor lee el dataframe de forma secuencial y extrae el último registro temporal disponible (estado instantáneo). Se aplica lógica booleana condicional para comprobar que las variables operativas no superen los límites seguros establecidos ($>90\%$ de capacidad o $>44\text{ PSI}$). En caso de anomalía, se inyecta dinámicamente un mensaje crítico en la interfaz.
3. **📊 Renderizado de Series de Tiempo:** Django empaqueta el histórico de datos en un diccionario nativo y lo envía de forma segura a la plantilla HTML. En el cliente frontend, **Chart.js** procesa este JSON creando un gráfico multi-eje (coexistencia de nivel y presión en la misma escala temporal), permitiendo a los operadores analizar tendencias y correlaciones de falla.
4. **🚀 Ejecución del Sistema:** El proyecto está estandarizado bajo el núcleo de Django. Para inicializar el servidor web de monitoreo de automatización, basta con abrir la terminal en la raíz del directorio y ejecutar el comando nativo:

```bash
python manage.py runserver

```

