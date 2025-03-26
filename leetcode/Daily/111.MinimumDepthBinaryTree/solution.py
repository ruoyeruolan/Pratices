# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/25 19:40
# @Description: 

from typing import Optional


class TreeNode:

    def __init__(
            self, 
            val: float = 0, 
            left: Optional['TreeNode'] = None, 
            right: Optional['TreeNode'] = None
    ) -> None:
        
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.getDepth(root)

    def getDepth(self, root:Optional[TreeNode]) -> int:

        if not root: return 0

        if root.left is None or root.right is None:
            return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

        return min(self.getDepth(root.left), self.getDepth(root.right)) + 1

