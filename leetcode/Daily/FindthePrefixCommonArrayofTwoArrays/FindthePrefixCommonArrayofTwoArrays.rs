// @Introduce  : 
// @File       : FindthePrefixCommonArrayofTwoArrays.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/14 17:28
// @Description: leeetcode 

// # You are given two **0-indexed** integer permutations `A` and `B` of length `n`.
// # A prefix common array of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.
// # Return the **prefix common array** of `A` and `B`.
// # A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

// # Example 1:
// # Input: A = [1,3,2,4], B = [3,1,2,4]
// # Output: [0,2,3,4]
// # Explanation: At i = 0: no number is common, so C[0] = 0.
// # At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
// # At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
// # At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
// # Example 2:

// # Input: A = [2,3,1], B = [3,1,2]
// # Output: [0,1,3]
// # Explanation: At i = 0: no number is common, so C[0] = 0.
// # At i = 1: only 3 is common in A and B, so C[1] = 1.
// # At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let length = a.len();
        let mut res = vec![0; length];
        // let mut freq = vec![0; length + 1];
        let mut freq = std::collections::HashMap::new();
        let mut common_count = 0;

        for i in 0..length {
            // freq[a[i] as usize] += 1;
            let entry = freq.entry(a[i]).or_insert(0);
            *entry += 1;
            if *entry == 2 {
                common_count += 1;
            }

            // freq[b[i] as usize] += 1;
            let entry = freq.entry(b[i]).or_insert(0);
            *entry += 1;
            if *entry == 2 {
                common_count += 1;
            }
            res[i] = common_count;
        }
        res
    }
}