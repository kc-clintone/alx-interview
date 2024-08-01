#!/usr/bin/python3
"""
Checking the lockboxes
"""


def canUnlockAll(boxes):
    """
    Making necessary checks
    """

    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n
