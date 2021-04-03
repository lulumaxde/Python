from random import randint


def gerador(i):
    cont = 0
    lista = list()
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1

        if cont >= 6:
            break
    lista.sort()
    print(f'Os numero sorteados foram {i}: {lista}')


def main():
    qtd = int(input('Digite a quantidade de vezes: '))
    i = 0
    while i <= qtd:
        gerador(i)
        i += 1

main()