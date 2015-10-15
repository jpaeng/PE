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
        number_length = 0
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
        k = int(common.str_permutation(j, digits))
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


# Problem 43: Sub-string Divisibility
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits
# 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
# Notes:
#     Since d2d3d4 is divisible by 2, d4 must be divisible by 2
#     Since d4d5d6 is divisible by 5, d6 must be either 0 or 5

def pandigital_sub_divisible(str_d4, str_d6, digits):
    """Return list 0-to-9 pandigital numbers that are divisible as described above."""
    digits = digits.replace(str_d4, "")
    digits = digits.replace(str_d6, "")
    divisible_pan_list = []

    # Loop through all permutations of digits
    for i in range(math.factorial(len(digits))):
        str_n = common.str_permutation(i, digits)
        str_n = str_n[:3] + str_d4 + str_n[3:]    # Create d2d3d4 divisible by 2
        str_n = str_n[:5] + str_d6 + str_n[5:]    # Create d4d5d6 divisible by 5
        d3d4d5 = int(str_n[2:5])
        if d3d4d5 % 3 == 0:
            d5d6d7 = int(str_n[4:7])
            if d5d6d7 % 7 == 0:
                d6d7d8 = int(str_n[5:8])
                if d6d7d8 % 11 == 0:
                    d7d8d9 = int(str_n[6:9])
                    if d7d8d9 % 13 == 0:
                        d8d9d10 = int(str_n[7:10])
                        if d8d9d10 % 17 == 0:
                            divisible_pan_list.append(int(str_n))
    return divisible_pan_list


# Problem 44: Pentagon Numbers
# Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2.
# The first ten pentagonal numbers are:
#     1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
# However, their difference, 70 - 22 = 48, is not pentagonal.
# Find the pair of pentagonal numbers, Pj and Pk, for which their
# sum and difference are pentagonal and D = |Pk - Pj| is minimised;
# what is the value of D?

def pentagonal_min_diff():
    """Return pentagonal pair with minimal difference that is also a pentagonal number."""
    n = 1
    pn = [1.0]
    min_diff = 10**9
    min_pair = ()
    sum_diff_pairs = []
    while True:
        n += 1
        new_pn = n*(3*n-1)/2
        for pn2 in reversed(pn):
            pn1 = new_pn - pn2
            if pn1 >= pn2:
                break
            elif common.is_in_ordered_list(pn1, pn):
                diff = pn2 - pn1
                if common.is_in_ordered_list(diff, pn):
                    sum_diff_pairs.append((int(pn1), int(pn2)))
                    print(sum_diff_pairs)
                    if min_diff > diff:
                        min_diff = diff
                        min_pair = (int(pn1), int(pn2))
        if min_diff < (new_pn - pn[len(pn)-1]):      # Stop if min_diff is less than the last pn step
            break
        else:
            pn.append(new_pn)
    return min_pair, min_diff


# Problem 45: Triangular, Pentagonal, and Hexagonal
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#     Triangle    Tn=n(n+1)/2   1, 3, 6, 10, 15, ...
#     Pentagonal  Pn=n(3n-1)/2  1, 5, 12, 22, 35, ...
#     Hexagonal   Hn=n(2n-1)    1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.

def tri_pent_hex(count):
    results = []
    t_index = 1
    p_index = 1
    h_index = 1
    tn = 1
    pn = 1
    hn = 1
    found = 0
    while found < count:
        while hn < max(tn, pn):
            h_index += 1
            hn = h_index*(2*h_index-1)
        while pn < max(tn, hn):
            p_index += 1
            pn = int(p_index*(3*p_index-1)/2)
        while tn < max(pn, hn):
            t_index += 1
            tn = int(t_index*(t_index+1)/2)
        if tn == pn == hn:
            results.append(int(tn))
            found += 1
            t_index += 1
            p_index += 1
            h_index += 1
            tn = t_index*(t_index+1)/2
            pn = p_index*(3*p_index-1)/2
            hn = h_index*(2*h_index-1)
    return results
        
        
# Problem 46: Goldbach's Other Conjecture
# It was proposed by Christian Goldbach that every odd composite number can
# be written as the sum of a prime and twice a square.
#      9 = 7 + 2x1**2
#     15 = 7 + 2x2**2
#     21 = 3 + 2x3**2
#     25 = 7 + 2x3**2
#     27 = 19 + 2x2**2
#     33 = 31 + 2x1**2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime
# and twice a square?

def not_goldbach(max_n, count):
    """ Return list of numbers that do not fit Goldbach's conjecture."""
    prime_list = common.sieve_erathosthenes(max_n)
    square_list = [n*n for n in range(1, int(math.sqrt(max_n))+1)]
    results = []

    for n in range(9, max_n, 2):    # Loop through odd numbers
        if not common.is_in_ordered_list(n, prime_list):    # composite is the opposite of prime
            found = False
            for p in prime_list:
                if p > (n-2):
                    break
                else:
                    n_p_2 = int((n - p)/2)
                    if common.is_in_ordered_list(n_p_2, square_list):
                        found = True
                        break
            if not found:
                results.append(n)
                if len(results) >= count:
                    break
    return results


# Problem 47: Distinct Primes Factors
# The first two consecutive numbers to have two distinct prime factors are:
#     14 = 2 x 7
#     15 = 3 x 5
# The first three consecutive numbers to have three distinct prime factors are:
#     644 = 2**2 x 7 x 23
#     645 = 3 x 5 x 43
#     646 = 2 x 17 x 19.
# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?

def consecutive_prime_factors(prime_factor_count, consecutive_count, max_n):
    """Return first sequence of numbers that have at least prime_factor_count."""
    prime_list = common.sieve_erathosthenes(max_n)
    n = 1
    count = 0
    while count < consecutive_count and n < max_n:
        n += 1
        if len(common.get_prime_factors(n, prime_list)) >= prime_factor_count:
            count += 1
        else:
            count = 0
    if n < max_n:
        results = [n-i for i in reversed(range(consecutive_count))]
    else:
        results = []
    return results


# Problem 48: Self Powers
# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

def sum_self_powers(max_n):
    """Return sum of self powers up to max_n."""
    result = 0
    for n in range(1, max_n+1):
        result += n**n
    return result


# Problem 49: Prime Permutations
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways:
#     (i) each of the three terms are prime, and,
#     (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

def prime_permutation_arithmetic_sequence(digit_count, term_count):
    """Return lists of arithmetic sequences that are both prime and permutations of digits."""

    # Make list of prime numbers of the correct digit_count.
    prime_list = common.sieve_erathosthenes(10**digit_count)
    n = 10**(digit_count-1)
    index = -1
    while index < 0:    # find index of first prime number with correct digit_count
        n += 1
        index = common.index_in_ordered_list(n, prime_list)     # returns -1 if n not found
    prime_list = prime_list[index:]   # prime_list now contains only primes of digit_count

    results = []        # results = the return variable to contain the sequence lists.

    # Loop thru each prime
    perm_count = math.factorial(digit_count)    # perm_count = the number of possible permutation of digit_count
    for prime in prime_list:        # loop thru primes
        str_digits = str(prime)
        perm_list = [prime]
        for index in range(1, perm_count):  # loop thru all permutations
            perm = int(common.str_permutation(index, str_digits))
            if common.is_in_ordered_list(perm, prime_list) and perm not in perm_list:
                perm_list.append(perm)      # perm_list contains only permutations that are prime
        len_perm_list = len(perm_list)
        if len_perm_list == 1:
            pass
        elif len_perm_list < term_count:
            for perm in reversed(perm_list[1:]):    # delete from prime_list all primes that are in perm_list so we
                prime_list.remove(perm)             # we don't recheck those primes.
        else:
            perm_list.sort()

            # Create diff_array containing the differences between each element of perm_list
            diff_array = [[0]*len_perm_list for x in range(len_perm_list)]
            for x in range(len_perm_list-1):
                for y in range(x+1, len_perm_list):
                    diff_array[x][y] = perm_list[y] - perm_list[x]

            # Count the number of equal differences between perm_list elements to find arithmetic sequences.
            for x in range(len_perm_list-1):
                for y in range(x+1, len_perm_list):
                    if diff_array[x][y]:        # diff_array[x][y] != 0
                        diff_count = common.count_in_array(diff_array[x][y], diff_array)    # count the number of diffs
                        if diff_count > 1:
                            # seq_coords gets the indices of the perm_list elements that have common differences.
                            # if any index occurs twice, this indicates the index of an element that is half-way
                            # between two others.
                            seq_coords = common.coords_in_array(diff_array[x][y], diff_array)
                            common_nodes = 0
                            for x1, y1 in seq_coords:
                                if common.count_in_array(x1, seq_coords) == 2:
                                    common_nodes += 1
                            if common_nodes >= term_count-2:
                                seq_list = []
                                for x1, y1 in seq_coords:
                                    if perm_list[x1] not in seq_list:
                                        seq_list.append(perm_list[x1])
                                    if perm_list[y1] not in seq_list:
                                        seq_list.append(perm_list[y1])
                                seq_list.sort()
                                results.append(seq_list)
                            for x1, y1 in seq_coords:
                                diff_array[x1][y1] = 0
                        else:
                            diff_array[x][y] = 0
            for perm in reversed(perm_list[1:]):    # delete from prime_list all primes that are in perm_list so we
                prime_list.remove(perm)             # we don't recheck those primes.
    return results






# Problem 40-49 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 49

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
        print(zdigcount, pandigital_primes(zdigcount, zdigits[:zdigcount]))
        zdigcount = 9
        print(zdigcount, pandigital_primes(zdigcount, zdigits[:zdigcount]))
    elif problem_num == 42:
        z_file = open('p042_words.txt')
        z_word_list = (z_file.read().replace('"', '')).split(',')
        z_file.close()
        print(triangle_words(['sky', 'SKY', 'ski'], 25))
        print(triangle_words(z_word_list, 25))
    elif problem_num == 43:
        z_digits = '0123456789'
        z_pan_div_list = pandigital_sub_divisible('0', '5', z_digits)
        for even in ['2', '4', '6', '8']:
            for five in ['0', '5']:
                z_pan_div_list.extend(pandigital_sub_divisible(even, five, z_digits))
        print(z_pan_div_list, sum(z_pan_div_list))
    elif problem_num == 44:
        print(pentagonal_min_diff())
    elif problem_num == 45:
        print(tri_pent_hex(3))
    elif problem_num == 46:
        print(not_goldbach(10**6, 2))
    elif problem_num == 47:
        print(consecutive_prime_factors(2, 2, 100))
        print(consecutive_prime_factors(3, 3, 1000))
        print(consecutive_prime_factors(4, 4, 10**6))
    elif problem_num == 48:
        print(sum_self_powers(10))
        print(sum_self_powers(100))
        print(str(sum_self_powers(1000))[-10:])
    elif problem_num == 49:
        zlist = [z for z in range(10)]
        for z in zlist:
            print(z)
            zlist.remove(zlist[len(zlist)-1])
        zlist = [z for z in range(10)]
        for z in zlist:
            print(z)
            zlist.remove(z)
        print(prime_permutation_arithmetic_sequence(4, 3))
