# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : StringBeValid.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/12 13:51
@Description: 
A parentheses string is a non-empty string consisting only of '(' and ')'. 
It is valid if any of the following conditions is true:

- It is ().
- It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.
"""

# Example 1:
# Input: s = "))()))", locked = "010100"
# Output: true
# Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
# We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
# Example 2:

# Input: s = "()()", locked = "0000"
# Output: true
# Explanation: We do not need to make any changes because s is already valid.
# Example 3:

# Input: s = ")", locked = "0"
# Output: false
# Explanation: locked permits us to change s[0]. 
# Changing s[0] to either '(' or ')' will not make s valid.


class Solution:

    def canBeVaild(self, s: str, locked: str) -> bool:
        length = len(s)
        if length % 2 == 1:
            return False
        
        op = []
        unlocked = []
        for i in range(length):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                op.append(i)
            elif s[i] == ')':
                if op:
                    op.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
                    
        while op and unlocked and op[-1] < unlocked[-1]:
            op.pop()
            unlocked.pop()
        if op:
            return False
        return True
    
    def canBeBaild_(self, s: str, locked: str) -> bool:

        length = len(s)

        if length % 2 == 1:
            return False
        
        op, unlocked = 0, 0
        for i in range(length):

            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                op += 1
            elif s[i] == ')':
                if op > 0:
                    op -= 1
                elif unlocked > 0:
                    unlocked -= 1
                else:
                    return False
        
        balance = 0
        for i in range(length - 1, -1, -1):

            if locked[i] == '0':
                balance -= 1
                unlocked -= 1
            elif s[i] == '(':
                balance += 1
                op -= 1
            elif s[i] == ')':
                balance -= 1
            
            if balance > 0:
                return False
            
            if op == 0 and unlocked == 0:
                break

        if op > 0:
            return False
        return True
    
    def canBeVaild__(self, s: str, locked: str) -> bool:
        
        length = len(s)
        if length&1 == 1: return False

        bMin, bMax = 0, 0
        for ind, val in enumerate(s):

            op = val == '('
            unlocked = locked[ind] == '0'

            if (not op) or unlocked:
                bMin -= 1
            else:
                bMin += 1
            
            if op or unlocked:
                bMax += 1
            else:
                bMax -= 1
            
            if bMax < 0: return False
            bMin = max(bMin, 0)
        return bMin == 0
        