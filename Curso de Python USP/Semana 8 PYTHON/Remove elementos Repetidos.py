def remove_repetidos(lista):
    nova_lista = []
    for i in lista :
        if i not in nova_lista :
            nova_lista.append(i)
    return sorted(nova_lista)

#def remove_repetidos(lista):
 #   lista2 = lista[:]
   # lista2.append(10)
  #  lista3 = lista[:]
   # for x in lista2:
    #    if lista2[x] == lista3[x+1]:
     #       del(lista2[x])
    #return((sorted(lista2)))
    
    

#def main():
#    lista = [2,4,2,2,3,3,1]
 #   remove_repetidos(lista)
    
#main()
