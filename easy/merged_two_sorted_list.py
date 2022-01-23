# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists_recursion(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Either list has reached the end, add the rest of items in the other list
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

    def mergeTwoLists_iteration(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Have a dummy node to points at empty location
        dummy = ListNode(-1)
        prev = dummy

        # Loop until either list ends
        while list1 and list2:
            # Set the pointer to the smallest value
            # Update the list to have remaining nodes
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            # Now prev is the newly pointed node
            prev = prev.next

        # Either list has reached the end, add the rest of items in the other list
        if list1 is None:
            prev.next = list2
        else:
            prev.next = list1

        # dummy node points to sorted list
        return dummy.next
