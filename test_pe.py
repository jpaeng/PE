
import common
import pytest

import p010
import p011
import p012
import p013
import p014
import p015
import p016
import p017
import p019

import p00x


def test_common():
    # variables
    ordered_list = list(range(-10, 10))
    prime_list_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # indexInOrderedList
    assert common.index_in_ordered_list(-10, ordered_list) == 0
    assert common.index_in_ordered_list( -1, ordered_list) == 9
    assert common.index_in_ordered_list(  0, ordered_list) == 10
    assert common.index_in_ordered_list(  9, ordered_list) == 19
    assert common.index_in_ordered_list( 10, ordered_list) == -1
    assert common.index_in_ordered_list(-11, ordered_list) == -1

    # isInOrderedList
    assert common.is_in_ordered_list(-10, ordered_list)
    assert common.is_in_ordered_list( -1, ordered_list)
    assert common.is_in_ordered_list(  0, ordered_list)
    assert common.is_in_ordered_list(  9, ordered_list)
    assert common.is_in_ordered_list( 10, ordered_list) is False
    assert common.is_in_ordered_list(-11, ordered_list) is False

    # sieve_erathosthenes
    assert common.sieve_erathosthenes(30) == prime_list_10
    assert common.sieve_erathosthenes(30) != ordered_list

    # getPrimeFactors
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
    assert p010.sum_of_primes(10) == 17


def test_p011():
    text = [str(x) for x in range(16)]
    text = ' '.join(text)
    grid = p011.text_to_grid(text, 4, 4)
    assert p011.greatest_n_adjacent_product(grid, 4, 4, 2) == 210

    text = [str(x) for x in range(15, -1, -1)]
    text = ' '.join(text)
    grid = p011.text_to_grid(text, 4, 4)
    assert p011.greatest_n_adjacent_product(grid, 4, 4, 2) == 210


def test_p012():
    assert p012.get_factors(1) == [1]
    assert p012.get_factors(16) == [1, 2, 4, 8, 16]
    assert p012.triangle_number_with_n_divisors(5) == (28, [1, 2, 4, 7, 14, 28])


def test_p013():
    text_list = [str(x) for x in range(1000, 10000, 100)]
    assert p013.sum_digits(text_list, 1) == 450
    assert p013.sum_digits(text_list, 2) == 4905


def test_p014():
    assert p014.collatz_sequence(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert p014.longest_collatz_sequence(15) == 9


def test_p015():
    assert p015.lattice_path_count_recursive((2, 2)) == 6
    assert p015.lattice_path_count_recursive((10, 10)) == 184756
    for n in range(1, 11):
        assert p015.lattice_path_count_formula(n) == p015.lattice_path_count_recursive((n, n))


def test_p016():
    assert p016.power_digit_sum(2, 15) == 26


def test_p017():
    assert p017.number_letter_count_math(5) == 4
    assert p017.number_letter_count_math(115) == 20
    assert p017.number_letter_count_math(342) == 23
    assert p017.sum_of_number_letter_counts_math(5) == 19
    assert p017.sum_of_number_letter_counts_math(342) == 6117


def test_p019():
    # TODO ERROR CONDITIONS
    curr_date = {'month': 7, 'day': 1, 'year': 2015, 'weekday': 3}     # 7/1/2015, Wednesday
    p019.increment_month(curr_date)
    assert curr_date == {'month': 8, 'day': 1, 'year': 2015, 'weekday': 6}
    p019.increment_month(curr_date)
    assert curr_date == {'month': 9, 'day': 1, 'year': 2015, 'weekday': 2}

    stop_date = {'month': 6, 'day': 25, 'year': 2016, 'weekday': 6}     # 6/25/2016, Saturday
    assert p019.count_weekdays(curr_date, 0, stop_date) == 2
