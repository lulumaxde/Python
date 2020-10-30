import math

a = int(input("Entre com o valor de a "))
b= int(input("Entre com o valor de b "))
c = int(input("Entre com o valor de c "))

delta =  (b**2)-(4*a*c)
raizdelta = math.sqrt(delta)

if delta >=0:
            xposi =  (((-b)+raizdelta)/(2*a)) 
            xnega =  (((-b)-raizdelta)/(2*a))     
            print("Raiz linha",xposi,"Raiz duas linha",xnega)
else:
            print("Não existe raiz real")