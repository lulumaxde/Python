def cria_matriz(matriz1,matriz2):
    matriz = []
    num_linhas = 3
    num_colunas = 3
    for i in range(num_linhas):
        #cria linnhas
        linha = []
        for j in range(num_colunas):
            #cria colunas
            valor = matriz1[i][j]*matriz2[i][j]
            linha.append(valor)
        matriz.append(linha)

    print(matriz)




cria_matriz([[1,2,3],[4,5,6],[7,8,9]],[[10,20,30],[40,50,60],[70,80,90]])
