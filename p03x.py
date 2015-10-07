""" Project Euler Problems 30-39
"""


import math
import common

from timeit import default_timer as timer


# Problem 30:  Digit Fifth Powers
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#     1634 = 1**4 + 6**4 + 3**4 + 4**4
#     8208 = 8**4 + 2**4 + 0**4 + 8**4
#     9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_of_digit_powers(n, power):
    """ Return sum of digits of n each raised to power.  Text conversion algorithm."""
    str_num = str(n)
    result = 0
    for a in str_num:
        result += int(a)**power
    return result


def position_value(n, position):
    """ Return the digit at position of n. LSB = position zero."""
    return int(n/(10**position) - 10*(int(n/(10**(position+1)))))


def increment_position(n, position):
    """ Return n with position digit incremented by 1."""
    return n + 10**position


def perfect_digit_powers(power):
    """ Return list of all perfect digit power numbers for a given power."""

    perfect_dig_list = set_next_digit(0, power, power)

    return perfect_dig_list


def set_next_digit(current_num, position, power):
    """ Return a list of perfect digit powers found by recursing position by position from msb to lsb."""
    current_sum = sum_of_digit_powers(current_num, power)
    incr_max = (current_num + (10**(position+1) - 1) - current_sum)
    if incr_max > 0:
        incr_max = int(incr_max**(1/power))     # loop max = root of (highest possible number) - (current sum)
    else:
        incr_max = 0
    if position == 0:
        current_num += incr_max
        if current_num == sum_of_digit_powers(current_num, power):
            perfect_dig_list = [current_num]
        else:
            perfect_dig_list = []
    else:
        perfect_dig_list = []
        incr_min = (current_num - (current_sum + position*9**power))
        if incr_min > 0:
            incr_min = int(incr_min**(1/power))     # loop min = root of (current number) - (highest possible sum)
        else:
            incr_min = 0

        for i in range(incr_min):
            current_num = increment_position(current_num, position)

        for i in range(incr_min, incr_max + 1):
            perfect_dig_list.extend(set_next_digit(current_num, position - 1, power))
            current_num = increment_position(current_num, position)
    return perfect_dig_list


# Problem 31:  Coin Sums
# In England the currency is made up of pound, L, and pence, p,
#     and there are eight coins in general circulation:
#         1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
# It is possible to make L2 in the following way:
#     1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can L2 be made using any number of coins?

def coin_combinations(value, coin_list, smallest_coin):
    """ Return the count of different possible combinations of coin_list coins that sum to the given value."""
    count = 0
    if len(coin_list) > 1:
        while value >= 0:
            count += coin_combinations(value, coin_list[1:], smallest_coin)
            value -= coin_list[0]
        return count
    elif (value >= 0) and (value % smallest_coin == 0):
        return 1
    else:
        return 0


# Problem 32:  Pandigital Products
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
#     for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier,
#     and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as
#     a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def is_pandigital_3(a, b, c):
    """ Return True if a, b, c combine to be pandigital per str_digits"""
    str_digits = '123456789'
    str_num = str(a) + str(b) + str(c)
    if len(str_num) == len(str_digits):
        for n in str_digits:
            if str_num.count(n) != 1:
                return False
    else:
        return False
    return True


def pandigital_products():
    """ Return list of products(c) of pandigital identities a * b = c."""
    pandigital_c_list = []

    # For 1-digit a, 4-digit b, and 4-digit c
    for a in range(2, 10):  # loop through 1-digit a
        b = 1233            # min b = 1234
        c = a * b
        while c < 9876:     # max c = 9876
            b += 1
            c = a * b
            if is_pandigital_3(a, b, c):
                if c not in pandigital_c_list:
                    pandigital_c_list.append(c)

    # For 2-digit a, 3-digit b, and 4-digit c
    for a in range(12, 99):  # loop through 2-digit a
        b = 122             # min b = 123
        c = a * b
        while c < 9876:     # max c = 9876
            b += 1
            c = a * b
            if is_pandigital_3(a, b, c):
                if c not in pandigital_c_list:
                    pandigital_c_list.append(c)
    return pandigital_c_list


# Problem 33:  Digit Canceling Fractions
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
# is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def digit_canceling_fractions():
    """ Return list of non-trivial digit canceling fractions."""
    fraction_list = []
    for num in range(1, 9):             # All possible single-digit numerators for fractions < 1
        for den in range(num+1, 10):    # All possible single-digit denominators for a given numerator for fractions < 1
            for digit in range(1, 10):  # All possible added digit
                fraction0 = num/den
                fraction1 = (digit*10 + num)/(den*10 + digit)
                fraction2 = (num*10 + digit)/(digit*10 + den)
                if fraction0 == fraction1:
                    fraction_list.append((num, den, (digit*10 + num), (den*10 + digit), fraction1))
                if fraction0 == fraction2:
                    fraction_list.append((num, den, (num*10 + digit), (digit*10 + den), fraction2))
    return fraction_list


# Problem 34:  Digit Factorials
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def digit_factorial_sum(n):
    """ Return the sum of the factorials of the digits of n."""
    factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)    # factorials for digits 0-9
    result = 0
    for char in str(n):
        result += factorials[int(char)]
    return result


def factorial_sum_search(in_n, num_length, start_n, max_n):
    """ Return list of numbers equal to factorial sum - recursive."""
    result = []
    # print(in_n)
    for num in range(start_n, min(10**num_length, max_n), 10**(num_length-1)):
        n = in_n + num
        fact_sum = digit_factorial_sum(n)
        if fact_sum > (n+num_length):
            break
        elif num_length == 1:
            if fact_sum == n:
                result.append(n)
        else:
            result.extend(factorial_sum_search(n, num_length-1, 0, max_n))

    return result


def factorial_sum_list(max_num=-1):
    """ Return list of all numbers which are equal to the sum of the factorials of their digits."""

    # Constants
    factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)    # factorials for digits 0-9

    # Max number to check
    max_digit_count = int(math.log10(factorials[9]*math.log10(factorials[9]))) + 1
    if max_num < 0:
        max_num = min(factorials[9]*max_digit_count, 10**(max_digit_count+1))

    # 1-digit numbers
    result_list = factorial_sum_search(0, 1, 0, max_num)

    # 2-digit numbers
    result_list.extend(factorial_sum_search(0, 2, 10**1, max_num))

    # 3-digit numbers
    result_list.extend(factorial_sum_search(0, 3, 10**2, max_num))

    # 4-digit numbers
    result_list.extend(factorial_sum_search(0, 4, 10**3, max_num))

    # 5-digit numbers
    result_list.extend(factorial_sum_search(0, 5, 10**4, max_num))

    # 6-digit numbers
    result_list.extend(factorial_sum_search(0, 6, 10**5, max_num))

    # 7-digit numbers
    result_list.extend(factorial_sum_search(0, 7, 10**6, max_num))

    return result_list


def factorial_sum_list_old(max_num=-1):
    """ Return list of all numbers which are equal to the sum of the factorials of their digits."""

    # Constants
    factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)    # factorials for digits 0-9
#    max_digits = (0, 3, 4, 6, 7, 8, 9, 9)      # the max digit that can be used at each digit count,
    #                                           e.g. 2-digit numbers can only use digits 0-4

    # Max number to check
    max_digit_count = int(math.log10(factorials[9]*math.log10(factorials[9]))) + 1
    if max_num < 0:
        max_num = min(factorials[9]*max_digit_count, 10**(max_digit_count+1))

    result_list = []

    # 1-digit numbers
    num_length = 1
#    for num0 in range(max_digits[num_length] + 1):
    for num0 in range(10):
        n = num0
        fact_sum = digit_factorial_sum(n)
        if fact_sum > (n+num_length):
            break
        elif fact_sum == n:
            result_list.append(n)

    # 2-digit numbers
    num_length = 2
    # for num1 in range(10, 10*(max_digits[num_length] + 1), 10):
    for num1 in range(10, 100, 10):
        n = num1
        fact_sum = digit_factorial_sum(n)
        if n > max_num:
            break
        elif fact_sum > (n+num_length):
            break
        else:
            # for num0 in range(max_digits[num_length] + 1):
            for num0 in range(10):
                n = num1 + num0
                fact_sum = digit_factorial_sum(n)
                if fact_sum > (n+num_length):
                    break
                elif fact_sum == n:
                    result_list.append(n)

    # 3-digit numbers
    num_length = 3
    for num2 in range(100, 1000, 100):
        n = num2
        fact_sum = digit_factorial_sum(n)
        if n > max_num:
            break
        elif fact_sum > (n+num_length):
            break
        else:
            for num1 in range(0, 100, 10):
                n = num2 + num1
                fact_sum = digit_factorial_sum(n)
                if fact_sum > (n+num_length):
                    break
                else:
                    for num0 in range(10):
                        n = num2 + num1 + num0
                        fact_sum = digit_factorial_sum(n)
                        if fact_sum > (n+num_length):
                            break
                        elif fact_sum == n:
                            result_list.append(n)

    # 4-digit numbers
    num_length = 4
    for num3 in range(1000, 10000, 1000):
        n = num3
        fact_sum = digit_factorial_sum(n)
        if n > max_num:
            break
        elif fact_sum > (n+num_length):
            break
        else:
            for num2 in range(0, 1000, 100):
                n = num3 + num2
                fact_sum = digit_factorial_sum(n)
                if fact_sum > (n+num_length):
                    break
                else:
                    for num1 in range(0, 100, 10):
                        n = num3 + num2 + num1
                        fact_sum = digit_factorial_sum(n)
                        if fact_sum > (n+num_length):
                            break
                        else:
                            for num0 in range(10):
                                n = num3 + num2 + num1 + num0
                                fact_sum = digit_factorial_sum(n)
                                if fact_sum > (n+num_length):
                                    break
                                elif fact_sum == n:
                                    result_list.append(n)

    # 5-digit numbers
    num_length = 5
    for num4 in range(10000, 100000, 10000):
        n = num4
        fact_sum = digit_factorial_sum(n)
        if n > max_num:
            break
        elif fact_sum > (n+num_length):
            break
        else:
            for num3 in range(0, 10000, 1000):
                n = num4 + num3
                fact_sum = digit_factorial_sum(n)
                if fact_sum > (n+num_length):
                    break
                else:
                    for num2 in range(0, 1000, 100):
                        n = num4 + num3 + num2
                        fact_sum = digit_factorial_sum(n)
                        if fact_sum > (n+num_length):
                            break
                        else:
                            for num1 in range(0, 100, 10):
                                n = num4 + num3 + num2 + num1
                                fact_sum = digit_factorial_sum(n)
                                if fact_sum > (n+num_length):
                                    break
                                else:
                                    for num0 in range(10):
                                        n = num4 + num3 + num2 + num1 + num0
                                        fact_sum = digit_factorial_sum(n)
                                        if fact_sum > (n+num_length):
                                            break
                                        elif fact_sum == n:
                                            result_list.append(n)

    # 6-digit numbers
    num_length = 6
    for num5 in range(100000, 1000000, 100000):
        n = num5
        fact_sum = digit_factorial_sum(n)
        if n > max_num:
            break
        elif fact_sum > (n+num_length):
            break
        else:
            for num4 in range(0, 100000, 10000):
                n = num5 + num4
                fact_sum = digit_factorial_sum(n)
                if fact_sum > (n+num_length):
                    break
                else:
                    for num3 in range(0, 10000, 1000):
                        n = num5 + num4 + num3
                        fact_sum = digit_factorial_sum(n)
                        if fact_sum > (n+num_length):
                            break
                        else:
                            for num2 in range(0, 1000, 100):
                                n = num5 + num4 + num3 + num2
                                fact_sum = digit_factorial_sum(n)
                                if fact_sum > (n+num_length):
                                    break
                                else:
                                    for num1 in range(0, 100, 10):
                                        n = num5 + num4 + num3 + num2 + num1
                                        fact_sum = digit_factorial_sum(n)
                                        if fact_sum > (n+num_length):
                                            break
                                        else:
                                            for num0 in range(10):
                                                n = num5 + num4 + num3 + num2 + num1 + num0
                                                fact_sum = digit_factorial_sum(n)
                                                if fact_sum > (n+num_length):
                                                    break
                                                elif fact_sum == n:
                                                    result_list.append(n)

    # 7-digit numbers
    # num_length = 7
    for num6 in range(1000000, 10000000, 1000000):
        n = num6
        # fact_sum = digit_factorial_sum(n)
        # if fact_sum > (n+num_length):
        if n > max_num:
            break
        else:
            for num5 in range(0, 1000000, 100000):
                n = num6 + num5
                # fact_sum = digit_factorial_sum(n)
                # if fact_sum > (n+num_length):
                if n > max_num:
                    break
                else:
                    for num4 in range(0, 100000, 10000):
                        n = num6 + num5 + num4
                        # fact_sum = digit_factorial_sum(n)
                        # if fact_sum > (n+num_length):
                        if n > max_num:
                            break
                        else:
                            for num3 in range(0, 10000, 1000):
                                n = num6 + num5 + num4 + num3
                                # fact_sum = digit_factorial_sum(n)
                                # if fact_sum > (n+num_length):
                                if n > max_num:
                                    break
                                else:
                                    for num2 in range(0, 1000, 100):
                                        n = num6 + num5 + num4 + num3 + num2
                                        # fact_sum = digit_factorial_sum(n)
                                        # if fact_sum > (n+num_length):
                                        if n > max_num:
                                            break
                                        else:
                                            for num1 in range(0, 100, 10):
                                                n = num6 + num5 + num4 + num3 + num2 + num1
                                                # fact_sum = digit_factorial_sum(n)
                                                # if fact_sum > (n+num_length):
                                                if n > max_num:
                                                    break
                                                else:
                                                    for num0 in range(10):
                                                        n = num6 + num5 + num4 + num3 + num2 + num1 + num0
                                                        fact_sum = digit_factorial_sum(n)
                                                        # if fact_sum > (n+num_length):
                                                        if n > max_num:
                                                            break
                                                        elif fact_sum == n:
                                                            result_list.append(n)

    return result_list


# Problem 35: Circular Primes
# The number, 197, is called a circular prime because all rotations of the digits:
#     197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

def check_circular_prime_not_efficient_for_sparse_list(n, prime_list):
    """If circular prime, return a list of all rotational combinations of n.  Else if not circular prime, return []."""
    circ_prime_list = [n]
    circular_prime_flag = True
    str_n = str(n)
    length_n = len(str_n)
    if length_n > 1:
        str_n2 = str_n + str_n
        for j in range(length_n-1):
            str_n2 = str_n2[1:]
            x = int(str_n2[:length_n])
            if x in prime_list:
                if x != n:
                    circ_prime_list.append(x)
                    prime_list.remove(x)
            else:
                circular_prime_flag = False
    if circular_prime_flag:
        return circ_prime_list
    else:
        return []


def circular_primes_not_efficient_for_sparse_list(max_n):
    prime_list = common.sieve_erathosthenes(max_n)
    circ_prime_list = []
    for p in prime_list:
        circ_prime_list.extend(check_circular_prime_not_efficient_for_sparse_list(p, prime_list))
    circ_prime_list.sort()
    return circ_prime_list


def is_circular_prime(n, prime_list):
    """ Return True if n is circular prime or False if n is not circular prime."""
    strn = str(n)
    if len(strn) > 1:
        for i in range(1, len(strn)):
            strni = strn[i:] + strn[:i]
            # if int(strni) not in prime_list:
            if not common.is_in_ordered_list(int(strni), prime_list):
                return False
    return True


def circular_primes(max_n):
    """Return list of all circular primes up to max_n."""
    prime_list = common.sieve_erathosthenes(max_n)
    circ_prime_list = []
    for p in prime_list:
        if is_circular_prime(p, prime_list):
            circ_prime_list.append(p)
    return circ_prime_list


# Problem 36: Double-base Palindromes
# The decimal number, 585 = 1001001001(binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def double_base_palindromes(max_n):
    """ Return a list of all decimal-binary palindromes up to max_n."""
    palindromes = []
    for n in range(1, max_n + 1, 2):    # binary palindromes must be odd
        if common.is_str_palindrome(str(n)) and common.is_str_palindrome(bin(n)[2:]):
            palindromes.append(n)
    return palindromes


# Problem 37: Truncatable Primes
# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def old_next_right_extend_prime(str_n):
    """Recursive return list of primes created by adding digits to the right. Stop if added digit creates non-prime."""
    usable_digits = ('1', '3', '7', '9')    # all possible multi-digit primes must end with one of these digits
    n = int(str_n)
    if common.is_prime(n):
        primes = [n]
        for p in usable_digits:
            primes.extend(old_next_right_extend_prime(str_n+p))
        return primes
    else:
        return []


def old_next_left_extend_prime(str_n):
    """Recursive return list of primes created by adding digits to the left. Stop if added digit creates non-prime."""
    usable_digits = ('1', '2', '3', '5', '7', '9')  # will not generate complete list of primes - just those reducible to single digit primes.
    n = int(str_n)
    if common.is_prime(n):
        primes = [n]
        for p in usable_digits:
            primes.extend(old_next_left_extend_prime(p+str_n))
        return primes
    else:
        return []


def old_truncatable_primes():
    """Return list of primes that are both left and right truncatable."""
    left_extend_primes = old_next_left_extend_prime('3')
    left_extend_primes.extend(old_next_left_extend_prime('7'))

    right_extend_primes = old_next_right_extend_prime('2')
    right_extend_primes.extend(old_next_right_extend_prime('3'))
    right_extend_primes.extend(old_next_right_extend_prime('5'))
    right_extend_primes.extend(old_next_right_extend_prime('7'))

    left_extend_primes.sort()
    right_extend_primes.sort()
    trunc_primes = []
    for p in left_extend_primes[2:]:
        if p in right_extend_primes:
            trunc_primes.append(p)
    # print(left_extend_primes)
    # print(right_extend_primes)
    # print(trunc_primes)
    return trunc_primes


def next_right_extend_prime(str_n, prime_list):
    """Recursive return list of primes created by adding digits to the right. Stop if added digit creates non-prime."""
    usable_digits = ('1', '3', '7', '9')    # all possible multi-digit primes must end with one of these digits
    n = int(str_n)
    if common.is_in_ordered_list(n, prime_list):
        primes = [n]
        for p in usable_digits:
            primes.extend(next_right_extend_prime(str_n+p, prime_list))
        return primes
    else:
        return []


def next_left_extend_prime(str_n, prime_list):
    """Recursive return list of primes created by adding digits to the left. Stop if added digit creates non-prime."""
    usable_digits = ('1', '2', '3', '5', '7', '9')  # will not generate complete list of primes - just those reducible to single digit primes.
    n = int(str_n)
    if common.is_in_ordered_list(n, prime_list):
        primes = [n]
        for p in usable_digits:
            primes.extend(next_left_extend_prime(p+str_n, prime_list))
        return primes
    else:
        return []


def truncatable_primes():
    """Return list of primes that are both left and right truncatable."""
    prime_list = common.sieve_erathosthenes(1000000)

    left_extend_primes = next_left_extend_prime('3', prime_list)
    left_extend_primes.extend(next_left_extend_prime('7', prime_list))

    right_extend_primes = next_right_extend_prime('2', prime_list)
    right_extend_primes.extend(next_right_extend_prime('3', prime_list))
    right_extend_primes.extend(next_right_extend_prime('5', prime_list))
    right_extend_primes.extend(next_right_extend_prime('7', prime_list))

    left_extend_primes.sort()
    right_extend_primes.sort()
    trunc_primes = []
    for p in left_extend_primes[2:]:
        if p in right_extend_primes:
            trunc_primes.append(p)
    # print(left_extend_primes)
    # print(right_extend_primes)
    # print(trunc_primes)
    return trunc_primes


# Problem 38: Pandigital Multiples
# Take the number 192 and multiply it by each of 1, 2, and 3:
#     192 x 1 = 192
#     192 x 2 = 384
#     192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def pandigital_concatenated_multiples():
    result_list = []

    # 4-digit + 5-digit = 9-digit
    for n in range(9876, 5123, -1):
        str_sum = str(n) + str(n*2)
        if common.is_pandigital(str_sum, '123456789'):
            result_list.append((int(str_sum), int(n), int(n*2)))
            break       # return just the largest 4-digit set

    # 3-digit + 3-digit + 3-digit = 9-digit
    for n in range(329, 123, -1):
        str_sum = str(n) + str(n*2) + str(n*3)
        if common.is_pandigital(str_sum, '123456789'):
            result_list.append((int(str_sum), int(n), int(n*2), int(n*3)))
            break       # return just the largest 3-digit set

    # 1-digit + 2-digit + 2-digit + 2-digit + 2-digit = 9-digit
    for n in range(9, 5, -1):
        str_sum = str(n) + str(n*2) + str(n*3) + str(n*4) + str(n*5)
        if common.is_pandigital(str_sum, '123456789'):
            result_list.append((int(str_sum), int(n), int(n*2), int(n*3), int(n*4), int(n*5)))
            break       # return just the largest 1-digit set

    return result_list


# Problem 39: Integer Right Triangles
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p <= 1000, is the number of solutions maximised?

def integral_right_triangle_perimeters(max_p):
    max_n = int(max_p/2)
    squares = [n*n for n in range(max_n+1)]
    perimeters_list = []
    for a in range(1, max_n+1):
        for b in range(a, max_n+1):
            c = common.index_in_ordered_list(squares[a]+squares[b], squares)
            if c > 0:
                p = a + b + c
                if p > max_p:
                    break
                else:
                    perimeters_list.append(p)
    return perimeters_list


# Problem 30-39 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 39

    if problem_num == 30:
        print()
        zpwr = 4
        z = 1634
        print(zpwr, z, sum_of_digit_powers(z, zpwr))
        z = 8208
        print(zpwr, z, sum_of_digit_powers(z, zpwr))
        z = 9474
        print(zpwr, z, sum_of_digit_powers(z, zpwr))

        print()
        z = 9876543210
        for zpos in range(10):
            print(z, zpos, position_value(z, zpos))

        print()
        z = 9876543210
        for zpos in range(10):
            print(z, zpos, increment_position(z, zpos))

        print()
        print(set_next_digit(1630, 0, 4))
        print(set_next_digit(1600, 1, 4))
        print(set_next_digit(1000, 2, 4))

        print()
        print(perfect_digit_powers(4))
        print(perfect_digit_powers(5))
    elif problem_num == 31:
        print(coin_combinations(4, [2, 1], 1))
        print(coin_combinations(6, [3, 2], 2))
        print(coin_combinations(6, [3, 2, 1], 1))
        print(coin_combinations(200, [200, 100, 50, 20, 10, 5, 2, 1], 1))
        print(coin_combinations(1, [200, 100, 50, 20, 10, 5, 2, 1], 1))
    elif problem_num == 32:
        print(is_pandigital_3(39, 186, 39*186))
        print(pandigital_products())
        print(sum(pandigital_products()))
    elif problem_num == 33:
        print()
        zfraction_list = digit_canceling_fractions()
        num_product = 1
        den_product = 1
        for fraction in zfraction_list:
            num_product *= fraction[0]
            den_product *= fraction[1]
        print(zfraction_list)
        print(common.reduce_fraction(num_product, den_product))
    elif problem_num == 34:
        print()
        print(factorial_sum_list(200))
        print(factorial_sum_list())
    elif problem_num == 35:
        print(circular_primes(100))
        print(len(circular_primes(1000000)))
    elif problem_num == 36:
        print(double_base_palindromes(1000))
        print(double_base_palindromes(1000000))
    elif problem_num == 37:
        prime_list_10M = common.sieve_erathosthenes(10000000)
        print(next_right_extend_prime('379', prime_list_10M))
        print(next_left_extend_prime('797', prime_list_10M))
        print(truncatable_primes())
    elif problem_num == 38:
        print(pandigital_concatenated_multiples())
    elif problem_num == 39:
        print()
        p_list = integral_right_triangle_perimeters(100)
        p_list.sort()
        print(p_list)
        p_list = integral_right_triangle_perimeters(1000)
        max_count = 0
        max_count_p = 0
        for zprime in p_list:
            zcount = p_list.count(zprime)
            if max_count < zcount:
                max_count = zcount
                max_count_p = zprime
        print(max_count_p, max_count)
