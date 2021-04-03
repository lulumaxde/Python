def gcd(i, j): 
    if (i == j): 
        return i 
   
    if (i > j): 
        return gcd(i - j, j) 
    return gcd(i, j - i) 


def isPossible(a, b, c, d):
     # Find absolute values of all as sign doesn't 
    # matter. 
    c, d, a, b = abs(c), abs(d), abs(a), abs(b) 
    
    if (gcd(c, d) == gcd(a, b)): 
        return 'Yes'
    return 'No'


      



def main():
    
    c, d = 35, 15
    a, b = 20, 25
   
# Contributed by Afzal Ansari   

    print(isPossible(a,b,c,d))


main()