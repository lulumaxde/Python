def registro(dados):
    registra = 'S'
    while registra == 'S':
        nome = input('Digite um nome: ')
        numero = int(input('Digite um numero: '))
        dados.append(nome)
        dados.append(numero)
        continuar = input('Deseja continuar S ou N? : ')
        registra = continuar.upper()
    return dados

def teste():
    galera = list()
    dado = list()

    tmenor = tmaior = 0

    for c in range(0,3):
        dado.append(str(input('Nome: ')))
        dado.append(int(input('Idade: ')))
        galera.append(dado[:])
        dado.clear()

    for p in galera:
        if p[1] >= 18:
            print(f'{p[0]} é maior de idade')
            tmaior += 1
        else:
            print(f'{p[0]} é menor de idade')
            tmenor += 1

    print(f'temos {tmenor} pessoas de menor e {tmaior} pessoas de maior')
def main():
    dados = list()
    #teste()
    pessoas = list()
    pessoas = [['pedro jorge', 25],['josefino reis', 36],['lucas carl', 24]]
    #registro(dados)
   #pessoas.append(dados[:])
    
    for j in pessoas:
        print(f'{j[0]} - {j[1]}')
       
    
    print(pessoas[0][0]) #[] POSIÇÃO DO REGISTRO #POSIÇÃO DO REGISTRO NOME OU IDADE
    print(pessoas[1][1]) #Idade jorge matheus
    print(pessoas[1][0]) # Nome Jorge e matheus
    print(pessoas[0]) #Idade e Nome primeiro registro
main()