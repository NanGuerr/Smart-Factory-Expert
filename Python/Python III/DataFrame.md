# ℹ️ DataFrame

```python

import pandas as pd
import numpy as np
​
# Datos simulados de sensores
data = {
    'Tiempo': ['2023-08-01 08:00', '2023-08-01 09:00', '2023-08-01 10:00', '2023-08-01 11:00', '2023-08-01 12:00', '2023-08-01 13:00'],
    'Sensor': ['FT-001', 'FT-002', 'FT-001', 'FT-002', 'FT-001', 'FT-002'],
    'Temperatura (C)': [35.2, 36.5, 34.8, 37.2, 33.6, 37.9],
    'Presión (bar)': [2.1, 2.0, 2.2, 1.9, 2.5, 1.8]
}
​
# Crear un DataFrame a partir de los datos

df = pd.DataFrame(data)

```

# Creando una Serie

```python

import pandas as pd
import numpy as np
​
miLista = ["A", "B", "C", "D", "E"]
indices = ["uno","dos","tres","cuatro", "cinco"]
​
serie = pd.Series(miLista, index=indices)
serie["cinco"]

```



