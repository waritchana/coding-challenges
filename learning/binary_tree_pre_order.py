# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        output_tree = []

        while stack:
            # Removes the element in LIFO
            current_node = stack.pop()
            if current_node is not None:
                output_tree.append(current_node.val)
                # Add right node first because it will get pop last
                if current_node.right is not None:
                    stack.append(current_node.right)
                if current_node.left is not None:
                    stack.append(current_node.left)
        return output_tree

    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Root first -> traverse to left subtree -> traverse to right subtree
        result = []
        if root:
            result.append(root.val)
            result.extend(self.preorderTraversal(root.left))
            result.extend(self.preorderTraversal(root.right))
        return result
    """


# This part will not work running, just to keep possible inputs for practice
root = [1, null, 2, 3]
root = []
root = [1]
preorderTraversal(root)
