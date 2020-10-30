#LISTA1

#Faça um script que calcule o aumento de salário. Ele deve
#solicitar o valor do salário e a porcentagem de aumento.
#Exiba o valor do aumento e do novo salário.


salario = int(input('Digite o salário: '))
aumento = int(input('Digite a % de aumento: '))

porcentagem = aumento / 100

aumentoP = salario*porcentagem

total = aumentoP+salario

print("Valor do aumento =  " + str(aumentoP))
print("Salario novo = " + str(total))

