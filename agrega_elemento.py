def agregar(lista: list, elemento: int|float|str|bool) -> None:
    '''*Recibe* una lista y un elemento. 
    Modifica la lista agregando el elemento a la lista.
    ### Args:
        lista: list
        elemento: int | float | str | bool
    ### Returns:
        None
    '''
    lista += [elemento]

def insertar(lista: list, elemento: int|float|str|bool, indice: int)->None:
    '''Recibe una lista, un elemento y un indice. 
    Modifica la lista agregando el elemento en 
    la posicion que se indica en el indice.
    ### Args:
        lista: list
        elemento: int | float | str | bool
        indice: int
    ### Returns:
        None    
    '''
    
    lista[:] = lista[:indice] + [elemento] + lista[(indice+1):]
    
    
def obtener_indice(lista: list, elemento: int|float|str|bool)->int:
    '''Recibe una lista y un elemento. 
    Devuelve la primer posicion donde se encuentre 
    el elemento, en el caso que no este devolvera -1.
    ### Args:
        lista: list
        elemento: int | float | str | bool
    ### Returns:
        int

    '''
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i 
    return -1

def eliminar(lista: list)->int:
    '''Elimina el ultimo elemento de la lista y lo retorna.
    ### Args:
        lista: list
    ### Returns:
        int
    '''
    ultimo_elemento = lista[-1]
    del lista[-1]
    return ultimo_elemento

def eliminar_primer_instancia(lista:list, elemento: int|float|str|bool)->int|float|str|bool|None:
   '''Recibe una lista y un elemento. 
   Elimna el elemento en la primer instancia que lo encuentre. En aso de no encontrarlo devolvera None
   
   ### Args:
        lista: list
        elemento: int | float | str | bool
    ### Returns:
        int | float | str | bool | None
   '''
   
   eliminado = None
   
   for i in range(len(lista)):
       if elemento == lista[i]:
           eliminado = lista[i]
           del lista[i]
           return eliminado
   return eliminado

def eliminar_todos(lista:list, elemento:int|float|str|bool)->list:
    i = 0
    while i < len(lista):
        if elemento == lista[i]:
           del lista[i]
           i-=1
        i += 1

    return lista


print(eliminar_primer_instancia([2,3,4], 20))

