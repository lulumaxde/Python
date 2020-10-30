
total = int(input("Digite um número inteiro:  "))

milhares = total//1000

restomilhares = total%1000

centenas = restomilhares//100

restocentenas = restomilhares%100

dezenas = restocentenas//10

print("O digito das dezenas é",dezenas)