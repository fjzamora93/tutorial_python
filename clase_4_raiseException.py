
"""
Empezamos por lo primero, que es aprender a levantar errores que ya tengan una clase:

En este caso la sintaxis parte de una función, donde debemos crear una condición:

            if condición:
                raise Error ("Este mensaje NO se va a desplegar")

Posteriormente, debemos seguir la sintaxis normal de los errores:

try:
    lo que quiera que se intente...
except Error:
    ejecutar lo que quiera que se haga ante este error.

"""


def main():
    while True:
        nombre= input("Heil: ")
        if nombre== "Hitler":
            raise ValueError ("Este es el nombre del error")
    

try:
    main()
except ValueError:
    print("Oh, no!! Hitler Error")





"""
¿Pero y si queremos crear nuestros propios errores?
"""


# Definir una excepción personalizada
class MiErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Función que provoca una excepción
def dividir(a, b):
    if b == 0:
        raise MiErrorPersonalizado("¡No puedes dividir entre cero!")
    return a / b

# Ejemplo de uso
try:
    resultado = dividir(10, 0)
except MiErrorPersonalizado as error:
    print(f"Se produjo un error: {error}")
else:
    print(f"El resultado de la división es: {resultado}")