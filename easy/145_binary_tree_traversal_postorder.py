from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        output_tree = []

        while stack:
            # Removes the element in LIFO
            current_node = stack.pop()
            if current_node is not None:
                output_tree.append(current_node.val)
                # Add left node first because it will get pop last
                if current_node.left is not None:
                    stack.append(current_node.left)
                if current_node.right is not None:
                    stack.append(current_node.right)
        return output_tree[::-1]


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
root = TreeNode(
    val=1,
    left=None,
    right=None
)
"""
print(Solution().postorderTraversal(root))
