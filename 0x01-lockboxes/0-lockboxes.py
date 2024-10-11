#!/usr/bin/python3
"""
This module provides functionality to determine if all the boxes in a list of
locked boxes can be opened. Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to other boxes.
Functions:
    canUnlockAll(boxes): Determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    A list of lists is given where each inner list
    represents a box and contains keys to other boxes.
    The function returns True if all boxes can be
    unlocked starting from the first box (index 0),
    otherwise it returns False.

    Parameters:
    boxes (list of list of int): A list of lists
    where each inner list contains integers representing keys.

    Returns:
    bool: True if all boxes can be unlocked,
    False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    for i in range(1, n):
        if not unlocked[i]:
            return False
    return True
