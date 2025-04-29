# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

# Almaceno en una lista los multiplos de 4 del 1 al 100
multiplos = list(range(4, 101, 4))

# Muestro la lista
print(multiplos)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

# Creo la lista
listaFavorita = [True, 25, "Lambda", 3.14, [False]]

# Muestro el penúltimo elemento
print(listaFavorita[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []

# Creo la lista vacia
listaVacia = []

# Agrego las 3 palabras
listaVacia.append("Me")
listaVacia.append("llamo")
listaVacia.append("Lautaro")

# Imprimo la lista resultante
print(listaVacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!

animales = ["perro", "gato", "conejo", "pez"]

# Reemplazo el segundo y el último valor de la lista
animales[1] = "loro"
animales[-1] = "oso"

# Muestro la lista resultante
print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# RESPUESTA: Básicamente se crea una lista con números y luego se remueve el mayor elemento en la lista (en este caso el 22), y se muestra por pantalla la lista resultante. Lo sé porque tengo experiencia con python

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

# Creo la lista según los criterios
lista = list(range(10, 31, 5))

# Muestro los dos primeros elementos
print(lista[0:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]

# Reemplazo los valores centrales
autos[1] = "bora"
autos[2] = "vento"

# Imprimo la lista de nuevo
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

# Creo lista "dobles"
dobles = []

# Agrego el doble de 5, 10 y 15
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

# Imprimo la lista "dobles"
print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

# Punto a
compras[2].append("jugo")

# Punto b
compras[1][1] = "tallarines"

# Punto c
compras[0].remove("pan")

# Punto d
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

# Creo la lista "lista_anidada"
lista_anidada = []

# Agrego los elementos correspondientes
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5, 57.9, 30.6])
lista_anidada.append(False)

# Imprimo "lista_anidada"
print(lista_anidada)
