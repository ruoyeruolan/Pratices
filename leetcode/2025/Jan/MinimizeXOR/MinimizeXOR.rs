// @Introduce  : 
// @File       : MinimizeXOR.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/15 20:16
// @Description:

// # Given two positive integers num1 and num2, find the positive integer x such that:
// # `x` has the same number of set bits as `num2`, and
// # The value `x XOR num1` is minimal.
// # Note that `XOR` is the bitwise `XOR` operation.

// # Return the integer `x`. The test cases are generated such that `x` is uniquely determined.
// # The number of **set bits** of an integer is the number of `1`'s in its binary representation.

// # Example 1:
// # Input: num1 = 3, num2 = 5
// # Output: 3
// # Explanation:
// # The binary representations of num1 and num2 are 0011 and 0101, respectively.
// # The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
// # Example 2:

// # Input: num1 = 1, num2 = 12
// # Output: 3
// # Explanation:
// # The binary representations of num1 and num2 are 0001 and 1100, respectively.
// # The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

impl Solution {
    pub fn minimize_xor(num1: i32, num2: i32) -> i32 {
        let mut count_num1 = num1.count_ones();
        let count_num2 = num2.count_ones();
        
        let mut result = num1;
        for i in 0..32 {
            if count_num1 == count_num2 {
                break
            }

            if count_num1 > count_num2 {
                if result & (1 << i) != 0 {
                    result &= !(1 << i);
                    count_num1 -= 1;
                }
            } else {
                if result & (1 << i) == 0 {
                    result |= 1 << i;
                    count_num1 += 1;
                }
            }
        }
        result
    }
}