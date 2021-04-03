#Crie um programa que leia o nome de uma cidade
#e diga se ela começa com o nome "SANTO"

def main():
    nome = input("Digite o nome da cidade: ")

    nomeM = nome.upper()
    nomeSeparado = nomeM.split()

    if nomeSeparado[0] == 'SANTO':
        print("Começa com *SANTO* ")
    else:
        print("Não começa com *SANTO* ")

 
main()