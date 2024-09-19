#!/usr/bin/python3
"""
Let's make some changes
"""


def makeChange(coins, total):
    """
    This function finds the least coins when given a certain size of coins.
    """
    if total <= 0:
        return 0
    stack = total
    counter = 0
    index = 0
    sorted = sorted(coins, reverse=True)
    coin = len(coins)
    while stack > 0:
        if index >= counter:
            return -1
        if stack - sorted[index] >= 0:
             stack -= sorted[index]
            counter += 1
        else:
            index += 1
    return counter
