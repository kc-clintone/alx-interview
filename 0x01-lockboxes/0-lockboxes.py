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

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Should return True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Should return True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Should return False

