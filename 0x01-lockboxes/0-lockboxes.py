#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be opened.
"""

def can_unlock_all(boxes):
    """Determine if all boxes can be opened."""
    # Start with the first box unlocked
    unlocked_boxes = {0}
    keys = set(boxes[0])

    # While we have keys that could potentially open new boxes
    while keys:
        new_keys = set()
        for key in keys:
            # If the key corresponds to a box
            if key < len(boxes) and key not in unlocked_boxes:
                # Unlock the box
                unlocked_boxes.add(key)
                # Add the keys from this box
                new_keys.update(boxes[key])
        keys = new_keys

    # If the number of unlocked boxes is equal to the total number of boxes
    # then all boxes can be opened
    return len(unlocked_boxes) == len(boxes)
