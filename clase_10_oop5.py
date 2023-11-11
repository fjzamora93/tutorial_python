
"""
PROPIEDADES (properties) MINUTO 1:20:00

Una propiedad es un atributo sobre el que se tiene un poco más de control.

En este punto esta parte no es TAAAAN importante, ya que habla más
sobre cómo ser correcto con el código y evitar que ningún collegue
o el usuario final te puedan romper el código.

Esta parte de la clase es bastante más cómplicada... así que se recomienda revisarla.

Dura hasta el 1:40:00 esta parte de la clase. De momento, puedes ignorarla.

A partir de ese minuto, comienza a enumerar todos los tipos de clases ().
El comando es el siguiente:

    print (type("nos dice el tipo de clase de lo que está entre paréntesis"))


    """



class Estudiante:
    def __init__(self, nombre, casa, patronus,charm):
        if not nombre:
            raise ValueError("Falta un nombre")                  
        self.nombre=nombre 
        self.casa=casa
        self.patronus=patronus
        self.charm=charm                  

    def __str__(self): #Esta línea de código es la que se usa para imprimir en pantalla un texto legible.
        return f"{self.nombre} está en {self.casa}... y aún no está el Patronus en el Str!!"
    
    #GETTER 
    @property
    def casa(self):
        return self._casa
    
    #SETTER
    @casa.setter
    def casa (self,casa):
        if casa not in ["griffindor", "hufflepuff", "ravenclaw", "slyherin"]:
             raise ValueError ("Casa no válida, ¿Ves por qué salta el error? ") 
        self._casa=casa



def main():
    estudiante= get_estudiante()
    estudiante.house="Privet Drive"
    print (estudiante)
    
    

def get_estudiante():
    nombre= input ("Nombre: ") 
    casa= input ("Casa: ")
    patronus= input ("Patronus: ")
    charm=input ("Charm: ")
    return Estudiante(nombre,casa, patronus,charm)


if __name__ == "__main__":
    main()