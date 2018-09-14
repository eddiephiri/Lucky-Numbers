# This module tallies the numbers picked by users in the numbers game
# The tally method accepts a list of lists and tallies the numbers in each ticket


def tally(arr):
    d = dict()

    for ticket in arr:
        for num in ticket:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
    return d

