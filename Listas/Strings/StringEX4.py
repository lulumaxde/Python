#leia um programa que leia um nome
#e diga se ele tem silva no nome

def main():
    nome = input("Digite seu nome inteiro: ")

    nomeM = nome.upper()
    nomeSeparado = nomeM.split()
    cont = 0
    
    for i in range(len(nomeSeparado)):
        if nomeSeparado[i] == "SILVA":
            print('Tem *SILVA* no nome')
            cont = 1
        
    if cont != 1:
        print('Não tem *SILVA* no nome')


main()