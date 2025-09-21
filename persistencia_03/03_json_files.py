import json

datos_programa = {
    "nombre": "Análisis y Desarrollo de Software (ADSO)",
    "ficha": 2556080,
    "activo": True,
    "aprendices": [
        {"nombre": "Ana", "promedio": 4.5},
        {"nombre": "Luis", "promedio": 4.2},
    ],
}

# Escribir un diccionario de Python a un archivo JSON
with open("programa.json", "w", encoding="utf-8") as f:
    # indent=4 hace que el archivo sea legible para humanos
    json.dump(datos_programa, f, indent=4, ensure_ascii=False)

# Leer un archivo JSON y convertirlo en un diccionario de Python
with open("programa.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(f"El programa se llama: {data['nombre']}")
