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


Solution().mergeTwoLists([1,2,4], [1,3,4])
