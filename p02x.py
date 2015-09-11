""" Project Euler Problems 20-29
"""


import math
import string
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
    """ Return the list of amicable numbers up to max_n."""
    am_list = []
    for n in range(2, max_n+1):
        divisor_sum = sum(common.get_proper_divisors(n))
        if divisor_sum > n:
            if n == sum(common.get_proper_divisors(divisor_sum)):
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
    """ Return the score of an list of names which is the sum of (alpha value of each name x its alphabetical position"""
    text_list.sort()
    score_total = 0
    for (index, name) in enumerate(text_list):
        score_total += (index+1)*alpha_value(name)
    return score_total


# Problem 23:  Non-Abundant Sums
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
#     which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n
#     and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
#     the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123
#     can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though
#     it is known that the greatest number that cannot be expressed as
#     the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def abundant_list(max_n):
    """ Return list of abundant numbers up to max_n."""
    alist = [n for n in range(2, max_n+1) if n < sum(common.get_proper_divisors(n))]
    return alist


def is_abundant_sum(xsum, abund_list):
    """ Return True or False whether num is the sum of abundant numbers."""
    if xsum < 24:
        return False
    else:
        index = 0
        complement = xsum - abund_list[index]
        while complement >= abund_list[index]:
            if complement in abund_list:
                return True
            else:
                index += 1
                complement = xsum - abund_list[index]
        return False


def abundant_sum_list(max_sum):
    """ Return list of all numbers up to max_n that can be expressed as the sum of two abundant numbers."""
    abund_list = abundant_list(max_sum)
    ab_sum_list = [xsum for xsum in range(24, max_sum+1) if is_abundant_sum(xsum, abund_list)]
    return ab_sum_list


def non_abundant_sum_list(max_sum):
    """ Return list of all numbers up to max_n that cannot be expressed as the sum of two abundant numbers."""
    abund_list = abundant_list(max_sum)
    # ab_sum_list = [xsum for xsum in range(2, max_sum-11) if not is_abundant_sum(xsum, abund_list)]
    ab_sum_list = [xsum for xsum in range(2, max_sum+1) if not is_abundant_sum(xsum, abund_list)]
    ab_sum_list.insert(0, 1)
    return ab_sum_list


# Problem 24:  Lexicographic Permutations
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#         012   021   102   120   201   210
# The lexicographic permutations of 0, 1, 2 and 3 are:
    # 0123
    # 0132
    # 0213
    # 0231
    # 0312
    # 0321

    # 1023
    # 1032
    # 1203
    # 1230
    # 1302
    # 1320

    # 2013
    # 2031
    # 2103
    # 2130
    # 2301
    # 2310

    # 3012
    # 3021
    # 3102
    # 3120
    # 3201
    # 3210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def lexi_perm(n, digit_count):
    """ Return the nth permutation of digit_count digits."""
    digits = (string.digits + string.ascii_lowercase)[:digit_count]
    result = ''
    remainder = n
    for position in range(digit_count-1, -1, -1):       # Start with msb and loop to lsb
        divisor = math.factorial(position)              # Factorials:  1 2 6 24 120 ...
        dividend = int(remainder/divisor)               # Determine which digit in list is next
        remainder = remainder % divisor                 # Remainder calculated for next loop
        result += digits[dividend]                      # Extend string to right
        digits = digits.replace(digits[dividend], '')   # Remove digit just used from list
    return result


# Problem 25:  1000-digit Fibonacci number
# The Fibonacci sequence is defined by the recurrence relation:
#     Fn = F(n-1) + F(n-2), where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacci_greater_than(min_n):
    fn = 1
    fn_1 = 1
    n = 2

    while fn < min_n:
        fn, fn_1 = fn + fn_1, fn
        n += 1

    return n, fn


# Problem 26:  Reciprocal Cycles
# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions with denominators 2 to 10 are given:
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def recurring_cycle(n):
    """ Return the length of the recurring cycle in 1/n.  Return 0 if no recurring cycle."""
    remainders = []
    remainder = 10
    while True:
        if remainder < n:
            remainder *= 10
        remainder = remainder % n
        if remainder == 0:
            return 0
        elif remainder in remainders:
            return len(remainders[remainders.index(remainder):])
        else:
            remainders.append(remainder)


# Problem 20-29 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 26

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
    elif problem_num == 23:
        z_abund_list = abundant_list(100)
        print()
        print(z_abund_list)
        print(abundant_sum_list(40))
        print(non_abundant_sum_list(40))
        print('Sum of all non-abundant numbers below 40:', sum(non_abundant_sum_list(40)))
        # print('Sum of all non-abundant numbers below 28123:', sum(non_abundant_sum_list(28123)))
        z_abund_list = abundant_list(10000)
        print('Odd abundant numbers below 10000: ', [z for z in z_abund_list if z % 2])
    elif problem_num == 24:
        print()
        pr24_bit_count = 4
        for z in range(math.factorial(pr24_bit_count)):
            print(z, lexi_perm(z, pr24_bit_count))
        print(999999, lexi_perm(999999, 10))
    elif problem_num == 25:
        print()
        for z in range(1, 5):
            print(fibonacci_greater_than(10**z))
        print(fibonacci_greater_than(10**999)[0])
    elif problem_num == 26:
        print()
        for z in range(1, 11):
            print(z, recurring_cycle(z))
        zlongest = 0
        zlongest_z = 1
        for z in range(1, 1000):
            zcycle_length = recurring_cycle(z)
            if zlongest < zcycle_length:
                zlongest = zcycle_length
                zlongest_z = z
        print(zlongest_z, zlongest)