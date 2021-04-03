


def organiza(frase):
    j = frase.replace('video','Paradinha')

    q = frase.upper() #MAIUSCULA
    p = frase.lower() #minuscula
    o = frase.title() #primeira letra Maiusculo demias normal
    errado = '   Parabéns você digitou errado!   '
    v = errado.strip() #elimina espaços iniciais e finais
    c = errado.split() # elimina espaços na string e divide em vetores
    t = errado.lstrip() #left strip começa da esquerda
    d = '-'.join(errado) #junta string desse modo
    print(f'Frase modificada: {frase}')
    print(f'Frase modificada: {j}')
    print(f'Frase modificada: {q}')
    print(f'Frase modificada: {p}')
    print(f'Frase modificada: {o}')
    print(f'Frase modificada: {errado}')
    print(f'Frase modificada: {c}')
    print(f'Frase modificada: {d}')
    print(f'Frase modificada: {t}')


def organizaDois(frase):
    print(frase[2])

    achar = frase.count('o',0,16) # retorna um numero com Qtd na String
    acharfrase = frase.find('video')    #retorna primeira posição onde apareceu o inicio da frase
    #Se não existir a palavra retorna -1
    print(achar)

    print(acharfrase, end=" ")

    existe = 'Curso' in frase #retorna True ou False
    print(existe)

def main():
    frase = 'Curso em video'
    organiza(frase)
    #organizaDois(frase)


main()