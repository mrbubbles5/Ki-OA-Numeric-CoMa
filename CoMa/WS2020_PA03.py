def sieve(n):
    N = prepareList(n)
    if N:
        for i in range(1,int(sqrt(n))):
            if N[i] == True:
                for j in range(i,n):
                    if N[j]%N[i]==0:
                        N[j] = False
    else:

        return None

    prim = []

    for i in range(1,n+1):
        if N[i]==True:
            prim.append(i+1)

    return prim


def prepareList(n):
    if n < 2:

        return False
    else:
        N = [True for i in range(n)]

        return N


def isprim(n):
    prim = sieve(n)

    if not prim:

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

        while dummy_n%prims[i]^(j+1)==0:
            j += 1

        if j!=0:
            dummy_n = dummy_n - prims[i]^j
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
            r = r + i[1]
        return r


def iscoprime(n,m):
    N = divisornumber(n)
    M = divisornumber(m)
    M_N = divisornumber(n*m)

    if n==None or m==None:
        return None
    elif M_N == N * M:
        return True

    else:
        return False