# 🏗️ Equipos

```python

from math import pi
class Tanque:
    def __init__(self,diametro,altura,nivel_maximo):
        self.diametro = diametro
        self.altura = altura
        self.nivel_maximo = nivel_maximo
        self.litros_actual = 0 
        self.nivel_actual = 0
​
    def llenar(self):
        pass
    
    def vaciar(self):
        pass
    
    def medirLitros(self):
        self.litros_actual = (((pi*((self.diametro/2)**2))*self.nivel_actual) / 1000)
        return self.litros_actual
​
class TanqueConValvulas(Tanque):
    def __init__(self, diametro, altura, nivel_maximo,valvulas):
        super().__init__(diametro, altura, nivel_maximo)
        self.valvulas = valvulas
​
    def abrir_valvula(self,indiceValvula):
        self.valvulas[indiceValvula].Abrir()
​
    def cerrar_valvula(self,indiceValvula):
        self.valvulas[indiceValvula].Cerrar()
​
    def update(self):
        self.litros_actual = self.litros_actual + sum([valvula.caudal for valvula in self.valvulas ])
        if self.litros_actual < 0:
            self.litros_actual = 0
        elif self.litros_actual > 2000:
            self.litros_actual = 2000
​
class Valvula:
    def __init__(self,tipo,caudalMax):
        assert (tipo == "Entrada" or tipo == "Salida"), "Tipo no admitido. Posibles: 'Entrada' ó 'Salida'"
        self.tipo = tipo
        self.caudalMax = caudalMax
        self.status = False #False = Cerrada, True = Abierta
        self.caudal = 0
    
    def Abrir(self):
        if self.tipo == "Entrada":
            self.caudal = self.caudalMax
        else:
            self.caudal = -self.caudalMax
            
        self.status = True
    
    def Cerrar(self):
        self.caudal = 0
        self.status = False
```

# ⏏️ Ejecucion

```python

import Equipos
import time
import matplotlib.pyplot as plt
import matplotlib.widgets as wg
​
valvula1 = Equipos.Valvula("Entrada", 15.0)
valvula2 = Equipos.Valvula("Salida", 50.0)
valvulas = [valvula1, valvula2]
​
Tanque = Equipos.TanqueConValvulas(300, 200, 80, valvulas)
​
mediciones = [0]
​
fig, ax2 = plt.subplots()
fig.subplots_adjust(bottom=0.25)
​
# Definimos las coordenadas y dimensiones del botón fuera del bucle while
ax_button1 = plt.axes([0.15, 0.05, 0.13, 0.095])
ax_button2 = plt.axes([0.45, 0.05, 0.13, 0.095])
ax_button3 = plt.axes([0.75, 0.05, 0.13, 0.095])
​
fig.subplots_adjust(bottom=0.25)
plt.style.use("seaborn-v0_8")
​
botonAbrir = wg.Button(ax_button1, 'Llenar')
botonCerrar = wg.Button(ax_button2, 'Cerrar')
botonVaciar = wg.Button(ax_button3, 'Vaciar')
​
def cmdLlenar(evento):
    print("LLENAR!")
    Tanque.abrir_valvula(0)
​
def cmdCerrar(evento):
    print("CERRAR!")
    Tanque.cerrar_valvula(0)
    Tanque.cerrar_valvula(1)
​
def cmdVaciar(evento):
    print("VACIAR!")
    Tanque.abrir_valvula(1)
​
botonAbrir.on_clicked(cmdLlenar)
botonCerrar.on_clicked(cmdCerrar)
botonVaciar.on_clicked(cmdVaciar)
​
try:
    while True:
        Tanque.update()
        mediciones.append(Tanque.litros_actual)
​
        ax2.clear()
        ax2.plot(mediciones, color="cadetblue")
        ax2.set_title("Llenado del tanque")
        plt.pause(0.17)
except KeyboardInterrupt:
    exit()
```
