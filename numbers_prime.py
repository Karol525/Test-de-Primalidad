#1) Generar todos los primos de 3, 4 y 5 cifras.
import miller_rabin
s = 40
def primos(digit):
    list = []
    if digit == 3:
        b, a = 99, 997
    elif digit == 4:
        b, a = 999, 9972
    elif digit == 5:
        b, a = 9999, 99990
    else:
        print("NUMERO INVALIDO")
        exit(1)
    for n in range(b,a):
        if miller_rabin.miller_rabin(n,s):
            list.append(n)
    return list
if __name__=='__main__':
    print(primos(3))
    #print(primos(4))
    #print(primos(5))
