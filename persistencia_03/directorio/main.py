# -*- coding: utf-8 -*-
"""
Módulo Principal - Interfaz de Usuario (UI).

Punto de entrada de la aplicación.
Maneja la interacción con el usuario (menús, entradas, salidas) usando la librería rich.
"""

import os

import agenda  # Importamos nuestro módulo de lógica de negocio

# --- Importaciones de la librería Rich ---
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, IntPrompt, Prompt
from rich.table import Table

# --- Inicialización de la Consola de Rich ---
console = Console()

# --- Constantes de Configuración de Rutas ---
DIRECTORIO_DATOS = 'data'
NOMBRE_ARCHIVO_CSV = 'aprendices.csv'
NOMBRE_ARCHIVO_JSON = 'aprendices.json'

# --- Funciones de Interfaz de Usuario con Rich ---

def solicitar_tipo_documento(permitir_vacio: bool = False) -> str | None:
    """
    Muestra un menú para que el usuario elija el tipo de documento usando Rich.

    Args:
        permitir_vacio (bool): Si es True, permite la opción de no cambiar.

    Returns:
        str | None: La abreviatura del tipo de documento seleccionado o None.
    """
    console.print("\nSeleccione el tipo de documento:", style="cyan")
    tipos = {
        '1': 'C.C', '2': 'T.I', '3': 'R.C', '4': 'C.E', '5': 'Pasaporte', '6': 'PPT'
    }
    descripciones = {
        '1': 'Cédula de Ciudadanía', '2': 'Tarjeta de Identidad', '3': 'Registro Civil',
        '4': 'Cédula de Extranjería', '5': 'Pasaporte', '6': 'Permiso de Permanencia Temporal'
    }

    opciones = list(tipos.keys())
    prompt_texto = ""

    if permitir_vacio:
        prompt_texto += "[bold yellow]0[/bold yellow]. No cambiar\n"
        opciones.insert(0, '0')

    for key, value in descripciones.items():
        prompt_texto += f"[bold yellow]{key}[/bold yellow]. {value}\n"

    console.print(prompt_texto)

    opcion = Prompt.ask("Opción", choices=opciones, show_choices=False)

    if permitir_vacio and opcion == '0':
        return None
    return tipos[opcion]


def menu_crear_aprendiz(filepath: str):
    """Maneja la lógica para registrar un nuevo aprendiz."""
    console.print(Panel.fit("[bold cyan]📝 Registrar Nuevo Aprendiz[/bold cyan]"))

    tipo_documento = solicitar_tipo_documento()
    documento = IntPrompt.ask("Número de Documento")
    nombres = Prompt.ask("Nombres")
    apellidos = Prompt.ask("Apellidos")
    direccion = Prompt.ask("Dirección")
    telefono = IntPrompt.ask("Teléfono")
    ficha = IntPrompt.ask("Número de Ficha")

    aprendiz_creado = agenda.crear_aprendiz(
        filepath, tipo_documento, documento, nombres, apellidos, direccion, telefono, ficha
    )

    if aprendiz_creado:
        console.print(Panel(f"✅ ¡Aprendiz registrado con éxito!\n   ID Asignado: [bold yellow]{aprendiz_creado['id']}[/bold yellow]",
                            border_style="green", title="Éxito"))
    else:
        console.print(Panel("⚠️ No se pudo registrar al aprendiz. Verifique los datos.",
                            border_style="red", title="Error"))


def menu_leer_aprendices(filepath: str):
    """Maneja la lógica para mostrar todos los aprendices en una tabla."""
    console.print(Panel.fit("[bold cyan]👥 Lista de Aprendices[/bold cyan]"))
    aprendices = agenda.leer_todos_los_aprendices(filepath)

    if not aprendices:
        console.print("[yellow]No hay aprendices registrados.[/yellow]")
        return

    # Creamos la tabla
    tabla = Table(title="Aprendices Registrados", border_style="blue", show_header=True, header_style="bold magenta")
    tabla.add_column("ID", style="dim", width=5)
    tabla.add_column("Ficha", justify="right")
    tabla.add_column("Tipo Doc.", justify="center")
    tabla.add_column("Documento", justify="right")
    tabla.add_column("Nombre Completo")
    tabla.add_column("Teléfono", justify="right")

    # Ordenamos por Ficha y luego por ID
    aprendices_ordenados = sorted(aprendices, key=lambda x: (int(x['ficha']), int(x['id'])))

    for ap in aprendices_ordenados:
        tabla.add_row(
            ap['id'],
            ap['ficha'],
            ap['tipo_documento'],
            ap['documento'],
            f"{ap['nombres']} {ap['apellidos']}",
            ap['telefono']
        )

    console.print(tabla)


def menu_actualizar_aprendiz(filepath: str):
    """Maneja la lógica para actualizar un aprendiz."""
    console.print(Panel.fit("[bold cyan]✏️ Actualizar Datos de Aprendiz[/bold cyan]"))
    documento = IntPrompt.ask("Ingrese el Documento del aprendiz a actualizar")

    aprendiz_actual = agenda.buscar_aprendiz_por_documento(filepath, str(documento))
    if not aprendiz_actual:
        console.print("\n[bold red]❌ No se encontró ningún aprendiz con ese documento.[/bold red]")
        return

    console.print("\nDatos actuales. Presione Enter para no modificar un campo.")
    datos_nuevos = {}

    nuevo_tipo_doc = solicitar_tipo_documento(permitir_vacio=True)
    if nuevo_tipo_doc: datos_nuevos['tipo_documento'] = nuevo_tipo_doc

    nombres = Prompt.ask(f"Nombres ({aprendiz_actual['nombres']})", default=aprendiz_actual['nombres'])
    if nombres != aprendiz_actual['nombres']: datos_nuevos['nombres'] = nombres

    apellidos = Prompt.ask(f"Apellidos ({aprendiz_actual['apellidos']})", default=aprendiz_actual['apellidos'])
    if apellidos != aprendiz_actual['apellidos']: datos_nuevos['apellidos'] = apellidos

    direccion = Prompt.ask(f"Dirección ({aprendiz_actual['direccion']})", default=aprendiz_actual['direccion'])
    if direccion != aprendiz_actual['direccion']: datos_nuevos['direccion'] = direccion

    telefono = IntPrompt.ask(f"Teléfono ({aprendiz_actual['telefono']})", default=int(aprendiz_actual['telefono']))
    if telefono != int(aprendiz_actual['telefono']): datos_nuevos['telefono'] = telefono

    ficha = IntPrompt.ask(f"Ficha ({aprendiz_actual['ficha']})", default=int(aprendiz_actual['ficha']))
    if ficha != int(aprendiz_actual['ficha']): datos_nuevos['ficha'] = ficha

    if not datos_nuevos:
        console.print("\n[yellow]No se modificó ningún dato.[/yellow]")
        return

    aprendiz_actualizado = agenda.actualizar_aprendiz(filepath, str(documento), datos_nuevos)
    if aprendiz_actualizado:
        console.print(Panel("✅ ¡Datos del aprendiz actualizados con éxito!", border_style="green", title="Éxito"))
    else:
        console.print(Panel("❌ Ocurrió un error al actualizar.", border_style="red", title="Error"))


def menu_eliminar_aprendiz(filepath: str):
    """Maneja la lógica para eliminar un aprendiz."""
    console.print(Panel.fit("[bold cyan]🗑️ Eliminar Aprendiz[/bold cyan]"))
    documento = IntPrompt.ask("Ingrese el Documento del aprendiz a eliminar")

    aprendiz = agenda.buscar_aprendiz_por_documento(filepath, str(documento))
    if not aprendiz:
        console.print("\n[bold red]❌ No se encontró ningún aprendiz con ese documento.[/bold red]")
        return

    confirmacion = Confirm.ask(
        f"¿Está seguro de que desea eliminar a [bold]{aprendiz['nombres']} {aprendiz['apellidos']}[/bold]?",
        default=False
    )

    if confirmacion:
        if agenda.eliminar_aprendiz(filepath, str(documento)):
            console.print(Panel("✅ ¡Aprendiz eliminado con éxito!", border_style="green", title="Éxito"))
        else:
            console.print(Panel("❌ Ocurrió un error al eliminar.", border_style="red", title="Error"))
    else:
        console.print("\n[yellow]Operación cancelada.[/yellow]")


def elegir_almacenamiento() -> str:
    """Pregunta al usuario qué formato de archivo desea usar y construye la ruta."""
    console.print(Panel.fit("[bold cyan]⚙️ Configuración de Almacenamiento[/bold cyan]"))

    prompt_texto = (
        "¿Dónde desea almacenar los datos?\n"
        "[bold yellow]1[/bold yellow]. CSV (Archivo de texto plano)\n"
        "[bold yellow]2[/bold yellow]. JSON (Formato más estructurado)"
    )
    console.print(prompt_texto)

    opcion = Prompt.ask(
        "Opción",
        choices=["1", "2"],
        default="2",
        show_choices=False
    )
    if opcion == '1':
        return os.path.join(DIRECTORIO_DATOS, NOMBRE_ARCHIVO_CSV)
    else:
        return os.path.join(DIRECTORIO_DATOS, NOMBRE_ARCHIVO_JSON)

def mostrar_menu_principal():
    """Imprime el menú principal en la consola usando un Panel de Rich."""
    menu_texto = (
        "[bold yellow]1[/bold yellow]. Registrar un nuevo aprendiz\n"
        "[bold yellow]2[/bold yellow]. Ver todos los aprendices\n"
        "[bold yellow]3[/bold yellow]. Actualizar datos de un aprendiz\n"
        "[bold yellow]4[/bold yellow]. Eliminar un aprendiz\n"
        "[bold red]5[/bold red]. Salir"
    )
    console.print(Panel(menu_texto, title="[bold]AGENDA DE APRENDICES SENA[/bold]", subtitle="Seleccione una opción", border_style="green"))

def main():
    """Función principal que ejecuta el bucle del menú."""
    archivo_seleccionado = elegir_almacenamiento()
    console.print(f"\n👍 Usando el archivo: [bold green]{archivo_seleccionado}[/bold green]")

    while True:
        mostrar_menu_principal()
        opcion = Prompt.ask("Opción", choices=["1", "2", "3", "4", "5"], show_choices=False)

        if opcion == '1':
            menu_crear_aprendiz(archivo_seleccionado)
        elif opcion == '2':
            menu_leer_aprendices(archivo_seleccionado)
        elif opcion == '3':
            menu_actualizar_aprendiz(archivo_seleccionado)
        elif opcion == '4':
            menu_eliminar_aprendiz(archivo_seleccionado)
        elif opcion == '5':
            console.print("\n[bold magenta]👋 ¡Hasta luego! Gracias por usar la agenda.[/bold magenta]")
            break

# --- Punto de Entrada del Script ---
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold red]Programa interrumpido por el usuario. Adiós.[/bold red]")

