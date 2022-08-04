from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        levels = []
        while queue:
            # All nodes in current level
            nodes = len(queue)
            # Empty list to contains nodes of each level
            level = []
            for i in range(nodes):
                node = queue.popleft()
                level.append(node.val)
                # Child nodes of current levels to be in the next level queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels
