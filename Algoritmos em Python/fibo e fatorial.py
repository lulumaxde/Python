a = "gato"

b = "O gato subiu no telhado"

c = "telhado"

def fib(n):

    a = 0
    b = 1
    aux = 0

    while b < n:
        print(b, end=' ')
        aux = b
        b = a+b
        a = aux
        n = n-1
    print()

def fat(n):
    fat = 1

    while n != 0:
        fat = fat*n
        n = n-1
    print(fat)



