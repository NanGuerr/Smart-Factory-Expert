import math
import time

class Valvula:
    def __init__(self, tipo="E", caudal=1.0):
        self.tipo = tipo  # "E" entrada, "S" salida
        self.caudal = caudal
        self.caudalActual = 0

    def abrirValvula(self):
        # Si es entrada, el flujo es positivo; si es salida, negativo.
        if self.tipo == "E":
            self.caudalActual = self.caudal
        else:
            self.caudalActual = -self.caudal

    def cerrarValvula(self):
        self.caudalActual = 0


class Tanque:
    def __init__(self, diametro=1.0, altura=1.0, valvulas=None):
        self.diametro = diametro
        self.altura = altura
        self.valvulas = valvulas if valvulas is not None else []
        
        # Variables internas
        self.nivelActual = 0     # Porcentaje (0-100%)
        self.volumenActual = 0   # Litros (o unidades cúbicas)
        self.volumenMaximo = 0
        
        # Inicializamos el volumen máximo al crear el objeto
        self.calcularNivel()

    def calcularNivel(self):
        # Fórmula: Volumen = Altura * Pi * Radio^2
        radio = self.diametro / 2
       
        # Convertimos a litros (1 m^3 = 1000 litros)
        self.volumenMaximo = (self.altura * math.pi * (radio ** 2)) * 1000  
       
        # Evitamos división por cero y calculamos el %
        if self.volumenMaximo > 0:
            self.nivelActual = (self.volumenActual / self.volumenMaximo) * 100
        else:
            self.nivelActual = 0

    def update(self, tiempo=1):
        # 1. Sumar caudales de todas las válvulas
        caudal_total = sum(v.caudalActual for v in self.valvulas)
        
        # 2. Calcular cuánta agua entró/salió en este intervalo
        variacion = caudal_total * tiempo
        self.volumenActual += variacion
        
        # 3. Calcular nivel y volumen máximo
        self.calcularNivel()
        
        # 4. Limitar (Clamping) para evitar errores físicos
        if self.volumenActual > self.volumenMaximo:
            self.volumenActual = self.volumenMaximo
        elif self.volumenActual < 0:
            self.volumenActual = 0
            
        # Recalcular nivel tras el límite
        self.calcularNivel()
        
        # 5. Esperar el tiempo de actualización
        time.sleep(tiempo)

    def cargarTanque(self):
        for v in self.valvulas:
            if v.tipo == "E":
                v.abrirValvula()
            else:
                v.cerrarValvula()

    def vaciarTanque(self):
        for v in self.valvulas:
            if v.tipo == "S":
                v.abrirValvula()
            else:
                v.cerrarValvula()

# --- Simulación ---

v1, v2, v3 = Valvula("E", 20), Valvula("E", 30), Valvula("S", 60)
tk1 = Tanque(diametro=1, altura=10, valvulas=[v1, v2, v3])

# Test 1: Carga (In: 50 L/s)
tk1.cargarTanque()
tk1.update(1)
print(f"Post-Carga: {tk1.nivelActual:.2f}% | {tk1.volumenActual:.2f}L de {tk1.volumenMaximo:.2f}L")

# Test 2: Vaciado (Out: 60 L/s)
# Como solo hay 50L, tras 1s de vaciado a 60L/s, el tanque debe quedar en 0 (Clamping)
tk1.vaciarTanque()
tk1.update(1)
print(f"Post-Vaciado: {tk1.nivelActual:.2f}% | {tk1.volumenActual:.2f}L")
