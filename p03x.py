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

def is_pandigital(a, b, c):
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
            if is_pandigital(a, b, c):
                if c not in pandigital_c_list:
                    pandigital_c_list.append(c)

    # For 2-digit a, 3-digit b, and 4-digit c
    for a in range(12, 99):  # loop through 2-digit a
        b = 122             # min b = 123
        c = a * b
        while c < 9876:     # max c = 9876
            b += 1
            c = a * b
            if is_pandigital(a, b, c):
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





# Problem 30-39 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 33

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
        print(is_pandigital(39, 186, 39*186))
        print(pandigital_products())
        print(sum(pandigital_products()))
    elif problem_num == 33:
        print()
        fraction_list = digit_canceling_fractions()
        num_product = 1
        den_product = 1
        for fraction in fraction_list:
            num_product *= fraction[0]
            den_product *= fraction[1]
        print(fraction_list)
        print(common.reduce_fraction(num_product, den_product))
