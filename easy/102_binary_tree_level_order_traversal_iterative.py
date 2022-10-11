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
        if root is None:
            return []

        queue = deque([root])
        levels = []

        while queue:
            # Empty list to contains nodes of each level
            level = []
            # How many nodes in current level
            count_nodes = len(queue)
            for i in range(count_nodes):
                node = queue.popleft()
                level.append(node.val)
                # Child nodes of current levels to be in the next level queue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            levels.append(level)
        return levels
