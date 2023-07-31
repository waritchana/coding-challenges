from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # To reserve to be the head of the final result
        head = ListNode(-1)
        # Moves as merging the list
        pointer = head
        # Work on each nodes until either list is empty
        while list1 and list2:
            if list1.val <= list2.val:
                # Sorted list points to a list with least value
                pointer.next = list1
                # Leftover list after one node is taken
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        # Either list is done, add remaining
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2
        # The node has already been assigned the next node
        # to when pointer has pointer.next for the first time
        return head.next

list1 = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=4,
            next=None
        )
    )
)
list2 = ListNode(
    val=1,
    next=ListNode(
        val=3,
        next=ListNode(
            val=4,
            next=None
        )
    )
)
head = Solution().mergeTwoLists(list1, list2)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)
print(head.next.next.next.next.val)
print(head.next.next.next.next.next.val)
