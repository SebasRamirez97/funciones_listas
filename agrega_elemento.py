def agregar(lista: list, elemento: int|float|str|bool|list) -> None:
    ''' Recibe una lista y un elemento. 
        Modifica la lista agregando el elemento a la lista.
    
    ### Args:
        lista: list
        elemento: int | float | str | bool | list
    ### Returns:
        None
    '''
    
    lista += [elemento]
    