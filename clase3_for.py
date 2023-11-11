#SEGUNDA PARTE DE LA CLASE 3, SOBRE BUCLES

#En esta ocasión vamos a empezar definiendo una función

def main(): #Lo primero es lo primero.. definimos una primera función
    miau(3) #donde se va a ejecutar una segunda función, que tenemos que definir

def miau(n): #incluimos entre paréntesis el argument que se está utilizando
    for _ in range (n): #aquí estamos diciendo que lo que hay entre paréntesis es el número de veces que se va a repetir
        print ("miau")
    
main()



#///////////////////////////////

def main2(): 
    number=set_number() #Lo primero es crear una función que permita "coger un número" y "retornarlo"
    miau(number) #Lo segundo es crear una función que repita la palabra "miau"

def set_number(): #"Esta función podría ser útil para eso... para cada vez que queramos que el usuario introduzca un valor"
    while True:
        m=int(input("Cuánto es n?"))
        if m>0: #OJO!!! La clave está en romper el bucle en cuanto el usuario introduzca un valor positivo. 
            break #Mientras meta otro tipo de datos, el bucle se repetirá indefinidamente y solo rehará la pregunta una y otra vez.
    return m #Y aquí vemos como Python va a TOMAR el valor del imput y nos lo va a retornar para que se repita el miau tanto como haya indicado.

def miau(m): 
    for _ in range (m): 
        print ("miau")

main2()