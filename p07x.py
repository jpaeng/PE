""" Project Euler Problems 70-79
"""


import math
import string
import common

from timeit import default_timer as timer


# 70. Totient permutation
# Euler's Totient function, f(n) [sometimes called the phi function], is used to determine the number of
# positive numbers less than or equal to n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, f(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so f(1)=1.
# Interestingly, f(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
# Find the value of n, 1 < n < 10**7, for which f(n) is a permutation of n and the ratio n/f(n) produces a minimum.
# Considerations:
#   1. n/phi(n) > 1.0 for all n > 1
#   2. n/phi(n) decreases for prime n as n gets larger
#   3. n/phi(n) is minimum for the largest prime in any given range.
#   4. n and phi(n) cannot be permutations of each other because phi(n) = n-1 for primes.  n and n-1 are never
#       permutations of each other.
#   5. Try numbers that are composites of two primes.

def minimum_totient_ratio_permuation(max_n):
    """Return number n < max_n with minimum n/phi(n) ratio where n and phi(n) are permutations of each other.
    Euler's product formula:
        n = (p1**k1) * (p2**k2) * ...
        phi(n)  = n * (1 - 1/p1) * (1 - 1/p2) * ...
                = n * (p1 - 1)/p1 * (p2 -1)/p2 * ...
        n/phi(n) = (p1*p2*...)/((p1-1)*(p2-1)*...) -> increases as more prime are added.
        where p1, p2, ... are primes.

    :param max_n:   maximum n to check
    :return:        n with the minimum n/phi(n) ratio in the form:  (n, phi(n), n/phi(n))
    """

    prime_list = common.prime_list_mr(2, (max_n+1)//2)
    
    # Find index of prime closest to sqrt(max_n)
    sqrt_max_n = math.sqrt(max_n)
    a = int(sqrt_max_n)
    while True:
        if a in prime_list:
            break
        else:
            a -= 1
    index_mid = prime_list.index(a)
    min_ratio = (0, 0, 0, 0, 10.0)

    # a loops down from sqrt(max_n), b loops up from sqrt(max_n)
    for index_a in reversed(range(index_mid//2, index_mid)):
        for index_b in range(index_mid, len(prime_list)):
            a = prime_list[index_a]
            b = prime_list[index_b]
            prod = a * b
            if prod > max_n:
                break
            else:
                ratio = a*b/((a-1)*(b-1))
                f = int(0.5 + prod/ratio)
                if common.is_permutation(str(prod), str(f)):
                    # print(a, b, prod, f, ratio)
                    if ratio < min_ratio[-1]:
                        min_ratio = (a, b, prod, f, ratio)
                    break

    return min_ratio


# 71. Ordered fractions
# Consider the fraction, n/d, where n and d are positive integers.
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#     1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
# By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size,
# find the numerator of the fraction immediately to the left of 3/7.

# 72. Counting fractions
# Consider the fraction, n/d, where n and d are positive integers.
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#     1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 21 elements in this set.
# How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?

# 73. Counting fractions in a range
# Consider the fraction, n/d, where n and d are positive integers.
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#     1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 3 fractions between 1/3 and 1/2.
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?

# 74. Digit factorial chains
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#     1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
# it turns out that there are only three such loops that exist:
#     169 -> 363601 -> 1454 -> 169
#     871 -> 45361 -> 871
#     872 -> 45362 -> 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#     69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
#     78 -> 45360 -> 871 -> 45361 (-> 871)
#     540 -> 145 (-> 145)
# Starting with 69 produces a chain of five non-repeating terms,
# but the longest non-repeating chain with a starting number below one million is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

# 75. Singular integer right triangles
# It turns out that 12 cm is the smallest length of wire that can be bent to form an
# integer sided right angle triangle in exactly one way, but there are many more examples.
#     12 cm: (3,4,5)
#     24 cm: (6,8,10)
#     30 cm: (5,12,13)
#     36 cm: (9,12,15)
#     40 cm: (8,15,17)
#     48 cm: (12,16,20)
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
# and other lengths allow more than one solution to be found;
# for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
#     120 cm: (30,40,50), (20,48,52), (24,45,51)
# Given that L is the length of the wire,
# for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?

# 76. Counting summations
# It is possible to write five as a sum in exactly six different ways:
#     4 + 1
#     3 + 2
#     3 + 1 + 1
#     2 + 2 + 1
#     2 + 1 + 1 + 1
#     1 + 1 + 1 + 1 + 1
# How many different ways can one hundred be written as a sum of at least two positive integers?

# 77. Prime summations
# It is possible to write ten as the sum of primes in exactly five different ways:
#     7 + 3
#     5 + 5
#     5 + 3 + 2
#     3 + 3 + 2 + 2
#     2 + 2 + 2 + 2 + 2
# What is the first value which can be written as the sum of primes in over five thousand different ways?

# 78. Coin partitions
# Let p(n) represent the number of different ways in which n coins can be separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
#     OOOOO
#     OOOO   O
#     OOO   OO
#     OOO   O   O
#     OO   OO   O
#     OO   O   O   O
#     O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.

# 79. Passcode derivation
# A common security method used for online banking is to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
# the expected reply would be: 317.
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order,
# analyse the file so as to determine the shortest possible secret passcode of unknown length.


# Problem 70-79 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 70

    if problem_num == 70:
        print('minimum_totient_ratio_permuation(10**5) =', minimum_totient_ratio_permuation(10**5))
        # print('minimum_totient_ratio_permuation(10**7) = ', minimum_totient_ratio_permuation(10**7))
    elif problem_num == 71:
        print()
    elif problem_num == 72:
        print()
    elif problem_num == 73:
        print()
    elif problem_num == 74:
        print()
    elif problem_num == 75:
        print()
    elif problem_num == 76:
        print()
    elif problem_num == 77:
        print()
    elif problem_num == 78:
        print()
    elif problem_num == 79:
        print()
