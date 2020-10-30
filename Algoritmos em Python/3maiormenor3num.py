#lista3

#Escreva um programa que leia 3 números e que imprima
#o maior e o menor


Num1 = int(input("Digite o primeiro numero: "))
Num2 = int(input("Digite o segundo numero: "))
Num3 = int(input("Digite o terceiro numero: "))
menor = 0
maior = 0

if(Num1 < Num2 and Num1 < Num3):
    menor = Num1
    if(Num2 < Num3):
        maior = Num3
    else:
        maior = Num2
elif(Num2 < Num1 and Num2 < Num3):
    menor = Num2
    if(Num1 < Num3):
        maior = Num3
    else:
        maior = Num1
else:
    menor = Num3
    if(Num1 < Num2):
        maior = Num2
    else:
        maior = Num1

print("Maior : " + str(maior))
print("Menor : " + str(menor))
