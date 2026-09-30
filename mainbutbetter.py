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