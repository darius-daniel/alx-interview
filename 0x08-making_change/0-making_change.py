#!/usr/bin/python3
""" Make Change
"""
from typing import List


def makeChange(coins: List, total: int) -> int:
    """ Determines the fewest number of coins needed to meet a given amount
    total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=true)
    counter = 0

    while total > 0:
        for idx, coin in enumerate(coins):
            if coin <= total:
                total -= coin
                break

        if idx == len(coins) - 1 and total > 0:
            return -1
        counter += 1
        
    return counter
            