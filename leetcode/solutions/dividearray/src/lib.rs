// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : lib.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/17 18:15
// @Description:
pub struct Solution;

pub mod dividearray;

pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

#[cfg(test)]
mod tests {
    use crate::dividearray::DivideArray;

    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn example() {
        assert_eq!(
            crate::Solution::divide_array(vec![3, 2, 3, 2, 2, 2]),
            true
        );
    }
}
