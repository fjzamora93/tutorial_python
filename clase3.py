#LOOPS (Bucles) con While y For

#La primera forma de establecer bucles que vamos a ver es con While, 
#que nos permitirá establecer un bucle en tanto se esté cumpliendo cierta condición.

i=3
while i!=0:
    print ("miau")
    i= i-1

#Básicamente esto es un contador. Cada vez que se ejecuta el bucle está restando 1.
#Aunque en programación solemos establecer los contadores desde 0 y sumamos a conveniencia.

j=0
while j<2:
    print("Este contador está bien... pero es un poco aparatoso, hay que quitar texto")
    j+=1

#Y ya de paso vemos el operador de "incremento" += y decremento -=.


#FOR es la otra forma de construir un bucle

for k in [0,1,2]:
    print ("y ya de paso acabamos de ver lo que es una LISTA, que está entre los paréntesis cuadrados")

#Este contador está muy bien... ¿pero y qué sucede si resulta que hay que contar hasta un millón?

for l in range(2):
    print ("establecer la función range sería la forma de poner un número alto")

#O.. alternativamente

print("miau\n"*4, sep="")

#Pero.... ¿y cómo lo hacemos con un inputo que le pedimos al usuario?
#En este caso mantendremos la condición de True para mantener el bucle. 

while True:
    n=int(input("¿Cuánto es n?"))
    if n>0:
        continue
    else:
        break

#Alternativamente, vamos a simplificar este código

while True:
    variable=int(input("Pon un número positivo para mantener el bucle"))
    if variable<0:
        break
        
