#!/usr/bin/python3
""" Make Change
"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to meet a given amount
    total.
    """
    if coins and total > 0:
        coins.sort(reverse=True)
        counter = 0

        for coin in coins:
            counter += total // coin
            total = total % coin

        if total == 0:
            return counter
        else:
            return -1
    elif len(coins) == 0:
        return -1

    return 0
