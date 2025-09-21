import pickle


# Vamos a usar una clase personalizada para ver el poder de pickle
class Aprendiz:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha
        self.programas = ["Python", "Bases de Datos"]

    def mostrar_info(self):
        print(f"Soy {self.nombre} de la ficha {self.ficha}.")


# 1. Creamos una instancia de nuestra clase
aprendiz_obj = Aprendiz("Carlos", "2556080")

# 2. Serializamos (guardamos) el objeto en un archivo
#    Se usa el modo 'wb' (write binary)
with open("aprendiz.pkl", "wb") as archivo:
    pickle.dump(aprendiz_obj, archivo)

# 3. Deserializamos (cargamos) el objeto desde el archivo
#    Se usa el modo 'rb' (read binary)
with open("aprendiz.pkl", "rb") as archivo:
    aprendiz_cargado = pickle.load(archivo)

# El objeto cargado es una instancia completamente funcional de la clase
print(type(aprendiz_cargado))
# <class '__main__.Aprendiz'>

aprendiz_cargado.mostrar_info()
# Salida: Soy Carlos de la ficha 2556080.
