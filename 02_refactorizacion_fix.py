# Módulo 3: Versión refactorizada del sistema de validación


def obtener_datos_usuario() -> tuple | None:
    """Pide al usuario su edad y tipo de entrada. Devuelve una tupla (edad, tipo) o None si hay un error."""
    try:
        edad = int(input("Por favor, introduce tu edad: "))
        tipo_entrada = input(
            "¿Qué tipo de entrada tienes (VIP, General o Estudiante)?: "
        ).upper()
        return edad, tipo_entrada
    except ValueError:
        print("Error: La edad debe ser un número válido.")
        return None


def validar_edad(edad: int) -> bool:
    """Valida la edad del usuario. Devuelve True si es válida, False en caso contrario."""
    if not (0 < edad < 100):
        print("Por favor, introduce una edad realista.")
        return False
    if edad < 18:
        print("Lo sentimos, este evento es solo para mayores de 18 años.")
        return False
    return True


def gestionar_acceso_por_entrada(tipo_entrada: str) -> str:
    """Determina el mensaje de acceso según el tipo de entrada."""
    match tipo_entrada:
        case "VIP":
            return "Acceso concedido a la zona VIP. ¡Disfruta!"
        case "GENERAL":
            return "Acceso concedido a la zona general. ¡Disfruta del evento!"
        case "ESTUDIANTE":
            return "Acceso concedido. Recuerda mostrar tu carné de estudiante."
        case _:
            return "Error: El tipo de entrada no es válido."


def generar_mensaje_adicional(tipo_entrada: str) -> str:
    """Genera un mensaje sobre bebidas basado en el tipo de entrada."""
    return (
        "Pasa a la barra por una bebida de cortesía."
        if tipo_entrada == "VIP"
        else "Puedes comprar bebidas en la barra."
    )


def main():
    """Función principal que orquesta el programa."""
    print("--- Bienvenido al sistema de validación de entradas (v2.0 Modular) ---")

    datos = obtener_datos_usuario()
    if datos is None:
        return  # Termina el programa si hubo un error en los datos

    edad_usuario, tipo_entrada_usuario = datos

    if validar_edad(edad_usuario):
        print(
            f"Edad verificada ({edad_usuario} años). Verificando entrada tipo {tipo_entrada_usuario}..."
        )

        mensaje_acceso = gestionar_acceso_por_entrada(tipo_entrada_usuario)
        print(mensaje_acceso)

        if mensaje_acceso.startswith("Acceso"):
            mensaje_bebida = generar_mensaje_adicional(tipo_entrada_usuario)
            print(mensaje_bebida)


# --- Punto de entrada del programa ---
if __name__ == "__main__":
    main()
