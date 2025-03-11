// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/11 20:02
// @Description:

impl Solution {
    fn count_of_substrings(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        let (mut count, mut start, mut end) = (0, 0, 0);
        let mut freq = vec![0; 3];

        while end < n {
            freq[(s[end] - b'a') as usize] += 1;

            while freq[0] > 0 && freq[1] > 0 && freq[2] > 0 {
                count += (n - end) as i32;

                freq[(s[start] - b'a') as usize] -= 1;
                start += 1;
            }
            end += 1;
        }
        count
    }
}
