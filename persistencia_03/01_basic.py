# --- 1. Escribiendo un archivo desde cero con el modo 'w' ---
lineas_a_escribir = ["Manzanas\n", "Peras\n", "Naranjas\n"]

# El archivo "lista_compras.txt" se creará (o se sobrescribirá si ya existe)
with open("lista_compras.txt", "w") as archivo:
    archivo.write("--- Mi Lista de Compras ---\n")
    archivo.writelines(lineas_a_escribir)
    print("Archivo 'lista_compras.txt' creado exitosamente.")

# --- 2. Añadiendo más contenido con el modo 'a' ---
with open("lista_compras.txt", "a") as archivo:
    archivo.write("Uvas\n")
    print("Se ha añadido un nuevo ítem a la lista.")


######### Leyendo desde un Archivo #########
# Asumimos que "lista_compras.txt" ya existe por el código anterior

print("\n--- Leyendo el archivo completo con .read() ---")
with open("lista_compras.txt", "r") as archivo:
    contenido_completo = archivo.read()
    print(contenido_completo)

print("\n--- Leyendo línea por línea con .readline() ---")
with open("lista_compras.txt", "r") as archivo:
    linea1 = archivo.readline()
    linea2 = archivo.readline()
    print(f"Primera línea: {linea1.strip()}")  # .strip() quita los saltos de línea
    print(f"Segunda línea: {linea2.strip()}")

print("\n--- Leyendo todas las líneas en una lista con .readlines() ---")
with open("lista_compras.txt", "r") as archivo:
    todas_las_lineas = archivo.readlines()
    print(todas_las_lineas)
    # Salida: ['--- Mi Lista de Compras ---\n', 'Manzanas\n', ...]


######### ✅ Método recomendado para leer archivos: #########
print("\n--- Leyendo con un bucle for (método recomendado) ---")
with open("lista_compras.txt", "r") as archivo:
    for numero_linea, linea in enumerate(archivo, 1):
        print(f"Línea {numero_linea}: {linea.strip()}")

# Example 2
# Escribir en un archivo .txt
with open("registro_sena.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Línea 1: Inicio de registro.\n")
    archivo.write("Línea 2: Proceso completado.\n")

# Leer el contenido de un archivo .txt
with open("registro_sena.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())  # .strip() elimina saltos de línea y espacios
