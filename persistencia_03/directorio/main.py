# -*- coding: utf-8 -*-
"""
Módulo Principal - Interfaz de Usuario (UI).

Punto de entrada de la aplicación.
Maneja la interacción con el usuario (menús, entradas, salidas).
"""

import os

import agenda  # Importamos nuestro módulo de lógica de negocio

# --- Constantes de Configuración de Rutas ---
DIRECTORIO_DATOS = 'data'
NOMBRE_ARCHIVO_CSV = 'aprendices.csv'
NOMBRE_ARCHIVO_JSON = 'aprendices.json'


# --- Funciones de Interfaz de Usuario ---

def solicitar_dato(mensaje: str, tipo: type = str, permitir_vacio: bool = False) -> any:
    """
    Solicita un dato al usuario y valida que no esté vacío y sea del tipo correcto.

    Args:
        mensaje (str): El mensaje a mostrar al usuario.
        tipo (type): El tipo de dato esperado (str, int).
        permitir_vacio (bool): Si es True, permite que el usuario presione Enter.

    Returns:
        any: El dato ingresado y validado.
    """
    while True:
        entrada = input(mensaje).strip()
        if not entrada and not permitir_vacio:
            print("❌ Error: Este campo no puede estar vacío.")
            continue
        if not entrada and permitir_vacio:
            return None # Retornamos None si se permite vacío y no se ingresa nada

        if tipo == int:
            if entrada.isdigit():
                return int(entrada)
            else:
                print("❌ Error: Por favor, ingrese un número válido.")
        elif tipo == str:
            return entrada

def solicitar_tipo_documento(permitir_vacio: bool = False) -> str | None:
    """
    Muestra un menú para que el usuario elija el tipo de documento.

    Args:
        permitir_vacio (bool): Si es True, la primera opción será no cambiar.

    Returns:
        str | None: La abreviatura del tipo de documento seleccionado o None.
    """
    print("Seleccione el tipo de documento:")
    tipos = {
        '1': 'C.C - Cédula de Ciudadanía',
        '2': 'T.I - Tarjeta de Identidad',
        '3': 'R.C - Registro Civil',
        '4': 'C.E - Cédula de Extranjería',
        '5': 'Pasaporte',
        '6': 'PPT - Permiso de Permanencia Temporal'
    }

    if permitir_vacio:
        print("  0. No cambiar")

    for key, value in tipos.items():
        print(f"  {key}. {value}")

    while True:
        opcion = input("Opción: ").strip()
        if permitir_vacio and opcion == '0':
            return None
        if opcion in tipos:
            # Retornamos la abreviatura, ej: 'C.C'
            return tipos[opcion].split(' - ')[0]
        else:
            print("❌ Opción no válida. Intente de nuevo.")


def menu_crear_aprendiz(filepath: str):
    """Maneja la lógica para registrar un nuevo aprendiz."""
    print("\n--- 📝 Registrar Nuevo Aprendiz ---")
    tipo_documento = solicitar_tipo_documento()
    documento = solicitar_dato("Número de Documento: ", tipo=int)
    nombres = solicitar_dato("Nombres: ")
    apellidos = solicitar_dato("Apellidos: ")
    direccion = solicitar_dato("Dirección: ")
    telefono = solicitar_dato("Teléfono: ", tipo=int)
    ficha = solicitar_dato("Número de Ficha: ", tipo=int)

    aprendiz_creado = agenda.crear_aprendiz(
        filepath, tipo_documento, documento, nombres, apellidos, direccion, telefono, ficha
    )

    if aprendiz_creado:
        print("\n✅ ¡Aprendiz registrado con éxito!")
        print(f"   ID Asignado: {aprendiz_creado['id']}")
    else:
        print("\n⚠️ No se pudo registrar al aprendiz. Verifique los datos.")

def menu_leer_aprendices(filepath: str):
    """Maneja la lógica para mostrar todos los aprendices."""
    print("\n--- 👥 Lista de Aprendices ---")
    aprendices = agenda.leer_todos_los_aprendices(filepath)

    if not aprendices:
        print("No hay aprendices registrados.")
        return

    # Ordenamos por Ficha (numérico) y luego por ID (numérico)
    aprendices_ordenados = sorted(aprendices, key=lambda x: (int(x['ficha']), int(x['id'])))

    for ap in aprendices_ordenados:
        print("-" * 35)
        print(f"  ID: {ap['id']}")
        print(f"  Tipo Documento: {ap['tipo_documento']}")
        print(f"  Documento: {ap['documento']}")
        print(f"  Nombre Completo: {ap['nombres']} {ap['apellidos']}")
        print(f"  Dirección: {ap['direccion']}")
        print(f"  Teléfono: {ap['telefono']}")
        print(f"  Ficha: {ap['ficha']}")
    print("-" * 35)

def menu_actualizar_aprendiz(filepath: str):
    """Maneja la lógica para actualizar un aprendiz."""
    print("\n--- ✏️ Actualizar Datos de Aprendiz ---")
    documento = solicitar_dato("Ingrese el Documento del aprendiz a actualizar: ", tipo=int)

    aprendiz_actual = agenda.buscar_aprendiz_por_documento(filepath, str(documento))
    if not aprendiz_actual:
        print("\n❌ No se encontró ningún aprendiz con ese documento.")
        return

    print("\nDatos actuales. Presione Enter para no modificar un campo.")

    datos_nuevos = {}

    # Actualizar tipo de documento
    nuevo_tipo_doc = solicitar_tipo_documento(permitir_vacio=True)
    if nuevo_tipo_doc: datos_nuevos['tipo_documento'] = nuevo_tipo_doc

    nombres = solicitar_dato(f"Nombres ({aprendiz_actual['nombres']}): ", permitir_vacio=True)
    if nombres: datos_nuevos['nombres'] = nombres

    apellidos = solicitar_dato(f"Apellidos ({aprendiz_actual['apellidos']}): ", permitir_vacio=True)
    if apellidos: datos_nuevos['apellidos'] = apellidos

    direccion = solicitar_dato(f"Dirección ({aprendiz_actual['direccion']}): ", permitir_vacio=True)
    if direccion: datos_nuevos['direccion'] = direccion

    telefono = solicitar_dato(f"Teléfono ({aprendiz_actual['telefono']}): ", tipo=int, permitir_vacio=True)
    if telefono: datos_nuevos['telefono'] = telefono

    ficha = solicitar_dato(f"Ficha ({aprendiz_actual['ficha']}): ", tipo=int, permitir_vacio=True)
    if ficha: datos_nuevos['ficha'] = ficha

    if not datos_nuevos:
        print("\nNo se modificó ningún dato.")
        return

    aprendiz_actualizado = agenda.actualizar_aprendiz(filepath, str(documento), datos_nuevos)
    if aprendiz_actualizado:
        print("\n✅ ¡Datos del aprendiz actualizados con éxito!")
    else:
        print("\n❌ Ocurrió un error al actualizar.")


def menu_eliminar_aprendiz(filepath: str):
    """Maneja la lógica para eliminar un aprendiz."""
    print("\n--- 🗑️ Eliminar Aprendiz ---")
    documento = solicitar_dato("Ingrese el Documento del aprendiz a eliminar: ", tipo=int)

    aprendiz = agenda.buscar_aprendiz_por_documento(filepath, str(documento))
    if not aprendiz:
        print("\n❌ No se encontró ningún aprendiz con ese documento.")
        return

    confirmacion = solicitar_dato(
        f"¿Está seguro de que desea eliminar a {aprendiz['nombres']} {aprendiz['apellidos']}? (s/n): "
    ).lower()

    if confirmacion == 's':
        if agenda.eliminar_aprendiz(filepath, str(documento)):
            print("\n✅ ¡Aprendiz eliminado con éxito!")
        else:
            print("\n❌ Ocurrió un error al eliminar.")
    else:
        print("\nOperación cancelada.")


def elegir_almacenamiento() -> str:
    """Pregunta al usuario qué formato de archivo desea usar y construye la ruta."""
    print("--- ⚙️ Configuración de Almacenamiento ---")
    while True:
        opcion = input("¿Dónde desea almacenar los datos? (1: CSV, 2: JSON): ").strip()
        if opcion == '1':
            return os.path.join(DIRECTORIO_DATOS, NOMBRE_ARCHIVO_CSV)
        elif opcion == '2':
            return os.path.join(DIRECTORIO_DATOS, NOMBRE_ARCHIVO_JSON)
        else:
            print("❌ Opción no válida. Por favor, elija 1 o 2.")

def mostrar_menu_principal():
    """Imprime el menú principal en la consola."""
    print("\n============== AGENDA DE APRENDICES SENA ==============")
    print("1. Registrar un nuevo aprendiz")
    print("2. Ver todos los aprendices")
    print("3. Actualizar datos de un aprendiz")
    print("4. Eliminar un aprendiz")
    print("5. Salir")
    print("=======================================================")

def main():
    """Función principal que ejecuta el bucle del menú."""
    archivo_seleccionado = elegir_almacenamiento()
    print(f"\n👍 Usando el archivo: {archivo_seleccionado}")

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            menu_crear_aprendiz(archivo_seleccionado)
        elif opcion == '2':
            menu_leer_aprendices(archivo_seleccionado)
        elif opcion == '3':
            menu_actualizar_aprendiz(archivo_seleccionado)
        elif opcion == '4':
            menu_eliminar_aprendiz(archivo_seleccionado)
        elif opcion == '5':
            print("\n👋 ¡Hasta luego! Gracias por usar la agenda.")
            break
        else:
            print("\n❌ Opción no válida. Por favor, intente de nuevo.")

# --- Punto de Entrada del Script ---
if __name__ == "__main__":
    main()

