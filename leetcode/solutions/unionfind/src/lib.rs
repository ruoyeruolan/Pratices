// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : lib.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/20 18:10
// @Description:

mod minimumcost;

pub struct Solution;

pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

#[cfg(test)]
mod tests {
    use crate::minimumcost::MinimumCost;

    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn example() {
        let res = Solution::minimum_cost(
            5,
            &vec![(0, 1, 7), (1, 3, 7), (1, 2, 1)],
            &vec![(0, 3), (3, 4)],
        );
        assert_eq!(res, vec![1, -1]);
    }
}
