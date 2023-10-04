#!/usr/bin/python3
"""Contains a function that determines if all lockboxes can be opened"""


def canUnlockAll(boxes: list):
    """
    Determines if all lockboxes can be opened
    :param boxes: list of lists of numbers
    :return: if all lockboxes can be opened, true. Else, false
    """
    openable = True

    for index, box in enumerate(boxes):
        if index > 0:
            if index in box or box == []:
                continue
            else:
                openable = False
                break
    return openable
