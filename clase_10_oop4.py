#PROGRAMACIÓN ORIENTADA A OBJETOS ---> PARTE 4 (minuto 50)

"""
En esta parte de la clase entramos más en profundidad en la utilidad de las Clases

raise ERROR es la función para elevar nuestros propios errores en caso
de que algo no vaya como nosotros queramos.

"""


class Estudiante:
    def __init__(self, nombre, casa, patronus,charm):
        if not nombre:
            raise ValueError("Falta un nombre")    
        if casa not in ["griffindor", "hufflepuff", "ravenclaw", "slyherin"]:
            raise ValueError ("Casa no válida ")               
        self.nombre=nombre 
        self.casa=casa
        self.patronus=patronus
        self.charm=charm                  

    def __str__(self):
        return f"{self.nombre} está en {self.casa}... y aún no está el Patronus en el Str!!"
        #Hay que tener cuidado. Si no insertamos esta función (str)
        #El intérprete no va a leer bien la clase.
        #Digamos que esta es la función para darle un "formato" a self.
        

    def hechizo(self):
        match self.charm:
            case "aire":
                return "⚡"
            case  "hielo":
                return "❄️"
            case "fuego":
                return "🔥"
            case "tierra":
                return "🍀"
            case "_":
                return "Hechizo desconocido"



def main():
    estudiante= get_estudiante()
    print (f"{estudiante}")
    print (estudiante.hechizo())  #->>>> MUCHO OJO. Aquí lo que estamos haciendo es LLAMAR LA FUNCIÓN, no a la VARIABLE (como en el anterior).
                                    #Para llamar a una función hay que incluir el (). De otra manera, Python entiende que es un ATRIBUTO del estudiante.

def get_estudiante():
    nombre= input ("Nombre: ") 
    casa= input ("Casa: ")
    patronus= input ("Patronus: ")
    charm=input ("Charm: ")
    return Estudiante(nombre,casa, patronus,charm)


if __name__ == "__main__":
    main()