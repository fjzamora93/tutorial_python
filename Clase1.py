

#La primera función que vamos a aprender es input, que nos ayudará a que el usuario introduzca un texto.
#En este caso "name" se trata de una VARIABLE, e input() es la FUNCIÓN. Las funciones tienen esta estructura: funcion()
#Todo lo que aparezca entrecomillado se expresará de forma literal. 
#Lo que no esté entrecomillas, se entenderá que es una variable.

name=input("what's your name¿? ") 
print("hello, ", name)

#Esta no es la única forma de expresarlo, también podemos hacerlo con el símbolo +

print("¿Qué tal estás?, "+name)

#Como podemos ver, dentro de la función insertamos lo que llamamos "arguments" o "parámetros".
#Si consultamos la guía de Python descubriremos que hay infinidad de argumentos para cada función.
#Por ejemplo, estos serían algunos de los arguments para la función print().

objects=print("cualquier número de objetos")
print(objects, sep=" ", end="/n", file=None, flush=False)

#Objects aparece en plural porque se refiere a cualquier número de objetos
#Sep=" " indica que el tipo de separación natural es un espacio. Eso quiere decir que lo que pongas entre comillas aparecerá entre los distintos argumentos.
#"/n" quiere decir New Line. Por defecto, al darle a enteder todo aparecerá en una nueva linea,
#pero si dejamos las comillas vacías "" estaremos dando a entender que no existe unan ueva linea, así que la terminal lo imprimirá todo junto.

#MODIFICACIONES
#Cada función admite distintos tipos de modificaciones. Veamos algunas.

name=name.strip() #con esto eliminaríamos espacios
name=name.title() #esto nos ayudaría a capitalizar las letras
name=name.strip().title() #sería la forma de escribirlo todo junto...
name=input("What's your name?").strip().title()

#Hay muchas modificaciones a las funciones, aunque eso requiere explorarlas.



#NÚMERO ENTEROS (INT)

#Esta es la primera forma de hacerlo. Lo tenemos todo escrito aquí... 
x=1
y=2
z=x+y
print(z)

#¿pero y si queremos que el usuario sea el que introduzca los datos?
variable1=input("cuál es la variable uno?")
variable2=input("¿Cuál es la variable dos?")
print("El resultado de la suma es:")
suma=int(variable1)+int(variable2)
print(suma)

#Para que haga la suma correctamente, debemos asegurarnos de que los valores están expresados como int().
#de cualquier otra forma el programa los interpretará como si fuesen un string.
#Para números decimales la función a emplear deberá ser float()

#INVENTAR TU PROPIA FUNCIÓN

#Llegado el momento, es posible que deseemos inventar nuestra propia función. 
#Para ello deberemos DEFINIR la función. Esto se hace tal que así.

def hello(to="world"):
    print ("hello", to)
    
name=input("what's your name?")
hello(name)

#Aquí lo que hemos hecho ha sido definir entre paréntesis el parámetro de la función que acabamos de crear.
#Lo hemos llamado "to" para que suene lógico, pero a la hora de introducir la función, ponemos "name", que es la variable creada justo antes.
#Si no se inserta nombre, dará por valor "world", que es lo que hemos definido por defecto.


#RETURN A VALUE

def square(n):
    return n*n

def main():
    x=int(input ("what's x?"))
    print("x squared is", square(x))

main()

