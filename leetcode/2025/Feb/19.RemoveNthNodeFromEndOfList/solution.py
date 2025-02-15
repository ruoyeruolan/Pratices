# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/15 13:27
@Description: 
"""

from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        res = ListNode(0, head)
        dummy: ListNode = res

        for _ in range(n):
            if not head:
                return None
            head = head.next
        
        while head:
            head = head.next
            
            if dummy.next:
                dummy = dummy.next
            else:
                return None
        
        if dummy.next:
            dummy.next = dummy.next.next
        return res.next
