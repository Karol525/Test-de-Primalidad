# 2)Implementar un programa que genere de manera aleatoria al menos 10 primos distintos de 16, 32 y 64 bits.
import miller_rabin 

def gen_bits(b):
    list = []
    for i in range(10):
        n = miller_rabin.randomgen_primos(b,s)
        list.append(n)
    return list

if __name__=='__main__':
    print(gen_bits(16,))
   # print(gen_bits(32))
    #print(gen_bits(64))
 
