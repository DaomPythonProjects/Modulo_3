# 🐍 Módulo 3: Funciones y Modularización en Python

¡Bienvenido al Módulo 3! Este repositorio está diseñado para ser una guía completa y práctica sobre funciones, modularización y manejo de archivos en Python. Aquí, damos el salto de escribir scripts simples a construir programas verdaderos, empaquetando nuestro código en bloques lógicos y reutilizables llamados funciones.

## 🎯 Objetivo del Módulo

- **Diseñar programas modulares y organizados** mediante el uso de funciones.
- **Desarrollar la capacidad de gestionar la persistencia de datos**, realizando operaciones básicas de lectura y escritura en archivos de texto.

## 📋 Contenidos del Repositorio

### 1. Funciones y Modularización

- **`01_funciones.py`**: Conceptos básicos de funciones, parámetros, argumentos (`*args`, `**kwargs`) y alcance de variables (scope).
- **`02_refactorizacion_origin.py`**: Un ejemplo de un script monolítico.
- **`02_refactorizacion_fix.py`**: El mismo script refactorizado en funciones, demostrando las ventajas de la modularización.

### 2. Persistencia de Datos

La carpeta `persistencia_03` contiene ejemplos de cómo leer y escribir datos en diferentes formatos:

- **`01_basic.py`**: Lectura y escritura de archivos de texto plano (`.txt`).
- **`02_csv_files.py`**: Manejo de archivos CSV (Valores Separados por Comas).
- **`03_json_files.py`**: Trabajo con archivos JSON (JavaScript Object Notation).
- **`04_pickle_files.py`**: Serialización de objetos de Python con Pickle.
- **`05_json_full.py`**: Un ejemplo más completo de cómo usar JSON en una aplicación.

### 3. Proyecto Integrador

La carpeta `proyecto_04` contiene un mini-proyecto que aplica todos los conceptos aprendidos en el módulo:

- **`main.py`**: Un gestor de contactos simple que permite agregar, ver, modificar y eliminar contactos, guardando la información en un archivo CSV.

### 4. Pruebas

La carpeta `tests` contiene pruebas unitarias para el proyecto del gestor de contactos:

- **`test_gestor_contactos.py`**: Pruebas para validar la funcionalidad del gestor de contactos.

## 🚀 Cómo Empezar

### Prerrequisitos

- Tener instalado Python 3.x en tu sistema.
- Un editor de código (se recomienda Visual Studio Code).

### Clonar el Repositorio

```bash
git clone <URL-del-repositorio>
cd <nombre-del-repositorio>
```

### Instalación de Dependencias

Este proyecto utiliza `pandas` y `pytest` para el manejo de archivos CSV en uno de los ejemplos. Para instalarlo, ejecuta:

```bash
uv sync
```

## 🛠️ Uso

Puedes ejecutar cada archivo `.py` de forma individual para ver los ejemplos en acción:

```bash
python 01_funciones.py
python persistencia_03/01_basic.py
```

Para ejecutar el proyecto del gestor de contactos:

```bash
python proyecto_04/main.py
```

## 📚 Temáticas Tratadas

- **Definición y llamada de funciones y procedimientos.**
- **Parámetros, argumentos (`*args`, `**kwargs`) y alcance de variables (scope).**
- **Refactorización de código** para mejorar su estructura y reutilización.
- **Lectura y escritura de archivos de texto** (`open`, `read`, `write`, `append`).
- **Manejo de persistencia de datos** con el manejador de contexto `with`.
- **Archivos CSV, JSON y Pickle.**
- **Pruebas unitarias con `pytest`.**

## 🤝 Cómo Contribuir

Si tienes alguna sugerencia o encuentras algún error, no dudes en abrir un *issue* o enviar un *pull request*.

¡Espero que este repositorio te sea de gran ayuda en tu viaje de aprendizaje con Python!
