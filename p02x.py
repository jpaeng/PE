""" Project Euler Problems 20-29
"""


import math
import common

from timeit import default_timer as timer


# Problem 20:  Factorial Digit Sum
# n! means n x (n - 1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

def sum_digits(num):
    """ Return the sum of the digits in num."""
    return sum([int(i) for i in str(num)])


# Problem 21:  Amicable Numbers
# Let d(n) be defined as the sum of proper divisors of n
#     (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b,
#     then a and b are an amicable pair
#     and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
#     therefore d(220) = 284.
#     The proper divisors of 284 are 1, 2, 4, 71 and 142;
#     so d(284) = 220.
# Note:  Proper Divisors of a number are the same as the Factors of the number except the number itself is not included.
# Evaluate the sum of all the amicable numbers under 10000.

def amicable_list(max_n):
    """Return the list of amicable numbers up to max_n."""
    am_list = []
    for n in range(2, max_n+1):
        divisor_sum = sum(common.get_factors(n)) - n
        if divisor_sum > n:
            if n == sum(common.get_factors(divisor_sum)) - divisor_sum:
                am_list.append(n)
                am_list.append(divisor_sum)
    return am_list


# Problem 1-9 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 21

    if problem_num == 20:
        print()
        print(sum_digits(math.factorial(10)))
        print(sum_digits(math.factorial(100)))
    elif problem_num == 21:
        print()
        pr21_list = amicable_list(1000)
        print(sum(pr21_list), pr21_list)
        pr21_list = amicable_list(10000)
        print(sum(pr21_list), pr21_list)
