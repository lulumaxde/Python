
def saude(pessoas, d_encontro, d_observacao):
    
    DoentesDia = pessoas[:]
    doente = list()
    Dias = d_observacao - d_encontro
    total = 0 
    maior = -1
    j = 0
    l = 0
    
    
    for i in range(len(pessoas)):
        if pessoas[i] != -1:
            doente.append(pessoas[i])
            if pessoas[i] > maior:
                maior = pessoas[i]
    #for k in range(len(DoentesDia)):
        #if DoentesDia[k] == -1:
            #DoentesDia[k] += 1
    tt = maior+14
    if tt < d_encontro:
        total = 0
    elif d_encontro == d_observacao:
        total = 0
    elif d_encontro >= 15 :
        total = 0
    else:
        if len(doente) != 0:     
            if maior < d_encontro+14:
                #while j < d_encontro:
                # for m in range(len(pessoas)):
                        #if DoentesDia[m] != -1:
                            #while DoentesDia[m] != d_encontro:
                                # DoentesDia[m] += 1
                    #j = j+1

                for k in range(len(DoentesDia)):
                    if DoentesDia[k] == -1:
                        DoentesDia[k] += 1
                
                while l < Dias:
                    for n in range(len(pessoas)):
                            DoentesDia[n] += 1
                    l = l+1

                for p in DoentesDia:
                    if(p < 15 ):
                        total += 1    
        else:
            total = 0
     
    print(total)
        
         

def main():
    
    pessoas = [-1 , 0, 3, -1, -1]
    d_encontro = 15
    d_observacao = 17
    saude(pessoas, d_encontro, d_observacao)



main()