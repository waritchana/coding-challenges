from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_head = ListNode(-1)
        pointer = final_head

        # Loop until either list is empty
        while list1 or list2:
            if list1.val <= list2.val:
                # Sorted list points to a list with least value
                pointer.next = list1
                # Leftover list after one node is taken
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            # Update current pointer to the added node
            pointer = pointer.next

        # Add leftover list (if available) to sorted list
        if list1:
            pointer.next = list1
        else:
            pointer.next = list2

        # The node has already been assigned the next node
        # to when pointer has pointer.next for the first time
        return final_head.next

Solution().mergeTwoLists([1,2,4], [1,3,4])

