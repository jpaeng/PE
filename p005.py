# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import common


def least_common_multiple_of_sequence(maxfactor):
    product = 1
    prime_list = common.sieve_erathosthenes(maxfactor)
    for prime in prime_list:
        prime_product = prime
        while prime_product <= maxfactor:
            product *= prime
            prime_product *= prime
    return product


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    print(least_common_multiple_of_sequence(10))
    print(least_common_multiple_of_sequence(20))
