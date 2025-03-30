// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : partionlabels.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/30 16:24
// @Description:

use crate::Solution;

pub trait PartitionLabels {
    fn partition_labels(s: String) -> Vec<i32>;
    fn partition_labels_(s: String) -> Vec<i32>;
}

impl PartitionLabels for Solution {
    fn partition_labels(s: String) -> Vec<i32> {
        let mut index4last = std::collections::HashMap::new();
        let (mut res, mut start, mut end) = (Vec::new(), 0, 0);

        for (idx, val) in s.chars().enumerate() {
            index4last.insert(val, idx);
        }

        for (idx, val) in s.chars().enumerate() {
            end = end.max(*index4last.get(&val).unwrap_or(&0));

            if idx == end {
                res.push((idx - start + 1) as i32);
                start = idx + 1;
            }
        }
        res
    }

    fn partition_labels_(s: String) -> Vec<i32> {
        let index4last: std::collections::HashMap<char, usize> =
            s.chars().enumerate().map(|(idx, val)| (val, idx)).collect();

        let (res, _, _) =
            s.chars()
                .enumerate()
                .fold((Vec::new(), 0, 0), |(mut res, start, end), (idx, val)| {
                    let new_end = end.max(*index4last.get(&val).unwrap());

                    if idx == new_end {
                        res.push((idx - start + 1) as i32);
                        (res, idx + 1, new_end)
                    } else {
                        (res, start, new_end)
                    }
                });
        res
    }
}
