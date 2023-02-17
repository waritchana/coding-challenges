from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, start, end):
        if start > end:
            return [None]

        all_combinations = []
        # Loop through every node as i
        for i in range(start, end+1):
            # All possible left subtrees if i is choosen to be a root
            # Recursive
            left_trees = self.dfs(start, i-1)
            # All possible right subtrees if i is choosen to be a root

            right_trees = self.dfs(i+1, end)

            # Pair all combination of left and right subtrees
            # if i is choosen to be a root
            for left_tree in left_trees:
                for right_tree in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = left_tree
                    current_tree.right = right_tree
                    all_combinations.append(current_tree)
        return all_combinations


    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        all_combinations =  self.dfs(1, n)
        # Turns tree nodes into elements in lists
        # E.g. [TreeNode{ val: 3,
        #   left: TreeNode{ val: 2,
        #       left: TreeNode{ val: 1,
        #           left: None, right: None
        #       }, right: None},
        #   right: None}]
        # To [3,2,null,1]
        return all_combinations


print(Solution().generateTrees(3))
