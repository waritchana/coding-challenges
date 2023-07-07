from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # Minus sum with current node's value until reaching leaf node
        targetSum -= root.val
        # Has reach a leaf node
        if not root.left and not root.right:
            if targetSum == 0:
                return True
            else:
                return False
        return self.hasPathSum(root.left, targetSum) or\
            self.hasPathSum(root.right, targetSum)


"""
root = TreeNode(
    val=5,
    left=TreeNode(
        val=4,
        left=TreeNode(
            val=11,
            left=TreeNode(
                val=7,
                left=None,
                right=None
            ),
            right=TreeNode(
                val=2,
                left=None,
                right=None
            )
        ),
        right=None
    ),
    right=TreeNode(
        val=8,
        left=TreeNode(
            val=13,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=4,
            left=None,
            right=TreeNode(
                val=1,
                left=None,
                right=None
            )
        )
    )
)
target_sum = 22
"""
root = TreeNode(
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
target_sum = 5
print(Solution().hasPathSum(root, target_sum))
