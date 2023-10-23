#!/usr/bin/python3
""" 0. UTF-8 Validation. """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: The given data set
    :return: True if it represent a valid UTF-8 encoding, False if not.
    """
    i = 0
    while i < len(data):
        # Check the number of bytes in the current character
        byte = data[i]
        if byte & 0b10000000 == 0:
            # 1-byte character
            i += 1
        elif byte & 0b11100000 == 0b11000000:
            # 2-byte character
            i += 1
            if i >= len(data) or (data[i] & 0b11000000 != 0b10000000):
                return False
        elif byte & 0b11110000 == 0b11100000:
            # 3-byte character
            i += 1
            for j in range(2):
                if i >= len(data) or (data[i] & 0b11000000 != 0b10000000):
                    return False
                i += 1
        elif byte & 0b11111000 == 0b11110000:
            # 4-byte character
            i += 1
            for j in range(3):
                if i >= len(data) or (data[i] & 0b11000000 != 0b10000000):
                    return False
                i += 1
        else:
            # Invalid UTF-8 start byte
            return False

    return True
