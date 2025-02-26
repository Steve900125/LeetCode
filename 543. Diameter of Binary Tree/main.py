#Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def depth(root: Optional[TreeNode]):
            if root is None:
                return 0

            left_depth = depth(root.left)
            right_depth = depth(root.right)

            # 更新目前最大直徑
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            # 回傳當前節點的高度
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.max_diameter