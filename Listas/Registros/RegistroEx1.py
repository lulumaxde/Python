def registro(dados):
    registra = 'S'
    maior = menor = 0
    pessoas = list()
    while registra == 'S':
        nome = input('Digite um nome: ')
        peso = int(input('Digite seu peso: '))
        dados.append(nome)
        dados.append(peso)
        pessoas.append(dados[:])
        dados.clear()
        continuar = input('Deseja continuar S ou N? : ')
        registra = continuar.upper()
    return pessoas

def main():
    dados = list()
    pessoas = registro(dados)
    maior = 0
    menor = 10000
    print(f'total de pessoas: {len(pessoas)}')

    for i in pessoas:
        if i[1] > maior:
            maior = i[1]
    
    for p in pessoas:
        if p[1] < menor:
            menor = p[1]

    for j in pessoas:
        if j[1] == maior:
            print(f'{j[0]} tem o maior peso {j[1]}')
       
    for p in pessoas:   
        if p[1] == menor:
            print(f'{p[0]} tem o menor peso {p[1]}')
    
    
        
    #print(f'{pessoas[1].sort(reverse = True)}')
        

main()