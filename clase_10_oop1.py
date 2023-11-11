#PROGRAMACIÓN ORIENTADA A OBJETOS ---> PARTE 1

"""
En esta primera parte vamos a estudiar el concepto de Tupla.

Una Tupla se comporta de manera similar a una LISTA salvo porque los valores
de las TUPLAS no se pueden cambiar. Es decir, una vez establecidos, darán error
en caso de que se intenten modificar.

Hasta ahora, este es el código del que partíamos, un código sencillo:

def main():
    name= input("Name: ")
    house= input ("House: ")
    print (f"{name} for {house}")

"""
#Pero vamos a dar un paso más allá y simplificar el código de arriba para que sea reutilizable:

def main():
    student= get_student()     #name, house= get_student()
                                    # Para que se vea de dónde viene la variable student.
                                    # Python por sí mismo "unpack" la variable de la función y
                                    # devuelve dos valores (name, student)
    print (f"{student[0]} from {student[1]}")

"""
Recordamos que es una coincidencia que las variables de la función principal
se llamen igual que las variables de la función secuendaria. 
Abajo, las variables podrían llamarse n, h, ya que es arriba donde se definirán bien.
"""
def get_student (): 
    name= input("Name: ")
    house= input ("House: ")
    return (name, house) #    ->    return [name, house] Esto ya no es una Tupla, es una LISTA.
        #Puedes ponerlo entre paréntesis o no. Al ponerlo entre paréntesis estás diciendo
        #que las dos variables están relacionadas de alguna manera (la Tupla). Entre [] es una LISTA.

if __name__ == "__main__":
    main()