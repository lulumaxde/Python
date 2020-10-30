# A = [[1,2,3],[4,5,6],[7,8,9]]

def matriz(linhas,colunas):

    matriz = []
    for i in range(linhas):

        linha = []
        for j in range(colunas):
            valor = int(input("Digite um numero "))
            linha.append(valor)

        matriz.append(linha)

    print(matriz)


matriz(3,3)
