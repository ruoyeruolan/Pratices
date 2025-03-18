// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/20 18:54
// @Description:

impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let n = nums.len();
        let mut res = Vec::with_capacity(n);

        for (idx, char) in nums.iter().enumerate() {
            let bytes = char.as_bytes()[idx];
            res.push(if bytes == b'0' { b'1' } else { b'0' });
        }

        unsafe { String::from_utf8_unchecked(res) }
    }
}
