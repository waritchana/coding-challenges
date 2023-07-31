from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursion
        if root is None or root.val == val:
            return root
        if val < root.val:
            root = self.searchBST(root.left, val)
        elif val > root.val:
            root = self.searchBST(root.right, val)
        return root


root = TreeNode(
    val=4,
    left=TreeNode(
        val=2,
        left=TreeNode(
            val=1,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=3,
            left=None,
            right=None
        )
    ),
    right=TreeNode(
        val=7,
        left=None,
        right=None
    )
)
#search_val = 5
search_val = 2
output = Solution().searchBST(root, search_val)
print(output.val)