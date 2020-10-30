def ehPrimo(n):
    if (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    else:
        i = 3
        while (i <= (n / i)):
            if ((n % i) == 0):
                return False
            i += 2
        return True
 
    return False


