# ⚙️ Gemelo Digital: Sistema de Control de Turbina

## 1. Lógica del Modelo Físico (`Turbina.py`)
El procedimiento `update()` es el motor de la simulación:
* **Aceleración:** Solo ocurre si el `motorAux` y la `junta` están activos.
* **Quemadores:** Aportan energía solo si la turbina ya ha superado un umbral de seguridad (478 RPM).
* **Fricción:** Aplica un freno constante, evitando que la turbina genere energía infinita.

## 2. Implementación del Control PID
El método `PID` permite operar en dos modos:
* **Manual:** El usuario controla la válvula directamente desde el slider.
* **Automático:** El algoritmo PID ajusta la válvula automáticamente:
    * **Proporcional (P):** Reacciona al error instantáneo.
    * **Integral (I):** Corrige el error acumulado a lo largo del tiempo (evita el "offset").
    * **Derivativo (D):** Anticipa el cambio del error (amortigua la respuesta).

## 3. Arquitectura del Dashboard (Dash)
El sistema utiliza `dcc.Interval` para crear un bucle de refresco cada 150ms:
1. **Entrada de Usuario:** `Checklist` (nodos activos), `RadioItems` (Modo), `Slider` (Válvula manual).
2. **Procesamiento:** Los *callbacks* de Dash interceptan los cambios de estado y ejecutan `T1.PID()` o `T1.update()`.
3. **Salida Visual:** El `dcc.Graph` actualiza una gráfica de líneas en tiempo real mostrando la evolución de las RPM frente al Setpoint.

## 4. Flujo de Datos
- **Entrada:** `dcc.Interval` -> `callback` -> `Turbina.update()` -> Cálculo de RPM.
- **Registro:** `actualizarDF` -> `Pandas DataFrame` -> Visualización histórica en el gráfico.

### 💡 Observaciones Técnicas

* **Seguridad:** El modelo incluye una protección `if self.RPM <= 0: self.RPM = 0`, lo cual es vital para evitar estados físicos imposibles en la simulación.
* **Integración:** El uso de `global df` dentro del callback es una forma sencilla de persistir los datos de la sesión, aunque en aplicaciones de producción se recomienda usar `dcc.Store` para manejar el estado de los datos de manera más robusta.

Este código representa la implementación de un **Gemelo Digital** (*Digital Twin*) de una turbina industrial utilizando Python, Dash y lógica de control PID. Es un excelente ejemplo de cómo modelar procesos físicos dinámicos y controlarlos a través de una interfaz web. 🏭

### 📝 Resumen del Análisis

* **Modelo de la Turbina (`Turbina.py`):** Define el comportamiento físico. Utiliza una simulación de estado donde el RPM aumenta por el aporte de un motor auxiliar y quemadores, y disminuye por fricción.
* **Controlador PID:** Es el cerebro del sistema. Calcula de forma automática la apertura de la válvula (`Valvula`) comparando el valor actual de RPM con un valor objetivo (`Setpoint`), ajustando la salida mediante componentes Proporcional, Integral y Derivativo.
* **Interfaz y Dashboard (`main.py`):** Utiliza *Dash* para crear un tablero interactivo. Conecta los controles de la interfaz (sliders, botones, modos) con los métodos de la clase `Turbina` mediante *callbacks*.

#  Turbina.py

```python

class Turbina():
    def __init__(self):
        self.motorAux = False
        self.junta = False
        self.Q1 = False
        self.Q2 = False
        self.Valvula = 0.0
​
        self.friccion = 5 # La turbina debería frenarse...
        self.aporteMotor = 0.0
        self.aporteQuemadores = 0.0 
​
        self.RPM = 0.0
        self.modoAuto = False
        self.anteriores = []
​
    def update(self):
        if self.motorAux == True and self.junta == True:
            self.aporteMotor = 20.0 # Si motor+junta, acelera
        else:
            self.aporteMotor = 0.0 # Si no, no hay aporte
​
        if self.RPM > 478.0 and self.Q1 and self.Q2: 
            self.aporteQuemadores = self.Valvula
        else:
            self.aporteQuemadores = 0.0 # Cuándo hay aporte de velocidad de quemadores?
        
        self.RPM = self.RPM + (self.aporteMotor + self.aporteQuemadores - self.friccion)
        if self.RPM <= 0:
            self.RPM = 0
​
    def PID(self,input, Man_Auto = False, SetpointMan = 0.0, SetpointAuto = 0.0):
            """
                Calcula la salida de un controlador PID (Proporcional, Integral, Derivativo).
​
                Args:
                    Man_Auto (bool): Modo manual (True) o automático (False).
                    SetpointMan (bool): Ignorado si Man_Auto es True. Modo manual de setpoint (True) o automático (False).
                    SetpointAuto (float): El valor del setpoint en modo automático.
​
                Returns:
                    None
​
                El método calcula la salida del controlador PID utilizando el valor actual (input) y el setpoint (SetpointAuto).
                Se almacena el histórico de velocidades en self.anteriores y se limita a 100 elementos.
                Se calculan los componentes P, I y D del controlador y se suman para obtener la salida.
                La salida se limita al rango de 0 a 100.
​
                """
            if Man_Auto == False:     
                # Si el PID está en modo automático...
​
                # Almaceno el vector velocidad en una lista de 100 elementos.
                self.anteriores.append(input)
                if len(self.anteriores) > 100:
                    self.anteriores = self.anteriores[-100:]
​
                SP = SetpointAuto        
                E = SP - input
                self.error = E 
                
                #error es la diferencia entre lo que tengo, y mi setpoint actual. Usamos la lista para ello. 
                E_accu = [(SP - elem) for elem in self.anteriores[-20:]]
                self.error_accu = E_accu
                
                kP = 3.0
                kI = 0.0001
                kD = 0.01
​
                #La acción proporcional es el error multiplicado por una constante
                aP = self.error * kP
                
                #La acción integral es el área de los valores, dividido por la constante
                aI = (kP * (sum(self.error_accu) / (len(self.error_accu)*0.002) * kI))
​
                #La acción derivativa es la proyección a futuro (pendiente) del error, multiplicado por una constante
                if len(self.anteriores)>2:
                    aD = (self.error_accu[-1]-self.error_accu[-2])*kD*kP
                else:
                    aD = 0.0
                
                #sumamos las componentes de las acciones Proporcional, Integral y Derivativa
                Salida = self.Valvula + aP + aI + aD
​
                #Limitamos la válvula de salida
                if Salida < 0:
                    self.Valvula = 0
                elif Salida > 100:
                    self.Valvula = 100         
                else:
                    self.Valvula = Salida
​
            else:
                # Si estamos en modo "Manual", la válvula se pone en la posición que definimos en el setpoint.
                self.Valvula = SetpointMan

```

# main.py

```python

from dash import Dash, html, dcc, Output, Input, callback
import Turbina
import plotly.express as px
import pandas as pd
from datetime import datetime
​
T1 = Turbina.Turbina()
modo = False
datos = {"Fecha":[],
         "RPM":[],
         "Valv":[],
         "SP":[]
}
​
df = pd.DataFrame(datos)
app = Dash(__name__, title="Gemelo digital")
​
app.layout = html.Div([
​
    html.H1(children='Gemelo digital de turbina'),
    dcc.Checklist(options=["Motor Auxiliar","Junta", "Quemador 1", "Quemador 2"], value=[], id="selectora", inline=True),
    html.Br(),html.Br(),
    html.Div("Modo:"),
    dcc.RadioItems(options=["Manual","Automático"], value="Manual", id="selectoraModo", inline=True),
    html.Br(),
    html.Div("Válvula"),
    dcc.Slider(0,100,1,{i: str(i) for i in range(0,101,10)},0,id="slider"),
    html.H1(children=f"RPM: {T1.RPM:.2f}", id="textoTur"),
    dcc.Interval(id='actualiz', interval=150, n_intervals=0),
    dcc.Graph(figure={},id="Grafico")
])
​
def actualizarDF(df,RPM,Valv,SP):
    fila_nueva = {
            "Fecha":datetime.now(),
            "RPM":RPM,
            "Valv":Valv,
            "SP":SP
    }
    df.loc[len(df)] = fila_nueva
    df_nvo = df
    return df_nvo
​
@callback(
    Input("selectora","value")
)
def fun(valor):
    T1.motorAux = 'Motor Auxiliar' in valor
    T1.junta = 'Junta' in valor
    T1.Q1 = 'Quemador 1' in valor
    T1.Q2 = 'Quemador 2' in valor
​
@callback(
        Output("slider","value"),
        Input("slider","value"),
        Input("selectoraModo","value"),
        Input("actualiz","n_intervals")
)
def fun(slider,modo,act):
    if modo == "Manual":
        T1.PID(T1.RPM,Man_Auto=True,SetpointMan=slider)
        return slider
    else:
        T1.PID(T1.RPM,Man_Auto=False,SetpointAuto=4600)
        return T1.Valvula
​
@callback(
    Output("textoTur","children"),
    Input("actualiz","n_intervals")
)
def fun(valor):
    T1.update()
    return (f"RPM: {T1.RPM:.2f}")
​
@callback(
    Output("Grafico","figure"),
    Input("actualiz","n_intervals")
)
def fun(valor):
    global df
    df = actualizarDF(df,T1.RPM,T1.Valvula,4600)
    fig = px.line(df, x="Fecha", y=["RPM","SP"], title='Coso')
    return fig
​
​
if __name__ == '__main__':
    app.run(debug=True)

```
