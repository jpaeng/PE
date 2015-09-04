""" Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

"""


from timeit import default_timer as timer


ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
         17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
ones_count = {n: len(ones[n]) for n in range(10)}
teens_count = {n: len(teens[n]) for n in range(10, 20)}
tens_count = {n: len(tens[n]) for n in range(2, 10)}


def number_letter_count_math(num):
    """Return the count of letters when num is spelled out. Math algorithm"""

    # Tens, ones
    stripped_num = num - 100*int(num/100)  # strip off thousands, hundreds
    if stripped_num < 1:
        count = 0
    elif stripped_num < 10:
        count = ones_count[stripped_num]
    elif stripped_num < 20:
        count = teens_count[stripped_num]
    else:
        count = tens_count[int(stripped_num/10)]
        stripped_num = num - 10*int(num/10)
        if stripped_num > 0:
            count += ones_count[stripped_num]

    # Hundreds
    if num >= 100:
        if count > 0:
            count += 3      # account for 'and'
        stripped_num = num - 1000*int(num/1000)        # strip off thousands
        if stripped_num > 0:
            count += ones_count[int(stripped_num/100)] + 7   # 'hundred' = 7

        # Thousands
        if num >= 1000:
            stripped_num = num - 10000*int(num/10000)      # strip off anything over 9999
            if stripped_num > 0:
                count += ones_count[int(stripped_num/1000)] + 8  # 'thousand' = 8

    return count


def number_letter_count_text(num):
    """Return the count of letters when num is spelled out. Text conversion algorithm"""
    if num > 19:
        str_num = str(num)
        length = len(str_num)
        digit_list = [int(str_num[i]) for i in range(length-1, -1, -1)]

    # Tens, ones
    stripped_num = num - 100*int(num/100)  # strip off thousands, hundreds
    if stripped_num < 1:
        count = 0
    elif stripped_num < 10:
        count = ones_count[stripped_num]
    elif stripped_num < 20:
        count = teens_count[stripped_num]
    else:
        count = tens_count[digit_list[1]]
        count += ones_count[digit_list[0]]

    # Hundreds
    if num >= 100:
        if count > 0:
            count += 3      # account for 'and'
        count += ones_count[digit_list[2]] + 7   # 'hundred' = 7

        # Thousands
        if num >= 1000:
            count += ones_count[digit_list[3]] + 8  # 'thousand' = 8

    return count


def sum_of_number_letter_counts_math(max_n):
    total = 0
    for i in range(1, max_n+1):
        total += number_letter_count_math(i)
    return total


def sum_of_number_letter_counts_text(max_n):
    total = 0
    for i in range(1, max_n+1):
        total += number_letter_count_text(i)
    return total


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    for n in range(1, 22):
        print(n, number_letter_count_math(n), number_letter_count_text(n))
    n = 342
    print(n, number_letter_count_math(n), number_letter_count_text(n))
    n = 115
    print(n, number_letter_count_math(n), number_letter_count_text(n))

    print()
    print(sum_of_number_letter_counts_math(5))
    print(sum_of_number_letter_counts_math(342))
    print(sum_of_number_letter_counts_math(1000))

    # Time Check
    print()
    count = 1000
    start = timer()
    for n in range(count):
        sum_of_number_letter_counts_math(count)
    time1 = timer()
    for n in range(count):
        sum_of_number_letter_counts_text(count)
    time2 = timer()

    print(time1-start)  # in ms
    print(time2-time1)  # in ms

