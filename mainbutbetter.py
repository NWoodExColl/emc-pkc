import sympy as sp
import random

E = 65537 

def computeD(ETFn,e):
    c = ETFn
    d = e
    a1 = 1
    a2 = 0
    b1 = 0
    b2 = 1
    r1 = d
    while r1 != 0:
        r2 = r1
        r1 = c%d
        q = (c-r1)/d
        b3 = b1 + b2*-q
        a3 = a1 + a2*-q
        c = d
        d = r1
        a1 = a2
        a2 = a3
        b1 = b2
        b2 = b3
    if r2 == 1:
        print("I have computed d to be",b1)
    else:
        print("you need to choose a diffrent value of d because it is not co-prime with the Eulers toitient function of n.")
    d = b1
    return d


def generatePrimes(order_of_mag):
        prime = 4
        while not sp.isprime(prime):
            prime = random.randint((10**(order_of_mag-1)), (10**order_of_mag))
        return prime

def to_binary(x): return str(bin(x))[2:]

def to_binary_but_better(x):
    binary = to_binary(x)
    for i in range(8-len(binary)):
        binary = "0" + binary
    return binary

def generic_crypt(message, key, n):
    c = 1
    bin_key = to_binary(key)
    for i in range(len(bin_key)):
        c = (c*c) % n
        if bin_key[i] == 1:
            c = (c*message) % n
    return c 

def generateKeys():
    print(generic_crypt(25, 13, 17))
    p = generatePrimes(10)
    q = generatePrimes(10)
    n = p*q
    ETFn = (q-1)*(p-1)
    print(n)
    d = computeD(ETFn,E)
    return n, d

n , d = generateKeys()

message = "We are trying to encrypt and decrypt a message"
message_num = ""
for i in list(message.encode('ascii')):
    message_num = message_num + to_binary_but_better(i)
message_num = int(message_num, 2)
print(message_num)