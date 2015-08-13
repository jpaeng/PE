# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(string):
    length = len(string)
    if length < 2:
        return True
    else:
        if string[0] == string[-1]:
            return isPalindrome(string[1:-1])
        else:
            return False


def isNumPalindrome(num):
    if num < 10:
        return True
    else:
        strnum = str(num)
        return isPalindrome(strnum)


def solution(num, maxfactor):
    f2 = None
    for n in range(num, 0, -1):
        if isNumPalindrome(n):
            for f1 in range(maxfactor, 0, -1):
                if n/f1 > maxfactor:
                    break
                elif n%f1 == 0:
                    f2 = n/f1
                    break
            if f2 != None:
                break
    return n, f1, f2


print (solution(100,15))
print (solution(10000,99))
print (solution(1000000,999))
print (solution(100000000,9999))
