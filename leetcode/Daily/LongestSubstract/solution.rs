// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/03 17:13
// @Description:

impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let (mut incrLen, mut descLen, mut maxLen) = (1, 1, 1);

        for idx in 0..(nums.len() - 1) {
            if nums[idx + 1] > nums[idx] {
                incrLen += 1;
                descLen = 1;
            } else if nums[idx + 1] < nums[idx] {
                descLen += 1;
                incrLen = 1;
            } else {
                incrLen = 1;
                descLen = 1;
            }

            // maxLen = std::cmp::max(maxLen, std::cmp::max(incrLen, descLen));
            maxLen = match (incrLen, descLen, maxLen) {
                (a, b, c) if a >= b && a >= c => a,
                (a, b, c) if b >= a && b >= c => b,
                (_, _, c) => c,
            };
        }
        maxLen
    }
}
