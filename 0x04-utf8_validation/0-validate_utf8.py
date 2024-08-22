#!/usr/bin/python3
"""
UTF-8 validation kodule
"""


def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding.

    Parameters:
    data (list of int):
        A list of integers where each integer represents one byte of data.
        Each integer should be in the range 0-255, corresponding to
        an 8-bit byte.

    Returns:
    bool: True if the dataset is a valid UTF-8 encoding, False otherwise.
    """

    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 | mask2)) == mask1:
                return False
            elif (byte & (mask1 | mask2 | (1 << 5))) == (mask1 | mask2):
                num_bytes = 2
            elif (byte & (mask1 | mask2 | (1 << 5) |
                  (1 << 4))) == (mask1 | mask2 | (1 << 5)):
                num_bytes = 3
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4) |
                  (1 << 3))) == (mask1 | mask2 | (1 << 5) | (1 << 4)):
                num_bytes = 4
            else:
                return False
        else:
            if (byte & (mask1 | mask2)) != mask1:
                return False
            num_bytes -= 1

    return num_bytes == 0
