# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/21 19:56
@Description: 
"""

import re
from typing import Optional, List

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
    
    def inorderTraversal_(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack = []

        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            
            curr = curr.right
        return res
