"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        parent = root
        most_left = None
        current_child = None

        # Each level
        while parent:
            # Each nodes in one level
            while parent:
                if parent.left:
                    if not most_left:
                        most_left = parent.left
                    else:
                        current_child.next = parent.left
                    current_child = parent.left
                if parent.right:
                    if not most_left:
                        most_left = parent.right
                    else:
                        current_child.next = parent.right
                    current_child = parent.right
                # To next node or at the end of the level goes to null
                parent = parent.next
            # Move onto the next level
            parent = most_left
            most_left = None
            current_child = None
        return root


# This part will not work running, just to keep possible inputs for practice
#               1
#           /        \
#          2          3
#       /    \          \
#      4      5          6
root = [1,2,3,4,5,6,7]
expected_answer = [1,#,2,3,#,4,5,6,7,#]
