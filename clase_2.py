#CONDITIONALS (if, elif, else)

#Antes de comenzar con los condicionales, vamos a repasar distintos símbolos arítméticos:
#> >= < <= == != 
#se utilizan de la misma forma que en aritmética normal. 

x= int(input("Cuánto es x?"))
y= int(input("Cuánto es y?"))
if x>y:
    print("x es menos que y")
elif x<y:
    print("x es más que y")
else:
    print ("x es igual que y")

#if marca el condicional por excelencia.
#elif, dentro del flujo, crea una opción exclusiva. Es decir, si cumple la condición "elif", es excluyente con cualquier otra opción.
#else se utiliza para cualquier otro caso que no se haya contemplado ni con if ni con elif.

#OR: presenta varias posibles condiciones que deben cumplirse

if x<y or x>y:
    print ("x es distinto de y")
else:
    print("x es igual que y")

#aunque el caso anterior se puede simplificar aún más

if x!=y:
    print("esto sería lo mismo que el caso anterior pero simplificado")


#AND: útil para añadir dos o más condiciones que deben cumplirse.
#Vamos a suponer un sistema de notas escolares.

score=int(input("¿Cuánto has sacado en el examen?"))

if score >=90 and score <= 100:
    print("Sobresaliente!")

elif score >=80 and score <90:
    print("Notable!") 

else:
    print ("otro resultado!")

#Aunque como sabemos, en programación el objetivo siempre es simplificarlo todo... así que se podría quedar así:

if score>90:
    print("Sobresaliente!!")
elif score>80:
    print("notable")
elif score>70:
    print("bieeeen")
else:
    print("otros resultados")

#MINUTO 35 DE LA CLASE 2. Utilizando booleanos para clasificar en una función creada por nosotros

def main():
    x=int(input("Escribe un número para clasificarlo en par o impar"))
    if is_even(x):
        print("número par")
    else:
        print("es un número impar")

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

main()

#Este ejercicio para crear funciones es un poco complicado. Así que vamos a explicarlo paso por paso. 
#En primer lugar, creamos una función cualquiera (a la que por conveniencia estamos llamando main)
#Dentro del primer paréntesis de la función no ponemos nada, porque en un principio esta función aún no se refiere a ninguna variable.
#Después tenemos que pedir con input que el usuario introduzca su variable (que en esta función se llamará X)
#Ahora pediremos al programa que active otra función (que aún no hemos creado) y que se llama "is_even" y que sirve para clasificar números con booleanos.
#OJO! Pero esta función aún no existe... así que vamos a crearla.

#Definimos la función y entre paréntesis dejamos una (n). ¿Por qué? Porque esta n será la variable que acabe remplazada en cualquier función.
#A partir de aquí, creamos el condicional y le pedimos que retorne "True" o "False".

#Existen varias formas de remplazar la función "def is_even" y hacerla aún más simple. Estas son dos formas de simplificarlo:

def is_even2(n):
    return True if n%2==0 else False

#Y la tercera forma de simplificarlo... ¿Para qué usar booleanos si le podemos pedir al programa que simplemente retorne el valor?

def is_even3(n):
    return n%2==0




#MATCH CLASIFICAR

name= input("¿Cómo te gusta tomar el café?")

match name:
    case "con leche":
        print ("Compra un Brasil")
    case "solo":
        print("Compra Etiopía")
    case "no sé":
        print ("Compra uno de cada")
    case _:
        print ("Cómpralos todos!")

#en caso de que queramos crear una respuesta para cualquier otro caso, simplemente escribiremos "_"