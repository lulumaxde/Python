




def main():
    numero = int(input("Digite um numero: "))
    linha = 1
    for i in range(numero):
        line = linha + i
        n = line
        while n != 0:
            print(f'{n}{line}')
            n -= n


main()