""" Project Euler Problems 20-29
"""


import math
import common

from timeit import default_timer as timer


# Problem 20:  Factorial digit sum

# n! means n x (n - 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def sum_digits(num):
    return sum([int(i) for i in str(num)])



# Problem 1-9 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 20

    if problem_num == 20:
        print(sum_digits(math.factorial(10)))
        print(sum_digits(math.factorial(100)))
