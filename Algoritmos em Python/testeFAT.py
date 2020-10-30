
largura = int(input())
altura = int(input())

while altura > 0:
    x = 0
    while x < largura:
        print("#", end = "")
        x = x+1
    altura = altura-1
    print()
