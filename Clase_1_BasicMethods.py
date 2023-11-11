"""

Material complementario:  Docs.python.org/3/library/functions.html#print


En esta primera clase vamos a explicar unos cuantos métodos bastante comunes.
Aquí hay muchos otros igualmente útiles:

PARA STRING: https://www.w3schools.com/python/python_strings_methods.asp

PARA LISTAS: https://www.w3schools.com/python/python_lists_methods.asp


"""
texto=input("Vamos a pasar este texto a distintos métodos: ")

#variable.lower()

minusculas=texto.lower()
print(f"1. Comenzamos con el texto en minusculas: {minusculas}")


#variable.upper()

mayusculas=texto.upper()
print(f"2. Ahora el texto aparecerá en mayúsculas: {mayusculas}")


#variable.title()

titulo=texto.title()
print(f"3. Ahora el texto aparecerá en mayúscula la primera de cada palabra: {titulo}")


#variable.casefold()

loweragresivo=texto.casefold()
print(f"4. Una versión más agresiva del lower: {loweragresivo}")


#variable.strip()

todojunto=texto.strip(" ").strip("a")
print(f"5. Nos cargamos los caracteres que haya al extremo de la cadena \n  (en este caso los espacios y la letra a): {todojunto}")


#variable.replace()
remplazar=texto.replace("a","@")
print(f"4. Remplaza los dos parámetros especificados: {remplazar}")

"""
MÉTODOS PARA LISTAS
"""

#variable.split()

lista_dividir=texto.split()
print(f"Divide con lo que haya en las comillas (por defecto espacio) y te devuelve una lista: \n  {lista_dividir}")

lista_dividir=texto.split(",",2) #ahora divde la coma, el segunda parámetro te dice de cuántos item es la lista
print (lista_dividir)


#variable.reverse()

print (f"Y ahora invertimos el orden: ", lista_dividir.reverse())


