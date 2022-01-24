# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Root first -> traverse to left subtree -> traverse to right subtree
        result = []
        if root:
            stack = [root]
        else:
            stack = []
        while len(stack) >= 1:
            current_root = stack.pop()
            result.append(current_root.val)
            # Add left node to the stack last so it gets pop first
            if current_root.right:
                stack.append(current_root.right)
            if current_root.left:
                stack.append(current_root.left)
        return result


# This part will not work running, just to keep possible inputs for practice
root = [1, null, 2, 3]
root = []
root = [1]
preorderTraversal(root)
