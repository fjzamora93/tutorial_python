"""
Minuto 2:22:00
INHERETANCE (Atributos prestados)

Lo que sucede cuando dos clases distintas tienen atributos en común.


La sintaxis para heredar atributos es esta:

        Subclase(ClasePrincipal)
            super().__init__(atributo)

Haciendo esto, la subclase va a heredar uno por uno
los atributos que estemos llamando en cada momento.

Minuto 2:33:00 -> EXCEPTIONS. Aquí ya desconecté
"""
class Wizard:
    def __init__(self, name):
        if not name:    
            raise ValueError ("Missing name")
        self.name=name



class Student(Wizard):
    def __init__(self, name, house):
        #self.name=name NOS CARGAMOS ESTA LINEA
        super().__init__(name) #Esta es la forma de llamar a la Clase Principal
        self.house=house
    def __str__(self):
        return f"Si no incluimos esta función __str__, el resultado en pantalla es feísimo, así que vamos a retornar {self.name} y {self.house}"
    ...

class Profesor(Wizard):
    def __init__(self, name, subject):
        #self.name=name NOS CARGAMOS ESTA LINEA
        super().__init__(name)
        self.subject=subject

    ...
wizard=Wizard("Albus")
student= Student("Harry", "Gryffindor")
professor= Profesor ("Severus", "Defensa contra las artes oscuras")

print (student)