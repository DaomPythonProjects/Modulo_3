# --- Constante Global ---
ARCHIVO_CONTACTOS = "contactos.csv"

# --- Funciones de Manejo de Datos ---


def cargar_contactos() -> list:
    """Lee el archivo CSV y devuelve una lista de contactos."""
    try:
        with open(ARCHIVO_CONTACTOS, "r") as archivo:
            lineas = archivo.readlines()
            contactos = []
            for linea in lineas:
                # Usamos .strip() para quitar saltos de línea y separamos por la coma
                nombre, telefono, email = linea.strip().split(",")
                contactos.append(
                    {"nombre": nombre, "telefono": telefono, "email": email}
                )
        return contactos
    except FileNotFoundError:
        # Si el archivo no existe, devolvemos una lista vacía
        return []


def guardar_contactos(contactos: list):
    """Guarda la lista de contactos en el archivo CSV."""
    with open(ARCHIVO_CONTACTOS, "w") as archivo:
        for contacto in contactos:
            linea = f"{contacto['nombre']},{contacto['telefono']},{contacto['email']}\n"
            archivo.write(linea)


# --- Funciones de Interfaz de Usuario ---


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Gestor de Contactos ---")
    print("1. Ver todos los contactos")
    print("2. Agregar un contacto")
    print("3. Modificar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")


def agregar_contacto(contactos: list):
    """Agrega un nuevo contacto a la lista."""
    print("\n--- Agregar Nuevo Contacto ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    guardar_contactos(contactos)
    print("¡Contacto agregado exitosamente!")


def ver_contactos(contactos: list):
    """Muestra todos los contactos."""
    print("\n--- Lista de Contactos ---")
    if not contactos:
        print("No hay contactos para mostrar.")
    else:
        for i, contacto in enumerate(contactos, 1):
            print(
                f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}"
            )


def modificar_contacto(contactos: list):
    """Modifica un contacto existente."""
    print("\n--- Modificar Contacto ---")
    ver_contactos(contactos)
    try:
        indice = int(input("Ingresa el número del contacto que deseas modificar: ")) - 1
        if 0 <= indice < len(contactos):
            contacto = contactos[indice]
            print(
                f"Modificando a {contacto['nombre']}. Deja en blanco para no cambiar."
            )
            nuevo_telefono = input(f"Nuevo teléfono ({contacto['telefono']}): ")
            nuevo_email = input(f"Nuevo email ({contacto['email']}): ")

            if nuevo_telefono:
                contacto["telefono"] = nuevo_telefono
            if nuevo_email:
                contacto["email"] = nuevo_email

            guardar_contactos(contactos)
            print("¡Contacto modificado exitosamente!")
        else:
            print("Número de contacto no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")


def eliminar_contacto(contactos: list):
    """Elimina un contacto de la lista."""
    print("\n--- Eliminar Contacto ---")
    ver_contactos(contactos)
    try:
        indice = int(input("Ingresa el número del contacto que deseas eliminar: ")) - 1
        if 0 <= indice < len(contactos):
            contacto_eliminado = contactos.pop(indice)
            guardar_contactos(contactos)
            print(f"¡Contacto '{contacto_eliminado['nombre']}' eliminado exitosamente!")
        else:
            print("Número de contacto no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")


# --- Lógica Principal del Programa ---


def main():
    """Función principal que ejecuta el bucle del programa."""
    contactos = cargar_contactos()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_contactos(contactos)
        elif opcion == "2":
            agregar_contacto(contactos)
        elif opcion == "3":
            modificar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    main()
