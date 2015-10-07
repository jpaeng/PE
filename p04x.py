""" Project Euler Problems 40-49
"""


import math
import string
import common

from timeit import default_timer as timer


# Problem 40: Champernowne's Constant
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part,
# find the value of the following expression.
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

def get_nth_digits_loop(n_list):
    """ Return list of nth digits of Champernovne's Constant given a list of n's. Longer execution vs formula."""
    nth_digits = []
    number = 0
    index = 0
    next_n = n_list.pop(0)
    found_all = False
    while not found_all:
        number += 1
        str_number = str(number)
        str_length = len(str_number)
        if next_n <= (index + str_length):
            for digit in range(str_length):
                index += 1
                if next_n == index:
                    nth_digits.append(int(str_number[digit]))
                    if len(n_list) == 0:
                        found_all = True
                        break
                    else:
                        next_n = n_list.pop(0)
        else:
            index += str_length
    return nth_digits


def get_nth_digits_formula(n_list):
    """ Return list of nth digits of Champernovne's Constant given a list of n's. Longer execution vs formula."""
    dn_list = []
    for n in n_list:
        dn_list.append(nth_digit(n))
    return dn_list


def nth_digit(n):
    """ Return nth digit (dn) of Champernovne's Constant."""

    # Constant = 0.123456789101112131415161718192021...
    # Corresponding base numbers 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ...

    # Find length of base number that dn is part of
    if n < 10:
        number_length = 1
    else:
        sub_tot = 0
        for k in range(2, 12):
            sub_tot += 10**(k-1)
            if n < (k * 10**k - sub_tot):   # Calculate n for each base number = 10**k
                number_length = k
                break

    # base number = the sequential number that dn is part of
    # position = digit position of dn in base number
    base_number = n
    for k in range(1, number_length):
        base_number += 10**k
    position = base_number % number_length
    base_number = int(base_number/number_length)

    # Find nth digit dn
    dn = int(str(base_number)[position])

    # print(n, number_length, base_number, position, dn)
    return dn


# Problem 41:  Pandigital Prime
# We shall say that an n-digit number is pandigital if
# it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
# Notes:
#   Number of permutations of '123456789' is 9! = 362880
#   Number of primes below 987654321 is n/ln(n) = 476987788

def pandigital_primes(n, digits):
    """ Return list of all n-digit pandigital primes."""
    prime_list = common.sieve_erathosthenes(10**n)
    pan_prime_list = []
    perm_count = math.factorial(n)
    for j in range(perm_count):
        k = int(common.lexi_perm(j, digits))
        if common.is_in_ordered_list(k, prime_list):
            pan_prime_list.append(k)
    return pan_prime_list


# Problem 42: Coded Triangle Numbers
# The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1);
# so the first ten triangle numbers are:
#     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?

def triangle_words(word_list, max_word_length):
    """Return list of triangle words in word_list."""
    alpha_values = dict(zip([char for char in string.ascii_uppercase], range(1, 27)))   # Dictionary of values for each
    alpha_values.update(dict(zip([char for char in string.ascii_lowercase], range(1, 27))))     # letter
    max_tn = max_word_length*26
    max_n = int(-0.5 + math.sqrt(0.25 + 2*max_tn)) + 1
    tn_list = tuple(int(n*(n+1)/2) for n in range(max_n+1))     # list of triangle numbers
    tr_word_list = []

    for word in word_list:
        word_value = 0
        for char in word:
            word_value += alpha_values.get(char)
        if word_value in tn_list:
            tr_word_list.append((word, word_value))
    return tr_word_list



# Problem 40-49 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 42

    if problem_num == 40:
        print()
        print(get_nth_digits_loop([10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7]))
        print(get_nth_digits_loop([190, 2890, 38890, 488890, 5888890, 68888890]))
        print()
        print(get_nth_digits_formula([10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7]))
        print(get_nth_digits_formula([190, 2890, 38890, 488890, 5888890, 68888890]))
        print()
        z_count = 1000
        start = timer()
        for z in range(z_count):
            get_nth_digits_loop([10**3, 10**4, 10**5])
        time1 = timer()
        for z in range(z_count):
            get_nth_digits_formula([10**3, 10**4, 10**5])
        time2 = timer()

        print(time1-start)  # in ms
        print(time2-time1)  # in ms
    elif problem_num == 41:
        zdigits = '123456789'
        zdigcount = 4
        print(zdigcount, pandigital_primes(zdigcount, zdigits[:zdigcount]))
        zdigcount = 5
        print(zdigcount, pandigital_primes(zdigcount, zdigits[:zdigcount]))
        zdigcount = 6
        print(zdigcount, pandigital_primes(zdigcount, zdigits[:zdigcount]))
        zdigcount = 7
        print(zdigcount, pandigital_primes(zdigcount, zdigits[:zdigcount]))
        zdigcount = 8
        # print(zdigcount, pandigital_primes(zdigcount, zdigits[:zdigcount]))
        zdigcount = 9
        # print(zdigcount, pandigital_primes(zdigcount, zdigits[:zdigcount]))
    elif problem_num == 42:
        z_file = open('p042_words.txt')
        z_word_list = (z_file.read().replace('"', '')).split(',')
        z_file.close()
        print(triangle_words(['sky', 'SKY', 'ski'], 25))
        print(triangle_words(z_word_list, 25))
