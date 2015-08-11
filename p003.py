# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def solution(n):
    if n<2:
        return 0

    # Remove factor out all 2s
    if n%2 == 0:
        lastFactor = 2
        n /= 2
        while n%2 == 0:
            n /= 2
    else:
        lastFactor = 3

    # At this point, only odd factors remain
    factor = 3
    maxFactor = int(math.sqrt(n))+1
    while n>1 and factor<maxFactor:
        if n%factor == 0:
            n /= factor
            lastFactor = factor
            while n%factor == 0:
                n /= factor
            maxFactor = int(math.sqrt(n))+1
        factor = factor + 2

    if n == 1:
        return lastFactor
    else:
        return n

print(solution(5))
print(solution(13195))
print(solution(600851475143))

