import random
import math

def jacobi(a,b):
    if a == 1:
        return 1
    elif a%2 == 0:
        return int(jacobi(a/2,b)*((-1)**(((b*b)-1)/8)))
    else:
        return int(jacobi(b%a,a)*(-1)**((a-1)*(b-1)/4))

def checkIfPrime(b):
    isPrime = True
    for i in range(10000):
        a = random.randint(1,b-1)
        if not(math.gcd(a,b) == 1 and jacobi(a,b) == (a**((b-1)/2)) % b):
            print("error")
            isPrime = False
        return isPrime

print(jacobi(16, 1013))
print(checkIfPrime(693))
#def generatePrimes():