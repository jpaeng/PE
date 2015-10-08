
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
def get_proper_divisors(num):   # Valid for num > 1
    """ Return list of all proper divisors of num.  Proper divisors are the same as factors except does not include num itself."""
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
    elif num%2 == 0:
        return False
    else:
        maxcheck = int(math.sqrt(num))+1
        for n in range(3, maxcheck, 2):
            if num%n == 0:
                return False
        return True


def sieve_erathosthenes(n):
    """ Return ordered list of primes up to n."""
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
def lexi_perm(n, digits):
    """ Return the nth permutation of digit_count digits."""
    digit_count = len(digits)
    result = ''
    remainder = n
    for position in range(digit_count-1, -1, -1):       # Start with msb and loop to lsb
        divisor = math.factorial(position)              # Factorials:  1 2 6 24 120 ...
        dividend = int(remainder/divisor)               # Determine which digit in list is next
        remainder = remainder % divisor                 # Remainder calculated for next loop
        result += digits[dividend]                      # Extend string to right
        digits = digits.replace(digits[dividend], '')   # Remove digit just used from list
    return result

# = Check Common Functions ===========================
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    # Check get_proper_divisors()
    print('Check get_proper_divisors()')
    print(12, get_proper_divisors(12))

    # Check get_factors()
    print('Check get_factors()')
    print(12, get_factors(12))

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

    # Check sieve_erathosthenes()
    print()
    for z in range(2, 11):
        print(z, sieve_erathosthenes(z))

    # Check get_factors()
    print('Check get_prime_factors()')
    zprime_list = sieve_erathosthenes(100)
    print(24, get_prime_factors(24, zprime_list))


    # Check reduce_fraction()
    print()
    y = 6
    for z in range(1, 13):
        print(y, z, reduce_fraction(y, z))
