import sys
import math
import time
import gc
import random
import matplotlib.pyplot as plt
import numpy as np

digitVTime = {}
def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

nargs = len(sys.argv)
if nargs != 2:
    sys.exit()

n = int(sys.argv[1])


def lcm(a,b):
    r = a*b
    j = r//gcd(a,b)
    return j

def gcdExtended(a, b):
    if a == 0: return b,0,1
    gcd,x1,y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd,x,y

def modInverse(a, m):
    g,x,_ = gcdExtended(a, m)
    if g != 1:return None
    res = (x % m + m) % m
    return res
 
def pow(x, y, M):
    res = 1
    x = x % M
    if x == 0: return 0
    while y > 0:
        # print(y)
        if (y & 1) == 1:
            res = (res*x)%M
        y = y >> 1
        x = (x*x)%M
    return res

def getFactor(n):
    r = int(math.sqrt(n))
    if n%2 == 0: return 2,n//2
    for i in range(3,r+1,2):
        if n%i == 0: return i, n//i
    return None, None

def getKeys(n):
    # global digitVTime
    start_time = time.time()
    factor1, factor2 = getFactor(n)
    end_time = time.time()
    # timeTaken = end_time - start_time
    # digit = len(str(n))
    # if digit in digitVTime.keys():
    #     if digitVTime[digit] < timeTaken:
    #         digitVTime[digit] = timeTaken
    # else:
    #     digitVTime[digit] = timeTaken

    print("factor ", factor1, " ", factor2)
    print("Time Taken to factorize N(digit) ",len(str(n)), " ", end_time-start_time)
    phi = (factor1-1)*(factor2-1)
    if factor1 != factor2:
        phi = lcm(factor2-1, factor1-1)
    else:
        phi = factor1*(factor2 -1)
    while True:
        e = random.randrange(2, phi)
        if gcd(phi,e)==1:break
    d = modInverse(e,phi)
    return e,d


def encrypt(plainText, e, n):
    cipherText = ''
    for c in plainText:
        c = ord(c)
        c = pow(c,e,n)
        cipherText += str(c) + " "
    return cipherText

def decrypt(cipherText, d, n):
    plainText = ''
    cipherText = cipherText.strip().split()
    for c in cipherText:
        c = int(c)
        c = pow(c,d,n)
        plainText += chr(c)
    return plainText

plainText = open('plaintext.txt', 'r').read()

def main(n):
    global plainText
    e,d = getKeys(n)
    print("encryption Key=",e,"decryption Key=",d,"number=", n)
    print('plainText ', plainText)
    cipherText = encrypt(plainText, e, n)
    print('cipherText ', cipherText)
    plainText = decrypt(cipherText,d,n)
    print('plainText ', plainText)

main(n)
'''


fp = open('nlist.txt', 'r')
for line in fp:
    n = int(line)
    # print(len(str(n)), " ", n)
    if len(str(n)) >21: break
    gc.collect()
    main(n)


plt.plot(digitVTime.keys(), digitVTime.values(), marker = 'o')
plt.title("Plot-1 Digit in Number vs Time to factorize")
plt.xlabel("Digit in Number")
plt.ylabel("Time to factorize")
plt.show()
'''