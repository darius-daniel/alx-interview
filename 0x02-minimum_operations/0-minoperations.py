#!/usr/bin/python3
"""
0. Minimum Operations
"""
from copy import deepcopy


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly n H
    character in a file
    :param n: a number
    :return: 0 if n is impossible to achieve, else return the fewest number of
    operations need to result in exactly n H
    """
    n_chars: int = 1
    n_ops: int = 0
    paste_n: int = 1

    while n_chars < n:
        if n_chars * 2 <= n:
            # Copy all and paste
            paste_n = deepcopy(n_chars)
            print(paste_n is n_chars)
            n_chars += paste_n
            n_ops += 2
        else:
            # Paste
            n_chars += paste_n
            n_ops += 1

        print("n_chars => {}".format(n_chars))

    return n_ops
