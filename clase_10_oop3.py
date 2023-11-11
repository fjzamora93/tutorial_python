#PROGRAMACIÓN ORIENTADA A OBJETOS ---> PARTE 3 (minuto 30)

"""
Finalmente llegamos a la necesidad de crear una CLASE (classes), que soluciona los problemas anteriores. 

Una Clase es un "molde" para trabajar con un tipo de datos dentro de cualquier
lenguaje de programación dentro de la Porgramación Orientada a Objetos.

"""

class Student:
    ...

def main():
    student= get_student()
    print (f"{student.name} from {student.house}")

def get_student():
    student = Student () #Ahora tenemos una variable que encaja con una clase.
    student.name= input ("Name: ") #Esta es la sintaxis de los ATRIBUTOS (no key, no value como en dict.)
    student.house= input ("House: ")
    return student

"""
        Para la función anterior (get_student), vamos a proponer una sintaxis alternativa:


        def get_student():
            name=input ("Name: ")
            house= input ("House: ")
            student= Student(name, house)  ->Esta línea es la que está creando una instancia.
            return student
            
"""



"""
    Y ahora vamos a trabajar con el código propiamente dicho de las CLASES.

    Concretamente, vamos a ver la Syntax de los METHODS.

    """

class Estudiante:
    def __init__(self, nombre, casa): #INIT (Initiate Item) es la sintaxis específica de la función para las clases.
                                        #self es el lugar donde se van a guardar las instancias.
        self.nombre=nombre 
        self.casa=casa                  #-> self está vacío y se llena con la instancia.

def main2():
    estudiante= get_estudiante()
    print (f"{estudiante.nombre} from {estudiante.casa}")

def get_estudiante():
    nombre= input ("Nombre: ") 
    casa= input ("Casa: ")
    estudiante= Estudiante (nombre,casa) #Esta es la sintaxis que está creando instancia.
    return estudiante

if __name__ == "__main__":
    main()
    main2()