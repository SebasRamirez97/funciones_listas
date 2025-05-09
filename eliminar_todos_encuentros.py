def eliminar_todos(lista:list, elemento:int|float|str|bool|list)->list:
    ''' Recibe una lista y un elemento. 
        Elimina todos los elementos de la lista que
        coincidan con el elemento ingresado y la devuelve.
   
    ### Args:
        lista: list
        elemento: int | float | str | bool | list
    ### Returns:
        list
    '''
    
    i = 0
    while i < len(lista):
        if elemento == lista[i]:
           del lista[i]
           i-=1
        i += 1

    return lista