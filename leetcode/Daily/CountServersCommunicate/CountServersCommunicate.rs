// @Introduce  :
// @File       : CountServersCommunicate.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/23 19:12
// @Description:

impl Solution {
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
        let mut count = 0;
        let num_rows = grid.len();
        for row in 0..num_rows {
            let row_sum: i32 = grid[row].iter().sum();

            if row_sum > 1 {
                count += row_sum;
            } else if row_sum == 1 {
                let col = grid[row].iter().position(|&x| x == 1).unwrap();
                let col_sum: i32 = (0..num_rows).map(|i| grid[i][col]).sum();
                if col_sum > 1 {
                    count += 1;
                }
            }
        }

        count
    }
}
