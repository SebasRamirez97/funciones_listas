def obtener_indice(lista: list, elemento: int|float|str|bool|list)->int:
    '''Recibe una lista y un elemento. 
    Devuelve la primer posicion donde se encuentre 
    el elemento, en el caso que no este devolvera -1.
    ### Args:
        lista: list
        elemento: int | float | str | bool | list
    ### Returns:
        int
    '''

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i 
    return -1