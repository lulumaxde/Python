def fatorial(num):
    fat = 1
    while(num!=1):
        fat = fat*num
        num = num-1
    return fat

def testa_fatorial():
    if fatorial(1) == 1:
        print("funciona")
    if fatorial(2) == 2:
        print("funciona")
    if fatorial(5) == 120:
        print("funciona")


def numero_binomial(num,k):
    return fatorial(num) // (fatorial(k)*fatorial(num-k))

