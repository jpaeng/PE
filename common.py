
import math
from timeit import default_timer as timer


# = File Procedures =================================
def read_single_line_text_file(file_name, remove_chr='"', split_delimiter=','):
    in_file = open(file_name)
    str_list = (in_file.read().replace(remove_chr,'')).split(split_delimiter)
    in_file.close()
    return str_list


def read_multi_line_text_file(file_name):
    in_file = open(file_name)
    rows = [line.rstrip() for line in in_file]
    in_file.close()
    return rows


# = String Procedures ===============================
def power_digit_sum(num, pwr):
    """Return the sum of the digits in the answer to num^pwr."""
    str_ans = str(num**pwr)
    sum_dig = sum(int(str_ans[i]) for i in range(len(str_ans)))
    return sum_dig


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


# = List Array Procedures ============================
def sort_2d_array(array, index=0):
    len_array = len(array)
    switched = True
    while(switched):
        switched = False
        for i in range(len_array-1):
            if array[i][index] > array[i+1][index]:
                array[i], array[i+1] = array[i+1], array[i]
                switched = True
    return array


def count_in_array(element, array):
    """Return count of elements in array. List can be any dimension > 1"""
    dim_count = 0           # dim_count = number of dimensions of the array
    dim_size = []           # dim_size = array size in each dimension
    temp_array = array
    while isinstance(temp_array, (list, tuple)):
        dim_count += 1
        dim_size.append(len(temp_array))
        temp_array = temp_array[0]

    count = 0
    coord = [0]*(dim_count-1)
    coord[0] = -1
    while True:
        increment_next_level = True
        for dim in range(dim_count-1):
            if increment_next_level:
                if coord[dim] == dim_size[dim]-1:
                    coord[dim] = 0
                else:
                    coord[dim] += 1
                    increment_next_level = False
        if increment_next_level:
            break
        temp_array = array
        for dim in range(dim_count-1):
            temp_array = temp_array[coord[dim]]
        count += temp_array.count(element)

    return count


def coords_in_array(element, array):
    """Return list of array coordinates containing element. List can be any dimension > 1"""
    dim_count = 0           # dim_count = number of dimensions of the array
    dim_size = []           # dim_size = array size in each dimension
    temp_array = array
    while isinstance(temp_array, (list, tuple)):
        dim_count += 1
        dim_size.append(len(temp_array))
        temp_array = temp_array[0]

    results = []
    coord = [0]*dim_count
    coord[0] = -1
    while True:
        increment_next_level = True
        for dim in range(dim_count):
            if increment_next_level:
                if coord[dim] == dim_size[dim]-1:
                    coord[dim] = 0
                else:
                    coord[dim] += 1
                    increment_next_level = False
        if increment_next_level:
            break
        temp_array = array
        for dim in range(dim_count):
            temp_array = temp_array[coord[dim]]
        if temp_array == element:
            results.append(list(coord))

    return results


# = Factor Procedures ================================
def get_proper_divisors(num):   # Valid for num > 1
    """ Return list of all proper divisors of num.
        Proper divisors are the same as factors except does not include num itself."""
    result = [1]
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


def get_factors(num):        # Valid for num > 1
    """Return list of all factors of num, including num itself."""
    result = get_proper_divisors(num)
    if num > 1:
        result.append(num)
    return result


# def get_prime_factors(num, prime_list): below in Prime Procedures section


# = Prime Procedures =================================
def is_prime(num):
    """Return True or False depending on whether num is prime."""
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        maxcheck = int(math.sqrt(num))+1
        for n in range(3, maxcheck, 2):
            if num % n == 0:
                return False
        return True


def is_prime_mr(n):
    """Return True or False depending on whether num is prime. Uses Miller-Rabin primality test."""
    if (n < 2) or (n%2 == 0):
        flag = False
    elif n == 2:
        flag = True
    else:
        flag = True
        r = 0
        d = n-1
        if n < 2047:
            a_list = [2]
        elif n < 1373653:
            a_list = [2, 3]
        elif n < 9080191:
            a_list = [31, 73]
        elif n < 25326001:
            a_list = [2, 3, 5]
        elif n < 3215031751:
            a_list = [2, 3, 5, 7]
        elif n < 4759123141:
            a_list = [2, 7, 61]
        elif n < 1122004669633:
            a_list = [2, 13, 23, 1662803]
        elif n < 2152302898747:
            a_list = [2, 3, 5, 7, 11]
        elif n < 3474749660383:
            a_list = [2, 3, 5, 7, 11, 13]
        else:       # if n < 341550071728321:
            a_list = [2, 3, 5, 7, 11, 13, 17]

        while(d%2 == 0):
            r += 1
            d = d // 2

        for a in a_list:
            x = pow(a, d, n)
            if (x == 1) or (x == n-1):
                continue
            for i in range(r-1):
                x = pow(x, 2, n)
                if x == 1:
                    flag = False
                    break
                if x == n-1:
                    break
            else:
                flag = False
                break
    return flag

def prime_list_mr(n):
    """ Return ordered list of primes up to n. Uses Miller-Rabin primality test."""
    prime_list = [2]
    for i in range(n+1):
        if is_prime_mr(i):
            prime_list.append(i)
    return prime_list

def sieve_erathosthenes(n):
    """ Return ordered list of primes up to n. Maximum n is around 2*10**8"""
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


def sieve_erathosthenes2(n, block_size = None):
    """ Return ordered list of primes up to n. Test up to 10**9. Takes a long time."""
    if block_size is None:
        block_size = 10**8
    if n < 2:
        prime_list = []
    elif n == 2:
        prime_list = [2]
    else:
        prime_list = [2, 3]

        if n <= block_size:
            sieve_e_by_section(prime_list, n)
        else:
            for i in range(block_size, n, block_size):
                sieve_e_by_section(prime_list, i)
            sieve_e_by_section(prime_list, n)

    return prime_list


def sieve_e_by_section(prime_list, n):
    """ Return ordered list of primes up to n."""
    last_prime = prime_list[-1]
    table_count = n-last_prime+1
    bool_table = [True]*table_count
    sqrtn = int(math.sqrt(n))
    if sqrtn % 2 == 0:
        sqrtn += 1
    else:
        sqrtn += 2
    
    for p in prime_list:
        start_i = p * ( 1 + int(last_prime/p)) - last_prime
        for i in range(start_i, table_count, p):
            bool_table[i] = False

    if sqrtn > last_prime:
        for i in range(1, sqrtn - last_prime + 1):
            if bool_table[i]:
                p = last_prime + i
                prime_list.append(p)
                start_j = p**2 - last_prime
                for j in range(start_j, table_count, p):
                    bool_table[j] = False
            
        start_i = sqrtn - last_prime + 2
        for i in range(start_i, table_count, 2):
            if bool_table[i]:
                p = last_prime + i
                prime_list.append(p)
    else:
        for i in range(2, table_count, 2):
            if bool_table[i]:
                p = last_prime + i
                prime_list.append(p)

    return prime_list


def get_prime_factors(num, prime_list):
    """ Return list of prime factors of num. Prime_list must be ordered."""
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


# = Fraction Procedures ==============================
def reduce_fraction(num, den):
    """Return tuple of num and den reduced to lowest common terms."""
    prime_list = sieve_erathosthenes(max(num, den))
    num_factor_list = get_prime_factors(num, prime_list)
    den_factor_list = get_prime_factors(den, prime_list)

    for num_factor in num_factor_list:
        if num_factor in den_factor_list:
            while True:
                num /= num_factor
                den /= num_factor
                if(num % num_factor) or (den % num_factor):
                    break
    return int(num), int(den)


# = Palindrome Procedures ============================
def is_str_palindrome(string):
    length = len(string)
    if length < 2:
        return True
    else:
        if string[0] == string[-1]:
            return is_str_palindrome(string[1:-1])
        else:
            return False


# = Pandigital Procedures ============================
def is_pandigital(str_n, str_digits):
    for c in str_digits:
        if str_n.count(c) != 1:
            return False
    return True


# = Combinations/Permutation Procedures ==============
def combinations(n, k):
    """Return C(n, k)."""
    return math.factorial(n)//math.factorial(k)//math.factorial(n-k)


def permutations(n, k):
    """Return P(n, k)."""
    return math.factorial(n)//math.factorial(n-k)


def next_combination(x):
    u = x & -x
    v = u + x
    if v == 0:
        return 0
    x = v + (((v^x)//u)>>2)
    return x


def generate_combinations_list(n, k):
    """ Return list of combinations of n-items take k at a time.

    Each item represented by an integer (0, 1, ...) which can be used as an index into a master list of items.
    :param n:   number of different items
    :param k:   number of items in each combination
    :return:    list of combinations in the form [(a00, a01, a02, ..., a0k), (...), ...]
    """

    combination_list = []
    binary_combination = 2**k-1
    combination_count = combinations(n, k)
    for loop in range(combination_count):
        combination = []
        for bit_position in range(n):
            if (1<<bit_position) & binary_combination:
                combination.append(bit_position)
        combination_list.append(tuple(combination))
        binary_combination = next_combination(binary_combination)
    return combination_list


def nth_permutation(n, element_list):
    """ Return the nth permutation of element_list."""
    element_count = len(element_list)
    result = []
    remainder = n
    for position in reversed(range(element_count)):     # Start with msb and loop to lsb
        divisor = math.factorial(position)              # Factorials:  1 2 6 24 120 ...
        dividend = int(remainder/divisor)               # Determine which digit in list is next
        remainder = remainder % divisor                 # Remainder calculated for next loop
        result.append(element_list[dividend])           # Extend string to right
        if dividend < len(element_list) - 1:               # Remove char just used from list
            element_list = element_list[:dividend] + element_list[dividend+1:]
        else:
            element_list = element_list[:dividend]
    return result


def str_permutation(n, str_chars):
    """ Return the nth permutation of char_count str_chars."""
    char_count = len(str_chars)
    result = ''
    remainder = n
    for position in range(char_count-1, -1, -1):        # Start with msb and loop to lsb
        divisor = math.factorial(position)              # Factorials:  1 2 6 24 120 ...
        dividend = int(remainder/divisor)               # Determine which digit in list is next
        remainder = remainder % divisor                 # Remainder calculated for next loop
        result += str_chars[dividend]                   # Extend string to right
        if dividend < len(str_chars) - 1:               # Remove char just used from list
            str_chars = str_chars[:dividend] + str_chars[dividend+1:]
        else:
            str_chars = str_chars[:dividend]
    return result


def is_permutation(str1, str2):
    """Return whether the characters of str1 and str2 are permutations of each other."""
    result = True
    if len(str1) != len(str2):
        result = False
    else:
        for c in str1:
            if str1.count(c) != str2.count(c):
                result = False
                break
    return result


def is_sub_permutation(str1, str2):
    """Return whether the characters of str1 is a substring permutation of str2."""
    result = True
    if len(str1) > len(str2):
        result = False
    else:
        for c in str1:
            if str1.count(c) > str2.count(c):
                result = False
                break
    return result


# = Check Common Functions ===========================
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    # Check get_proper_divisors()
    print()
    print('Check get_proper_divisors()')
    print(12, get_proper_divisors(12))

    # Check get_factors()
    print()
    print('Check get_factors()')
    print(12, get_factors(12))

    # Time Check index_in_ordered_list()
    print()
    print('Time Check index_in_ordered_list()')
    z_ordered_list = [z for z in range(10000)]
    time_count = 1000

    start = timer()
    for z in range(time_count):
        time_ans = index_in_ordered_list(921, z_ordered_list)
    time1 = timer()
    for z in range(time_count):
        time_ans = z_ordered_list.index(921)
    time2 = timer()

    print()
    print(time1-start)  # in ms
    print(time2-time1)  # in ms

    # Time Check is_in_ordered_list()
    print()
    print('Time Check is_in_ordered_list()')
    start = timer()
    for z in range(time_count):
        time_ans = is_in_ordered_list(921, z_ordered_list)
    time1 = timer()
    for z in range(time_count):
        time_ans = 921 in z_ordered_list
    time2 = timer()

    print()
    print(time1-start)  # in ms
    print(time2-time1)  # in ms

    # Check array procedures
    print()
    print('Check coords_in_array(), count_in_array()')
    zlist = [z for z in range(12)]
    zlist = [zlist[z:z+3] for z in range(4)]
    print(zlist)
    print(sum(zlist1.count(2) for zlist1 in zlist))
    for z in range(6):
        print(z, coords_in_array(z, zlist))
    zlist = [zlist]*5
    print(zlist)
    for z in range(7):
        print(z, coords_in_array(z, zlist))
    for z in range(7):
        print(z, count_in_array(z, zlist))

    # Time Check array procedures
    print()
    print('Time Check count_in_array(), coords_in_array()')
    zlist = [z for z in range(60)]
    zlist = [zlist[z:z+10] for z in range(10)]
    zlist = [zlist]*5
    time_count = 1000

    start = timer()
    for z in range(time_count):
        time_ans = count_in_array(150, zlist)
    time1 = timer()
    for z in range(time_count):
        time_ans = coords_in_array(150, zlist)
    time2 = timer()

    print()
    print(time1-start)  # in ms
    print(time2-time1)  # in ms

    # Check next_combination()
    print()
    print('Check next_combination()')
    zresult = 31
    for z in range(10):
        zresult = next_combination(zresult)
        print(bin(zresult))

    # Check generate_combinations_list()
    print()
    print('Check generate_combinations_list()')
    zresult = generate_combinations_list(10, 5)
    print(zresult)

    # Check nth_permutation()
    zlist = [i for i in range(1, 5)]
    z_bit_count = len(zlist)
    print()
    print('Check nth_permutation()')
    for z in range(math.factorial(z_bit_count)):
        print(z, nth_permutation(z, zlist))

    # Check str_permutation()
    z_bit_count = 4
    print()
    print('Check str_permutation()')
    for z in range(math.factorial(z_bit_count)):
        print(z, str_permutation(z, '1234'))

    print()
    print('Check lexi_perm_duplicate_digits()')
    for z in range(math.factorial(z_bit_count)):
        print(z, str_permutation(z, '1040'))

    # Check sieve_erathosthenes()
    print()
    print('Check sieve_erathosthenes()')
    for z in range(2, 11):
        print(z, sieve_erathosthenes(z))
    z = 1000
    print(z, sieve_erathosthenes(z))
    print(z, sieve_erathosthenes2(z, 100))
    print(z, prime_list_mr(z))

    # Check get_factors()
    print()
    print('Check get_prime_factors()')
    zprime_list = sieve_erathosthenes(100)
    print(24, get_prime_factors(24, zprime_list))

    # Check reduce_fraction()
    print()
    print('Check reduce_fraction()')
    y = 6
    for z in range(1, 13):
        print(y, z, reduce_fraction(y, z))
