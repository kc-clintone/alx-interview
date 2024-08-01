#!/usr/bin/python3
"""
Checking the lockboxes
"""

def canUnlockAll(boxes):
    """
    Making necessary checks
    """

    n = len(boxes)
    unlocked = set([0])  # Starting with the first box unlocked
    keys = [0]  # Then start with the keys from the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in unlocked and key < n:  # We then check if the box is within range and not unlocked yet
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n
