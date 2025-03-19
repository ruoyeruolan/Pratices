// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : lib.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/18 20:00
// @Description:

pub struct Solution;

pub mod minoperationsbitarray;
pub mod nicesubarray;

pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

#[cfg(test)]
mod tests {
    use crate::nicesubarray::LongestNiceSunarray;

    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn example_longest_nice_subarray() {
        let res = Solution::longest_nice_sunarray(vec![1, 3, 8, 48, 10]);
        assert_eq!(res, 3);
    }
}
