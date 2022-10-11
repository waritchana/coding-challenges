# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Root first -> traverse to left subtree -> traverse to right subtree
        result = []
        if root:
            result.extend(self.preorderTraversal(root.right))
            result.extend(self.preorderTraversal(root.left))
            result.append(root.val)
        # Opposite of pre-order
        return result[::-1]
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        output_tree = []

        while stack:
            # Removes the element in LIFO
            current_node = stack.pop()
            output_tree.append(current_node.val)
            # Add left node first because it will get pop last
            if current_node.left is not None:
                stack.append(current_node.left)
            if current_node.right is not None:
                stack.append(current_node.right)
        # Opposite of pre-order
        return output_tree[::-1]


# This part will not work running, just to keep possible inputs for practice
root = [1, null, 2, 3]
root = []
root = [1]
postorderTraversal(root)
