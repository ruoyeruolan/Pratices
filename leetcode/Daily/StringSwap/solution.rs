// @Introduce  :
// @File       : solution.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/02/05 17:25
// @Description:

impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let s1 = s1.chars().collect();
        let s2 = s2.chars().collect();
        let (mut misMatch, mut idx1, mut idx2) = (0, 0, 0);
        for idx in 0..s1.len() {
            if s1[idx] != s2[idx] {
                misMatch += 1;

                if misMatch > 2 {
                    return false;
                } else if misMatch == 1 {
                    idx1 = idx;
                } else {
                    idx2 = idx;
                }
            }
        }
        s1[idx1] == s2[idx2] && s1[idx2] == s2[idx1]
    }
}
