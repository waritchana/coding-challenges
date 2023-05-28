from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # When one list runs out of node, add leftover list to the end
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        # Connect the least and next values
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        head.next = self.mergeTwoLists(list1, list2)
        return head

        """
        Recursively return head as head.next from the base case
        head = 1, list1 = 2->4, list2 = 1->3->4, head.next = 1
        head = 1, list1 = 2->4, list2 = 3->4,    head.next = 2
        head = 2, list1 = 4,    list2 = 3->4,    head.next = 3
        head = 3, list1 = 4,    list2 = 4,       head.next = 4
        head = 4, list1 = None, list2 = 4,       head.next = 4
        head = 4,
        """


Solution().mergeTwoLists([1,2,4], [1,3,4])
