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

def check_prime_concatenations(prime1, prime2, prime_list):
    str_prime1 = str(prime1)
    str_prime2 = str(prime2)

    status = True
    prime_cat = int(str_prime1 + str_prime2)
    if not common.is_in_ordered_list(prime_cat, prime_list):
        status = False

    prime_cat = int(str_prime2 + str_prime1)
    if not common.is_in_ordered_list(prime_cat, prime_list):
        status = False

    return status


def check_prime_pairs(index, prime_set, prime_list):
    status = True
    for prime in prime_set:
        if not check_prime_concatenations(prime, prime_list[index], prime_list):
            status = False
    return status


def min_prime_pair_set(prime_count):
    if prime_count < 5:
        prime_list = common.sieve_erathosthenes2(10**(2*prime_count))
        min_prime_sum = 10**prime_count
    else:
        prime_list = common.sieve_erathosthenes2(10**8)
        min_prime_sum = 10**8

    min_prime_set = []

    prime_index = 1     # No pair with 2 will work
    while prime_list[prime_index] < min_prime_sum//prime_count:
        prime_set = [prime_list[prime_index]]
        prime_sum = prime_set[0]
        next_prime_index = prime_index + 1
        while prime_list[next_prime_index]+prime_sum < min_prime_sum:
            if check_prime_pairs(next_prime_index, prime_set, prime_list):
                prime_set.append(prime_list[next_prime_index])
                prime_sum = sum(prime_set)
                if len(prime_set) >= 4:
                    print('    ', len(prime_set), prime_set)
                if prime_sum > min_prime_sum:
                    break
                if len(prime_set) == prime_count:
                    if prime_sum < min_prime_sum:
                        min_prime_set = prime_set[:]
                        min_prime_sum = prime_sum
                    break
            next_prime_index += 1
        prime_index += 1

    return min_prime_set, min_prime_sum


def check_prime_concatenations_mr(prime1, prime2):
    str_prime1 = str(prime1)
    str_prime2 = str(prime2)

    status = True
    prime_cat = int(str_prime1 + str_prime2)
    if not common.is_prime_mr(prime_cat):
        status = False

    prime_cat = int(str_prime2 + str_prime1)
    if not common.is_prime_mr(prime_cat):
        status = False

    return status


def check_prime_pairs_mr(prime1, prime_set):
    status = True
    for prime2 in prime_set:
        if not check_prime_concatenations_mr(prime1, prime2):
            status = False
    return status


def min_prime_pair_set_mr(prime_count):
    if prime_count < 5:
        prime_list = common.sieve_erathosthenes2(10**prime_count)
        min_prime_sum = 10**prime_count
    else:
        prime_list = common.sieve_erathosthenes2(10**6)
        min_prime_sum = 10**9
    prime_list_count = len(prime_list)

    min_prime_set = []

    prime_index = 1     # No pair with 2 will work
    while prime_list[prime_index] < min_prime_sum//prime_count:
        prime_set = [prime_list[prime_index]]
        prime_sum = prime_set[0]
        next_prime_index = prime_index + 1
        while prime_list[next_prime_index]+prime_sum < min_prime_sum:
            if check_prime_pairs_mr(prime_list[next_prime_index], prime_set):
                prime_set.append(prime_list[next_prime_index])
                prime_sum = sum(prime_set)
                if len(prime_set) >= 4:
                    print('    ', len(prime_set), prime_set)
                if prime_sum > min_prime_sum:
                    break
                if len(prime_set) == prime_count:
                    if prime_sum < min_prime_sum:
                        min_prime_set = prime_set[:]
                        min_prime_sum = prime_sum
                    break
            next_prime_index += 1
            if next_prime_index == prime_list_count:
                break
        prime_index += 1
        if prime_index == prime_list_count:
            break

    return min_prime_set, min_prime_sum


# 61 Cyclical figurate numbers
# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers
# and are generated by the following formulae:
#     Triangle	 	P3,n=n(n+1)/2       1, 3, 6, 10, 15, ...
#     Square	 	P4,n=n**2           1, 4, 9, 16, 25, ...
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

def generate_polygonal_number_list(side_count, digit_count):
    """
    Create a list of all polygonal numbers of digit_count length of a particular side_count.
    :param side_count:  polygonal side count, e.g. Triangle side_count = 3, Square side_count = 4, etc.
    :param digit_count: number of digits in the numbers
    :return:            list of all polygonal numbers of the specified side_count with the specified digit_count
    """

    # Trying out lambda functions
    # formula = side_count formula
    # f_index = formula to determine the indices of the numbers of the specified digit_count
    if side_count == 3:
        formula = lambda x: x*(x+1)//2
        f_index = lambda x: 1+int((math.sqrt(8*x)-1)/2)     # sqrt(8*x+1)-1)/2
    elif side_count == 4:
        formula = lambda x: x*x
        f_index = lambda x: 1+int(math.sqrt(x-1))           # sqrt(x)
    elif side_count == 5:
        formula = lambda x: x*(3*x-1)//2
        f_index = lambda x: 1+int((math.sqrt(24*x)+1)/6)    # (sqrt(24*x+1)+1)/6
    elif side_count == 6:
        formula = lambda x: x*(2*x-1)
        f_index = lambda x: 1+int((math.sqrt(8*x)+1)/4)     # (sqrt(8*x+1)+1)/4
    elif side_count == 7:
        formula = lambda x: x*(5*x-3)//2
        f_index = lambda x: 1+int((math.sqrt(40*x+8)+3)/10) # (sqrt(40*x+9)+3)/10
    elif side_count == 8:
        formula = lambda x: x*(3*x-2)
        f_index = lambda x: 1+int((math.sqrt(3*x)+1)/3)     # (sqrt(3*x+1)+1)/3
    else:
        formula = lambda x: 0
        f_index = lambda x: 0

    start_index = f_index(10**(digit_count-1))
    stop_index  = f_index(10**(digit_count))

    number_list = [formula(i) for i in range(start_index, stop_index)]

    return number_list


def cyclic_4digit_set(set_count):
    """
    Find set of set_count 4-digit numbers, each a different polygonal type that form a cyclic set.
    :param set_count:   the count of numbers forming th cyclic set
    :return:            a list of tuples of the form (side_count, number) that form the cyclic set.
    """

    # Generate the polygonal lists for triangle...octagonal numbers
    polygonal_numbers = []
    for index in range(6):
        side_count = index + 3
        polygonal_numbers.append(PrefixSuffixNumbersClass(side_count, generate_polygonal_number_list(side_count, 4)))

    # Delete numbers that have single digit suffixes
    for index in range(6):
        for num, prefix, suffix in reversed(polygonal_numbers[index]):
            if suffix < 10:
                polygonal_numbers[index].delete_number(num)

    # Cyclic sets require suffixes to be matched to prefixes.
    # Delete numbers that have prefixes that have no matching suffix on a different polygonal type
    # Delete numbers that have suffixes that have no matching prefix on a different polygonal type
    deleted = True
    while deleted:
        deleted = False
        for index in range(6):
            other_indices = [i for i in range(6)]
            other_indices.remove(index)
            for num, prefix, suffix in reversed(polygonal_numbers[index]):
                prefix_total = 0
                suffix_total = 0
                for index2 in other_indices:
                    prefix_count, suffix_count = polygonal_numbers[index2].prefix_suffix_counts(prefix)
                    suffix_total += suffix_count
                    prefix_count, suffix_count = polygonal_numbers[index2].prefix_suffix_counts(suffix)
                    prefix_total += prefix_count
                if (prefix_total == 0) or (suffix_total == 0):
                    deleted = True
                    polygonal_numbers[index].delete_number(num)

    # Find cyclic sets
    cyclic_set = []
    for num, prefix, suffix in polygonal_numbers[-1]:
        side_list = polygonal_numbers[:-1]
        set_list = [(8, num)]   # start with octagonal number because there are the fewest octagonal 4-digit numbers
                                # then find chains going forward and backward from that number.
        prefix_suffix_list = add_node_prefix_suffix(4, side_list, suffix, set_list) # find 4-number prefix-suffix chains
        suffix_prefix_list = add_node_suffix_prefix(4, side_list, prefix, set_list) # find 4-number suffix-prefix chains
        # look for matches between last number of forward list and last number of backward list in order to make cyclic
        for chain_prefix_suffix in prefix_suffix_list:
            for chain_suffix_prefix in suffix_prefix_list:
                if chain_prefix_suffix[-1] == chain_suffix_prefix[-1]:
                    # check that each number represents a different polygonal type
                    sides = []
                    for node in chain_prefix_suffix:
                        sides.append(node[0])
                    for node in chain_suffix_prefix[1:-1]:
                        if node[0] not in sides:
                            sides.append(node[0])
                    if len(sides) > 5:
                        cyclic_set.append(chain_prefix_suffix[:] + list(reversed(chain_suffix_prefix[1:-1])))

    return cyclic_set


def add_node_prefix_suffix(remaining_count, remaining_side_list, pref, set_list):
    """
    Recursive function to find prefix-suffix chains of set length with each number of a different polygonal type.
    :param remaining_count:     count of numbers remaining to be found
    :param remaining_side_list: list of polygonal types not yet used and still available
    :param pref:                prefix to be found
    :param set_list:            list of numbers already in chain
    :return:                    list of chains from initial number in set_list
    """

    remaining_count -= 1
    return_list = []
    if remaining_count > 0:
        for index in range(len(remaining_side_list)):
            side_list = remaining_side_list[:index] + remaining_side_list[index+1:]
            for num, prefix, suffix in remaining_side_list[index]:
                if prefix == pref:     # number[2] == suffix
                    return_list.extend(add_node_prefix_suffix(remaining_count, side_list, suffix, set_list+[(remaining_side_list[index].get_side_count(), num)]))
    else:
        if len(set_list) < 2:
            return_list = []
        else:
            return_list = [set_list]

    return return_list


def add_node_suffix_prefix(remaining_count, remaining_side_list, suff, set_list):
    """Recursive function to find suffix-prefix chains of set length with each number of a different polygonal type.

    :param remaining_count:     count of numbers remaining to be found
    :param remaining_side_list: list of polygonal types not yet used and still available
    :param suff:                suffix to be found
    :param set_list:            list of numbers already in chain
    :return:                    list of chains from initial number in set_list
    """

    remaining_count -= 1
    return_list = []
    if remaining_count > 0:
        for index in range(len(remaining_side_list)):
            side_list = remaining_side_list[:index] + remaining_side_list[index+1:]
            for num, prefix, suffix in remaining_side_list[index]:
                if suffix == suff:     # number[2] == suffix
                    return_list.extend(add_node_suffix_prefix(remaining_count, side_list, prefix,
                                                      set_list+[(remaining_side_list[index].get_side_count(), num)]))
    else:
        if len(set_list) < 2:
            return_list = []
        else:
            return_list = [set_list]

    return return_list


class PrefixSuffixNumbersClass:
    """Packages 4-digit numbers with their 2-digit prefixes and suffixes to simplify parameters

    Keeps track of the polygonal side count, and length of list.
    """

    def __init__(self, side_count, numberlist):
        self.side_count = side_count
        self.len = len(numberlist)
        self.numberlist = [(numberlist[i], int(str(numberlist[i])[:2]), int(str(numberlist[i])[2:])) for i in range(self.len)]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.len:
            self.index += 1
            return self.numberlist[self.index-1]
        else:
            raise StopIteration

    def __reversed__(self):
        return reversed(self.numberlist)

    def __len__(self):
        return self.len

    def get_side_count(self):
        return self.side_count

    def delete_number(self, number):
        for node in self.numberlist:
            if node[0] == number:
                self.numberlist.remove(node)
                break
        self.len = len(self.numberlist)

    def prefix_suffix_counts(self, target):
        prefix_count = 0
        suffix_count = 0
        for number, prefix, suffix in self.numberlist:
            if prefix == target:
                prefix_count += 1
            if suffix == target:
                suffix_count += 1
        return prefix_count, suffix_count


# 62 Cubic permutations
# The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.

def cube_permutations(perm_count):
    """Return the smallest set of perm_count cubes that are permutations of each other.

    :param perm_count:  the number of cube permutations to look for
    :return:            list of cube permutations of the first cube that has at least perm_count permutations
    """

    found = False
    perm_list = []
    max_digit_count = 14
    stop_base = 3
    for digit_count in range(2, max_digit_count+1):
        # first create list of cubes of the same length
        start_base = stop_base
        stop_base = int(math.pow(10**digit_count, 0.3333333333)) + 1
        cube_list = [base**3 for base in range(start_base, stop_base)]
        for cube in cube_list:
            count = 0
            perm_list = []
            # count the number of permutations of cube
            for cube2 in cube_list:
                if common.is_permutation(str(cube), str(cube2)):
                    perm_list.append(cube2)
                    count += 1
                    if count >= perm_count:
                        found = True
                        break
            if found:
                break
        if found:
            break

    if len(perm_list) >= perm_count:
        return perm_list
    else:
        return []

# 63 Powerful digit counts
# The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?


def power_digit_counts():
    count = 0
    power = 1
    while math.log10(9**power)+1 >= power:      # log10(n)+1 gives the number of digits in n in base 10.
        for base in range(1, 10):
            if int(math.log10(base**power))+1 == power:
                count += 1
        power += 1
    return count


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
# Exactly four continued fractions, for N <= 13, have an odd period.
# How many continued fractions for N <= 10000 have an odd period?

def continued_fraction_coeffs(number):
    """Return list of continuing fraction coefficients.  ROUNDING ERRORS BEYOND SOME UNKNOWN NUMBER OF TERMS

    :param number: Starting number for
    :return:
    """

    max_loop = 100
    resolution = 10**6

    repeating_sequence = []
    non_repeating_sequence = [int(number)]
    if int(number*resolution) != non_repeating_sequence[0]*resolution:
        remainder_list = [1.0/(number - non_repeating_sequence[0])]
        index = 0
        while len(repeating_sequence)==0 and (index < max_loop):
            index += 1
            non_repeating_sequence.append(int(remainder_list[-1]))
            remainder = (remainder_list[-1] - non_repeating_sequence[-1])
            remainder_list.append(1.0/remainder)
            remainder_int = int(remainder_list[-1]*resolution)
            for index2 in range(index):
                if int(remainder_list[index2]*resolution) == remainder_int:
                    repeating_sequence = non_repeating_sequence[index2+1:]
                    non_repeating_sequence = non_repeating_sequence[:index2+1]
                    break
        non_repeating_sequence.append(tuple(repeating_sequence))
    return non_repeating_sequence


def sqrt_continued_fraction_coeffs(number, max_term = 1000):
    """Return list of continuing fraction coefficients for sqrt of number.  NO ROUNDING ERRORS.

    For each term the following variables are calculated:
            a(n) = int(1/a(n-1)_remainder)
            a(n)_remainder      = fractional part of a(n)
            1/(a(n)_remainder   = (sqrt(number)+b)/d
                                = a(n+1) + (sqrt(number)+c)/d
    :param number:      number for which sqrt(number) to be analyzed
    :param max_term:    maximum count of terms to be returned
    :return:            list of coefficients to be returned in the form
                                [a0, (a1, a2, a3)]
                        where a0 is non-repeating
                        and (a1, a2, a3) are repeating
    """

    resolution = 10**6
    sqrt_num = math.sqrt(number)

    repeating_sequence = []
    non_repeating_sequence = [int(sqrt_num)]
    if int(sqrt_num*resolution) != int(sqrt_num)*resolution:    # check for perfect squares
        loop_input = sqrt_num
        a = int(loop_input)
        remainder = loop_input-a
        remainder_p1 = 1/remainder          # remainder of a(n+1)
        remainder_p1 -= int(remainder_p1)   # just take fractional portion
        b = a
        d = number-(a*a)
        c = int(sqrt_num - d*(remainder_p1) + 0.1)  # round this number, not just int
        c_d_list = [(c, d)]
        index = 0
        while len(repeating_sequence)==0 and (index < max_term):
            index += 1
            loop_input = (sqrt_num + b) / d
            a = int(loop_input)
            non_repeating_sequence.append(a)
            remainder = loop_input-a
            remainder_p1 = 1/remainder          # remainder of a(n+1)
            remainder_p1 -= int(remainder_p1)   # just take fractional portion
            b = c
            d = (number-(c*c))//d
            c = int(sqrt_num - d*(remainder_p1) + 0.1)  # round this number, not just int
            c_d_list.append((c, d))
            for index2 in range(index):
                if c_d_list[index2] == c_d_list[index]:
                    repeating_sequence = non_repeating_sequence[index2+1:]
                    non_repeating_sequence = non_repeating_sequence[:index2+1]
                    break
        non_repeating_sequence.append(tuple(repeating_sequence))
    return non_repeating_sequence


def continued_fractions_term_counts(coeff_list):
    """

    :param coeff_list:
    :return:
    """

    if isinstance(coeff_list[-1], tuple):
        nonrepeating_count = len(coeff_list) - 1
        repeating_count = len(coeff_list[-1])
        if (repeating_count % 2) == 0:
            odd_periodic = False
        else:
            odd_periodic = True
    else:
        nonrepeating_count = len(coeff_list)
        repeating_count = 0
        odd_periodic = False

    return odd_periodic, nonrepeating_count, repeating_count


def continued_fractions_term_stats(function, start_n, max_n):
    """

    :param function:
    :param start_n:
    :param max_n:
    :return:
    """

    one_nonrepeating_count = 0
    zero_repeating_count = 0
    zero_nonrepeating_count = 0
    odd_periodic_count = 0
    even_periodic_count = 0

    for n in range(start_n, max_n+1):
        coeff_list = function(n)
        odd_periodic, nonrepeating_count, repeating_count = continued_fractions_term_counts(coeff_list)

        if nonrepeating_count == 1 and repeating_count == 0:
            one_nonrepeating_count += 1
        if repeating_count == 0:
            zero_repeating_count += 1
        else:
            if odd_periodic:
                odd_periodic_count += 1
            else:
                even_periodic_count += 1
        if nonrepeating_count == 0:
            zero_nonrepeating_count += 1

    return one_nonrepeating_count, zero_repeating_count, zero_nonrepeating_count, odd_periodic_count, even_periodic_count


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


def continued_fraction_approximation(coeff_list, n):
    """Return fractional approximations of continued fractions given a list of coefficients.

    :param coeff_list:  of the form [a1, a2, (b1, b2, b3, ...)] where there is at least one non-repeating coeff a1.
    :param n:           number of coefficients to use in the approximation
    :return:            numerator, denominator, fractional approximation
    """

    if isinstance(coeff_list[-1], tuple):
        nonrepeating_len = len(coeff_list) - 1
        repeating_len = len(coeff_list[-1])
    else:
        nonrepeating_len = len(coeff_list)
        repeating_len = 0
        if nonrepeating_len < n:
            # error !!!
            pass

    num = 0
    den = 1
    if n > 1:
        if n <= nonrepeating_len:
            for index in reversed(range(1, n)):
                num, den = den, coeff_list[index]*den + num
        else:
            repeat_list = coeff_list[-1]
            repeat_n = n - nonrepeating_len

            # initial loop
            start_index = repeat_n % repeating_len
            if start_index > 0:
                for index in reversed(range(start_index)):
                    num, den = den, repeat_list[index]*den + num

            # repeated loops
            for repeat_index in range(repeat_n // repeating_len):
                for index in reversed(range(repeating_len)):
                    num, den = den, repeat_list[index]*den + num

            # non-repeating coeffs
            if nonrepeating_len > 1:
                nonrepeat_list = coeff_list[:-1]
                for index in reversed(range(1, nonrepeating_len)):
                    num, den = den, nonrepeat_list[index]*den + num

    den, num = den, coeff_list[0]*den + num

    return num, den, num/den


def generate_continued_fraction_coeffs_e(n):
    """Return the first n coefficients for continued fraction expansion of e."""

    coeff_list = [2]
    for index in range(1, 2+(n-1)//3):
        coeff_list.extend([1, 2*index, 1])

    return coeff_list[:n]


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


# Problem 60-69 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 65

    if problem_num == 60:
        print()
        zprime_list = common.sieve_erathosthenes(10**5)
        print('check_prime_concatenations(7, 109, zprime_list) = ', check_prime_concatenations(7, 109, zprime_list))
        print('check_prime_concatenations(7, 11, zprime_list) = ', check_prime_concatenations(7, 11, zprime_list))
        print('check_prime_pairs(1, [7, 109], zprime_list) = ', check_prime_pairs(1, [7, 109], zprime_list))
        print('check_prime_pairs(4, [7, 109], zprime_list) = ', check_prime_pairs(4, [7, 109], zprime_list))
        print('min_prime_pair_set(2) = ', min_prime_pair_set(2))
        print('min_prime_pair_set(3) = ', min_prime_pair_set(3))
#        print('min_prime_pair_set(4) = ', min_prime_pair_set(4))
        print('min_prime_pair_set_mr(4) = ', min_prime_pair_set_mr(4))
        print('min_prime_pair_set_mr(5) = ', min_prime_pair_set_mr(5))
    elif problem_num == 61:
        print()
        zside_count = 3
        for z in range(1, 4):
            print('polygonal_number_list(', zside_count, ',', z, ') = ', generate_polygonal_number_list(zside_count, z))
        print()
        zresult = cyclic_4digit_set(6)
        print('cyclic_4digit_set( 6 ) = ', zresult)
        print('sum(cyclic_4digit_set( 6 )) = ', sum([z[1] for z in zresult[0]]))
    elif problem_num == 62:
        print()
        print(cube_permutations(3))
        print(cube_permutations(4))
        print(cube_permutations(5))
    elif problem_num == 63:
        print(power_digit_counts())
    elif problem_num == 64:
        print()
        z = 23
        zcoeff_list = sqrt_continued_fraction_coeffs(z)
        print('sqrt_continued_fraction_coeffs(', z, ') :', zcoeff_list, '  counts: ',
              continued_fractions_term_counts(zcoeff_list))
        print()
        for z in range(2, 14):
            zcoeff_list = sqrt_continued_fraction_coeffs(z)
            print('sqrt_continued_fraction_coeffs(', z, ') :', zcoeff_list, '  counts: ',
                  continued_fractions_term_counts(zcoeff_list))
        print()
        print('continued_fractions_term_stats(sqrt_continued_fraction_coeffs, 2, 13) = ',
              continued_fractions_term_stats(sqrt_continued_fraction_coeffs, 2, 13))
        print('continued_fractions_term_stats(sqrt_continued_fraction_coeffs, 2, 10000) = ',
              continued_fractions_term_stats(sqrt_continued_fraction_coeffs, 2, 10000))
    elif problem_num == 65:
        print()
        zlast_index = 10
        zcoeff_list = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        for z in range(1, zlast_index+1):
            print(continued_fraction_approximation(zcoeff_list, z))
        print()
        zcoeff_list = [1, (2,)]
        for z in range(1, zlast_index+1):
            print(continued_fraction_approximation(zcoeff_list, z))
        print()
        zcoeff_list = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1]
        for z in range(1, zlast_index+1):
            print(continued_fraction_approximation(zcoeff_list, z))
        print()
        for z in range(1, zlast_index+1):
            print(z, generate_continued_fraction_coeffs_e(z))
        print()
        z = 100
        zcoeff_list = generate_continued_fraction_coeffs_e(z)
        print(z, continued_fraction_approximation(zcoeff_list, z))
    elif problem_num == 66:
        print()
    elif problem_num == 67:
        print()
    elif problem_num == 68:
        print()
    elif problem_num == 69:
        print()
