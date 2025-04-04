# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/04 17:16
# @Description: 

from typing import Optional

class TreeNode:

    def __init__(
            self, 
            val: int = 0, 
            left: Optional['TreeNode'] = None, 
            right: Optional['TreeNode'] = None
    ):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def lcaDeepestLeaves(
            self, 
            root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        
        def dfs(root: Optional[TreeNode]):

            if not root:
                return 0, None
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root
        return dfs(root=root)[1]


def create_binary_tree(values) -> Optional[TreeNode]:
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
    
    root = [3,5,1,6,2,0,8,None,None,7,4]
    root_ = create_binary_tree(root)

    s = Solution()
    s.lcaDeepestLeaves(root_)