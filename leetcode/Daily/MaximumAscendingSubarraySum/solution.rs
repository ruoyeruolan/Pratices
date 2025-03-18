// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/04 20:13
// @Description:

impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let mut maxSum = nums[0];
        let mut cSum = nums[0];

        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                cSum += nums[i]
            } else {
                maxSum = std::cmp::max(maxSum, cSum);
                cSum = nums[i]
            }
        }
        std::cmp::max(maxSum, cSum)
    }
}
