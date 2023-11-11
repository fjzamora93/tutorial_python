"""
En las lecciones anteriores de este módulo aprendimos a crear diccionarios, 
pero no vimos exactamente cómo podría buscar el usuario a través de ellos
y obtener un OUTPUT dependiendo del INPUT entregado, así que vamos allá:

"""


#En primer lugar hay que crear una LISTA de DICCIONARIOS:

emojis = [
    {"id": "agua", "icono": "💧"},
    {"id": "fuego", "icono": "🔥"},
    {"id": "aire", "icono": "💨"},
    {"id": "tierra", "icono": "☘️"},
    {"id": "hielo", "icono": "❄️"},
    {"id": "rayo", "icono": "⚡"},
    {"id": "amor", "icono": "❤️"},
    {"id": "magia", "icono": "✨"}
]
"""
Recordamos que la sintaxis de cada valor de la lista es:
        
        emoji[numero_de_item]["key_seleccionado"]
        
Por ejemplo: 
"""

print (emojis[3]["id"])         #Nos llevará al ITEM 4 del dict e imprimirá la id.
print (emojis[2]["icono"])      #Nos llevará al ITEM 3 del dict e imprimirá el icono.
print (emojis[0]["id"], emojis[0]["icono"])#Nos llevará al ITEM 1 del dict e imprimirá primero el icono y luego la id.


"""Siguiendo esta misma lógica, nosotros mismos podríamos asignar un valor a cada item del diccionario"""

fuego=emojis[1]["icono"]
print (fuego)

"""
Pero esa sintaxis no es suficiente en una búsqueda, ya que las variables no están asignadas.
¿porque cómo va a saber el usuario la posición de cada elemento?
Para ello, creamos una iteración:

for CADA_ELEMENTO en LISTA:
    if IMPUT == CADA_ELEMENTO["id"] (o el identificador que hayamos usado)
        print (CADA_ELEMENTO["icono"])

En este caso Python recorrería el diccionario completo y cuando encontrase una correspondencia, le asignaría el valor de la variable y la imprimiría.
"""

codigo= input ("Inserte el código: ")
for elemento in emojis: #Creamos una iteración para que empiece a buscar.
    if codigo==elemento["id"]: #El usuario introduce la ID, que nos ayudará a localizarlo
        print (elemento["icono"]) #El Output será el icono en cuestión
        almacen=(elemento["icono"]) #Opcionalmente podemos guardarlo en una variable para operar con ella más tarde.

print ("Y ahora se imprimirá la variable guardada ", almacen)

