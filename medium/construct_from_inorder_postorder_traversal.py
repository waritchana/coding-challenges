# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(inorder_left, inorder_right):
            # No node to construct subtrees
            if inorder_left > inorder_right:
                return None

            # In postorder (left -> right -> root)
            # We know the last index of input tree is root
            root = TreeNode(postorder.pop())

            # In inorder, root can be used to separate left and right subtree
            index = map_inorder[root.val]

            # Do right tree first because the next root
            # must be last index of postorder
            # left <- right <- root
            root.right = helper(index+1, inorder_right)
            root.left = helper(inorder_left, index-1)

            return root

        # Create a hash map so that we know the index of the root
        # {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i

        root = helper(0, len(inorder)-1)
        return root
