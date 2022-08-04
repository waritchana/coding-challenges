from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def setupLevels (self, root, level, levels):
        # Initiate new level
        if len(levels) == level:
            levels.append([])
        levels[level].append(root.val)
        # Recursively add new levels and update levels
        if root.left:
            self.setupLevels(root.left, level+1, levels)
        if root.right:
            self.setupLevels(root.right, level+1, levels)
        return levels

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        return self.setupLevels(root, 0, [])
