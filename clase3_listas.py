#LISTAS

#En esta tercera parte de la clase 3 vamos a ver de qué manera funcionan las listas [] y los diccionarios {}
#Comencemos con uno sencillo: una lista de estudiantes

students= ["Harry", "Cedric", "Luna", "Draco"]

print (students[0])
print (students[1])
print (students[3]) #Vamos a saltarnos el número 2, para que veamos cómo se salta la posición 3 (Luna)

#Como vemos, este sistema es muy ortopédico, así que vamos a remplazarlo por un sistema que imprima todo del tirón

for (estudiante) in students: #Hasta el momento utilizábamos el símbolo _ para representar la variable que está entre for _ in. Pero ahora queremos identificar esta variable.
    print (estudiante) #Al ponerle de nombre "estudiante" a la variable estamos diciendo que eso es lo que es cada item de la LISTA.

#¡Perfecto! Ahora está impresa la lista completa. 
#Aunque vamos a complicarlo un poco más... ¿Y si queremos especificar que sea TOOOODA la longitud de la lista?
#la función "len" (de length) ahora mismo no aporta mucho más, aunque será útil en el futuro. Vamos a ver cómo queda:

for (i) in range(len(students)):  #Solo para este caso, vamos a remplazar la variable "estudiante" por una "i"
    print(i, students[i]) #aquí estamos diciendo que imprima la key "i" y a continuación la lista "students", ¿y qué contiene la lista? Todos los valores de i.

#Pero lo importante de esta función es que vemos cómo en la lista TODAS las key tienen un valor número asignado (comenzando Harry en 0)
#Para corregir este efecto, vamos a sumar +1 a la i, de tal forma que la primera posición sea la 1 y no la 0.

for (i) in range(len(students)): 
    print(i+1, students[i]) #Pero como la función len no nos es demasiado útil aún, la vamos a dejar aquí.

#DICCIONARIOS {}

#¿Qué es un diccionario? Básicamente lo que vamos a ver a continuación:
hogwarts={
    "Hermione":"Griffindor", #Fíjate que los valores en el diccionario se asignan con dos puntos : y no con el símbolo =.
    "Cho":"Ravenclaw",
    "Newt":"Hufflepuff",
} #La primera columan son los key (alumno). La segunda columna son los values que toman estos keys (casa).

for alumno in hogwarts:
    print (alumno, hogwarts[alumno], sep=", ")


#¿PERO Y SI SON 3 DATOS LOS QUE TENEMOS?
#En este caso vamos a crear una LISTA de DICCIONARIOS. 

alumnado = [
    {"name":"Dean", "house":"Griffindor", "patronus":"perro"},
    {"name":"Pansy", "house":"Slythering", "patronus":"ninguno"},
    {"name":"Parvati", "house":"Ravenclaw", "patronus":"cuervo"},
]

for alumno in alumnado:
    print (alumno ["name"], alumno["house"], alumno["patronus"], sep=", ")



#EL PROBLEMA DE MARIO (minuto 1:05:00)
#Este ejercicio es muy abstracto, así que se recomienda ver el video siempre que sea necesario

#Ejercicio 1: crear una columna de 3 bloques.

def main():
    print_column(3)

def print_column(height):
    for _ in range (height):
        print ("#")

main()

#Ejercicio 2: crear una fila de 5 bloques

def main2():
    print_row(5)

def print_row(weight):
    print ("?"*weight)

main2()

#Ejercicio 3: crear un cubo. Aquí la cosa se complica... porque estamos creando un bucle dentro de un bucle.

def main3():
    print_square(3)

def print_square(size):
    for i in range (size): #aquí estamos diciendo "para cada fila i" en el cuadrado
        for j in range (size): #para cada ladrillo de la fila
            print ("#", end="")
        print()

main3()

#Ejercicio 4: Aunqu es probable que el sistema anterior fuese un poco abstracto. Vamos a intentar simplificarlo

def main4():
    print_cuadrado(3)

def print_cuadrado(size):
    for i in range (size):
        print("?"*size)

main4()

#Ejercicio 5: O si queremos condensar aún más el código...

def main5():
    print_bloque(7)

def print_bloque(size):
    for i in range(size):
        print_row(size) #¡Y adivina qué! Esta función ya la habíamos creado antes!!!

main5()