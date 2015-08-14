# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import common

def solution(maxfactor):
    product = 1
    primeList = common.sieve_erathosthenes(maxfactor)
    for prime in primeList:
        primeProduct=prime
        while primeProduct <= maxfactor:
            product *= prime
            primeProduct *= prime
    return product

print(solution(10))
print(solution(20))

