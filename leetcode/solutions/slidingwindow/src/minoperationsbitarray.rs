// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : minoperationsbitarray.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/19 17:37
// @Description:

/// You are given a **binary array** `nums`.
///
/// You can do the following operation on the array any number of times (possibly zero):
///
/// - Choose any `3` consecutive elements from the array and flip all of them.
///
/// **Flipping** an element means changing its value from `0` to `1`, and from `1` to `0`.
///
/// Return the **minimum number of operations** required to make all elements in `nums` equal to `1`. If it is impossible, return `-1`.
///
/// **Example 1**:
///
/// **Input**: nums = [0,1,1,1,0,0]
///
/// **Output**: 3
///
/// **Explanation**:
///
/// We can do the following operations:
///
/// Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
/// Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
/// Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
///
/// **Example 2**:
///
/// **Input**: nums = [0,1,1,1]
///
/// **Output**: -1
///
/// **Explanation**:
///
/// It is impossible to make all elements equal to 1.
///
/// **Constraints**:
///
/// - `3 <= nums.length <= 10^5`
/// - `0 <= nums[i] <= 1`
///
use crate::Solution;

pub trait MinimumOperations {
    fn minoperationsbitarray(nums: Vec<i32>) -> i32;
    fn minoperationsbitarray_(nums: Vec<i32>) -> i32;
}

impl MinimumOperations for Solution {
    fn minoperationsbitarray(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        let n = nums.len();
        let mut count = 0;

        for idx in 0..(n - 2) {
            if nums[idx] == 0 {
                nums[idx] = 1;
                nums[idx + 1] ^= 1;
                nums[idx + 2] ^= 1;

                count += 1
            }
        }

        if nums[n - 2] == 0 || nums[n - 1] == 0 {
            return -1;
        }
        count
    }

    fn minoperationsbitarray_(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        let (n, mut count) = (nums.len(), 0);

        for idx in 0..(n - 2) {
            if nums[idx] == 0 {
                nums[idx] = 1;
                nums[idx + 1] ^= 1;
                nums[idx + 2] ^= 1;

                count += 1;
            }
        }

        if nums.iter().sum::<i32>() as usize == n {
            return count;
        }
        -1
    }
}
