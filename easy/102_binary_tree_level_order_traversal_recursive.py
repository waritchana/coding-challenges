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
        if not root:
            return []
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
        return self.setupLevels(root, 0, [])


root = TreeNode(
    val=3,
    left=TreeNode(
        val=9,
        left=None,
        right=None
    ),
    right=TreeNode(
        val=20,
        left=TreeNode(
            val=15,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=7,
            left=None,
            right=None
        )
    )
)
print(Solution().levelOrder(root))
