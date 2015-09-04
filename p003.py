# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def largest_prime_factor(n):
    if n < 2:
        return 0

    # Remove factor out all 2s
    if n % 2 == 0:
        last_factor = 2
        n /= 2
        while n % 2 == 0:
            n /= 2
    else:
        last_factor = 3

    # At this point, only odd factors remain
    factor = 3
    max_factor = int(math.sqrt(n))+1
    while n > 1 and factor < max_factor:
        if n % factor == 0:
            n /= factor
            last_factor = factor
            while n % factor == 0:
                n /= factor
            max_factor = int(math.sqrt(n))+1
        factor += 2

    if n == 1:
        return last_factor
    else:
        return n

if __name__ == '__main__':
    print(largest_prime_factor(5))
    print(largest_prime_factor(13195))
    print(largest_prime_factor(600851475143))
