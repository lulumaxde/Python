#Faça um programa que leia uma frase e diga
# quantas vezes aparece a letra"A"
#em que oisição eça aparece a primeira vez
# em que posição ela aparece a última vez


def main():
    
    nome = input("Digite seu nome inteiro: ")
    nomeM = nome.upper()

    totalFrase = nomeM.count("A")

    invertida = nomeM[::-1]

    UltimoFraseinvertida = invertida.find('A')

    Ultimo = len(nome) - UltimoFraseinvertida 

    FirstFrase = nomeM.find('A')

    UltimoFrase = nomeM.find('A')

    print(f'Quantidade de letras *A*: {totalFrase}')
    print(f'Primeira aparição {FirstFrase}')
    print(f'Ultima aparição {Ultimo-1}')

main()