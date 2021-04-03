
def main():
    lista = []
    maior = -10000
    menor = 100000

    for i in range(0,5):
        num = int(input("Digite um numero: "))
        lista.append(num)
    print(lista)

    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            k = i
        if lista[i] < menor:
            menor = lista[i]
            l = i
    print(f'Vetor na posição {k} é o maior numero {maior}')
    print(f'Vetor na Posição {l} é o menor numero {menor}')
        
main()