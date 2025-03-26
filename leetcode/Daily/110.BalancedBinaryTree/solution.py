# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/25 19:22
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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) >= 0

    def Height(self, root: Optional[TreeNode]) -> int:  # 后序遍历

        if not root: return 0

        leftHeight, rightHeight = self.Height(root.left), self.Height(root.right)

        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1
        
