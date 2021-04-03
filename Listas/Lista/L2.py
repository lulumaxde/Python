def main():
    
    tam = int(input("Digite a quantidade de numero: "))
    lista = []
    i = 0

    while i < tam:
        numero = int(input("Digite um numero para inserir na lista: "))
        if numero in lista:
            lista.remove(numero)
        lista.append(numero)
        i= i+1
    lista.sort()
    print(lista)
main()