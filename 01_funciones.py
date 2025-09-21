######### 1.1. 🤔 ¿Qué es una Función y Por Qué Usarla? #########

# 1. Palabra clave "def" para definir
# |    2. Nombre de la función (snake_case)
# |    |          3. Paréntesis con parámetros (opcional)
# |    |          |
def nombre_de_la_funcion(parametro1, parametro2):
    # 4. Cuerpo de la función (código indentado)
    #    Realiza alguna tarea...

    # 5. Declaración "return" (opcional)
    return "un resultado"


resultado = nombre_de_la_funcion("valor1", "valor2")
print(resultado)

######### 1.2. 🛠️ Definiendo y Llamando Funciones #########
##### Funciones Simples #######


# Definición de la función
def saludar():
    """Esta función imprime un saludo simple en la consola."""
    print("¡Hola, bienvenido al curso de Python!")
    print("Espero que estés aprendiendo mucho.")


# Llamada a la función
print("Iniciando el programa...")
saludar()  # El código dentro de la función se ejecuta aquí
print("El programa ha terminado.")


##### La Declaración return #######
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    resultado = a + b
    return resultado


# Llamamos a la función y guardamos el valor de retorno en una variable
total = sumar(15, 7)
print(f"El resultado de la suma es: {total}")  # Salida: El resultado de la suma es: 22


# También podemos devolver múltiples valores (Python los empaqueta en una tupla)
def obtener_coordenadas():
    """Devuelve una ubicación X, Y, Z."""
    x = 10
    y = 20
    z = 30
    return x, y, z


ubicacion = obtener_coordenadas()
print(f"Ubicación obtenida: {ubicacion}")  # Salida: Ubicación obtenida: (10, 20, 30)
print(f"Coordenada Y: {ubicacion[1]}")  # Salida: Coordenada Y: 20

##### Parámetros y Argumentos #######


# "nombre" y "edad" son PARÁMETROS
def generar_perfil(nombre, edad):
    perfil = f"Usuario: {nombre}, Edad: {edad} años."
    return perfil


# "Ana" y 28 son ARGUMENTOS posicionales (el orden importa)
perfil_ana = generar_perfil("Ana", 28)
print(perfil_ana)

# Usando argumentos de palabra clave (keyword arguments), el orden no importa
perfil_juan = generar_perfil(edad=45, nombre="Juan")
print(perfil_juan)


######### 1.3. ✨ Parámetros Avanzados y Flexibilidad #########
##### Valores por Defecto #######
def crear_usuario(nombre, activo=True, rol="invitado"):
    """Crea un usuario con un estado y rol por defecto."""
    print(f"Creando usuario: {nombre}")
    print(f"  - Rol: {rol}")
    print(f"  - Activo: {activo}")


# Llamada simple, usa los valores por defecto
crear_usuario("Diego")

# Llamada especificando un rol diferente
crear_usuario("Maria", rol="administrador")


##### Argumentos de Longitud Variable (args y *kwargs) #######
# Ejemplo con *args para sumar cualquier cantidad de números
def sumar_todo(*args):
    """Suma todos los números pasados como argumentos."""
    print(f"Recibí estos números: {args}")
    total = 0
    for numero in args:
        total += numero
    return total


print(sumar_todo(1, 5, 10))  # Salida: 16
print(sumar_todo(20, 30, 50, 100))  # Salida: 200


# Ejemplo con **kwargs para construir un perfil
def mostrar_detalles_personales(**kwargs):
    """Muestra los detalles de una persona."""
    print(f"Detalles recibidos: {kwargs}")
    for clave, valor in kwargs.items():
        print(f"- {clave.capitalize()}: {valor}")


mostrar_detalles_personales(nombre="Carlos", profesion="Ingeniero", ciudad="Sogamoso")

######### 1.4. 🌐 Alcance de Variables (Scope) #########
# Variable GLOBAL
saldo_global = 1000


def hacer_compra(precio):
    # Variable LOCAL
    impuesto = 0.19
    costo_total = precio + (precio * impuesto)

    # Podemos leer la variable global
    print(f"El saldo antes de la compra es: {saldo_global}")

    # ¡No podemos modificar una variable global directamente!
    # Para hacerlo, necesitaríamos la palabra clave "global", pero es mejor evitarlo.
    # saldo_global -= costo_total # Esto daría un error

    print(f"El costo total de la compra es: {costo_total}")


hacer_compra(100)
# print(costo_total) # Esto daría un error, porque "costo_total"
# solo existe dentro de la función.


######### 1.5. 📝 Documentación y Buenas Prácticas #########
##### Docstrings #######
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio (float): El radio del círculo. Debe ser un número positivo.

    Returns:
        float: El área calculada del círculo.
    """
    if radio < 0:
        return 0
    return 3.14159 * (radio**2)


# Las herramientas y los editores pueden mostrarte esta documentación
help(calcular_area_circulo)


##### Type Hinting (Anotaciones de Tipo) #######
# La misma función, pero con Type Hints
def calcular_area_circulo_tipado(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio (float): El radio del círculo. Debe ser un número positivo.

    Returns:
        float: El área calculada del círculo.
    """
    if radio < 0:
        return 0.0  # Es buena práctica devolver el mismo tipo que se declara
    return 3.14159 * (radio**2)


area = calcular_area_circulo_tipado(10.5)
print(f"El área es: {area}")

######### 1.6. 📝 Funciones Lambda y Programación Funcional en Python #########
add = lambda a, b: a + b
print(add(10, 4))

multiply = lambda a, b: a * b
print(multiply(80, 5))

# Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrados:", squared_numbers)

# Pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Pares:", even_numbers)

# Impares
impar_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("impares: ", impar_numbers)


######### ♾️ 1.7 Recursividad #########
# Suma de numeros de recusiva
def sum_numbers(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + sum_numbers(n - 1)


result = sum_numbers(5)
print(f"Suma de los primeros 5 números es: {result}")


# Serie Fibonacci recusiva
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        return memo[n]


print(fibonacci_memo(10))  # Salida: 55
