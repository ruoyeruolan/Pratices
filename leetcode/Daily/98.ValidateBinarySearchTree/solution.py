# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/24 19:32
@Description: 
"""

from turtle import right
from typing import Optional

from click import Option
from sympy import true

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        
        if not root:
            return True
        
        if not (min_val < root.val < max_val):
            return False
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)

        