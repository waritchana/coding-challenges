from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None

        stack = []
        output_tree = []

        while stack or root is not None:
            # Add nodes to stack until reaching the most left node
            # of current node (root)
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            output_tree.append(root.val)
            # Go right from the node, upper level will get pop
            # next round if right is None
            root = root.right
        return output_tree


# root = [1,null,2,3]
root = TreeNode(
    val=1,
    left=None,
    right=TreeNode(
        val=2,
        left=TreeNode(
            val=3,
            left=None,
            right=None
        ),
        right=None
    )
)
"""
root = None
root = TreeNode(
    val=1,
    left=None,
    right=None
)
"""
print(Solution().inorderTraversal(root))
