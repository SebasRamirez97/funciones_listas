def eliminar_primer_instancia(lista:list, elemento: int|float|str|bool|list)->int|float|str|bool|None:
    ''' Recibe una lista y un elemento. 
        Elimna el primer elemento de la lista que
        coincida con el elemento ingresado y lo retorna. 
        En caso de no encontrarlo devolvera None.
   
    ### Args:
        lista: list
        elemento: int | float | str | bool | list
    ### Returns:
        int | float | str | bool | list | None
    '''
   
    eliminado = None
   
    for i in range(len(lista)):
       if elemento == lista[i]:
           eliminado = lista[i]
           del lista[i]
           return eliminado
    return eliminado