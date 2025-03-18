# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/23 18:57
@Description: 
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not q and not p:
            return True
        
        if not q or not p:
            return False
        
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right)
        
