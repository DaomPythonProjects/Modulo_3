import json

########### Práctica 1: Convertir un String JSON a un Diccionario de Python (json.loads) ###########

# 1. Tenemos una cadena de texto (string) con formato JSON
#    (Usamos triples comillas para definir un string de múltiples líneas)
aprendiz_json_string = """
{
  "nombre": "Ana Sofia",
  "ficha": 2556789,
  "esActivo": true,
  "conocimientos": ["Python", "HTML", "CSS"]
}
"""

# 2. Usamos json.loads() para "cargar el string" y convertirlo a un diccionario
aprendiz_dict = json.loads(aprendiz_json_string)

# 3. Ahora podemos trabajar con los datos como un diccionario normal de Python
print(f"El tipo de dato ahora es: {type(aprendiz_dict)}")
print(f"Nombre del aprendiz: {aprendiz_dict['nombre']}")
print(f"Ficha: {aprendiz_dict['ficha']}")

# Accediendo a un elemento de la lista dentro del diccionario
print(f"Primer conocimiento: {aprendiz_dict['conocimientos'][0]}")

########### Práctica 2: Convertir un Diccionario de Python a un String JSON (json.dumps) ###########
import json

# 1. Tenemos un diccionario de Python
instructor_dict = {
    "nombre": "Carlos Rojas",
    "profesion": "Ingeniero de Sistemas",
    "rol": "Instructor SENA",
    "tecnologias": ["Python", "Java", "SQL"],
    "activo": True
}

# 2. Usamos json.dumps() para "volcar el diccionario a un string"
instructor_json_string = json.dumps(instructor_dict)

# 3. El resultado es una cadena de texto en formato JSON
print(f"El tipo de dato ahora es: {type(instructor_json_string)}")
print("JSON en una sola línea:")
print(instructor_json_string)

# Podemos hacerlo más legible con el parámetro 'indent'
instructor_json_formateado = json.dumps(instructor_dict, indent=4, sort_keys=True)
print("\nJSON formateado (pretty-print):")
print(instructor_json_formateado)

# sort_keys=True ordena las claves alfabéticamente