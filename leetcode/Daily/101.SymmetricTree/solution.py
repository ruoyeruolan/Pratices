# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/23 19:10
@Description: 
"""

from pickletools import read_uint1
from typing import Optional

from click import Option

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)
    
    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]):

        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)
