### 1️⃣ ¿Cómo leer los *Holding Registers* en formato Big-Endian?

El nodo **`MB_Server`** de `node-red-contrib-modbus` entrega los datos nativamente en forma de un búfer de bytes (`msg.payload` tipo `buffer`).

Para interpretar esos bytes como registros de 16 bits en orden **Big-Endian** (el estándar de red donde el byte más significativo *MSB* va primero), puedes utilizar un nodo **Function** conectado a la salida del servidor y extraer los valores usando los métodos nativos de JavaScript para buffers:

```javascript
// Suponiendo que msg.payload es un Buffer (ej. el puerto de holding registers)
let buf = msg.payload;
let valoresHolding = [];

// Recorremos el buffer de 2 en 2 bytes (cada registro Modbus = 16 bits = 2 bytes)
for (let i = 0; i < buf.length; i += 2) {
    // Lee un entero sin signo de 16 bits en formato Big-Endian
    let val = buf.readUInt16BE(i); 
    valoresHolding.push(val);
}

msg.payload = valoresHolding;
return msg;

```

Si prefieres evitar código manual, puedes conectar un nodo **`node-red-contrib-buffer-parser`** inmediatamente después del servidor para convertir automáticamente el búfer en un arreglo de números enteros eligiendo la opción de tipo `UInt16BE`.

---

### 2️⃣ ¿Por qué las *Coils* se ponen en un solo registro (búfer de bytes) y cómo saber a cuál pertenecen?

En el protocolo Modbus y en la arquitectura interna de Node-RED, las **Coils** (salidas digitales de 1 bit) y las *Discrete Inputs* **no se guardan como un array de booleanos independientes**, sino empaquetadas bit a bit dentro de un búfer de bytes.

* **¿Por qué?:** Cada byte del búfer almacena **8 coils juntas** (8 bits). Por ejemplo, el bit 0 del primer byte corresponde a la Coil 0, el bit 1 a la Coil 1, y así sucesivamente hasta completar el byte, pasando al siguiente para la Coil 8.
* **¿Cómo saber a cuál pertenecen?:** Para extraer el estado de una Coil específica sabiendo su dirección numérica (por ejemplo, la Coil con índice `n`), debes calcular en qué byte se encuentra y aplicar una operación de desplazamiento de bits (*bitmask*):

```javascript
let buf = msg.payload; // Búfer de coils del MB_Server
let numeroCoilDeseada = 5; // Ejemplo: queremos consultar la Coil #5

let byteIndex = Math.floor(numeroCoilDeseada / 8);
let bitIndex = numeroCoilDeseada % 8;

// Verificamos si el bit está encendido (1) o apagado (0)
let estadoCoil = (buf[byteIndex] & (1 << bitIndex)) !== 0;

msg.payload = estadoCoil;
return msg;

```
