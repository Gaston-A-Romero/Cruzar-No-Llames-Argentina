import os
from collections import defaultdict
import pandas as pd

# Usamos el directorio actual (donde está el script)
print("Generando archivo... Espere un momento")
directorio = os.getcwd()
# Guardar el archivo del no llames con el siguiente nombre (excluir fecha)
registro_txt = os.path.join(directorio, "Registro_No_Llame.txt")
numeros_excel = os.path.join(directorio, "números.xlsx")
salida_excel = os.path.join(directorio, "duplicados.xlsx")

# Declarar el hashmap con frecuencias
frecuencias = defaultdict(int)

# Leer registros del archivo de 'No Llame'
with open(registro_txt, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        numero = linea.strip()
        if numero:
            frecuencias[numero] += 1

print("Cantidad de números en el no llames: ", len(frecuencias))

# Leer el archivo de Excel
df_numeros = pd.read_excel(numeros_excel)

# Obtener la primera columna y convertir a string
columna_numeros = df_numeros.columns[0]
df_numeros[columna_numeros] = df_numeros[columna_numeros].astype(str)

# Limpiar espacios en claves del hashmap
frecuencias = {k.strip(): v for k, v in frecuencias.items()}
print("Numeros en el archivo de la base numeros.xlsx: ", len(df_numeros[columna_numeros]))

# Sumar 1 a la frecuencia si el número aparece en el archivo Excel
for num in df_numeros[columna_numeros]:
    num = num.strip()
    if num in frecuencias:
        frecuencias[num] += 1

# Filtrar los números cuya frecuencia final sea > 1 -> estan repetidos
duplicados = [num for num, count in frecuencias.items() if count > 1]

# Guardas en un nuevo archivo Excel
df_duplicados = pd.DataFrame(duplicados, columns=["Numero"])
df_duplicados.to_excel(salida_excel, index=False)

print(f"✔️ Archivo generado: {salida_excel} con {len(df_duplicados)} duplicados.")
