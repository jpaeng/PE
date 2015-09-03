""" Power digit sum

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?

"""


def power_digit_sum(num, pwr):
    str_ans = str(num**pwr)
    sum_dig = sum(int(str_ans[i]) for i in range(len(str_ans)))
    return sum_dig


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    for n in range(16):
        print(n, 2**n, power_digit_sum(2, n))
    print()
    print(1000, power_digit_sum(2, 1000))
