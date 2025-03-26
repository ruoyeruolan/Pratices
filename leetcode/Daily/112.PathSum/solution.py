# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/25 20:05
# @Description: 


from typing import Optional, List

class TreeNode:

    def __init__(
            self, 
            val: int = 0, 
            left: Optional['TreeNode'] = None, 
            right: Optional['TreeNode'] = None
    ) -> None:
        
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(root: Optional[TreeNode], path: list, target: int):

            if not root:
                return

            if not root.left and not root.right and target == root.val:
                res.append(path + [root.val])
                return
            
            dfs(root.left, path + [root.val], target - root.val)
            dfs(root.right, path + [root.val], target - root.val)
        dfs(root, [], targetSum)
        return res
        

