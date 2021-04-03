def main():
    dados = list()
    par = list()
    impar = list()

    for i in range(0,7):
        num = int(input('Digite um numero: '))
        dados.append(num)
        if num%2 == 0:
            par.append(num)
        else:
            impar.append(num)
    print(f'Os valores pares são {par}')
    print(f'Os valores ímpares são {impar}')

main()