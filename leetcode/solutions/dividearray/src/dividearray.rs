// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : dividearray.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/17 18:18
// @Description: 2206

use crate::Solution;

pub trait DivideArray {
    fn divide_array(nums: Vec<i32>) -> bool;
}

impl DivideArray for Solution {
    fn divide_array(nums: Vec<i32>) -> bool {
        let mut freq = std::collections::HashMap::new();

        nums.iter()
            .for_each(|&num| *freq.entry(num).or_insert(0) += 1);

        freq.values().all(|&count| count % 2 == 0)
    }
}
