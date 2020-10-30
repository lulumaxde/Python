#import math
#
#def delta(a,b,c):
 #   delta = b**2-4*a*c
  #  return delta

#def main():
 #   a = int(input("Digite um numero "))
  #  b = int(input("Digite um numero "))
   # c = int(input("Digite um numero "))
     #imprime(a,b,c)

# def imprime(a,b,c):
 #   delta(a,c,b)
  #  raiz = delta(a,b,c)
   # if (raiz == 0):
    #    raiz1 = (-b + math.sqrt(raiz))//(2*a)
    #elif (raiz < 0):
     #   print(" Não existe raiz real")
    #else:
        
      #  raiz1 = (-b + math.sqrt(raiz))//(2*a)
       # raiz2 = (-b - math.sqrt(raiz))//(2*a)
        #print(raiz1)
        #print(raiz2)
from math import sqrt,trunc



def main():
    a = int(input("Digite um numero "))
    b = int(input("Digite um numero "))
    c = int(input("Digite um numero "))
    imprime(a,b,c)

def delta(a,b,c):
    delta = b**2-4*a*c
    return delta


def imprime(a,b,c):
    delta(a,c,b)
    raiz = delta(a,b,c)
    if (raiz == 0):
        raiz1 = (-b +sqrt(raiz))//(2*a)
    elif (raiz < 0):
        print(" Não existe raiz real")
    else:
        
        raiz1 = (-b + sqrt(raiz))//(2*a)
        raiz2 = (-b - sqrt(raiz))//(2*a)
        print(trunc(raiz1))
        print(trunc(raiz2)) 

main()


