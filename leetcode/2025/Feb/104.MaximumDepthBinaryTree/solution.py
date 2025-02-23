# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/23 19:36
@Description: 
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.isVaild(root, depth=0)
        
    def isVaild(self, root: Optional[TreeNode], depth: int):

        if not root:
            return depth 
         
        return max(self.isVaild(root.left, depth + 1), self.isVaild(root.right, depth + 1))

