#!/usr/bin/python3
"""Contains a function that determines if all lockboxes can be opened"""


def canUnlockAll(boxes: list) -> bool:
    """
    Determines if all lockboxes can be opened
    :param boxes: list of lists of numbers
    :return: if all lockboxes can be opened, true. Else, false
    """
    if len(boxes) == 0:
        return False
    elif len(boxes) == 1:
        return True

    available_keys: list = []
    for index, box in enumerate(boxes):
        for key in box:
            if key not in available_keys:
                available_keys.append(key)

        if index >= 1 and index not in available_keys:
            return False

    return True
