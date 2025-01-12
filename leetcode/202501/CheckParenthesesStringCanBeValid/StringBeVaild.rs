// @Introduce  : 
// @File       : StringBeVaild.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/12 16:12
// @Description:
// A parentheses string is a non-empty string consisting only of '(' and ')'.
// It is valid if any of the following conditions is true:

// - It is ().
// - It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
// - It can be written as (A), where A is a valid parentheses string.

// You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

// If locked[i] is '1', you cannot change s[i].But if locked[i] is '0', you can change s[i] to either '(' or ')'.
// Return true if you can make s a valid parentheses string. Otherwise, return false.

// # Example 1:
// # Input: s = "))()))", locked = "010100"
// # Output: true
// # Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
// # We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
// # Example 2:

// # Input: s = "()()", locked = "0000"
// # Output: true
// # Explanation: We do not need to make any changes because s is already valid.
// # Example 3:

// # Input: s = ")", locked = "0"
// # Output: false
// # Explanation: locked permits us to change s[0].
// # Changing s[0] to either '(' or ')' will not make s valid.


impl Solution {
    pub fn can_be_valid(s: String, locked: String) -> bool {
        let length = s.len();
        if length % 2 == 1 {return false}

        let s: Vec<char> = s.chars().collect();
        let locked: Vec<char> = locked.chars().collect();
        let mut op: Vec<usize> = Vec::new();
        let mut unlocked: Vec<usize> = Vec::new();

        for i in 0..length {
            if locked[i] == '0' {
                unlocked.push(i);
            } else if s[i] == '(' {
                op.push(i);
            } else if s[i] == ')' {
                if let Some(_) = op.pop() {} else if let Some(_) = unlocked.pop() {} else {return false}

            }
        }

        while let (Some(&op_top), Some(&unlocked_top)) = (op.last(), unlocked.last()) {
            if op_top < unlocked_top {
                op.pop();
                unlocked.pop();
            } else {
                break
            }
        }
        op.is_empty()
    }
}