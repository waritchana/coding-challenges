from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursion
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            # Plus one to include top of the tree
            return 1 + max(left_height, right_height)


root = TreeNode(
    val=3,
    left=TreeNode(
        val=9,
        left=None,
        right=None
    ),
    right=TreeNode(
        val=20,
        left=TreeNode(
            val=15,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=7,
            left=None,
            right=None
        )
    )
)
print(Solution().maxDepth(root))