from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        return (
            (left.val == right.val) and\
            (self.isMirror(left.left, right.right)) and\
            (self.isMirror(left.right, right.left))
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

"""
root = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(
            val=3,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=4,
            left=None,
            right=None
        )
    ),
    right=TreeNode(
        val=2,
        left=TreeNode(
            val=4,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=3,
            left=None,
            right=None
        )
    )
)
"""
root = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=None,
        right=TreeNode(
            val=3,
            left=None,
            right=None
        )
    ),
    right=TreeNode(
        val=2,
        left=None,
        right=TreeNode(
            val=3,
            left=None,
            right=None
        )
    )
)
print(Solution().isSymmetric(root))