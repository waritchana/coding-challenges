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
            result.append(root.val)
            result.extend(self.preorderTraversal(root.left))
            result.extend(self.preorderTraversal(root.right))
        return result


# This part will not work running, just to keep possible inputs for practice
root = [1, null, 2, 3]
root = []
root = [1]
preorderTraversal(root)
