
import pytest
"""
La realización de test es una parte primordial para cualquier programador.

Existen varias herramientas para realizar test unitarios, aquí vamos a ver  tan solo una.

En primer lugar, es apropiado utilizar nombres adecuados para los test. 

Así, el documento debería llamarse por lo general:

            test_NombreDelPrograma.py

Mientras que cada función a testr debería llamarse:

            def test_funcion.py
            

"""

#La función que vamos a utilizar para realizar test se llama "assert", a través de la cuál declaramos que cierto valor debe ser ese y no otro.
#Esta función será clave para la librería que utilizaremos para realizar los test.


from calculadora_simple import suma #importamos la función

"""
La primera forma de probar el código es a través de "assert"
Pero esta forma puede ser lenta y repetitiva, ya que involucra estar
continuamente escribiendo "try" y "except AssertionError:

Quedaría así:
"""

def main():
    test_suma()

def test_suma():
    try:
        assert suma(2,2)==4 #Si el assert es correcto, no sucederá nada.
    except AssertionError:
        print ("MAL! 2+2 es 4")
    try:
        assert suma(2,2)==3 #Aquí se generará un Assertion error
    except AssertionError:
        print ("INCORRECTO!!! 2+2 es 4")

main()

""""
La otra forma de hacer los test es a través de "pytest", en teorái se escribe en la consola lo siguiente:

    pytest nombreDelArchivo.py

Aunque este comando no está funcionando.
"""