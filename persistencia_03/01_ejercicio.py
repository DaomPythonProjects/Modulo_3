import os

# Constante para el nombre del archivo, facilita su modificación si es necesario.
NOMBRE_ARCHIVO = "productos.txt"

def cargar_productos(nombre_archivo):
    """
    Carga los productos desde un archivo de texto.

    Args:
        nombre_archivo (str): La ruta del archivo a leer.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa un producto.
              Retorna una lista vacía si el archivo no existe o está vacío.
    """
    productos = []
    # Verificar si el archivo existe antes de intentar leerlo
    if not os.path.exists(nombre_archivo):
        print(f"Advertencia: El archivo '{nombre_archivo}' no existe. Se creará uno nuevo al agregar un producto.")
        return productos

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # Omitir líneas en blanco
                if not linea.strip():
                    continue

                partes = linea.strip().split(',')

                # Validar que la línea tenga el formato esperado (nombre,precio)
                if len(partes) == 2:
                    nombre = partes[0]
                    try:
                        precio = float(partes[1])
                        productos.append({'nombre': nombre, 'precio': precio})
                    except ValueError:
                        print(f"Advertencia: Se omitió la línea '{linea.strip()}' por tener un precio no válido.")
                else:
                    print(f"Advertencia: Se omitió la línea '{linea.strip()}' por formato incorrecto.")
    except IOError as e:
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")

    return productos

def guardar_producto(nombre_archivo, producto):
    """
    Añade un nuevo producto al final del archivo.

    Args:
        nombre_archivo (str): La ruta del archivo donde se guardará el producto.
        producto (dict): Un diccionario con 'nombre' y 'precio' del producto.
    """
    try:
        # 'a' (append) para añadir al final sin sobrescribir el contenido existente.
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{producto['nombre']},{producto['precio']}\n")
        print(f"Producto '{producto['nombre']}' guardado correctamente.")
    except IOError as e:
        print(f"Error al escribir en el archivo '{nombre_archivo}': {e}")

def mostrar_productos(productos):
    """
    Muestra una lista de productos de forma ordenada en la consola.

    Args:
        productos (list): La lista de productos a mostrar.
    """
    if not productos:
        print("\n>> No hay productos para mostrar.")
        return

    print("\n--- LISTA DE PRODUCTOS ---")
    print(f"{'Producto':<20} | {'Precio':>10}")
    print("-" * 33)

    for producto in productos:
        # Formateamos el precio como moneda (ej: 1,250.50)
        precio_formateado = f"${producto['precio']:,.2f}"
        print(f"{producto['nombre']:<20} | {precio_formateado:>10}")
    print("-" * 33)

def main():
    """
    Función principal que ejecuta el menú interactivo del programa.
    """
    while True:
        # Cargar los productos siempre al inicio del bucle para tener la lista actualizada.
        lista_productos = cargar_productos(NOMBRE_ARCHIVO)

        print("\n--- MENÚ DE GESTIÓN DE PRODUCTOS ---")
        print("1. Mostrar todos los productos")
        print("2. Agregar un nuevo producto")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_productos(lista_productos)

        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto: ").strip()

            # Bucle para asegurar que el precio sea un número válido
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    if precio < 0:
                        print("El precio no puede ser negativo. Inténtelo de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Precio no válido. Por favor, ingrese solo números.")

            # Validar que el nombre no esté vacío
            if nombre:
                nuevo_producto = {'nombre': nombre, 'precio': precio}
                guardar_producto(NOMBRE_ARCHIVO, nuevo_producto)
            else:
                print("El nombre del producto no puede estar vacío.")

        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    main()
