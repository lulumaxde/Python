def somarpares(matriz):
    total = 0
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i][j]%2 == 0:
                total = total+matriz[i][j]
    print(total)

def maiorlinha(matriz):
    maior = 0
    for i in range(1,2):
        for j in range(0,3):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    print(maior)

def somarlinha(matriz):
    total = 0
    for i in range(1,2):
        for j in range(0,3):
                total = total+matriz[i][j]
    print(total)

def imprime(matriz):
    for i in range(0,3):
        for j in range(0,3):
            print(f'{matriz[i][j]}', end =' ')
        print()

def main():
    matriz = []
    
    for i in range(0,3):
        linha = []
        for j in range(0,3):
            valor = int(input('Digite um valor: '))
            linha.append(valor)
        matriz.append(linha)
    
    imprime(matriz)
    somarpares(matriz)
    somarlinha(matriz)
    maiorlinha(matriz)
main()