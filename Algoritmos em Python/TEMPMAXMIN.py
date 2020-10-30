def mínima(temp):
    mini = 500000

    for x in range (len(temp)):
        if (temp[x] < mini):
            mini = temp[x]
    return (mini)

def máxima(temp):
    maxi = -50000

    for x in range (len(temp)):
        if (temp[x] > maxi):
            maxi = temp[x]
    return (maxi)



def MinMax(temp):
   print("A menor temperatura do mês foi : ", mínima(temp), "C.")
   print("A maior temperatura do mês foi : ", máxima(temp), "C.")
   
def main():
    n = int(input("Digite o numero de dias "))
    temp = []
    for i in range(n):
        temp.append(int(input("Digite a temperatura ")))
        
    mínima(temp)
    máxima(temp)
    MinMax(temp)

main()


