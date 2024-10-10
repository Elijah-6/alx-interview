#!/usr/bin/python3
"""
This module provides functionality to determine if all the boxes in a list of
locked boxes can be opened. Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to other boxes.
Functions:
    canUnlockAll(boxes): Determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
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
