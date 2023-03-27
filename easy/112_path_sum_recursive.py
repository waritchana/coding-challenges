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
        if root is not None:
            return False

        # Minus until reaching leaf node
        targetSum -= root.val
        # Has reach leaf node
        if not root.left and not root.right:
            if targetSum == 0:
                return True
            else:
                return False
        return self.hasPathSum(root.left, targetSum) or\
            self.hasPathSum(root.right, targetSum)
