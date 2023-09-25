#!/usr/bin/python3

"""
Contains a function that returns a list of lists of integers representing the
Pascal's triangle of n
"""


def pascal_triangle(n: int):
    """
    Compute the values of the Pascal's triangle of n;
    :param n: number of values to compute
    :return: a list of lists of integers
    """
    triangle = [[0]]

    for i in range(1, n + 1):
        if i == 1:
            triangle.append([1])
        elif i == 2:
            triangle.append([1, 1])
        else:
            row = [1]
            prev_row = triangle[i - 1]

            for j in range(1, len(prev_row)):
                row.append(prev_row[j] + prev_row[j - 1])

            row.append(1)
            triangle.append(row)

    return triangle[1:]
