from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check head empty for an empty input case
        # Base case when head.next is null
        if not head or not head.next:
            return head
        # [1,2,3,4,5] reaching the base case where new_head is 5
        new_head = self.reverseList(head.next)
        # 4 -> 5 -> None now 4 -> 5 -> 4 pointing backward
        head.next.next = head
        # 4 -> None break the cycle
        head.next = None
        # Return 5 and its following nodes
        return new_head


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