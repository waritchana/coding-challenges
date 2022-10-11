# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root):
        if root is None:
            return 0, True

        left_count, left_is_uni = self.helper(root.left)
        right_count, right_is_uni = self.helper(root.right)

        if left_is_uni and right_is_uni:
            # Has left child but value is not the same as root - not uni
            if root.left is not None and root.left.val != root.val:
                return left_count + right_count, False
            # Has right child but value is not the same as root - not uni
            elif root.right is not None and root.right.val != root.val:
                return left_count + right_count, False
            # Has either left or right child's value is the same as root,
            #   other empty - is uni
            # Has no children - is uni
            # Has two children same value as root - is uni
            else:
                return 1 + left_count + right_count, True
        else:
            # One or two children value not same as root - not uni
            return left_count + right_count, False


    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count_all, _ = self.helper(root)
        return count_all

# This part will not work running, just to keep possible inputs for practice
#               5
#           /        \
#          1          5
#       /    \          \
#      5      5           5
root = [5,1,5,5,5,null,5]
