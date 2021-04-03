
def loc_pessoa(loc_inicial, velocidade, tempo):
    posifinal = loc_inicial[:]

    for i in range(len(loc_inicial)):
       posifinal[i] = loc_inicial[i] + (tempo*velocidade[i])

       while  (posifinal[i] > 100 or posifinal[i] < 0):
            if posifinal[i] < 0:
                dist = posifinal[i] * -1
                posifinal[i] = 0 + dist

            if posifinal[i] > 100:
                dist = posifinal[i] - 100
                posifinal[i] = 100 - dist      

    print(f'posição final = {posifinal}')

def main():
    loc_inicial = [12,94]
    velocidade = [3,-11]
    tempo = 1000

    loc_pessoa(loc_inicial, velocidade, tempo)


main()