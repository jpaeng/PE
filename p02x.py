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


# Problem 22:  Name Scores
# Using p022_names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# Begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?


def alpha_value(name):
    """ Return the alphabetical value of name calculated from the value of each character in name."""
    total = 0
    for char in name.upper():
        total += ord(char)-64
    return total


def alpha_list_score(text_list):
    """Return the score of an list of names which is the sum of (alpha value of each name x its alphabetical position"""
    text_list.sort()
    score_total = 0
    for (index, name) in enumerate(text_list):
        score_total += (index+1)*alpha_value(name)
    return score_total




# Problem 20-29 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 22

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
    elif problem_num == 22:
        print()
        p022_name = 'Alex'
        print(p022_name, alpha_value(p022_name))
        p022_name = 'Colin'
        print(p022_name, alpha_value(p022_name))
        p022_name = 'Jock'
        print(p022_name, alpha_value(p022_name))
        file_ptr = open('p022_names.txt')
        p022_names_list = (file_ptr.read().replace('"', '')).split(',')
        file_ptr.close()
        print(alpha_list_score(p022_names_list))
