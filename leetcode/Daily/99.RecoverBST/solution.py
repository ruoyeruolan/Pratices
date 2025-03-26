# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/25 04:20
# @Description: 

from typing import Optional

class TreeNode:

    def __init__(self, val: float = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        x, y = None, None
        pred = TreeNode(float('-inf'))

        stack = []
        p = root

        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            
            p = stack.pop()
            
            if not x and pred.val > p.val:
                x = pred
            
            if x and pred.val > p.val:
                y = p
            
            pred = p
            p = p.right

        if x and y:
            x.val, y.val = y.val, x.val


if __name__ == '__mian__':

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(4)

    s = Solution()
    s.recoverTree(root)