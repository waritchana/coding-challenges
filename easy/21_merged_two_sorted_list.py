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
        head = ListNode(-1)
        pointer = head

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
        return head.next
