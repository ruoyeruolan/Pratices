// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/15 19:16
// @Description:

impl Solution {
    fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        let houses = nums.len();
        let (mut min_, mut max_) = (1, *nums.iter().max().unwrap());

        while min_ < max_ {
            let mid = (min_ + max_) / 2;
            let mut house_stealed = 0;

            let mut idx = 0;
            while idx < houses {
                if nums[idx] <= mid {
                    house_stealed += 1;
                    idx += 2;
                } else {
                    idx += 1;
                }
            }

            if house_stealed >= k {
                max_ = mid;
            } else {
                min_ = mid + 1;
            }
        }
        min_
    }
}
