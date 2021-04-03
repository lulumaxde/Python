#Faça um programa que leia um inteiro de 0 a 9999
# e mostre cada um dos digitos separados
#ex Digite um numero: 1834
#unidade: 4
#dezena: 3
#centena: 8 
#milhar: 1

def main():

    num = int(input("Digite um numero de 0 a 9999: "))

    if num < 10:
        print(num)
    elif num >= 10 and num < 100:
        unidade = num%10 #retorna o resto
        dezena = num//10 #retorna inteiro da divisão
        print(f'unidade: {unidade}')
        print(f'dezena: {dezena}')
        
    elif num >= 100 and num < 1000:
        centena = num//100
        restoDezena = num%100
        dezena = restoDezena//10
        unidade = restoDezena%10
        print(f'unidade: {unidade}')
        print(f'dezena: {dezena}')
        print(f'centena: {centena}')
    elif num >= 1000 and num < 10000:
        milhar = num//1000
        restomilhar = num%1000
        centena = restomilhar//100
        restocentena = num%100
        dezena = restocentena//10
        unidade = restocentena%10
        print(f'unidade: {unidade}')
        print(f'dezena: {dezena}')
        print(f'centena: {centena}')
        print(f'milhar: {milhar}')
    
    else:
        print("não calculado ainda")


main()