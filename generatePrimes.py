import random
import math

def jacobi(a,b):
    if a == 1:
        return 1
    elif a%2 == 0:
        return jacobi(a/2,b)*(-1)**((b*b-1)/8)
    else:
        return jacobi(b%a,a)*(-1)**((a-1)*(b-1)/4)

def checkIfPrime(b):
    isPrime = True
    for i in range(100):
        a = random.randint(1,b-1)
        if not(math.gcd(a,b) == 1 and jacobi(a,b) == (a**(b-1)/2)%b):
            isPrime = False
        return isPrime

print(checkIfPrime(29))

#def generatePrimes():