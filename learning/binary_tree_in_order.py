# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


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

    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Left subtree -> root -> traverse to right subtree
        result = []
        if root:
            result.extend(self.inorderTraversal(root.left))
            result.append(root.val)
            result.extend(self.inorderTraversal(root.right))
        return result
    """


# This part will not work running, just to keep possible inputs for practice
root = [1, null, 2, 3]
root = []
root = [1]
preorderTraversal(root)
