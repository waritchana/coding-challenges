from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next # Next node to work on
            current_node.next = prev_node # Points backward
            prev_node = current_node # Current node to be pointed to in the next iteration
            current_node = next_node # Move to the following node
        # At the end, prev_node is the new head
        return prev_node


head = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=5,
                    next=None
                )
            )
        )
    )
)
new_head = Solution().reverseList(head)
print(new_head.val)
print(new_head.next.val)
print(new_head.next.next.val)
print(new_head.next.next.next.val)
print(new_head.next.next.next.next.val)
print(new_head.next.next.next.next.next)
