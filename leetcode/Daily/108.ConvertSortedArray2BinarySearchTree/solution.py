# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/24 19:08
@Description: 
"""

from typing import List, Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        return self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums: List[int], start: int, end: int) -> Optional[TreeNode]:

        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])

        root.left = self.buildTree(nums, start, mid - 1)
        root.right = self.buildTree(nums, mid + 1, end)
        return root