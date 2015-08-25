# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def solution(sum):
    result = -1
    for a in range(1,int(sum/2)):
        for c in range(int((sum-a)/2), sum-2*a):
            b = sum - a - c
            if a**2 + b**2 == c**2:
                result = a*b*c
                break
        if result > 0:
            break
    return a, b, c, result


print(solution(1000))
if False:
#    for n in range(5, 20):
    for n in range(5, 1010):
        ans = solution(n)
        if ans[3] > 0:
            print(n, ans)