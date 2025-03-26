# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/26 17:34
# @Description: 

from typing import Optional

class TreeNode:

    def __init__(self, val:float=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None) -> None:
        
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def __init__(self) -> None:

        self.pred = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root: return

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.pred
        root.left = None

        self.pred = root
    
    def flatten_(self, root:Optional[TreeNode]) -> None:

        stack = []
        while root or stack:

            if root and root.right:
                stack.append(root.right)

            if root and root.left:
                root.right = root.left
                root.left = None

            elif stack and root:
                root.right = stack.pop()
            
            root = root.right if root else None


def create_binary_tree(values):
    if not values or values[0] is None:
        return None
        
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
            
    return root


if __name__ == '__main__':

    root = create_binary_tree([1,2,5,3,4,None,6])
    s = Solution()
    s.flatten_(root)