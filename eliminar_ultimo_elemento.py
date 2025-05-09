def eliminar(lista: list)->int:
    ''' Elimina el ultimo elemento de la lista y lo retorna.
    
    ### Args:
        lista: list
    ### Returns:
        int
    '''

    ultimo_elemento = lista[-1]
    del lista[-1]
    return ultimo_elemento