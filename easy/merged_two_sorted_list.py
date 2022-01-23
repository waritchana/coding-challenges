# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Either list has reached the end, add the rest of items in the other list.
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        # Set the pointer to the smaller head
        # Current node is now the newly pointed value
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    self.mergeTwoLists([1,2,4], [1,3,4])
