#LISTA4

#Crie um programa que crie uma matriz de dimensão 3x3
#e preencha com valores lidos pelo teclado. No final,
#mostre a matriz

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input('Digite um valor: ')))
    matriz.append(linha)
print(matriz)
