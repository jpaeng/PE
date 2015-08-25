# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import common


def solution(n):
    prime_list = common.sieve_erathosthenes(n)
    return sum(prime_list)


print(solution(2000000))
