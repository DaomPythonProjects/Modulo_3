import csv

# Escribir en un archivo CSV
with open('aprendices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['nombre', 'programa', 'ficha'])
    writer.writerow(['Ana', 'ADSO', '2556080'])
    writer.writerow(['Luis', 'Sistemas', '2458091'])

# Leer un archivo CSV como diccionarios
with open('aprendices.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['nombre']} está en la ficha {row['ficha']}.")


# Se requiere instalar: pip install pandas
import pandas as pd

# Leer un CSV con una sola línea es muy fácil
df = pd.read_csv('aprendices.csv')
print(df)

# Agregar datos y guardar es igual de simple
nuevo_aprendiz = {'nombre': 'Maria', 'programa': 'ADSO', 'ficha': '2556080'}
df.loc[len(df)] = nuevo_aprendiz
df.to_csv('aprendices_actualizado.csv', index=False) # index=False evita guardar una columna extra con el índice