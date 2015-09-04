""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples(max_n, n):
    """
    Sum all integers from 0 to max_n that are multiples of n
    Note:
        n + 2n + 3n + ...   = n(1+2+3+...)
        1 + 2 + 3 + ... + p = p*(p+1)/2
    """
    p = int(max_n / n)  # integer division
    return n * (p * (p + 1) / 2)


def sum_of_two_multiples(max_n):
    return sum_of_multiples(max_n, 3) + sum_of_multiples(max_n, 5) - sum_of_multiples(max_n, 15)


if __name__ == '__main__':
    print(sum_of_two_multiples(9))
    print(sum_of_two_multiples(999))
