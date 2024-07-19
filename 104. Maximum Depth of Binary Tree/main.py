# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        else:
            if root.left != None:
                left_height = 1 + self.maxDepth(root.left)
            else:
                left_height = 1
            
            if root.right != None:
                right_height = 1 + self.maxDepth(root.right)
            else:
                right_height  = 1
        
        if left_height > right_height:
            return left_height
        else :
            return right_height
         