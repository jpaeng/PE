# Find the greatest product of five consecutive digits in the 1000-digit number.

from timeit import default_timer as timer

strnum = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'


def handle_zero(index, prod_count, string_length, window_list, num_string):
    prod = 1
    if index+prod_count < string_length:
        window_list[0] = 1
        for window_index in range(1, prod_count):
            window_list[window_index] = int(num_string[index+window_index])
            if window_list[window_index] == 0:
                index, prod = handle_zero(index+window_index, prod_count, string_length, window_list, num_string)
                index -= prod_count
                break
            else:
                prod *= window_list[window_index]
    index += prod_count
    return index, prod


def solution1(num_string, prod_count):
    prod = 1
    max_prod = 0
    string_length = len(num_string)
    window_list = []
    window_index = 0
    if prod_count < string_length:
        for window_index in range(prod_count):
            window_list.append(int(num_string[window_index]))
            prod *= window_list[window_index]
        max_prod = prod
        max_window_index = prod_count - 1
        index = prod_count
        while index < string_length:
            if window_index >= max_window_index:
                window_index = 0
            else:
                window_index += 1
            prod /= window_list[window_index]
            window_list[window_index] = int(num_string[index])
            if window_list[window_index] == 0:
                index, prod = handle_zero(index, prod_count, string_length, window_list, num_string)
            else:
                prod *= window_list[window_index]
                index += 1
            max_prod = max(max_prod, prod)
    return max_prod


def solution2(num_string, prod_count):
    string_length = len(num_string)
    num_list = []
    max_prod = 1
    if prod_count < string_length:
        for index in range(prod_count):
            num_list.append(int(num_string[index]))
        for index in range(prod_count, string_length):
            num_list.append(int(num_string[index]))
            max_prod = max(max_prod, num_list[index] * num_list[index-1] * num_list[index-2] * num_list[index-3]
                           * num_list[index-4])
    return max_prod


def solution3(num_string, prod_count):
    string_length = len(num_string)
    max_prod = 0
    if prod_count < string_length:
        num_list = [int(num_string[i]) for i in range(string_length)]
        for i in range(prod_count, string_length):
            prod = 1
            for j in range(prod_count):
                prod *= num_list[i-j]
            max_prod = max(max_prod, prod)
    return max_prod


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    print(len(strnum))

    print(solution1(strnum, 5))
    print(solution2(strnum, 5))
    print(solution3(strnum, 5))

    # Time Check
    count = 1000
    start = timer()
    for n in range(count):
        solution1(strnum, 5)
    time1 = timer()
    for n in range(count):
        solution2(strnum, 5)
    time2 = timer()
    for n in range(count):
        solution3(strnum, 5)
    time3 = timer()

    print(time1-start)  # in ms
    print(time2-time1)  # in ms
    print(time3-time2)  # in ms
