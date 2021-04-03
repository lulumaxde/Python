
def transmissao(lista_loc_eixo_x, lista_loc_eixo_y):
    tam = 0
    area = list()
    
    inf = 0
    for i in range(len(lista_loc_eixo_x)):
        tam = lista_loc_eixo_x[i] *  lista_loc_eixo_y[i]
        area.append(tam)
    ant = area[:]

    for j in range(len(area)):
        p = j-1
        ant = area[j] - area[p]
        if ant < 0:
            ant = ant * -1

        if ant < 9:
            inf += 1

    print(inf)

def main():
    lista_loc_eixo_x = [5,7,5]
    lista_loc_eixo_y = [5,5,5]
    transmissao(lista_loc_eixo_x, lista_loc_eixo_y)
main()
