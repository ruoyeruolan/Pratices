# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/17 20:22
@Description: 
"""

from typing import Optional

from sklearn import dummy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        dummy = head.next.next
        newHead = head.next
        newHead.next = head

        newHead.next.next = self.swapPairs(dummy)
        return newHead

