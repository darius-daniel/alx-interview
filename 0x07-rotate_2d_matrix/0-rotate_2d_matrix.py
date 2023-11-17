#!/usr/bin/python3
""" 0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix) -> None:
    """ Rotates an n x n matrix 90 degrees clockwise in place
    """
    if matrix and [] not in matrix:
        for r_idx in range(len(matrix)):

            for c_idx in range(r_idx, len(matrix[r_idx])):
                matrix[r_idx][c_idx], matrix[c_idx][r_idx] = (
                    matrix[c_idx][r_idx], matrix[r_idx][c_idx]
                )

            matrix[r_idx].reverse()
