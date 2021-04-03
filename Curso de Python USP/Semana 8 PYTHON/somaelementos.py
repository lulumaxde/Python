def soma_elementos(lista):
    lista2 = lista[:]
    total = 0
    for x in range (len(lista2)):
        total = total+lista[x]
    return total

def main():
    lista = [2,4,2,2,3,3,1]
    soma_elementos(lista)

main()
