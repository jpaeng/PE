
import math
import common
import pytest

import p00x
import p01x
import p02x


def test_common():
    # variables
    ordered_list = list(range(-10, 10))
    prime_list_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

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

    # get_factors
    assert common.get_factors(1) == [1]
    assert common.get_factors(16) == [1, 2, 4, 8, 16]

    # sieve_erathosthenes
    assert common.sieve_erathosthenes(30) == prime_list_10
    assert common.sieve_erathosthenes(30) != ordered_list

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


def test_p007():
    assert p00x.nth_prime(6)   == 13
    assert p00x.nth_prime(100) == 541
    assert p00x.nth_prime(121) == 661
    assert p00x.nth_prime(167) == 991


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


def test_p016():
    assert p01x.power_digit_sum(2, 15) == 26


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


def test_p024():
    assert p02x.lexi_perm(11, 4) == '1320'
    assert p02x.lexi_perm(999999, 10) == '2783915460'


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
