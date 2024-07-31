#!/usr/bin/python3
"""
This script prints pascal's triangle for a given number
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal’s triangle
    """
    triangle = []

    if n <= 0:
        return triangle
    for i in range(n):
        tmp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                tmp_list.append(1)
            else:
                tmp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(tmp_list)
    return triangle
