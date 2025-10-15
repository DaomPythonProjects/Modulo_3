# -*- coding: utf-8 -*-
"""
Módulo de Lógica de Negocio.

Contiene todas las funciones para gestionar la agenda de aprendices (CRUD).
Este módulo utiliza 'gestor_datos' para la persistencia.
"""

from typing import Any, Dict, List, Optional

import gestor_datos


def generar_id(aprendices: List[Dict[str, Any]]) -> int:
    """
    Genera un nuevo ID autoincremental para un aprendiz.

    Args:
        aprendices (List[Dict[str, Any]]): La lista actual de aprendices.

    Returns:
        int: El nuevo ID a asignar.
    """
    if not aprendices:
        return 1
    max_id = max(int(ap.get('id', 0)) for ap in aprendices)
    return max_id + 1

def crear_aprendiz(
        filepath: str,
        tipo_documento: str,
        documento: int,
        nombres: str,
        apellidos: str,
        direccion: str,
        telefono: int,
        ficha: int
) -> Optional[Dict[str, Any]]:
    """
    (CREATE) Agrega un nuevo aprendiz a la agenda.

    Valida que el número de documento no exista antes de agregarlo.

    Args:
        filepath (str): Ruta al archivo de datos.
        tipo_documento (str): Abreviatura del tipo de documento (ej. 'C.C').
        documento (int): Número de documento del aprendiz.
        nombres (str): Nombres del aprendiz.
        apellidos (str): Apellidos del aprendiz.
        direccion (str): Dirección de residencia.
        telefono (int): Número de teléfono.
        ficha (int): Número de la ficha del programa.

    Returns:
        Optional[Dict[str, Any]]: El diccionario del aprendiz creado o None si ya existía.
    """
    aprendices = gestor_datos.cargar_datos(filepath)
    str_documento = str(documento)

    if any(ap.get('documento') == str_documento for ap in aprendices):
        print(f"\n❌ Error: El documento '{str_documento}' ya se encuentra registrado.")
        return None

    nuevo_id = generar_id(aprendices)

    nuevo_aprendiz = {
        'id': str(nuevo_id),
        'tipo_documento': tipo_documento,
        'documento': str_documento,
        'nombres': nombres,
        'apellidos': apellidos,
        'direccion': direccion,
        'telefono': str(telefono),
        'ficha': str(ficha)
    }

    aprendices.append(nuevo_aprendiz)
    gestor_datos.guardar_datos(filepath, aprendices)
    return nuevo_aprendiz

def leer_todos_los_aprendices(filepath: str) -> List[Dict[str, Any]]:
    """
    (READ) Obtiene la lista completa de aprendices.

    Args:
        filepath (str): Ruta al archivo de datos.

    Returns:
        List[Dict[str, Any]]: La lista de aprendices.
    """
    return gestor_datos.cargar_datos(filepath)

def buscar_aprendiz_por_documento(filepath: str, documento: str) -> Optional[Dict[str, Any]]:
    """
    Busca un aprendiz específico por su número de documento.

    Args:
        filepath (str): Ruta al archivo de datos.
        documento (str): El documento a buscar.

    Returns:
        Optional[Dict[str, Any]]: El diccionario del aprendiz si se encuentra, de lo contrario None.
    """
    aprendices = gestor_datos.cargar_datos(filepath)
    for aprendiz in aprendices:
        if aprendiz.get('documento') == documento:
            return aprendiz
    return None

def actualizar_aprendiz(
        filepath: str,
        documento: str,
        datos_nuevos: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """
    (UPDATE) Modifica los datos de un aprendiz existente.

    Args:
        filepath (str): Ruta al archivo de datos.
        documento (str): El documento del aprendiz a actualizar.
        datos_nuevos (Dict[str, Any]): Un diccionario con los campos a actualizar.

    Returns:
        Optional[Dict[str, Any]]: El diccionario del aprendiz actualizado, o None si no se encontró.
    """
    aprendices = gestor_datos.cargar_datos(filepath)
    aprendiz_encontrado = None
    indice = -1

    for i, aprendiz in enumerate(aprendices):
        if aprendiz.get('documento') == documento:
            aprendiz_encontrado = aprendiz
            indice = i
            break

    if aprendiz_encontrado:
        # Convertimos todos los nuevos valores a string para consistencia
        for key, value in datos_nuevos.items():
            datos_nuevos[key] = str(value)

        aprendiz_encontrado.update(datos_nuevos)
        aprendices[indice] = aprendiz_encontrado
        gestor_datos.guardar_datos(filepath, aprendices)
        return aprendiz_encontrado

    return None

def eliminar_aprendiz(filepath: str, documento: str) -> bool:
    """
    (DELETE) Elimina un aprendiz de la agenda.

    Args:
        filepath (str): Ruta al archivo de datos.
        documento (str): El documento del aprendiz a eliminar.

    Returns:
        bool: True si el aprendiz fue eliminado, False si no se encontró.
    """
    aprendices = gestor_datos.cargar_datos(filepath)
    aprendiz_a_eliminar = None

    for aprendiz in aprendices:
        if aprendiz.get('documento') == documento:
            aprendiz_a_eliminar = aprendiz
            break

    if aprendiz_a_eliminar:
        aprendices.remove(aprendiz_a_eliminar)
        gestor_datos.guardar_datos(filepath, aprendices)
        return True

    return False

