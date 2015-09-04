""" Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

    3
   7 4
  2 4 6
 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)

"""


text_triangle = '\
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


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    triangle = format_list_triangle(text_triangle)
    sum_triangle = max_sum_triangle(triangle)

    # print original triangle
    print()
    for n in range(len(triangle)):
        print(triangle[n])

    # print max sum triangle
    print()
    for n in range(len(sum_triangle)):
        print(sum_triangle[n])

    # print the maximum sum from the bottom row
    print()
    print(max(sum_triangle[len(sum_triangle)-1]))
