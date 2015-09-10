
import math
from timeit import default_timer as timer


# = List Procedures =================================
def index_in_ordered_list(n, ordered_list):      # binary search
    lo = 0
    hi = len(ordered_list)-1
    while (hi - lo) > 1:
        mid = int((lo+hi)/2)
        if n == ordered_list[mid]:
            return mid
        elif n < ordered_list[mid]:
            hi = mid
        else:
            lo = mid

    if n == ordered_list[lo]:
        return lo
    elif n == ordered_list[hi]:
        return hi

    return -1


def is_in_ordered_list(n, ordered_list):      # binary search
    index = index_in_ordered_list(n, ordered_list)
    if index < 0:
        return False
    else:
        return True


# = Factor Procedures ================================
def get_factors(num):        # Valid for num > 1
    result = [1]
    if num > 1:
        hiresult = [num]
    else:
        hiresult = []
    maxcheck = int(math.sqrt(num))+1
    for n in range(2, maxcheck):
        if num % n == 0:
            n2 = int(num/n)
            result.append(n)
            if n != n2:
                hiresult.insert(0, n2)
    result.extend(hiresult)
    return result


# def get_prime_factors(num, prime_list): below in Prime Procedures section


# = Prime Procedures =================================
def sieve_erathosthenes(n):
    bool_table = [True]*(n+1)
    bool_table[0] = False
    bool_table[1] = False

    if n == 2:
        prime_list = [2]
    elif n == 3:
        prime_list = [2, 3]
    else:
        prime_list = []
        sqrtn = int(math.sqrt(n))
        for i in range(2, sqrtn+1):
            if bool_table[i]:
                prime_list.append(i)
                for j in range(i**2, n+1, i):
                    bool_table[j] = False

        if sqrtn % 2 == 0:
            sqrtn += 1
        else:
            sqrtn += 2
        for i in range(sqrtn, n+1, 2):
            if bool_table[i]:
                prime_list.append(i)

    return prime_list


def get_prime_factors(num, prime_list):
    if is_in_ordered_list(num, prime_list):
        result = [num]
    else:
        result = []
        hiresult = []
        maxcheck = int(math.sqrt(num))+1
        for n in range(2, maxcheck):
            if num % n == 0:
                n2 = num/n
                if is_in_ordered_list(n, prime_list):
                    result.append(n)
                if is_in_ordered_list(n2, prime_list) and (n != n2):
                    hiresult.insert(0, num/n)
        result.extend(hiresult)
    return result


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    # Check sieve_erathosthenes()
    print()
    for n in range(2, 11):
        print(n, sieve_erathosthenes(n))

    # Time Check index_in_ordered_list()
    ordered_list = [z for z in range(10000)]
    time_count = 1000

    start = timer()
    for z in range(time_count):
        time_ans = index_in_ordered_list(921, ordered_list)
    time1 = timer()
    for z in range(time_count):
        time_ans = ordered_list.index(921)
    time2 = timer()

    print()
    print(time1-start)  # in ms
    print(time2-time1)  # in ms

    # Time Check is_in_ordered_list()
    start = timer()
    for z in range(time_count):
        time_ans = is_in_ordered_list(921, ordered_list)
    time1 = timer()
    for z in range(time_count):
        time_ans = 921 in ordered_list
    time2 = timer()

    print()
    print(time1-start)  # in ms
    print(time2-time1)  # in ms

