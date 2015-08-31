# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_str_palindrome(string):
    length = len(string)
    if length < 2:
        return True
    else:
        if string[0] == string[-1]:
            return is_str_palindrome(string[1:-1])
        else:
            return False


def is_num_palindrome(num):
    if num < 10:
        return True
    else:
        strnum = str(num)
        return is_str_palindrome(strnum)


def solution(num, maxfactor):
    n = None
    f1 = None
    f2 = None
    for n in range(num, 0, -1):
        if is_num_palindrome(n):
            for f1 in range(maxfactor, 0, -1):
                if n / f1 > maxfactor:
                    break
                elif n % f1 == 0:
                    f2 = int(n / f1)
                    break
            if f2 is None:
                break
    return n, f1, f2


print(solution(100, 15))
print(solution(10000, 99))
# print(solution(1000000, 999))
# print(solution(100000000, 9999))
