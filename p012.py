# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
#                                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

import math

def getFactors(num):        # Valid for num > 1
    result = [1]
    if num > 1:
        hiresult = [num]
    else:
        hiresult = []
    maxcheck = int(math.sqrt(num))+1
    for n in range(2, maxcheck):
        if num%n == 0:
            n2 = int(num/n)
            result.append(n)
            if n != n2:
                hiresult.insert(0, n2)
    result.extend(hiresult)
    return result


def solution(target_factor_count):
    triangle_num = 0
    n = 0
    while True:
        n += 1
        triangle_num += n
        factors = getFactors(triangle_num)
        if len(factors) > target_factor_count:
            break
    return triangle_num, factors


triangle_num, factors = solution(5)
print(triangle_num, len(factors), factors)
