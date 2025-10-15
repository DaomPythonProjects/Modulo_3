# Definicion del Ejercicio
import csv
import json
import os

# Definimos los nombres de nuestros archivos de datos.
ARCHIVO_CSV = 'aprendices.csv'
ARCHIVO_JSON = 'aprendices.json'
# Definimos las columnas que usaremos. 'ficha' será nuestro identificador único.
CAMPOS = ['ficha', 'nombres', 'apellidos', 'direccion', 'telefono']

def inicializar_archivos():
    """
    Verifica si los archivos de datos existen. Si no, los crea con las cabeceras.
    """
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=CAMPOS)
            writer.writeheader()

    if not os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, mode='w', encoding='utf-8') as json_file:
            json.dump([], json_file) # Inicializa con una lista vacía

def cargar_datos():
    """
    Carga los datos desde el archivo JSON.
    Usamos JSON como fuente principal por la facilidad
    de manejo de estructuras de datos.
    """
    inicializar_archivos() # Nos aseguramos de que los archivos existan
    with open(ARCHIVO_JSON, mode='r', encoding='utf-8') as json_file:
        try:
            return json.load(json_file)
        except json.JSONDecodeError:
            # Si el archivo está vacío o corrupto, retornamos una lista vacía.
            return []

def guardar_datos(aprendices):
    """
    Guarda la lista completa de aprendices en ambos archivos (CSV y JSON).
    """
    # Guardar en JSON
    with open(ARCHIVO_JSON, mode='w', encoding='utf-8') as json_file:
        json.dump(aprendices, json_file, indent=4)

    # Guardar en CSV
    with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(aprendices)

def crear_aprendiz():
    """
    (CREATE) - Solicita los datos de un nuevo aprendiz y lo agrega a la agenda.
    """
    print("\n--- 📝 Registrar Nuevo Aprendiz ---")
    aprendices = cargar_datos()

    ficha = input("Número de Ficha: ").strip()

    # Verificamos que la ficha no exista para evitar duplicados
    if any(ap['ficha'] == ficha for ap in aprendices):
        print("\n❌ ¡Error! El número de ficha ya existe. Intente con otro.")
        return

    aprendiz = {'ficha': ficha}
    for campo in CAMPOS[1:]: # Solicitamos los demás campos (nombres, apellidos, etc.)
        aprendiz[campo] = input(f"{campo.replace('_', ' ').capitalize()}: ").strip()

    aprendices.append(aprendiz)
    guardar_datos(aprendices)
    print("\n✅ ¡Aprendiz registrado con éxito!")

def leer_aprendices():
    """
    (READ) - Muestra todos los aprendices registrados en la agenda.
    """
    print("\n--- 👥 Lista de Aprendices ---")
    aprendices = cargar_datos()

    if not aprendices:
        print("No hay aprendices registrados.")
        return

    for aprendiz in aprendices:
        print("-" * 25)
        print(f"  Ficha: {aprendiz['ficha']}")
        print(f"  Nombres: {aprendiz['nombres']}")
        print(f"  Apellidos: {aprendiz['apellidos']}")
        print(f"  Dirección: {aprendiz['direccion']}")
        print(f"  Teléfono: {aprendiz['telefono']}")
    print("-" * 25)

def actualizar_aprendiz():
    """
    (UPDATE) - Modifica los datos de un aprendiz existente, buscado por su ficha.
    """
    print("\n--- ✏️ Actualizar Datos de Aprendiz ---")
    aprendices = cargar_datos()
    ficha_a_buscar = input("Ingrese el Número de Ficha del aprendiz a actualizar: ").strip()

    aprendiz_encontrado = None
    indice = -1

    for i, aprendiz in enumerate(aprendices):
        if aprendiz['ficha'] == ficha_a_buscar:
            aprendiz_encontrado = aprendiz
            indice = i
            break

    if not aprendiz_encontrado:
        print("\n❌ No se encontró ningún aprendiz con esa ficha.")
        return

    print("\nDatos actuales del aprendiz. Presione Enter para no modificar un campo.")

    nuevos_datos = aprendiz_encontrado.copy()
    for campo in CAMPOS[1:]:
        valor_actual = aprendiz_encontrado[campo]
        nuevo_valor = input(f"{campo.capitalize()} ({valor_actual}): ").strip()
        if nuevo_valor: # Si el usuario ingresó algo, se actualiza.
            nuevos_datos[campo] = nuevo_valor

    aprendices[indice] = nuevos_datos
    guardar_datos(aprendices)
    print("\n✅ ¡Datos del aprendiz actualizados con éxito!")

def eliminar_aprendiz():
    """
    (DELETE) - Elimina un aprendiz de la agenda, buscado por su ficha.
    """
    print("\n--- 🗑️ Eliminar Aprendiz ---")
    aprendices = cargar_datos()
    ficha_a_eliminar = input("Ingrese el Número de Ficha del aprendiz a eliminar: ").strip()

    aprendiz_a_eliminar = None
    for aprendiz in aprendices:
        if aprendiz['ficha'] == ficha_a_eliminar:
            aprendiz_a_eliminar = aprendiz
            break

    if not aprendiz_a_eliminar:
        print("\n❌ No se encontró ningún aprendiz con esa ficha.")
        return

    confirmacion = input(f"¿Está seguro de que desea eliminar a {aprendiz_a_eliminar['nombres']} {aprendiz_a_eliminar['apellidos']}? (s/n): ").lower()

    if confirmacion == 's':
        aprendices.remove(aprendiz_a_eliminar)
        guardar_datos(aprendices)
        print("\n✅ ¡Aprendiz eliminado con éxito!")
    else:
        print("\nOperación cancelada.")

def mostrar_menu():
    """
    Muestra el menú principal de la aplicación.
    """
    print("\n============== AGENDA DE APRENDICES SENA ==============")
    print("1. Registrar un nuevo aprendiz")
    print("2. Ver todos los aprendices")
    print("3. Actualizar datos de un aprendiz")
    print("4. Eliminar un aprendiz")
    print("5. Salir")
    print("=======================================================")

def main():
    """
    Función principal que ejecuta el bucle del menú.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            crear_aprendiz()
        elif opcion == '2':
            leer_aprendices()
        elif opcion == '3':
            actualizar_aprendiz()
        elif opcion == '4':
            eliminar_aprendiz()
        elif opcion == '5':
            print("\n👋 ¡Hasta luego! Gracias por usar la agenda.")
            break
        else:
            print("\n❌ Opción no válida. Por favor, intente de nuevo.")

# --- Punto de Entrada del Script ---
# Este bloque asegura que la función main() solo se ejecute cuando el script es el archivo principal.
if __name__ == "__main__":
    main()
