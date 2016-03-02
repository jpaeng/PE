
import math
import common
import pytest

import p00x
import p01x
import p02x
import p03x
import p04x
import p05x
import p06x


def test_common():
    # variables
    ordered_list = list(range(-10, 10))
    prime_list_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # power_digit_sum
    common.power_digit_sum(2, 15) == 26

    # index_in_ordered_list
    assert common.index_in_ordered_list(-10, ordered_list) == ordered_list.index(-10)
    assert common.index_in_ordered_list( -1, ordered_list) == ordered_list.index(-1)
    assert common.index_in_ordered_list(  0, ordered_list) == ordered_list.index(0)
    assert common.index_in_ordered_list(  9, ordered_list) == ordered_list.index(9)
    assert common.index_in_ordered_list( 10, ordered_list) == -1
    assert common.index_in_ordered_list(-11, ordered_list) == -1

    # is_in_ordered_list
    assert common.is_in_ordered_list(-10, ordered_list)
    assert common.is_in_ordered_list( -1, ordered_list)
    assert common.is_in_ordered_list(  0, ordered_list)
    assert common.is_in_ordered_list(  9, ordered_list)
    assert common.is_in_ordered_list( 10, ordered_list) is False
    assert common.is_in_ordered_list(-11, ordered_list) is False

    assert common.str_permutation(11, '0123') == '1320'
    assert common.str_permutation(999999, '0123456789') == '2783915460'

    # get_factors
    assert common.get_factors(1) == [1]
    assert common.get_factors(16) == [1, 2, 4, 8, 16]

    # sieve_erathosthenes
    assert common.sieve_erathosthenes(30) == prime_list_10
    assert common.sieve_erathosthenes(30) != ordered_list
    assert common.sieve_erathosthenes2(30) == prime_list_10
    assert common.prime_list_mr(30) == prime_list_10

    # get_prime_factors
    assert common.get_prime_factors(0, prime_list_10) == []
    assert common.get_prime_factors(2, prime_list_10) == [2]
    assert common.get_prime_factors(512, prime_list_10) == [2]
    assert common.get_prime_factors(60, prime_list_10) == [2, 3, 5]
    assert common.get_prime_factors(6469693230, prime_list_10) == prime_list_10

    #


def test_p001():
    with pytest.raises(ZeroDivisionError):
        p00x.sum_of_multiples(100, 0)
    assert p00x.sum_of_multiples(9, 1) == 45
    assert p00x.sum_of_two_multiples(9, 3, 5) == 23


def test_p002():
    assert p00x.sum_even_fibonacci(33) == 10
    assert p00x.sum_even_fibonacci(34) == 44


def test_p003():
    assert p00x.largest_prime_factor(0) == 0
    assert p00x.largest_prime_factor(5) == 5
    assert p00x.largest_prime_factor(13195) == 29


def test_p004():
    assert p00x.is_num_palindrome(11)
    assert p00x.is_num_palindrome(909)
    assert p00x.is_num_palindrome(422) is False

    assert p00x.largest_palindrome_product(100, 15) == (99, 11, 9)
    assert p00x.largest_palindrome_product(101, 15) == (99, 11, 9)
    assert p00x.largest_palindrome_product(101, 15) != (99, 11, 10)


def test_p005():
    assert p00x.least_common_multiple_of_sequence(10) == 2520


def test_p006():
    assert p00x.square_of_sum_minus_sum_of_squares(10) == 2640


# def test_p007():
#     assert p00x.nth_prime(6)   == 13
#     assert p00x.nth_prime(100) == 541
#     assert p00x.nth_prime(121) == 661
#     assert p00x.nth_prime(167) == 991


def test_p010():
    assert p01x.sum_of_primes(10) == 17


def test_p011():
    text = [str(x) for x in range(16)]
    text = ' '.join(text)
    grid = p01x.text_to_grid(text, 4, 4)
    assert p01x.greatest_n_adjacent_product(grid, 4, 4, 2) == 210

    text = [str(x) for x in range(15, -1, -1)]
    text = ' '.join(text)
    grid = p01x.text_to_grid(text, 4, 4)
    assert p01x.greatest_n_adjacent_product(grid, 4, 4, 2) == 210


def test_p012():
    assert p01x.triangle_number_with_n_divisors(5) == (28, [1, 2, 4, 7, 14, 28])


def test_p013():
    text_list = [str(x) for x in range(1000, 10000, 100)]
    assert p01x.sum_msb_digits(text_list, 1) == 450
    assert p01x.sum_msb_digits(text_list, 2) == 4905


def test_p014():
    assert p01x.collatz_sequence(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert p01x.longest_collatz_sequence(15) == 9


def test_p015():
    assert p01x.lattice_path_count_recursive((2, 2)) == 6
    assert p01x.lattice_path_count_recursive((10, 10)) == 184756
    for n in range(1, 11):
        assert p01x.lattice_path_count_formula(n) == p01x.lattice_path_count_recursive((n, n))


def test_p017():
    assert p01x.number_letter_count_math(5) == 4
    assert p01x.number_letter_count_math(115) == 20
    assert p01x.number_letter_count_math(342) == 23
    assert p01x.sum_of_number_letter_counts_math(5) == 19
    assert p01x.sum_of_number_letter_counts_math(342) == 6117


def test_p019():
    # TODO ERROR CONDITIONS
    curr_date = {'month': 7, 'day': 1, 'year': 2015, 'weekday': 3}     # 7/1/2015, Wednesday
    p01x.increment_month(curr_date)
    assert curr_date == {'month': 8, 'day': 1, 'year': 2015, 'weekday': 6}
    p01x.increment_month(curr_date)
    assert curr_date == {'month': 9, 'day': 1, 'year': 2015, 'weekday': 2}

    stop_date = {'month': 6, 'day': 25, 'year': 2016, 'weekday': 6}     # 6/25/2016, Saturday
    assert p01x.count_weekdays(curr_date, 0, stop_date) == 2


def test_p020():
    assert p02x.sum_digits(math.factorial(10)) == 27


def test_p021():
    assert p02x.amicable_list(10000) == [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]


def test_p022():
    assert p02x.alpha_value('Colin') == 53
    p022_name_list = ['Jock', 'Alex', 'Colin']
    assert p02x.alpha_list_score(p022_name_list) == 265


def test_p023():
    assert p02x.abundant_list(40) == [12, 18, 20, 24, 30, 36, 40]
    assert p02x.abundant_sum_list(40) == [24, 30, 32, 36, 38, 40]
    assert p02x.non_abundant_sum_list(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_p025():
    assert p02x.fibonacci_greater_than(10) == (7, 13)
    assert p02x.fibonacci_greater_than(100) == (12, 144)


def test_p026():
    assert p02x.recurring_cycle(2) == 0
    assert p02x.recurring_cycle(7) == 6
    assert p02x.recurring_cycle(9) == 1


def test_p027():
    pr27_coeff_list = common.sieve_erathosthenes(50)
    pr27_prime_list = common.sieve_erathosthenes(3000)
    assert p02x.consecutive_prime_count(1, 41, pr27_prime_list) == 40
    assert p02x.consecutive_prime_count(-1, 41, pr27_prime_list) == 41
    assert p02x.max_count_given_b(41, pr27_coeff_list, pr27_prime_list) == (-1, 41, 41)
    assert p02x.max_count_combination(pr27_coeff_list, pr27_prime_list) == (-5, 47, 43)


def test_p028():
    assert p02x.number_spiral_diagonal_sum(5, 1, 1) == 101
    assert p02x.number_spiral_diagonal_sum(1001, 1, 1) == 669171001


def test_p029():
    pr29_list = [z for z in range(2, 6)]
    assert len(p02x.distinct_powers(pr29_list)) == 15
    pr29_list = [z for z in range(2, 101)]
    assert len(p02x.distinct_powers(pr29_list)) == 9183


def test_p030():
    assert p03x.sum_of_digit_powers(1634, 4) == 1634
    assert p03x.sum_of_digit_powers(8208, 4) == 8208
    assert p03x.sum_of_digit_powers(9474, 4) == 9474
    assert p03x.sum_of_digit_powers(1635, 4) == 2003
    assert p03x.sum_of_digit_powers(8218, 4) == 8209
    assert p03x.sum_of_digit_powers(9574, 4) == 9843
    assert p03x.position_value(9876543210, 3) == 3
    assert p03x.increment_position(9876543210, 4) == 9876553210
    assert p03x.set_next_digit(1000, 2, 4) == [1634]
    assert p03x.perfect_digit_powers(4) == [1, 1634, 8208, 9474]


def test_p031():
    coin_list = [200, 100, 50, 20, 10, 5, 2, 1]
    assert p03x.coin_combinations(0, coin_list, 1) == 1
    assert p03x.coin_combinations(1, coin_list, 1) == 1
    assert p03x.coin_combinations(2, coin_list, 1) == 2
    assert p03x.coin_combinations(3, coin_list, 1) == 2
    assert p03x.coin_combinations(4, coin_list, 1) == 3
    assert p03x.coin_combinations(200, coin_list, 1) == 73682


def test_p032():
    assert p03x.is_pandigital_3(0, 0, 0) == False
    assert p03x.is_pandigital_3(1, 1111, 1111) == False
    assert p03x.is_pandigital_3(1, 2345, 6789)
    assert p03x.is_pandigital_3(39, 186, 7254)
    assert p03x.pandigital_products() == [6952, 7852, 5796, 5346, 4396, 7254, 7632]


def test_p034():
    assert p03x.factorial_sum_list(200) == [1, 2, 145]


def test_p035():
    assert p03x.circular_primes(100) == [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]


def test_p036():
    assert p03x.double_base_palindromes(1000) == [1, 3, 5, 7, 9, 33, 99, 313, 585, 717]


def test_p037():
    assert p03x.truncatable_primes() == [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]


def test_p038():
    assert p03x.pandigital_concatenated_multiples() == [(932718654, 9327, 18654), (327654981, 327, 654, 981), (918273645, 9, 18, 27, 36, 45)]


def test_p040():
    assert p04x.nth_digit(188) == 9
    assert p04x.nth_digit(189) == 9
    assert p04x.nth_digit(190) == 1
    assert p04x.nth_digit(191) == 0
    assert p04x.nth_digit(192) == 0
    assert p04x.nth_digit(193) == 1
    assert p04x.nth_digit(194) == 0
    assert p04x.nth_digit(195) == 1
    assert p04x.nth_digit(196) == 1
    assert p04x.nth_digit(197) == 0
    assert p04x.nth_digit(198) == 2


def test_p041():
    assert p04x.pandigital_primes(4, '1234') == [1423, 2143, 2341, 4231]


def test_p042():
    assert p04x.triangle_words(['sky', 'SKY', 'ski'], 25) == [('sky', 55), ('SKY', 55)]


def test_p043():
    assert p04x.pandigital_sub_divisible('6', '5', '0123456789') == [1406357289, 4106357289]


def test_p045():
    assert p04x.tri_pent_hex(3) == [1, 40755, 1533776805]


def test_p047():
    assert p04x.consecutive_prime_factors(3, 3, 1000) == [644, 645, 646]


def test_p049():
    assert p04x.prime_permutation_arithmetic_sequence(4, 3) == [[1487, 4817, 8147], [2969, 6299, 9629]]


def test_p050():
    assert p05x.consecutive_prime_sum(100) == (6, 41, [2, 3, 5, 7, 11, 13])


def test_p051():
    assert p05x.prime_digit_replacement_families(2, 6) == [[13, 23, 43, 53, 73, 83]]


def test_p052():
    assert p05x.smallest_permuted_multiples(10, [2, 3, 4, 5, 6]) == 142857


def test_p053():
    assert p05x.combination_counts(10, 100) == 5
    assert p05x.combination_counts(23, 1000000) == 4
    assert p05x.combination_counts_max_n(11, 100) == 13


def test_p055():
    assert p05x.lychrel_numbers(1000) == [196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986]


def test_p057():
    assert p05x.next_sqrt_fraction(577, 408) == (1393, 985)


def test_p058():
    assert p05x.next_spiral_corner(4, 4, 25) == (1, 6, 31)
    assert p05x.spiral_corner_prime_ratio_mr(0.1, 10**9) == (688590081, 26240, 52481, 0.09999809454850327)


def test_p059():
    assert p05x.decrypt_xor([65, 42, 107], [42, 65, 42]) == ([107, 107, 65], 279, 1.0)


def test_p060():
    assert p06x.check_prime_concatenations_mr(7, 109) == True
    assert p06x.check_prime_concatenations_mr(7, 11) == False
    assert p06x.check_prime_pairs_mr(1, [7, 109]) == True
    assert p06x.check_prime_pairs_mr(4, [7, 109]) == False
    assert p06x.min_prime_pair_set_mr(4) == ([3, 7, 109, 673], 792)


def test_p061():
    assert p06x.generate_polygonal_number_list(3, 2) == [10, 15, 21, 28, 36, 45, 55, 66, 78, 91]
    assert p06x.cyclic_4digit_set(6) == [[(8, 1281), (6, 8128), (5, 2882), (3, 8256), (4, 5625), (7, 2512)]]


def test_p062():
    assert p06x.cube_permutations(3) == [41063625, 56623104, 66430125]


def test_p064():
    assert p06x.sqrt_continuing_fraction_coeffs(23) == [4, (1, 3, 1, 8)]
    assert p06x.continuing_fractions_term_stats(p06x.sqrt_continuing_fraction_coeffs, 2, 13) == (2, 2, 0, 4, 6)
