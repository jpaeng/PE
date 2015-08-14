
import common
import pytest
import p001
import p002
import p003
import p004
import p005

def test_common():
    # variables
    ordered_list = list(range(-10,10))
    prime_list_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # indexInOrderedList
    assert common.indexInOrderedList(-10, ordered_list) == 0
    assert common.indexInOrderedList( -1, ordered_list) == 9
    assert common.indexInOrderedList(  0, ordered_list) == 10
    assert common.indexInOrderedList(  9, ordered_list) == 19
    assert common.indexInOrderedList( 10, ordered_list) == -1
    assert common.indexInOrderedList(-11, ordered_list) == -1

    # isInOrderedList
    assert common.isInOrderedList(-10, ordered_list)
    assert common.isInOrderedList( -1, ordered_list)
    assert common.isInOrderedList(  0, ordered_list)
    assert common.isInOrderedList(  9, ordered_list)
    assert common.isInOrderedList( 10, ordered_list) == False
    assert common.isInOrderedList(-11, ordered_list) == False

    # sieve_erathosthenes
    assert common.sieve_erathosthenes(30) == prime_list_10
    assert common.sieve_erathosthenes(30) != ordered_list

    # getPrimeFactors
    assert common.getPrimeFactors(0, prime_list_10) == []
    assert common.getPrimeFactors(2, prime_list_10) == [2]
    assert common.getPrimeFactors(512, prime_list_10) == [2]
    assert common.getPrimeFactors(60, prime_list_10) == [2, 3, 5]
    assert common.getPrimeFactors(6469693230, prime_list_10) == prime_list_10

    #


def test_p001():
    with pytest.raises(ZeroDivisionError):
        p001.sum_multiples(100, 0)
    assert p001.sum_multiples(9, 1)==45

    assert p001.solution(9) == 23


def test_p002():
    assert p002.solution(33) == 10
    assert p002.solution(34) == 44


def test_p003():
    assert p003.solution(0) == 0
    assert p003.solution(5) == 5
    assert p003.solution(13195) == 29


def test_p004():
    assert p004.isNumPalindrome(11)
    assert p004.isNumPalindrome(909)
    assert p004.isNumPalindrome(422) == False

    assert p004.solution(100, 15) == (99, 11, 9)
    assert p004.solution(101, 15) == (99, 11, 9)
    assert p004.solution(101, 15) != (99, 11, 10)

def test_p005():
    assert p005.solution(10) == 2520