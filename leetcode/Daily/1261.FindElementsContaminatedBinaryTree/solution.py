# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/21 16:24
@Description: 
"""

from typing import Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set()
        self.dfs(root, 0)

        # self.bfs(root)
        

    def find(self, target: int) -> bool:
        return target in self.nodes

    def dfs(self, currNode: Optional[TreeNode], currVal: int):

        if currNode is None: return

        self.nodes.add(currVal)
        self.dfs(currNode.left, currVal * 2 + 1)
        self.dfs(currNode.right, currVal * 2 + 2)
    
    def bfs(self, root: Optional[TreeNode]):

        q = [root]
        if isinstance(root, TreeNode):
            root.val = 0

        while q:
            currNode = q.pop(0)

            if isinstance(currNode, TreeNode):
                self.nodes.add(currNode.val)

                if currNode.left:
                    currNode.left.val = currNode.val * 2 + 1
                    q.append(currNode.left)
                
                if currNode.right:
                    currNode.right.val = currNode.val * 2 + 2
                    q.append(currNode.right)

