import sympy as sp
import random

E = 65537 

def generatePrimes(n, order_of_mag):
    for i in range(n):
        prime = 4
        while not sp.isprime(prime):
            prime = random.randint((10**(order_of_mag-1)), (10**order_of_mag))
        print(prime)

def to_binary(x): return str(bin(x))[2:]

def generic_crypt(message, key, n):
    c = 1
    bin_key = to_binary(key)
    for i in range(len(bin_key)):
        c = (c*c) % n
        if bin_key[i] == 1:
            c = (c*message) % n
    return c 

print(generic_crypt(25, 13, 17))
print(generatePrimes(2, 10))