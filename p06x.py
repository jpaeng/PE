""" Project Euler Problems 60-69
"""


import math
import string
import common

from timeit import default_timer as timer


# 60 Prime pair sets
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
# the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


# 61 Cyclical figurate numbers
# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers
# and are generated by the following formulae:
#     Triangle	 	P3,n=n(n+1)/2       1, 3, 6, 10, 15, ...
#     Square	 	P4,n=n2             1, 4, 9, 16, 25, ...
#     Pentagonal	P5,n=n(3n-1)/2      1, 5, 12, 22, 35, ...
#     Hexagonal	 	P6,n=n(2n-1)        1, 6, 15, 28, 45, ...
#     Heptagonal	P7,n=n(5n-3)/2      1, 7, 18, 34, 55, ...
#     Octagonal	 	P8,n=n(3n-2)        1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.
# The set is cyclic, in that the last two digits of each number is the first two digits of the next number
# (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882),
# is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
# triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.


# 62 Cubic permutations
# The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.


# 63 Powerful digit counts
# The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?


# 64 Odd period square roots
# All square roots are periodic when written as continued fractions and can be written in the form:
#     (see page)
# It can be seen that the sequence is repeating. For conciseness, we use the notation v23 = [4;(1,3,1,8)],
# to indicate that the block (1,3,1,8) repeats indefinitely.
# The first ten continued fraction representations of (irrational) square roots are:
#     v2=[1;(2)], period=1
#     v3=[1;(1,2)], period=2
#     v5=[2;(4)], period=1
#     v6=[2;(2,4)], period=2
#     v7=[2;(1,1,1,4)], period=4
#     v8=[2;(1,4)], period=2
#     v10=[3;(6)], period=1
#     v11=[3;(3,6)], period=2
#     v12= [3;(2,6)], period=2
#     v13=[3;(1,1,1,1,6)], period=5
# Exactly four continued fractions, for N = 13, have an odd period.
# How many continued fractions for N = 10000 have an odd period?


# 65 Convergents of e
# The square root of 2 can be written as an infinite continued fraction.
# The infinite continued fraction can be written, v2 = [1;(2)], (2) indicates that 2 repeats ad infinitum.
# In a similar way, v23 = [4;(1,3,1,8)].
#     (see page)
# Hence the sequence of the first ten convergents for v2 are:
#     1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
# What is most surprising is that the important mathematical constant,
#     e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# The first ten terms in the sequence of convergents for e are:
#     2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.


# 66 Diophantine equation
# Consider quadratic Diophantine equations of the form:
#         x**2 - Dy**2 = 1
# For example, when D=13, the minimal solution in x is 649**2 - 13x180**2 = 1.
# It can be assumed that there are no solutions in positive integers when D is square.
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#     3**2 - 2x2**2 = 1
#     2**2 - 3x1**2 = 1
#     9**2 - 5x4**2 = 1
#     5**2 - 6x2**2 = 1
#     8**2 - 7x3**2 = 1
# Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.
# Find the value of D = 1000 in minimal solutions of x for which the largest value of x is obtained.


# 67 Maximum path sum II
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 23.
#         3
#        7 4
#       2 4 6
#      8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.
# NOTE: This is a much more difficult version of Problem 18.
#     It is not possible to try every route to solve this problem, as there are 2**99 altogether!
#     If you could check one trillion (10**12) routes every second it would take over twenty billion years to check them all.
#     There is an efficient algorithm to solve it. ;o)


# 68 Magic 5-gon ring
# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
#     (see page)
# Working clockwise, and starting from the group of three with the numerically lowest external node
# (4,3,2 in this example), each solution can be described uniquely.
# For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12.
# There are eight solutions in total.
#     Total	Solution Set
#     9     4,2,3; 5,3,1; 6,1,2
#     9     4,3,2; 6,2,1; 5,1,3
#     10    2,3,5; 4,5,1; 6,1,3
#     10    2,5,3; 6,3,1; 4,1,5
#     11    1,4,6; 3,6,2; 5,2,4
#     11    1,6,4; 5,4,2; 3,2,6
#     12    1,5,6; 2,6,4; 3,4,5
#     12    1,6,5; 3,5,4; 2,4,6
# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
# What is the maximum 16-digit string for a "magic" 5-gon ring?


# 69 Totient maximum
# Euler's Totient function, f(n) [sometimes called the phi function], is used to determine the number of numbers
# less than n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, f(9)=6.
#     n	Relatively Prime	f(n)	n/f(n)
#     2	1	1	2
#     3	1,2	2	1.5
#     4	1,3	2	2
#     5	1,2,3,4	4	1.25
#     6	1,5	2	3
#     7	1,2,3,4,5,6	6	1.1666...
#     8	1,3,5,7	4	2
#     9	1,2,4,5,7,8	6	1.5
#     10	1,3,7,9	4	2.5
# It can be seen that n=6 produces a maximum n/f(n) for n <= 10.
# Find the value of n <= 1,000,000 for which n/f(n) is a maximum.
