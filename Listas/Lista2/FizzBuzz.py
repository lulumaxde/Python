#frase = "Curso em video"

#print(frase[2])

def fizzBuzz():
    # Write your code here
    n = int(input())
    i = 1
    for p in range(n):
        
        if(i%3 == 0 and i%5 !=0):
            print('Fizz')
        elif(i%5 == 0 and i%3 !=0):
            print('Buzz')
        elif(i%3 == 0 and i%5 == 0):
            print("FizzBuzz")
        else:
            print(i)
        i = i+1


fizzBuzz()