from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the
list's nodes (i.e., only nodes themselves may be changed.)
eg. Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # No node or has reached last node
        if not head or not head.next:
            return head
        # Nodes that will be swapped
        firstNode = head
        secondNode = head.next

        # Do the swap
        # Calling the function with head of the next pair of nodes
        # The call swaps the next two nodes and further until the most left
        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode

        # Second node becomes the new head after swapping
        return secondNode
