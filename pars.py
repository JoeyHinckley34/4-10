from operator import mul
from fractions import Fraction
from functools import reduce

def nCk(n, k): 
    return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))

def genPars(n):
    if n < 2:
        return []
    parList = []
    for i in range(0, n*2, 2):
        for j in range(i+4, n*2+1, 2):
            parList.append([i, j])
    if not (nCk(n, 2) == len(parList)):
        print("Error generating parentheses")
        return []
    return parList

def printnCkpretty(x):
    for n in range(x):
        print(' '.join('%5d' % nCk(n, k) for k in range(n+1)).center(100))


def test():
    n = [ 1, '+', 2, '+', 5, '+', 5]

    parList = genPars(int((len(n)+1)/2))

    final = [n]

    for p in parList:
        x = n[:]

        print(x)

        if len(p) != 2:
            print("ERROR incorrect number of parentheses")
        x.insert(p[0],'(')
        x.insert(p[1],')')
        final.append(x)

    for f in final:
        print(f)

    printnCkpretty(17)

test()


