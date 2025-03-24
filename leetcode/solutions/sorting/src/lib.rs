// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : lib.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/24 18:19
// @Description:

pub struct Solution;

mod freedays;

pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

#[cfg(test)]
mod tests {
    use crate::freedays::CountDays;

    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn it_works_example() {
        assert_eq!(
            Solution::count_days(10, vec![vec![5, 7], vec![1, 3], vec![9, 10]]),
            2
        );
    }
}
