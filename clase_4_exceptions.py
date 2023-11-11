
""" 
Las excepciones se utilizan para detectar errores 
en el código.


"""

#ValueError
"""ValueError cuando el valor de la variable no es válido, 
por ejemplo si introduce un string donde debería haber un número entero."""

try:
    x= int(input("¿Cuánto es X? "))
    print (f"x es {x}")

except ValueError:
    print ("x no es un número entero")


#NameError

"""Este error salta cuando intentas operar con una variable antes de asignarle un valor.
Por ejemplo, en el siguiente caso saltaría un NameError si cambiásemos la X por una Y, 
ya que la variable Y no tiene valor asignado."""

try:
    x=1
    print (f"Imprimimos {x}, para obtener un NameError debemos cambiar x por una variable sin valor asignado" ) #remplazar x por y para obtener un NameError
except NameError:
    print("NameError. Este error salta cuando intentas operar con una variable sin valor asignado")
    

#pass

"""Es otra forma de manejar los errores. Después de indicar el except Error, puedes indentar una nueva linea
de código donde simplemente digas "pass. Esto es útil en un bucle donde volverá a pedirte el nombre de la variable en caso de ValueError"""

#TypeError
"""El TypeError sucede cuando intentas operar con valores que no son compatibles entre sí. 
Por ejemplo, sumar un string y un número entero, o una variable que no tiene valor asignado"""

try:
    y=1
    y=None
    print (y-1)
    
except TypeError:
    print("Felicidades! Obtuviste TypeError")



#UnboundLocalError

"""Este error salta cuando intentas operar con una variable antes de que el usuario le asigne un valor en la Terminal.
Por ejemplo, en el siguiente caso saltaría un UnboundLocalError si el usuario no introdujese el valor de Z."""

#EJEMPLO INCOMPLETO
try:
    print (y)
    
except UnboundLocalError:
    print("Este error salta cuando intentas operar con una variable antes de asignarle un valor desde la TERMINAL. Desde aquí no lo vamos a poder ver")