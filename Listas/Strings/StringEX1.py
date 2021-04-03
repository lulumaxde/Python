#Faça um programa que receba um nome e print-os
#nome
#nome tudo em maiusculo
#nome tudo em minusculo
#conte o tamanho da string excluindo os espaços em branco
#print o tamanho do First Name

def main():
    n = input("Digite um nome : ")
    nMaiuscula = n.upper()
    nMinuscula = n.lower()
    nFirst = n.split()
    print(nFirst)
    TamFirstname = nFirst[0]
    cont = 0
    for i in range(len(n)):
        if(n[i] != " "):
            cont = cont+1
            
        
        
    print(n)
    print(nMaiuscula)
    print(nMinuscula)
    print(cont)
    print(len(TamFirstname))

main()