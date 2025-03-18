// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/10 19:15
// @Description:

impl Solution {
    pub fn clear_digits(s: String) -> String {
        let mut result = Vec::new();

        for val in s.chars() {
            if val.is_ascii_digit() && !val.is_empty() {
                result.pop();
            } else {
                result.push(val);
            }
        }
        result.into_iter().collect()
    }
}
