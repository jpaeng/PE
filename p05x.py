""" Project Euler Problems 50-59
"""


import math
import string
import common

from timeit import default_timer as timer


# Problem 50: Consecutive Prime Sum
# The prime 41, can be written as the sum of six consecutive primes:
#     41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def consecutive_prime_sum(max_sum):
    """Return longest list of consecutive primes that sum to a prime under max_sum."""
    prime_list = common.sieve_erathosthenes(max_sum)
    max_sum = prime_list[-1]        # redefine max_sum to be largest prime number < original max_sum
    max_length = 1
    max_length_sum = 2
    max_list = []
    len_prime_list = len(prime_list)

    for start_index in range(len_prime_list):
        # for each start_index, start checking with sequence of current max_length
        current_index = start_index + max_length
        if current_index > len_prime_list:
            break
        else:
            current_sum = sum(prime_list[start_index:current_index])
            if current_sum > max_sum:
                break
            else:
                # for each added prime, check that sum does not exceed max_sum
                for current_index in range(current_index, len_prime_list):
                    current_sum += prime_list[current_index]
                    if current_sum > max_sum:
                        break
                    elif common.is_in_ordered_list(current_sum, prime_list):
                        max_length_sum = current_sum
                        max_length = current_index - start_index + 1
                        max_list = prime_list[start_index:current_index+1]
    return max_length, max_length_sum, max_list


# Problem 51: Prime Digit Replacements
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
#     13, 23, 43, 53, 73, and 83,
# are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having 7
# primes among the ten generated numbers, yielding the family:
#     56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

def digit_replacement_families(num):
    """Return list of all possible digit replacement families of num."""
    str_num = str(num)
    digits = [c for c in str_num]
    digits = list(set(digits))      # remove duplicates to make a list of unique digits in str_num

    results = []

    for digit in digits:
        family = [int(str_num.replace(digit, c)) for c in "0123456789"]
        results.append(family)

    return results


def prime_digit_replacement_families(digit_count, family_count):
    """Return families of prime numbers generated by digit replacement with at least family_count members."""

    # Make list of prime numbers of the correct digit_count.
    prime_list = common.sieve_erathosthenes(10**digit_count)
    n = 10**(digit_count-1)
    index = -1
    while index < 0:    # find index of first prime number with correct digit_count
        n += 1
        index = common.index_in_ordered_list(n, prime_list)     # returns -1 if n not found
    prime_list = prime_list[index:]   # prime_list now contains only primes of digit_count

    results = []        # results = the return variable to contain the family lists.

    # Loop through primes, making and checking prime families
    for prime in prime_list:
        family_list = digit_replacement_families(prime)
        for family in family_list:
            prime_family = [num for num in family if common.is_in_ordered_list(num, prime_list)]
            if len(prime_family) >= family_count and prime_family not in results:
                results.append(prime_family)

    return results


# Problem 52: Permuted Multiples
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
# but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def smallest_permuted_multiples(start_n, multipliers):
    """ Return the smallest number greater than start_n for which multiples contains the same digits."""
    n = start_n
    perm_status = False
    while True:         # loop until number found
        max_n = int(10**int(math.log10(start_n+1)+1)/max(multipliers))  # find max n which will keep the same digit count
        for n in range(start_n, max_n + 1):     # loop through n of the same digit count
            str_n = str(n)
            for mult in multipliers:
                perm_status = common.is_permutation(str_n, str(mult*n))
                if not perm_status:
                    break
            if perm_status:
                break
        if perm_status:
            break
        start_n = 10**int(math.log10(n)+1)      # calculate start n for increasing digit count by 1
    if perm_status:
        return n
    else:
        return 0    # return 0 if not found (will never execute because function will run infinite loop instead


# Problem 53: Combinatoric Selections
# There are exactly ten ways of selecting three from five, 12345:
#     123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, 5C3 = 10.
# In general, nCr = n!/(r!(n-r)!), where r != n, n! = nx(n-1)x...x3x2x1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
# How many, not necessarily distinct, values of  nCr, for 1 = n = 100, are greater than one-million?
# NOTE:  nCr = nC(n-r)

def combination_counts(n, threshold):
    """For a given n, return the count of r's that generate nCr >= threshold."""
    hi = int(n/2)
    lo = 1

    # make sure at least one nCr > threshold
    combs = common.combinations(n, hi)
    if combs < threshold:
        count = 0
    else:
        # binary search to find r when nCr falls below threshold
        while True:
            mid = int((hi + lo)/2)
            combs = common.combinations(n, mid)
            if combs < threshold:
                lo = mid
            else:
                hi = mid
            if hi - lo < 2:
                break
        # calculate the number of r values for which nCr >= threshold
        if n % 2:
            count = 2*int(n/2 - hi + 1)
        else:
            count = 2*int(n/2 - hi) + 1

    return count


def combination_counts_max_n(max_n, threshold):
    """Return the count of all (n, r) combinations up to max_n that generate nCr > threshold."""
    count = 0
    for n in range(1, max_n+1):
        count += combination_counts(n, threshold)
    return count


# Problem 54: Poker Hands
# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:  2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# If two players have the same ranked hands then the rank made up of the highest value wins;
# for example, a pair of eights beats a pair of fives (see example 1 below).
# But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared
# (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
# Consider the following five hands dealt to two players:
# Hand    Player 1            Player 2            Winner
#   1     5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
#         Pair of Fives       Pair of Eights
#   2     5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
#         Highest card Ace    Highest card Queen
#   3     2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
#         Three Aces          Flush with Diamonds
#   4     4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
#         Pair of Queens      Pair of Queens
#         Highest card Nine   Highest card Seven
#   5     2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
#         Full House          Full House
#         With Three Fours    with Three Threes
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.
# How many hands does Player 1 win?

def card_parse(str_card):
    """Return list [suit, value] for given str_card."""
    len_card = len(str_card)
    if len_card < 2:
        card = ['error', -100]
    elif len_card > 3:
        card = ['error', -100]
    else:
        card = [str_card[-1]]   # first element is the suit: C D H or S
        if str_card[0] == 'T':  # 10-cards are represented by T
            card.append(10)
        elif str_card[0] == 'J':
            card.append(11)
        elif str_card[0] == 'Q':
            card.append(12)
        elif str_card[0] == 'K':
            card.append(13)
        elif str_card[0] == 'A':
            card.append(14)
        else:
            card.append(int(str_card[:-1]))     # numerical cards
    return card


def card_counts(cards):
    """Return a list of tuples (value, count) for given cards. Input assumed to be sorted by value."""
    value_index = 1
    counts = []
    while len(cards) > 0:
        count = 1
        value = cards[-1][value_index]
        cards.pop()     # remove cards that have been counted
        for i in reversed(range(len(cards))):   # loop until card value changes
            if cards[-1][value_index] == value:
                count += 1
                cards.pop()     # remove cards that have been counted
            else:
                break
        counts.append((value, count))
        counts = common.sort_2d_array(counts, 0)    # sort by value
        counts = common.sort_2d_array(counts, 1)    # sort by count
        # return list sorted by count, then by value, both ascending
    return counts


def score_hand(cards):
    """Return score given a hand of cards.
    Scores:
        Royal Flush:    14e8
        Straight Flush: 2e8 - 14e8
        Four of a Kind: 2e7 - 14e7
        Full House:     2e6 - 14e6
        Flush:          7e5 - 14e5
        Straight:       6e4 - 14e4
        Three of a Kind:2e3 - 14e3
        Two Pairs:      200 - 1400
        One Pair:       20 - 140
        High Card:      2 - 14 (Face value)
    """

    suit_index = 0
    value_index = 1
    len_card = len(cards)
    cards = common.sort_2d_array(cards, value_index)
    value = []

    is_straight = True
    for i in range(len_card-1):
        if cards[i+1][value_index] != cards[i][value_index]+1:
            is_straight = False
            break
    
    is_flush = True
    for i in range(len_card-1):
        if cards[i][suit_index] != cards[i+1][suit_index]:
            is_flush = False
            break

    if is_straight and is_flush:
        value.append(cards[-1][value_index] * 10**8)
    elif is_flush:
        value.append(cards[-1][value_index] * 10**5)
    elif is_straight:
        value.append(cards[-1][value_index] * 10**4)
    else:
        counts = card_counts(cards)
        if counts[-1][1] == 4:      # four of a kind
            value.append(counts[1][0] * 10**7)
            value.append(counts[0][0])
        elif counts[-1][1] == 3:
            if counts[-2][1] == 2:  # full house
                value.append(counts[1][0] * 10**6)
                value.append(counts[0][0])
            else:                   # three of a kind
                value.append(counts[2][0] * 10**3)
                value.append(counts[1][0])
                value.append(counts[0][0])
        elif counts[-1][1] == 2:
            if counts[-2][1] == 2:  # two pair
                value.append(counts[2][0] * 10**2)
                value.append(counts[1][0])
                value.append(counts[0][0])
            else:                   # one pair
                value.append(counts[3][0] * 10**1)
                value.append(counts[2][0])
                value.append(counts[1][0])
                value.append(counts[0][0])
        else:
            for i in reversed(range(len(counts))):
                value.append(counts[i][0])

    return value


def play_hand(str_line):
    """Return winner of a hand of poker coded in str_line. str_line contains 10 cards delimited by spaces."""
    winner = 0
    str_cards = str_line.split(' ')
    if len(str_cards) == 10:
        cards1 = [card_parse(str_cards[i]) for i in range(5)]
        cards2 = [card_parse(str_cards[i]) for i in range(5, 10)]
        score1 = score_hand(cards1)
        score2 = score_hand(cards2)
        for i in range(len(score1)):
            if score1[i] > score2[i]:
                winner = 1
                break
            elif score1[i] < score2[i]:
                winner = 2
                break
    return winner


def play_poker_file(file_name):
    """Return win numbers for player 1 and player 2 for games recorded in file."""
    str_lines = common.read_multi_line_text_file(file_name)

    wins1 = 0
    wins2 = 0

    for line in str_lines:
        if play_hand(line) == 1:
            wins1 += 1
        else:
            wins2 += 1

    return wins1, wins2


# Problem 55: Lychrel Numbers
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce palindromes so quickly. For example,
#      349 + 943  = 1292,
#     1292 + 2921 = 4213
#     4213 + 3124 = 7337
# That is, 349 took three iterations to arrive at a palindrome.
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
# Due to the theoretical nature of these numbers, and for the purpose of this problem,
# we shall assume that a number is Lychrel until proven otherwise.
# In addition you are given that for every number below ten-thousand, it will either
#     (i) become a palindrome in less than fifty iterations, or,
#     (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
# In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
#     4668731596684224866951378664 (53 iterations, 28-digits).
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
# How many Lychrel numbers are there below ten-thousand?
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.


# Problem 56: Powerful Digit Sum
# A googol (10**100) is a massive number: one followed by one-hundred zeros;
# 100**100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?


# Problem 57: Square Root Convergents
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#     sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# By expanding this for the first four iterations, we get:
#     1 + 1/2 = 3/2 = 1.5
#     1 + 1/(2 + 1/2) = 7/5 = 1.4
#     1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#     1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion,
# 1393/985, is the first example where the number of digits in the numerator exceeds
# the number of digits in the denominator.
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?


# Problem 58: Spiral Primes
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#     37 36 35 34 33 32 31
#     38 17 16 15 14 13 30
#     39 18  5  4  3 12 29
#     40 19  6  1  2 11 28
#     41 20  7  8  9 10 27
#     42 21 22 23 24 25 26
#     43 44 45 46 47 48 49
# It is interesting to note that the odd squares lie along the bottom right diagonal,
# but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
# that is, a ratio of 8/13 ~ 62%.
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square spiral for which the ratio of primes
# along both diagonals first falls below 10%?


# Problem 59: XOR Decryption
# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code
# for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
# taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
# For unbreakable encryption, the key is the same length as the plain text message,
# and the key is made up of random bytes.
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves",
# it is impossible to decrypt the message.
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
# and the knowledge that the plain text must contain common English words, decrypt the message and find the sum
# of the ASCII values in the original text.


# Problem 50-59 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 54

    if problem_num == 50:
        print()
        print(consecutive_prime_sum(100))
        print(consecutive_prime_sum(1000))
        print(consecutive_prime_sum(1000000))
    elif problem_num == 51:
        print()
        print(digit_replacement_families(122))
        print(prime_digit_replacement_families(2, 6))
        print(prime_digit_replacement_families(5, 7))
        print(prime_digit_replacement_families(6, 8))
    elif problem_num == 52:
        print()
        print(smallest_permuted_multiples(10, [2]))
        print(smallest_permuted_multiples(10, [3]))
        print(smallest_permuted_multiples(10, [4]))
        print(smallest_permuted_multiples(10, [5]))
        print(smallest_permuted_multiples(10, [6]))
        print(smallest_permuted_multiples(10, [2, 3]))
        print(smallest_permuted_multiples(10, [2, 3, 4]))
        print(smallest_permuted_multiples(10, [2, 3, 4, 5]))
        print(smallest_permuted_multiples(10, [2, 3, 4, 5, 6]))
    elif problem_num == 53:
        print()
        zn = 10
        zcount = 100
        print(zn, zcount, combination_counts(zn, zcount))
        zn = 11
        zcount = 100
        print(zn, zcount, combination_counts(zn, zcount))
        zn = 23
        zcount = 1000000
        print(zn, zcount, combination_counts(zn, zcount))
        zn = 100
        zcount = 1000000
        print(zn, zcount, combination_counts_max_n(zn, zcount))
    elif problem_num == 54:
        print()
        print(card_parse('2H'))
        print(card_parse('QC'))
        print(card_parse('TD'))
        zcards1 = [card_parse(z) for z in '2H 2D 4C 4D 4S'.split(' ')]
        zcards2 = [card_parse(z) for z in '3C 3D 3S 9S 9D'.split(' ')]
        print(card_counts(zcards1))
        print(card_counts(zcards2))
        zcards1 = [card_parse(z) for z in '2H 2D 4C 4D 4S'.split(' ')]
        zcards2 = [card_parse(z) for z in '3C 3D 3S 9S 9D'.split(' ')]
        print(score_hand(zcards1))
        print(score_hand(zcards2))
        print(1, play_hand('5H 5C 6S 7S KD 2C 3S 8S 8D TD'))
        print(2, play_hand('5D 8C 9S JS AC 2C 5C 7D 8S QH'))
        print(3, play_hand('2D 9C AS AH AC 3D 6D 7D TD QD'))
        print(4, play_hand('4D 6S 9H QH QC 3D 6D 7H QD QS'))
        print(5, play_hand('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'))
        print(play_poker_file('p054_poker.txt'))
    elif problem_num == 55:
        print()
    elif problem_num == 56:
        print()
    elif problem_num == 57:
        print()
    elif problem_num == 58:
        print()
    elif problem_num == 59:
        print()
