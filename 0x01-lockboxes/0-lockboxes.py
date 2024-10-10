#!/usr/bin/python3

"""unlock all locked boxes if you have the keys in the preemting box

    Returns:
       Boolean: true if all boxes are unlocked.
"""

def canUnlockAll(boxes):
    opened = set(boxes[0])
    todo = [box[0] for box in boxes if box[0] in opened]
    while todo:
        box = todo.pop()
        for neighbor in boxes[box]:
            if neighbor not in opened:
                opened.add(neighbor)
                todo.append(neighbor)
    return len(opened) == len(boxes)
