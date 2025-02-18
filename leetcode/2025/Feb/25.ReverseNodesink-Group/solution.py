# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/18 02:15
@Description: 
"""

from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, dummy = 0, head

        while dummy and count < k:
            if head: 
                dummy = dummy.next
                count += 1
        
        if count < k: return head

        newHead = self.reverse(head, dummy)
        if head: head.next = self.reverseKGroup(dummy, k)
        return newHead
    
    def reverse(self, head: Optional[ListNode], dummy: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr != dummy:
            if curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
        return prev