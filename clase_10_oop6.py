"""
1:51:00 -> class methods
2:13:00 -> Cuando se pone interesante

@classmethod

VOLVER A VER ESTA CLASE

Según avancemos dentro de nuestro código, vamos a querer
que todas las propiedades, funciones y atributos de un objeto
estén dentro del mismo bloque de código.

En este caso vamos a enfocarnos en los MÉTODOS DE CLASE.
Es decir, las funciones que van a suceder dentro de una CLASE.

Los métodos de clase son DECORADORES que pueden llamarse sin tener que crear una instancia en primer lugar.

Sus principales usos son: 
-El método puede crear instancias desde dentro de la clase (sin crear una función externa).
-Puede Configurar atributos de clase.
-Puede realizar operaciones de clase.

Y todo esto sin tener que crear instancias, lo que hace que sea muuuuy conveniente.

"""
class Estudiante:
    def __init__(self, name, house):              
        self.name=name 
        self.house=house             

    def __str__(self):
        return f"{self.name} está en {self.house}... y aún no está el Patronus en el Str!!"
    
    @classmethod #Me sigue sin quedar claro para qué sirve esto
    def get(cls): #cls es la sintaxis para no repetir Class
        name=input ("Name: ")
        house=input ("House: ")
        return cls(name, house) #Esta linea significa "crea un objeto de esta clase"

def main():
    estudiante= Estudiante.get()
    print (estudiante)
    

#Nos cargamos este código y ahora estará dentro de la clase de Estudiante.    
"""
    def get_estudiante():
    nombre= input ("Nombre: ") 
    casa= input ("Casa: ")
    return Estudiante(nombre,casa)
"""

if __name__ == "__main__":
    main()