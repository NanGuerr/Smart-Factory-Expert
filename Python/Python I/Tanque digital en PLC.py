import math
import time

class Turbina():
    def __init__(self):
        # --- ENTRADAS (Desde el PLC hacia la Turbina) ---
        self.Valvula = 0.0       # 0.0 a 100.0%
        self.motorAux = False    # Motor de arranque
        self.junta = False       # Acople neumático
        self.modoAuto = False    # Control Manual/Auto
        self.Ch1 = False         # Chispero 1
        self.Ch2 = False         # Chispero 2
        self.quemEmergencia = False
        self.chisperoEmergencia = False
        self.frenos = False      # Comando de frenos 

        # --- SALIDAS (Hacia el PLC / Sensores) ---
        self.Q1 = False          # Sensor de llama 1 
        self.Q2 = False          # Sensor de llama 2
        self.valvulaManualCerrada = False # 1 = Cerrada, 0 = Abierta 
        self.frenoAplicado = False
        self.RPM = 0.0

        # --- VARIABLES FÍSICAS INTERNAS ---
        self.friccion = 8.0      # Pérdida natural de velocidad
        self.limiteRPM = 6000.0  # Velocidad máxima según sensor 
        self.factorCombustion = 2.5 # Fuerza de los quemadores

    def update(self):
        """Simula la física de la turbina un segundo a la vez."""
        
        # 1. Aporte del motor auxiliar 
        # Debe ganarle a la fricción para que la máquina arranque
        aporteMotor = 25.0 if (self.motorAux and self.junta) else 0.0

        # 2. Lógica de ignición y llama 
        # Si hay combustible (valvula > 5%) y chisperos activos, se prenden los fuegos
        if self.Valvula > 5.0:
            if self.Ch1: self.Q1 = True
            if self.Ch2: self.Q2 = True
        else:
            # Si no hay combustible, la llama se apaga
            self.Q1 = self.Q2 = False

        # 3. Aporte de los quemadores 
        # Solo aportan velocidad si ambos están encendidos
        if self.Q1 and self.Q2:
            aporteQuemadores = self.Valvula * self.factorCombustion
        else:
            aporteQuemadores = 0.0

        # 4. Cálculo de inercia 
        # RPM = Velocidad Anterior + Aportes - Fricción
        nueva_velocidad = self.RPM + aporteMotor + aporteQuemadores - self.friccion
        
        # 5. Límites de RPM (No puede ser negativo ni superar el límite del sensor)  
        self.RPM = max(0.0, min(self.limiteRPM, nueva_velocidad))

# --- INICIO DE LA SECUENCIA DE CONTROL ---

TUR1 = Turbina()
segundos = 0

print(f"\n{'TIEMPO':<10}  | {'ESTADO':<20} |{'RPM':<10}| {'VÁLVULA':<10}")
print("-" * 60)

try:
    while segundos <= 30:
        # --- LÓGICA DE CONTROL ---
        
        if segundos < 5:
            # Prueba de inercia (Todo apagado)
            estado = "Inercia inicial"
            
        elif segundos < 10:
            # Prueba de Motor y Junta 
            estado = "Motor + Junta"
            TUR1.motorAux = True
            TUR1.junta = True
            
        elif segundos < 20:
            # Prueba de Ignición y Combustión 
            estado = "Ignición Quemadores"
            TUR1.Ch1 = TUR1.Ch2 = True # Chisperos 
            TUR1.Valvula = 30.0         # Abrimos gas
            
        elif segundos < 25:
            # Prueba sin motor
            estado = "Solo Quemadores"
            TUR1.motorAux = False
            TUR1.junta = False
            TUR1.Ch1 = TUR1.Ch2 = False
            
        else:
            # Corte de combustible 
            estado = "Corte de Gas"
            TUR1.Valvula = 0.0

        # --- ACTUALIZACIÓN DEL MODELO ---
        TUR1.update()
        
        # --- REPORTE ---
        print(f"{segundos:2}s         | {estado:<20} | {TUR1.RPM:7.2f}  | {TUR1.Valvula:4.1f}%")
        
        segundos += 1
        time.sleep(0.5) # Aceleramos la simulación 

except KeyboardInterrupt:
    print("\nSimulación interrumpida.")
