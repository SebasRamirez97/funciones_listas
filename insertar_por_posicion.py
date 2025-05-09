def insertar(lista: list, elemento: int|float|str|bool|list, indice: int)->None:
    ''' Recibe una lista, un elemento y un indice. 
        Modifica la lista agregando el elemento en 
        la posicion que se indica en el indice.
    
    ### Args:
        lista: list
        elemento: int | float | str | bool | list
        indice: int
    ### Returns:
        None    
    '''
    
    lista[:] = lista[:indice] + [elemento] + lista[(indice+1):]