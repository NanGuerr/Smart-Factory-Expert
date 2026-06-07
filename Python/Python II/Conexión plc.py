from pymodbus.client import ModbusSerialClient

# ==========================================
# 1. Configuración de la Conexión
# ==========================================
# Ajusta estos parámetros para que coincidan con la configuración 
# de comunicación de tu SINAMICS V20 (Parámetros P2010, P2014, etc.)
client = ModbusSerialClient(
    port='COM3',      # En Windows 'COMx', en Linux suele ser '/dev/ttyUSB0'
    baudrate=9600,    # Velocidad de transmisión (Revisar P2010 en el V20)
    bytesize=8,
    parity='E',       # 'E' (Even/Par), 'O' (Odd/Impar), 'N' (None/Ninguna)
    stopbits=1,
    timeout=1         # Tiempo de espera de respuesta en segundos
)

# ==========================================
# 2. Datos de la Lectura
# ==========================================
SLAVE_ID = 1          # Dirección Modbus del VFD en la red (Revisar P2011)
REGISTER_ADDRESS = 24 # El offset de 40025 (40025 - 40001 = 24)
COUNT = 1             # Cantidad de registros a leer

# ==========================================
# 3. Ejecución
# ==========================================
print("Intentando conectar con el equipo...")

if client.connect():
    print("Conexión serial establecida. Leyendo registro...")
    
    # Utilizamos FC 03 (Read Holding Registers)
    response = client.read_holding_registers(
        address=REGISTER_ADDRESS, 
        count=COUNT, 
        slave=SLAVE_ID
    )
    
    # Comprobar si hubo un error en la lectura
    if not response.isError():
        # Obtenemos el valor crudo (0 - 65535)
        raw_value = response.registers[0]
        
        # Conversión a entero con signo (Complemento a 2 para 16 bits)
        # Si el bit más significativo está encendido (> 32767), el número es negativo.
        if raw_value > 32767:
            rpm = raw_value - 65536
        else:
            rpm = raw_value
            
        # Comprobar que esté dentro de los límites del manual
        if -16250 <= rpm <= 16250:
            print(f"✅ Lectura exitosa: La velocidad actual es {rpm} RPM")
        else:
            print(f"⚠️ Valor fuera de los límites esperados: {rpm} (Crudo: {raw_value})")
            
    else:
        print(f"❌ Error al leer el registro Modbus: {response}")
        
    # Siempre cerrar el puerto al terminar
    client.close()
else:
    print("❌ No se pudo abrir el puerto serial. Verifica el 'port' y si el cable está conectado.")
