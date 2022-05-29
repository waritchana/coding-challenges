from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if (not head) or (not head.next):
            return head
        # Reach base case where head = 4 and head.next = 5
        # reversed_list is 5
        reversed_list = reverseList(head.next)
        # 4 -> 5 -> 4 cyclic linked list
        head.next.next = head
        # 5 -> 4 -> None
        head.next = None
        # Return 5 and its following nodes
        return reversed_list
