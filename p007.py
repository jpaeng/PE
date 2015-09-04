# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# There are approximately X/ln(X) primes among the first X numbers.
# So the nth prime will be close to the number -nW(-1/n) where W() is the Lambert product log function.

import scipy.special
import common


def nth_prime(n):
    # valid for n >= 4
    search_range = (-n)*(scipy.special.lambertw(-1.0/n, -1)).real
    prime_list = common.sieve_erathosthenes(int(search_range))
    return prime_list[n-1]


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    print(nth_prime(4))
    print(nth_prime(6))
    print(nth_prime(10))
    print(nth_prime(150))
    print(nth_prime(10001))
