from collections import deque
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative - queue
        queue = deque()
        queue.append((p, q))

        while queue:
            p, q = queue.popleft()

            if not p and not q:
                continue # Prevent from appending since they are empty
            if (not p or not q) or (p.val != q.val):
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
        return True


p = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=None,
        right=None
    ),
    right=TreeNode(
        val=3,
        left=None,
        right=None
    )
)
q = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=None,
        right=None
    ),
    right=TreeNode(
        val=3,
        left=None,
        right=None
    )
)
print(Solution().isSameTree(p, q))
