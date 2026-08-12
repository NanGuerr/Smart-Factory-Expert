## 📊 Análisis y Procesamiento de Archivos CSV en Node-RED

Cuando trabajamos con archivos CSV en Node-RED (utilizando el nodo CSV oficial de FlowFuse), los datos se convierten automáticamente en un arreglo de objetos JavaScript donde cada fila representa un elemento.

### 💻 Script para Procesar "X" Cantidad de Filas

Si necesitas procesar archivos con un número dinámico o indeterminado de filas (por ejemplo, para buscar un valor máximo como la corriente máxima), puedes utilizar el siguiente código dentro de un nodo **Function**:

```javascript
let arraycsv = msg.payload; // cargamos todo el contenido que viene del nodo csv
let nmro_registros = arraycsv.length; // obtenemos el largo del array (cant. elementos)

msg.index = nmro_registros;

flow.set("corriente_max", msg.payload[0].corriente);

for(let i = 0; i < nmro_registros; i++){
    if(flow.get("corriente_max") < msg.payload[i].corriente){
        flow.set("corriente_max", msg.payload[i].corriente);
    }
}

msg.payload = flow.get("corriente_max");
return msg;

```

---

### 🌐 Fuentes y Enlaces de Referencia

* 📖 **Wikipedia:** [Comma-separated values - Wikipedia](https://en.wikipedia.org/wiki/Comma-separated_values) 📄
* ⚙️ **FlowFuse:** [CSV Node Guide - FlowFuse](https://flowfuse.com/node-red/core-nodes/csv/) 🛠️
