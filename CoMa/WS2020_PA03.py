import math
import time

def sieve(n):
    start = time.time()
    N = prepareList(n)
    if N != False:
        for i in range(1,int(math.sqrt(n))):
            if N[i] == True:
                for j in range(i+1,n):
                    if (j+1)%(i+1)==0:
                        N[j] = False
    else:

        return None

    prim = []

    for i in range(1,n):
        if N[i]==True:
            prim.append(i+1)
    stopped_time = time.time() - start
    print("{}s for {} elemnts".format(stopped_time,n))
    return prim


def prepareList(n):
    if n < 2:

        return False
    else:
        N = [True for i in range(n)]

        return N


def isprime(n):
    prim = sieve(n)

    if prim==None:

        return None
    elif n in prim:

        return True
    else:

        return False


def factorization(n):
    m = n//2
    prims = sieve(m)
    factors = []
    dummy_n = n

    if prims == None:
        return None

    for i in range(len(prims)-1,-1,-1):
        j = 0
        print(dummy_n,prims[i],j)
        while dummy_n%prims[i]**(j+1)==0:
            j += 1

        if j!=0:
            dummy_n = dummy_n / prims[i]**j
            factors.append([prims[i],j])

    return sorted(factors, key=lambda prim: prim[0])


def divisornumber(n):
    N =  factorization(n)

    if N == None:
        return None

    elif n == 1:
        return 1

    else:
        r = 1
        for i in N:
            r = r * (i[1]+1)
        return r


def iscoprime(n,m):
    N = divisornumber(n)
    M = divisornumber(m)
    M_N = divisornumber(n*m)

    if N==None or M==None:
        return None
    elif M_N == N * M:
        return True

    else:
        return False