
def indice():
    valores = []

    valores.append(5)
    valores.append(6)
    valores.append(7)

    for c, v in enumerate(valores):
        print(f'Na posição {c} encontrei o valor {v}!')

def vazio():
    valores = []

    valores.append(5)
    valores.append(6)
    valores.append(7)

    print(valores)

def copia():
    a = [2,3,4,7]
    b = a
    b[2] = 8

    print(f'Lista A: {a}')
    print(f'Lista B: {b}')

    print()
    a = [2,3,4,7]
    c = a[:] #Faz uma cópia não aponta para mesmo endereço
    c[2] = 8

    print(f'Lista A: {a}')
    print(f'Lista C: {c}')

#lista.append Adiciona elemento na ultima linha
#lista.remove('nome da chave') Remove o elemento com o nome informado
#lanche.pop('Indice da lista') Remove o elemento do indice informado
#lanche.pop() Remove o ultimo elemento
#len(lanche) tamanho da lista
#lanche.sort() ordena
#lanche.sort(reverse=true)ordena de forma decrescente
def testes():

    
    lanche= ['hamburguer', 'Pizza', 'Pudim']
    print(lanche[0])
    num = [1,2,3,6,7,11,5,4,3,2,0]
    lanche.append('batata')
    num.sort(reverse=True)
    #print(num)

    if 5 in num:
        num.remove(5)
    print(num)
        

    #lanche.remove('hamburguer')

    #print(lanche)

def main():
    #copia()
    #indice()
    #vazio()
    testes()

main()