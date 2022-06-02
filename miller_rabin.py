import random
import math

def exp_Mod(a, x, n):
    if x == 0:
        return 1
    elif x % 2 == 0:
        t = exp_Mod(a, x / 2, n)
        return (t * t) % n
    else:
        t = exp_Mod(a, x - 1, n)
        return (t * (a % n)) % n

def es_compuesto(a,n,t,u):
    x = exp_Mod(a, u, n)
    if x == 1 or x == n - 1:
        return False
    for i in range(1, t + 1):
        x = exp_Mod(x, 2, n)
        if x == n - 1:
            return False
    return True

def miller_rabin(n,s):
    t = 0
    u = n-1
    while u % 2 == 0:
        t += 1
        u //=2
    for j in range (s):
        a = random.randrange(2,n-1)
        if es_compuesto(a, n, t, u):
            return False
    return True

def random_bits (b):
    n = random.randint(2,pow(2,b)-1)
    m = pow(2,b-1) + 1
    n = n | m
    return n

def randomgen_primos(b,s):
    n = random_bits(b) 
    while miller_rabin(n, s) == False:
        n += 2
    return n

def gen_primos(n):
    s = 40
    if n % 2 == 0:
        n += 1
    else:
        n = (n + 1) - (n % 2)
    while miller_rabin(n,s) == False:
        n += 2
    return n




