""" Project Euler Problems 10-19
"""


import math
import common

from timeit import default_timer as timer


# Problem 10:  Sum of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def sum_of_primes(n):
    prime_list = common.sieve_erathosthenes(n)
    return sum(prime_list)


# Problem 11:  Greatest Product of Adjacent Numbers
# In the 20x20 grid below, what is the greatest product of four adjacent numbers
# in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?

def text_to_grid(text, xsize, ysize):
    grid_list = text.split(" ")
    for index in range(len(grid_list)):
        grid_list[index] = int(grid_list[index])
    grid = []
    for index in range(0, xsize*ysize, ysize):
        grid.append(grid_list[index:index+xsize])
    return grid


def greatest_n_adjacent_product(grid, xsize, ysize, product_count):
    max_product = -1
    for x in range(xsize-product_count+1):
        for y in range(ysize-product_count+1):
            if grid[x][y] > 0:
                products = [grid[x][y]]*3
                for i in range(1, product_count):
                    products[0] *= grid[x+i][y]     # right product
                    products[1] *= grid[x][y+i]     # down product
                    products[2] *= grid[x+i][y+i]   # right diagonal product
                max_product = max(max_product, max(products))
    for x in range(product_count-1, xsize):
        for y in range(ysize-product_count+1):
            if grid[x][y] > 0:
                product = grid[x][y]
                for i in range(1, product_count):
                    product *= grid[x-i][y+i]       # left diagonal product
                max_product = max(max_product, product)
    y = ysize-1     # last row
    for x in range(xsize-product_count+1):
        if grid[x][y] > 0:
            product = grid[x][y]
            for i in range(1, product_count):
                product *= grid[x+i][y]     # right product
            max_product = max(max_product, product)
    x = xsize-1     # last column
    for y in range(ysize-product_count+1):
        if grid[x][y] > 0:
            product = grid[x][y]
            for i in range(1, product_count):
                product *= grid[x][y+i]     # down product
            max_product = max(max_product, product)

    return max_product


# Problem 12:  Triangle Number Divisors
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

def triangle_number_with_n_divisors(target_factor_count):
    triangle_num = 0
    n = 0
    while True:
        n += 1
        triangle_num += n
        factors = common.get_factors(triangle_num)
        if len(factors) > target_factor_count:
            break
    return triangle_num, factors


# Problem 13:  MSB Sum of 50-digit Numbers
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def sum_msb_digits(str_list, n):
    """ Return the left n digits of the sum of str_list. """
    total = sum(int(str_num[:n]) for str_num in str_list)
    return total


# Problem 14:  Collatz Sequence Problem
# The following iterative sequence is defined for the set of positive integers:
#     n -> n/2 (n is even)
#     n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#     13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz_sequence(n):
    """Return Collatz Sequence for n as a list. """
    col_list = [n]
    while n > 1:
        if n % 2:   # odd
            n = 3*n + 1
        else:       # even
            n = int(n/2)
        col_list.append(n)
    return col_list


def longest_collatz_sequence(upper_limit):
    """Return number (bound by upper_limit) with longest Collatz Sequence. """
    max_start = -1
    max_length = -1
    for n in range(1, upper_limit + 1):
        length = len(collatz_sequence(n))
        if max_length < length:
            max_length = length
            max_start = n
    return max_start


# Problem 15:  Lattice Paths
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

def lattice_path_count_recursive(position):
    """Returns number of routes to bottom right corner (0, 0) from current position. """
    if position[0] == 0:
        path_count = 1
    elif position[1] == 0:
        path_count = 1
    else:
        path_count = lattice_path_count_recursive((position[0] - 1, position[1]))
        path_count += lattice_path_count_recursive((position[0], position[1] - 1))

    return path_count


def lattice_path_count_formula(grid_size):
    """Returns number of lattice paths in a grid_size grid. """
    path_node_count = 2*grid_size - 1   # the number of nodes in each path
    path_count = int(2*math.factorial(path_node_count)/(math.factorial(grid_size)*math.factorial(grid_size-1)))
    return path_count


# Problem 16:  Power Digit Sum
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?

# See power_digit_sum(num, pwr) in common.py


# Problem 17:  Number Letter Counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

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
        letter_count = 0
    elif stripped_num < 10:
        letter_count = ones_count[stripped_num]
    elif stripped_num < 20:
        letter_count = teens_count[stripped_num]
    else:
        letter_count = tens_count[int(stripped_num/10)]
        stripped_num = num - 10*int(num/10)
        if stripped_num > 0:
            letter_count += ones_count[stripped_num]

    # Hundreds
    if num >= 100:
        if letter_count > 0:
            letter_count += 3      # account for 'and'
        stripped_num = num - 1000*int(num/1000)        # strip off thousands
        if stripped_num > 0:
            letter_count += ones_count[int(stripped_num/100)] + 7   # 'hundred' = 7

        # Thousands
        if num >= 1000:
            stripped_num = num - 10000*int(num/10000)      # strip off anything over 9999
            if stripped_num > 0:
                letter_count += ones_count[int(stripped_num/1000)] + 8  # 'thousand' = 8

    return letter_count


def number_letter_count_text(num):
    """Return the letter_count of letters when num is spelled out. Text conversion algorithm"""
    if num > 19:
        str_num = str(num)
        length = len(str_num)
        digit_list = [int(str_num[i]) for i in range(length-1, -1, -1)]

    # Tens, ones
    stripped_num = num - 100*int(num/100)  # strip off thousands, hundreds
    if stripped_num < 1:
        letter_count = 0
    elif stripped_num < 10:
        letter_count = ones_count[stripped_num]
    elif stripped_num < 20:
        letter_count = teens_count[stripped_num]
    else:
        letter_count = tens_count[digit_list[1]]
        letter_count += ones_count[digit_list[0]]

    # Hundreds
    if num >= 100:
        if letter_count > 0:
            letter_count += 3      # account for 'and'
        letter_count += ones_count[digit_list[2]] + 7   # 'hundred' = 7

        # Thousands
        if num >= 1000:
            letter_count += ones_count[digit_list[3]] + 8  # 'thousand' = 8

    return letter_count


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


# Problem 18:  Maximum Path Sum I
# 
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
# 
#     3
#    7 4
#   2 4 6
#  8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom of the triangle below:
# 
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
# it cannot be solved by brute force, and requires a clever method! ;o)

def format_list_triangle(text):
    """Return a 2D list representing a triangle formed from space separated numbers in input text."""
    text_list = text.split(' ')
    num_list = [int(text_list[n]) for n in range(len(text_list))]
    tria_list = []
    row = 0
    while True:
        row += 1        # row length = row number
        remaining = len(num_list)
        if row < remaining:
            tria_list.append(num_list[:row])
            num_list = num_list[row:]
        elif row == remaining:
            tria_list.append(num_list)
            break
        else:
            break
    return tria_list


def max_sum_triangle(tria_list):
    """Return a triangle with the maximum sum of previous rows at each node."""
    sum_tria_list = [tria_list[0]]                  # row 0
    sum_tria_list.append([tria_list[1][0] + tria_list[0][0], tria_list[1][1] + tria_list[0][0]])    # row 1
    for row in range(2, len(tria_list)):            # row 2-
        sum_row = []
        sum_row.append(tria_list[row][0] + sum_tria_list[row-1][0])
        for i in range(1, row):
            # add the higher of the two numbers in the previous row to the current node
            sum_row.append(tria_list[row][i] + max(sum_tria_list[row-1][i-1], sum_tria_list[row-1][i]))
        sum_row.append(tria_list[row][row] + sum_tria_list[row-1][row-1])
        sum_tria_list.append(sum_row)
    return sum_tria_list


# Problem 19:  Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
#     1 Jan 1900 was a Monday.
#     Thirty days has September, April, June and November.
#     All the rest have thirty-one,
#     Saving February alone, which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4,
#       but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def increment_month(date):
    """ Increment date={'month':, 'day':, 'year':, 'weekday':} by one month.
        0 = Sunday
        1 = Monday
        2 = Tuesday
        3 = Wednesday
        4 = Thursday
        5 = Friday
        6 = Saturday
    """
    # TODO ERROR CONDITIONS
    if date['month'] in [4, 6, 9, 11]:          # 30-day months
        date['month'] += 1
        date['weekday'] = (date['weekday']+2) % 7
    elif date['month'] in [1, 3, 5, 7, 8, 10]:  # 31-day months except December
        date['month'] += 1
        date['weekday'] = (date['weekday']+3) % 7
    elif date['month'] == 2:                    # February
        date['month'] += 1
        if (date['year'] % 400) == 0:   # 29 days
            date['weekday'] = (date['weekday']+1) % 7
        elif (date['year'] % 100) == 0: # 28 days
            pass
        elif (date['year'] % 4) == 0:   # 29 days
            date['weekday'] = (date['weekday']+1) % 7
        else:                           # 28 days
            pass
    else:                                       # December
        date['year'] += 1
        date['month'] = 1
        date['weekday'] = (date['weekday']+3) % 7


def count_weekdays(date, weekday, end_date):
    """Return count of 'weekday's occurring between date and end_date for the same day-of-the-month as begin_date."""

    if end_date['day'] < date['day']:   # Stop one month ahead if month increments will overshoot
        end_month = end_date['month'] - 1
    else:
        end_month = end_date['month']

    count = 0
    while date['year'] < end_date['year']:
        increment_month(date)
        if date['weekday'] == weekday:
            count += 1
        # print(count, date)

    while date['month'] < end_month:
        increment_month(date)
        if date['weekday'] == weekday:
            count += 1
        # print(count, date)

    return count


# Problem 10-19 Checks
if __name__ == '__main__':  # only if run as a script, skip when imported as module
    problem_num = 19

    if problem_num == 10:
        print(sum_of_primes(10))
        print(sum_of_primes(2000000))
    elif problem_num == 11:
        pr11_grid_text = '\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

        pr11_grid = text_to_grid(pr11_grid_text, 20, 20)
        print(greatest_n_adjacent_product(pr11_grid, 20, 20, 4))
    elif problem_num == 12:
        z, factor_list = triangle_number_with_n_divisors(5)
        print(z, len(factor_list), factor_list)
        z, factor_list = triangle_number_with_n_divisors(500)
        print(z, len(factor_list))
    elif problem_num == 13:
        pr13_nlist_string = '\
37107287533902102798797998220837590246510135740250 \
46376937677490009712648124896970078050417018260538 \
74324986199524741059474233309513058123726617309629 \
91942213363574161572522430563301811072406154908250 \
23067588207539346171171980310421047513778063246676 \
89261670696623633820136378418383684178734361726757 \
28112879812849979408065481931592621691275889832738 \
44274228917432520321923589422876796487670272189318 \
47451445736001306439091167216856844588711603153276 \
70386486105843025439939619828917593665686757934951 \
62176457141856560629502157223196586755079324193331 \
64906352462741904929101432445813822663347944758178 \
92575867718337217661963751590579239728245598838407 \
58203565325359399008402633568948830189458628227828 \
80181199384826282014278194139940567587151170094390 \
35398664372827112653829987240784473053190104293586 \
86515506006295864861532075273371959191420517255829 \
71693888707715466499115593487603532921714970056938 \
54370070576826684624621495650076471787294438377604 \
53282654108756828443191190634694037855217779295145 \
36123272525000296071075082563815656710885258350721 \
45876576172410976447339110607218265236877223636045 \
17423706905851860660448207621209813287860733969412 \
81142660418086830619328460811191061556940512689692 \
51934325451728388641918047049293215058642563049483 \
62467221648435076201727918039944693004732956340691 \
15732444386908125794514089057706229429197107928209 \
55037687525678773091862540744969844508330393682126 \
18336384825330154686196124348767681297534375946515 \
80386287592878490201521685554828717201219257766954 \
78182833757993103614740356856449095527097864797581 \
16726320100436897842553539920931837441497806860984 \
48403098129077791799088218795327364475675590848030 \
87086987551392711854517078544161852424320693150332 \
59959406895756536782107074926966537676326235447210 \
69793950679652694742597709739166693763042633987085 \
41052684708299085211399427365734116182760315001271 \
65378607361501080857009149939512557028198746004375 \
35829035317434717326932123578154982629742552737307 \
94953759765105305946966067683156574377167401875275 \
88902802571733229619176668713819931811048770190271 \
25267680276078003013678680992525463401061632866526 \
36270218540497705585629946580636237993140746255962 \
24074486908231174977792365466257246923322810917141 \
91430288197103288597806669760892938638285025333403 \
34413065578016127815921815005561868836468420090470 \
23053081172816430487623791969842487255036638784583 \
11487696932154902810424020138335124462181441773470 \
63783299490636259666498587618221225225512486764533 \
67720186971698544312419572409913959008952310058822 \
95548255300263520781532296796249481641953868218774 \
76085327132285723110424803456124867697064507995236 \
37774242535411291684276865538926205024910326572967 \
23701913275725675285653248258265463092207058596522 \
29798860272258331913126375147341994889534765745501 \
18495701454879288984856827726077713721403798879715 \
38298203783031473527721580348144513491373226651381 \
34829543829199918180278916522431027392251122869539 \
40957953066405232632538044100059654939159879593635 \
29746152185502371307642255121183693803580388584903 \
41698116222072977186158236678424689157993532961922 \
62467957194401269043877107275048102390895523597457 \
23189706772547915061505504953922979530901129967519 \
86188088225875314529584099251203829009407770775672 \
11306739708304724483816533873502340845647058077308 \
82959174767140363198008187129011875491310547126581 \
97623331044818386269515456334926366572897563400500 \
42846280183517070527831839425882145521227251250327 \
55121603546981200581762165212827652751691296897789 \
32238195734329339946437501907836945765883352399886 \
75506164965184775180738168837861091527357929701337 \
62177842752192623401942399639168044983993173312731 \
32924185707147349566916674687634660915035914677504 \
99518671430235219628894890102423325116913619626622 \
73267460800591547471830798392868535206946944540724 \
76841822524674417161514036427982273348055556214818 \
97142617910342598647204516893989422179826088076852 \
87783646182799346313767754307809363333018982642090 \
10848802521674670883215120185883543223812876952786 \
71329612474782464538636993009049310363619763878039 \
62184073572399794223406235393808339651327408011116 \
66627891981488087797941876876144230030984490851411 \
60661826293682836764744779239180335110989069790714 \
85786944089552990653640447425576083659976645795096 \
66024396409905389607120198219976047599490197230297 \
64913982680032973156037120041377903785566085089252 \
16730939319872750275468906903707539413042652315011 \
94809377245048795150954100921645863754710598436791 \
78639167021187492431995700641917969777599028300699 \
15368713711936614952811305876380278410754449733078 \
40789923115535562561142322423255033685442488917353 \
44889911501440648020369068063960672322193204149535 \
41503128880339536053299340368006977710650566631954 \
81234880673210146739058568557934581403627822703280 \
82616570773948327592232845941706525094512325230608 \
22918802058777319719839450180888072429661980811197 \
77158542502016545090413245809786882778948721859617 \
72107838435069186155435662884062257473692284509516 \
20849603980134001723930671666823555245252804609722 \
53503534226472524250874054075591789781264330331690'
        pr13_nlist_strlist = pr13_nlist_string.split(' ')
        for z in range(1, 14):
            print(z, sum_msb_digits(pr13_nlist_strlist, z))
        print('00', 12345678901234567890)
    elif problem_num == 14:
        for z in range(1, 16):
            print(collatz_sequence(z))
        print()
        max_collatz = longest_collatz_sequence(999999)
        print(max_collatz, len(collatz_sequence(max_collatz)))
    elif problem_num == 15:
        for z in range(1, 11):
            print("{0}x{0}:".format(z), lattice_path_count_recursive((z, z)), lattice_path_count_formula(z))
        print()
        print("20x20:", lattice_path_count_formula(20))
    elif problem_num == 16:
        for z in range(16):
            print(z, 2**z, common.power_digit_sum(2, z))
        print()
        print(1000, common.power_digit_sum(2, 1000))
    elif problem_num == 17:
        for z in range(1, 22):
            print(z, number_letter_count_math(z), number_letter_count_text(z))
        z = 342
        print(z, number_letter_count_math(z), number_letter_count_text(z))
        z = 115
        print(z, number_letter_count_math(z), number_letter_count_text(z))
    
        print()
        print(sum_of_number_letter_counts_math(5))
        print(sum_of_number_letter_counts_math(342))
        print(sum_of_number_letter_counts_math(1000))
    
        # Time Check
        print()
        z_count = 1000
        start = timer()
        for z in range(z_count):
            sum_of_number_letter_counts_math(z_count)
        time1 = timer()
        for z in range(z_count):
            sum_of_number_letter_counts_text(z_count)
        time2 = timer()
    
        print(time1-start)  # in ms
        print(time2-time1)  # in ms
    elif problem_num == 18:
        pr18_text_triangle = '\
75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

        pr18_triangle = format_list_triangle(pr18_text_triangle)
        pr18_sum_triangle = max_sum_triangle(pr18_triangle)
    
        # print original triangle
        print()
        for z in range(len(pr18_triangle)):
            print(pr18_triangle[z])
    
        # print max sum triangle
        print()
        for z in range(len(pr18_sum_triangle)):
            print(pr18_sum_triangle[z])
    
        # print the maximum sum from the bottom row
        print()
        print(max(pr18_sum_triangle[len(pr18_sum_triangle)-1]))
    elif problem_num == 19:
        curr_date = {'month': 1, 'day': 1, 'year': 1900, 'weekday': 1}      # 1/1/1900, Monday
        for z in range(12):
            increment_month(curr_date)
            print(curr_date)
    
        start_date = {'month': 7, 'day': 1, 'year': 2015, 'weekday': 3}     # 7/1/2015, Wednesday
        stop_date = {'month': 6, 'day': 25, 'year': 2016, 'weekday': 6}     # 6/25/2016, Saturday
        print(count_weekdays(start_date, 0, stop_date), start_date)
    
        start_date = {'month': 1, 'day': 1, 'year': 1901, 'weekday': 2}     # 1/1/1901, Tuesday
        stop_date = {'month': 12, 'day': 31, 'year': 2000, 'weekday': 0}    # 12/31/2000, Sunday
        print(count_weekdays(start_date, 0, stop_date), start_date)
