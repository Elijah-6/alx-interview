#!/usr/bin/python3
"""Generates the pascal triangle up to n rows
"""
def pascal_triangle(n):
    """Generates the pascal triangle up to n rows

    Args:
        n (int): number of rows

    Returns:
        array: pascal triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
