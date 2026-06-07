# Tanque parte 1 (Esqueleto)
"""Crear el gemelo digital de un tanque de agua.
En la primera parte, vamos a crear solamente el "esqueleto" de nuestro tanque, dejando todas las funciones vacías.
Tanque parte 1: Armando el esqueleto
Resolver el ejercicio en código Python, vamos a crear nuestro gemelo digital! Para ello, primero vamos a trabajar creando la estructura básica. 
Crear las clases de dos objetos, Tanque y Válvula. A continuación, veremos los detalles de cada uno."""

class Tanque:
    def __init__(self, diametro=1.0, altura=1.0, valvulas=[]):
        # Atributos de entrada
        self.diametro = diametro
        self.altura = altura
        self.valvulas = valvulas
        
        # Variables internas
        self.nivelActual = 0
        self.caudal = 0
        self.volumenActual = 0
        self.volumenMaximo = 0

    def calcularNivel(self):
        pass

    def update(self, tiempo):
        pass

    def cargarTanque(self):
        pass

    def vaciarTanque(self):
        pass


class Valvula:
    def __init__(self, tipo ="E", caudal =1.0):
        # Atributos de entrada
        self.tipo = tipo  # "E" entrada, "S" salida
        self.caudal = caudal
        
        # Variables internas
        self.caudalActual = 0

    def abrirValvula(self):
        pass

    def cerrarValvula(self):
        pass
    
# --- Ejemplo de instanciación ---
# Creamos una válvula de entrada y una de salida
v1 = Valvula(tipo = "E", caudal = 2.5)
v2 = Valvula(tipo = "S", caudal = 1.8)

# Creamos el tanque con esas válvulas
mi_tanque = Tanque(diametro = 2.0, altura = 5.0, valvulas = [v1, v2])

print(f"Tanque creado con éxito. Altura: {mi_tanque.altura}m, Válvulas: {len(mi_tanque.valvulas)}")
