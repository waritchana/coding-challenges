from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        while pointer and pointer.next:
            # Skip the next node if it duplicates
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            # Moves to the next node if not duplicates
            else:
                pointer = pointer.next
        return head


head = [1,1,2,3,3]
#head = [1,1,2]
Solution().deleteDuplicates(head)
