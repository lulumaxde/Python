def soma_matrizes(m1, m2):

    matriz = []
    linha = len(m1)
    coluna = len(m1[0])

    linha2 = len(m2)
    coluna2 = len(m2[0])

    if(linha == linha2 and coluna == coluna2):

        for i in range(linha):

            linha = []

            for j in range(coluna):

                valor = m1[i][j]+m2[i][j]
            
                linha.append(valor)

            matriz.append(linha)
        return matriz

    else:
        return False




               
