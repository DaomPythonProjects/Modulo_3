print("--- Bienvenido al sistema de validación de entradas ---")

# --- BLOQUE 1: OBTENER DATOS ---
try:
    edad = int(input("Por favor, introduce tu edad: "))
    tipo_entrada = input(
        "¿Qué tipo de entrada tienes (VIP, General o Estudiante)?: "
    ).upper()
except ValueError:
    print("Error: La edad debe ser un número válido.")
    exit()

# --- BLOQUE 2: VALIDAR EDAD ---
mensaje_acceso = ""
if not (0 < edad < 100):
    print("Por favor, introduce una edad realista.")
elif edad < 18:
    print("Lo sentimos, este evento es solo para mayores de 18 años.")
else:
    # --- BLOQUE 3: GESTIONAR TIPO DE ENTRADA ---
    print(f"Edad verificada ({edad} años). Verificando entrada tipo {tipo_entrada}...")
    match tipo_entrada:
        case "VIP":
            mensaje_acceso = "Acceso concedido a la zona VIP. ¡Disfruta!"
        case "GENERAL":
            mensaje_acceso = "Acceso concedido a la zona general. ¡Disfruta del evento!"
        case "ESTUDIANTE":
            mensaje_acceso = (
                "Acceso concedido. Recuerda mostrar tu carné de estudiante."
            )
        case _:
            mensaje_acceso = "Error: El tipo de entrada no es válido."

    print(mensaje_acceso)

    # --- BLOQUE 4: MENSAJE ADICIONAL ---
    if mensaje_acceso.startswith("Acceso"):
        mensaje_bebida = (
            "Pasa a la barra por una bebida de cortesía."
            if tipo_entrada == "VIP"
            else "Puedes comprar bebidas en la barra."
        )
        print(mensaje_bebida)
