# tests/test_gestor_contactos.py

import pytest

# Renombramos el módulo original para evitar conflictos de nombres
import proyecto_04.main as gestor

# --- Fixtures: Nuestros "Ingredientes" para las Pruebas ---


@pytest.fixture
def contactos_de_prueba():
    """Devuelve una lista de contactos de ejemplo para usar en las pruebas."""
    return [
        {"nombre": "Ana", "telefono": "111", "email": "ana@test.com"},
        {"nombre": "Carlos", "telefono": "222", "email": "carlos@test.com"},
    ]


@pytest.fixture
def archivo_temporal(tmp_path):
    """
    Crea un archivo de contactos temporal y seguro para una prueba.

    Usa la fixture 'tmp_path' de pytest que provee una ruta a un directorio temporal único.
    """
    # tmp_path nos da una ruta, creamos un archivo dentro de ella
    return tmp_path / "contactos_test.csv"


# --- Pruebas para Cargar y Guardar ---


def test_cargar_contactos_archivo_no_existe(archivo_temporal, monkeypatch):
    """
    Prueba que `cargar_contactos` devuelve una lista vacía si el archivo no existe.
    `monkeypatch` se usa para cambiar la variable global `ARCHIVO_CONTACTOS`
    dentro del módulo `gestor` para que apunte a nuestro archivo temporal.
    """
    # Arrange: Hacemos que la función a probar use nuestro archivo temporal
    monkeypatch.setattr(gestor, "ARCHIVO_CONTACTOS", str(archivo_temporal))

    # Act: Llamamos a la función
    contactos = gestor.cargar_contactos()

    # Assert: Verificamos que el resultado es el esperado
    assert contactos == []


def test_guardar_y_cargar_contactos(archivo_temporal, monkeypatch, contactos_de_prueba):
    """
    Prueba que los contactos guardados son los mismos que se cargan después.
    Este es un test de integración para `guardar_contactos` y `cargar_contactos`.
    """
    # Arrange: Apuntamos al archivo temporal
    monkeypatch.setattr(gestor, "ARCHIVO_CONTACTOS", str(archivo_temporal))

    # Act 1: Guardamos los contactos de prueba
    gestor.guardar_contactos(contactos_de_prueba)

    # Act 2: Cargamos los contactos desde ese mismo archivo
    contactos_cargados = gestor.cargar_contactos()

    # Assert: Verificamos que los datos cargados son idénticos a los originales
    assert contactos_cargados == contactos_de_prueba


# --- Pruebas para la Lógica de la Aplicación (con simulación de input) ---


def test_agregar_contacto(archivo_temporal, monkeypatch):
    """
    Prueba que la función `agregar_contacto` añade un nuevo contacto al archivo.
    """
    # Arrange 1: Apuntamos al archivo temporal
    monkeypatch.setattr(gestor, "ARCHIVO_CONTACTOS", str(archivo_temporal))

    # Arrange 2: Simulamos las entradas del usuario con monkeypatch.
    # Proporcionamos una lista de las respuestas que el usuario daría.
    entradas_simuladas = ["Nuevo Contacto", "333", "nuevo@test.com"]
    # `iter` convierte la lista en un iterador, `next` lo consumirá en cada llamada a `input`.
    monkeypatch.setattr("builtins.input", lambda _: next(iter(entradas_simuladas)))

    # Arrange 3: Empezamos con una lista vacía de contactos
    contactos_iniciales = []

    # Act: Ejecutamos la función que pide los datos al "usuario"
    gestor.agregar_contacto(contactos_iniciales)

    # Assert: Verificamos que el archivo ahora contiene el nuevo contacto
    contactos_cargados = gestor.cargar_contactos()
    assert len(contactos_cargados) == 1
    assert contactos_cargados[0]["nombre"] == "Nuevo Contacto"


def test_eliminar_contacto(archivo_temporal, monkeypatch, contactos_de_prueba):
    """
    Prueba que la función `eliminar_contacto` remueve un contacto existente.
    """
    # Arrange 1: Apuntamos al archivo temporal y lo pre-poblamos con datos
    monkeypatch.setattr(gestor, "ARCHIVO_CONTACTOS", str(archivo_temporal))
    gestor.guardar_contactos(contactos_de_prueba)

    # Arrange 2: Simulamos que el usuario elige eliminar el contacto número 2 ('Carlos')
    monkeypatch.setattr("builtins.input", lambda _: "2")

    # Arrange 3: Cargamos los contactos para pasarlos a la función
    contactos_actuales = gestor.cargar_contactos()

    # Act: Ejecutamos la función
    gestor.eliminar_contacto(contactos_actuales)

    # Assert: Verificamos que la lista guardada ahora solo tiene 1 contacto ('Ana')
    contactos_finales = gestor.cargar_contactos()
    assert len(contactos_finales) == 1
    assert contactos_finales[0]["nombre"] == "Ana"
