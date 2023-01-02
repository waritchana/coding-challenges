# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serialize_recursion(root, string):
            if root is None:
                string += "None,"
            else:
                # Travel recursively root -> left subtree -> right subtree
                string += str(root.val) + ","
                string = serialize_recursion(root.left, string)
                string = serialize_recursion(root.right, string)
            return string
        string = serialize_recursion(root, "")
        return string


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserialize_recursion(data_list):
            if data_list[0] == "None":
                data_list.pop(0)
                return None
            else:
                root = TreeNode(data_list[0])
                data_list.pop(0)
                root.left = deserialize_recursion(data_list)
                root.right = deserialize_recursion(data_list)
                return root
        data_list = data.split(",")
        root = deserialize_recursion(data_list)
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
