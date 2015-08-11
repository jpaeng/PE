
import math


# = List Procedures =================================
def indexInOrderedList(n, orderedList):      # binary search
    lo = 0
    hi = len(orderedList)-1
    while (hi - lo) > 1:
        mid = int((lo+hi)/2)
        if n == orderedList[mid]:
            return mid
        elif n < orderedList[mid]:
            hi = mid
        else:
            lo = mid

    if n == orderedList[lo]:
        return lo
    elif n == orderedList[hi]:
        return hi

    return -1


def isInOrderedList(n, orderedList):      # binary search
    index = indexInOrderedList(n, orderedList)
    if index < 0:
        return False
    else:
        return True


# = Prime Procedures =================================
def sieve_erathosthenes(n):
    boolTable = [True]*(n+1)
    boolTable[0] = False
    boolTable[1] = False

    primeList = []
    sqrtn = int(math.sqrt(n))
    for i in range(2, sqrtn+1):
        if boolTable[i]:
            primeList.append(i)
            for j in range(i**2, n+1, i):
                boolTable[j] = False

    if sqrtn%2 == 0:
        sqrtn += 1
    else:
        sqrtn += 2
    for i in range(sqrtn, n+1, 2):
        if boolTable[i]:
            primeList.append(i)

    return primeList


def getPrimeFactors(num, primeList):
    if isInOrderedList(num, primeList):
        result = [num]
    else:
        result = []
        hiresult = []
        maxcheck = int(math.sqrt(num))+1
        for n in range(2,maxcheck):
            if num%n == 0:
                n2 = num/n
                if isInOrderedList(n, primeList):
                    result.append(n)
                if isInOrderedList(n2, primeList) and (n != n2):
                    hiresult.insert(0,num/n)
        result.extend(hiresult)
    return(result)