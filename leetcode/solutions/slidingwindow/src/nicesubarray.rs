// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : nicesubarray.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/18 20:02
// @Description:

use crate::Solution;

/// You are given an array `nums` consisting of **positive integers**.

/// We call a subarray of `nums` **nice** if the bitwise **AND** of every pair of elements that are in **different** positions in the subarray is equal to **0**.

/// Return the length of the longest nice subarray.

/// **A subarray is a contiguous part of an array**.

/// Note that subarrays of length 1 are always considered nice.
///
/// **Example 1**:
///
/// **Input**: nums = [1,3,8,48,10]
///
/// **Output**: 3
///
/// **Explanation**: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
///
/// - 3 AND 8 = 0.
/// - 3 AND 48 = 0.
/// - 8 AND 48 = 0.
///
/// It can be proven that no longer nice subarray can be obtained, so we return 3.
///
/// **Example 2**:
///
/// **Input**: nums = [3,1,5,11,13]
///
/// **Output**: 1
///
/// **Explanation**: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
///
/// **Constraints**:
///
/// - `1 <= nums.length <= 10^5`
///
/// - `1 <= nums[i] <= 10^9`

pub trait LongestNiceSunarray {
    fn longest_nice_sunarray(nums: Vec<i32>) -> i32;
    fn longest_nice_sunarray_iter(nums: Vec<i32>) -> i32;
}

impl LongestNiceSunarray for Solution {
    fn longest_nice_sunarray(nums: Vec<i32>) -> i32 {
        let (n, mut used, mut start, mut length) = (nums.len(), 0, 0, 0);

        for end in 0..n {
            while used & nums[end] != 0 {
                used ^= nums[start];
                start += 1;
            }
            used |= nums[end];
            length = std::cmp::max(length, end - start + 1)
        }
        length as i32
    }

    fn longest_nice_sunarray_iter(nums: Vec<i32>) -> i32 {
        let (mut used, mut start, mut length) = (0, 0, 0);

        for (end, &num) in nums.iter().enumerate() {
            while (used & num) != 0 {
                used ^= nums[start];
                start += 1;
            }
            used |= num;
            length = length.max(end - start + 1)
        }
        length as i32
    }
}
