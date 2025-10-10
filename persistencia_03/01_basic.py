import os

# 1. Abrir el archivo y asignarlo a una variable
# Rutas Relativas y Absolutas
#archivo = open('../mi_archivo.txt', 'w') # Ruta Relativa
#archivo = open('D:\DevProjects\Python\Modulo_3\mi_archivo.txt', 'w') # Ruta Absoluta

# --- 1. Escribiendo un archivo desde cero con el modo 'w' ---
lineas_a_escribir = ["Manzanas\n", "Peras\n", "Naranjas\n"]

# Opciones de apertura de archivos:
# 'r' - Modo lectura (por defecto)
# 'w' - Modo escritura (crea o sobrescribe)
# 'a' - Modo añadir (agrega al final del archivo)
# 'x' - Modo exclusivo (falla si el archivo ya existe)

# # El archivo "lista_compras.txt" se creará (o se sobrescribirá si ya existe)
# with open("lista_compras.txt", "w") as archivo:
#     # Sola linea de texto
#     archivo.write("--- Mi Lista de Compras ---\n")
#     # Se utiliza para listas
#     archivo.writelines(lineas_a_escribir)
#     print("Archivo 'lista_compras.txt' creado exitosamente.")

# # --- 2. Añadiendo más contenido con el modo 'a' ---
# with open("lista_compras.txt", "a") as archivo:
#     archivo.write("Peras\n")
#     print("Se ha añadido un nuevo ítem a la lista.")


# ######### Leyendo desde un Archivo #########
# # Asumimos que "lista_compras.txt" ya existe por el código anterior
#
# print("\n--- Leyendo el archivo completo con .read() ---")
# with open("lista_compras.txt", "r") as archivo:
#     contenido_completo = archivo.read()
#     print(contenido_completo)
#
# print("\n--- Leyendo todas las líneas en una lista con .readlines() ---")
# with open("lista_compras.txt", "r") as archivo:
#     todas_las_lineas = archivo.readlines()
#     print(todas_las_lineas)
#     # Salida: ['--- Mi Lista de Compras ---\n', 'Manzanas\n', ...]
#
# print("\n--- Leyendo línea por línea con .readline() ---")
# with open("lista_compras.txt", "r") as archivo:
#     # linea1 = archivo.readline()
#     # linea2 = archivo.readline()
#     # print(f"Primera línea: {linea1.strip()}") # .strip() quita los saltos de línea
#     # print(f"Segunda línea: {linea2.strip()}")
#
#     for linea in archivo.readlines():
#         if linea.startswith("Manzanas"):
#             continue
#         print(linea.strip())  # .strip() quita los saltos de línea

######### ✅ Método recomendado para leer archivos: #########
file_lista = "lista_compras.txt"

if os.path.exists(file_lista):
    with open(file_lista, "a", encoding="utf-8") as archivo:
        archivo.write("Nuevo Elemento\n")

    print("\n--- Leyendo con un bucle for (método recomendado) ---")
    with open(file_lista, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, 1):
            print(f"Línea {numero_linea}: {linea.strip()}")
else:
    with open(file_lista, "w", encoding="utf-8") as archivo:
        archivo.write("Línea 1: Inicio de registro.\n")
        archivo.write("Línea 2: Proceso completado.\n")