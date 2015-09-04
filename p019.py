""" Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September, April, June and November.
    All the rest have thirty-one,
    Saving February alone, which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
      but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""


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


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    curr_date = {'month': 1, 'day': 1, 'year': 1900, 'weekday': 1}      # 1/1/1900, Monday
    for n in range(12):
        increment_month(curr_date)
        print(curr_date)

    start_date = {'month': 7, 'day': 1, 'year': 2015, 'weekday': 3}     # 7/1/2015, Wednesday
    stop_date = {'month': 6, 'day': 25, 'year': 2016, 'weekday': 6}     # 6/25/2016, Saturday
    print(count_weekdays(start_date, 0, stop_date), start_date)

    start_date = {'month': 1, 'day': 1, 'year': 1901, 'weekday': 2}     # 1/1/1901, Tuesday
    stop_date = {'month': 12, 'day': 31, 'year': 2000, 'weekday': 0}    # 12/31/2000, Sunday
    print(count_weekdays(start_date, 0, stop_date), start_date)
