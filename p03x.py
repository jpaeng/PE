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



# Problem 30-39 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 31

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
