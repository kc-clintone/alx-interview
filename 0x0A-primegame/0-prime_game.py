#!/usr/bin/python3
"""
Prime game - interview practic
https://www.github.com/kc-clintone
"""


def isWinner(x, nums):
    """
    This function determines the  winner of a prime game session with `x` rounds
    """
    if x < 1 or not nums:
        return None
    maria, ben = 0, 0
    number = max(nums)
    prime_nums = [True for _ in range(1, number + 1, 1)]
    prime_nums[0] = False
    for index, is_prime in enumerate(prime_nums, 1):
        if index == 1 or not is_prime:
            continue
        for j in range(index + index, number + 1, index):
            prime_nums[j - 1] = False
    for _, number in zip(range(x), nums):
        prime_counter = len(list(filter(lambda x: x, prime_nums[0: number])))
        ben += prime_counter % 2 == 0
        maria += prime_counter % 2 == 1
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
