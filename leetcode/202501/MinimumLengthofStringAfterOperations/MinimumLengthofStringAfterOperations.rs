// @Introduce  : 
// @File       : MinimumLengthofStringAfterOperations.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/01/13 22:38
// @Description:

impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        use std::collections::HashSet;

        let mut res = 0;
        let unique_chars: HashSet<_> = s.chars().collect();

        for &c in &unique_chars {
            let count = s.chars().filter(|&x| x == c).count();
            if count % 2 == 1 {
                res += 1;
            } else {
                res += 2;
            }
        }
        res
    }

    pub fn minimum_length_(s: String) -> i32 {
        let length = s.len() as i32;
        let mut length2Subtraction = 0;
        let mut freq = vec![0; 26];

        for c in s.chars() {freq[(c as u8 - b'a') as usize] += 1;}
        
        for frequency in freq {
            if frequency % 2 != 0 {
                removable_len += frequency - 1;
            } else if frequency != 0 {
                removable_len += frequency - 2;
            }
        }
        
        length - removable_len
    }
}