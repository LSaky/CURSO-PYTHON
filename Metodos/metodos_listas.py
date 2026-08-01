#LIST - se usa para crear listas
Lista = list(["Dissel", 23, "calle 89", 2003 ])

#LEN - Nos devuelve cuantos elementos hay en una lista
resultado = len(Lista)

#APPEND - Agrega un elemento a la lista
Lista.append("ELEMENTO1")

#INSERT - Agrega un elemento a la lista en un indice especifico
Lista.insert(2,"ELEMENTO2")

#EXTEND - Agrega varios elementos a una lista
Lista.extend([True, "otro elemento agregado"])

#POP - Elimina un elemento de la lista por su indice, se usa -1 para eliminar el ultimo elemento y -2 para eliminar el anteultimo
Lista.pop(2)

#REMOVE - Elimina un elemento de la lista por su valor, nosotros elegimos cual elemento eliminar por su nombre
Lista.remove("ELEMENTO1")

#CLEAR - Elimina todos los elementos de la lista y despues queda una lista vacia
Lista.clear()

Lista2 = [2,56,34,28,35,True,20,False,24]

#SORT - Ordena la lista de menor a mayo, pero solo funciona si es una lista de numeros y booleanos
Lista2.sort()

#REVERSE = Invierte los elementos de una lista (el ultimo pasa al primero, el penultimo al segundo etc)
Lista2.reverse()

print(Lista2)



