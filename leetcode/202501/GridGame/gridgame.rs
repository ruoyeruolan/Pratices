// @Introduce  :
// @File       : gridgame.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/21 20:50
// @Description:

impl Solution {
    pub fn grid_game(grid: Vec<Vec<i32>>) -> i64 {
        use std::cmp::{max, min};
        let mut firstrowsum = grid[0].iter().map(|&x| x as i64).sum();
        let mut secondrowsum: i64 = 0;
        let mut result = i64::MAX;

        for i in 0..grid[0].len() {
            firstrowsum -= grid[0][i] as i64;
            result = min(result, max(firstrowsum, secondrowsum));
            secondrowsum += grid[1][i] as i64;
        }
        result
    }
}
