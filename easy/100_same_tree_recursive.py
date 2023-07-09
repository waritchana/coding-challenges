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
        # Recursive
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        return (
            self.isSameTree(p.left, q.left) and\
            self.isSameTree(p.right, q.right)
        )


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
