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

        most_left = root

        # Stop at the last level
        while most_left.left:
            head = most_left
            # Go through all nodes in each level
            while head:
                # Left node to right node of the same parent
                head.left.next = head.right
                # Right node to left node of the neighbor parent
                if head.next:
                    head.right.next = head.next.left
                # Move to next node on the same level
                head = head.next
            # Move to the next level
            most_left = most_left.left
        return root


# This part will not work running, just to keep possible inputs for practice
#               1
#           /        \
#          2          3
#       /    \          \
#      4      5          6
root = [1,2,3,4,5,6,7]
expected_answer = [1,#,2,3,#,4,5,6,7,#]
