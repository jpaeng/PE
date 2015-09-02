""" Collatz Sequence Problem
The following iterative sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

"""


def collatz_sequence(n):
    """Return Collatz Sequence for n as a list. """
    col_list = [n]
    while n > 1:
        if n % 2:   # odd
            n = 3*n + 1
        else:       # even
            n = int(n/2)
        col_list.append(n)
    return col_list


def solution(upper_limit):
    """Return number (bound by upper_limit) with longest Collatz Sequence. """
    max_start = -1
    max_length = -1
    for n in range(1, upper_limit + 1):
        length = len(collatz_sequence(n))
        if max_length < length:
            max_length = length
            max_start = n
    return max_start


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    for i in range(1, 16):
        print(collatz_sequence(i))
    print()
    max_start = solution(999999)
    print(max_start, len(collatz_sequence(max_start)))
