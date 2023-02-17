from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        for curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node # Points backward
            prev_node = curr_node
            curr_node = next_node
        head = prev_node # new head is the last item of original node
        return head
