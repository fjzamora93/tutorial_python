#PROGRAMACIÓN ORIENTADA A OBJETOS ---> PARTE 2

"""

En este ejemplo vamos a hacer algo similar al caso anterior... Teníamos el problema
de que con la Tupla no podíamos cambiar el valor de las variables. ¿Pero y si el usuario
introduce por error un dato incorrecto?

Bueno, sencillamente en lugar de una Tupla deberíamos introducir un diccionario.
Aquí vamos a ver cómo crear el diccionario.

En el primer sistema se va a crear el diccionario creando primero el diccionario y luego
introduciendo el key y el valor dentro de él.


def main():
    student= get_student()
    if student["name"] == "Padma":
        student ["house"]="Ravenclaw"
    print (f"{student['name']} es de {student['house']}") 

def get_student():
    student= {} 
    student ["name"]= input("Name: ")
    student ["house"]= input ("House: ")
    return student

"""
#En el segundo caso vamos a crear las variables y luego las retornamos en un diccionario.

def main():
    student= get_student()
    if student['name']== "Padma":
        student['house']= "Ravenclaw"
    print (f"{student['name']} es de {student['house']}") #Se usa comillas simples en lugar de dobles para evitar la confusión
                                                            #Ya que en el string ya hay dobles comillas.

def get_student():
    name= input("Name: ")
    house= input ("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()