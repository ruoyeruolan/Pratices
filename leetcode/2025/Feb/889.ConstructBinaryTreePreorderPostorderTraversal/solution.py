# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/23 18:20
@Description: 
"""

from typing import List, Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
            self, 
            preorder: List[int], 
            postorder: List[int]
    ) -> Optional[TreeNode]:
        pass