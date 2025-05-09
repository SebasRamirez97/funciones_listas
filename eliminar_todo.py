def vaciar_lista(lista:list)->None:
    ''' Recibe una lista y la deja vacia.
    
    ### Args:
        lista: list
        Returns:
        None
    '''
    
    i = 0
    while lista != []:
        del lista[i]

