# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/22 15:31
@Description: 
"""

from typing import Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None
        
        stack = []
        i, n = 0, len(traversal)

        while i < n:

            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            start = i
            while i < n and traversal[i].isdigit():
                i += 1
            val = int(traversal[start:i])

            node = TreeNode(val)
            
            while len(stack) > depth:
                stack.pop()
            
            if stack:
                parent = stack[-1][0]

                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            
            stack.append((node, depth))
        return stack[0][0] if stack else None

if __name__ == '__main__':

    traversal = "1-2--3---4-5--6---7"  # "1-2--3--4-5--6--7"  # "1-401--349---90--88"
    traversal.split('-')
