// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/02 15:54
// @Description:

impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let n = nums.len();

        if n <= 1 {
            return true;
        }

        let mut count = 0;
        for idx in 1..n {
            if nums[idx] < nums[idx - 1] {
                count += 1;
            }
        }

        if nums[0] < nums[n - 1] {
            count += 1;
        }

        count <= 1
    }
}
