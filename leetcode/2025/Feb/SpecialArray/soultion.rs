// @Introduce  :
// @File       : soultion.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/01 15:59
// @Description:

impl Solution {
    pub fn is_array_special(nums: Vec<i32>) -> bool {
        for i in 0..(nums.len() - 1) {
            if (nums[i] & 1) ^ (nums[i + 1] & 1) == 0 {
                return false;
            }
        }
        true
    }

    pub fn is_array_special_(nums: Vec<i32>) -> bool {
        for i in 0..(nums.len() - 1) {
            if nums[i] % 2 == nums[i + 1] % 2 {
                return false;
            }
        }
        true
    }
}
