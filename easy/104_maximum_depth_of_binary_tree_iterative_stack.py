# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative - stack
        max_height = 0
        # Initiate stack with the first node and its height
        stack = [(root, 1)]
        while stack:
            root, root_height = stack.pop()
            # Skip root.left and root.right added that is actually None
            if root:
                max_height = max(root_height, max_height)
                stack.append((root.left, root_height+1))
                stack.append((root.right, root_height+1))
        return max_height
