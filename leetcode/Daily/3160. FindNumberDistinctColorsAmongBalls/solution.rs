// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/07 19:09
// @Description:

impl Solution {
    pub fn query_results(limit: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = Vec::new();
        let mut color_map = std::collections::HashMap::new();
        let mut ball_map = std::collections::HashMap::new();

        for query in queries {
            let ball = query[0];
            let color = query[1];

            if let Some(&pcolor) = ball_map.get(&ball) {
                if let Some(count) = color_map.get_mut(&pcolor) {
                    *count -= 1;

                    if *count == 0 {
                        color_map.remove(&pcolor);
                    }
                }
            }

            ball_map.insert(ball, color);
            *color_map.entry(color).or_insert(0) += 1;
            result.push(color_map.len() as i32)
        }
        result
    }
}
